#!/usr/bin/env python3
"""Validate bounded event-ID parity between the frozen catalog and design graph.

The design graph is a causal-map artifact and intentionally does not have to
enumerate every catalog event. This gate therefore rejects scope violations,
unexpected catalog IDs and unexpected duplicate headings, while reporting
catalog IDs absent from graph chains as an explicit coverage delta. It is not a
semantic-equality or gameplay-reachability proof.
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
    duplicate_counts: dict[str, int] = {}
    for source in manifest["source_of_truth"]["catalog_sources"]:
        path = ROOT / source
        if not path.exists():
            raise SystemExit(f"missing catalog source: {source}")
        for line in path.read_text(encoding="utf-8").splitlines():
            match = HEADING.match(line.strip())
            if match:
                event = match.group(1)
                catalog_ids.add(event)
                duplicate_counts[event] = duplicate_counts.get(event, 0) + 1

    graph_ids: set[str] = set()
    for match in CHAIN.finditer(GRAPH.read_text(encoding="utf-8")):
        for token in TOKEN.findall(match.group(1)):
            event = canon(token)
            if event in expected:
                graph_ids.add(event)

    catalog_only = sorted(catalog_ids - graph_ids - excluded, key=lambda x: int(x[1:]))
    graph_only = sorted(graph_ids - expected - excluded, key=lambda x: int(x[1:]))
    unexpected_catalog = sorted(catalog_ids - expected - excluded, key=lambda x: int(x[1:]))
    allowed_duplicates = sorted(
        event for event, count in duplicate_counts.items()
        if count > 1 and event in manifest.get("allowed_catalog_duplicate_event_ids", [])
    )
    unexpected_duplicates = sorted(
        event for event, count in duplicate_counts.items()
        if count > 1 and event in expected and event not in allowed_duplicates
    )

    errors: list[str] = []
    if graph_only:
        errors.append(f"graph contains non-frozen/non-excluded event IDs: {', '.join(graph_only)}")
    if unexpected_catalog:
        errors.append(f"catalog contains non-frozen/non-excluded event IDs: {', '.join(unexpected_catalog)}")
    if unexpected_duplicates:
        errors.append(f"unexpected duplicate catalog headings: {', '.join(unexpected_duplicates)}")

    report = {
        "schema_version": "1.1",
        "scope": f"E{lo:02d}-E{hi}",
        "catalog_event_ids": len(catalog_ids & expected),
        "graph_event_ids": len(graph_ids & expected),
        "catalog_only_ids": catalog_only,
        "catalog_only_count": len(catalog_only),
        "graph_only_ids": graph_only,
        "unexpected_catalog_ids": unexpected_catalog,
        "allowed_duplicate_ids": allowed_duplicates,
        "unexpected_duplicate_ids": unexpected_duplicates,
        "errors": errors,
        "semantic_equality_proven": False,
        "graph_catalog_id_coverage_proven": not errors,
        "interpretation": [
            "The causal design graph is allowed to be a partial map of the full catalog.",
            "Catalog-only IDs are a coverage delta for source/graph review, not an integrity failure by themselves.",
            "ID parity remains necessary for any graph-represented event but is insufficient for semantic equality.",
            "No outbound graph edge is not treated as an error because terminal/consumer/qualification roles may be valid.",
            "E273-E277 remain excluded from frozen production semantics.",
        ],
    }
    out = ROOT / "docs" / "MACHINE_CATALOG_GRAPH_PARITY_01.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "catalog_event_ids": report["catalog_event_ids"],
        "graph_event_ids": report["graph_event_ids"],
        "catalog_only_ids": report["catalog_only_count"],
        "errors": len(errors),
    }, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
