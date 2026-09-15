#!/usr/bin/env python3
"""Validate the conservative replay producer provenance contract."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "MACHINE_REPLAY_PRODUCER_PROVENANCE_01.json"

REQUIRED = {"E186", "E247", "E248"}
FORBIDDEN_CONSUMERS = {"E249", "E250", "E270"}


def main() -> int:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    records = data.get("records", [])
    by_consumer = {record.get("consumer"): record for record in records}

    if set(by_consumer) != REQUIRED:
        raise SystemExit(
            f"replay provenance scope mismatch: expected {sorted(REQUIRED)}, "
            f"got {sorted(by_consumer)}"
        )

    if data.get("status") != "PARTIAL":
        raise SystemExit("provenance contract must remain PARTIAL until exact bindings are authored")

    e186 = by_consumer["E186"]
    if not (
        e186.get("producer_event") == "E131"
        and e186.get("candidate_key") == "all_voices_heard"
        and e186.get("binding_status") == "PARTIAL_SOURCE_EVIDENCE"
    ):
        raise SystemExit("E186 provenance must remain the conservative E131/all_voices_heard partial finding")

    for consumer in ("E247", "E248"):
        record = by_consumer[consumer]
        if record.get("binding_status") != "OPEN":
            raise SystemExit(f"{consumer} must remain OPEN until an authored producer/key tuple exists")
        if record.get("producer_event") is not None or record.get("candidate_key") is not None:
            raise SystemExit(f"{consumer} must not contain an invented producer/key")

    if FORBIDDEN_CONSUMERS.intersection(by_consumer):
        raise SystemExit("ordinary authored nodes were incorrectly included as replay producer consumers")

    if data.get("runtime_verified") is not False:
        raise SystemExit("runtime_verified must remain false for source-only provenance")

    print("replay producer provenance contract: PASS (conservative partial/open boundary)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
