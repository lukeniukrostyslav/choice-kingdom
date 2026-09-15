#!/usr/bin/env python3
"""Cross-check machine predicate status against the authoritative contract table.

This is a bounded source-consistency gate. It does not infer gameplay semantics,
reachability, runtime invalidation, or promote OPEN/PARTIAL contracts.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
CONTRACT = ROOT / "docs" / "CANONICAL_DERIVED_PREDICATE_CONTRACT_01.md"
OUT = ROOT / "docs" / "MACHINE_PREDICATE_CONTRACT_PARITY_01.json"

EXPECTED = {
    "pred.border_crisis": "CLOSED",
    "pred.guild_logistics_cooperation": "CLOSED",
    "pred.food_stable": "OPEN / BLOCKED",
    "pred.transport_disruption": "SOURCE PRODUCER CLOSED",
    "pred.winter_severe": "CLOSED",
    "pred.market_pressure": "CLOSED",
    "pred.guild_labor_tension": "OPEN",
    "pred.information_pressure_high": "OPEN",
    "pred.guild_influence_strong": "PARTIAL",
    "pred.systemic_explanation_verified": "PARTIAL",
    "pred.coalition_cooperation": "PARTIAL",
    "pred.constitutional_prepared_strong": "PARTIAL",
    "pred.budget_reform": "SOURCE-CLOSED",
    "pred.final_charter_prerequisites": "OPEN",
}


def normalize(status: str) -> str:
    status = status.upper().strip()
    if status.startswith("SOURCE PRODUCER CLOSED"):
        return "SOURCE PRODUCER CLOSED"
    if status.startswith("CLOSED"):
        return "CLOSED"
    if status.startswith("OPEN / BLOCKED"):
        return "OPEN / BLOCKED"
    if status.startswith("OPEN"):
        return "OPEN"
    if status.startswith("PARTIAL"):
        return "PARTIAL"
    if status.startswith("SOURCE-CLOSED"):
        return "SOURCE-CLOSED"
    return status


def main() -> int:
    data = json.loads(GRAPH.read_text(encoding="utf-8"))
    text = CONTRACT.read_text(encoding="utf-8")
    machine = data.get("composite_predicates", {})
    errors: list[str] = []
    checked: dict[str, dict[str, str | bool]] = {}

    for predicate, expected in EXPECTED.items():
        row = machine.get(predicate)
        if row is None:
            errors.append(f"missing machine predicate: {predicate}")
            continue
        machine_status = str(row.get("status", ""))
        pattern = re.compile(r"^\|\s*`" + re.escape(predicate) + r"`\s*\|.*?\|\s*([^|\n]+?)\s*\|\s*$", re.MULTILINE)
        match = pattern.search(text)
        if not match:
            errors.append(f"missing authoritative contract row: {predicate}")
            continue
        contract_status = match.group(1).strip()
        # The table may contain a longer lifecycle qualifier after the canonical status.
        machine_norm = normalize(machine_status)
        contract_norm = normalize(contract_status)
        ok = machine_norm == normalize(expected) and contract_norm == normalize(expected)
        checked[predicate] = {
            "expected": expected,
            "machine_status": machine_status,
            "contract_status": contract_status,
            "match": ok,
        }
        if not ok:
            errors.append(
                f"{predicate}: expected {expected!r}, machine={machine_status!r}, contract={contract_status!r}"
            )

    report = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.predicate_contract_parity",
        "scope": "E01-E272",
        "readiness": "BLOCKED" if errors else "SOURCE_LEVEL_CLOSED",
        "gameplay_verified": False,
        "semantic_equality_proven": False,
        "errors": errors,
        "checked": checked,
        "rules": [
            "authoritative markdown and machine contract must agree on frozen predicate status",
            "status parity does not prove gameplay reachability",
            "status parity does not prove runtime invalidation",
            "OPEN/PARTIAL predicates are never promoted by this gate",
        ],
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": report["readiness"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
