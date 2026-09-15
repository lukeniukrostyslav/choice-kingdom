#!/usr/bin/env python3
"""Produce a conservative candidate-triage inventory for E01-E272.

This tool never declares true orphans from graph degree alone. It combines the
machine graph classification with explicit source-registry references and emits
review queues for semantic QA.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASSIFICATION = ROOT / "docs" / "MACHINE_GRAPH_NODE_CLASSIFICATION_01.json"
MATRIX = ROOT / "docs" / "MACHINE_PRODUCER_CONSUMER_MATRIX_01.json"
OUT = ROOT / "docs" / "MACHINE_CANDIDATE_TRIAGE_01.json"


def main() -> int:
    classification = json.loads(CLASSIFICATION.read_text(encoding="utf-8"))
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    producer_events = set()
    consumer_events = set()
    for row in matrix.get("rows", []):
        producer_events.update(row.get("producer_events", []))
        consumer_events.update(row.get("consumer_events", []))

    unreferenced = []
    no_outbound = []
    inbound_only = []
    for node in classification["nodes"]:
        event = node["event"]
        if event not in producer_events and event not in consumer_events:
            unreferenced.append(event)
        if not node["outbound"]:
            no_outbound.append(event)
        if node["inbound"] and not node["outbound"]:
            inbound_only.append(event)

    report = {
        "schema_version": "1.0",
        "scope": "E01-E272",
        "semantic_triage_only": True,
        "true_orphans_declared": False,
        "queues": {
            "unreferenced_registry_candidates": sorted(set(unreferenced), key=lambda x: int(x[1:])),
            "no_outbound_candidates": sorted(set(no_outbound), key=lambda x: int(x[1:])),
            "inbound_only_candidates": sorted(set(inbound_only), key=lambda x: int(x[1:])),
            "ending_candidates": [f"E{i:02d}" for i in range(265, 271)],
            "replay_candidates": [f"E{i:02d}" for i in range(247, 251)],
        },
        "hard_rules": [
            "degree alone cannot prove orphanhood",
            "consumer cannot manufacture prerequisite",
            "meta state cannot contaminate fresh-run state",
            "E273-E277 excluded from production reachability",
        ],
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: len(v) for k, v in report["queues"].items()}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
