#!/usr/bin/env python3
"""Validate the source-level causal reachability contract for E01-E272.

S07 closes only the graph's authored causal structure. It does NOT claim
conditional gameplay reachability, runtime engine execution, replay execution,
or ending precedence. Those remain downstream runtime gates.

A valid graph must have:
- frozen E01-E272 scope with no excluded-event leakage;
- no self-loops;
- no directed causal cycles;
- every causal edge belongs to a rooted directed component;
- every event without a causal edge is explicitly declared as coverage-only;
- no causal edge may be inferred from a coverage declaration;
- coverage-only nodes remain explicitly non-causal.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
GRAPH = ROOT / "docs" / "EVENT_GRAPH.md"
OUT = ROOT / "docs" / "MACHINE_CAUSAL_REACHABILITY_01.json"
TOKEN = re.compile(r"\bE(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9])(?:-[A-Z])?\b")
CHAIN = re.compile(r"`([^`]*->[^`]*)`")
COVERAGE = re.compile(r"^-\s+(E(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9]))\s+—\s+coverage declaration only\s*$")


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
    referenced: set[str] = set()
    errors: list[str] = []

    for match in CHAIN.finditer(text):
        ids = [canon(token) for token in TOKEN.findall(match.group(1))]
        for event in ids:
            if event in excluded:
                errors.append(f"excluded event leaked into causal graph: {event}")
            elif event not in events:
                errors.append(f"out-of-scope event in causal graph: {event}")
            else:
                referenced.add(event)
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

    # Every event not participating in a causal edge must be explicitly
    # coverage-declared. This preserves the authored distinction between
    # node inventory and causal semantics.
    edge_events = {e for edge in edges for e in edge}
    missing_classification = sorted(events - edge_events - coverage, key=key)
    if missing_classification:
        errors.append(
            "events lacking either causal-edge participation or explicit "
            f"coverage classification: {', '.join(missing_classification)}"
        )

    # Kahn topological check: cycles are invalid because they would create
    # circular causal prerequisites at source level.
    indegree = {event: len(inbound[event]) for event in events}
    queue = deque(sorted((e for e in events if indegree[e] == 0), key=key))
    topo: list[str] = []
    while queue:
        src = queue.popleft()
        topo.append(src)
        for dst in sorted(outbound[src], key=key):
            indegree[dst] -= 1
            if indegree[dst] == 0:
                queue.append(dst)
    cyclic = sorted(events - set(topo), key=key)
    if cyclic:
        errors.append(f"directed causal cycle detected: {', '.join(cyclic)}")

    # A causal component is rooted if at least one node has no inbound causal
    # edge. Coverage-only nodes are deliberately excluded from this test.
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

    # Coverage-only nodes must have no causal edges. This prevents a future
    # edit from silently upgrading inventory declarations into semantics.
    coverage_edge_leaks = sorted(coverage & edge_events, key=key)
    if coverage_edge_leaks:
        errors.append(
            "coverage-only nodes also participate in causal edges: "
            + ", ".join(coverage_edge_leaks)
        )

    report = {
        "schema_version": "1.0",
        "scope": "E01-E272",
        "excluded_events": sorted(excluded, key=key),
        "causal_edge_count": len(edges),
        "causal_node_count": len(causal_nodes),
        "structural_root_count": len(roots),
        "structural_roots": roots,
        "causal_nodes_reachable_from_structural_root": len(reachable),
        "causal_nodes_unreachable_from_structural_root": len(unreachable_causal),
        "coverage_only_node_count": len(coverage),
        "coverage_only_nodes": sorted(coverage, key=key),
        "directed_cycle_count": 1 if cyclic else 0,
        "cycle_nodes": cyclic,
        "source_level_causal_reachability_closed": not errors,
        "runtime_gameplay_reachability_proven": False,
        "runtime_engine_execution_proven": False,
        "replay_reachability_proven": False,
        "ending_precedence_proven": False,
        "semantic_boundary": (
            "S07 source closure proves only that every authored causal edge is "
            "rooted and acyclic and every non-edge event is explicitly classified. "
            "It does not infer conditional gameplay feasibility or runtime execution."
        ),
        "errors": errors,
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
