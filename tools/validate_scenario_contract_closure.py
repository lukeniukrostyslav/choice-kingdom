#!/usr/bin/env python3
"""Validate the frozen scenario contract boundary without inventing runtime facts."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
INVENTORY = ROOT / "scenario-source-inventory.json"
errors: list[str] = []

def load(path: Path) -> dict:
    if not path.exists():
        errors.append(f"missing required file: {path.relative_to(ROOT)}")
        return {}
    return json.loads(path.read_text(encoding="utf-8"))

graph = load(GRAPH)
expected: set[str] = set()
if graph:
    scope = graph.get("scope", {})
    first, last = int(scope.get("first_event", 0)), int(scope.get("last_event", 0))
    excluded = set(scope.get("excluded_events", []))
    expected = {f"E{i:02d}" for i in range(first, last + 1)} - excluded
    if (first, last) != (1, 272):
        errors.append(f"unexpected frozen scope: E{first:02d}-E{last:02d}")
    if excluded != {"E273", "E274", "E275", "E276", "E277"}:
        errors.append(f"unexpected excluded scope: {sorted(excluded)}")
    if len(expected) != 272:
        errors.append(f"expected production event count is 272, got {len(expected)}")

inventory = load(INVENTORY)
if inventory:
    actual_ids = {event.get("event_id") for event in inventory.get("events", [])}
    if actual_ids != expected:
        missing = sorted(expected - actual_ids, key=lambda x: int(x[1:]))
        extra = sorted(actual_ids - expected, key=lambda x: int(x[1:]))
        if missing:
            errors.append("inventory missing events: " + ", ".join(missing))
        if extra:
            errors.append("inventory contains out-of-scope events: " + ", ".join(extra))
    if inventory.get("predicate_cycles"):
        errors.append("predicate dependency cycles present in compiled inventory")

# Index authored event blocks from every catalog named by the machine graph.
catalog_blocks: dict[str, str] = {}
heading_re = re.compile(r"^### (E\d{2,3}) — (.+)$", re.M)
allowed_duplicates = set(graph.get("allowed_catalog_duplicate_event_ids", []))
for source in graph.get("source_of_truth", {}).get("catalog_sources", []):
    path = ROOT / source
    if not path.exists():
        errors.append(f"missing catalog source: {source}")
        continue
    text = path.read_text(encoding="utf-8")
    matches = list(heading_re.finditer(text))
    for i, match in enumerate(matches):
        event_id = match.group(1)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        if event_id in catalog_blocks and event_id not in allowed_duplicates:
            errors.append(f"duplicate canonical event block: {event_id}")
        else:
            catalog_blocks[event_id] = catalog_blocks.get(event_id, "") + text[match.start():end]

# Source-closed producer declarations are source-level evidence. Validate that
# their authored event and A/B choice boundary exists; the fact itself may be
# explicit prose rather than a machine backtick token.
for record in graph.get("source_closed_producers", []):
    event = record.get("event", "")
    choice = str(record.get("choice", ""))
    if event not in expected:
        errors.append(f"source-closed producer outside scope: {event}")
        continue
    block = catalog_blocks.get(event, "")
    if not block:
        errors.append(f"source-closed producer event missing from catalogs: {event}")
        continue
    if choice in {"A", "B", "A/B"}:
        labels = set(re.findall(r"(?:^-|^\s*)\s*\*\*([AB])\s*[—:]", block, re.M))
        if not set(choice.split("/")).issubset(labels):
            errors.append(f"producer choice boundary not authored: {event} {choice}")

# Delayed candidate identity must stay inside E01-E272 and never self-satisfy.
for row in graph.get("delayed_consumers", []):
    consumer = row.get("consumer", "")
    if consumer not in expected:
        errors.append(f"delayed consumer outside scope: {consumer}")
    for candidate in row.get("candidates", []):
        for candidate_event in re.findall(r"E\d{2,3}", candidate):
            if candidate_event not in expected:
                errors.append(f"delayed candidate outside scope: {consumer} <- {candidate}")
            if candidate_event == consumer:
                errors.append(f"delayed consumer self-satisfies: {consumer}")

required_negatives = {
    "consumer_cannot_manufacture_prerequisite",
    "excluded_events_cannot_enter_production",
    "generic_compensation_route_cannot_union_sources",
    "ordinary_history_cannot_be_meta_state",
    "relationship_is_not_institutional_domain",
    "security_is_not_border_crisis",
    "four_way_bargain_is_not_cooperation",
}
negative_ids = {item.get("id") for item in graph.get("hard_negatives", [])}
missing_negatives = sorted(required_negatives - negative_ids)
if missing_negatives:
    errors.append("missing hard-negative rules: " + ", ".join(missing_negatives))

print("CONTRACT_CLOSURE_AUDIT: FAIL" if errors else "CONTRACT_CLOSURE_AUDIT: PASS")
for error in errors:
    print(f"- {error}")
if not errors:
    print(f"scope_events={len(expected)}")
    print(f"catalog_event_blocks={len(catalog_blocks)}")
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
