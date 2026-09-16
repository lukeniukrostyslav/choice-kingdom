#!/usr/bin/env python3
"""Close the source-level canonical graph contract without inventing runtime semantics.

S09 covers the canonical graph as a source contract: frozen event coverage,
scope integrity, catalog/graph node parity, and explicit classification of
non-runtime causal edges. Runtime gameplay reachability and engine execution
remain separate gates.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
GRAPH = ROOT / "docs" / "EVENT_GRAPH.md"
HEADING = re.compile(r"^###\s+(E(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9]))\b")
TOKEN = re.compile(r"\bE(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9])(?:-[A-Z])?\b")
CHAIN = re.compile(r"`([^`]*->[^`]*)`")


def canon(token: str) -> str:
    return token.split("-", 1)[0]


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    lo = manifest["scope"]["first_event"]
    hi = manifest["scope"]["last_event"]
    expected = {f"E{i:02d}" for i in range(lo, hi + 1)}
    excluded = set(manifest["scope"]["excluded_events"])

    catalog_ids: set[str] = set()
    for source in manifest["source_of_truth"]["catalog_sources"]:
        path = ROOT / source
        if not path.exists():
            raise SystemExit(f"missing catalog source: {source}")
        for line in path.read_text(encoding="utf-8").splitlines():
            m = HEADING.match(line.strip())
            if m:
                catalog_ids.add(m.group(1))

    graph_ids: set[str] = set()
    edges: set[tuple[str, str]] = set()
    for match in CHAIN.finditer(GRAPH.read_text(encoding="utf-8")):
        ids = [canon(x) for x in TOKEN.findall(match.group(1))]
        for event in ids:
            if event in expected:
                graph_ids.add(event)
            elif event not in excluded:
                raise SystemExit(f"out-of-scope graph event: {event}")
        edges.update((a, b) for a, b in zip(ids, ids[1:]) if a in expected and b in expected)

    errors: list[str] = []
    missing_catalog = sorted(expected - catalog_ids, key=lambda x: int(x[1:]))
    missing_graph = sorted(expected - graph_ids, key=lambda x: int(x[1:]))
    excluded_leaks = sorted(graph_ids & excluded, key=lambda x: int(x[1:]))
    if missing_catalog:
        errors.append(f"missing authoritative catalog headings: {', '.join(missing_catalog)}")
    if missing_graph:
        errors.append(f"missing frozen graph node references: {', '.join(missing_graph)}")
    if excluded_leaks:
        errors.append(f"excluded expansion nodes leaked into graph: {', '.join(excluded_leaks)}")

    report = {
        "schema_version": "1.0",
        "scope": f"E{lo:02d}-E{hi}",
        "catalog_nodes": len(catalog_ids & expected),
        "graph_nodes": len(graph_ids & expected),
        "unique_in_scope_edges": len(edges),
        "catalog_graph_node_parity_proven": not missing_catalog and not missing_graph,
        "excluded_scope_integrity_proven": not excluded_leaks,
        "source_level_canonical_graph_closed": not errors,
        "runtime_gameplay_reachability_proven": False,
        "runtime_engine_execution_proven": False,
        "semantic_boundary": "Every graph edge is a frozen design-level causal candidate. No edge is promoted to runtime semantics by this gate.",
        "errors": errors,
    }
    out = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_CLOSURE_01.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
