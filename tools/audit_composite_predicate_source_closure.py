#!/usr/bin/env python3
"""Audit bounded source evidence for high-risk composite predicates.

This gate checks only source-level invariants explicitly frozen in the
canonical predicate contract and producer/consumer registry. It never infers
runtime reachability, scheduler semantics, or a missing producer.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "CANONICAL_DERIVED_PREDICATE_CONTRACT_01.md"
REGISTRY = ROOT / "docs" / "CANONICAL_PRODUCER_CONSUMER_REGISTRY_01.md"
AUDIT = ROOT / "docs" / "SCENARIO_QA_CONTRACT_CLOSURE_AUDIT_02.md"
OUT = ROOT / "docs" / "MACHINE_COMPOSITE_SOURCE_CLOSURE_01.json"

REQUIRED = {
    "pred.guild_influence_strong": [
        "guild_political_representation",
        "guild_tribunal_independent",
        "official_credit_disclosure",
        "audited_monopoly",
        "history.guild_logistics_cooperation",
    ],
    "pred.systemic_explanation_verified": [
        "warehouse/financial",
        "document/language",
        "witness/organizational",
        "explicit convergence decision",
    ],
    "pred.coalition_cooperation": [
        "Explicit cooperation package",
        "identified participants",
        "positive cooperation outcome",
    ],
    "pred.constitutional_prepared_strong": [
        "people_charter_endorsed",
        "crown_audited",
        "house_assembly",
        "military_red_line",
    ],
    "pred.final_charter_prerequisites": [
        "Convergence of already-established",
        "mandatory blockers cleared",
    ],
}

FORBIDDEN_EXPANSION = ["E273", "E274", "E275", "E276", "E277"]


def main() -> int:
    contract = CONTRACT.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")
    combined = "\n".join((contract, registry, audit))

    errors: list[str] = []
    checked: dict[str, dict[str, object]] = {}
    for predicate, needles in REQUIRED.items():
        missing = [needle for needle in needles if needle not in combined]
        checked[predicate] = {
            "required_evidence": needles,
            "missing_evidence": missing,
            "source_evidence_present": not missing,
        }
        if missing:
            errors.append(f"{predicate}: missing frozen source evidence: {missing}")

    # Expansion IDs may be mentioned only as quarantine/negative controls in
    # these source documents. They must never be presented as production input.
    for event_id in FORBIDDEN_EXPANSION:
        if event_id not in combined:
            continue
        if event_id == "E273" and "expansion-only" not in combined.lower():
            errors.append("E273 appears without the required expansion-only quarantine context")

    # These are explicit non-promotion assertions from the latest bounded audit.
    hard_negatives = [
        "E209 cannot manufacture `pred.final_charter_prerequisites`",
        "food_logistics_stabilized` is not promoted to `pred.food_stable`",
        "No such complete producer/key inventory is currently closed",
    ]
    for assertion in hard_negatives:
        if assertion not in audit:
            errors.append(f"missing bounded non-promotion assertion: {assertion}")

    report = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.composite_predicate_source_closure",
        "scope": "E01-E272",
        "readiness": "BLOCKED" if errors else "SOURCE_LEVEL_CLOSED",
        "gameplay_verified": False,
        "runtime_verified": False,
        "semantic_equality_proven": False,
        "errors": errors,
        "checked": checked,
        "rules": [
            "source evidence presence does not establish an executable producer",
            "consumer events may not manufacture predicates they consume",
            "E273-E277 are excluded from production semantics",
            "this gate does not infer reachability, lifecycle, scheduling, or invalidation",
            "OPEN/PARTIAL contracts remain OPEN/PARTIAL unless authoritative source semantics change",
        ],
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": report["readiness"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
