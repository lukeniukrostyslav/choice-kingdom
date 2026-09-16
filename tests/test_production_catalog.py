from __future__ import annotations

import json
from pathlib import Path

from tools.compile_production_catalog import OUT, compile_catalog

ROOT = Path(__file__).resolve().parents[1]


def test_committed_production_catalog_matches_authored_projection() -> None:
    actual = json.loads(OUT.read_text(encoding="utf-8"))
    assert actual == compile_catalog()
    assert actual["event_count"] == 272
    assert sum(len(event["choices"]) for event in actual["events"]) == 520
    assert sum(not event["choices"] for event in actual["events"]) == 13
    assert actual["scope"]["excluded_events"] == ["E273", "E274", "E275", "E276", "E277"]
