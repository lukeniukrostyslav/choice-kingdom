#!/usr/bin/env python3
"""Classify E01-E272 graph nodes without promoting heuristics to runtime truth.

This is a QA inventory only. It deliberately distinguishes degree-based candidates
from authoritative semantic classifications; missing source text remains OPEN.
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


def canon(value: str) -> str:
    return value.split("-", 1)[0]


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected = {f"E{i:02d}" for i in range(manifest["scope"]["first_event"], manifest["scope"]["last_event"] + 1)}
    excluded = set(manifest["scope"]["excluded_events"])
    catalog_ids: set[str] = set()
    for source in manifest["source_of_truth"]["catalog_sources"]:
        for line in (ROOT / source).read_text(encoding="utf-8").splitlines():
            m = HEADING.match(line.strip())
            if m:
                catalog_ids.add(m.group(1))

    graph_text = GRAPH.read_text(encoding="utf-8")
    inbound: dict[str, set[str]] = {e: set() for e in expected}
    outbound: dict[str, set[str]] = {e: set() for e in expected}
    for match in CHAIN.finditer(graph_text):
        ids = [canon(x) for x in TOKEN.findall(match.group(1))]
        for src, dst in zip(ids, ids[1:]):
            if src in expected and dst in expected:
                outbound[src].add(dst)
                inbound[dst].add(src)

    delayed = {row["consumer"] for row in manifest.get("delayed_consumers", [])}
    replay = {f"E{i:02d}" for i in range(247, 251)}
    endgame = {f"E{i:02d}" for i in range(265, 271)}

    rows = []
    for event in sorted(expected, key=lambda x: int(x[1:])):
        ins, outs = inbound[event], outbound[event]
        reasons: list[str] = []
        if event not in catalog_ids:
            category = "SOURCE_MISSING"
            reasons.append("no authoritative catalog heading in configured source set")
        elif event in replay:
            category = "REPLAY_CANDIDATE"
            reasons.append("inside E247-E250 replay-divergence layer")
        elif event in delayed:
            category = "DELAYED_CONSUMER_CANDIDATE"
            reasons.append("listed in canonical delayed-consumer registry")
        elif event in endgame and not outs:
            category = "TERMINAL_OR_ENDING_CANDIDATE"
            reasons.append("late endgame node with no outbound design edge")
        elif not ins and not outs:
            category = "ISOLATED_CANDIDATE"
            reasons.append("zero graph degree; not yet a true-orphan verdict")
        elif not ins:
            category = "ROOT_CANDIDATE"
            reasons.append("no inbound design edge")
        elif not outs:
            category = "TERMINAL_OR_CONSUMER_CANDIDATE"
            reasons.append("no outbound design edge")
        else:
            category = "ORDINARY_GRAPH_NODE"
            reasons.append("has inbound and outbound design edges")
        rows.append({"event": event, "category": category, "inbound": sorted(ins), "outbound": sorted(outs), "reasons": reasons})

    summary: dict[str, int] = {}
    for row in rows:
        summary[row["category"]] = summary.get(row["category"], 0) + 1

    report = {
        "schema_version": "1.0",
        "scope": "E01-E272",
        "excluded": sorted(excluded),
        "catalog_headings_found": len(catalog_ids),
        "catalog_headings_missing": sorted(expected - catalog_ids),
        "classification_is_not_reachability_proof": True,
        "summary": summary,
        "nodes": rows,
    }
    out = ROOT / "docs" / "MACHINE_GRAPH_NODE_CLASSIFICATION_01.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"scope": report["scope"], "catalog_headings_found": len(catalog_ids), "summary": summary, "missing_catalog": sorted(expected - catalog_ids)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
