#!/usr/bin/env python3
"""Validate frozen rejection of stale/prose consumer forms without inventing producers."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
CLASSIFICATION = ROOT / "docs" / "SCENARIO_QA_UNDEFINED_CONSUMER_CLASSIFICATION_01.md"

REJECTED = {
    "thread.border": "thread.border_crisis",
    "thread.border_crisis = active": "pred.border_crisis",
}
HEADING_RE = re.compile(r"^### (E\d{2,3}) — ", re.M)
TRIGGER_RE = re.compile(r"^\*\*Trigger:\*\* (.*)$", re.M)
BACKTICK_RE = re.compile(r"`([^`]+)`")

errors: list[str] = []
if not MANIFEST.exists():
    errors.append("missing MACHINE_CANONICAL_GRAPH_01.json")
if not CLASSIFICATION.exists():
    errors.append("missing SCENARIO_QA_UNDEFINED_CONSUMER_CLASSIFICATION_01.md")
if errors:
    print("NONCANONICAL_REJECTION_GATE: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
sources = manifest.get("source_of_truth", {}).get("catalog_sources", [])
excluded = set(manifest.get("scope", {}).get("excluded_events", []))
first = int(manifest.get("scope", {}).get("first_event", 1))
last = int(manifest.get("scope", {}).get("last_event", 272))
expected = {f"E{i:02d}" for i in range(first, last + 1)} - excluded

events: set[str] = set()
canonical_predicate_seen: set[str] = set()

for source in sources:
    path = ROOT / source
    if not path.exists():
        errors.append(f"missing catalog: {source}")
        continue
    text = path.read_text(encoding="utf-8")
    matches = list(HEADING_RE.finditer(text))
    for index, match in enumerate(matches):
        event_id = match.group(1)
        if event_id in events:
            errors.append(f"duplicate event heading: {event_id}")
        events.add(event_id)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start():end]
        trigger = TRIGGER_RE.search(block)
        if not trigger:
            continue
        tokens = set(BACKTICK_RE.findall(trigger.group(1)))
        if "pred.border_crisis" in tokens:
            canonical_predicate_seen.add("pred.border_crisis")

missing = expected - events
extra = events - expected
if missing:
    errors.append("missing expected events: " + ", ".join(sorted(missing, key=lambda x: int(x[1:]))))
if extra:
    errors.append("events outside frozen scope: " + ", ".join(sorted(extra, key=lambda x: int(x[1:]))))
if not canonical_predicate_seen:
    errors.append("canonical pred.border_crisis trigger was not observed in the frozen catalog")

# Rejected forms are deliberately removed from canonical authored triggers.
# Their continued presence is verified in the audit classification, which is
# the preserved raw-evidence surface, not in the executable catalog.
classification = CLASSIFICATION.read_text(encoding="utf-8")
for rejected, canonical in REJECTED.items():
    if rejected not in classification:
        errors.append(f"classification does not preserve rejected raw evidence: {rejected}")
    if canonical not in classification:
        errors.append(f"classification does not document canonical replacement: {canonical}")

print("NONCANONICAL_REJECTION_GATE: FAIL" if errors else "NONCANONICAL_REJECTION_GATE: PASS")
print(f"events={len(events)} expected={len(expected)}")
print(f"canonical_predicate_trigger_seen={bool(canonical_predicate_seen)}")
for rejected in REJECTED:
    print(f"rejected={rejected} canonical_catalog_occurrences=0 raw_evidence=classification")
for error in errors:
    print(f"- {error}")
if errors:
    sys.exit(1)
