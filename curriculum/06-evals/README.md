# 06 — Evaluation-Driven Development

> **Goal:** Turn subjective demos into a repeatable improvement loop.

## Learn

- Golden datasets, code-based graders, model-based graders, human review, and calibration.
- Component, final-answer, and trajectory evaluation.
- Benchmark design as request, environment, stopping criteria, and scorer.
- Error taxonomies, slices, regression gates, pass@k, and repeated-run reliability.

## Build

- Create at least 50 representative cases from real or realistically simulated tasks.
- Use deterministic graders wherever the expected state can be computed.
- Calibrate any LLM judge against a small human-labeled set.

## Prove

- Every system change can be compared to a fixed baseline.
- The report includes quality, cost, latency, safety, and error slices.
- A failed case maps to a concrete next action.

## Explain / interview prompts

- How do you know your eval set represents production?
- When is LLM-as-a-judge appropriate?
- How do you prevent overfitting to a benchmark?

## Exit criteria

- [ ] A runnable artifact exists.
- [ ] A representative eval set exists.
- [ ] At least one failure mode is documented.
- [ ] Quality, latency, cost, and safety implications are considered.
- [ ] You can explain one design trade-off without relying on framework marketing language.

## Resources

- [Stanford CS329Z](https://cs329z.stanford.edu/)
- [OpenAI — Evals guide](https://platform.openai.com/docs/guides/evals)
- [Eval report template](../../templates/eval-report.md)

[← Back to roadmap](../../ROADMAP.md)
