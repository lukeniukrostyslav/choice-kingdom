from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs/MACHINE_CANONICAL_GRAPH_01.json"
EXPECTED = {f"E{i:02d}" for i in range(1, 273)}
HEADING = re.compile(r"^### (E\d{2,3}) — .+$", re.M)
CHOICE_HEADING = re.compile(r"^(?:-\s*)?\*\*([ABC])\s*[—:]\s*(.*?)\*\*", re.M)
CHOICE_PLAIN = re.compile(r"^\s*-\s*([ABC])(?:\s+[A-Za-zА-Яа-я]|\s*[—:])(.+?)\s*$", re.M)
DELTA_RE = re.compile(r"[+-](?:\d+(?:\.\d+)?\s*)?[A-Za-zА-Яа-я_]+")
TOKEN_RE = re.compile(r"`[^`]+`")
CLAUSE_RE = re.compile(r"^\s*-\s*(?:Immediate|Flag|Unlock|Producer|Delayed|Resolution|Clear|Trigger|Effect|State|History|Meta|Ending|Condition)\s*:", re.I | re.M)
LIFECYCLE_RE = re.compile(r"\b(?:clear|clears|reset|resets|resolve|resolves|cancel|cancels|invalidate|invalidates|revoke|revokes|prevent|prevents|schedule|schedules|unlock|unlocks|create|creates|strengthen|strengthens|close|closes|establish|establishes|produce|produces|record|records|later|delayed|immediate|risk|route|evidence|pressure|credibility|stability|reform|contradiction)\b", re.I)
ACTION_RE = re.compile(r"\b(?:open|follow|inspect|subsidize|trace|replace|honor|renegotiate|protect|hear|catalogue|destroy|admit|close|end|publish|leave|accept|refuse|verify|investigate|preserve|compensate|hunt|fund|requisition|restrict|allow|deny|offer|grant|reject|raid|archive|sign|search|defend|punish|write|remove|keep|take|ask|invoke|ratify|endorse|decide|continue|expose|conceal|redact|submit|seal|audit|centralize|support|withdraw)\b", re.I)
STATE_HINT = re.compile(r"(?:\b(?:state|flag|predicate|history|thread|meta|ending|cycle|condition|route|evidence|trigger|effect|immediate|delayed|unlock|producer|resolution)\b|`[^`]+`)", re.I)
SPECIAL_EVENTS = {"E32", *{f"E{i:02d}" for i in range(61, 71)}, "E210", "E270"}
SPECIAL_EVENT_HINT = re.compile(r"\b(?:Source-level producer|canonical producer|explicitly establishes|explicitly records|derived gate|Ending|Purpose|convergence-only|resolution families|convergence producer|convergence decision)\b", re.I)

EXPECTED_EVENT_COUNT = 272
EXPECTED_SPECIAL_EVENT_COUNT = len(SPECIAL_EVENTS)
EXPECTED_NORMAL_EVENT_COUNT = EXPECTED_EVENT_COUNT - EXPECTED_SPECIAL_EVENT_COUNT
# Frozen authored cardinality: 259 normal events have A+B, plus the documented E108-C alternative.
EXPECTED_CHOICE_ROW_COUNT = EXPECTED_NORMAL_EVENT_COUNT * 2 + 1
EXPECTED_ADDITIONAL_CHOICE_EVENTS = {"E108": {"C"}}


def semantic_signature(body: str) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    return (tuple(DELTA_RE.findall(body)), tuple(TOKEN_RE.findall(body)), tuple(sorted(set(m.group(0).lower() for m in LIFECYCLE_RE.finditer(body)))), tuple(sorted(set(m.group(0).lower() for m in ACTION_RE.finditer(body))))


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
extra = sorted(set(blocks) - EXPECTED, key=lambda x: int(x[1:]))
if extra:
    fail("catalog contains out-of-scope event blocks: " + ", ".join(extra))
if len(blocks) != EXPECTED_EVENT_COUNT:
    fail(f"event cardinality drift: expected {EXPECTED_EVENT_COUNT}, found {len(blocks)}")

missing_special = sorted(SPECIAL_EVENTS - set(blocks), key=lambda x: int(x[1:]))
if missing_special:
    fail("special-event classification references missing events: " + ", ".join(missing_special))

gaps: list[str] = []
rows = 0
special_rows = 0
authored_events = 0
normal_events = 0
for event_id in sorted(EXPECTED, key=lambda x: int(x[1:])):
    block = blocks[event_id]
    heading_end = block.find("\n")
    prose = block[heading_end + 1:] if heading_end >= 0 else ""
    prose_lines = [line.strip() for line in prose.splitlines() if line.strip() and not re.match(r"^-\s*[ABC](?:\s|[—:])", line)]
    has_explicit_trigger = bool(re.search(r"^\*\*Trigger:\*\*", block, re.M))
    if not (prose_lines or has_explicit_trigger):
        gaps.append(f"{event_id}: missing authored trigger/narrative content")
    else:
        authored_events += 1

    matches = list(CHOICE_HEADING.finditer(block))
    if not matches:
        matches = list(CHOICE_PLAIN.finditer(block))
    labels = [m.group(1).upper() for m in matches]

    if event_id in SPECIAL_EVENTS:
        if event_id == "E270":
            if labels != ["A"]:
                gaps.append(f"E270: canonical convergence node must contain exactly one authored A decision, found {labels}")
            elif not re.search(r"systemic_explanation_convergence|convergence producer|convergence decision", block, re.I):
                gaps.append("E270: missing explicit convergence producer marker")
            else:
                special_rows += 1
        elif matches:
            gaps.append(f"{event_id}: classified special/convergence node but contains player-choice rows")
        elif not SPECIAL_EVENT_HINT.search(block):
            gaps.append(f"{event_id}: special/convergence classification lacks explicit authored marker")
        else:
            special_rows += 1
        continue

    normal_events += 1
    if not matches:
        gaps.append(f"{event_id}: no authored A/B choices")
        continue
    if "A" not in labels or "B" not in labels or len(labels) < 2 or len(labels) != len(set(labels)):
        gaps.append(f"{event_id}: expected at least one A and one B with unique labels, found {labels}")
        continue
    allowed = {"A", "B"} | EXPECTED_ADDITIONAL_CHOICE_EVENTS.get(event_id, set())
    unexpected = sorted(set(labels) - allowed)
    if unexpected:
        gaps.append(f"{event_id}: unexpected additional choice labels {unexpected}; allowed {sorted(allowed)}")
        continue
    if event_id in EXPECTED_ADDITIONAL_CHOICE_EVENTS and set(labels) != {"A", "B", *EXPECTED_ADDITIONAL_CHOICE_EVENTS[event_id]}:
        gaps.append(f"{event_id}: documented additional-choice contract drift, found {labels}")
        continue
    if event_id not in EXPECTED_ADDITIONAL_CHOICE_EVENTS and set(labels) != {"A", "B"}:
        gaps.append(f"{event_id}: undocumented choice cardinality drift, found {labels}")
        continue

    signatures: dict[str, tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = {}
    for index, match in enumerate(matches):
        rows += 1
        next_start = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        body = block[match.start():next_start].strip()
        label = match.group(1).upper()
        signatures[label] = semantic_signature(body)
        has_effect = bool(DELTA_RE.search(body) or TOKEN_RE.search(body) or CLAUSE_RE.search(body) or LIFECYCLE_RE.search(body) or ACTION_RE.search(body))
        if not has_effect:
            gaps.append(f"{event_id}-{label}: no explicit authored effect/state payload")
        has_state_signal = bool(DELTA_RE.search(body) or TOKEN_RE.search(body) or CLAUSE_RE.search(body) or STATE_HINT.search(body) or LIFECYCLE_RE.search(body) or ACTION_RE.search(body))
        if not has_state_signal:
            gaps.append(f"{event_id}-{label}: no machine-recognizable state/evidence signal")
    if len(set(signatures.values())) != len(signatures):
        gaps.append(f"{event_id}: authored choice alternatives have identical effect signatures")

if normal_events != EXPECTED_NORMAL_EVENT_COUNT:
    gaps.append(f"normal-event cardinality drift: expected {EXPECTED_NORMAL_EVENT_COUNT}, found {normal_events}")
if special_rows != EXPECTED_SPECIAL_EVENT_COUNT:
    gaps.append(f"special-event cardinality drift: expected {EXPECTED_SPECIAL_EVENT_COUNT}, validated {special_rows}")
if rows != EXPECTED_CHOICE_ROW_COUNT:
    gaps.append(f"choice-row cardinality drift: expected {EXPECTED_CHOICE_ROW_COUNT}, found {rows}")
if authored_events != EXPECTED_EVENT_COUNT:
    gaps.append(f"authored event coverage drift: expected {EXPECTED_EVENT_COUNT}, found {authored_events}")

if gaps:
    print("CHOICE_TRANSITION_SEMANTICS: FAIL")
    print(f"events={len(blocks)}")
    print(f"normal_events={normal_events}")
    print(f"choice_rows={rows}")
    print(f"special_state_events={special_rows}")
    print(f"authored_events={authored_events}")
    print(f"semantic_gaps={len(gaps)}")
    for gap in gaps[:100]: print(f"- {gap}")
    if len(gaps) > 100: print(f"- ... {len(gaps)-100} more")
    raise SystemExit(1)

print("CHOICE_TRANSITION_SEMANTICS: PASS")
print(f"events={len(blocks)}")
print(f"normal_events={normal_events}")
print(f"choice_rows={rows}")
print(f"special_state_events={special_rows}")
print(f"authored_events={authored_events}")
print("semantic_gaps=0")
print("at_least_A_and_B=true")
print("documented_additional_choice_E108_C=true")
print("explicit_transition_payload=true")
print("alternative_effect_signatures_distinct=true")
print("authored_event_coverage=true")
print(f"frozen_cardinality={EXPECTED_EVENT_COUNT}/{EXPECTED_NORMAL_EVENT_COUNT}/{EXPECTED_SPECIAL_EVENT_COUNT}/{EXPECTED_CHOICE_ROW_COUNT}")
