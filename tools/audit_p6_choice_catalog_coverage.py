"""Audit the production choice catalog for P6 visual-family coverage.

The audit derives its families only from the frozen authored catalog. It never
creates canonical IDs, characters, factions, or gameplay outcomes.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from runtime.catalog import AuthoredCatalog

ROOT = Path(__file__).resolve().parents[1]


def build_report(root: Path = ROOT) -> dict[str, int]:
    catalog = AuthoredCatalog.from_repository(root)
    catalog.validate()

    report = Counter()
    report["events"] = len(catalog.events)
    report["choices"] = sum(len(event.choices) for event in catalog.events.values())
    report["two_way_events"] = sum(len(event.choices) == 2 for event in catalog.events.values())
    report["three_plus_way_events"] = sum(len(event.choices) >= 3 for event in catalog.events.values())
    report["resource_delta_choices"] = sum(
        bool(choice.resource_deltas)
        for event in catalog.events.values()
        for choice in event.choices
    )
    report["relationship_delta_choices"] = sum(
        bool(choice.relationship_deltas)
        for event in catalog.events.values()
        for choice in event.choices
    )
    report["state_token_choices"] = sum(
        bool(choice.state_tokens)
        for event in catalog.events.values()
        for choice in event.choices
    )
    report["clear_token_choices"] = sum(
        bool(choice.clear_tokens)
        for event in catalog.events.values()
        for choice in event.choices
    )
    report["triggered_events"] = sum(bool(event.trigger) for event in catalog.events.values())
    return dict(report)


def main() -> None:
    for key, value in build_report().items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
