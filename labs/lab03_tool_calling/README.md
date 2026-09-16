# Lab 03 — Tool Calling, Approval and Idempotency

[English](README.md) · [简体中文](README.zh-CN.md)

Validate a proposed tool call, block an unapproved write, then repeat an approved operation without duplicating it. All issues live in local SQLite; nothing is sent to GitHub.

## Run

From the repository root, after installing dependencies (Python 3.11+, 3.12 recommended):

```bash
python -m labs.lab03_tool_calling.app
python -m pytest tests/test_tool_calling.py -q
```

No API key or network is required. Demos use temporary storage and clean it up afterward; your project files are untouched.

## Walkthrough

1. Read `tools.py`: the registry exposes `search_docs` and `create_issue`; schemas reject unknown tools/fields and incorrect types. `search_docs` returns a fixed policy fixture, not a real search engine.
2. Run the demo. The first write is blocked. The trusted demo controller then explicitly approves the displayed operation; both subsequent calls return the same issue ID and `issue_count` is 1.
3. Trace `fingerprint`: approval covers the tool, exact arguments and operation ID. The model cannot add an `approved` field or invoke an `approve` tool.
4. Read the transaction: the local issue and its receipt commit together. Reusing an operation ID with changed arguments fails, even if that new payload is approved.

## Exercises

1. Change the body after approval and observe rejection. Approve a new operation ID to create a genuinely separate issue.
2. Run the rollback test: receipt persistence fails, so the issue insert rolls back too.
3. Replace fixed search with Lab 02 retrieval. Keep authorization in the dispatcher, outside model-generated content.

## Boundaries and limitations

This is a single-user simulator, not production authorization. The process and database must be trusted. Approvals expire on restart; a committed receipt may be read again without reapproval because it performs no new write. A local transaction cannot make an external GitHub/API call atomic: use provider idempotency or reconcile uncertain outcomes before retry. No tenant isolation, approval expiry timer or credential management is implemented.

## Exit check and interview

- [ ] Run the demo/tests and explain their output.
- [ ] Change one behavior and record expected versus observed results.
- [ ] Explain one failure and one production limitation without notes.

[Week 5 学习任务](../../STUDY_GUIDE.md#week-5) · [Interview](../../interview/README.md#week-5)
