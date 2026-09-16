from pathlib import Path
from tempfile import TemporaryDirectory

from .tools import ApprovalRequired, ToolRegistry


def main() -> None:
    with TemporaryDirectory() as directory:
        tools = ToolRegistry(Path(directory) / "tools.sqlite")
        call = {
            "tool": "create_issue",
            "arguments": {
                "title": "Review billing dispute",
                "body": "Customer reports duplicate charge.",
            },
            "operation_id": "demo-issue-1",
        }
        print("Proposed operation:", call)
        try:
            tools.execute(call)
        except ApprovalRequired:
            print("Blocked: this write needs approval.")
        # Simulates a human approving the displayed payload; not an LLM decision.
        tools.approve(call)
        first = tools.execute(call)
        second = tools.execute(call)
        print({"first": first, "retry": second, "issue_count": tools.issue_count()})


if __name__ == "__main__":
    main()
