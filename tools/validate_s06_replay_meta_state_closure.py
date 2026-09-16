from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs/MACHINE_REPLAY_CONTRACT_01.json"
GRAPH = ROOT / "docs/MACHINE_CANONICAL_GRAPH_01.json"

EXPECTED = {"E186", "E247", "E248"}
EXCLUDED = {"E273", "E274", "E275", "E276", "E277"}


def fail(message: str) -> None:
    print("S06_REPLAY_META_STATE_CLOSURE: FAIL")
    print(f"- {message}")
    raise SystemExit(1)


def load(path: Path) -> dict:
    if not path.exists():
        fail(f"missing {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def event_blocks() -> dict[str, str]:
    graph = load(GRAPH)
    sources = graph.get("source_of_truth", {}).get("catalog_sources", [])
    heading = re.compile(r"^### (E\d{2,3}) — .+$", re.M)
    result: dict[str, str] = {}
    for source in sources:
        path = ROOT / source
        if not path.exists():
            fail(f"missing catalog source: {source}")
        text = path.read_text(encoding="utf-8")
        matches = list(heading.finditer(text))
        for i, match in enumerate(matches):
            event_id = match.group(1)
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            if event_id in result:
                fail(f"duplicate authored event heading: {event_id}")
            result[event_id] = text[match.start():end]
    return result


contract = load(CONTRACT)
if contract.get("schema") != "choice-kingdom-machine-replay-contract-1":
    fail("unexpected replay contract schema")

scope = contract.get("scope", {})
if scope.get("production_first_event") != "E01" or scope.get("production_last_event") != "E272":
    fail("production scope must be E01-E272")
if set(scope.get("excluded_events", [])) != EXCLUDED:
    fail("excluded scope must be exactly E273-E277")

entries = contract.get("contracts", [])
if {e.get("event_id") for e in entries} != EXPECTED:
    fail("replay contract must cover exactly E186, E247 and E248")

blocks = event_blocks()
errors: list[str] = []
seen_keys: set[str] = set()
for entry in entries:
    event_id = entry.get("event_id")
    block = blocks.get(event_id, "")
    if not block:
        errors.append(f"missing authored event: {event_id}")
        continue
    trigger = re.search(r"^\*\*Trigger:\*\* (.+)$", block, re.M)
    actual_trigger = trigger.group(1).strip() if trigger else ""
    if actual_trigger != entry.get("source_trigger"):
        errors.append(f"{event_id}: source trigger drift")
    key = entry.get("canonical_meta_key", "")
    if not key.startswith("meta.replay."):
        errors.append(f"{event_id}: canonical meta key is not replay scoped")
    if key in seen_keys:
        errors.append(f"duplicate canonical meta key: {key}")
    seen_keys.add(key)
    if entry.get("producer_scope") != "completed_prior_run_meta_export":
        errors.append(f"{event_id}: invalid producer scope")
    if entry.get("exactly_once_import") is not True:
        errors.append(f"{event_id}: exactly_once_import must be true")
    if not entry.get("reset"):
        errors.append(f"{event_id}: reset boundary missing")

rules = contract.get("rules", [])
required_rules = [
    "Replay metadata is a producer boundary, not an authored event producer.",
    "A new run may import only the explicitly listed meta keys from the immediately completed prior run.",
    "Run-specific flags, active predicates, pending delayed events and terminal state never cross the reset boundary.",
    "E186 retains its same-run warehouse_arson route; replay metadata is an additional explicitly bound route.",
    "E247 and E248 prose trigger labels are normalized by this machine contract and are not independent runtime predicates.",
]
for rule in required_rules:
    if rule not in rules:
        errors.append(f"missing mandatory replay boundary rule: {rule}")

if errors:
    print("S06_REPLAY_META_STATE_CLOSURE: FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("S06_REPLAY_META_STATE_CLOSURE: PASS")
print("production_scope=E01-E272")
print("excluded=E273-E277")
print("replay_meta_events=3")
print("canonical_meta_keys=3")
print("exactly_once_imports=3")
print("fresh_run_without_prior_completion=zero_replay_keys")
print("terminal_state_cross_run=forbidden")
print("pending_delayed_state_cross_run=forbidden")
print("runtime_replay_execution=downstream_not_claimed")
