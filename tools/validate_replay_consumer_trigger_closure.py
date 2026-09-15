#!/usr/bin/env python3
"""Validate the source-closed replay consumer trigger boundary without promoting replay runtime semantics."""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "MACHINE_REPLAY_CONSUMER_TRIGGER_CLOSURE_01.json"
SOURCE = ROOT / "docs" / "SCENARIO_QA_REPLAY_CONSUMER_TRIGGER_CLOSURE_01.md"
EXPECTED = {"E186", "E247", "E248", "E249", "E250", "E270"}


def main() -> int:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    source = SOURCE.read_text(encoding="utf-8")
    errors: list[str] = []
    records = {row["event"]: row for row in contract.get("records", [])}
    if set(records) != EXPECTED:
        errors.append(f"record scope mismatch: {sorted(records)}")
    for event in sorted(EXPECTED):
        row = records.get(event, {})
        if row.get("meta_producer") != "OPEN":
            errors.append(f"{event}: meta producer must remain OPEN")
        if f"{event}" not in source:
            errors.append(f"{event}: source QA document does not mention consumer")
    for key in ("runtime_verified", "fresh_run_isolation_verified", "replay_reachability_verified", "save_load_isolation_verified", "ending_qualification_verified"):
        if contract.get(key) is not False:
            errors.append(f"{key} must remain false until runtime evidence exists")
    if contract.get("consumer_trigger_status") != "CLOSED":
        errors.append("consumer_trigger_status must be CLOSED")
    if contract.get("persistent_meta_producer_status") != "OPEN":
        errors.append("persistent_meta_producer_status must remain OPEN")
    status = "PASS" if not errors else "BLOCKED"
    print(json.dumps({"status": status, "consumer_count": len(records), "errors": len(errors)}, sort_keys=True))
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
