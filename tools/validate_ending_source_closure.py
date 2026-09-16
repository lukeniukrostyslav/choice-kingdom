#!/usr/bin/env python3
"""Validate the complete source-level ending qualification and precedence boundary."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUAL = ROOT / "docs" / "MACHINE_ENDING_QUALIFICATION_CONTRACT_01.json"
PREC = ROOT / "docs" / "MACHINE_ENDING_PRECEDENCE_TABLE_01.json"
ALIAS = ROOT / "docs" / "MACHINE_ENDING_ALIAS_BOUNDARY_01.json"
MATRIX = ROOT / "docs" / "ENDING_PRECEDENCE_TEST_MATRIX_01.md"

FAMILIES = [
    "Steward",
    "Iron Crown",
    "Golden Compact",
    "People's Charter",
    "Broken Diadem",
    "Quiet Throne",
    "Second Founder",
]

POSITIVE = ["Second Founder", "People's Charter", "Golden Compact", "Steward", "Iron Crown"]


def main() -> int:
    q = json.loads(QUAL.read_text(encoding="utf-8"))
    p = json.loads(PREC.read_text(encoding="utf-8"))
    a = json.loads(ALIAS.read_text(encoding="utf-8"))
    matrix = MATRIX.read_text(encoding="utf-8")
    errors: list[str] = []

    if q.get("scope") != "E01-E272":
        errors.append("qualification scope is not E01-E272")
    if p.get("scope") != "E01-E272":
        errors.append("precedence scope is not E01-E272")
    if list(q.get("families", {})) != FAMILIES:
        errors.append("ending family inventory/order mismatch")

    for family in FAMILIES:
        data = q["families"].get(family, {})
        for key in ("positive_all", "positive_any", "negative_blockers"):
            if not isinstance(data.get(key), list):
                errors.append(f"{family}: {key} must be a list")
        if not data.get("positive_all") and not data.get("positive_any"):
            errors.append(f"{family}: no positive qualification clauses")
        if family != "Broken Diadem" and not data.get("negative_blockers"):
            errors.append(f"{family}: negative blocker set is empty")

    if p.get("positive_priority") != POSITIVE:
        errors.append("positive priority table is not the frozen authored order")
    if len(set(p.get("positive_priority", []))) != len(POSITIVE):
        errors.append("positive priority contains duplicates or omissions")
    if set(p.get("positive_priority", [])) != set(POSITIVE):
        errors.append("positive priority does not cover every positive family")

    required_pairs = {tuple(pair) for pair in p.get("pairwise_coverage", [])}
    # All ten unordered positive-ending pairs are mandatory. The authored table
    # stores each pair in its explicit authored direction; do not infer priority
    # from that direction.
    required_positive_pairs = {
        tuple(sorted((higher, lower)))
        for index, higher in enumerate(POSITIVE)
        for lower in POSITIVE[index + 1 :]
    }
    actual_positive_pairs = {
        tuple(sorted(pair))
        for pair in required_pairs
        if pair[0] in POSITIVE and pair[1] in POSITIVE
    }
    if not required_positive_pairs.issubset(actual_positive_pairs):
        errors.append("required positive pairwise precedence coverage incomplete")
    if not all(("Quiet Throne", f) in required_pairs for f in POSITIVE):
        errors.append("Quiet Throne pairwise coverage incomplete")
    if not all(("Broken Diadem", f) in required_pairs for f in POSITIVE):
        errors.append("Broken Diadem pairwise coverage incomplete")

    rules = set(q.get("canonical_source_rules", []))
    for required_rule in (
        "pred.final_charter_prerequisites is consumer-only and E209 cannot manufacture it",
        "pred.systemic_explanation_verified is produced by the E270-A convergence contract and cannot be inferred from relationship state",
        "pred.coalition_cooperation is produced by the E148-A cross-faction package contract; E261-A alone is insufficient",
        "forbidden ending aliases cannot satisfy any prerequisite",
        "E273-E277 cannot satisfy any production ending prerequisite",
    ):
        if required_rule not in rules:
            errors.append(f"missing canonical source rule: {required_rule}")

    if a.get("scope") != "E01-E272":
        errors.append("alias boundary scope mismatch")
    if not a.get("canonical_identifiers") or not a.get("forbidden_runtime_aliases"):
        errors.append("alias boundary inventories are incomplete")

    for section in ("## Deterministic precedence order", "## Required authored priority table", "## Exit criteria"):
        if section not in matrix:
            errors.append(f"ending matrix missing {section}")

    for flag in ("fresh_run_reachability_verified", "replay_reachability_verified", "runtime_execution_verified"):
        if q.get(flag) is not False:
            errors.append(f"{flag} must remain false until runtime exists")
    if p.get("runtime_verified") is not False:
        errors.append("precedence runtime_verified must remain false")

    result = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.ending_source_closure_validation",
        "scope": "E01-E272",
        "readiness": "PASS" if not errors else "FAIL",
        "source_contract_closed": not errors,
        "ending_families": len(FAMILIES),
        "positive_priority_entries": len(p.get("positive_priority", [])),
        "pairwise_coverage_entries": len(p.get("pairwise_coverage", [])),
        "runtime_execution_verified": False,
        "fresh_run_reachability_verified": False,
        "replay_reachability_verified": False,
        "errors": errors,
    }
    out = ROOT / "docs" / "MACHINE_ENDING_SOURCE_CLOSURE_VALIDATION_01.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("readiness", "source_contract_closed", "ending_families", "positive_priority_entries", "pairwise_coverage_entries", "errors")}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
