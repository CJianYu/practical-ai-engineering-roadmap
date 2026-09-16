.PHONY: setup render validate test lint all

setup:
	python -m pip install -r requirements-dev.txt

render:
	python scripts/render_roadmap.py

validate: render
	python scripts/validate_roadmap.py
	python -m pytest -q
	ruff check labs scripts tests
	git diff --exit-code ROADMAP.md

test:
	python -m pytest -q

lint:
	ruff check labs scripts tests

all: validate
