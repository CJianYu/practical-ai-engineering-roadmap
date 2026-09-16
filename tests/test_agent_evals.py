import json
import subprocess
import sys
from copy import deepcopy

import pytest

from labs.lab05_agent_evals.evals import DATA, compare, evaluate, load_cases


def test_candidate_improves_fixed_fixture_set():
    cases = load_cases(DATA)
    baseline = evaluate(cases, "baseline")
    candidate = evaluate(cases, "candidate")
    assert baseline["pass_rate"] == 7 / 8
    assert candidate["pass_rate"] == 1
    assert candidate["unauthorized_writes"] == 0
    assert compare(baseline, candidate)["passed"]
    assert candidate["slices"]["validation"] == {"passed": 4, "total": 4}


def test_aggregate_tie_cannot_hide_individual_regression():
    cases = load_cases(DATA)
    baseline = evaluate(cases, "baseline")
    regressed = evaluate(cases, "regressed")
    assert regressed["pass_rate"] == baseline["pass_rate"]
    gate = compare(baseline, regressed)
    assert not gate["passed"]
    assert gate["regressions"] == ["lookup"]


def test_safety_gate_fails_even_when_quality_is_unchanged():
    baseline = evaluate(load_cases(DATA), "candidate")
    candidate = deepcopy(baseline)
    candidate["unauthorized_writes"] = 1
    assert not compare(baseline, candidate)["passed"]


def test_mismatched_cases_are_not_comparable():
    baseline = evaluate(load_cases(DATA), "baseline")
    candidate = deepcopy(baseline)
    candidate["cases"].pop()
    with pytest.raises(ValueError, match="matching"):
        compare(baseline, candidate)


def test_empty_and_duplicate_datasets_are_rejected(tmp_path):
    path = tmp_path / "cases.jsonl"
    first = DATA.read_text().splitlines()[0]
    for text in ["", first + "\n" + first]:
        path.write_text(text)
        with pytest.raises(ValueError):
            load_cases(path)


@pytest.mark.parametrize("version, exit_code", [("candidate", 0), ("regressed", 1)])
def test_cli_report_and_exit_status(tmp_path, version, exit_code):
    output = tmp_path / "report.json"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "labs.lab05_agent_evals.evals",
            "--candidate",
            version,
            "--output",
            str(output),
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == exit_code, result.stderr
    assert json.loads(output.read_text())["gate"]["passed"] is (exit_code == 0)
