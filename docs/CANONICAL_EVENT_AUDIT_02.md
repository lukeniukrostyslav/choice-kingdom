# Choice Kingdom — Canonical Event Audit 02

Date: 2026-09-14
Scope: targeted cross-file reconciliation after Audit 01
Status: **AUDIT IN PROGRESS — NOT CONTENT READY**

## Findings

### 1. Repeated character-event titles are broader than the first audit recorded

The authored set contains additional repeated titles:

- E36 — **Mara's Resignation**
- E95 — **Mara's Resignation Letter** (same narrative role; near-duplicate title)
- E226 — **Mara's Resignation**
- E37 — **Rowan's Oath**
- E96 — **Rowan's Oath**

These may be intentional callbacks, but they currently risk presenting separate causal nodes as interchangeable scenes. Canonicalization must retain stable IDs and add context labels/subtitles where callbacks are intended. Narrative QA must also verify that the later nodes materially react to changed state rather than merely replaying the same conversation.

### 2. Several trigger expressions are clearly derived conditions, not durable flags

Examples observed in the expansion corpus include:

- `high trust`
- `strong treasury pressure`
- `food shortage`
- `winter severity`
- `border tension`
- `low security`
- `strong market oversight`
- `severe winter`
- `low army readiness`
- `guild labor tension`
- `information route`
- `high information pressure`
- `simultaneous food, border and civic pressure`
- `at least two procurement clues`
- `three or more related clues`

These must not be silently encoded as arbitrary booleans. Each needs either a deterministic formula over canonical resources/history/threads or an explicit canonical state marker. Otherwise reachability and balance simulation will be non-reproducible.

### 3. The catalog contains semantically similar but differently named state facts

Examples that require normalization review:

- `local_relief_councils` vs `civic relief` / `local civic participation` concepts;
- `public_infrastructure_trust` vs `public_bridge`;
- `guild leverage`, `merchant charter`, `guild political representation` and `commercial route`;
- `winter severity`, `severe winter`, `winter illness` and `food pressure`;
- `information route`, `information pressure`, `secret evidence route` and named evidence flags.

These should be represented by canonical thread/history/flag IDs or derived conditions, not by a growing uncontrolled vocabulary.

### 4. Repeated event concepts require downstream-difference verification

E36/E95/E226 and E37/E96 are especially important because they all concern institutional/military loyalty. QA must prove that each occurrence has a distinct prerequisite, decision pressure and downstream consequence. If one is only a textual repeat, it should be rewritten or converted into a callback that explicitly references the earlier choice.

### 5. Existing graph and authored triggers can diverge

`EVENT_GRAPH.md` contains useful candidate edges, but its edges are not yet a verified runtime registry. For example, it connects expansion events across later nodes while the catalog still uses prose conditions. Canonicalization must treat the event catalog + state vocabulary as the source material and the graph as a consistency target, then report graph-only or catalog-only edges.

## Actionable QA work

1. Add every repeated title/near-title to a disambiguation list.
2. Convert derived trigger phrases into named deterministic predicates.
3. Build producer/consumer maps for durable flags.
4. Separate current-run facts from immutable history and replay metadata.
5. Verify each repeated character callback changes future state or interpretation.
6. Compare graph edges against actual trigger/effect relationships.
7. Do not increase event count until these checks identify a genuine content gap.

## Gate

This audit increases the precision of the canonicalization phase but does **not** increase engine readiness. E01–E270 remain authored, not production-integrated.
