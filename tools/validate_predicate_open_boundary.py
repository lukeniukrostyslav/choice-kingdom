#!/usr/bin/env python3
"""Enforce the source-level quarantine for predicates without authored producers."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "CANONICAL_DERIVED_PREDICATE_CONTRACT_01.md"
AUDIT = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
OUT = ROOT / "docs" / "MACHINE_PREDICATE_OPEN_BOUNDARY_01.json"

BLOCKED = {
    "pred.guild_labor_tension": "No E01-E272 producer verified; E275-B is expansion-only.",
    "pred.information_pressure_high": "No E01-E272 producer verified; E276-B is expansion-only.",
}


def main() -> int:
    text = CONTRACT.read_text(encoding="utf-8")
    graph = json.loads(AUDIT.read_text(encoding="utf-8"))
    errors: list[str] = []
    checked: dict[str, dict[str, object]] = {}

    for predicate, reason in BLOCKED.items():
        marker = f"`{predicate}`"
        start = text.find(marker)
        in_contract = start >= 0 and "OPEN / BLOCKED" in text[start : start + 300]
        expansion_id = "E275-B" if predicate == "pred.guild_labor_tension" else "E276-B"
        expansion_quarantine = expansion_id in text and "Expansion quarantine" in text
        leaked = predicate in json.dumps(graph.get("source_closed_producers", []), sort_keys=True)
        ok = in_contract and expansion_quarantine and not leaked
        checked[predicate] = {
            "expected": "OPEN_BLOCKED_SOURCE_BOUNDARY",
            "contract_explicitly_blocked": in_contract,
            "expansion_producer_quarantined": expansion_quarantine,
            "leaked_into_source_closed_producers": leaked,
            "reason": reason,
            "ok": ok,
        }
        if not ok:
            errors.append(f"{predicate}: open-boundary contract is not conservative")

    result = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.predicate_open_boundary",
        "readiness": "PASS_OPEN_BOUNDARY_ENFORCED" if not errors else "FAIL",
        "scope": "E01-E272",
        "blocked_predicates": checked,
        "runtime_verified": False,
        "note": "This gate does not close the predicates. It prevents prose, aliases, or E273-E277 from being promoted into production predicate semantics without an authored E01-E272 producer.",
        "errors": errors,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": result["readiness"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
