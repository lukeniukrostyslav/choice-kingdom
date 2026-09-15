#!/usr/bin/env python3
"""Verify every frozen source-closed producer is backed by an authored event/choice."""
from __future__ import annotations
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json").read_text(encoding="utf-8"))
first = int(manifest["scope"]["first_event"])
last = int(manifest["scope"]["last_event"])
excluded = set(manifest["scope"].get("excluded_events", []))
expected = {f"E{i:02d}" for i in range(first, last + 1)} - excluded
sources = manifest["source_of_truth"]["catalog_sources"]
head_re = re.compile(r"^### (E\d{2,3}) — (.+)$", re.M)
choice_re = re.compile(r"(?:^|\n)\s*(?:-\s*)?\*\*([AB])\s*(?:—|:|-)", re.M)

blocks: dict[str, str] = {}
for source in sources:
    text = (ROOT / source).read_text(encoding="utf-8")
    matches = list(head_re.finditer(text))
    for i, m in enumerate(matches):
        event = m.group(1)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        if event in blocks:
            raise SystemExit(f"duplicate authored event heading: {event}")
        blocks[event] = text[m.start():end]

errors: list[str] = []
for row in manifest.get("source_closed_producers", []):
    fact = row["fact"]
    event = row["event"]
    choice = row["choice"]
    if event not in expected:
        errors.append(f"{fact}: producer event {event} is outside frozen scope")
        continue
    block = blocks.get(event, "")
    if not block:
        errors.append(f"{fact}: producer event {event} missing from authored catalogs")
        continue
    if choice == "explicit crisis outcome":
        if "pred.transport_disruption" not in block:
            errors.append(f"{fact}: explicit crisis outcome contract missing from {event}")
        continue
    choices = {m.group(1) for m in choice_re.finditer(block)}
    wanted = {choice} if choice in {"A", "B"} else {"A", "B"}
    if not wanted.issubset(choices):
        errors.append(f"{fact}: declared choice {choice} not present in {event} (choices={sorted(choices)})")

print("SOURCE_CLOSED_PRODUCERS: FAIL" if errors else "SOURCE_CLOSED_PRODUCERS: PASS")
print(f"events_in_scope={len(expected)}")
print(f"declared_source_closed_producers={len(manifest.get('source_closed_producers', []))}")
print(f"errors={len(errors)}")
for error in errors:
    print(f"- {error}")
if errors:
    sys.exit(1)
