#!/usr/bin/env python3
"""Validate the frozen authored E01-E272 production content surface.

This gate is intentionally content-structural. It verifies that the frozen
catalog is complete, internally consistent, and mechanically consumable without
inventing gameplay semantics that belong to the routing/runtime gates.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.catalog import AuthoredCatalog  # noqa: E402
from runtime.state import EXCLUDED_EVENTS, PRODUCTION_FIRST, PRODUCTION_LAST, RELATIONSHIPS, RESOURCES  # noqa: E402

EXPECTED_NO_CHOICE_EVENTS = 13
EXPECTED_CHOICES = 520


def validate() -> list[str]:
    errors: list[str] = []
    catalog = AuthoredCatalog.from_repository(ROOT)
    catalog.validate()

    expected_ids = [f"E{i:02d}" for i in range(PRODUCTION_FIRST, PRODUCTION_LAST + 1)]
    actual_ids = list(catalog.events)
    if actual_ids != expected_ids:
        errors.append("catalog event ids are not the frozen contiguous E01-E272 sequence")

    if any(event_id in catalog.events for event_id in EXCLUDED_EVENTS):
        errors.append("excluded E273-E277 entered the production catalog")

    seen_choice_ids: set[str] = set()
    choice_count = 0
    no_choice_count = 0
    for event_id, event in catalog.events.items():
        if not event.title.strip():
            errors.append(f"{event_id}: empty title")
        if not event.source.strip():
            errors.append(f"{event_id}: missing source")
        if not event.choices:
            no_choice_count += 1
            continue

        labels = [choice.label for choice in event.choices]
        expected_labels = [chr(ord("A") + index) for index in range(len(labels))]
        if labels != expected_labels:
            errors.append(f"{event_id}: choice labels must be contiguous A..N, got {labels}")

        for choice in event.choices:
            choice_count += 1
            if choice.choice_id in seen_choice_ids:
                errors.append(f"duplicate choice id: {choice.choice_id}")
            seen_choice_ids.add(choice.choice_id)
            if choice.choice_id != f"{event_id}-{choice.label}":
                errors.append(f"{event_id}: non-canonical choice id {choice.choice_id}")
            if not choice.text.strip():
                errors.append(f"{choice.choice_id}: empty choice text")
            if not choice.body.strip():
                errors.append(f"{choice.choice_id}: empty authored body")
            unknown_resources = set(choice.resource_deltas) - set(RESOURCES)
            if unknown_resources:
                errors.append(f"{choice.choice_id}: unknown resources {sorted(unknown_resources)}")
            unknown_relationships = set(choice.relationship_deltas) - set(RELATIONSHIPS)
            if unknown_relationships:
                errors.append(f"{choice.choice_id}: unknown relationships {sorted(unknown_relationships)}")
            if any(not token.strip() for token in (*choice.state_tokens, *choice.clear_tokens)):
                errors.append(f"{choice.choice_id}: empty state token")

    if choice_count != EXPECTED_CHOICES:
        errors.append(f"expected {EXPECTED_CHOICES} choices, found {choice_count}")
    if no_choice_count != EXPECTED_NO_CHOICE_EVENTS:
        errors.append(f"expected {EXPECTED_NO_CHOICE_EVENTS} no-choice nodes, found {no_choice_count}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("PRODUCTION CONTENT VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PRODUCTION CONTENT VALIDATION: PASS")
    print(f"events={PRODUCTION_LAST - PRODUCTION_FIRST + 1}")
    print(f"choices={EXPECTED_CHOICES}")
    print(f"no_choice_events={EXPECTED_NO_CHOICE_EVENTS}")
    print("scope=E01-E272")
    print("source_of_truth=authored markdown")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
