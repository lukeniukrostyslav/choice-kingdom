from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs/MACHINE_CANONICAL_GRAPH_01.json"
EXPECTED = {f"E{i:02d}" for i in range(1, 273)}
HEADING = re.compile(r"^### (E\d{2,3}) — .+$", re.M)
CHOICE_HEADING = re.compile(r"^(?:-\s*)?\*\*([AB])\s*[—:]\s*(.*?)\*\*", re.M)
CHOICE_PLAIN = re.compile(r"^\s*-\s*([AB])(?:\s+[A-Za-zА-Яа-я]|\s*[—:])(.+?)\s*$", re.M)
DELTA_RE = re.compile(r"[+-](?:\d+(?:\.\d+)?\s*)?[A-Za-zА-Яа-я_]+")
TOKEN_RE = re.compile(r"`[^`]+`")
CLAUSE_RE = re.compile(r"^\s*-\s*(?:Immediate|Flag|Unlock|Producer|Delayed|Resolution|Clear|Trigger|Effect|State|History|Meta|Ending|Condition)\s*:", re.I | re.M)
LIFECYCLE_RE = re.compile(r"\b(?:clear|clears|reset|resets|resolve|resolves|cancel|cancels|invalidate|invalidates|revoke|revokes|prevent|prevents|schedule|schedules|unlock|unlocks|create|creates|strengthen|strengthens|close|closes|establish|establishes|produce|produces|record|records|later|delayed|immediate|risk|route|evidence|pressure|credibility|stability|reform|contradiction)\b", re.I)
ACTION_RE = re.compile(r"\b(?:open|follow|inspect|subsidize|trace|replace|honor|renegotiate|protect|hear|catalogue|destroy|admit|close|end|publish|leave|accept|refuse|verify|investigate|preserve|compensate|hunt|fund|requisition|restrict|allow|deny|offer|grant|reject|raid|archive|sign|search|defend|punish|write|remove|keep|take|ask|invoke|ratify|endorse|decide|continue|expose|conceal|redact|submit|seal|audit|centralize|support|withdraw)\b", re.I)
STATE_HINT = re.compile(r"(?:\b(?:state|flag|predicate|history|thread|meta|ending|cycle|condition|route|evidence|trigger|effect|immediate|delayed|unlock|producer|resolution)\b|`[^`]+`)", re.I)
SPECIAL_EVENTS = {"E32", "E61", "E62", "E63", "E64", "E65", "E66", "E67", "E68", "E69", "E70", "E210", "E270"}
SPECIAL_EVENT_HINT = re.compile(r"\b(?:Source-level producer|canonical producer|explicitly establishes|explicitly records|derived gate|Ending|Purpose|convergence-only|resolution families|convergence producer|convergence decision)\b", re.I)


def semantic_signature(body: str) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    return (
        tuple(DELTA_RE.findall(body)),
        tuple(TOKEN_RE.findall(body)),
        tuple(sorted(set(m.group(0).lower() for m in LIFECYCLE_RE.finditer(body)))),
        tuple(sorted(set(m.group(0).lower() for m in ACTION_RE.finditer(body)))),
    )


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
missing_special = sorted(SPECIAL_EVENTS - set(blocks), key=lambda x: int(x[1:]))
if missing_special:
    fail("special-event classification references missing events: " + ", ".join(missing_special))

gaps: list[str] = []
rows = 0
special_rows = 0
triggered_events = 0
for event_id in sorted(EXPECTED, key=lambda x: int(x[1:])):
    block = blocks[event_id]

    # Every production event needs an authored trigger so the content contract
    # cannot contain an orphan node that only exists structurally in the catalog.
    if not re.search(r"^\*\*Trigger:\*\*", block, re.M):
        gaps.append(f"{event_id}: missing authored Trigger section")
    else:
        triggered_events += 1

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

    if not matches:
        gaps.append(f"{event_id}: no authored A/B choices")
        continue
    if len(matches) != 2 or set(labels) != {"A", "B"}:
        gaps.append(f"{event_id}: expected exactly one A and one B choice, found {labels}")
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

    if signatures.get("A") == signatures.get("B"):
        gaps.append(f"{event_id}: A/B choices have identical authored effect signatures")

if gaps:
    print("CHOICE_TRANSITION_SEMANTICS: FAIL")
    print(f"events={len(blocks)}")
    print(f"choice_rows={rows}")
    print(f"special_state_events={special_rows}")
    print(f"events_with_trigger={triggered_events}")
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
print(f"events_with_trigger={triggered_events}")
print("semantic_gaps=0")
print("exactly_one_A_and_one_B=true")
print("explicit_transition_payload=true")
print("alternative_effect_signatures_distinct=true")
print("authored_trigger_coverage=true")
