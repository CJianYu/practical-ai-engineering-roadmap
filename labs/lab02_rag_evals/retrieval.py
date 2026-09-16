from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

TOKEN_RE = re.compile(r"[a-z0-9]+")


@dataclass(frozen=True)
class Document:
    id: str
    title: str
    text: str


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


def load_documents(path: Path) -> list[Document]:
    documents: list[Document] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            documents.append(Document(**row))
    return documents


def score(query: str, document: Document) -> float:
    """Simple lexical baseline with term frequency and title boost."""

    query_terms = Counter(tokenize(query))
    body_terms = Counter(tokenize(document.text))
    title_terms = Counter(tokenize(document.title))

    body_overlap = sum(min(count, body_terms[term]) for term, count in query_terms.items())
    title_overlap = sum(min(count, title_terms[term]) for term, count in query_terms.items())
    return float(body_overlap + (2 * title_overlap))


def search(query: str, documents: Iterable[Document], k: int = 3) -> list[Document]:
    if k < 1:
        raise ValueError("k must be at least 1")

    ranked = sorted(documents, key=lambda doc: (-score(query, doc), doc.id))
    return ranked[:k]
