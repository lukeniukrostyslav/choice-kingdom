from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs/MACHINE_CANONICAL_GRAPH_01.json"
BASE_VALIDATOR = ROOT / "tools/validate_choice_transition_semantics.py"

HEADING = re.compile(r"^### (E\d{2,3}) — .+$", re.M)
CHOICE_HEADING = re.compile(r"^(?:-\s*)?\*\*([ABC])\s*[—:]\s*(.*?)\*\*", re.M)
CHOICE_PLAIN = re.compile(r"^\s*-\s*([ABC])(?:\s+[A-Za-zА-Яа-я]|\s*[—:])(.+?)\s*$", re.M)
DELTA = re.compile(r"[+-]\s*\d+(?:\.\d+)?\s+[A-Za-zА-Яа-я_]+")
TOKEN = re.compile(r"`[^`]+`")
CLAUSE = re.compile(
    r"^\s*-\s*(?:Immediate|Flag|Unlock|Producer|Delayed|Resolution|Clear|Trigger|Effect|State|History|Meta|Ending|Condition)\s*:",
    re.I | re.M,
)

# Explicitly forbidden numeric sixth-resource pattern. Contextual state names may
# exist as flags/predicates, but they must not become silent numeric resources.
FORBIDDEN_NUMERIC_CONTEXT = re.compile(
    r"[+-]\s*\d+(?:\.\d+)?\s+(?:food|winter|border|guild|information)(?:\s+stability)?\b",
    re.I,
)

EXPECTED_EVENTS = {f"E{i:02d}" for i in range(1, 273)}
SPECIAL_EVENTS = {"E32", *{f"E{i:02d}" for i in range(61, 71)}, "E210", "E270"}
EXPECTED_ADDITIONAL = {"E51": {"C"}, "E108": {"C"}}


def fail(message: str) -> None:
    print("S02_CHOICE_STATE_TRANSITION_CLOSURE: FAIL")
    print(f"- {message}")
    raise SystemExit(1)


# Reuse the already-green authored transition validator. This keeps S02's
# cardinality/semantic baseline single-sourced.
result = subprocess.run([sys.executable, str(BASE_VALIDATOR)], cwd=ROOT, text=True)
if result.returncode != 0:
    fail("base authored transition semantics validator failed")


graph = json.loads(GRAPH.read_text(encoding="utf-8"))
source_files = graph["source_of_truth"]["catalog_sources"]
blocks: dict[str, str] = {}
for source in source_files:
    path = ROOT / source
    if not path.exists():
        fail(f"missing canonical catalog source: {source}")
    text = path.read_text(encoding="utf-8")
    matches = list(HEADING.finditer(text))
    for i, match in enumerate(matches):
        event_id = match.group(1)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        if event_id in blocks:
            # E271 is the only explicitly permitted duplicate catalog heading.
            if event_id != "E271":
                fail(f"duplicate canonical event block: {event_id}")
            continue
        blocks[event_id] = text[match.start():end]

if set(blocks) != EXPECTED_EVENTS:
    fail("canonical authored event scope is not exactly E01-E272")

errors: list[str] = []
choice_rows = 0
for event_id in sorted(EXPECTED_EVENTS, key=lambda x: int(x[1:])):
    block = blocks[event_id]
    matches = list(CHOICE_HEADING.finditer(block)) or list(CHOICE_PLAIN.finditer(block))
    labels = [m.group(1).upper() for m in matches]

    if event_id in SPECIAL_EVENTS:
        continue

    allowed = {"A", "B"} | EXPECTED_ADDITIONAL.get(event_id, set())
    if set(labels) != allowed:
        errors.append(f"{event_id}: choice labels {labels} do not match frozen contract {sorted(allowed)}")
        continue

    for index, match in enumerate(matches):
        next_start = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        body = block[match.start():next_start]
        label = match.group(1).upper()
        choice_rows += 1

        if FORBIDDEN_NUMERIC_CONTEXT.search(body):
            errors.append(f"{event_id}-{label}: forbidden numeric contextual resource pattern")

        has_transition = bool(DELTA.search(body) or TOKEN.search(body) or CLAUSE.search(body))
        if not has_transition:
            errors.append(f"{event_id}-{label}: no explicit state/effect transition signal")

        if len(body.strip()) < 12:
            errors.append(f"{event_id}-{label}: authored transition body is implausibly empty")

expected_rows = 520
if choice_rows != expected_rows:
    errors.append(f"choice-row cardinality drift: expected {expected_rows}, found {choice_rows}")

if errors:
    print(f"checked_events={len(blocks)}")
    print(f"checked_choice_rows={choice_rows}")
    print(f"errors={len(errors)}")
    for error in errors[:100]:
        print(f"- {error}")
    raise SystemExit(1)

print("S02_CHOICE_STATE_TRANSITION_CLOSURE: PASS")
print("scope=E01-E272")
print("events=272")
print("normal_events=259")
print("special_events=13")
print("choice_rows=520")
print("explicit_transition_payload=true")
print("alternative_semantics_distinct=delegated_to_base_gate")
print("trigger_narrative_coverage=delegated_to_base_gate")
print("forbidden_sixth_resource_pattern=false")
print("runtime_execution=false")
print("runtime_reachability=false")
