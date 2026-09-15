from __future__ import annotations
import json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CONTRACT=ROOT/"docs/MACHINE_DELAY_CONTRACT_01.json"
GRAPH=ROOT/"docs/MACHINE_CANONICAL_GRAPH_01.json"
errors=[]
contract=json.loads(CONTRACT.read_text(encoding="utf-8")); graph=json.loads(GRAPH.read_text(encoding="utf-8"))
expected_scope={f"E{i:02d}" for i in range(1,273)}; excluded=set(graph["scope"].get("excluded_events",[]))
if (graph["scope"]["first_event"],graph["scope"]["last_event"])!=(1,272): errors.append("machine graph scope is not E01-E272")
if excluded!={"E273","E274","E275","E276","E277"}: errors.append("excluded scope is not exactly E273-E277")
expected_delays={("E25","B","E184"):4,("E118","B","E242"):6,("E45","B","E181"):5,("E117","B","E182"):4,("E118","B","E183"):5,("E17","A","E185"):None,("E18","B","E243"):5,("E09","B","E244"):5,("E20","A","E245"):6,("E160","A","E246"):5}
actual_delays={}; keys=set()
for row in contract.get("delays",[]):
    source=row.get("sourceEventId",""); target=row.get("resolutionTarget",""); key=row.get("exactlyOnceKey",""); choice=row.get("sourceChoiceId",""); identity=(source,choice,target); earliest=row.get("earliestTurn",{}).get("relativeToSource"); actual_delays[identity]=earliest
    if source not in expected_scope or target not in expected_scope: errors.append(f"out-of-scope delay: {source} -> {target}")
    if source in excluded or target in excluded: errors.append(f"excluded event used by delay: {source} -> {target}")
    if key in keys or not key: errors.append(f"duplicate/missing exactlyOnceKey: {key}")
    keys.add(key); expected=expected_delays.get(identity,"MISSING")
    if expected=="MISSING": errors.append(f"unexpected delay identity: {source}-{choice} -> {target}")
    elif earliest!=expected: errors.append(f"wrong earliestTurn for {source}-{choice} -> {target}: expected {expected!r}, got {earliest!r}")
    if expected is None:
        if "later military crisis" not in str(row.get("cancellationRule","")): errors.append("E17-A -> E185 must retain the authored later-military-crisis condition")
    elif not isinstance(earliest,int) or earliest<1: errors.append(f"invalid relative earliestTurn for {source}-{choice}")
    if not str(row.get("cancellationRule","")): errors.append(f"missing cancellationRule: {source}-{choice}")
    if row.get("saveLoadPolicy")!="persistent": errors.append(f"delay is not save/load persistent: {source}-{choice}")
    if row.get("replayPolicy")!="run_scoped_pending_delay": errors.append(f"delay replay policy is not run-scoped: {source}-{choice}")
    if not re.fullmatch(r"E\d{2,3}",target): errors.append(f"invalid resolution target: {target}")
if set(actual_delays)!=set(expected_delays): errors.append(f"canonical delayed consequence identity set mismatch; missing={sorted(set(expected_delays)-set(actual_delays))}")
delayed={row["consumer"]:row for row in graph.get("delayed_consumers",[])}
expected_sources={"E181":("E45","B"),"E182":("E117","B"),"E183":("E118","B"),"E184":("E25","B"),"E185":("E17","A"),"E242":("E118","B"),"E243":("E18","B"),"E244":("E09","B"),"E245":("E20","A"),"E246":("E160","A")}
for consumer,(source,choice) in expected_sources.items():
    row=delayed.get(consumer)
    if not row or f"{source}-{choice}" not in row.get("candidates",[]): errors.append(f"canonical graph missing {source}-{choice} candidate for {consumer}")
    if consumer in {"E184","E242"} and row and row.get("status")!="CLOSED": errors.append(f"canonical graph delay status not CLOSED for {consumer}")
if errors:
    print("MACHINE_DELAY_CONTRACT: FAIL"); [print(f"- {e}") for e in errors]; raise SystemExit(1)
print("MACHINE_DELAY_CONTRACT: PASS"); print(f"delays={len(contract.get('delays',[]))}"); print("identity_set=E181-E185,E242-E246"); print("scope=E01-E272"); print("excluded=E273-E277"); print("save_load_policy=persistent"); print("replay_policy=run_scoped_pending_delay"); print("runtime_cancellation=OPEN")
