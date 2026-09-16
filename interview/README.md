# Applied AI Engineering Interview Preparation

[English](README.md) · [简体中文](README.zh-CN.md) · [Study guide](../STUDY_GUIDE.md)

For Applied AI, AI Product and Full-stack AI roles. Adjust emphasis using actual job descriptions and the employer’s interview process. Training-heavy MLE/research roles require additional math, ML and training preparation. Prompts below are original practice exercises, not claimed company questions.

## How to practice

Use the study plan’s one-hour weekly interview block: 15 minutes answering without notes, 20 coding/designing, 15 reviewing references and 10 logging gaps. Explain in your strongest language first, then record a three-minute English answer.

Practice rubric, not a hiring standard: 0 = cannot answer; 1 = can define; 2 = can compare options and failures; 3 = can support an answer with code/experiments and limitations. Two consecutive scores of 2 on core topics and 3 on your project are a useful self-check before mocks.

## Interview areas

| Area | Practice | Evidence |
|---|---|---|
| Coding | Algorithms plus JSON handling, async timeouts, retries and retrieval scoring | Working code, edge cases and complexity |
| AI engineering | LLMs, RAG, tools, agents and evals | Weekly answers and counterexamples |
| System design | Multi-tenant support agent, document QA, patch service | Architecture, permissions, SLOs, cost and scale |
| Project / behavioral | Failure, trade-off and collaboration disagreement | Your contribution, measured outcomes and reflection |

<a id="resources"></a>
## Resources and selection order

Use the weekly topic resource first. During interview preparation, select ML Interviews, System Design Primer and LeetCode according to diagnosed gaps rather than completing every resource.

| Resource | How to use it |
|---|---|
| [How Transformer LLMs Work](https://learn.deeplearning.ai/courses/how-transformer-llms-work/) | Tokens, embeddings, attention, decoding. |
| [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/) | Model validation, extra fields, conversion and strictness. |
| [DeepLearning.AI — Retrieval Augmented Generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation) | Retrieval, chunking and evaluation; use selected topics, not the whole course in two hours. |
| [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | Workflow versus agent; routing, loops and tool design. Use architectural ideas, not old SDK examples. |
| [DeepLearning.AI — Agentic AI](https://learn.deeplearning.ai/courses/agentic-ai) | Optional deeper course: select tool use, planning and evaluation. |
| [DeepLearning.AI — Evaluating AI Agents](https://www.deeplearning.ai/short-courses/evaluating-ai-agents/) | Tracing, component/trajectory evaluation and judge improvement. |
| [OWASP — LLM Top 10](https://genai.owasp.org/llm-top-10/) | Focus on prompt injection, sensitive information disclosure and excessive agency. |
| [Google — Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/) | Select Service Level Objectives, Monitoring Distributed Systems and Handling Overload. |
| [Chip Huyen — AI Engineering companion repository](https://github.com/chiphuyen/aie-book) | Reference on evaluation, RAG, agents and application architecture; not an interview question bank. |
| [Chip Huyen — Introduction to Machine Learning Interviews](https://huyenchip.com/ml-interviews-book/) | Role mapping, ML basics and evaluation. Older, broader ML material; skip training-heavy topics unless the job requires them. |
| [System Design Primer](https://github.com/donnemartin/system-design-primer) | Caching, queues, storage, scaling and system-design practice; add AI-specific eval and safety constraints yourself. |
| [LeetCode — Top Interview 150](https://leetcode.com/studyplan/top-interview-150/) | Select arrays, hash maps, two pointers, intervals, trees and heaps based on a diagnostic; finishing all 150 is optional. |
| [Python — Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html) | Practice cancellation, timeouts and concurrent tasks using docs matching your Python version. |
| [Stanford CS329Z — Engineering AI Agents](https://cs329z.stanford.edu/) | Optional course spine when the relevant public material is available; do not block progress waiting for lectures. |

Resource review: 2026-09-16. Author/official pages were reviewed for relevance. Some DeepLearning.AI course pages blocked automated access (403/access restrictions); titles/topics were checked against the official catalog and accessible pages, not the full authenticated course. Courses and practice platforms may require accounts or payment; certificates/subscriptions are not completion requirements. The AI Engineering repository is companion material, not the full book.

## Weekly prompts and answer checkpoints

<a id="week-0"></a>
### Week 0

**Which AI role are you preparing for? Why does this use case need AI?**

Checkpoints: Map five job descriptions to coding, AI systems, ML depth and product skills; state one deterministic alternative and a measurable user outcome.

Study: [Week 0](../STUDY_GUIDE.md#week-0) · [Chip Huyen — Introduction to Machine Learning Interviews](https://huyenchip.com/ml-interviews-book/)

<a id="week-1"></a>
### Week 1

**Explain token generation. Would a larger context window solve every knowledge problem?**

Checkpoints: Cover tokens, attention and decoding; distinguish context capacity from evidence relevance, freshness, cost and reliability.

Study: [Week 1](../STUDY_GUIDE.md#week-1) · [How Transformer LLMs Work](https://learn.deeplearning.ai/courses/how-transformer-llms-work/)

<a id="week-2"></a>
### Week 2

**A response passes its schema but is wrong. What do you test? When is retry safe?**

Checkpoints: Separate syntax/type constraints from semantic correctness and authorization; handle refusal/truncation and bounded retries; use idempotency for side effects.

Study: [Week 2](../STUDY_GUIDE.md#week-2) · [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/)

<a id="week-3"></a>
### Week 3

**Your RAG answer is wrong. How do you locate the failure?**

Checkpoints: Trace ingestion → retrieval → context → generation. Inspect labeled evidence, Recall@k and citations; test missing evidence and abstention.

Study: [Week 3](../STUDY_GUIDE.md#week-3) · [DeepLearning.AI — Retrieval Augmented Generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation)

<a id="week-4"></a>
### Week 4

**When do hybrid retrieval and reranking help? How do you prove an improvement?**

Checkpoints: Compare exact-term and semantic failures; use fixed data and held-out queries, measure latency/cost, report sample size and negative results.

Study: [Week 4](../STUDY_GUIDE.md#week-4) · [DeepLearning.AI — Retrieval Augmented Generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation)

<a id="week-5"></a>
### Week 5

**A tool times out after creating an issue. Should the agent retry?**

Checkpoints: A timeout leaves outcome uncertain. Use operation IDs, deduplication and outcome reconciliation before retry; validate arguments and enforce permissions outside the model.

Study: [Week 5](../STUDY_GUIDE.md#week-5) · [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)

<a id="week-6"></a>
### Week 6

**What state must survive a crash? How do you prevent repeated actions and endless loops?**

Checkpoints: Persist operation outcomes and checkpoint versions; bind approvals to exact arguments, limit steps/time/cost, and explain why memory is not an authorization source.

Study: [Week 6](../STUDY_GUIDE.md#week-6) · [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)

<a id="week-7"></a>
### Week 7

**An LLM judge says the candidate is better. Is that sufficient to ship?**

Checkpoints: Use held-out representative cases, human calibration, deterministic checks and error slices; inspect grader bias, uncertainty and regressions.

Study: [Week 7](../STUDY_GUIDE.md#week-7) · [DeepLearning.AI — Evaluating AI Agents](https://www.deeplearning.ai/short-courses/evaluating-ai-agents/)

<a id="week-8"></a>
### Week 8

**A retrieved document asks the agent to upload customer data. What stops it?**

Checkpoints: Treat document text as data; enforce server-side authorization, tenant isolation, tool/network limits and scoped approval. A system prompt alone is insufficient.

Study: [Week 8](../STUDY_GUIDE.md#week-8) · [OWASP — LLM Top 10](https://genai.owasp.org/llm-top-10/)

<a id="week-9"></a>
### Week 9

**Quality is stable but p95 doubles. How do you investigate and reduce it?**

Checkpoints: Break down queue/retrieval/model/tool timings; examine load and token growth, caching correctness, concurrency limits, fallbacks and quality-cost trade-offs.

Study: [Week 9](../STUDY_GUIDE.md#week-9) · [Google — Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/)

<a id="week-10"></a>
### Week 10

**A generated patch passes tests. What else must happen before it is trusted?**

Checkpoints: Inspect scope, tests’ coverage and changes, dependencies, secrets and execution isolation; separate patch creation from review, merge and deployment rights.

Study: [Week 10](../STUDY_GUIDE.md#week-10) · [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)

<a id="week-11"></a>
### Week 11

**Design a support agent for multiple customers. What is your simplest viable architecture?**

Checkpoints: Clarify workload/SLOs; sketch ingestion, tenant-aware retrieval, model gateway, tool approvals, async jobs and evals; explain one rejected option and scale bottlenecks.

Study: [Week 11](../STUDY_GUIDE.md#week-11) · [System Design Primer](https://github.com/donnemartin/system-design-primer)

<a id="week-12"></a>
### Week 12

**Describe your largest project failure and the change you can actually quantify.**

Checkpoints: Use situation → your decision → implementation → measured outcome → limitations. Link a commit/report and separate your work from generated or team contributions.

Study: [Week 12](../STUDY_GUIDE.md#week-12) · [Chip Huyen — AI Engineering companion repository](https://github.com/chiphuyen/aie-book)

## Practical coding and design drills

1. **30-minute coding:** implement a batch caller with bounded concurrency, per-call timeout and at most two retries. Clarify retryable errors; test cancellation, partial failures and output order using mocks.
2. **30-minute coding:** rank documents and calculate Recall@k/MRR. Define behavior for no relevant documents, duplicate IDs, empty input and tied scores.
3. **45-minute design:** design a multi-tenant support agent. Spend 5 minutes on users/load/metrics, 10 on data flow, 15 on retrieval/permissions, 10 on failure/cost and 5 on trade-offs.
4. **15-minute project defense:** ask a peer to challenge your baseline, labeling, test leakage, costs and personal contribution.

## Four-week application sprint

Allow an additional two–three hours weekly, or extend the learning schedule if your total budget remains eight hours.

| Week | Focus | Exit check |
|---|---|
| 1 | Map five job descriptions; review LLM/RAG; solve two diagnostic coding tasks | Identify the two largest gaps |
| 2 | One system-design mock; agents/evals/safety review; timed coding | Record scores and corrective actions |
| 3 | One 60-minute mock: 20 coding + 25 design + 15 project; address gaps | Improved answer or code for each gap |
| 4 | Repeat the mock format; record an English demo; audit résumé claims | Every project metric is traceable |

Résumé pattern: On **[workload/sample size]**, changed **[component]**, moving **[metric]** from **[baseline]** to **[result]**, with **[cost/latency trade-off]**. Fill placeholders only with measured results.
