from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs/MACHINE_REPLAY_CONTRACT_01.json"
GRAPH = ROOT / "docs/MACHINE_CANONICAL_GRAPH_01.json"


def fail(message: str) -> None:
    print("REPLAY_META_CONTRACT: FAIL")
    print(f"- {message}")
    raise SystemExit(1)


def load_json(path: Path) -> dict:
    if not path.exists():
        fail(f"missing {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def load_event_blocks() -> dict[str, tuple[str, str]]:
    graph = load_json(GRAPH)
    sources = graph.get("source_of_truth", {}).get("catalog_sources", [])
    heading = re.compile(r"^### (E\d{2,3}) — .+$", re.M)
    blocks: dict[str, tuple[str, str]] = {}
    for source in sources:
        path = ROOT / source
        if not path.exists():
            fail(f"missing catalog source: {source}")
        text = path.read_text(encoding="utf-8")
        matches = list(heading.finditer(text))
        for i, match in enumerate(matches):
            event_id = match.group(1)
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            block = text[match.start():end]
            trigger_match = re.search(r"^\*\*Trigger:\*\* (.+)$", block, re.M)
            trigger = trigger_match.group(1).strip() if trigger_match else ""
            if event_id in blocks:
                fail(f"duplicate authored event heading: {event_id}")
            blocks[event_id] = (source, trigger)
    return blocks


contract = load_json(CONTRACT)
if contract.get("schema") != "choice-kingdom-machine-replay-contract-1":
    fail("unexpected replay contract schema")

scope = contract.get("scope", {})
if scope.get("production_first_event") != "E01" or scope.get("production_last_event") != "E272":
    fail("replay contract scope must be E01-E272")
if set(scope.get("excluded_events", [])) != {"E273", "E274", "E275", "E276", "E277"}:
    fail("replay contract must exclude exactly E273-E277")

entries = contract.get("contracts", [])
if {e.get("event_id") for e in entries} != {"E186", "E247", "E248"}:
    fail("replay contract must cover exactly E186, E247 and E248")

blocks = load_event_blocks()
errors: list[str] = []
for entry in entries:
    event_id = entry["event_id"]
    if event_id not in blocks:
        errors.append(f"missing authored event: {event_id}")
        continue
    source, trigger = blocks[event_id]
    if trigger != entry["source_trigger"]:
        errors.append(
            f"{event_id} trigger drift: expected {entry['source_trigger']!r}, got {trigger!r} ({source})"
        )
    key = entry.get("canonical_meta_key", "")
    if not key.startswith("meta.replay."):
        errors.append(f"{event_id} canonical_meta_key is not replay-scoped: {key!r}")
    if entry.get("producer_scope") != "completed_prior_run_meta_export":
        errors.append(f"{event_id} must use completed_prior_run_meta_export")
    if entry.get("exactly_once_import") is not True:
        errors.append(f"{event_id} must require exactly-once meta import")
    if not entry.get("reset"):
        errors.append(f"{event_id} missing reset boundary")

if errors:
    print("REPLAY_META_CONTRACT: FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("REPLAY_META_CONTRACT: PASS")
print("events=3")
print("replay_meta_keys=3")
print("exactly_once_imports=3")
print("production_scope=E01-E272")
print("excluded=E273-E277")
