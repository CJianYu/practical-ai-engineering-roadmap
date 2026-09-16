# 05 — Agents, State, and Memory

> **Goal:** Build bounded autonomy with explicit state, stopping conditions, recovery, and human oversight.

## Learn

- Agent loops, ReAct, plan-and-execute, reflection, termination, and step budgets.
- Short-term state, long-term memory, files and databases as external memory.
- Checkpointing, interruption, resume, and human-in-the-loop approval.
- Why single-agent systems are often preferable to multi-agent complexity.

## Build

- Implement a framework-light agent loop, then optionally reimplement it with an orchestration framework.
- Persist state and resume one interrupted task.
- Store structured decisions, not an unbounded transcript dump.

## Prove

- The agent stops under success, failure, cancellation, and budget exhaustion.
- Repeated calls and loops are detected.
- A human can inspect state and approve or reject a risky step.

## Explain / interview prompts

- What makes an agent different from a workflow?
- How would you debug a long trajectory?
- When does memory hurt performance or safety?

## Exit criteria

- [ ] A runnable artifact exists.
- [ ] A representative eval set exists.
- [ ] At least one failure mode is documented.
- [ ] Quality, latency, cost, and safety implications are considered.
- [ ] You can explain one design trade-off without relying on framework marketing language.

## Resources

- [DeepLearning.AI — Agentic AI](https://www.deeplearning.ai/courses/agentic-ai)
- [Stanford CS329Z](https://cs329z.stanford.edu/)
- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction)

[← Back to roadmap](../../ROADMAP.md)
