#!/usr/bin/env python3
"""Guard unresolved predicate consumers against accidental expansion producers."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs/MACHINE_CANONICAL_GRAPH_01.json"
INVENTORY = ROOT / "docs/CANONICAL_PRODUCER_INVENTORY_01.md"

REQUIRED_OPEN = {
    "pred.guild_labor_tension",
    "pred.information_pressure_high",
}
EXPANSION = {f"E{i}" for i in range(273, 278)}


def main() -> int:
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    inventory = INVENTORY.read_text(encoding="utf-8")
    errors: list[str] = []

    scope = graph["scope"]
    if scope["first_event"] != 1 or scope["last_event"] != 272:
        errors.append("production scope is not exactly E01-E272")

    if not all(item in inventory for item in REQUIRED_OPEN):
        errors.append("required frozen-scope unresolved predicates are not documented")

    # These predicates are explicitly unresolved in the frozen catalog.  The
    # validator rejects any attempt to close them using expansion-only nodes.
    for event_id in sorted(EXPANSION):
        if event_id in inventory and "expansion" not in inventory.lower():
            errors.append(f"expansion event {event_id} appears without expansion quarantine")

    # The machine graph must retain these predicates as unresolved blockers.
    blockers = set(graph.get("known_not_yet_verified", []))
    for predicate in REQUIRED_OPEN:
        if predicate not in blockers:
            errors.append(f"machine graph no longer records blocker: {predicate}")

    print(f"FROZEN_PREDICATE_BLOCKERS: {'PASS' if not errors else 'FAIL'}")
    print(f"required_open={len(REQUIRED_OPEN)}")
    print(f"errors={len(errors)}")
    for error in errors:
        print(f"- {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
