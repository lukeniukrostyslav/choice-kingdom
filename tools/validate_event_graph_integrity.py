#!/usr/bin/env python3
"""Validate the authored event graph's identifier and edge integrity.

This is intentionally a structural gate, not a gameplay reachability proof.
The design graph is a causal-map artifact and is not required to enumerate every
catalog event: terminal, consumer-only, qualification, delayed-callback and
otherwise unexpanded nodes may legitimately have no graph node yet. The gate
therefore validates every event ID that *is* represented in the graph, while
reporting coverage against the frozen production scope for follow-up work.
Semantic prerequisites, state effects, delayed timing and fresh-run reachability
remain separate gates.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "EVENT_GRAPH.md"

EVENT_RE = re.compile(r"\bE(\d{2,3})\b")
EDGE_RE = re.compile(r"`([^`]+)`")

FROZEN_MIN = 1
FROZEN_MAX = 272
EXCLUDED = set(range(273, 278))


def event_id(number: int) -> str:
    return f"E{number:02d}"


def main() -> int:
    text = GRAPH.read_text(encoding="utf-8")
    ids = {int(match.group(1)) for match in EVENT_RE.finditer(text)}

    errors: list[str] = []
    outside = sorted(n for n in ids if n < FROZEN_MIN or n > FROZEN_MAX)
    if outside:
        errors.append(
            "event IDs outside frozen E01-E272 scope: "
            + ", ".join(event_id(n) for n in outside)
        )

    excluded_present = sorted(ids & EXCLUDED)
    if excluded_present:
        errors.append(
            "excluded expansion IDs present in production graph: "
            + ", ".join(event_id(n) for n in excluded_present)
        )

    edge_count = 0
    self_edges: list[str] = []
    unknown_edge_nodes: set[int] = set()

    # Only inspect graph-code spans. Narrative prose elsewhere can mention IDs
    # without representing a causal edge.
    for code in EDGE_RE.findall(text):
        if "->" not in code and "-X->" not in code:
            continue
        tokens = [int(value) for value in EVENT_RE.findall(code)]
        if len(tokens) < 2:
            continue
        for source, target in zip(tokens, tokens[1:]):
            edge_count += 1
            if source == target:
                self_edges.append(event_id(source))
            for value in (source, target):
                if not (FROZEN_MIN <= value <= FROZEN_MAX):
                    unknown_edge_nodes.add(value)

    if self_edges:
        errors.append("self-edge(s): " + ", ".join(sorted(set(self_edges))))
    if unknown_edge_nodes:
        errors.append(
            "edge references outside frozen scope: "
            + ", ".join(event_id(n) for n in sorted(unknown_edge_nodes))
        )
    if not ids:
        errors.append("EVENT_GRAPH.md contains no event IDs")

    expected = set(range(FROZEN_MIN, FROZEN_MAX + 1))
    missing = sorted(expected - ids)

    print(f"graph events: {len(ids)}")
    print(f"graph causal edges inspected: {edge_count}")
    print(f"frozen scope: {event_id(FROZEN_MIN)}-{event_id(FROZEN_MAX)}")
    print(f"graph coverage of frozen scope: {len(ids)}/{len(expected)}")
    print(f"graph events not represented as graph nodes: {len(missing)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("EVENT GRAPH INTEGRITY: PASS")
    print("Note: this gate does not require exhaustive node coverage and does not prove semantic equality or gameplay reachability.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
