#!/usr/bin/env python3
"""Validate the machine-readable Choice Kingdom canonical graph contract."""
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
HEADING_EVENT_RE = re.compile(r"^###\s+(E(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9]))\b")


def canonical_event(event_id: str) -> str:
    return event_id.split("-", 1)[0]


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    lo = manifest["scope"]["first_event"]
    hi = manifest["scope"]["last_event"]
    excluded = set(manifest["scope"]["excluded_events"])
    allowed_duplicate_ids = set(manifest.get("allowed_catalog_duplicate_event_ids", []))
    expected = {f"E{i:02d}" for i in range(lo, hi + 1)}
    errors: list[str] = []
    warnings: list[str] = []

    catalog_sources = [ROOT / p for p in manifest["source_of_truth"]["catalog_sources"]]
    required_files = [EVENT_GRAPH, PRODUCER_INVENTORY, *catalog_sources]
    for path in required_files:
        if not path.exists():
            errors.append(f"required source file is missing: {path.relative_to(ROOT)}")
    if errors:
        print("CANONICAL GRAPH VALIDATION: FAIL")
        for e in errors:
            print(f"ERROR: {e}")
        return 1

    graph_text = EVENT_GRAPH.read_text(encoding="utf-8")
    inventory_text = PRODUCER_INVENTORY.read_text(encoding="utf-8")

    catalog_counts: dict[str, int] = {}
    for path in catalog_sources:
        for line in path.read_text(encoding="utf-8").splitlines():
            match = HEADING_EVENT_RE.match(line.strip())
            if match:
                event_id = match.group(1)
                catalog_counts[event_id] = catalog_counts.get(event_id, 0) + 1

    missing_catalog = sorted(expected - set(catalog_counts))
    duplicate_catalog = sorted(e for e, count in catalog_counts.items() if count > 1 and e in expected and e not in allowed_duplicate_ids)
    allowed_duplicates_present = sorted(e for e, count in catalog_counts.items() if count > 1 and e in allowed_duplicate_ids)
    out_of_scope_catalog = sorted(e for e in catalog_counts if e not in expected and e not in excluded)
    excluded_catalog = sorted(e for e in catalog_counts if e in excluded)
    if missing_catalog:
        warnings.append(f"authoritative catalog source headings missing for {len(missing_catalog)} frozen IDs: {', '.join(missing_catalog)}")
    if duplicate_catalog:
        errors.append(f"authoritative catalog duplicates frozen event headings: {', '.join(duplicate_catalog)}")
    if allowed_duplicates_present:
        warnings.append(f"explicitly allowed bridge duplicate headings: {', '.join(allowed_duplicates_present)}")
    if out_of_scope_catalog:
        errors.append(f"authoritative catalog contains unexpected event IDs: {', '.join(out_of_scope_catalog)}")
    if excluded_catalog:
        warnings.append(f"excluded expansion headings are documented in selected catalog sources: {', '.join(excluded_catalog)}")

    edges: list[tuple[str, str]] = []
    referenced: set[str] = set()
    outbound: set[str] = set()
    inbound: set[str] = set()
    for match in CHAIN_RE.finditer(graph_text):
        ids = [canonical_event(x) for x in EVENT_TOKEN_RE.findall(match.group(1))]
        for event_id in ids:
            referenced.add(event_id)
            if event_id not in expected and event_id not in excluded:
                errors.append(f"out-of-scope event reference in graph chain: {event_id}")
        for src, dst in zip(ids, ids[1:]):
            if src in expected and dst in expected:
                edges.append((src, dst))
                outbound.add(src)
                inbound.add(dst)

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

    catalog_events = set(catalog_counts) & expected
    outbound_only_missing = sorted(catalog_events - outbound - inbound)
    inbound_only = sorted(catalog_events & inbound - outbound)
    terminal_or_consumer_candidates = sorted(catalog_events - outbound)
    if terminal_or_consumer_candidates:
        warnings.append(
            f"catalog events without outbound design edges: {len(terminal_or_consumer_candidates)}; "
            "these require terminal/consumer/qualification classification before orphan claims"
        )

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
        if row["event"] not in expected:
            errors.append(f"manifest producer outside frozen scope: {row['event']}")

    for row in manifest["delayed_consumers"]:
        consumer = row["consumer"]
        if consumer not in expected:
            errors.append(f"delayed consumer outside frozen scope: {consumer}")
        if row["status"] == "OPEN" and len(row.get("candidates", [])) > 1:
            warnings.append(f"open delayed source remains intentionally ambiguous: {consumer}")

    required_negatives = {"consumer_cannot_manufacture_prerequisite","excluded_events_cannot_enter_production","generic_compensation_route_cannot_union_sources","ordinary_history_cannot_be_meta_state"}
    actual_negatives = {x["id"] for x in manifest["hard_negatives"]}
    for item in sorted(required_negatives - actual_negatives):
        errors.append(f"missing mandatory hard-negative rule: {item}")

    report = {
        "frozen_scope": f"E{lo:02d}-E{hi}",
        "catalog_event_headings": len(catalog_counts),
        "catalog_frozen_event_headings": len(catalog_events),
        "catalog_missing_frozen_events": len(missing_catalog),
        "catalog_missing_frozen_event_ids": missing_catalog,
        "catalog_duplicate_frozen_events": len(duplicate_catalog),
        "allowed_catalog_duplicate_events": allowed_duplicates_present,
        "graph_edges_unique": len(seen),
        "graph_edges_repeated_in_design_doc": len(repeated_edges),
        "graph_event_nodes_referenced": len(referenced & expected),
        "graph_event_nodes_missing_from_design_graph": len(expected - referenced),
        "graph_events_without_outbound_edges": len(terminal_or_consumer_candidates),
        "graph_events_without_outbound_edge_ids": terminal_or_consumer_candidates,
        "graph_inbound_only_catalog_candidates": inbound_only,
        "graph_true_isolated_catalog_candidates": outbound_only_missing,
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
