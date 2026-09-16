#!/usr/bin/env python3
"""Validate S01 source-level scenario closure for frozen E01-E272.

S01 is closed here only at the authored/source-contract layer. This gate proves
that the frozen catalog is exhaustive and in-scope, every authored event is
classified by the canonical graph or an explicit coverage declaration, the
structural graph has no unreachable causal nodes, and the existing canonical
inventory is exhaustive. It deliberately does not claim Decision Engine
execution, conditional gameplay reachability, replay execution, or Android
runtime readiness.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
GRAPH = ROOT / "docs" / "EVENT_GRAPH.md"
INVENTORY = ROOT / "docs" / "scenario-source-inventory.json"
OUT = ROOT / "docs" / "MACHINE_S01_SCENARIO_CLOSURE_01.json"

HEADING = re.compile(r"^###\s+(E(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9]))\b")
TOKEN = re.compile(r"\bE(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9])(?:-[A-Z])?\b")
CHAIN = re.compile(r"`([^`]*->[^`]*)`")
COVERAGE = re.compile(r"^-\s+(E(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9]))\s+—\s+coverage declaration only\s*$")


def number(event: str) -> int:
    return int(event[1:])


def canon(token: str) -> str:
    return token.split("-", 1)[0]


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    first = int(manifest["scope"]["first_event"])
    last = int(manifest["scope"]["last_event"])
    expected = {f"E{i:02d}" for i in range(first, last + 1)}
    excluded = set(manifest["scope"]["excluded_events"])
    errors: list[str] = []

    catalog_ids: set[str] = set()
    duplicate_counts: dict[str, int] = {}
    for source in manifest["source_of_truth"]["catalog_sources"]:
        path = ROOT / source
        if not path.exists():
            errors.append(f"missing authoritative catalog source: {source}")
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            match = HEADING.match(line.strip())
            if match:
                event = match.group(1)
                catalog_ids.add(event)
                duplicate_counts[event] = duplicate_counts.get(event, 0) + 1

    catalog_missing = sorted(expected - catalog_ids, key=number)
    catalog_extra = sorted(catalog_ids - expected - excluded, key=number)
    catalog_excluded = sorted(catalog_ids & excluded, key=number)
    allowed_duplicates = set(manifest.get("allowed_catalog_duplicate_event_ids", []))
    unexpected_duplicates = sorted(
        event for event, count in duplicate_counts.items()
        if count > 1 and event in expected and event not in allowed_duplicates
    )
    if catalog_missing:
        errors.append("missing frozen catalog events: " + ", ".join(catalog_missing))
    if catalog_extra:
        errors.append("out-of-scope catalog events: " + ", ".join(catalog_extra))
    if catalog_excluded:
        errors.append("excluded expansion events leaked into catalog: " + ", ".join(catalog_excluded))
    if unexpected_duplicates:
        errors.append("unexpected duplicate catalog headings: " + ", ".join(unexpected_duplicates))

    graph_text = GRAPH.read_text(encoding="utf-8")
    edge_events: set[str] = set()
    edges: set[tuple[str, str]] = set()
    for match in CHAIN.finditer(graph_text):
        ids = [canon(token) for token in TOKEN.findall(match.group(1))]
        for event in ids:
            if event in excluded:
                errors.append(f"excluded event leaked into graph: {event}")
            elif event not in expected:
                errors.append(f"out-of-scope event leaked into graph: {event}")
            else:
                edge_events.add(event)
        for src, dst in zip(ids, ids[1:]):
            if src in expected and dst in expected and src != dst:
                edges.add((src, dst))

    coverage = {m.group(1) for m in map(COVERAGE.match, graph_text.splitlines()) if m}
    coverage_outside = sorted(coverage - expected, key=number)
    if coverage_outside:
        errors.append("out-of-scope coverage declarations: " + ", ".join(coverage_outside))

    classified = edge_events | coverage
    unclassified = sorted(expected - classified, key=number)
    if unclassified:
        errors.append("unclassified frozen events: " + ", ".join(unclassified))

    # Structural reachability: every explicit causal node must be reachable from
    # at least one structural root. This intentionally uses graph structure only.
    inbound = {event: set() for event in expected}
    outbound = {event: set() for event in expected}
    for src, dst in edges:
        outbound[src].add(dst)
        inbound[dst].add(src)
    causal_nodes = set(edge_events)
    roots = sorted((event for event in causal_nodes if not inbound[event]), key=number)
    reachable = set(roots)
    stack = list(roots)
    while stack:
        src = stack.pop()
        for dst in outbound[src]:
            if dst not in reachable:
                reachable.add(dst)
                stack.append(dst)
    unreachable_causal = sorted(causal_nodes - reachable, key=number)
    if unreachable_causal:
        errors.append("structurally unreachable causal nodes: " + ", ".join(unreachable_causal))

    inventory_status = "NOT_CHECKED"
    inventory_events = None
    if INVENTORY.exists():
        try:
            inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
            inventory_events = inventory.get("event_count")
            inventory_status = "PASS" if inventory_events == len(expected) else "FAIL"
            if inventory_status == "FAIL":
                errors.append(
                    f"scenario source inventory event_count expected {len(expected)}, got {inventory_events}"
                )
        except (OSError, json.JSONDecodeError) as exc:
            inventory_status = "FAIL"
            errors.append(f"cannot parse scenario-source-inventory.json: {exc}")
    else:
        # The inventory is generated by the dedicated CI workflow; running S01
        # locally before that workflow should remain actionable rather than
        # silently passing.
        inventory_status = "MISSING"
        errors.append("scenario-source-inventory.json is missing; run the source-inventory compiler first")

    result = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.s01_scenario_source_closure",
        "scope": "E01-E272",
        "excluded_events": sorted(excluded, key=number),
        "catalog_event_count": len(catalog_ids & expected),
        "expected_event_count": len(expected),
        "catalog_missing_count": len(catalog_missing),
        "catalog_extra_count": len(catalog_extra),
        "unexpected_duplicate_count": len(unexpected_duplicates),
        "graph_edge_count": len(edges),
        "graph_causal_event_count": len(causal_nodes),
        "graph_structural_root_count": len(roots),
        "graph_structurally_reachable_count": len(reachable),
        "graph_structurally_unreachable_count": len(unreachable_causal),
        "coverage_declaration_count": len(coverage),
        "classified_event_count": len(classified & expected),
        "unclassified_event_count": len(unclassified),
        "inventory_status": inventory_status,
        "inventory_event_count": inventory_events,
        "source_level_s01_closed": not errors,
        "source_level_percentage": 100 if not errors else 0,
        "runtime_gameplay_reachability_proven": False,
        "decision_engine_execution_proven": False,
        "fresh_run_reachability_proven": False,
        "replay_reachability_proven": False,
        "android_runtime_proven": False,
        "errors": errors,
        "boundary": "S01 source closure is not runtime/gameplay completion; runtime gates remain downstream of the Decision Engine.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "source_level_s01_closed": result["source_level_s01_closed"],
        "catalog_event_count": result["catalog_event_count"],
        "classified_event_count": result["classified_event_count"],
        "graph_structurally_unreachable_count": result["graph_structurally_unreachable_count"],
        "inventory_status": inventory_status,
        "errors": len(errors),
    }, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
