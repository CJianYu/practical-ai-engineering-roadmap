# 03 — Retrieval-Augmented Generation

> **Goal:** Ground model behavior in retrievable evidence and diagnose retrieval separately from generation.

## Learn

- Ingestion, cleaning, chunking, metadata, embeddings, indexing, retrieval, context assembly, and citations.
- Keyword, vector, and hybrid search; metadata filters; query rewriting; reranking.
- Retrieval metrics such as Recall@k, MRR, and NDCG.
- Abstention and freshness: what to do when evidence is missing or stale.

## Build

- Complete `labs/lab02_rag_evals` before adding a generation model.
- Build an ingestion pipeline that preserves source, title, timestamp, and access metadata.
- Compare a baseline retriever with one improvement on the same labeled set.

## Prove

- You can identify whether a bad answer came from retrieval, context assembly, or generation.
- Answers cite valid source chunks and abstain when evidence is insufficient.
- Retrieval improvements are supported by an offline experiment, not anecdotes.

## Explain / interview prompts

- Why can fixed-size chunking fail?
- When is hybrid search useful?
- How would you keep an index fresh and permission-aware?

## Exit criteria

- [ ] A runnable artifact exists.
- [ ] A representative eval set exists.
- [ ] At least one failure mode is documented.
- [ ] Quality, latency, cost, and safety implications are considered.
- [ ] You can explain one design trade-off without relying on framework marketing language.

## Resources

- [DeepLearning.AI — Retrieval Augmented Generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation)
- [Stanford CS329Z](https://cs329z.stanford.edu/)
- [Lab 02](../../labs/lab02_rag_evals/README.md)

[← Back to roadmap](../../ROADMAP.md)
