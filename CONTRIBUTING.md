# Contributing

Thank you for helping build a practical, evidence-driven learning path.

## Contribution principles

1. Keep the target learner clear: an existing software engineer becoming an Applied AI Engineer.
2. Prefer runnable artifacts, evaluations, and production evidence over broad link lists.
3. Make one scoped change per pull request.
4. Do not copy proprietary course notes, assignment solutions, private datasets, or employer code.
5. Use synthetic or explicitly shareable data.
6. Explain when a new resource should be used and what gap it fills.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
make validate
```

## Updating the roadmap

`roadmap.yaml` is the source of truth.

1. Edit `roadmap.yaml`.
2. Run `make render`.
3. Commit both `roadmap.yaml` and `ROADMAP.md`.
4. Run `make validate`.

## Adding a lab

A lab should include:

- a focused learning objective;
- a runnable implementation;
- deterministic local tests where possible;
- an evaluation or measurable output;
- a README with extension experiments;
- no mandatory paid API for the basic test path.

## Adding a resource

Open a Resource Suggestion issue first when the addition is substantial. Include:

- the exact module;
- the learner gap;
- why the source is authoritative or reproducible;
- whether it replaces or complements an existing item.

## Pull request review

Maintainers review for correctness, learner value, reproducibility, scope, licensing, and maintenance cost. A popular tool is not automatically a necessary curriculum dependency.
