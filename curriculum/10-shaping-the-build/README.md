# 10 — Shape the Build

> **Goal:** Choose valuable AI tasks and turn ambiguity into an evidence-backed system design.

## Learn

- User task discovery, problem decomposition, AI-versus-code boundaries, and risk-adjusted prototypes.
- Designing around model uncertainty instead of hiding it.
- Architecture decision records, success metrics, and stop conditions.
- How evaluation evidence should change product scope.

## Build

- Revise the original proposal using eval results and user feedback.
- Write at least three architecture decision records.
- Remove one feature whose complexity is not justified by evidence.

## Prove

- Every AI component has a reason to exist.
- Product claims are bounded by measured capability.
- The team knows when to use a smaller workflow, a stronger model, better data, or no AI.

## Explain / interview prompts

- How do you decide whether a task is suitable for AI?
- When should an AI prototype become a deterministic feature?
- What evidence would make you change the architecture?

## Exit criteria

- [ ] A runnable artifact exists.
- [ ] A representative eval set exists.
- [ ] At least one failure mode is documented.
- [ ] Quality, latency, cost, and safety implications are considered.
- [ ] You can explain one design trade-off without relying on framework marketing language.

## Resources

- [Andrew Ng — AI Engineering Skills Map](https://www.andrewng.org/writing)
- [Architecture decision template](../../templates/architecture-decision-record.md)
- [Capstone specification](../../capstone/README.md)

**Follow along:** [Weekly assignments](../../STUDY_GUIDE.md) · [Interview preparation](../../interview/README.md) · [面试中文指南](../../interview/README.zh-CN.md)

[← Back to roadmap](../../ROADMAP.md)
