#!/usr/bin/env python3
"""Validate the source-level causal reachability contract for E01-E272.

S07 closes the authored causal-graph structure only. It does NOT claim
conditional gameplay feasibility, runtime engine execution, replay execution,
or ending precedence. Those remain downstream runtime gates.

The graph contract requires frozen scope, no self-loops, complete event
classification, and every event participating in an explicit causal edge to
be reachable from at least one structural causal root. Directed cycles are
reported as feedback candidates rather than rejected: the source graph may
contain authored feedback relationships, but those relationships do not by
themselves prove a playable loop.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
GRAPH = ROOT / "docs" / "EVENT_GRAPH.md"
OUT = ROOT / "docs" / "MACHINE_CAUSAL_REACHABILITY_01.json"
TOKEN = re.compile(r"\bE(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9])(?:-[A-Z])?\b")
CHAIN = re.compile(r"`([^`]*->[^`]*)`")
COVERAGE = re.compile(r"^-\s+(E(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9]))\s+—\s+coverage declaration only\s*$")
EXPECTED_CAUSAL_EDGE_COUNT = 305
EXPECTED_CAUSAL_NODE_COUNT = 221


def canon(value: str) -> str:
    return value.split("-", 1)[0]


def key(value: str) -> int:
    return int(value[1:])


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    first = int(manifest["scope"]["first_event"])
    last = int(manifest["scope"]["last_event"])
    events = {f"E{i:02d}" for i in range(first, last + 1)}
    excluded = set(manifest["scope"]["excluded_events"])
    text = GRAPH.read_text(encoding="utf-8")

    edges: set[tuple[str, str]] = set()
    inbound: dict[str, set[str]] = defaultdict(set)
    outbound: dict[str, set[str]] = defaultdict(set)
    errors: list[str] = []

    for match in CHAIN.finditer(text):
        ids = [canon(token) for token in TOKEN.findall(match.group(1))]
        for event in ids:
            if event in excluded:
                errors.append(f"excluded event leaked into causal graph: {event}")
            elif event not in events:
                errors.append(f"out-of-scope event in causal graph: {event}")
        for src, dst in zip(ids, ids[1:]):
            if src not in events or dst not in events:
                continue
            if src == dst:
                errors.append(f"self-loop: {src} -> {dst}")
                continue
            edges.add((src, dst))
            outbound[src].add(dst)
            inbound[dst].add(src)

    coverage = {m.group(1) for m in map(COVERAGE.match, text.splitlines()) if m}
    for event in coverage:
        if event not in events:
            errors.append(f"out-of-scope coverage declaration: {event}")

    edge_events = {event for edge in edges for event in edge}
    missing_classification = sorted(events - edge_events - coverage, key=key)
    if missing_classification:
        errors.append(
            "events lacking either causal-edge participation or explicit "
            f"coverage classification: {', '.join(missing_classification)}"
        )

    if len(edges) != EXPECTED_CAUSAL_EDGE_COUNT:
        errors.append(
            f"causal edge cardinality drift: expected {EXPECTED_CAUSAL_EDGE_COUNT}, got {len(edges)}"
        )
    if len(edge_events) != EXPECTED_CAUSAL_NODE_COUNT:
        errors.append(
            f"causal node cardinality drift: expected {EXPECTED_CAUSAL_NODE_COUNT}, got {len(edge_events)}"
        )

    causal_nodes = edge_events
    roots = sorted((e for e in causal_nodes if not inbound[e]), key=key)
    reachable = set(roots)
    stack = list(roots)
    while stack:
        src = stack.pop()
        for dst in outbound[src]:
            if dst not in reachable:
                reachable.add(dst)
                stack.append(dst)

    unreachable_causal = sorted(causal_nodes - reachable, key=key)
    if unreachable_causal:
        errors.append(
            "causal nodes are not reachable from a structural causal root: "
            + ", ".join(unreachable_causal)
        )

    index = 0
    indices: dict[str, int] = {}
    lowlink: dict[str, int] = {}
    stack_nodes: list[str] = []
    on_stack: set[str] = set()
    cyclic_components: list[list[str]] = []

    def strongconnect(node: str) -> None:
        nonlocal index
        indices[node] = index
        lowlink[node] = index
        index += 1
        stack_nodes.append(node)
        on_stack.add(node)
        for nxt in outbound[node]:
            if nxt not in causal_nodes:
                continue
            if nxt not in indices:
                strongconnect(nxt)
                lowlink[node] = min(lowlink[node], lowlink[nxt])
            elif nxt in on_stack:
                lowlink[node] = min(lowlink[node], indices[nxt])
        if lowlink[node] == indices[node]:
            component: list[str] = []
            while True:
                member = stack_nodes.pop()
                on_stack.remove(member)
                component.append(member)
                if member == node:
                    break
            if len(component) > 1:
                cyclic_components.append(sorted(component, key=key))

    for node in sorted(causal_nodes, key=key):
        if node not in indices:
            strongconnect(node)

    cyclic_components.sort(key=lambda component: key(component[0]))

    report = {
        "schema_version": "1.2",
        "scope": "E01-E272",
        "excluded_events": sorted(excluded, key=key),
        "causal_edge_count": len(edges),
        "expected_causal_edge_count": EXPECTED_CAUSAL_EDGE_COUNT,
        "causal_node_count": len(causal_nodes),
        "expected_causal_node_count": EXPECTED_CAUSAL_NODE_COUNT,
        "structural_root_count": len(roots),
        "structural_roots": roots,
        "causal_nodes_reachable_from_structural_root": len(reachable),
        "causal_nodes_unreachable_from_structural_root": len(unreachable_causal),
        "coverage_classification_count": len(coverage),
        "coverage_classification_nodes": sorted(coverage, key=key),
        "directed_feedback_component_count": len(cyclic_components),
        "directed_feedback_components": cyclic_components,
        "source_level_causal_reachability_closed": not errors,
        "runtime_gameplay_reachability_proven": False,
        "runtime_engine_execution_proven": False,
        "replay_reachability_proven": False,
        "ending_precedence_proven": False,
        "semantic_boundary": (
            "S07 source closure proves that every explicit causal edge belongs "
            "to a rooted structural component and every event is classified. "
            "Feedback components are reported, not treated as runtime loops. "
            "No conditional gameplay feasibility or runtime execution is inferred."
        ),
        "errors": errors,
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
