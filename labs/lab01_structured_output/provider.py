from __future__ import annotations

from typing import Any, Protocol


class StructuredOutputProvider(Protocol):
    """Small provider-neutral contract used by the application boundary."""

    def generate_ticket(self, text: str) -> dict[str, Any]:
        ...


class KeywordMockProvider:
    """Deterministic provider for local learning and tests.

    Replace this adapter with an official model SDK in your own project. The
    application code should not need to change when the provider changes.
    """

    def generate_ticket(self, text: str) -> dict[str, Any]:
        lowered = text.lower()
        if any(word in lowered for word in ("charged", "payment", "refund", "invoice")):
            category = "billing"
            priority = "high"
        elif any(word in lowered for word in ("crash", "error", "failed", "broken")):
            category = "bug"
            priority = "high"
        elif any(word in lowered for word in ("feature", "please add", "would love")):
            category = "feature_request"
            priority = "medium"
        elif any(word in lowered for word in ("login", "password", "account")):
            category = "account"
            priority = "medium"
        else:
            category = "other"
            priority = "low"

        return {
            "category": category,
            "priority": priority,
            "summary": text.strip()[:160],
            "requires_human": category in {"billing", "account"},
            "confidence": 0.82,
        }


class StaticProvider:
    """Test helper that returns one predefined payload."""

    def __init__(self, payload: dict[str, Any]) -> None:
        self.payload = payload

    def generate_ticket(self, text: str) -> dict[str, Any]:
        del text
        return self.payload
