from __future__ import annotations

from .provider import KeywordMockProvider, StructuredOutputProvider
from .schemas import SupportTicket


def classify_ticket(text: str, provider: StructuredOutputProvider) -> SupportTicket:
    """Classify text and validate the provider response at the boundary."""

    if not text.strip():
        raise ValueError("ticket text must not be empty")

    raw = provider.generate_ticket(text)
    return SupportTicket.model_validate(raw)


def main() -> None:
    provider = KeywordMockProvider()
    ticket = classify_ticket(
        "I was charged twice after generation failed. Please help.", provider
    )
    print(ticket.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
