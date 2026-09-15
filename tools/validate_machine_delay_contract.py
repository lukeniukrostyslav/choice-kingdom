from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs/MACHINE_DELAY_CONTRACT_01.json"
GRAPH = ROOT / "docs/MACHINE_CANONICAL_GRAPH_01.json"

errors: list[str] = []
contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
graph = json.loads(GRAPH.read_text(encoding="utf-8"))
expected_scope = {f"E{i:02d}" for i in range(1, 273)}
excluded = set(graph["scope"].get("excluded_events", []))

if (graph["scope"]["first_event"], graph["scope"]["last_event"]) != (1, 272):
    errors.append("machine graph scope is not E01-E272")
if excluded != {"E273", "E274", "E275", "E276", "E277"}:
    errors.append("excluded scope is not exactly E273-E277")

keys: set[str] = set()
for row in contract.get("delays", []):
    source = row.get("sourceEventId", "")
    target = row.get("resolutionTarget", "")
    key = row.get("exactlyOnceKey", "")
    source_choice = row.get("sourceChoiceId", "")
    earliest = row.get("earliestTurn", {}).get("relativeToSource")
    if source not in expected_scope or target not in expected_scope:
        errors.append(f"out-of-scope delay: {source} -> {target}")
    if source in excluded or target in excluded:
        errors.append(f"excluded event used by delay: {source} -> {target}")
    if key in keys or not key:
        errors.append(f"duplicate/missing exactlyOnceKey: {key}")
    keys.add(key)
    if not isinstance(earliest, int) or earliest < 1:
        errors.append(f"invalid relative earliestTurn for {source}-{source_choice}")
    cancellation = str(row.get("cancellationRule", ""))
    if not cancellation:
        errors.append(f"missing cancellationRule: {source}-{source_choice}")
    if row.get("saveLoadPolicy") != "persistent":
        errors.append(f"delay is not save/load persistent: {source}-{source_choice}")
    if row.get("replayPolicy") != "run_scoped_pending_delay":
        errors.append(f"delay replay policy is not run-scoped: {source}-{source_choice}")
    if not re.fullmatch(r"E\d{2,3}", target):
        errors.append(f"invalid resolution target: {target}")

# Cross-check the source identities frozen in the canonical graph.
delayed = {row["consumer"]: row for row in graph.get("delayed_consumers", [])}
expected_sources = {"E184": ("E25", "B"), "E242": ("E118", "B")}
for consumer, (source, choice) in expected_sources.items():
    row = delayed.get(consumer)
    if not row or f"{source}-{choice}" not in row.get("candidates", []):
        errors.append(f"canonical graph missing {source}-{choice} candidate for {consumer}")
    if row and row.get("status") != "CLOSED":
        errors.append(f"canonical graph delay status not CLOSED for {consumer}")

if errors:
    print("MACHINE_DELAY_CONTRACT: FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("MACHINE_DELAY_CONTRACT: PASS")
print(f"delays={len(contract.get('delays', []))}")
print("scope=E01-E272")
print("excluded=E273-E277")
print("save_load_policy=persistent")
print("replay_policy=run_scoped_pending_delay")
