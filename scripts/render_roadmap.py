from __future__ import annotations

from typing import Any

from validate_roadmap import ROOT, load_roadmap, validate

OUTPUT_PATH = ROOT / "ROADMAP.md"


def escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render(data: dict[str, Any]) -> str:
    errors = validate(data)
    if errors:
        raise ValueError("; ".join(errors))

    lines = [
        "# 12-Week Practical AI Engineering Roadmap",
        "",
        (
            "> Generated from [`roadmap.yaml`](roadmap.yaml). "
            "Edit the YAML, then run `make render`."
        ),
        "",
        f"**Audience:** {data['primary_audience']}",
        "",
        (
            f"**Default pace:** {data['duration_weeks']} weeks, approximately "
            f"{data['hours_per_week']} hours per week, plus Week 0 orientation."
        ),
        "",
        "## Roadmap",
        "",
        "| Week | Focus | Hours | Learn | Build | Prove | Metrics |",
        "|---:|---|---:|---|---|---|---|",
    ]

    for week in data["weeks"]:
        module_link = f"[{week['title']}]({week['module']})"
        learn = "<br>".join(f"• {item}" for item in week["learn"])
        prove = "<br>".join(f"• {item}" for item in week["prove"])
        metrics = "<br>".join(f"• {item}" for item in week["metrics"])
        cells = [
            str(week["week"]),
            module_link,
            str(week["estimated_hours"]),
            learn,
            week["build"],
            prove,
            metrics,
        ]
        lines.append("| " + " | ".join(escape_cell(cell) for cell in cells) + " |")

    lines.extend(
        [
            "",
            "## Completion evidence",
            "",
            "A learner who completes the roadmap should be able to show:",
            "",
            "- one deployed AI system rather than a collection of disconnected notebooks;",
            "- a representative eval dataset and repeatable runner;",
            "- baseline-versus-candidate experiments;",
            "- quality, cost, latency, reliability, and safety metrics;",
            "- a threat model and approval boundaries;",
            "- architecture decisions and an error taxonomy;",
            "- a concise technical demo and honest résumé claims.",
            "",
            "## Optional foundations",
            "",
            (
                "See the [skill matrix](docs/skill-matrix.md#optional-foundations-track) "
                "for parallel software and machine-learning foundations."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    OUTPUT_PATH.write_text(render(load_roadmap()), encoding="utf-8")
    print(f"wrote {OUTPUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
