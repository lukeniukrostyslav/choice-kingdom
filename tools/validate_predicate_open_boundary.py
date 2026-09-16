#!/usr/bin/env python3
"""Enforce the production predicate boundary and formal exclusion of non-production candidates."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "CANONICAL_DERIVED_PREDICATE_CONTRACT_01.md"
AUDIT = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
OUT = ROOT / "docs" / "MACHINE_PREDICATE_OPEN_BOUNDARY_01.json"

EXCLUDED = {
    "pred.guild_labor_tension": ("E275-B", "guild-labor tension"),
    "pred.information_pressure_high": ("E276-B", "information pressure"),
}


def main() -> int:
    text = CONTRACT.read_text(encoding="utf-8")
    graph = json.loads(AUDIT.read_text(encoding="utf-8"))
    errors: list[str] = []
    checked: dict[str, dict[str, object]] = {}
    source_closed = graph.get("source_closed_producers", [])
    derived = graph.get("derived_source_contracts", [])

    for predicate, (expansion_id, label) in EXCLUDED.items():
        marker = f"`{predicate}`"
        start = text.find(marker)
        window = text[start : start + 500] if start >= 0 else ""
        explicitly_excluded = "EXCLUDED / NOT-A-PRODUCTION-PREDICATE" in window
        expansion_only = expansion_id in text and "expansion-only" in text.lower()
        source_closed_leak = any(item.get("fact") == predicate for item in source_closed)
        derived_contract_leak = any(item.get("fact") == predicate for item in derived)
        ok = explicitly_excluded and expansion_only and not source_closed_leak and not derived_contract_leak
        checked[predicate] = {
            "expected": "FORMALLY_EXCLUDED_FROM_PRODUCTION",
            "contract_explicitly_excluded": explicitly_excluded,
            "expansion_candidate_quarantined": expansion_only,
            "leaked_into_source_closed_producers": source_closed_leak,
            "leaked_into_derived_source_contracts": derived_contract_leak,
            "label": label,
            "ok": ok,
        }
        if not ok:
            errors.append(f"{predicate}: formal production exclusion is not enforced")

    result = {
        "schema_version": "2.1",
        "contract": "choice_kingdom.predicate_production_boundary",
        "readiness": "PASS_PRODUCTION_BOUNDARY_CLOSED" if not errors else "FAIL",
        "scope": "E01-E272",
        "formally_excluded_predicates": checked,
        "runtime_verified": False,
        "note": "The two candidates are formally removed from production predicate semantics. They may appear in the contract only as negative QA fixtures; they cannot become source-closed or derived production inputs. E275/E276 remain expansion-only and require an explicit scope change plus re-audit for any future admission.",
        "errors": errors,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": result["readiness"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
