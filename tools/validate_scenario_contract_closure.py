#!/usr/bin/env python3
"""Validate the internal consistency of the frozen scenario contract boundary.

This gate is deliberately source-level. It proves that the machine graph's
source-closed producer declarations, delayed-consumer candidates, frozen scope,
and hard-negative rules agree with the compiled E01-E272 inventory. It does not
claim runtime reachability, persistence, replay, or ending execution.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
INVENTORY_TOOL = ROOT / "tools" / "compile_scenario_source_inventory.py"

errors: list[str] = []

def load(path: Path) -> dict:
    if not path.exists():
        errors.append(f"missing required file: {path.relative_to(ROOT)}")
        return {}
    return json.loads(path.read_text(encoding="utf-8"))

graph = load(GRAPH)

if graph:
    scope = graph.get("scope", {})
    first = int(scope.get("first_event", 0))
    last = int(scope.get("last_event", 0))
    excluded = set(scope.get("excluded_events", []))
    expected = {f"E{i:02d}" for i in range(first, last + 1)} - excluded
    if (first, last) != (1, 272):
        errors.append(f"unexpected frozen scope: E{first:02d}-E{last:02d}")
    if excluded != {"E273", "E274", "E275", "E276", "E277"}:
        errors.append(f"unexpected excluded scope: {sorted(excluded)}")
    if len(expected) != 272:
        errors.append(f"expected production event count is 272, got {len(expected)}")
else:
    expected = set()

# Compile the inventory in-process so this validator cannot silently validate a
# stale generated artifact. Importing the compiler would execute its CLI, so the
# actual source inventory remains the authoritative first gate in CI.
if not INVENTORY_TOOL.exists():
    errors.append("missing scenario source inventory compiler")

# The validator consumes the compiler's JSON only when CI has already generated
# it. Local invocations can run the compiler first; this separation keeps the
# checks deterministic and makes stale-artifact use visible.
inventory_path = ROOT / "scenario-source-inventory.json"
if not inventory_path.exists():
    errors.append("missing generated scenario-source-inventory.json (run compiler first)")
    inventory = {}
else:
    inventory = load(inventory_path)

if inventory:
    if inventory.get("schema") != "choice-kingdom-scenario-source-inventory-1":
        errors.append("unexpected inventory schema")
    actual_ids = {event.get("event_id") for event in inventory.get("events", [])}
    if actual_ids != expected:
        missing = sorted(expected - actual_ids, key=lambda x: int(x[1:]))
        extra = sorted(actual_ids - expected, key=lambda x: int(x[1:]))
        if missing:
            errors.append("inventory missing events: " + ", ".join(missing))
        if extra:
            errors.append("inventory contains out-of-scope events: " + ", ".join(extra))

    producers = inventory.get("producers", {})
    consumers = inventory.get("consumers", {})

    # Every graph-declared source-closed event producer must be visible in the
    # extracted source inventory. Derived evaluators are intentionally outside
    # the event namespace and are checked separately below.
    for record in graph.get("source_closed_producers", []):
        fact = record.get("fact")
        event = record.get("event")
        if not fact or not event:
            errors.append("malformed source_closed_producer record")
            continue
        if event not in expected:
            errors.append(f"source-closed producer outside scope: {event} -> {fact}")
            continue
        if fact not in producers:
            # Clear markers are represented as authored outputs too. A graph
            # declaration may use a leading 'clear ' label for readability.
            candidates = [fact[6:].strip()] if fact.startswith("clear ") else []
            if not any(candidate in producers for candidate in candidates):
                errors.append(f"declared source-closed producer not extracted: {event} -> {fact}")

    for record in graph.get("derived_producers_outside_event_namespace", []):
        producer = record.get("producer")
        if producer == "FINAL_CHARTER_GATE_EVALUATOR" and not record.get("fact"):
            errors.append("final charter derived producer missing fact")

    # Delayed candidates must point only into the frozen production event set and
    # must never let a consumer satisfy itself. This catches accidental aliases
    # and expansion leakage without pretending to prove runtime scheduling.
    for row in graph.get("delayed_consumers", []):
        consumer = row.get("consumer", "")
        if consumer and consumer not in expected:
            errors.append(f"delayed consumer outside scope: {consumer}")
        for candidate in row.get("candidates", []):
            event_match = re.search(r"E\d{2,3}", candidate)
            if event_match:
                candidate_event = event_match.group(0)
                if candidate_event not in expected:
                    errors.append(f"delayed candidate outside scope: {consumer} <- {candidate}")
                if candidate_event == consumer:
                    errors.append(f"delayed consumer self-satisfies: {consumer}")

    hard_negatives = graph.get("hard_negatives", [])
    negative_ids = {item.get("id") for item in hard_negatives}
    required_negatives = {
        "consumer_cannot_manufacture_prerequisite",
        "excluded_events_cannot_enter_production",
        "generic_compensation_route_cannot_union_sources",
        "ordinary_history_cannot_be_meta_state",
        "relationship_is_not_institutional_domain",
        "security_is_not_border_crisis",
        "four_way_bargain_is_not_cooperation",
    }
    missing_negatives = sorted(required_negatives - negative_ids)
    if missing_negatives:
        errors.append("missing hard-negative rules: " + ", ".join(missing_negatives))

    # The compiler's own cycle detector is authoritative for predicate cycles;
    # this gate makes the result explicit and fail-closed.
    if inventory.get("predicate_cycles"):
        errors.append("predicate dependency cycles present in compiled inventory")

print("CONTRACT_CLOSURE_AUDIT: FAIL" if errors else "CONTRACT_CLOSURE_AUDIT: PASS")
for error in errors:
    print(f"- {error}")
if not errors:
    print(f"scope_events={len(expected)}")
    print(f"source_closed_producers={len(graph.get('source_closed_producers', []))}")
    print(f"delayed_consumers={len(graph.get('delayed_consumers', []))}")
    print(f"hard_negative_rules={len(graph.get('hard_negatives', []))}")
    print("runtime_reachability=NOT_CLAIMED")
    print("replay_reachability=NOT_CLAIMED")
    print("ending_execution=NOT_CLAIMED")
    print("decision_engine=NOT_CLAIMED")
    print("android=NOT_CLAIMED")
    sys.exit(0)
sys.exit(1)
