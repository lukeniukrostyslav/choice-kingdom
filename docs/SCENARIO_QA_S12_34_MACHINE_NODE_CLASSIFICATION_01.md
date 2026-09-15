# Scenario QA S12.34 — Machine Graph Node Classification 01

## Purpose

Advance the E01–E272 canonical graph from degree-count discovery toward a machine-checkable classification inventory without falsely declaring semantic orphans.

## Scope

- Frozen production scope: **E01–E272**.
- E273–E277 remain excluded from production graph semantics.
- This pass consumes the canonical machine graph manifest, authoritative catalog-source list, and `EVENT_GRAPH.md`.

## What changed

Added `tools/classify_graph_nodes.py`.

The classifier compiles every frozen event into one QA candidate class:

- `SOURCE_MISSING` — no authoritative catalog heading was found in the configured source set.
- `REPLAY_CANDIDATE` — E247–E250 replay-divergence layer.
- `DELAYED_CONSUMER_CANDIDATE` — event is listed in the canonical delayed-consumer registry.
- `TERMINAL_OR_ENDING_CANDIDATE` — late endgame node with no outbound design edge.
- `ISOLATED_CANDIDATE` — zero graph degree; explicitly **not** a true-orphan verdict.
- `ROOT_CANDIDATE` — no inbound design edge.
- `TERMINAL_OR_CONSUMER_CANDIDATE` — no outbound design edge.
- `ORDINARY_GRAPH_NODE` — both inbound and outbound design edges exist.

The generated JSON inventory is intentionally CI-produced because the classification is derived data, not an authored source of truth.

## Existing graph findings carried forward

S12.32 established the current degree-level baseline:

- 270/272 catalog headings are currently discoverable from the configured authoritative catalog source set.
- 296 unique design-level event edges are present.
- 69 catalog events have no outbound design edge.
- 15 are inbound-only candidates.
- 54 are currently unreferenced candidates.

These counts are **classification candidates**, not reachability proof. A node with no outbound edge may be a terminal, ending qualification node, consumer-only node, delayed callback, or intentionally isolated source. A node with no inbound edge may be a root/source node rather than an orphan.

## Important unresolved source gap

E33 and E34 remain `SOURCE_MISSING` until exact authoritative authored headings/effects/delayed semantics are recovered. The QA layer does not invent them.

## Verification contract

GitHub Actions now runs:

1. `python3 tools/validate_canonical_graph.py`
2. `python3 tools/classify_graph_nodes.py`

The first remains the source-level canonical contract gate. The second is a deterministic derived inventory and must not be treated as an authored semantic contract.

## Result / interpretation

S12.34 materially improves the machine QA boundary: the 69 no-outbound candidates can now be classified mechanically before semantic closure work, while preserving the hard rule that degree alone cannot prove an orphan or reachability.

### Still OPEN

- complete producer→consumer token matrix;
- authoritative semantic classification of every candidate;
- fresh-run reachability;
- replay reachability with strict `meta.*` isolation;
- ending incoming paths and deterministic precedence;
- catalog↔machine semantic equality;
- E33/E34 authoritative source recovery.

## Gate status

**S12.34 = machine classification infrastructure GREEN; semantic orphan/reachability closure remains OPEN.**
