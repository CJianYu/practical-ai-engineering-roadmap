# 12-Week Practical AI Engineering Roadmap

> Generated from [`roadmap.yaml`](roadmap.yaml). Edit the YAML, then run `make render`.

**Audience:** Software engineers transitioning into Applied AI Engineering.

**Default pace:** 12 weeks, approximately 8 hours per week, plus Week 0 orientation.

## Roadmap

| Week | Focus | Hours | Learn | Build | Prove | Metrics |
|---:|---|---:|---|---|---|---|
| 0 | [Orientation and Baseline](curriculum/00-orientation/README.md) | 4 | • Applied AI Engineer versus ML Engineer versus Research Engineer<br>• Task selection, scope, acceptance criteria, and evidence | A one-page capstone proposal and an initial set of 20 representative evaluation cases. | • The problem has clear users, tasks, boundaries, and failure definitions<br>• Every planned feature maps to a measurable acceptance criterion | • Eval case count<br>• Requirements coverage |
| 1 | [LLM Foundations for Builders](curriculum/01-llm-foundations/README.md) | 8 | • Tokens, embeddings, attention, transformer blocks, decoding, and context windows<br>• Why models are probabilistic and how that changes software design | A token, context, latency, and cost exploration notebook or service. | • Explain the generation loop without relying on framework vocabulary<br>• Demonstrate how prompts, temperature, context, and model choice affect outputs | • Token count<br>• Latency<br>• Estimated cost |
| 2 | [Model APIs and Structured Output](curriculum/02-model-apis/README.md) | 8 | • Structured outputs, schema validation, streaming, retries, timeouts, fallbacks, and model routing<br>• Context engineering and prompt versioning | A typed, provider-neutral model gateway. | • Invalid model output cannot cross the application boundary silently<br>• Calls expose latency, token usage, cost, retries, and prompt version | • Schema-valid response rate<br>• Retry rate<br>• p50 and p95 latency<br>• Cost per request |
| 3 | [RAG Foundations](curriculum/03-rag/README.md) | 8 | • Document processing, chunking, metadata, embeddings, indexing, retrieval, and citations<br>• Retrieval failure versus generation failure | A cited document assistant with an ingestion pipeline. | • The system retrieves the correct evidence for a labeled query set<br>• Answers cite valid sources and abstain when evidence is missing | • Recall at k<br>• Mean reciprocal rank<br>• Citation correctness<br>• Abstention accuracy |
| 4 | [Retrieval Improvement](curriculum/03-rag/README.md) | 8 | • Keyword search, vector search, hybrid retrieval, metadata filters, query rewriting, and reranking<br>• Offline retrieval experiments and error slicing | A hybrid retrieval pipeline with a reranking experiment. | • The improved pipeline beats the Week 3 baseline on the same eval set<br>• Trade-offs in quality, latency, and cost are documented | • Recall lift<br>• NDCG or MRR lift<br>• Retrieval latency |
| 5 | [Tools and Deterministic Workflows](curriculum/04-tools-and-workflows/README.md) | 8 | • Function calling, tool schemas, MCP concepts, validation, idempotency, retries, and compensating actions<br>• When normal code is better than an agent loop | A tool registry and a deterministic multi-step workflow. | • Tool selection and arguments are evaluated separately from final response quality<br>• Write operations are idempotent and protected by approval gates | • Tool-selection accuracy<br>• Argument accuracy<br>• Tool execution success rate |
| 6 | [Agents, State, and Memory](curriculum/05-agents-and-memory/README.md) | 8 | • Agent loops, stopping conditions, planning, reflection, checkpoints, short-term state, and long-term memory<br>• Human-in-the-loop patterns and recovery from partial failure | A stateful single-agent workflow with checkpointing and approval. | • Tasks resume after interruption<br>• Loops terminate safely and repeated tool calls are detected | • Task success rate<br>• Average steps per task<br>• Recovery success rate<br>• Loop-limit violations |
| 7 | [Evaluation-Driven Development](curriculum/06-evals/README.md) | 10 | • Golden datasets, code graders, LLM-as-judge, trajectory evaluation, human calibration, and error analysis<br>• Request, environment, stopping criteria, and scorer as a benchmark tuple | A repeatable evaluation harness with at least 50 representative cases. | • Every significant system change produces a comparable evaluation report<br>• Failure modes are categorized and linked to the next engineering action | • Task success rate<br>• Pass at k and pass power k where relevant<br>• Judge-human agreement<br>• Regression count |
| 8 | [Safety, Permissions, and Adversarial Inputs](curriculum/07-safety/README.md) | 8 | • Direct and indirect prompt injection, data leakage, least privilege, sandboxing, approvals, and audit logs<br>• Threat modeling for tools and retrieved content | A permission policy and adversarial test suite. | • Untrusted content cannot authorize tool use<br>• Sensitive or destructive actions require explicit approval | • Unauthorized action rate<br>• Attack success rate on the local red-team set<br>• Approval bypass count |
| 9 | [Production and LLMOps](curriculum/08-production/README.md) | 8 | • Tracing, monitoring, budgets, caches, rate limits, fallbacks, incident response, and feedback collection<br>• Versioning prompts, data, models, tools, and eval sets | A deployed service with observability and a regression gate. | • Operators can diagnose a failed task from traces<br>• The service respects latency and cost budgets under expected load | • Availability<br>• p50 and p95 latency<br>• Cost per successful task<br>• Fallback rate |
| 10 | [Coding Agents and Sandboxed Execution](curriculum/09-coding-agents/README.md) | 8 | • Repository context, planning, file editing, command policies, test execution, diffs, and review gates<br>• Long-running task harnesses and bounded autonomy | A coding workflow that produces a tested patch inside a sandbox. | • The agent cannot modify files outside its allowed scope<br>• A patch is never merged or deployed without review | • Patch success rate<br>• Test-pass rate<br>• Files changed per task<br>• Policy violation count |
| 11 | [Shape the Build](curriculum/10-shaping-the-build/README.md) | 6 | • Task decomposition, user value, AI-versus-code boundaries, rapid prototypes, and risk-adjusted iteration<br>• Architecture decision records and evidence-backed prioritization | A revised product spec and a set of architecture decisions based on eval evidence. | • Features are prioritized by user value, failure risk, and measurable impact<br>• The team can explain why each AI component exists | • Acceptance-criteria coverage<br>• Decisions supported by evidence |
| 12 | [Capstone and Career Evidence](capstone/README.md) | 12 | • Technical storytelling, reproducibility, demo design, and portfolio evidence<br>• Translating system results into honest resume bullets | A public demo, repository, architecture diagram, eval report, security model, and short English walkthrough. | • Another engineer can reproduce the system and its evaluation<br>• Claims in the demo and resume are backed by artifacts or metrics | • Reproducibility checklist completion<br>• Eval coverage<br>• Demo success rate |

## Completion evidence

A learner who completes the roadmap should be able to show:

- one deployed AI system rather than a collection of disconnected notebooks;
- a representative eval dataset and repeatable runner;
- baseline-versus-candidate experiments;
- quality, cost, latency, reliability, and safety metrics;
- a threat model and approval boundaries;
- architecture decisions and an error taxonomy;
- a concise technical demo and honest résumé claims.

## Optional foundations

See the [skill matrix](docs/skill-matrix.md#optional-foundations-track) for parallel software and machine-learning foundations.
