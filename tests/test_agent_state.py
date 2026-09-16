import json
import subprocess
import sys

import pytest

from labs.lab03_tool_calling.tools import ToolRegistry
from labs.lab04_agent_state.agent import Agent, SimulatedCrash


def make_agent(tmp_path):
    tools = ToolRegistry(tmp_path / "tools.sqlite")
    return Agent(tmp_path / "state.sqlite", tools), tools


def call():
    return {
        "tool": "create_issue",
        "arguments": {"title": "Billing", "body": "Review"},
        "operation_id": "issue-1",
    }


def test_resume_in_new_process_after_write_before_checkpoint(tmp_path):
    agent, tools = make_agent(tmp_path)
    agent.create("task", [call()])
    assert agent.run("task")["status"] == "waiting_approval"
    tools.approve(call())
    with pytest.raises(SimulatedCrash):
        agent.run("task", crash_after_write=True)
    assert tools.issue_count() == 1
    assert agent.load("task")["index"] == 0
    code = """
import json, sys
from pathlib import Path
from labs.lab03_tool_calling.tools import ToolRegistry
from labs.lab04_agent_state.agent import Agent
root = Path(sys.argv[1])
tools = ToolRegistry(root / "tools.sqlite")
agent = Agent(root / "state.sqlite", tools)
print(json.dumps({"state": agent.run("task"), "count": tools.issue_count()}))
"""
    result = subprocess.run(
        [sys.executable, "-c", code, str(tmp_path)], capture_output=True, text=True, check=True
    )
    data = json.loads(result.stdout)
    assert data["state"]["status"] == "completed"
    assert data["state"]["attempts"] == 3
    assert data["count"] == 1
    assert len(data["state"]["results"]) == 1


def test_budget_survives_restart(tmp_path):
    agent, tools = make_agent(tmp_path)
    agent.create("task", [call()], max_steps=1)
    assert agent.run("task")["status"] == "waiting_approval"
    restarted, _ = make_agent(tmp_path)
    state = restarted.run("task")
    assert state["status"] == "budget_exhausted"
    assert state["attempts"] == 1
    assert tools.issue_count() == 0


def test_cancelled_task_does_not_execute(tmp_path):
    agent, tools = make_agent(tmp_path)
    agent.create("task", [call()])
    agent.cancel("task")
    tools.approve(call())
    assert agent.run("task")["status"] == "cancelled"
    assert tools.issue_count() == 0


def test_completed_task_is_not_replayed(tmp_path):
    agent, tools = make_agent(tmp_path)
    agent.create("task", [call()])
    tools.approve(call())
    first = agent.run("task")
    assert agent.run("task") == first
    assert tools.issue_count() == 1


def test_conflicting_operation_fails_task(tmp_path):
    agent, tools = make_agent(tmp_path)
    changed = call()
    changed["arguments"]["body"] = "Different"
    agent.create("task", [call(), changed])
    tools.approve(call())
    tools.approve(changed)
    state = agent.run("task")
    assert state["status"] == "failed"
    assert tools.issue_count() == 1
