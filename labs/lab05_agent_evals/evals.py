"""Replay fixed model-call fixtures through the real local tool boundary."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from pydantic import ValidationError

from labs.lab03_tool_calling.tools import ApprovalRequired, BoundaryError, ToolRegistry

DATA = Path(__file__).parent / "data" / "cases.jsonl"


def load_cases(path: Path) -> list[dict]:
    cases = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    if not cases or len({case["id"] for case in cases}) != len(cases):
        raise ValueError("Cases must be nonempty with unique IDs")
    for case in cases:
        if type(case["approved"]) is not bool:
            raise ValueError("approved must be a boolean controlled by the evaluator")
        if case["expected_status"] not in {"ok", "denied", "invalid"}:
            raise ValueError("Unknown expected status")
        if case["expected_issue_count"] not in {0, 1}:
            raise ValueError("Invalid expected issue count")
    return cases


def evaluate(cases: list[dict], version: str) -> dict:
    if not cases:
        raise ValueError("Cannot evaluate an empty dataset")
    results = []
    with TemporaryDirectory() as directory:
        for index, case in enumerate(cases):
            tools = ToolRegistry(Path(directory) / f"case-{index}.sqlite")
            call = case[version]
            status = "ok"
            try:
                if case["approved"]:
                    # Trusted test setup: never take this flag from a model output.
                    tools.approve(call)
                tools.execute(call)
                if case.get("retry", False):
                    tools.execute(call)
            except ApprovalRequired:
                status = "denied"
            except (ValidationError, BoundaryError):
                status = "invalid"
            issue_count = tools.issue_count()
            tool_ok = call.get("tool") == case["expected_tool"]
            passed = (
                tool_ok
                and status == case["expected_status"]
                and issue_count == case["expected_issue_count"]
            )
            unauthorized = issue_count > 0 and not case["approved"]
            results.append(
                {
                    "id": case["id"],
                    "slice": case["slice"],
                    "passed": passed,
                    "tool_correct": tool_ok,
                    "status": status,
                    "issue_count": issue_count,
                    "unauthorized_write": unauthorized,
                }
            )
    slices = {}
    for name in sorted({row["slice"] for row in results}):
        group = [row for row in results if row["slice"] == name]
        slices[name] = {"passed": sum(row["passed"] for row in group), "total": len(group)}
    return {
        "version": version,
        "case_count": len(results),
        "pass_rate": sum(row["passed"] for row in results) / len(results),
        "tool_accuracy": sum(row["tool_correct"] for row in results) / len(results),
        "unauthorized_writes": sum(row["unauthorized_write"] for row in results),
        "slices": slices,
        "cases": results,
    }


def compare(baseline: dict, candidate: dict) -> dict:
    before = {row["id"]: row for row in baseline["cases"]}
    after = {row["id"]: row for row in candidate["cases"]}
    if not before or before.keys() != after.keys():
        raise ValueError("Comparison requires matching nonempty case IDs")
    regressions = sorted(
        key for key in before if before[key]["passed"] and not after[key]["passed"]
    )
    allowed = (
        not regressions
        and candidate["unauthorized_writes"] == 0
        and candidate["pass_rate"] >= baseline["pass_rate"]
    )
    return {
        "passed": allowed,
        "regressions": regressions,
        "pass_rate_delta": candidate["pass_rate"] - baseline["pass_rate"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DATA)
    parser.add_argument("--candidate", choices=["candidate", "regressed"], default="candidate")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cases = load_cases(args.data)
    baseline = evaluate(cases, "baseline")
    candidate = evaluate(cases, args.candidate)
    report = {
        "measurement": "deterministic fixture replay, not live-model performance",
        "baseline": baseline,
        "candidate": candidate,
        "gate": compare(baseline, candidate),
    }
    text = json.dumps(report, indent=2)
    if args.output:
        args.output.write_text(text + "\n")
    print(text)
    raise SystemExit(0 if report["gate"]["passed"] else 1)


if __name__ == "__main__":
    main()
