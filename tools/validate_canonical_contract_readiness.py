#!/usr/bin/env python3
"""Validate the bounded machine contract and emit an explicit readiness ledger.

This is a source-level gate, not a gameplay/reachability proof. It verifies that
required contract sections are present, frozen scope is respected, delayed
statuses are explicit, composite predicates expose their closure state, and hard
negatives are declared. OPEN/PARTIAL items remain visible rather than being
silently promoted to CLOSED.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
OUT = ROOT / "docs" / "MACHINE_CONTRACT_READINESS_01.json"

REQUIRED_COMPOSITES = {
    "pred.guild_influence_strong",
    "pred.systemic_explanation_verified",
    "pred.coalition_cooperation",
    "pred.constitutional_prepared_strong",
    "pred.budget_reform",
    "pred.final_charter_prerequisites",
    "pred.food_stable",
}


def main() -> int:
    data = json.loads(GRAPH.read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []

    scope = data.get("scope", {})
    if scope.get("first_event") != 1 or scope.get("last_event") != 272:
        errors.append("frozen production scope must be E01-E272")
    if set(scope.get("excluded_events", [])) != {f"E{i:02d}" for i in range(273, 278)}:
        errors.append("excluded scope must be exactly E273-E277")

    if len(data.get("source_closed_producers", [])) < 1:
        errors.append("source_closed_producers is missing or empty")
    if not data.get("delayed_consumers"):
        errors.append("delayed_consumers is missing or empty")
    if set(data.get("composite_predicates", {})) != REQUIRED_COMPOSITES:
        missing = sorted(REQUIRED_COMPOSITES - set(data.get("composite_predicates", {})))
        extra = sorted(set(data.get("composite_predicates", {})) - REQUIRED_COMPOSITES)
        if missing:
            errors.append("missing composite predicates: " + ", ".join(missing))
        if extra:
            warnings.append("additional composite predicates present: " + ", ".join(extra))
    if len(data.get("hard_negatives", [])) < 5:
        errors.append("hard-negative contract inventory is unexpectedly small")

    delayed_statuses = {}
    for row in data.get("delayed_consumers", []):
        consumer = row.get("consumer")
        status = row.get("status")
        candidates = row.get("candidates")
        if not consumer or status not in {"CLOSED", "PARTIAL", "OPEN"}:
            errors.append(f"invalid delayed consumer row: {row!r}")
            continue
        if not isinstance(candidates, list):
            errors.append(f"delayed candidates must be a list: {consumer}")
        delayed_statuses[status] = delayed_statuses.get(status, 0) + 1
        if status == "OPEN":
            warnings.append(f"delayed producer closure remains OPEN: {consumer}")
        elif status == "PARTIAL":
            warnings.append(f"delayed lifecycle closure remains PARTIAL: {consumer}")

    predicate_statuses = {}
    for name, row in data.get("composite_predicates", {}).items():
        status = row.get("status")
        if status not in {"SOURCE-CLOSED", "PARTIAL", "OPEN", "OPEN/BLOCKED"}:
            errors.append(f"invalid predicate status for {name}: {status!r}")
        predicate_statuses[status] = predicate_statuses.get(status, 0) + 1
        if status in {"OPEN", "OPEN/BLOCKED"}:
            warnings.append(f"predicate remains {status}: {name}")
        elif status == "PARTIAL":
            warnings.append(f"predicate remains PARTIAL: {name}")

    readiness = "BLOCKED" if errors else ("SOURCE_LEVEL_PARTIAL" if warnings else "SOURCE_LEVEL_CLOSED")
    report = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.machine_contract_readiness",
        "scope": "E01-E272",
        "readiness": readiness,
        "is_gameplay_readiness": False,
        "is_reachability_proof": False,
        "errors": errors,
        "warnings": warnings,
        "delayed_status_counts": delayed_statuses,
        "predicate_status_counts": predicate_statuses,
        "source_closed_producer_count": len(data.get("source_closed_producers", [])),
        "hard_negative_count": len(data.get("hard_negatives", [])),
        "known_not_yet_verified": data.get("known_not_yet_verified", []),
        "rules": [
            "OPEN and PARTIAL source contracts are never promoted automatically",
            "ID parity does not prove semantic equality",
            "source-level closure does not prove gameplay reachability",
            "frozen production scope excludes E273-E277",
        ],
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": readiness, "errors": len(errors), "warnings": len(warnings)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
