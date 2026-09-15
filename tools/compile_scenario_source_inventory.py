#!/usr/bin/env python3
"""Compile a conservative producer/consumer inventory from canonical scenario prose."""
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
first = int(manifest.get("scope", {}).get("first_event", 1)); last = int(manifest.get("scope", {}).get("last_event", 272))
expected = {f"E{i:02d}" for i in range(first, last + 1)} - excluded
heading_re = re.compile(r"^### (E\d{2,3}) — (.+)$", re.M)
trigger_re = re.compile(r"^\*\*Trigger:\*\* (.*)$", re.M)
backtick_re = re.compile(r"`([^`]+)`")
choice_re = re.compile(r"^- \*\*[AB]\b.*$", re.M)
errors: list[str] = []; events: dict[str, dict] = {}; producers: dict[str, list[dict]] = defaultdict(list); consumers: dict[str, list[dict]] = defaultdict(list); predicate_edges: dict[str, set[str]] = defaultdict(set)
for source in sources:
    path = ROOT / source
    if not path.exists(): errors.append(f"missing catalog: {source}"); continue
    text = path.read_text(encoding="utf-8"); matches = list(heading_re.finditer(text))
    for index, match in enumerate(matches):
        event_id, title = match.group(1), match.group(2).strip()
        if event_id in events: errors.append(f"duplicate authored event heading: {event_id}"); continue
        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(text); block = text[match.start():block_end]
        trigger_match = trigger_re.search(block); trigger_text = trigger_match.group(1).strip() if trigger_match else ""; trigger_tokens = sorted(set(backtick_re.findall(trigger_text)))
        choices = []
        for choice in choice_re.findall(block):
            output_tokens = sorted(set(backtick_re.findall(choice))); choices.append({"text": choice, "outputs": output_tokens})
            for token in output_tokens: producers[token].append({"event": event_id, "source": source, "choice": choice[:120]})
        for token in trigger_tokens: consumers[token].append({"event": event_id, "source": source, "trigger": trigger_text})
        for source_predicate in [t for t in trigger_tokens if t.startswith("pred.")]:
            for target_predicate in sorted({t for c in choices for t in c["outputs"] if t.startswith("pred.")}): predicate_edges[source_predicate].add(target_predicate)
        events[event_id] = {"event_id": event_id, "title": title, "source": source, "trigger": trigger_text, "trigger_tokens": trigger_tokens, "choices": choices}
missing = sorted(expected - set(events), key=lambda x: int(x[1:])); extra = sorted(set(events) - expected, key=lambda x: int(x[1:]))
if missing: errors.append("missing expected events: " + ", ".join(missing))
if extra: errors.append("events outside frozen scope: " + ", ".join(extra))
duplicates = {token: writers for token, writers in sorted(producers.items()) if len(writers) > 1}
# Same canonical token written by both mutually-exclusive choices of one event is a source-level contradiction.
contradictory_writers: dict[str, list[dict]] = {}
for event_id, event in events.items():
    by_token: dict[str, set[str]] = defaultdict(set)
    for choice in event["choices"]:
        m = re.match(r"^- \*\*([AB])\b", choice["text"])
        if not m: continue
        for token in choice["outputs"]: by_token[token].add(m.group(1))
    for token, labels in by_token.items():
        if {"A", "B"}.issubset(labels): contradictory_writers.setdefault(token, []).append({"event": event_id, "choices": sorted(labels)})
if contradictory_writers: errors.append("same-event contradictory writers: " + "; ".join(f"{token} ({','.join(x['event'] for x in xs)})" for token, xs in sorted(contradictory_writers.items())))
# Cross-event duplicate writers are not automatically contradictions: they are retained as an
# explicit semantic-writer review set so the QA process cannot silently collapse multiple sources.
semantic_writer_collisions = {
    token: writers for token, writers in duplicates.items()
    if len({writer["event"] for writer in writers}) > 1
}
undefined_consumers = sorted({token for token in consumers if token not in producers})
predicate_nodes = sorted(set(predicate_edges) | {t for t in producers if t.startswith("pred.")} | {t for t in consumers if t.startswith("pred.")})
predicate_graph = {node: sorted(predicate_edges.get(node, set())) for node in predicate_nodes}
predicate_cycles: list[list[str]] = []; state: dict[str, int] = {}; stack: list[str] = []
def visit(node: str) -> None:
    state[node] = 1; stack.append(node)
    for target in predicate_graph.get(node, []):
        if state.get(target, 0) == 0: visit(target)
        elif state.get(target) == 1 and target in stack:
            cycle = stack[stack.index(target):] + [target]
            if cycle not in predicate_cycles: predicate_cycles.append(cycle)
    stack.pop(); state[node] = 2
for node in predicate_nodes:
    if state.get(node, 0) == 0: visit(node)
undefined_predicate_consumers = sorted({t for t in consumers if t.startswith("pred.") and t not in producers})
if predicate_cycles: errors.append("predicate dependency cycle(s): " + "; ".join(" -> ".join(c) for c in predicate_cycles))
inventory = {"schema":"choice-kingdom-scenario-source-inventory-2","scope":{"first_event":first,"last_event":last,"excluded_events":sorted(excluded)},"event_count":len(events),"events":[events[k] for k in sorted(events,key=lambda x:int(x[1:]))],"producers":dict(sorted(producers.items())),"consumers":dict(sorted(consumers.items())),"duplicate_output_tokens":duplicates,"semantic_writer_collisions":semantic_writer_collisions,"contradictory_same_event_writers":contradictory_writers,"undefined_consumers":undefined_consumers,"predicate_dependency_graph":predicate_graph,"undefined_predicate_consumers":undefined_predicate_consumers,"predicate_cycles":predicate_cycles,"notes":["Source-level inventory only; no gameplay/fresh-run reachability claim.","A trigger token without an extracted producer is unresolved, not invented.","All cross-event duplicate writers are retained as an explicit semantic-writer review set.","Same-event A/B writers for the same token are machine-failing contradictions.","Undefined consumers are reported separately from undefined predicate producers.","Predicate dependency cycles are machine-failing; undefined predicate producers remain source-QA findings until explicitly classified."]}
print("SOURCE_INVENTORY: FAIL" if errors else "SOURCE_INVENTORY: PASS")
for error in errors: print(f"- {error}")
print(f"events={len(events)} expected={len(expected)}"); print(f"unique_output_tokens={len(producers)}"); print(f"trigger_tokens={len(consumers)}"); print(f"duplicate_output_tokens={len(duplicates)}"); print(f"semantic_writer_collisions={len(semantic_writer_collisions)}"); print(f"contradictory_same_event_writers={len(contradictory_writers)}"); print(f"undefined_consumers={len(undefined_consumers)}"); print(f"predicate_nodes={len(predicate_nodes)}"); print(f"predicate_edges={sum(len(x) for x in predicate_graph.values())}"); print(f"undefined_predicate_consumers={len(undefined_predicate_consumers)}"); print(f"predicate_cycles={len(predicate_cycles)}")
if duplicates: print("duplicate_output_token_names=" + ",".join(sorted(duplicates)))
if contradictory_writers: print("contradictory_same_event_writer_names=" + ",".join(sorted(contradictory_writers)))
if undefined_consumers: print("undefined_consumer_names=" + ",".join(undefined_consumers))
if undefined_predicate_consumers: print("undefined_predicate_consumer_names=" + ",".join(undefined_predicate_consumers))
if errors: sys.exit(1)
out = ROOT / "scenario-source-inventory.json"; out.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"); print(f"inventory_file={out.name}")
