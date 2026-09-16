# 07 — Safety, Permissions, and Adversarial Inputs

> **Goal:** Design systems that fail safely when models process untrusted content or control tools.

## Learn

- Direct and indirect prompt injection, data leakage, excessive agency, and unsafe output handling.
- Least privilege, read/write separation, approval, sandboxing, rate limits, and auditability.
- Threat modeling model inputs, retrieved documents, tools, secrets, and outputs.
- Why instructions inside retrieved content are data, not authority.

## Build

- Create a threat model and permission matrix.
- Add red-team cases that attempt approval bypass, secret access, destructive actions, and instruction injection.
- Require explicit user approval for sensitive writes.

## Prove

- Unauthorized write-action rate is zero on the local adversarial set.
- Tool credentials have the narrowest practical scope.
- Every sensitive action has an attributable audit event.

## Explain / interview prompts

- Why is prompt injection not solved by a stronger system prompt?
- How should permissions differ between reading and writing?
- What belongs inside a sandbox?

## Exit criteria

- [ ] A runnable artifact exists.
- [ ] A representative eval set exists.
- [ ] At least one failure mode is documented.
- [ ] Quality, latency, cost, and safety implications are considered.
- [ ] You can explain one design trade-off without relying on framework marketing language.

## Resources

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [OpenAI — Prompt injection](https://openai.com/index/prompt-injections/)
- [Stanford CS329Z safety module](https://cs329z.stanford.edu/)

**Follow along:** [Weekly assignments](../../STUDY_GUIDE.md) · [Interview preparation](../../interview/README.md) · [面试中文指南](../../interview/README.zh-CN.md)

[← Back to roadmap](../../ROADMAP.md)
