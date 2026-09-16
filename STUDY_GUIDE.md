# Follow-along Study Guide

[English](STUDY_GUIDE.md) · [简体中文](STUDY_GUIDE.zh-CN.md) · [Interview](interview/README.md)

A default path for experienced software developers: **assigned reading → minimum build → exit check → interview explanation**. Use one primary resource each week. Optional study must not block progress.

## Pace and scope

The 12 weeks are stage labels, not a job guarantee. The original estimates total about 104 hours including Week 0; full courses, debugging and interview practice can exceed that. At eight hours a week, plan for 16–20 calendar weeks. One 18-week schedule: stages 0–2 in four weeks, 3–4 in three, 5–6 in three, 7–9 in four, and 10–12 in four. Adjust after each exit check.

Use each eight-hour block for two hours of selected study, four of building/evaluation, one of interview practice and one of review. Assigned topics are reading scopes, not claims about completing full courses in two hours. During active applications, add two–three hours per week or extend the schedule.

**Implementation status:** only Lab 01 (mock classifier) and Lab 02 (lexical retrieval, six queries) have supplied implementations. Later stages are assignments for your own capstone; the capstone directory contains a specification, not a finished application. Live model APIs may incur fees: start offline and set your own budget before connecting a provider.

## Start today

1. Use Python 3.11+ (3.12 recommended) and follow the [README](README.md) through `make validate`.
2. Copy the [proposal](templates/project-proposal.md) and [weekly tracker](templates/progress-tracker.md) into your own project.
3. Complete Week 0, then follow the numbered stages below. If blocked, reduce scope before repeating the exit check.

<a id="week-0"></a>
## Week 0 — Orientation

1. **Study:** [Chip Huyen — Introduction to Machine Learning Interviews](https://huyenchip.com/ml-interviews-book/) — Identify your target role; read the local project proposal template.
2. **Build:** Collect 5 target job descriptions; choose one support use case and write 20 eval cases.
3. **Exit check:** State users, inputs, expected answers and forbidden actions; exclude private data.
4. **Interview:** [Week 0](interview/README.md#week-0) — Answer without notes, check the rubric, then cite your code or evaluation.

<a id="week-1"></a>
## Week 1 — LLM foundations

1. **Study:** [How Transformer LLMs Work](https://learn.deeplearning.ai/courses/how-transformer-llms-work/) — Tokens → embeddings → attention → decoding; stop after you can explain the generation loop.
2. **Build:** Compare two prompt/context variants on 10 of your cases; record model/configuration, usage and latency.
3. **Exit check:** Explain context limits and one failure; do not treat model-reported confidence as calibrated probability.
4. **Interview:** [Week 1](interview/README.md#week-1) — Answer without notes, check the rubric, then cite your code or evaluation.

<a id="week-2"></a>
## Week 2 — Structured calls

1. **Study:** [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/) — Basic models → extra fields → data conversion/strictness → validation errors.
2. **Build:** Run Lab 01; replace the mock with one provider adapter in your own capstone, with bounded retries and timeouts.
3. **Exit check:** Reject invalid payloads; report schema validity separately from classification correctness.
4. **Interview:** [Week 2](interview/README.md#week-2) — Answer without notes, check the rubric, then cite your code or evaluation.

<a id="week-3"></a>
## Week 3 — Retrieval baseline

1. **Study:** [DeepLearning.AI — Retrieval Augmented Generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation) — Study ingestion, chunking and retrieval evaluation first.
2. **Build:** Run Lab 02; expand from its 6 toy queries to 20 labeled queries on your own documents. Add cited answers afterward.
3. **Exit check:** Report Recall@k/MRR and inspect 3 failures; distinguish retrieval errors from unsupported answers.
4. **Interview:** [Week 3](interview/README.md#week-3) — Answer without notes, check the rubric, then cite your code or evaluation.

<a id="week-4"></a>
## Week 4 — Retrieval experiments

1. **Study:** [DeepLearning.AI — Retrieval Augmented Generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation) — Select hybrid search and reranking topics; change one component at a time.
2. **Build:** Compare lexical baseline with one vector/hybrid/reranking candidate; reserve untouched test queries.
3. **Exit check:** Keep data/configs fixed; record quality and latency even if the candidate loses.
4. **Interview:** [Week 4](interview/README.md#week-4) — Answer without notes, check the rubric, then cite your code or evaluation.

<a id="week-5"></a>
## Week 5 — Tool workflows

1. **Study:** [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — Read workflows, routing and tool design; optionally study Agentic AI tool use.
2. **Build:** Implement two read-only tools and a draft-issue tool; writes use an explicit approval boundary.
3. **Exit check:** Test wrong arguments, tool errors and duplicate requests; explain idempotency.
4. **Interview:** [Week 5](interview/README.md#week-5) — Answer without notes, check the rubric, then cite your code or evaluation.

<a id="week-6"></a>
## Week 6 — Stateful agents

1. **Study:** [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — Read the agent loop and stopping conditions; optionally study planning.
2. **Build:** Add step/time budgets, persisted state and approval; simulate failure after a tool call.
3. **Exit check:** Resume without duplicating a write; prove termination and identify the approved action precisely.
4. **Interview:** [Week 6](interview/README.md#week-6) — Answer without notes, check the rubric, then cite your code or evaluation.

<a id="week-7"></a>
## Week 7 — Evaluation harness

1. **Study:** [DeepLearning.AI — Evaluating AI Agents](https://www.deeplearning.ai/short-courses/evaluating-ai-agents/) — Prioritize component evaluation, trajectory evaluation and judge calibration.
2. **Build:** Grow to at least 50 cases, separate development/test sets, add deterministic graders and human review.
3. **Exit check:** Compare two versions on held-out cases; report denominators, slices and judge-human disagreement.
4. **Interview:** [Week 7](interview/README.md#week-7) — Answer without notes, check the rubric, then cite your code or evaluation.

<a id="week-8"></a>
## Week 8 — Permission boundaries

1. **Study:** [OWASP — LLM Top 10](https://genai.owasp.org/llm-top-10/) — Read the three risk categories listed in the resource guide; map them to your tools.
2. **Build:** Add tenant filters and 10 adversarial cases covering injection, leakage and approval bypass.
3. **Exit check:** No unauthorized writes in this test set; document coverage limits rather than claiming universal safety.
4. **Interview:** [Week 8](interview/README.md#week-8) — Answer without notes, check the rubric, then cite your code or evaluation.

<a id="week-9"></a>
## Week 9 — Production

1. **Study:** [Google — Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/) — Read the three selected SRE chapters; apply their ideas to model calls.
2. **Build:** Deploy one service, add trace IDs, budget limits and timeout/fallback; run a small load experiment.
3. **Exit check:** Report p95 and cost per successful task with workload/sample count and a rollback procedure.
4. **Interview:** [Week 9](interview/README.md#week-9) — Answer without notes, check the rubric, then cite your code or evaluation.

<a id="week-10"></a>
## Week 10 — Coding workflow

1. **Study:** [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — Revisit agents in coding and tool design; use your execution environment’s official isolation documentation.
2. **Build:** Generate a small patch in an isolated disposable environment with limited credentials/network; review the diff and tests.
3. **Exit check:** Demonstrate boundary enforcement; a temporary directory or passing tests alone is not a sandbox/security proof.
4. **Interview:** [Week 10](interview/README.md#week-10) — Answer without notes, check the rubric, then cite your code or evaluation.

<a id="week-11"></a>
## Week 11 — System design

1. **Study:** [System Design Primer](https://github.com/donnemartin/system-design-primer) — Select caching, queues and storage trade-offs; design around the capstone’s requirements.
2. **Build:** Write two ADRs and draw the data/permission flow; cut one feature using eval evidence.
3. **Exit check:** Defend a simpler alternative and explain what changes at 10× traffic.
4. **Interview:** [Week 11](interview/README.md#week-11) — Answer without notes, check the rubric, then cite your code or evaluation.

<a id="week-12"></a>
## Week 12 — Portfolio and interviews

1. **Study:** [Chip Huyen — AI Engineering companion repository](https://github.com/chiphuyen/aie-book) — Review your weakest topics, then use the interview guide’s mock schedule.
2. **Build:** Publish reproducible setup, evaluation report, architecture and a 3–5 minute demo; run two mock interviews.
3. **Exit check:** A second person can reproduce a result; every résumé number has a source and limitations.
4. **Interview:** [Week 12](interview/README.md#week-12) — Answer without notes, check the rubric, then cite your code or evaluation.

## Continue learning

Move on after meeting the exit check and update the tracker’s interview review. See [ROADMAP.md](ROADMAP.md) for the full competency map and the [interview resource table](interview/README.md#resources) for access notes.
