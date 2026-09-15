#!/usr/bin/env python3
"""Cross-check machine composite predicate status against the authoritative contract table.

This is a bounded source-consistency gate. It does not infer gameplay semantics,
reachability, runtime invalidation, or promote OPEN/BLOCKED contracts.
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
    "pred.guild_influence_strong": "SOURCE-CLOSED",
    "pred.systemic_explanation_verified": "SOURCE-CLOSED",
    "pred.coalition_cooperation": "SOURCE-CLOSED",
    "pred.constitutional_prepared_strong": "SOURCE-CLOSED",
    "pred.budget_reform": "SOURCE-CLOSED",
    "pred.final_charter_prerequisites": "OPEN / BLOCKED",
    "pred.food_stable": "OPEN / BLOCKED",
}


def normalize(status: str) -> str:
    status = re.sub(r"[*`_]", "", status).upper().strip()
    status = re.sub(r"\s*/\s*", " / ", status)
    if status.startswith("SOURCE-CLOSED"):
        return "SOURCE-CLOSED"
    if status.startswith("OPEN / BLOCKED"):
        return "OPEN / BLOCKED"
    if status.startswith("OPEN"):
        return "OPEN"
    if status.startswith("PARTIAL"):
        return "PARTIAL"
    if status.startswith("CLOSED"):
        return "CLOSED"
    return status


def main() -> int:
    data = json.loads(GRAPH.read_text(encoding="utf-8"))
    text = CONTRACT.read_text(encoding="utf-8")
    machine = data.get("composite_predicates", {})
    errors: list[str] = []
    checked: dict[str, dict[str, str | bool]] = {}

    machine_keys = set(machine)
    expected_keys = set(EXPECTED)
    unexpected = sorted(machine_keys - expected_keys)
    missing = sorted(expected_keys - machine_keys)
    for predicate in missing:
        errors.append(f"missing machine composite predicate: {predicate}")
    for predicate in unexpected:
        errors.append(f"unexpected machine composite predicate not frozen by this gate: {predicate}")

    for predicate, expected in EXPECTED.items():
        row = machine.get(predicate)
        if row is None:
            continue
        machine_status = str(row.get("status", ""))
        pattern = re.compile(
            r"^\|\s*`" + re.escape(predicate) + r"`\s*\|.*?\|\s*([^|\n]+?)\s*\|\s*$",
            re.MULTILINE,
        )
        match = pattern.search(text)
        if not match:
            errors.append(f"missing authoritative contract row: {predicate}")
            continue
        contract_status = match.group(1).strip()
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
        "schema_version": "1.2",
        "contract": "choice_kingdom.predicate_contract_parity",
        "scope": "E01-E272",
        "readiness": "BLOCKED" if errors else "SOURCE_LEVEL_CLOSED",
        "gameplay_verified": False,
        "semantic_equality_proven": False,
        "errors": errors,
        "checked": checked,
        "rules": [
            "only the machine graph composite_predicates section is checked by this gate",
            "source-closed producer predicates are validated by their producer inventories, not this composite gate",
            "authoritative markdown and machine composite contract must agree on frozen status",
            "status parity does not prove gameplay reachability",
            "status parity does not prove runtime invalidation",
            "OPEN/OPEN-BLOCKED predicates are never promoted by this gate",
        ],
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": report["readiness"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
