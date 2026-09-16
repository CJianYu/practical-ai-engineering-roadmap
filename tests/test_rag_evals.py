from pathlib import Path

from labs.lab02_rag_evals.evals import load_cases, run_evaluation
from labs.lab02_rag_evals.retrieval import load_documents, search

DATA = Path("labs/lab02_rag_evals/data")


def test_retrieves_pricing_document() -> None:
    documents = load_documents(DATA / "docs.jsonl")
    result = search("How many generations are in the Starter plan?", documents, k=1)
    assert result[0].id == "pricing"


def test_baseline_metrics_are_reproducible() -> None:
    documents = load_documents(DATA / "docs.jsonl")
    cases = load_cases(DATA / "eval_cases.jsonl")
    metrics = run_evaluation(documents, cases, k=3)
    assert metrics["case_count"] == 6.0
    assert metrics["recall@3"] >= 0.9
    assert metrics["mrr"] >= 0.8
