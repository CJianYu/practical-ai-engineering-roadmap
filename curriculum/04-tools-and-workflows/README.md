# 04 — Tools and Deterministic Workflows

> **Goal:** Connect models to real systems without surrendering control of business logic.

## Learn

- Function calling, clear tool schemas, validation, idempotency, retries, and compensating actions.
- Read versus write tools; least privilege; approval boundaries.
- MCP concepts and when a standard tool interface helps.
- Workflow patterns: routing, parallelization, orchestrator-worker, and evaluator-optimizer.

## Build

Start with [Lab 03](../../labs/lab03_tool_calling/README.md) ([中文](../../labs/lab03_tool_calling/README.zh-CN.md)), then extend it in your capstone.

- Implement a small tool registry with explicit input and output schemas.
- Create one deterministic multi-step workflow before adding an open agent loop.
- Add idempotency keys and approval to every write action.

## Prove

- Measure tool selection and argument correctness independently.
- Tool errors are visible, typed, and recoverable.
- Repeated model calls cannot duplicate a destructive action.

## Explain / interview prompts

- How do you decide between a workflow and an agent?
- What makes a good tool interface for a model?
- How do you make a write tool safe to retry?

## Exit criteria

- [ ] A runnable artifact exists.
- [ ] A representative eval set exists.
- [ ] At least one failure mode is documented.
- [ ] Quality, latency, cost, and safety implications are considered.
- [ ] You can explain one design trade-off without relying on framework marketing language.

## Resources

- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/)
- [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Stanford CS329Z](https://cs329z.stanford.edu/)

**Follow along:** [Weekly assignments](../../STUDY_GUIDE.md) · [Interview preparation](../../interview/README.md) · [面试中文指南](../../interview/README.zh-CN.md)

[← Back to roadmap](../../ROADMAP.md)
