#!/usr/bin/env python3
"""Validate the machine-readable Choice Kingdom canonical graph contract.

Source-level validator only: design-level EVENT_GRAPH edges are not runtime truth.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
EVENT_GRAPH = ROOT / "docs" / "EVENT_GRAPH.md"
PRODUCER_INVENTORY = ROOT / "docs" / "CANONICAL_PRODUCER_INVENTORY_01.md"

EVENT_TOKEN_RE = re.compile(r"\bE(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9])(?:-[A-Z])?\b")
CHAIN_RE = re.compile(r"`([^`]*->[^`]*)`")


def canonical_event(event_id: str) -> str:
    return event_id.split("-", 1)[0]


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    lo = manifest["scope"]["first_event"]
    hi = manifest["scope"]["last_event"]
    excluded = set(manifest["scope"]["excluded_events"])
    expected = {f"E{i:02d}" for i in range(lo, hi + 1)}
    errors: list[str] = []
    warnings: list[str] = []

    if not EVENT_GRAPH.exists():
        errors.append("EVENT_GRAPH.md is missing")
    if not PRODUCER_INVENTORY.exists():
        errors.append("CANONICAL_PRODUCER_INVENTORY_01.md is missing")
    if errors:
        print("CANONICAL GRAPH VALIDATION: FAIL")
        for e in errors:
            print(f"ERROR: {e}")
        return 1

    graph_text = EVENT_GRAPH.read_text(encoding="utf-8")
    inventory_text = PRODUCER_INVENTORY.read_text(encoding="utf-8")

    # Parse explicit design-level backtick chains. Narrative scope notes are ignored.
    edges: list[tuple[str, str]] = []
    referenced: set[str] = set()
    for match in CHAIN_RE.finditer(graph_text):
        ids = [canonical_event(x) for x in EVENT_TOKEN_RE.findall(match.group(1))]
        for event_id in ids:
            referenced.add(event_id)
            if event_id not in expected and event_id not in excluded:
                errors.append(f"out-of-scope event reference in graph chain: {event_id}")
        for src, dst in zip(ids, ids[1:]):
            if src in expected and dst in expected:
                edges.append((src, dst))

    # Repeated design edges are legal: the same causal edge can be documented by
    # several layer sections. Record them, but do not confuse them with a semantic
    # contradiction or runtime duplicate writer.
    seen: set[tuple[str, str]] = set()
    repeated_edges: set[tuple[str, str]] = set()
    for src, dst in edges:
        if (src, dst) in seen:
            repeated_edges.add((src, dst))
        seen.add((src, dst))
        if src == dst:
            errors.append(f"self-loop event edge: {src} -> {dst}")
    if repeated_edges:
        warnings.append(f"design graph repeats {len(repeated_edges)} already-documented causal edges")

    # Check actual producer rows only; inventory prose is allowed to mention excluded
    # expansion candidates as an explicit quarantine rule.
    producer_rows = []
    for line in inventory_text.splitlines():
        if line.startswith("|") and "|" in line[1:]:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 4 and cells[0] not in {"Canonical fact / predicate", "---"}:
                producer_rows.append(line)
    producer_blob = "\n".join(producer_rows)
    for excluded_id in excluded:
        if re.search(rf"\b{re.escape(excluded_id)}(?:-[A-Z])?\b", producer_blob):
            errors.append(f"excluded expansion producer leaked into canonical inventory: {excluded_id}")

    for row in manifest["source_closed_producers"]:
        event_id = row["event"]
        if event_id not in expected:
            errors.append(f"manifest producer outside frozen scope: {event_id}")

    for row in manifest["delayed_consumers"]:
        consumer = row["consumer"]
        if consumer not in expected:
            errors.append(f"delayed consumer outside frozen scope: {consumer}")
        if row["status"] == "OPEN" and len(row.get("candidates", [])) > 1:
            warnings.append(f"open delayed source remains intentionally ambiguous: {consumer}")

    required_negatives = {
        "consumer_cannot_manufacture_prerequisite",
        "excluded_events_cannot_enter_production",
        "generic_compensation_route_cannot_union_sources",
        "ordinary_history_cannot_be_meta_state",
    }
    actual_negatives = {x["id"] for x in manifest["hard_negatives"]}
    for item in sorted(required_negatives - actual_negatives):
        errors.append(f"missing mandatory hard-negative rule: {item}")

    report = {
        "frozen_scope": f"E{lo:02d}-E{hi}",
        "excluded_scope": sorted(excluded),
        "graph_edges_unique": len(seen),
        "graph_edges_repeated_in_design_doc": len(repeated_edges),
        "graph_event_nodes_referenced": len(referenced & expected),
        "graph_event_nodes_missing_from_design_graph": len(expected - referenced),
        "source_closed_producers": len(manifest["source_closed_producers"]),
        "delayed_consumers": len(manifest["delayed_consumers"]),
        "hard_negative_rules": len(actual_negatives),
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if errors:
        print("CANONICAL GRAPH VALIDATION: FAIL")
        return 1
    print("CANONICAL GRAPH VALIDATION: PASS (source-level contract checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
