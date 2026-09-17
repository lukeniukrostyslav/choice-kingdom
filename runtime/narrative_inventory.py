from __future__ import annotations

import json
from pathlib import Path

from .catalog import AuthoredCatalog


def build_narrative_key_inventory(root: Path) -> dict:
    catalog = AuthoredCatalog.from_repository(root)
    events = []
    choice_count = 0
    for event in catalog.events.values():
        choices = []
        for choice in event.choices:
            choice_count += 1
            choices.append({
                "choice_id": choice.choice_id,
                "label": choice.label,
                "text": choice.text,
                "body": choice.body,
            })
        events.append({
            "event_id": event.event_id,
            "title": event.title,
            "trigger": event.trigger,
            "choices": choices,
        })
    return {
        "schema_version": "1.0",
        "locale_neutral": True,
        "event_count": len(events),
        "choice_count": choice_count,
        "events": events,
    }


def write_narrative_key_inventory(root: Path, output: Path) -> None:
    output.write_text(
        json.dumps(build_narrative_key_inventory(root), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
