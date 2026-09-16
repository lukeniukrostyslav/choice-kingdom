#!/usr/bin/env python3
"""Compile the frozen authored catalog into a deterministic runtime-data artifact.

This compiler is deliberately mechanical: it does not infer missing gameplay
semantics. The authored markdown remains the source of truth; this JSON is a
machine-readable projection for future UI/runtime consumers.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.catalog import AuthoredCatalog
from runtime.state import EXCLUDED_EVENTS, PRODUCTION_FIRST, PRODUCTION_LAST, RELATIONSHIPS, RESOURCES

OUT = ROOT / "docs" / "MACHINE_PRODUCTION_CATALOG_01.json"
UNLOCK_RE = re.compile(r"^-\s*\*\*Unlocks?\*\*\s+`?(E\d{2,3})", re.I | re.M)


def compile_catalog() -> dict:
    catalog = AuthoredCatalog.from_repository(ROOT)
    catalog.validate()
    events = []
    for event in catalog.events.values():
        choices = []
        for choice in event.choices:
            choices.append(
                {
                    "choice_id": choice.choice_id,
                    "label": choice.label,
                    "text": choice.text,
                    "body": choice.body,
                    "resource_deltas": dict(sorted(choice.resource_deltas.items())),
                    "relationship_deltas": dict(sorted(choice.relationship_deltas.items())),
                    "state_tokens": list(choice.state_tokens),
                    "clear_tokens": list(choice.clear_tokens),
                    "immediate_unlocks": list(dict.fromkeys(UNLOCK_RE.findall(choice.body))),
                }
            )
        events.append(
            {
                "event_id": event.event_id,
                "title": event.title,
                "trigger": event.trigger,
                "authored_prerequisites": list(catalog.authored_prerequisites(event.event_id)),
                "source": event.source,
                "choices": choices,
            }
        )
    return {
        "schema": "choice-kingdom-production-catalog-1",
        "schema_version": 1,
        "source": "AuthoredCatalog.from_repository",
        "scope": {
            "first_event": PRODUCTION_FIRST,
            "last_event": PRODUCTION_LAST,
            "excluded_events": sorted(EXCLUDED_EVENTS),
        },
        "canonical_vocabulary": {
            "resources": list(RESOURCES),
            "relationships": list(RELATIONSHIPS),
        },
        "event_count": len(events),
        "events": events,
    }


def main() -> None:
    payload = compile_catalog()
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("PRODUCTION CATALOG COMPILE: PASS")
    print(f"events={payload['event_count']}")
    print(f"choices={sum(len(e['choices']) for e in payload['events'])}")
    print(f"no_choice_events={sum(not e['choices'] for e in payload['events'])}")
    print(f"output={OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
