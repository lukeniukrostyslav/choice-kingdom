#!/usr/bin/env python3
"""Compile a conservative producer/consumer inventory from canonical scenario prose.

This is intentionally source-level only: it does not infer gameplay reachability,
turn scheduling, persistence, replay provenance, or predicate satisfaction.
It extracts exact authored event ids, trigger tokens, and option output tokens so
later gates can reason about producer/consumer coverage without inventing writers.
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"

if not MANIFEST.exists():
    print("SOURCE_INVENTORY: FAIL\n- missing canonical graph manifest")
    sys.exit(1)

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
sources = manifest.get("source_of_truth", {}).get("catalog_sources", [])
excluded = set(manifest.get("scope", {}).get("excluded_events", []))
first = int(manifest.get("scope", {}).get("first_event", 1))
last = int(manifest.get("scope", {}).get("last_event", 272))
expected = {f"E{i:02d}" for i in range(first, last + 1)} - excluded

heading_re = re.compile(r"^### (E\d{2,3}) — (.+)$", re.M)
trigger_re = re.compile(r"^\*\*Trigger:\*\* (.*)$", re.M)
backtick_re = re.compile(r"`([^`]+)`")
choice_re = re.compile(r"^- \*\*[AB]\b.*$", re.M)

errors: list[str] = []
events: dict[str, dict] = {}
producers: dict[str, list[dict]] = defaultdict(list)
consumers: dict[str, list[dict]] = defaultdict(list)

for source in sources:
    path = ROOT / source
    if not path.exists():
        errors.append(f"missing catalog: {source}")
        continue
    text = path.read_text(encoding="utf-8")
    matches = list(heading_re.finditer(text))
    for index, match in enumerate(matches):
        event_id, title = match.group(1), match.group(2).strip()
        if event_id in events:
            errors.append(f"duplicate authored event heading: {event_id}")
            continue
        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start():block_end]
        trigger_match = trigger_re.search(block)
        trigger_text = trigger_match.group(1).strip() if trigger_match else ""
        trigger_tokens = sorted(set(backtick_re.findall(trigger_text)))
        choices = []
        for choice in choice_re.findall(block):
            output_tokens = sorted(set(backtick_re.findall(choice)))
            choices.append({"text": choice, "outputs": output_tokens})
            for token in output_tokens:
                producers[token].append({"event": event_id, "source": source, "choice": choice[:120]})
        for token in trigger_tokens:
            consumers[token].append({"event": event_id, "source": source, "trigger": trigger_text})
        events[event_id] = {
            "event_id": event_id,
            "title": title,
            "source": source,
            "trigger": trigger_text,
            "trigger_tokens": trigger_tokens,
            "choices": choices,
        }

missing = sorted(expected - set(events), key=lambda x: int(x[1:]))
extra = sorted(set(events) - expected, key=lambda x: int(x[1:]))
if missing:
    errors.append("missing expected events: " + ", ".join(missing))
if extra:
    errors.append("events outside frozen scope: " + ", ".join(extra))

# A token can legitimately have several writers (e.g. repeated authored state),
# so duplicates are reported rather than treated as failures. Predicate contracts
# and semantic conflict rules decide whether a duplicate is valid.
duplicates = {
    token: writers for token, writers in sorted(producers.items()) if len(writers) > 1
}

inventory = {
    "schema": "choice-kingdom-scenario-source-inventory-1",
    "scope": {"first_event": first, "last_event": last, "excluded_events": sorted(excluded)},
    "event_count": len(events),
    "events": [events[k] for k in sorted(events, key=lambda x: int(x[1:]))],
    "producers": dict(sorted(producers.items())),
    "consumers": dict(sorted(consumers.items())),
    "duplicate_output_tokens": duplicates,
    "notes": [
        "Source-level inventory only; no gameplay/fresh-run reachability claim.",
        "A trigger token without an extracted producer is unresolved, not invented.",
        "Multiple writers are reported for semantic contradiction review.",
    ],
}

print("SOURCE_INVENTORY: FAIL" if errors else "SOURCE_INVENTORY: PASS")
for error in errors:
    print(f"- {error}")
print(f"events={len(events)} expected={len(expected)}")
print(f"unique_output_tokens={len(producers)}")
print(f"trigger_tokens={len(consumers)}")
print(f"duplicate_output_tokens={len(duplicates)}")
if duplicates:
    print("duplicate_output_token_names=" + ",".join(sorted(duplicates)))

if errors:
    sys.exit(1)

# Keep stdout compact for CI; write the full inventory for artifact upload.
out = ROOT / "scenario-source-inventory.json"
out.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"inventory_file={out.name}")
