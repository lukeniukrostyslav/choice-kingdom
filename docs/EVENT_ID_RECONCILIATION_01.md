# Choice Kingdom — Event ID Reconciliation 01

Date: 2026-09-14
Status: **PROVISIONAL MAPPING — NOT SCHEMA READY**

## Purpose
Resolve the verified E35–E40 source collision without deleting authored material or silently changing stable IDs.

## Canonical-source decision
For the current campaign, `docs/EVENT_CATALOG_ACT_V_EXPANSION.md` is the candidate canonical source for E35 onward because it explicitly extends the E01–E34 skeleton and is the source represented by the expanded event graph.

The six older nodes in `docs/EVENT_CATALOG.md` are therefore retained as **legacy authored nodes**, not executable duplicate IDs.

## Provisional legacy mapping

| Legacy source ID | Legacy title | Provisional preserved ID | Action before schema lock |
|---|---|---|---|
| E35 | The Last Council | LEGACY-E35 | Compare narrative purpose against E47/E51/E60 and either merge or assign a new canonical ID |
| E36 | The Ledger Opens | LEGACY-E36 | Compare against E43/E53 and investigation spine; preserve any unique consequences |
| E37 | The Choice of Heir | LEGACY-E37 | Compare against E59/E60 and succession logic; preserve unique succession consequences if needed |
| E38 | The Final Speech | LEGACY-E38 | Compare against E60/final constitutional scenes; preserve only if it adds a distinct player-state consequence |
| E39 | The Crown's Answer | LEGACY-E39 | Compare against E58/E59/E60; likely merge candidate, but no deletion before downstream audit |
| E40 | Epilogue: What Remains | LEGACY-E40 | Compare against E68–E70 replay/epilogue hooks; retain only if its historical consequence is distinct |

## Important rule
`LEGACY-E35` through `LEGACY-E40` are audit identifiers only. They must **not** be consumed by the production engine.

No final replacement IDs are assigned yet. Assigning E271+ automatically would inflate the campaign without proving that the old nodes contain unique causal content. Merging them automatically would risk deleting authored consequences. The correct next step is downstream comparison.

## Downstream comparison targets
- LEGACY-E35 → E47, E51, E58–E60
- LEGACY-E36 → E43, E53, investigation/ledger nodes
- LEGACY-E37 → E59–E60 and succession/ending predicates
- LEGACY-E38 → E60 and ending/constitutional callbacks
- LEGACY-E39 → E58–E60 and ending resolution
- LEGACY-E40 → E68–E70 and ending epilogues

## Required verification before schema lock
1. Compare every choice and consequence in each legacy node with current canonical nodes.
2. Identify unique flags, relationship changes, delayed effects, history markers and ending effects.
3. Trace all incoming/outgoing references to the legacy concepts.
4. Merge unique causal content into an existing canonical event where appropriate, or allocate a new stable ID only when the event is genuinely distinct.
5. Update `EVENT_GRAPH.md`, `CONTENT_QA_MATRIX.md`, canonical audits and all references atomically.
6. Run duplicate-ID and reachability checks after reconciliation.

## Gate
This document resolves the ambiguity at the **source-management level**, but the content itself is not yet reconciled. Production schema remains blocked until the downstream comparison is complete.
