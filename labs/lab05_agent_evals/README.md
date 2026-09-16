# Lab 05 — Agent Evaluation and Regression Gates

[English](README.md) · [简体中文](README.zh-CN.md)

Replay eight fixed proposed-call cases through Lab 03. Compare baseline/candidate tool choice, execution status, final issue count, safety violations and error slices. This measures fixture behavior, not live-model intelligence.

## Run

From the repository root, after installing dependencies (Python 3.11+, 3.12 recommended):

```bash
python -m labs.lab05_agent_evals.evals
python -m pytest tests/test_agent_evals.py -q
```

No API key or network is required. Demos use temporary storage and clean it up afterward; your project files are untouched.

## Walkthrough

1. Read `data/cases.jsonl`. Each row contains trusted expected outcomes and fixed baseline/candidate/regressed proposals. The evaluator controls approval; model outputs never do.
2. Run the default comparison: baseline passes 7/8 cases; candidate passes 8/8. Both create zero unauthorized writes. These are deliberately constructed teaching results.
3. Inspect per-case results and slices in the JSON report. Invalid calls count as success only when the expected outcome is rejection.
4. Run `--candidate regressed`: aggregate pass rate ties the baseline at 7/8, but `lookup` regresses, so the process exits 1. A passing gate does not imply readiness for production.

## Exercises

1. Write a report with `--output /tmp/agent-eval-report.json`; inspect the failed case and propose one fix.
2. Add 10 held-out cases with expected side effects and trust boundaries. Keep development cases separate; fixture IDs and labels are not model inputs.
3. Replace proposed-call fixtures with outputs from two frozen model/prompt versions. Record model/configuration, repeated runs, actual usage and latency separately. Add human-calibrated judges only for outcomes deterministic checks cannot assess.

```bash
python -m labs.lab05_agent_evals.evals --output /tmp/agent-eval-report.json
# Expected exit code: 1 (intentional regression)
python -m labs.lab05_agent_evals.evals --candidate regressed
```

## Boundaries and limitations

The eight cases are tiny synthetic fixtures, with no claim of statistical significance or representative production coverage. No live model, LLM judge, calibrated quality score, cost or latency benchmark is supplied. The gate rejects per-case regressions, increased aggregate error or any unauthorized write; it does not enforce a universal minimum quality threshold. For production, set thresholds from task risk and workload evidence.

## Exit check and interview

- [ ] Run the demo/tests and explain their output.
- [ ] Change one behavior and record expected versus observed results.
- [ ] Explain one failure and one production limitation without notes.

[Week 7 学习任务](../../STUDY_GUIDE.md#week-7) · [Interview](../../interview/README.md#week-7)
