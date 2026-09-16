# 00 — Orientation and Baseline

> **Goal:** Choose the right target role, scope one real project, and define evidence before implementation.

## Learn

- The practical difference between Applied AI Engineer, ML Engineer, Research Engineer, and AI Product Engineer.
- Task-level automation versus vague job-level claims.
- How to define users, representative tasks, constraints, failure modes, and acceptance criteria.
- Why an evaluation set should begin before the system is built.

## Build

- Complete `templates/project-proposal.md` for one real domain.
- Write 20 representative user requests, including normal, ambiguous, missing-data, and adversarial cases.
- Create an architecture v0 that separates deterministic code, model calls, retrieval, and tools.

## Prove

- Every planned feature maps to at least one user task and one acceptance criterion.
- You can state what the system must never do.
- A reviewer can understand the project in five minutes.

## Explain / interview prompts

- Why does this problem need an LLM at all?
- Which parts should remain deterministic?
- What would make you stop building this project?

## Exit criteria

- [ ] A runnable artifact exists.
- [ ] A representative eval set exists.
- [ ] At least one failure mode is documented.
- [ ] Quality, latency, cost, and safety implications are considered.
- [ ] You can explain one design trade-off without relying on framework marketing language.

## Resources

- [Andrew Ng — AI Engineering Skills Map](https://www.andrewng.org/writing)
- [Project proposal template](../../templates/project-proposal.md)
- [Skill matrix](../../docs/skill-matrix.md)

**Follow along:** [Weekly assignments](../../STUDY_GUIDE.md) · [Interview preparation](../../interview/README.md) · [面试中文指南](../../interview/README.zh-CN.md)

[← Back to roadmap](../../ROADMAP.md)
