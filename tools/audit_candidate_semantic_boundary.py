#!/usr/bin/env python3
"""Build a deterministic semantic-boundary inventory for graph candidates.

This tool intentionally does not infer true orphans. It cross-references the
machine node-classification inventory with explicit delayed/replay/endgame
registries and emits a conservative queue for authoritative-source review.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASSIFICATION = ROOT / "docs" / "MACHINE_GRAPH_NODE_CLASSIFICATION_01.json"
MANIFEST = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
OUT = ROOT / "docs" / "MACHINE_CANDIDATE_SEMANTIC_BOUNDARY_01.json"


def main() -> int:
    classification = json.loads(CLASSIFICATION.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    delayed = {row["consumer"] for row in manifest.get("delayed_consumers", [])}
    replay = {f"E{i:02d}" for i in range(247, 251)}
    endings = {f"E{i:02d}" for i in range(265, 271)}

    queues: dict[str, list[str]] = {
        "SOURCE_MISSING": [],
        "REPLAY_ONLY_REVIEW": [],
        "DELAYED_CALLBACK_REVIEW": [],
        "ENDING_OR_TERMINAL_REVIEW": [],
        "ROOT_SOURCE_REVIEW": [],
        "CONSUMER_ONLY_REVIEW": [],
        "ISOLATED_HIGH_PRIORITY_REVIEW": [],
    }

    for row in classification["nodes"]:
        event = row["event"]
        category = row["category"]
        if category == "SOURCE_MISSING":
            queues["SOURCE_MISSING"].append(event)
        elif event in replay:
            queues["REPLAY_ONLY_REVIEW"].append(event)
        elif event in delayed:
            queues["DELAYED_CALLBACK_REVIEW"].append(event)
        elif event in endings and not row["outbound"]:
            queues["ENDING_OR_TERMINAL_REVIEW"].append(event)
        elif category == "ROOT_CANDIDATE":
            queues["ROOT_SOURCE_REVIEW"].append(event)
        elif category == "TERMINAL_OR_CONSUMER_CANDIDATE":
            queues["CONSUMER_ONLY_REVIEW"].append(event)
        elif category == "ISOLATED_CANDIDATE":
            queues["ISOLATED_HIGH_PRIORITY_REVIEW"].append(event)

    for values in queues.values():
        values.sort(key=lambda x: int(x[1:]))

    report = {
        "schema_version": "1.0",
        "scope": "E01-E272",
        "excluded_events": manifest["scope"]["excluded_events"],
        "is_semantic_reachability_proof": False,
        "is_true_orphan_detector": False,
        "queues": queues,
        "counts": {key: len(value) for key, value in queues.items()},
        "rules": [
            "degree alone never proves orphanhood",
            "SOURCE_MISSING remains open until authoritative source is recovered",
            "replay events remain isolated from ordinary meta state",
            "delayed consumers require lifecycle/source validation",
            "ending/terminal candidates require incoming-path and precedence review",
            "root candidates may be intentional source events",
            "consumer-only candidates may be valid terminal consumers",
            "isolated candidates require authoritative source inspection before any orphan verdict",
            "E273-E277 are excluded from production semantics",
        ],
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report["counts"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
