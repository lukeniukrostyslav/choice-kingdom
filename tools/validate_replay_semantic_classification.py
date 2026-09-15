#!/usr/bin/env python3
"""Validate the conservative replay-vs-ordinary semantic classification."""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "MACHINE_REPLAY_SEMANTIC_CLASSIFICATION_01.json"
SOURCE = ROOT / "docs" / "SCENARIO_QA_REPLAY_SEMANTIC_CLASSIFICATION_01.md"
EXPECTED = {
    "E186": ("REPLAY_DEPENDENT", True),
    "E247": ("REPLAY_DEPENDENT", True),
    "E248": ("REPLAY_DEPENDENT", True),
    "E249": ("ORDINARY_STATE", False),
    "E250": ("ORDINARY_STATE", False),
    "E270": ("ORDINARY_STATE", False),
}


def main() -> int:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    source = SOURCE.read_text(encoding="utf-8")
    errors: list[str] = []
    records = {row["event"]: row for row in contract.get("records", [])}
    if set(records) != set(EXPECTED):
        errors.append(f"record scope mismatch: {sorted(records)}")
    for event, (classification, producer_required) in EXPECTED.items():
        row = records.get(event, {})
        if row.get("classification") != classification:
            errors.append(f"{event}: classification mismatch")
        if row.get("meta_producer_required") is not producer_required:
            errors.append(f"{event}: meta_producer_required mismatch")
        if event not in source:
            errors.append(f"{event}: source classification missing")
    if contract.get("classification_status") != "CLOSED":
        errors.append("classification_status must be CLOSED")
    if contract.get("runtime_verified") is not False:
        errors.append("runtime_verified must remain false")
    status = "PASS" if not errors else "BLOCKED"
    print(json.dumps({"status": status, "records": len(records), "errors": len(errors)}, sort_keys=True))
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
