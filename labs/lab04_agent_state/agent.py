"""A scripted planner drives a bounded loop; checkpoints contain durable task state."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from pydantic import ValidationError

from labs.lab03_tool_calling.tools import ApprovalRequired, BoundaryError, ToolRegistry


class SimulatedCrash(RuntimeError):
    pass


class Agent:
    def __init__(self, checkpoint: Path, tools: ToolRegistry):
        self.checkpoint = checkpoint
        self.tools = tools
        with sqlite3.connect(checkpoint) as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS tasks (id TEXT PRIMARY KEY, state TEXT NOT NULL)"
            )

    def create(self, task_id: str, plan: list[dict], max_steps: int = 5) -> None:
        if max_steps < 1:
            raise ValueError("max_steps must be positive")
        for call in plan:
            self.tools.validate(call)
        state = {
            "plan": plan,
            "index": 0,
            "attempts": 0,
            "max_steps": max_steps,
            "status": "ready",
            "results": [],
            "error": None,
        }
        with sqlite3.connect(self.checkpoint) as db:
            db.execute("INSERT INTO tasks VALUES (?, ?)", (task_id, json.dumps(state)))

    def load(self, task_id: str) -> dict:
        with sqlite3.connect(self.checkpoint) as db:
            row = db.execute("SELECT state FROM tasks WHERE id = ?", (task_id,)).fetchone()
        if row is None:
            raise KeyError(task_id)
        return json.loads(row[0])

    def save(self, task_id: str, state: dict) -> None:
        with sqlite3.connect(self.checkpoint) as db:
            db.execute("UPDATE tasks SET state = ? WHERE id = ?", (json.dumps(state), task_id))

    def cancel(self, task_id: str) -> dict:
        state = self.load(task_id)
        if state["status"] not in {"completed", "failed", "budget_exhausted"}:
            state["status"] = "cancelled"
            self.save(task_id, state)
        return state

    def run(self, task_id: str, crash_after_write: bool = False) -> dict:
        state = self.load(task_id)
        if state["status"] in {"completed", "failed", "cancelled", "budget_exhausted"}:
            return state
        while state["index"] < len(state["plan"]):
            if state["attempts"] >= state["max_steps"]:
                state["status"] = "budget_exhausted"
                break
            call = state["plan"][state["index"]]
            # Charge attempts before execution so a crash cannot reset the budget.
            state["attempts"] += 1
            state["status"] = "running"
            self.save(task_id, state)
            try:
                result = self.tools.execute(call)
            except ApprovalRequired as error:
                state.update(status="waiting_approval", error=str(error))
                break
            except (BoundaryError, ValidationError) as error:
                state.update(status="failed", error=str(error))
                break
            if crash_after_write and call["tool"] == "create_issue":
                raise SimulatedCrash("Write committed; checkpoint not yet updated")
            state["results"].append(result)
            state["index"] += 1
            state["error"] = None
        else:
            state["status"] = "completed"
        self.save(task_id, state)
        return state
