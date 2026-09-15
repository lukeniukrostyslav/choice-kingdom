#!/usr/bin/env python3
"""Validate canonical delayed-consequence identity without inventing runtime timing."""
from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
OUT = ROOT / "docs" / "MACHINE_DELAYED_LIFECYCLE_GATE_01.json"
EXPECTED = {
    "E181": ({"CLOSED"}, "E45-B"), "E182": ({"CLOSED"}, "E117-B"),
    "E183": ({"CLOSED"}, "E118-B"), "E184": ({"CLOSED"}, "E25-B"),
    "E185": ({"PARTIAL", "OPEN"}, "E17-A"), "E242": ({"CLOSED"}, "E118-B"),
    "E243": ({"CLOSED"}, "E18-B"), "E244": ({"CLOSED"}, "E09-B"),
    "E245": ({"CLOSED", "PARTIAL"}, "E20-A"), "E246": ({"CLOSED", "PARTIAL"}, "E160-A"),
}
def main() -> int:
    data = json.loads(GRAPH.read_text(encoding="utf-8"))
    rows = {r.get("consumer"): r for r in data.get("delayed_consumers", [])}
    errors=[]; warnings=[]; checked={}
    for consumer,(statuses,required) in EXPECTED.items():
        row=rows.get(consumer)
        if row is None: errors.append(f"missing delayed consumer: {consumer}"); continue
        status=row.get("status"); candidates=row.get("candidates",[])
        checked[consumer]={"status":status,"required_candidate":required,"candidate_present":required in candidates}
        if status not in statuses: errors.append(f"{consumer}: unexpected status {status!r}")
        if required not in candidates: errors.append(f"{consumer}: required source candidate {required!r} is absent")
        if status in {"OPEN","PARTIAL"}: warnings.append(f"{consumer}: runtime scheduling/cancellation remains open")
    for row in data.get("delayed_consumers",[]):
        text=json.dumps(row,ensure_ascii=False).lower()
        if "absolute due" in text or "invented turn" in text: errors.append(f"prohibited invented timing language: {row.get('consumer')}")
    report={"schema_version":"1.3","contract":"choice_kingdom.delayed_lifecycle_gate","scope":"E01-E272","readiness":"BLOCKED" if errors else ("PARTIAL" if warnings else "CLOSED"),"gameplay_verified":False,"checked":checked,"errors":errors,"warnings":warnings,"rules":["source identity and lifecycle closure are separate","relative authored delays are preserved; absolute due turns are not invented","OPEN/PARTIAL rows cannot be promoted by this validator","E184 source identity is closed at E25-B","E242 source identity is closed at E118-B","E185 cheap_weapons identity is distinct from the later military-crisis condition"]}
    OUT.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"readiness":report["readiness"],"errors":len(errors),"warnings":len(warnings)},sort_keys=True))
    return 1 if errors else 0
if __name__ == "__main__": raise SystemExit(main())
