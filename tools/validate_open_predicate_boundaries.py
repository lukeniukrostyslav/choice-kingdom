#!/usr/bin/env python3
"""Validate that unresolved predicate contracts remain explicitly unresolved.

This is a negative-safety gate: it must fail if an OPEN predicate is silently
promoted to a producer without an authored frozen-scope contract.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs/MACHINE_CANONICAL_GRAPH_01.json"
CLOSURE = ROOT / "docs/CANONICAL_CONTRACT_CLOSURE_PASS_01.md"
OUT = ROOT / "docs/MACHINE_OPEN_PREDICATE_BOUNDARY_01.json"

OPEN_PREDICATES = {
    "pred.guild_labor_tension": "OPEN",
    "pred.information_pressure_high": "OPEN",
}
EXCLUDED = {"E273", "E274", "E275", "E276", "E277"}


def main() -> int:
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    closure = CLOSURE.read_text(encoding="utf-8")
    producers = graph.get("source_closed_producers", [])
    errors: list[str] = []
    checked: dict[str, dict[str, object]] = {}

    producer_by_fact = {}
    for row in producers:
        fact = row.get("fact")
        if fact:
            producer_by_fact.setdefault(fact, []).append(row)

    for predicate, expected_status in OPEN_PREDICATES.items():
        rows = producer_by_fact.get(predicate, [])
        excluded_rows = [
            row for row in rows
            if any(event in str(row.get("event", "")) for event in EXCLUDED)
        ]
        checked[predicate] = {
            "expected_status": expected_status,
            "canonical_graph_producer_rows": rows,
            "excluded_scope_rows": excluded_rows,
            "closure_explicitly_open": f"`{predicate}` | OPEN" in closure,
        }
        if rows:
            errors.append(
                f"{predicate}: canonical graph unexpectedly contains source-closed producer rows: {rows}"
            )
        if excluded_rows:
            errors.append(
                f"{predicate}: excluded E273-E277 material was admitted as a producer"
            )
        if f"`{predicate}` | OPEN" not in closure:
            errors.append(f"{predicate}: closure document no longer records the contract as OPEN")

    report = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.open_predicate_boundary",
        "scope": "E01-E272",
        "status": "PASS" if not errors else "FAIL",
        "runtime_verified": False,
        "errors": errors,
        "checked": checked,
        "rules": [
            "OPEN predicates must not acquire an inferred producer",
            "E273-E277 are excluded from frozen production semantics",
            "absence of a producer is not evidence that a predicate is satisfied",
            "this gate does not promote or invent authored semantics",
        ],
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
