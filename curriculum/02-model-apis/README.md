# 02 — Model APIs and Structured Output

> **Goal:** Put a reliable software boundary around a probabilistic model.

## Learn

- Structured output, schema validation, streaming, timeouts, retries, rate limits, and fallbacks.
- Provider-neutral interfaces, model routing, token accounting, and prompt versioning.
- Context engineering: selecting, ordering, compressing, and labeling information.
- Why parsing JSON is not the same as validating a business object.

## Build

- Complete `labs/lab01_structured_output`.
- Create a typed model gateway for one real application task.
- Record prompt version, model, tokens, latency, retries, and cost for every call.

## Prove

- Malformed output fails closed instead of silently entering application state.
- The application can switch model providers without rewriting business logic.
- Regression tests cover missing fields, extra fields, and invalid enum values.

## Explain / interview prompts

- How do you design retries without multiplying cost or duplicating actions?
- Where should schema validation happen?
- How would you route requests between fast and strong models?

## Exit criteria

- [ ] A runnable artifact exists.
- [ ] A representative eval set exists.
- [ ] At least one failure mode is documented.
- [ ] Quality, latency, cost, and safety implications are considered.
- [ ] You can explain one design trade-off without relying on framework marketing language.

## Resources

- [Pydantic documentation](https://docs.pydantic.dev/latest/)
- [LiteLLM documentation](https://docs.litellm.ai/)
- [Lab 01](../../labs/lab01_structured_output/README.md)

[← Back to roadmap](../../ROADMAP.md)
