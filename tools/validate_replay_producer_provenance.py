#!/usr/bin/env python3
"""Validate the replay producer boundary against the canonical replay contract."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CONTRACT=ROOT/"docs"/"MACHINE_REPLAY_PRODUCER_PROVENANCE_01.json"
REPLAY=ROOT/"docs"/"MACHINE_REPLAY_CONTRACT_01.json"
REQUIRED={"E186","E247","E248"}; FORBIDDEN={"E249","E250","E270"}
def main()->int:
    data=json.loads(CONTRACT.read_text(encoding="utf-8")); replay=json.loads(REPLAY.read_text(encoding="utf-8")); records=data.get("records",[]); by={r.get("consumer"):r for r in records}
    if set(by)!=REQUIRED: raise SystemExit(f"replay provenance scope mismatch: expected {sorted(REQUIRED)}, got {sorted(by)}")
    if data.get("status")!="SOURCE_BOUNDARY_CLOSED": raise SystemExit("provenance boundary must be SOURCE_BOUNDARY_CLOSED")
    replay_by={r.get("event_id"):r for r in replay.get("contracts",[])}
    for consumer in REQUIRED:
        r=by[consumer]; rr=replay_by.get(consumer)
        if rr is None: raise SystemExit(f"missing canonical replay contract for {consumer}")
        if r.get("producer_event") is not None or r.get("producer_choice") is not None: raise SystemExit(f"{consumer}: authored producer must remain null")
        key=rr.get("canonical_meta_key")
        if r.get("candidate_key")!=key: raise SystemExit(f"{consumer}: provenance key does not match replay contract")
        if r.get("binding_status")!="CLOSED_AT_REPLAY_BOUNDARY": raise SystemExit(f"{consumer}: replay boundary not closed")
        if rr.get("producer_scope")!="completed_prior_run_meta_export": raise SystemExit(f"{consumer}: invalid producer boundary")
        if rr.get("exactly_once_import") is not True: raise SystemExit(f"{consumer}: exactly-once import contract missing")
    if FORBIDDEN.intersection(by): raise SystemExit("ordinary authored nodes were incorrectly included")
    if data.get("runtime_verified") is not False: raise SystemExit("runtime_verified must remain false")
    print("replay producer provenance contract: PASS (source replay boundary closed; runtime remains open)")
    return 0
if __name__=="__main__": raise SystemExit(main())
