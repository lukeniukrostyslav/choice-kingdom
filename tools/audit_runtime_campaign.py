#!/usr/bin/env python3
"""Run a deterministic production-catalog runtime traversal diagnostic.

This tool is deliberately an audit, not a semantic inference engine. It uses only
currently implemented DecisionEngine trigger/routing semantics and records where
runtime execution stops. It must never promote prose trigger guesses into gameplay.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from runtime.engine import DecisionEngine
from runtime.state import GameState

EXPECTED = {f"E{i:02d}" for i in range(1, 273)}
EXCLUDED = {f"E{i:02d}" for i in range(273, 278)}
IMMEDIATE = re.compile(r"^-\s*\*\*Unlocks?\*\*\s+`?(E\d{2,3})", re.I | re.M)


# Deterministic baseline only: this is a measurement gate, not gameplay policy.
def choose_event(engine: DecisionEngine, state: GameState):
    """Prefer the lowest event id, matching the stable baseline traversal."""
    candidates = [event for event in engine.available(state) if event.choices]
    if not candidates:
        return None
    return min(candidates, key=lambda event: int(event.event_id[1:]))


def main() -> int:
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("runtime-campaign-audit")
    visited: list[str] = []
    execution_errors: list[dict[str, str]] = []
    steps = 0

    while steps < 1000:
        event = choose_event(engine, state)
        if event is None:
            break
        choice = event.choices[0]
        try:
            result = engine.execute(state, event.event_id, choice.choice_id)
        except Exception as exc:  # diagnostic boundary: preserve exact failure text
            execution_errors.append({
                "event": event.event_id,
                "choice": choice.choice_id,
                "error": str(exc),
            })
            break
        visited.append(result.event_id)
        steps += 1

    visited_set = set(visited)
    missing = sorted(EXPECTED - visited_set, key=lambda value: int(value[1:]))
    blocked_triggers = [
        {"event": event_id, "trigger": engine.event(event_id).trigger}
        for event_id in missing
        if engine.event(event_id).trigger
    ]
    available_at_stop = [event.event_id for event in engine.available(state) if event.choices]
    immediate_routes_seen = sorted({
        target
        for event_id in visited_set
        for choice in engine.event(event_id).choices
        for target in IMMEDIATE.findall(choice.body)
    }, key=lambda value: int(value[1:]))

    report = {
        "schema_version": "1.0",
        "scope": "E01-E272",
        "excluded_events": sorted(EXCLUDED),
        "audit_only": True,
        "semantic_boundary": (
            "This report measures only currently implemented runtime semantics. "
            "Missing events are not declared impossible; unresolved prose predicates, "
            "special convergence nodes and production trigger normalization remain open."
        ),
        "steps": steps,
        "visited_event_count": len(visited_set),
        "visited_events": sorted(visited_set, key=lambda value: int(value[1:])),
        "missing_event_count": len(missing),
        "missing_events": missing,
        "available_choices_at_stop": available_at_stop,
        "execution_errors": execution_errors,
        "immediate_routes_seen": immediate_routes_seen,
        "blocked_trigger_count": len(blocked_triggers),
        "blocked_triggers": blocked_triggers,
        "current_state": state.snapshot(),
    }
    out = ROOT / "docs" / "MACHINE_RUNTIME_CAMPAIGN_AUDIT_01.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PASS",
        "steps": steps,
        "visited_event_count": len(visited_set),
        "missing_event_count": len(missing),
        "blocked_trigger_count": len(blocked_triggers),
        "execution_errors": len(execution_errors),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
