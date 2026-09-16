from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from .retrieval import Document, load_documents, search


@dataclass(frozen=True)
class EvalCase:
    id: str
    query: str
    relevant_doc_ids: tuple[str, ...]


def load_cases(path: Path) -> list[EvalCase]:
    cases: list[EvalCase] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            cases.append(
                EvalCase(
                    id=row["id"],
                    query=row["query"],
                    relevant_doc_ids=tuple(row["relevant_doc_ids"]),
                )
            )
    return cases


def recall_at_k(retrieved_ids: list[str], relevant_ids: tuple[str, ...]) -> float:
    relevant = set(relevant_ids)
    if not relevant:
        return 1.0
    return len(relevant.intersection(retrieved_ids)) / len(relevant)


def reciprocal_rank(retrieved_ids: list[str], relevant_ids: tuple[str, ...]) -> float:
    relevant = set(relevant_ids)
    for rank, doc_id in enumerate(retrieved_ids, start=1):
        if doc_id in relevant:
            return 1.0 / rank
    return 0.0


def run_evaluation(
    documents: list[Document], cases: list[EvalCase], k: int = 3
) -> dict[str, float]:
    recalls: list[float] = []
    reciprocal_ranks: list[float] = []

    for case in cases:
        retrieved_ids = [doc.id for doc in search(case.query, documents, k=k)]
        recalls.append(recall_at_k(retrieved_ids, case.relevant_doc_ids))
        reciprocal_ranks.append(reciprocal_rank(retrieved_ids, case.relevant_doc_ids))

    return {
        f"recall@{k}": sum(recalls) / len(recalls),
        "mrr": sum(reciprocal_ranks) / len(reciprocal_ranks),
        "case_count": float(len(cases)),
    }


def main() -> None:
    data_dir = Path(__file__).parent / "data"
    documents = load_documents(data_dir / "docs.jsonl")
    cases = load_cases(data_dir / "eval_cases.jsonl")
    metrics = run_evaluation(documents, cases, k=3)
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
