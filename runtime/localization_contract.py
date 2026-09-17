from __future__ import annotations

import json
from pathlib import Path

from .catalog import AuthoredCatalog
from .localization import SUPPORTED_LOCALES

NARRATIVE_FIELDS = ("title", "trigger", "choice.text")


def build_locale_contract(root: Path) -> dict:
    catalog = AuthoredCatalog.from_repository(root)
    events = []
    for event in catalog.events.values():
        events.append({
            "event_id": event.event_id,
            "keys": [
                f"{event.event_id}.title",
                f"{event.event_id}.trigger",
                *[f"{choice.choice_id}.text" for choice in event.choices],
            ],
        })
    keys = [key for event in events for key in event["keys"]]
    return {
        "schema_version": "1.0",
        "event_count": len(events),
        "choice_count": sum(len(event["keys"]) - 2 for event in events) // 2,
        "narrative_key_count": len(keys),
        "locales": list(SUPPORTED_LOCALES),
        "events": events,
    }


def write_locale_contract(root: Path, output: Path) -> None:
    output.write_text(
        json.dumps(build_locale_contract(root), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
