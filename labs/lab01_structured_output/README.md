# Lab 01 — Structured Output as a Software Boundary

A model response is untrusted input. This lab uses a provider-neutral adapter and a Pydantic schema so invalid output cannot silently enter the application.

## Run

From the repository root:

```bash
pip install -r requirements-dev.txt
python -m labs.lab01_structured_output.app
pytest tests/test_structured_output.py -q
```

## What to observe

- Business logic depends on `StructuredOutputProvider`, not a vendor SDK.
- `SupportTicket` forbids extra fields and constrains enums, lengths, and confidence.
- Invalid provider output raises a validation error.
- The mock is deterministic so the learning boundary can be tested without an API key.

## Extend it

1. Add an adapter using the official SDK of your chosen provider.
2. Record model, prompt version, tokens, latency, retries, and cost.
3. Add retry logic only for errors that are safe and useful to retry.
4. Create 20 labeled tickets and measure category accuracy and schema-valid rate.
5. Compare a fast model and a stronger model on cost per correct classification.

## Exit criteria

- [ ] Invalid fields fail closed.
- [ ] Provider-specific code is isolated in an adapter.
- [ ] Unit tests do not require network access.
- [ ] Production calls would expose quality, latency, and cost metrics.
