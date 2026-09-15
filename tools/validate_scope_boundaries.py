#!/usr/bin/env python3
"""Validate frozen production/replay/ending scope boundaries.

This is intentionally a boundary validator, not a reachability validator. It
fails closed if excluded expansion events enter production machine contracts,
if ending/replay candidate queues drift from their frozen ranges, or if the
canonical graph scope is inconsistent with PROJECT_STATE expectations.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
TRIAGE = ROOT / "docs" / "MACHINE_CANDIDATE_TRIAGE_01.json"
OUT = ROOT / "docs" / "MACHINE_SCOPE_BOUNDARY_AUDIT_01.json"

EXPECTED_SCOPE = {f"E{i:02d}" for i in range(1, 273)}
EXPECTED_EXCLUDED = {f"E{i:02d}" for i in range(273, 278)}
EXPECTED_ENDINGS = {f"E{i:02d}" for i in range(265, 271)}
EXPECTED_REPLAY = {f"E{i:02d}" for i in range(247, 251)}


def event_id(value: str) -> bool:
    return isinstance(value, str) and len(value) >= 3 and value[0] == "E" and value[1:].isdigit()


def main() -> int:
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    triage = json.loads(TRIAGE.read_text(encoding="utf-8"))

    scope = graph.get("scope", {})
    first_event = scope.get("first_event")
    last_event = scope.get("last_event")
    excluded = set(scope.get("excluded_events", []))
    errors: list[str] = []

    if first_event != 1 or last_event != 272:
        errors.append(f"canonical scope drift: expected E01-E272, got E{first_event}-E{last_event}")
    if excluded != EXPECTED_EXCLUDED:
        errors.append(f"excluded scope drift: expected {sorted(EXPECTED_EXCLUDED)}, got {sorted(excluded)}")
    if EXPECTED_SCOPE & excluded:
        errors.append("production scope overlaps excluded expansion scope")

    for section, values in {
        "source_closed_producers": [x.get("event") for x in graph.get("source_closed_producers", [])],
        "delayed_consumers": [x.get("consumer") for x in graph.get("delayed_consumers", [])],
    }.items():
        bad = sorted(v for v in values if v and v not in EXPECTED_SCOPE)
        if bad:
            errors.append(f"{section} contains out-of-scope production events: {bad}")

    queues = triage.get("queues", {})
    ending = set(queues.get("ending_candidates", []))
    replay = set(queues.get("replay_candidates", []))
    if ending != EXPECTED_ENDINGS:
        errors.append(f"ending candidate boundary drift: {sorted(ending)}")
    if replay != EXPECTED_REPLAY:
        errors.append(f"replay candidate boundary drift: {sorted(replay)}")

    for queue_name, values in queues.items():
        if not isinstance(values, list):
            errors.append(f"queue {queue_name} is not a list")
            continue
        malformed = sorted(v for v in values if not event_id(v))
        excluded_found = sorted(v for v in values if v in EXPECTED_EXCLUDED)
        if malformed:
            errors.append(f"queue {queue_name} has malformed event IDs: {malformed}")
        if excluded_found:
            errors.append(f"queue {queue_name} contains excluded events: {excluded_found}")

    report = {
        "schema_version": "1.0",
        "scope": "E01-E272",
        "excluded_scope": sorted(EXPECTED_EXCLUDED),
        "ending_candidate_boundary": sorted(EXPECTED_ENDINGS),
        "replay_candidate_boundary": sorted(EXPECTED_REPLAY),
        "reachability_proven": False,
        "semantic_orphans_proven": False,
        "errors": errors,
        "status": "GREEN" if not errors else "RED",
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
