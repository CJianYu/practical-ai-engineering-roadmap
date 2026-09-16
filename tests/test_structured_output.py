import pytest
from pydantic import ValidationError

from labs.lab01_structured_output.app import classify_ticket
from labs.lab01_structured_output.provider import KeywordMockProvider, StaticProvider


def test_valid_ticket_is_parsed() -> None:
    ticket = classify_ticket("I was charged twice", KeywordMockProvider())
    assert ticket.category == "billing"
    assert ticket.requires_human is True


def test_extra_fields_fail_closed() -> None:
    provider = StaticProvider(
        {
            "category": "bug",
            "priority": "high",
            "summary": "Generation failed repeatedly",
            "requires_human": False,
            "confidence": 0.9,
            "unexpected": "must be rejected",
        }
    )
    with pytest.raises(ValidationError):
        classify_ticket("Generation failed", provider)


def test_invalid_confidence_fails_closed() -> None:
    provider = StaticProvider(
        {
            "category": "bug",
            "priority": "high",
            "summary": "Generation failed repeatedly",
            "requires_human": False,
            "confidence": 1.7,
        }
    )
    with pytest.raises(ValidationError):
        classify_ticket("Generation failed", provider)


def test_empty_input_is_rejected() -> None:
    with pytest.raises(ValueError):
        classify_ticket("   ", KeywordMockProvider())
