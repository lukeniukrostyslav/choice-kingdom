#!/usr/bin/env python3
"""Audit structural reachability of the frozen E01-E272 design graph.

This is deliberately weaker than gameplay reachability: EVENT_GRAPH.md contains
structural design edges, not the complete conditional state machine. The report
identifies structural roots, graph reachability, weakly connected components,
and sink candidates. It never declares a gameplay orphan or an ending as
reachable merely because an edge exists.
"""
from __future__ import annotations

import json
import re
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
GRAPH = ROOT / "docs" / "EVENT_GRAPH.md"
OUT = ROOT / "docs" / "MACHINE_STRUCTURAL_REACHABILITY_01.json"
TOKEN = re.compile(r"\bE(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9])(?:-[A-Z])?\b")
CHAIN = re.compile(r"`([^`]*->[^`]*)`")


def canon(value: str) -> str:
    return value.split("-", 1)[0]


def event_key(value: str) -> int:
    return int(value[1:])


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    first = manifest["scope"]["first_event"]
    last = manifest["scope"]["last_event"]
    events = {f"E{i:02d}" for i in range(first, last + 1)}
    excluded = set(manifest["scope"]["excluded_events"])
    graph_text = GRAPH.read_text(encoding="utf-8")
    edges: set[tuple[str, str]] = set()
    inbound = {event: set() for event in events}
    outbound = {event: set() for event in events}

    for match in CHAIN.finditer(graph_text):
        ids = [canon(token) for token in TOKEN.findall(match.group(1))]
        for src, dst in zip(ids, ids[1:]):
            if src in events and dst in events and src != dst:
                edges.add((src, dst))
                outbound[src].add(dst)
                inbound[dst].add(src)

    roots = sorted((event for event in events if not inbound[event]), key=event_key)
    reachable = set(roots)
    frontier = list(roots)
    while frontier:
        src = frontier.pop()
        for dst in outbound[src]:
            if dst not in reachable:
                reachable.add(dst)
                frontier.append(dst)

    structurally_unreachable = sorted(events - reachable, key=event_key)
    sink_candidates = sorted(
        (event for event in events if not outbound[event]), key=event_key
    )

    # Weakly connected components expose graph islands without implying playability.
    undirected = {event: set() for event in events}
    for src, dst in edges:
        undirected[src].add(dst)
        undirected[dst].add(src)
    components: list[list[str]] = []
    unseen = set(events)
    while unseen:
        seed = min(unseen, key=event_key)
        queue = deque([seed])
        component: set[str] = set()
        unseen.remove(seed)
        while queue:
            node = queue.popleft()
            component.add(node)
            for neighbour in undirected[node]:
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    queue.append(neighbour)
        components.append(sorted(component, key=event_key))
    components.sort(key=lambda component: (event_key(component[0]), len(component)))

    report = {
        "schema_version": "1.1",
        "scope": "E01-E272",
        "excluded_events": sorted(excluded),
        "edge_count": len(edges),
        "root_count": len(roots),
        "roots": roots,
        "structurally_reachable_count": len(reachable),
        "structurally_unreachable_count": len(structurally_unreachable),
        "structurally_unreachable": structurally_unreachable,
        "sink_candidate_count": len(sink_candidates),
        "sink_candidates": sink_candidates,
        "weak_component_count": len(components),
        "weak_component_sizes": [len(component) for component in components],
        "weak_components": components,
        "is_gameplay_reachability_proof": False,
        "is_orphan_detector": False,
        "interpretation": [
            "A graph root is structural, not necessarily a playable fresh-run entry point.",
            "Structural reachability does not prove conditional feasibility, state prerequisites, timing, or ending precedence.",
            "A structurally unreachable node requires source/graph review but is not automatically an orphan.",
            "A sink candidate is only a graph-degree observation; it may be an authored terminal, consumer, delayed callback, or incomplete graph edge.",
            "Weakly disconnected components identify graph islands for source review and do not prove gameplay isolation.",
            "Replay/meta transfer is not inferred from ordinary graph edges.",
            "E273-E277 are excluded from the production graph scope.",
        ],
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        k: report[k]
        for k in (
            "edge_count",
            "root_count",
            "structurally_reachable_count",
            "structurally_unreachable_count",
            "sink_candidate_count",
            "weak_component_count",
        )
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
