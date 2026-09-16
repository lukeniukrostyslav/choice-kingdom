#!/usr/bin/env python3
"""S08 source-closure gate for the frozen E01-E272 production catalog.

S08 is a source-level producer/consumer gate. Runtime qualification belongs to
later gates and must not be silently promoted here. This validator proves that
all producer families explicitly admitted to S08 are source-backed, that the
frozen scope is respected, and that composite predicates have source-closed
contracts. Runtime-open fields are intentionally allowed and reported.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs/MACHINE_CANONICAL_GRAPH_01.json"

REQUIRED_FACTS = {
    "public_bridge": ("E18", "B"),
    "flexible_accounts": ("E09", "B"),
    "veteran_patronage": ("E117", "B"),
    "estate_exception": ("E118", "B"),
    "border_compensation": ("E125", "A"),
    "requisition_compensation": ("E156", "A"),
    "winter_rent_ceiling": ("E160", "A"),
    "history.guild_logistics_cooperation": ("E136", "B"),
    "history.guild_representation": ("E144", "A/B"),
    "history.cross_faction_package": ("E148", "A"),
    "history.house_assembly": ("E161", "A"),
    "people_charter_endorsed": ("E50", "A"),
    "guild_political_representation": ("E49", "A"),
    "full_ledger_published": ("E53", "A"),
    "pred.market_pressure": ("E19", "B"),
    "clear.pred.market_pressure": ("E19", "A"),
    "pred.winter_severe": ("E29", "A/B"),
    "pred.transport_disruption": ("E32", "explicit crisis outcome"),
    "clear.pred.transport_disruption": ("E136", "A/B"),
    "pred.border_crisis": ("E271", "A"),
    "clear.pred.border_crisis": ("E272", "A/B"),
    "pred.food_stable": ("E192", "B"),
    "clear.pred.food_stable": ("E192", "A"),
    "military_constitutional_evidence": ("E199", "A"),
    "auditor_independence": ("E142", "A"),
    "crown_audited": ("E154", "A"),
    "legislative_budget_lock": ("E198", "A"),
    "soldier_compensation": ("E20", "A"),
    "cheap_weapons": ("E17", "A"),
    "infrastructure_concession": ("E45", "B"),
    "emergency_decree_used": ("E02", "A"),
    "emergency_power": ("E33", "A"),
    "constitutional_limit": ("E33", "B"),
    "people_heard": ("E34", "A"),
    "systemic_explanation_convergence": ("E270", "A"),
    "secret_evidence_route": ("E25", "B"),
}

REQUIRED_COMPOSITES = {
    "pred.guild_influence_strong",
    "pred.food_stable",
    "pred.systemic_explanation_verified",
    "pred.coalition_cooperation",
    "pred.constitutional_prepared_strong",
    "pred.budget_reform",
    "pred.final_charter_prerequisites",
}

ALLOWED_EXCLUDED = {"E273", "E274", "E275", "E276", "E277"}


def fail(msg: str) -> None:
    print(f"S08_SOURCE_CLOSURE: FAIL\n- {msg}")
    raise SystemExit(1)


def main() -> None:
    if not GRAPH.exists():
        fail("missing docs/MACHINE_CANONICAL_GRAPH_01.json")
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    scope = graph.get("scope", {})
    if scope.get("first_event") != 1 or scope.get("last_event") != 272:
        fail(f"unexpected frozen scope: {scope}")
    excluded = set(scope.get("excluded_events", []))
    if excluded != ALLOWED_EXCLUDED:
        fail(f"unexpected excluded scope: {sorted(excluded)}")

    producers = {x["fact"]: x for x in graph.get("source_closed_producers", [])}
    missing = []
    wrong = []
    for fact, (event, choice) in REQUIRED_FACTS.items():
        item = producers.get(fact)
        if item is None:
            missing.append(fact)
            continue
        if item.get("event") != event or item.get("choice") != choice:
            wrong.append(f"{fact}: expected {event}/{choice}, got {item.get('event')}/{item.get('choice')}")
    if missing:
        fail("missing required source-closed producers: " + ", ".join(sorted(missing)))
    if wrong:
        fail("producer identity mismatch: " + "; ".join(wrong))

    composites = graph.get("composite_predicates", {})
    bad = []
    for fact in REQUIRED_COMPOSITES:
        item = composites.get(fact)
        if not item or item.get("status") != "SOURCE-CLOSED":
            bad.append(fact)
    if bad:
        fail("composite predicates not SOURCE-CLOSED: " + ", ".join(sorted(bad)))

    # Frozen production semantics must never contain expansion candidates.
    for section in ("source_closed_producers", "derived_source_contracts", "delayed_consumers"):
        for item in graph.get(section, []):
            blob = json.dumps(item, ensure_ascii=False)
            if any(eid in blob for eid in ALLOWED_EXCLUDED):
                fail(f"excluded event leaked into {section}: {item}")

    print("S08_SOURCE_CLOSURE: PASS")
    print("scope=E01-E272")
    print(f"required_source_producers={len(REQUIRED_FACTS)}")
    print(f"required_source_closed_composites={len(REQUIRED_COMPOSITES)}")
    print("runtime_open_fields=allowed_and_reported_by_later_gates")


if __name__ == "__main__":
    main()
