from pathlib import Path
from tempfile import TemporaryDirectory

from labs.lab03_tool_calling.tools import ToolRegistry

from .agent import Agent, SimulatedCrash


def main() -> None:
    with TemporaryDirectory() as directory:
        root = Path(directory)
        tools = ToolRegistry(root / "tools.sqlite")
        agent = Agent(root / "state.sqlite", tools)
        call = {
            "tool": "create_issue",
            "arguments": {"title": "Investigate billing", "body": "Human review requested."},
            "operation_id": "task-1-issue",
        }
        agent.create("task-1", [call])
        print("First run:", agent.run("task-1")["status"])
        tools.approve(call)  # Simulated human-controller action.
        try:
            agent.run("task-1", crash_after_write=True)
        except SimulatedCrash as error:
            print(error)
        # Rebuild both objects; only persisted data survives, not in-memory approval.
        restarted_tools = ToolRegistry(root / "tools.sqlite")
        restarted = Agent(root / "state.sqlite", restarted_tools)
        state = restarted.run("task-1")
        print(
            {
                "status": state["status"],
                "attempts": state["attempts"],
                "issue_count": restarted_tools.issue_count(),
            }
        )


if __name__ == "__main__":
    main()
