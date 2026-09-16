# AI Engineering Skill Matrix

Use this matrix to decide what to learn next and what evidence belongs in a portfolio.

| Skill area | Working knowledge | Portfolio evidence | Useful metrics |
|---|---|---|---|
| LLM foundations | Tokens, context, decoding, model limits | Cost/context experiment | Tokens, latency, cost |
| Model APIs | Structured output, retries, routing | Typed provider-neutral gateway | Schema validity, retry rate |
| RAG | Ingestion, retrieval, citations | Cited assistant + labeled set | Recall@k, MRR, citation accuracy |
| Tools | Schemas, validation, idempotency | Tool registry + workflow | Tool/argument accuracy |
| Agents | State, termination, checkpoints | Bounded agent with approval | Task success, steps, recovery |
| Evals | Datasets, graders, calibration | Repeatable eval harness | Success rate, agreement, regressions |
| Safety | Injection, permissions, sandboxing | Threat model + red-team suite | Unauthorized action rate |
| Production | Tracing, rollout, budgets | Deployed monitored service | p95, availability, cost/success |
| Coding agents | Context, sandbox, tests, review | Tested patch workflow | Patch success, policy violations |
| Product judgment | Task choice, scope, trade-offs | Proposal + ADRs + removed features | Evidence coverage |

## Self-assessment levels

### Level 0 — Aware

You can define the concept but have not built it.

### Level 1 — Implemented

You have a small working example.

### Level 2 — Evaluated

You have representative tests, metrics, and documented failures.

### Level 3 — Operated

You have deployed it, monitored it, and changed it based on real evidence.

For job readiness, aim for Level 2 across the core skills and Level 3 in at least one capstone system.

## Optional foundations track

This track is useful when software or ML fundamentals are missing. It should run in parallel and should not delay all practical work.

### Software foundations

- Python typing, async I/O, packaging, testing, HTTP, SQL, Docker, and CI/CD
- System design: queues, caches, idempotency, authentication, authorization, and observability
- Security: secrets, input validation, least privilege, and threat modeling

### Machine-learning foundations

- train/validation/test splits;
- supervised learning and common metrics;
- bias/variance and error analysis;
- embeddings and similarity;
- neural-network and transformer basics;
- data leakage and distribution shift.

Suggested anchor: [DeepLearning.AI Machine Learning Specialization](https://www.deeplearning.ai/courses/machine-learning-specialization/).

## Role targeting

| Target role | Prioritize | De-prioritize initially |
|---|---|---|
| Applied AI Engineer | RAG, tools, agents, evals, production | Distributed pretraining, CUDA kernels |
| AI Product Engineer | Applied AI + frontend/UX + product judgment | Deep model research |
| ML Engineer | ML fundamentals, data pipelines, training, serving | Agent-framework breadth |
| Research Engineer | Math, PyTorch/JAX, papers, experiments, training systems | Product polish |
