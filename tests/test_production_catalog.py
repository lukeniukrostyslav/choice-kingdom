from __future__ import annotations

from tools.compile_production_catalog import compile_catalog


def test_production_catalog_projection_is_deterministic_and_complete() -> None:
    first = compile_catalog()
    second = compile_catalog()
    assert first == second
    assert first["event_count"] == 272
    assert sum(len(event["choices"]) for event in first["events"]) == 520
    assert sum(not event["choices"] for event in first["events"]) == 13
    assert first["scope"]["excluded_events"] == ["E273", "E274", "E275", "E276", "E277"]
