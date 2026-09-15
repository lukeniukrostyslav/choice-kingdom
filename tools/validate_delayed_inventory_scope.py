#!/usr/bin/env python3
"""Validate delayed-inventory source IDs against the authoritative catalog scope.

This is a source-level consistency gate. It does not infer timing, producer
semantics, cancellation, reachability, or runtime lifecycle behavior. It only
ensures that event IDs named by the delayed inventory are actually present in
one of the catalog sources declared by MACHINE_CANONICAL_GRAPH_01.json and are
inside frozen production scope.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
INVENTORY = ROOT / "docs" / "CANONICAL_DELAY_INVENTORY_01.md"
OUT = ROOT / "docs" / "MACHINE_DELAY_INVENTORY_SCOPE_01.json"

EVENT = re.compile(r"\bE(\d{2,3})\b")
RANGE = re.compile(r"E(\d{2,3})\s*[–-]\s*E(\d{2,3})")
HEADING = re.compile(r"^###\s+(E\d{2,3})\b")


def expand_inventory_ids(text: str) -> set[str]:
    ids: set[str] = set()
    for match in RANGE.finditer(text):
        start, end = int(match.group(1)), int(match.group(2))
        step = 1 if start <= end else -1
        ids.update(f"E{i:02d}" for i in range(start, end + step, step))
    for match in EVENT.finditer(text):
        ids.add(f"E{int(match.group(1)):02d}")
    return ids


def catalog_ids(manifest: dict) -> set[str]:
    ids: set[str] = set()
    for source in manifest["source_of_truth"]["catalog_sources"]:
        path = ROOT / source
        if not path.exists():
            raise SystemExit(f"missing catalog source: {source}")
        for line in path.read_text(encoding="utf-8").splitlines():
            match = HEADING.match(line.strip())
            if match:
                ids.add(match.group(1))
    return ids


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    inventory_text = INVENTORY.read_text(encoding="utf-8")
    referenced = expand_inventory_ids(inventory_text)
    available = catalog_ids(manifest)

    lo = int(manifest["scope"]["first_event"])
    hi = int(manifest["scope"]["last_event"])
    excluded = set(manifest["scope"].get("excluded_events", []))
    frozen = {f"E{i:02d}" for i in range(lo, hi + 1)} - excluded

    outside_scope = sorted(referenced - frozen, key=lambda x: int(x[1:]))
    missing_from_catalog = sorted(referenced - available, key=lambda x: int(x[1:]))

    errors: list[str] = []
    if outside_scope:
        errors.append("inventory references outside frozen scope: " + ", ".join(outside_scope))
    if missing_from_catalog:
        errors.append("inventory references IDs absent from catalog headings: " + ", ".join(missing_from_catalog))

    report = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.delayed_inventory_scope",
        "scope": f"E{lo:02d}-E{hi:02d}",
        "referenced_event_count": len(referenced),
        "catalog_event_count": len(available),
        "referenced_events": sorted(referenced, key=lambda x: int(x[1:])),
        "outside_scope": outside_scope,
        "missing_from_catalog": missing_from_catalog,
        "status": "PASS" if not errors else "BLOCKED",
        "semantic_timing_verified": False,
        "runtime_lifecycle_verified": False,
        "errors": errors,
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({"status": report["status"], "errors": len(errors), "referenced_event_count": len(referenced)}, sort_keys=True))
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
