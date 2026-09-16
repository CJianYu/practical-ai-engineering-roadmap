# 09 — Coding Agents and Sandboxed Execution

> **Goal:** Use coding agents as bounded engineering systems rather than unreviewed code generators.

## Learn

- Repository context, specifications, planning, file editing, commands, tests, diffs, and review.
- Command allowlists, network controls, filesystem boundaries, secrets, and ephemeral environments.
- Long-running task checkpoints and harness design.
- Evaluating patches on correctness, tests, scope, and policy compliance.

## Build

- Give the agent an approved issue and a constrained workspace.
- Require a plan before modification and run tests before presenting a diff.
- Prevent direct merge and production deployment.

## Prove

- The agent cannot modify files outside the allowed path.
- Every patch includes test evidence and a human-readable summary.
- Failures stop rather than expanding scope indefinitely.

## Explain / interview prompts

- How would you sandbox a coding agent?
- What context does a coding agent need?
- How do you evaluate a patch beyond “tests pass”?

## Exit criteria

- [ ] A runnable artifact exists.
- [ ] A representative eval set exists.
- [ ] At least one failure mode is documented.
- [ ] Quality, latency, cost, and safety implications are considered.
- [ ] You can explain one design trade-off without relying on framework marketing language.

## Resources

- [Stanford CS329Z coding agents module](https://cs329z.stanford.edu/)
- [SWE-agent](https://github.com/SWE-agent/SWE-agent)
- [OpenHands](https://github.com/All-Hands-AI/OpenHands)

[← Back to roadmap](../../ROADMAP.md)
