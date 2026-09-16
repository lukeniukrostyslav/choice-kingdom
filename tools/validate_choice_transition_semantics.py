from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs/MACHINE_CANONICAL_GRAPH_01.json"
EXPECTED = {f"E{i:02d}" for i in range(1, 273)}
HEADING = re.compile(r"^### (E\d{2,3}) — .+$", re.M)
CHOICE_HEADING = re.compile(r"^(?:-\s*)?\*\*([AB])\s*[—:]\s*(.*?)\*\*\s*$", re.M)
CHOICE_PLAIN = re.compile(r"^(?:-\s*)?([AB])\s*[—:]\s*(.+?)\s*$", re.M)
TOKEN_RE = re.compile(r"`[^`]+`")
DELTA_RE = re.compile(r"[+-]\d+(?:\.\d+)?\s+[A-Za-zА-Яа-я_]+")
CLAUSE_RE = re.compile(r"^\s*-\s*(?:Immediate|Flag|Unlock|Producer|Delayed|Resolution|Clear|Trigger|Effect|State|History|Meta|Ending|Condition)\s*:", re.I | re.M)
EFFECT_PATTERNS = [
    DELTA_RE,
    TOKEN_RE,
    CLAUSE_RE,
    re.compile(r"\b(?:clear|clears|reset|resets|resolve|resolves|cancel|cancels|invalidate|invalidates|revoke|revokes|prevent|prevents|schedule|schedules|unlock|unlocks|delayed|immediate|establish|establishes|produces|sets|marks)\b", re.I),
]
STATE_HINT = re.compile(r"(?:\b(?:state|flag|predicate|history|thread|meta|ending|cycle|condition|route|evidence|trigger|effect|immediate|delayed|unlock|producer|resolution)\b|`[^`]+`)", re.I)
SPECIAL_EVENT_HINT = re.compile(r"\b(?:Source-level producer|canonical producer|explicitly establishes|explicitly records|derived gate)\b", re.I)


def semantic_signature(body: str) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    deltas = tuple(DELTA_RE.findall(body))
    tokens = tuple(TOKEN_RE.findall(body))
    clauses = tuple(sorted(set(
        m.group(1).lower()
        for m in re.finditer(
            r"^\s*-\s*(Immediate|Flag|Unlock|Producer|Delayed|Resolution|Clear|Trigger|Effect|State|History|Meta|Ending|Condition)\s*:",
            body,
            re.I | re.M,
        )
    )))
    return deltas, tokens, clauses


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
special_rows = 0
for event_id in sorted(EXPECTED, key=lambda x: int(x[1:])):
    block = blocks[event_id]
    matches = list(CHOICE_HEADING.finditer(block))
    if not matches:
        matches = list(CHOICE_PLAIN.finditer(block))
    labels = [m.group(1).upper() for m in matches]

    # Some frozen production events are authored state producers rather than
    # player-choice events (for example E32). They require explicit canonical
    # producer/state prose instead of an invented A/B transition.
    if not matches:
        if SPECIAL_EVENT_HINT.search(block):
            special_rows += 1
            continue
        gaps.append(f"{event_id}: no authored A/B choices and no explicit canonical special-event producer contract")
        continue

    if len(matches) != 2 or set(labels) != {"A", "B"}:
        gaps.append(f"{event_id}: expected exactly one A and one B choice, found {labels}")
        continue

    signatures: dict[str, tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = {}
    for index, match in enumerate(matches):
        rows += 1
        next_start = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        body = block[match.start():next_start].strip()
        label = match.group(1).upper()
        signatures[label] = semantic_signature(body)

        if not any(p.search(body) for p in EFFECT_PATTERNS):
            gaps.append(f"{event_id}-{label}: no explicit authored effect/state payload")
        if not CLAUSE_RE.search(body) and not DELTA_RE.search(body) and not TOKEN_RE.search(body):
            gaps.append(f"{event_id}-{label}: no machine-recognizable transition payload")
        elif not STATE_HINT.search(body):
            gaps.append(f"{event_id}-{label}: effect lacks state/evidence marker")

    if signatures.get("A") == signatures.get("B"):
        gaps.append(f"{event_id}: A/B choices have identical authored effect signatures")

if gaps:
    print("CHOICE_TRANSITION_SEMANTICS: FAIL")
    print(f"events={len(blocks)}")
    print(f"choice_rows={rows}")
    print(f"special_state_events={special_rows}")
    print(f"semantic_gaps={len(gaps)}")
    for gap in gaps[:100]:
        print(f"- {gap}")
    if len(gaps) > 100:
        print(f"- ... {len(gaps)-100} more")
    raise SystemExit(1)

print("CHOICE_TRANSITION_SEMANTICS: PASS")
print(f"events={len(blocks)}")
print(f"choice_rows={rows}")
print(f"special_state_events={special_rows}")
print("semantic_gaps=0")
print("exactly_one_A_and_one_B=true")
print("explicit_transition_payload=true")
print("alternative_effect_signatures_distinct=true")
