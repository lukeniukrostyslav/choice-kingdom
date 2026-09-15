from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs/MACHINE_CANONICAL_GRAPH_01.json"
EXPECTED = {f"E{i:02d}" for i in range(1, 273)}
HEADING = re.compile(r"^### (E\d{2,3}) — .+$", re.M)
CHOICE = re.compile(r"^(?:\*\*|-\s*)([AB])\s*[—:]\s*(.+?)(?:\*\*)?$", re.M)

# A choice must carry authored state/effect semantics, not merely a prose label.
EFFECT_PATTERNS = [
    re.compile(r"[+-]\d+(?:\.\d+)?\s+[A-Za-zА-Яа-я_]+"),
    re.compile(r"`[^`]+`"),
    re.compile(r"\b(?:clear|clears|reset|resets|resolve|resolves|cancel|cancels|invalidate|invalidates|revoke|revokes|prevent|prevents|schedule|schedules|unlock|unlocks|delayed|immediate|establish|establishes|produces|sets|marks)\b", re.I),
]
STATE_HINT = re.compile(r"(?:\b(?:state|flag|predicate|history|thread|meta|ending|cycle|condition|route|evidence|trigger|effect)\b|`[^`]+`)", re.I)


def fail(msg: str) -> None:
    print("CHOICE_TRANSITION_SEMANTICS: FAIL")
    print(f"- {msg}")
    raise SystemExit(1)


graph = json.loads(GRAPH.read_text(encoding="utf-8"))
scope = graph["scope"]
expected = {f"E{i:02d}" for i in range(int(scope["first_event"]), int(scope["last_event"]) + 1)} - set(scope.get("excluded_events", []))
if expected != EXPECTED:
    fail("production scope is not exactly E01-E272")

blocks: dict[str, str] = {}
for source in graph["source_of_truth"]["catalog_sources"]:
    path = ROOT / source
    if not path.exists():
        fail(f"missing catalog source: {source}")
    text = path.read_text(encoding="utf-8")
    matches = list(HEADING.finditer(text))
    for i, match in enumerate(matches):
        event_id = match.group(1)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        if event_id in blocks:
            fail(f"duplicate canonical event block: {event_id}")
        blocks[event_id] = text[match.start():end]

missing = sorted(EXPECTED - set(blocks), key=lambda x: int(x[1:]))
if missing:
    fail("missing authored event blocks: " + ", ".join(missing))

gaps: list[str] = []
rows = 0
for event_id in sorted(EXPECTED, key=lambda x: int(x[1:])):
    matches = list(CHOICE.finditer(blocks[event_id]))
    labels = {m.group(1) for m in matches}
    if labels != {"A", "B"}:
        gaps.append(f"{event_id}: expected exactly A+B choices, found {sorted(labels)}")
        continue
    for match in matches:
        rows += 1
        body = match.group(2).strip()
        if not any(p.search(body) for p in EFFECT_PATTERNS):
            gaps.append(f"{event_id}-{match.group(1)}: no explicit authored effect/state token")
        elif not STATE_HINT.search(body):
            gaps.append(f"{event_id}-{match.group(1)}: effect lacks state/evidence marker")

if gaps:
    print("CHOICE_TRANSITION_SEMANTICS: FAIL")
    print(f"events={len(blocks)}")
    print(f"choice_rows={rows}")
    print(f"semantic_gaps={len(gaps)}")
    for gap in gaps[:100]:
        print(f"- {gap}")
    if len(gaps) > 100:
        print(f"- ... {len(gaps)-100} more")
    raise SystemExit(1)

print("CHOICE_TRANSITION_SEMANTICS: PASS")
print(f"events={len(blocks)}")
print(f"choice_rows={rows}")
print("semantic_gaps=0")
