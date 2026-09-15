#!/usr/bin/env python3
"""Compile the working producer/consumer registry into a machine QA matrix.

The output is derived QA data, never runtime input. OPEN/PARTIAL rows remain
open; this tool does not invent aliases or turn prose into producers.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs" / "CANONICAL_PRODUCER_CONSUMER_REGISTRY_01.md"
MANIFEST = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
ROW = re.compile(r"^\|\s*`?([^|]+?)`?\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|$")
EVENT = re.compile(r"\bE(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9])(?:-[A-Z])?\b")


def canonical(value: str) -> str:
    return value.split("-", 1)[0]


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    lo, hi = manifest["scope"]["first_event"], manifest["scope"]["last_event"]
    expected = {f"E{i:02d}" for i in range(lo, hi + 1)}
    excluded = set(manifest["scope"]["excluded_events"])

    rows = []
    errors = []
    for line in REGISTRY.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if not m or m.group(1).strip() in {"Canonical key / family", "---"}:
            continue
        key, kind, producers, consumers, status, note = [x.strip() for x in m.groups()]
        producer_events = sorted({canonical(x) for x in EVENT.findall(producers)})
        consumer_events = sorted({canonical(x) for x in EVENT.findall(consumers)})
        bad = sorted((set(producer_events) | set(consumer_events)) - expected - excluded)
        if bad:
            errors.append(f"{key}: out-of-scope registry event(s): {', '.join(bad)}")
        excluded_refs = sorted((set(producer_events) | set(consumer_events)) & excluded)
        if excluded_refs:
            errors.append(f"{key}: excluded production contamination: {', '.join(excluded_refs)}")
        rows.append({
            "key": key,
            "type": kind,
            "producer_events": producer_events,
            "consumer_events": consumer_events,
            "status": status,
            "qa_note": note,
        })

    summary = {}
    for row in rows:
        summary[row["status"]] = summary.get(row["status"], 0) + 1

    report = {
        "schema_version": "1.0",
        "scope": f"E{lo:02d}-E{hi}",
        "source": str(REGISTRY.relative_to(ROOT)),
        "runtime_input": False,
        "rows": rows,
        "summary_by_status": summary,
        "errors": errors,
        "open_rows": [r["key"] for r in rows if "OPEN" in r["status"] or "PARTIAL" in r["status"]],
    }
    out = ROOT / "docs" / "MACHINE_PRODUCER_CONSUMER_MATRIX_01.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "summary_by_status": summary, "open_or_partial": len(report["open_rows"]), "errors": errors}, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
