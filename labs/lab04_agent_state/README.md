# Lab 04 — Agent State, Checkpoints and Recovery

[English](README.md) · [简体中文](README.zh-CN.md)

Resume a bounded tool loop after a crash between a committed write and its checkpoint. A scripted planner supplies a fixed plan so failure behavior is reproducible; this is not an autonomous LLM agent.

## Run

From the repository root, after installing dependencies (Python 3.11+, 3.12 recommended):

```bash
python -m labs.lab04_agent_state.app
python -m pytest tests/test_agent_state.py -q
```

No API key or network is required. Demos use temporary storage and clean it up afterward; your project files are untouched.

## Walkthrough

1. Read `agent.py`: task state stores the plan, next-call index, consumed attempts, results and status.
2. Run the demo: it pauses at `waiting_approval`; the trusted controller approves; a simulated crash occurs after the tool commits.
3. New registry and agent objects reopen the databases with no in-memory approval. The retry reads the durable receipt and completes with one issue. Expected final status: `completed`, attempts: 3, issue count: 1.
4. Read the subprocess test: a separate Python process resumes the task. Also inspect cancellation, operation conflict and persistent-budget tests.

## Exercises

1. Set `max_steps=1`: the first blocked attempt consumes the budget, and a later resume ends in `budget_exhausted`. Waiting does not reset budgets.
2. Cancel a task before execution; verify no issue is created. Re-run a completed task; results remain unchanged.
3. Replace the scripted plan with model proposals only after understanding the state machine. Keep validation, approval and durable receipts outside the planner.

## Boundaries and limitations

One worker per task is required: there is no distributed lock or concurrent cancellation protocol. Only attempt budgets are implemented, not wall-clock/token budgets. Unexpected storage failures propagate; inspect durable state before retry. Cancellation is checked between run invocations and cannot undo a committed write. Checkpoints are trusted local state, not a sandbox. External APIs still need their own outcome reconciliation.

## Exit check and interview

- [ ] Run the demo/tests and explain their output.
- [ ] Change one behavior and record expected versus observed results.
- [ ] Explain one failure and one production limitation without notes.

[Week 6 学习任务](../../STUDY_GUIDE.md#week-6) · [Interview](../../interview/README.md#week-6)
