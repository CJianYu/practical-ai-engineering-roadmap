# 01 — LLM Foundations for Builders

> **Goal:** Develop a useful mental model of model behavior without pausing product work for months of theory.

## Learn

- Tokens, tokenization, embeddings, attention, transformer blocks, context windows, and autoregressive generation.
- Training versus inference; base models versus instruction-tuned models.
- Decoding controls, test-time compute, nondeterminism, and common hallucination patterns.
- Why context quality and task formulation often matter more than clever wording.

## Build

- Create a small explorer that records prompt tokens, output tokens, latency, and estimated cost.
- Run the same task across at least two prompts or models.
- Document three observed failure modes and hypotheses.

## Prove

- Explain one-token-at-a-time generation in plain language.
- Predict which changes affect quality, context usage, latency, and cost.
- Avoid treating model output as a trusted program result.

## Explain / interview prompts

- Why can the same prompt produce different answers?
- What happens when relevant evidence falls outside the context window?
- When does a larger model not solve the product problem?

## Exit criteria

- [ ] A runnable artifact exists.
- [ ] A representative eval set exists.
- [ ] At least one failure mode is documented.
- [ ] Quality, latency, cost, and safety implications are considered.
- [ ] You can explain one design trade-off without relying on framework marketing language.

## Resources

- [DeepLearning.AI — How Transformer LLMs Work](https://learn.deeplearning.ai/courses/how-transformer-llms-work/)
- [Stanford CS336 — Language Modeling from Scratch](https://stanford-cs336.github.io/)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)

**Follow along:** [Weekly assignments](../../STUDY_GUIDE.md) · [Interview preparation](../../interview/README.md) · [面试中文指南](../../interview/README.zh-CN.md)

[← Back to roadmap](../../ROADMAP.md)
