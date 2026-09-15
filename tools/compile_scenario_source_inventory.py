#!/usr/bin/env python3
"""Compile conservative E01-E272 producer/consumer inventory with frozen source contracts."""
from __future__ import annotations
from collections import defaultdict
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"docs/MACHINE_CANONICAL_GRAPH_01.json"
if not MANIFEST.exists():
    print("SOURCE_INVENTORY: FAIL\n- missing canonical graph manifest"); sys.exit(1)
manifest=json.loads(MANIFEST.read_text(encoding="utf-8"))
sources=manifest.get("source_of_truth",{}).get("catalog_sources",[])
excluded=set(manifest.get("scope",{}).get("excluded_events",[])); first=int(manifest.get("scope",{}).get("first_event",1)); last=int(manifest.get("scope",{}).get("last_event",272))
expected={f"E{i:02d}" for i in range(first,last+1)}-excluded
heading_re=re.compile(r"^### (E\d{2,3}) — (.+)$",re.M); trigger_re=re.compile(r"^\*\*Trigger:\*\* (.*)$",re.M); backtick_re=re.compile(r"`([^`]+)`"); choice_re=re.compile(r"^- \*\*[AB]\b.*$",re.M)
clear_re=re.compile(r"(?:^|\s)(?:clear|clears|cleared|reset|resets|remove|removes|removed|erase|erases|erased|invalidate|invalidates|invalidated|revoke|revokes|revoked|cancel|cancels|cancelled|canceled)\s+(?:the\s+)?$",re.I)
errors=[]; events={}; producers=defaultdict(list); consumers=defaultdict(list); predicate_edges=defaultdict(set)
ALIASES=manifest.get("canonical_trigger_normalizations",{})
for source in sources:
    path=ROOT/source
    if not path.exists(): errors.append(f"missing catalog: {source}"); continue
    text=path.read_text(encoding="utf-8"); matches=list(heading_re.finditer(text))
    for i,m in enumerate(matches):
        event_id,title=m.group(1),m.group(2).strip()
        if event_id in events: errors.append(f"duplicate authored event heading: {event_id}"); continue
        block=text[m.start():matches[i+1].start() if i+1<len(matches) else len(text)]
        tm=trigger_re.search(block); trigger=tm.group(1).strip() if tm else ""
        raw=sorted(set(backtick_re.findall(trigger))); tokens=sorted({ALIASES.get(t,t) for t in raw})
        choices=[]
        for choice in choice_re.findall(block):
            outs=[]; clears=[]
            for x in backtick_re.finditer(choice):
                token=x.group(1); prefix=choice[:x.start()]
                (clears if clear_re.search(prefix) else outs).append(token)
            outs=sorted(set(outs)); clears=sorted(set(clears)); choices.append({"text":choice,"outputs":outs,"clears":clears})
            for token in outs: producers[token].append({"event":event_id,"source":source,"choice":choice[:120],"kind":"authored"})
        for token in tokens: consumers[token].append({"event":event_id,"source":source,"trigger":trigger})
        for p in [t for t in tokens if t.startswith("pred.")]:
            for q in sorted({t for c in choices for t in c["outputs"] if t.startswith("pred.")}): predicate_edges[p].add(q)
        events[event_id]={"event_id":event_id,"title":title,"source":source,"trigger":trigger,"trigger_tokens":tokens,"choices":choices}

# The machine graph freezes source-backed producers that are explicit in authored
# prose but represented as contract rows rather than ordinary choice-line tokens.
contracts=list(manifest.get("source_closed_producers",[]))+list(manifest.get("derived_source_contracts",[]))
for c in contracts:
    fact=c["fact"]; producers[fact].append({"event":c.get("event","DERIVED"),"source":c.get("source","docs/MACHINE_CANONICAL_GRAPH_01.json"),"choice":c.get("choice","source contract"),"kind":"source_contract"})
missing=sorted(expected-set(events),key=lambda x:int(x[1:])); extra=sorted(set(events)-expected,key=lambda x:int(x[1:]))
if missing: errors.append("missing expected events: "+", ".join(missing))
if extra: errors.append("events outside frozen scope: "+", ".join(extra))
duplicates={t:w for t,w in sorted(producers.items()) if len(w)>1}
same_event_shared={}
for eid,event in events.items():
    by=defaultdict(set)
    for c in event["choices"]:
        mm=re.match(r"^- \*\*([AB])\b",c["text"])
        if mm:
            for t in c["outputs"]: by[t].add(mm.group(1))
    for t,labels in by.items():
        if {"A","B"}.issubset(labels): same_event_shared.setdefault(t,[]).append({"event":eid,"choices":sorted(labels)})
IDEMPOTENT={("history.guild_logistics_cooperation","E194"),("ledger_fragment_a","E21")}
semantic={t:w for t,w in duplicates.items() if len({x["event"] for x in w})>1 and not any((t,x["event"]) in IDEMPOTENT for x in w)}
reaffirmed={t:[x for x in w if (t,x["event"]) in IDEMPOTENT] for t,w in duplicates.items() if any((t,x["event"]) in IDEMPOTENT for x in w)}
undefined=sorted({t for t in consumers if t not in producers}); nodes=sorted(set(predicate_edges)|{t for t in producers if t.startswith("pred.")}|{t for t in consumers if t.startswith("pred.")}); graph={n:sorted(predicate_edges.get(n,set())) for n in nodes}
cycles=[]; state={}; stack=[]
def visit(n):
    state[n]=1; stack.append(n)
    for q in graph.get(n,[]):
        if state.get(q,0)==0: visit(q)
        elif state.get(q)==1 and q in stack:
            cyc=stack[stack.index(q):]+[q]
            if cyc not in cycles: cycles.append(cyc)
    stack.pop(); state[n]=2
for n in nodes:
    if state.get(n,0)==0: visit(n)
undefined_pred=sorted({t for t in consumers if t.startswith("pred.") and t not in producers})
if cycles: errors.append("predicate dependency cycle(s): "+"; ".join(" -> ".join(c) for c in cycles))
inventory={"schema":"choice-kingdom-scenario-source-inventory-3","scope":{"first_event":first,"last_event":last,"excluded_events":sorted(excluded)},"event_count":len(events),"events":[events[k] for k in sorted(events,key=lambda x:int(x[1:]))],"producers":dict(sorted(producers.items())),"consumers":dict(sorted(consumers.items())),"duplicate_output_tokens":duplicates,"semantic_writer_collisions":semantic,"same_event_shared_writers":same_event_shared,"reaffirmed_tokens":reaffirmed,"undefined_consumers":undefined,"predicate_dependency_graph":graph,"undefined_predicate_consumers":undefined_pred,"predicate_cycles":cycles,"canonical_trigger_aliases":ALIASES,"source_contract_count":len(contracts),"notes":["Source-level inventory only; no gameplay/fresh-run reachability claim.","Canonical trigger aliases are source-language normalization, not invented runtime facts.","Source-closed and derived contracts are admitted only when frozen in MACHINE_CANONICAL_GRAPH_01.json.","E194 history.guild_logistics_cooperation and E21 ledger_fragment_a are frozen idempotent reaffirmations."]}
print("SOURCE_INVENTORY: FAIL" if errors else "SOURCE_INVENTORY: PASS")
for e in errors: print("- "+e)
for k,v in [("events",len(events)),("expected",len(expected)),("unique_output_tokens",len(producers)),("trigger_tokens",len(consumers)),("duplicate_output_tokens",len(duplicates)),("semantic_writer_collisions",len(semantic)),("same_event_shared_writers",len(same_event_shared)),("reaffirmed_tokens",len(reaffirmed)),("source_contracts",len(contracts)),("undefined_consumers",len(undefined)),("predicate_nodes",len(nodes)),("predicate_edges",sum(len(x) for x in graph.values())),("undefined_predicate_consumers",len(undefined_pred)),("predicate_cycles",len(cycles))]: print(f"{k}={v}")
if undefined: print("undefined_consumer_names="+",".join(undefined))
if undefined_pred: print("undefined_predicate_consumer_names="+",".join(undefined_pred))
if errors: sys.exit(1)
out=ROOT/"scenario-source-inventory.json"; out.write_text(json.dumps(inventory,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"); print("inventory_file="+out.name)
