from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs/MACHINE_CANONICAL_GRAPH_01.json"
EXPECTED = {f"E{i:02d}" for i in range(1, 273)}


def fail(message: str) -> None:
    print("CHOICE_STATE_TRANSITIONS: FAIL")
    print(f"- {message}")
    raise SystemExit(1)


graph = json.loads(GRAPH.read_text(encoding="utf-8"))
expected = {
    f"E{i:02d}"
    for i in range(
        int(graph["scope"]["first_event"]), int(graph["scope"]["last_event"]) + 1
    )
    if f"E{i:02d}" not in set(graph["scope"].get("excluded_events", []))
}
if expected != EXPECTED:
    fail("machine graph production scope is not exactly E01-E272")

heading = re.compile(r"^### (E\d{2,3}) — .+$", re.M)
choice = re.compile(r"^\*\*([AB])\s*[—:]\s*(.+?)\*\*$", re.M)
blocks: dict[str, str] = {}
for source in graph["source_of_truth"]["catalog_sources"]:
    path = ROOT / source
    if not path.exists():
        fail(f"missing catalog source: {source}")
    text = path.read_text(encoding="utf-8")
    matches = list(heading.finditer(text))
    for i, match in enumerate(matches):
        event_id = match.group(1)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[match.start():end]
        if event_id in blocks:
            fail(f"duplicate canonical event block: {event_id}")
        blocks[event_id] = block

missing_events = sorted(expected - set(blocks), key=lambda x: int(x[1:]))
if missing_events:
    fail("missing authored event blocks: " + ", ".join(missing_events))

choice_rows = []
missing_effects = []
for event_id in sorted(expected, key=lambda x: int(x[1:])):
    rows = list(choice.finditer(blocks[event_id]))
    labels = {m.group(1) for m in rows}
    if labels and labels != {"A", "B"}:
        missing = "A" if "A" not in labels else "B"
        missing_effects.append(f"{event_id}: missing authored choice {missing}")
    for index, match in enumerate(rows):
        next_start = rows[index + 1].start() if index + 1 < len(rows) else len(blocks[event_id])
        body = blocks[event_id][match.start():next_start]
        has_delta = bool(re.search(r"[+-]\d+(?:\.\d+)?\s+[A-Za-zА-Яа-я_]+", body))
        has_token = bool(re.search(r"`[^`]+`", body))
        has_lifecycle = bool(re.search(r"\b(clear|clears|reset|resets|resolve|resolves|cancel|cancels|invalidate|invalidates|revoke|revokes|prevent|prevents|schedule|schedules|unlock|unlocks|delayed|immediate)\b", body, re.I))
        evidence = has_delta or has_token or has_lifecycle
        choice_rows.append((event_id, match.group(1), evidence, body))
        if not evidence:
            missing_effects.append(f"{event_id}-{match.group(1)}: no explicit state/effect evidence ({match.group(2).strip()})")

if missing_effects:
    print("CHOICE_STATE_TRANSITIONS: FAIL")
    print(f"events={len(blocks)}")
    print(f"choice_rows={len(choice_rows)}")
    print(f"transition_gaps={len(missing_effects)}")
    for item in missing_effects[:100]:
        print(f"- {item}")
    if len(missing_effects) > 100:
        print(f"- ... {len(missing_effects) - 100} more")
    raise SystemExit(1)

print("CHOICE_STATE_TRANSITIONS: PASS")
print(f"events={len(blocks)}")
print(f"choice_rows={len(choice_rows)}")
print("transition_gaps=0")
