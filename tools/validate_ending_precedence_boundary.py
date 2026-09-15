#!/usr/bin/env python3
"""Validate the conservative ending-precedence boundary contract."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "MACHINE_ENDING_PRECEDENCE_BOUNDARY_01.json"

REQUIRED_FAMILIES = {
    "Steward",
    "Iron Crown",
    "Golden Compact",
    "People's Charter",
    "Broken Diadem",
    "Quiet Throne",
    "Second Founder",
}
REQUIRED_RULE_FRAGMENTS = (
    "Second Founder",
    "People's Charter",
    "Iron Crown",
    "Golden Compact",
    "Steward",
    "Broken Diadem",
    "Quiet Throne",
    "E267-E270",
    "Replay/meta",
    "E33/E34",
)
REQUIRED_OPEN_GATES = [
    "exact positive prerequisite set per family",
    "exact negative blocker set per family",
    "tie-break order when multiple families qualify",
    "fresh-run evaluation order",
    "replay evaluation order",
    "deterministic terminal selection",
]


def main() -> int:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    errors: list[str] = []
    if set(data.get("families", [])) != REQUIRED_FAMILIES:
        errors.append("ending family inventory mismatch")
    rules = data.get("rules", [])
    for fragment in REQUIRED_RULE_FRAGMENTS:
        if not any(fragment in rule for rule in rules):
            errors.append(f"missing boundary rule: {fragment}")
    if data.get("required_runtime_resolution", []) != REQUIRED_OPEN_GATES:
        errors.append("required runtime resolution gate list mismatch")
    if data.get("precedence_verified") is not False:
        errors.append("precedence_verified must remain false")
    if data.get("fresh_run_reachability_verified") is not False:
        errors.append("fresh_run_reachability_verified must remain false")
    if data.get("replay_reachability_verified") is not False:
        errors.append("replay_reachability_verified must remain false")
    if data.get("decision_engine_promotion_authorized") is not False:
        errors.append("decision_engine_promotion_authorized must remain false")

    print(json.dumps({"status": "PASS" if not errors else "FAIL", "errors": errors}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
