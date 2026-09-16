#!/usr/bin/env python3
"""Validate the frozen delayed-consequence source/lifecycle contract.

This is a source/contract gate, not the production Decision Engine.
"""
from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
DELAY = ROOT / "docs" / "MACHINE_DELAY_CONTRACT_01.json"
OUT = ROOT / "docs" / "MACHINE_DELAYED_LIFECYCLE_GATE_01.json"
EXPECTED = {
    "E181": ("E45-B"), "E182": ("E117-B"), "E183": ("E118-B"),
    "E184": ("E25-B"), "E185": ("E17-A"), "E242": ("E118-B"),
    "E243": ("E18-B"), "E244": ("E09-B"), "E245": ("E20-A"),
    "E246": ("E160-A"),
}
EXPECTED_DELAY_KEYS = {
    "E181": "delay.E45B.E181.second_toll_increase",
    "E182": "delay.E117B.E182.veteran_promise",
    "E183": "delay.E118B.E183.noble_exception_return",
    "E184": "delay.E25B.E184.quiet_evidence",
    "E185": "delay.E17A.E185.cheap_steel_failure",
    "E242": "delay.E118B.E242.renewed_exception",
    "E243": "delay.E18B.E243.old_bridge",
    "E244": "delay.E09B.E244.audit_comes_due",
    "E245": "delay.E20A.E245.soldiers_son_returns",
    "E246": "delay.E160A.E246.price_ceiling_memory",
}
def main() -> int:
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    delay = json.loads(DELAY.read_text(encoding="utf-8"))
    rows = {r.get("consumer"): r for r in graph.get("delayed_consumers", [])}
    delay_rows = {r.get("resolutionTarget"): r for r in delay.get("delays", [])}
    errors=[]; warnings=[]; checked={}
    if set(delay_rows) != set(EXPECTED_DELAY_KEYS):
        errors.append(f"machine delay scope drift: expected {sorted(EXPECTED_DELAY_KEYS)}, got {sorted(delay_rows)}")
    keys = [r.get("exactlyOnceKey") for r in delay.get("delays", [])]
    if len(keys) != len(set(keys)):
        errors.append("duplicate exactlyOnceKey in machine delay contract")
    for consumer,required in EXPECTED.items():
        row=rows.get(consumer); drow=delay_rows.get(consumer)
        if row is None: errors.append(f"missing delayed consumer: {consumer}"); continue
        if drow is None: errors.append(f"missing machine delay contract row: {consumer}"); continue
        status=row.get("status"); candidates=row.get("candidates",[])
        expected_key=EXPECTED_DELAY_KEYS[consumer]
        checked[consumer]={"status":status,"required_candidate":required,"candidate_present":required in candidates,"exactly_once_key":drow.get("exactlyOnceKey")}
        if status != "CLOSED": errors.append(f"{consumer}: delayed source status is not CLOSED: {status!r}")
        if required not in candidates: errors.append(f"{consumer}: required source candidate {required!r} is absent")
        if drow.get("exactlyOnceKey") != expected_key: errors.append(f"{consumer}: unexpected exactlyOnceKey {drow.get('exactlyOnceKey')!r}")
        if drow.get("saveLoadPolicy") != "persistent": errors.append(f"{consumer}: saveLoadPolicy is not persistent")
        if drow.get("replayPolicy") != "run_scoped_pending_delay": errors.append(f"{consumer}: replayPolicy drift")
        earliest = drow.get("earliestTurn")
        if consumer == "E185":
            if earliest is not None: errors.append("E185 must remain condition-bound with earliestTurn=null")
            if "military crisis" not in str(drow.get("cancellationRule", "")).lower():
                errors.append("E185 condition-bound military-crisis rule is missing")
        elif not isinstance(earliest, dict) or not isinstance(earliest.get("relativeToSource"), int) or earliest["relativeToSource"] < 1:
            errors.append(f"{consumer}: invalid relative earliestTurn")
    for row in graph.get("delayed_consumers",[]):
        text=json.dumps(row,ensure_ascii=False).lower()
        if "absolute due" in text or "invented turn" in text: errors.append(f"prohibited invented timing language: {row.get('consumer')}")
    report={"schema_version":"1.5","contract":"choice_kingdom.delayed_lifecycle_gate","scope":"E01-E272","readiness":"BLOCKED" if errors else "CLOSED","gameplay_verified":False,"checked":checked,"errors":errors,"warnings":warnings,"rules":["source identity and lifecycle closure are separate","relative authored delays are preserved; absolute due turns are not invented","condition-bound E185 uses earliestTurn=null with an explicit later military-crisis condition","all ten high-risk delayed consumers have unique machine identities","persistent save/load and run-scoped replay policies are explicit","E184 source identity is closed at E25-B","E242 source identity is closed at E118-B","E185 cheap_weapons identity is distinct from the later military-crisis condition"]}
    OUT.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"readiness":report["readiness"],"errors":len(errors),"warnings":len(warnings)},sort_keys=True))
    return 1 if errors else 0
if __name__ == "__main__": raise SystemExit(main())
