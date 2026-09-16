from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
ROADMAP_PATH = ROOT / "roadmap.yaml"
REQUIRED_WEEK_FIELDS = {
    "week",
    "id",
    "title",
    "module",
    "estimated_hours",
    "learn",
    "build",
    "prove",
    "metrics",
}


def load_roadmap(path: Path = ROADMAP_PATH) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("roadmap root must be a mapping")
    return data


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    weeks = data.get("weeks")
    if not isinstance(weeks, list) or not weeks:
        return ["weeks must be a non-empty list"]

    seen_weeks: set[int] = set()
    seen_ids: set[str] = set()

    for index, entry in enumerate(weeks):
        label = f"weeks[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{label} must be a mapping")
            continue

        missing = REQUIRED_WEEK_FIELDS.difference(entry)
        if missing:
            errors.append(f"{label} is missing: {sorted(missing)}")
            continue

        week = entry["week"]
        if week in seen_weeks:
            errors.append(f"duplicate week: {week}")
        seen_weeks.add(week)

        entry_id = entry["id"]
        if entry_id in seen_ids:
            errors.append(f"duplicate id: {entry_id}")
        seen_ids.add(entry_id)

        module_path = ROOT / entry["module"]
        if not module_path.is_file():
            errors.append(f"missing module file: {entry['module']}")

        if not isinstance(entry["learn"], list) or not entry["learn"]:
            errors.append(f"{label}.learn must be a non-empty list")
        if not isinstance(entry["prove"], list) or not entry["prove"]:
            errors.append(f"{label}.prove must be a non-empty list")
        if not isinstance(entry["metrics"], list) or not entry["metrics"]:
            errors.append(f"{label}.metrics must be a non-empty list")
        if not isinstance(entry["estimated_hours"], int) or entry["estimated_hours"] < 1:
            errors.append(f"{label}.estimated_hours must be a positive integer")

    expected_weeks = set(range(0, 13))
    if seen_weeks != expected_weeks:
        errors.append(f"week numbers must be 0..12, found {sorted(seen_weeks)}")

    return errors


def main() -> None:
    errors = validate(load_roadmap())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print("roadmap.yaml is valid")


if __name__ == "__main__":
    main()
