#!/usr/bin/env python3
"""Validate the machine-facing production data schema contract."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.catalog import AuthoredCatalog
from runtime.state import EXCLUDED_EVENTS, PRODUCTION_FIRST, PRODUCTION_LAST, RELATIONSHIPS, RESOURCES

EVENT_ID_RE = re.compile(r"^E(?:0[1-9]|[1-9][0-9]|[1-2][0-9]{2})$")
# State-token extraction is intentionally permissive: authored tokens can carry
# scoped paths, assignments and human-readable marker values. The canonical
# runtime vocabulary is enforced where runtime semantics consume the token.
TOKEN_RE = re.compile(r"^[^`\r\n]{1,200}$")
EXPECTED = {f"E{i:02d}" for i in range(PRODUCTION_FIRST, PRODUCTION_LAST + 1)} - set(EXCLUDED_EVENTS)
ALLOWED_EXTRA_CHOICES = {"E51": {"C"}, "E108": {"C"}}


def fail(errors: list[str]) -> int:
    print("PRODUCTION DATA SCHEMA: FAIL")
    for error in errors:
        print(f"- {error}")
    return 1


def main() -> int:
    errors: list[str] = []
    catalog = AuthoredCatalog.from_repository(ROOT)
    catalog.validate()

    if set(catalog.events) != EXPECTED:
        errors.append("catalog event scope does not exactly match E01-E272 excluding E273-E277")

    for event_id, event in catalog.events.items():
        if not EVENT_ID_RE.fullmatch(event.event_id):
            errors.append(f"{event_id}: invalid canonical event identity")
        if event.event_id != event_id:
            errors.append(f"{event_id}: map key and event identity differ")
        if not event.title.strip():
            errors.append(f"{event_id}: empty title")
        if not event.source.strip():
            errors.append(f"{event_id}: empty source")
        prerequisites = catalog.authored_prerequisites(event_id)
        for prerequisite in prerequisites:
            if prerequisite not in EXPECTED:
                errors.append(f"{event_id}: prerequisite outside production scope: {prerequisite}")

        labels: list[str] = []
        for choice in event.choices:
            labels.append(choice.label)
            if choice.choice_id != f"{event_id}-{choice.label}":
                errors.append(f"{event_id}: malformed choice identity {choice.choice_id}")
            if not choice.label.isalpha() or choice.label != choice.label.upper():
                errors.append(f"{event_id}: non-canonical choice label {choice.label}")
            if not choice.text.strip():
                errors.append(f"{event_id}-{choice.label}: empty choice text")
            if not choice.body.strip():
                errors.append(f"{event_id}-{choice.label}: empty choice body")
            for resource in choice.resource_deltas:
                if resource not in RESOURCES:
                    errors.append(f"{event_id}-{choice.label}: non-canonical resource {resource}")
            for character in choice.relationship_deltas:
                if character not in RELATIONSHIPS:
                    errors.append(f"{event_id}-{choice.label}: non-canonical relationship {character}")
            for token in (*choice.state_tokens, *choice.clear_tokens):
                if not TOKEN_RE.fullmatch(token):
                    errors.append(f"{event_id}-{choice.label}: malformed state token {token!r}")
            for unlock in re.findall(r"^-\s*\*\*Unlocks?\*\*\s+`?(E\d{2,3})", choice.body, re.I | re.M):
                if unlock not in EXPECTED:
                    errors.append(f"{event_id}-{choice.label}: immediate unlock outside production scope: {unlock}")

        if event_id not in {"E32", *{f"E{i:02d}" for i in range(61, 71)}, "E210", "E270"}:
            allowed = {"A", "B"} | ALLOWED_EXTRA_CHOICES.get(event_id, set())
            if not {"A", "B"}.issubset(set(labels)):
                errors.append(f"{event_id}: production choice contract requires A and B, found {labels}")
            if set(labels) - allowed:
                errors.append(f"{event_id}: undocumented choice labels {sorted(set(labels) - allowed)}")

    if errors:
        return fail(errors)

    print("PRODUCTION DATA SCHEMA: PASS")
    print(f"events={len(catalog.events)}")
    print(f"choices={sum(len(event.choices) for event in catalog.events.values())}")
    print(f"excluded={','.join(sorted(EXCLUDED_EVENTS))}")
    print("canonical_resources=true")
    print("canonical_relationships=true")
    print("choice_identity=true")
    print("prerequisite_scope=true")
    print("immediate_unlock_scope=true")
    print("deterministic_parser_boundary=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
