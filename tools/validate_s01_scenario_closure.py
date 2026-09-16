#!/usr/bin/env python3
"""Validate S01 source-level scenario closure for frozen E01-E272.

S01 is closed here only at the authored/source-contract layer. This gate proves
that the frozen catalog is exhaustive and in-scope, every authored event is
classified by the canonical graph or an explicit coverage declaration, the
structural graph has no unreachable causal nodes, and the canonical inventory
is exhaustive. It deliberately does not claim Decision Engine execution,
conditional gameplay reachability, replay execution, or Android readiness.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/MACHINE_CANONICAL_GRAPH_01.json"
GRAPH = ROOT / "docs/EVENT_GRAPH.md"
INVENTORY = ROOT / "scenario-source-inventory.json"
OUT = ROOT / "docs/MACHINE_S01_SCENARIO_CLOSURE_01.json"
HEADING = re.compile(r"^###\s+(E(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9]))\b")
TOKEN = re.compile(r"\bE(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9])(?:-[A-Z])?\b")
CHAIN = re.compile(r"`([^`]*->[^`]*)`")
COVERAGE = re.compile(r"^-\s+(E(?:[1-9][0-9]{2}|[1-9][0-9]|0[1-9]))\s+—\s+coverage declaration only\s*$")

def num(e: str) -> int: return int(e[1:])
def canon(t: str) -> str: return t.split("-", 1)[0]

def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    first, last = int(manifest["scope"]["first_event"]), int(manifest["scope"]["last_event"])
    expected = {f"E{i:02d}" for i in range(first, last + 1)}
    excluded = set(manifest["scope"]["excluded_events"])
    errors: list[str] = []

    catalog_ids: set[str] = set(); duplicate_counts: dict[str,int] = {}
    for source in manifest["source_of_truth"]["catalog_sources"]:
        path = ROOT / source
        if not path.exists(): errors.append(f"missing authoritative catalog source: {source}"); continue
        for line in path.read_text(encoding="utf-8").splitlines():
            m = HEADING.match(line.strip())
            if m:
                e=m.group(1); catalog_ids.add(e); duplicate_counts[e]=duplicate_counts.get(e,0)+1
    missing=sorted(expected-catalog_ids,key=num); extra=sorted(catalog_ids-expected-excluded,key=num); leaked=sorted(catalog_ids&excluded,key=num)
    allowed=set(manifest.get("allowed_catalog_duplicate_event_ids", []))
    dup=sorted(e for e,c in duplicate_counts.items() if c>1 and e in expected and e not in allowed)
    if missing: errors.append("missing frozen catalog events: "+", ".join(missing))
    if extra: errors.append("out-of-scope catalog events: "+", ".join(extra))
    if leaked: errors.append("excluded expansion events leaked into catalog: "+", ".join(leaked))
    if dup: errors.append("unexpected duplicate catalog headings: "+", ".join(dup))

    text=GRAPH.read_text(encoding="utf-8"); edge_events:set[str]=set(); edges:set[tuple[str,str]]=set()
    for m in CHAIN.finditer(text):
        ids=[canon(t) for t in TOKEN.findall(m.group(1))]
        for e in ids:
            if e in excluded: errors.append(f"excluded event leaked into graph: {e}")
            elif e not in expected: errors.append(f"out-of-scope event leaked into graph: {e}")
            else: edge_events.add(e)
        for a,b in zip(ids,ids[1:]):
            if a in expected and b in expected and a!=b: edges.add((a,b))
    coverage={m.group(1) for m in map(COVERAGE.match,text.splitlines()) if m}
    bad_cov=sorted(coverage-expected,key=num)
    if bad_cov: errors.append("out-of-scope coverage declarations: "+", ".join(bad_cov))
    classified=edge_events|coverage; unclassified=sorted(expected-classified,key=num)
    if unclassified: errors.append("unclassified frozen events: "+", ".join(unclassified))

    inbound={e:set() for e in expected}; outbound={e:set() for e in expected}
    for a,b in edges: outbound[a].add(b); inbound[b].add(a)
    causal=set(edge_events); roots=sorted((e for e in causal if not inbound[e]),key=num)
    reachable=set(roots); stack=list(roots)
    while stack:
        a=stack.pop()
        for b in outbound[a]:
            if b not in reachable: reachable.add(b); stack.append(b)
    unreachable=sorted(causal-reachable,key=num)
    if unreachable: errors.append("structurally unreachable causal nodes: "+", ".join(unreachable))

    inventory_status="MISSING"; inventory_events=None
    if INVENTORY.exists():
        try:
            data=json.loads(INVENTORY.read_text(encoding="utf-8")); inventory_events=data.get("event_count"); inventory_status="PASS" if inventory_events==len(expected) else "FAIL"
            if inventory_status=="FAIL": errors.append(f"scenario source inventory event_count expected {len(expected)}, got {inventory_events}")
        except (OSError,json.JSONDecodeError) as exc: inventory_status="FAIL"; errors.append(f"cannot parse scenario-source-inventory.json: {exc}")
    else: errors.append("scenario-source-inventory.json is missing; compiler must run first")

    result={"schema_version":"1.1","contract":"choice_kingdom.s01_scenario_source_closure","scope":"E01-E272","excluded_events":sorted(excluded,key=num),"catalog_event_count":len(catalog_ids&expected),"expected_event_count":len(expected),"catalog_missing_count":len(missing),"catalog_extra_count":len(extra),"unexpected_duplicate_count":len(dup),"graph_edge_count":len(edges),"graph_causal_event_count":len(causal),"graph_structural_root_count":len(roots),"graph_structurally_reachable_count":len(reachable),"graph_structurally_unreachable_count":len(unreachable),"coverage_declaration_count":len(coverage),"classified_event_count":len(classified&expected),"unclassified_event_count":len(unclassified),"inventory_status":inventory_status,"inventory_event_count":inventory_events,"source_level_s01_closed":not errors,"source_level_percentage":100 if not errors else 0,"runtime_gameplay_reachability_proven":False,"decision_engine_execution_proven":False,"fresh_run_reachability_proven":False,"replay_reachability_proven":False,"android_runtime_proven":False,"errors":errors,"boundary":"S01 source closure is not runtime/gameplay completion; runtime gates remain downstream of the Decision Engine."}
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({k:result[k] for k in ("source_level_s01_closed","catalog_event_count","classified_event_count","graph_structurally_unreachable_count","inventory_status")}|{"errors":len(errors)},indent=2))
    return 1 if errors else 0

if __name__ == "__main__": raise SystemExit(main())
