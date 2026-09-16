# Lab 02 — Eval-driven Retrieval Before Generation

This lab deliberately starts without embeddings or an LLM. It creates a deterministic lexical baseline, then measures retrieval quality with Recall@k and Mean Reciprocal Rank (MRR).

A simple measured baseline is more useful than an impressive RAG demo with no idea why it succeeds or fails.

## Run

From the repository root:

```bash
python -m labs.lab02_rag_evals.evals
pytest tests/test_rag_evals.py -q
```

## Files

- `data/docs.jsonl` — small document corpus;
- `data/eval_cases.jsonl` — labeled queries and relevant document IDs;
- `retrieval.py` — framework-free lexical retrieval;
- `evals.py` — Recall@k, MRR, and evaluation runner.

## Experiments

Keep the same eval cases and change one variable at a time:

1. Add stop-word handling or stemming.
2. Add BM25.
3. Add embeddings.
4. Combine lexical and vector scores.
5. Add a reranker.
6. Slice results by query type.

For every experiment, record quality, latency, and cost. A more complex retriever is only better when the measured trade-off supports the product.

## Exit criteria

- [ ] The retrieval dataset is separate from implementation code.
- [ ] The same cases compare baseline and candidate systems.
- [ ] Retrieval failure is diagnosed before generation is blamed.
- [ ] Improvement claims include both metrics and representative failures.
