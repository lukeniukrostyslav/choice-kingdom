#!/usr/bin/env python3
"""Validate S01 source-level scenario closure for frozen E01-E272.

S01 is closed only at the authored/source-contract layer. Runtime Decision
Engine execution, conditional gameplay reachability, replay execution and
Android readiness remain downstream gates.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"docs/MACHINE_CANONICAL_GRAPH_01.json"
INVENTORY=ROOT/"scenario-source-inventory.json"
CAUSAL=ROOT/"docs/MACHINE_CAUSAL_REACHABILITY_01.json"
OUT=ROOT/"docs/MACHINE_S01_SCENARIO_CLOSURE_01.json"
HEADING=re.compile(r"^###\s+(E(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9]))\b")

def num(e:str)->int: return int(e[1:])

def main()->int:
    manifest=json.loads(MANIFEST.read_text(encoding="utf-8"))
    first,last=int(manifest["scope"]["first_event"]),int(manifest["scope"]["last_event"])
    expected={f"E{i:02d}" for i in range(first,last+1)}
    excluded=set(manifest["scope"]["excluded_events"])
    errors:list[str]=[]

    catalog_ids:set[str]=set(); counts:dict[str,int]={}
    for source in manifest["source_of_truth"]["catalog_sources"]:
        path=ROOT/source
        if not path.exists(): errors.append(f"missing authoritative catalog source: {source}"); continue
        for line in path.read_text(encoding="utf-8").splitlines():
            m=HEADING.match(line.strip())
            if m:
                e=m.group(1); catalog_ids.add(e); counts[e]=counts.get(e,0)+1
    missing=sorted(expected-catalog_ids,key=num)
    extra=sorted(catalog_ids-expected-excluded,key=num)
    leaked=sorted(catalog_ids&excluded,key=num)
    allowed=set(manifest.get("allowed_catalog_duplicate_event_ids",[]))
    duplicates=sorted(e for e,c in counts.items() if c>1 and e in expected and e not in allowed)
    if missing: errors.append("missing frozen catalog events: "+", ".join(missing))
    if extra: errors.append("out-of-scope catalog events: "+", ".join(extra))
    if leaked: errors.append("excluded expansion events leaked into catalog: "+", ".join(leaked))
    if duplicates: errors.append("unexpected duplicate catalog headings: "+", ".join(duplicates))

    inventory_status="MISSING"; inventory_events=None
    if INVENTORY.exists():
        try:
            data=json.loads(INVENTORY.read_text(encoding="utf-8")); inventory_events=data.get("event_count")
            inventory_status="PASS" if inventory_events==len(expected) else "FAIL"
            if inventory_status=="FAIL": errors.append(f"source inventory event_count expected {len(expected)}, got {inventory_events}")
        except (OSError,json.JSONDecodeError) as exc:
            inventory_status="FAIL"; errors.append(f"cannot parse scenario-source-inventory.json: {exc}")
    else: errors.append("scenario-source-inventory.json is missing")

    causal_status="MISSING"; causal_unreachable=None
    if CAUSAL.exists():
        try:
            causal=json.loads(CAUSAL.read_text(encoding="utf-8"))
            causal_status="PASS" if causal.get("source_level_causal_reachability_closed") is True else "FAIL"
            causal_unreachable=causal.get("causal_nodes_unreachable_from_structural_root")
            if causal_status=="FAIL": errors.append("canonical causal reachability report is not closed")
            if causal.get("scope")!="E01-E272": errors.append("causal reachability report scope drift")
        except (OSError,json.JSONDecodeError) as exc:
            causal_status="FAIL"; errors.append(f"cannot parse causal reachability report: {exc}")
    else: errors.append("MACHINE_CAUSAL_REACHABILITY_01.json is missing")

    result={
        "schema_version":"1.2",
        "contract":"choice_kingdom.s01_scenario_source_closure",
        "scope":"E01-E272",
        "excluded_events":sorted(excluded,key=num),
        "catalog_event_count":len(catalog_ids&expected),
        "expected_event_count":len(expected),
        "catalog_missing_count":len(missing),
        "catalog_extra_count":len(extra),
        "unexpected_duplicate_count":len(duplicates),
        "inventory_status":inventory_status,
        "inventory_event_count":inventory_events,
        "causal_reachability_status":causal_status,
        "causal_unreachable_count":causal_unreachable,
        "source_level_s01_closed":not errors,
        "source_level_percentage":100 if not errors else 0,
        "runtime_gameplay_reachability_proven":False,
        "decision_engine_execution_proven":False,
        "fresh_run_reachability_proven":False,
        "replay_reachability_proven":False,
        "android_runtime_proven":False,
        "errors":errors,
        "boundary":"S01 source closure is not runtime/gameplay completion; runtime gates remain downstream of the Decision Engine."
    }
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"source_level_s01_closed":result["source_level_s01_closed"],"catalog_event_count":result["catalog_event_count"],"inventory_status":inventory_status,"causal_reachability_status":causal_status,"errors":len(errors)},indent=2))
    return 1 if errors else 0

if __name__=="__main__": raise SystemExit(main())
