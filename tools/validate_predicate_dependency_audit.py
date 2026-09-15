#!/usr/bin/env python3
"""Validate the conservative predicate dependency/cycle boundary contract."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "MACHINE_PREDICATE_DEPENDENCY_AUDIT_01.json"
OUT = ROOT / "docs" / "MACHINE_PREDICATE_DEPENDENCY_VALIDATION_01.json"

EXPECTED = {
    "pred.guild_influence_strong": "OPEN",
    "pred.systemic_explanation_verified": "OPEN",
    "pred.coalition_cooperation": "OPEN",
    "pred.constitutional_prepared_strong": "OPEN",
    "pred.budget_reform": "SOURCE_CLOSED_RUNTIME_OPEN",
    "pred.final_charter_prerequisites": "OPEN_BLOCKED",
    "pred.food_stable": "OPEN_BLOCKED",
    "pred.border_crisis": "SOURCE_CLOSED_RUNTIME_OPEN",
}

REQUIRED_RULES = {
    "consumer_cannot_manufacture_prerequisite",
    "composite_predicates_require_explicit_component_evidence",
    "ordinary_history_is_not_replay_meta",
    "E33_E34_are_canonical_production_events",
    "E273_E277_excluded",
}


def main() -> int:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    errors: list[str] = []
    predicates = contract.get("predicates", {})
    checked: dict[str, dict[str, object]] = {}

    for key, expected in EXPECTED.items():
        actual = predicates.get(key)
        ok = actual == expected
        checked[key] = {"expected": expected, "actual": actual, "ok": ok}
        if not ok:
            errors.append(f"{key}: expected {expected!r}, got {actual!r}")

    rules = set(contract.get("rules", []))
    for required in sorted(REQUIRED_RULES - rules):
        errors.append(f"missing hard rule: {required}")

    if contract.get("replay_meta_inventory_closed") is not False:
        errors.append("replay meta inventory must remain open")
    if contract.get("fresh_run_reachability_verified") is not False:
        errors.append("fresh-run reachability must remain unverified")
    if contract.get("runtime_verified") is not False:
        errors.append("runtime verification must remain false")

    result = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.predicate_dependency_audit_validation",
        "readiness": "PASS_CONSERVATIVE_SCREEN" if not errors else "FAIL",
        "checked": checked,
        "errors": errors,
        "runtime_verified": False,
        "reachability_verified": False,
        "replay_meta_inventory_closed": False,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": result["readiness"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
