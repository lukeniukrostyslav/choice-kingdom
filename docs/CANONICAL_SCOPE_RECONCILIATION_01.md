# Choice Kingdom — Canonical Scope Reconciliation 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA — CANONICAL SCOPE CLARIFICATION

## Purpose

Resolve the remaining documentation wording that incorrectly treats E35–E40 as unresolved legacy source IDs.

## Authoritative scope

The frozen production authored checkpoint is **E01–E272**. `docs/EVENT_CATALOG_ACT_V_EXPANSION.md` explicitly states that it is a continuation of `docs/EVENT_CATALOG.md` and extends the initial E01–E34 skeleton. Therefore E35–E272 are part of the canonical authored scope unless a later explicit scope decision changes the frozen boundary.

## E35–E40 disposition

- E35 is canonical and consumes the E33 resolution state.
- E36 is canonical and must retain its stable ID; downstream distinction from E226 remains a separate QA task.
- E37 is canonical; downstream distinction from E227 remains open.
- E38 is canonical and explicitly produces `hereditary_seats_limited` on choice A. This is a verified producer for delayed-consequence analysis.
- E39 is canonical; downstream distinction from E229 remains open.
- E40 is canonical; downstream distinction from E241 remains open.

## Important distinction

Canonical scope status is separate from semantic-duplicate status. A node can be canonical while still requiring a source-level duplicate/semantic-collision audit. The correct state for E35–E40 is therefore **canonical, with selected downstream comparisons still open**, not "legacy source-ID conflict unresolved".

## Consequence for QA backlog

The old backlog item:

`E35–E40 legacy source-ID conflict fully resolved in canonical catalog`

must not be interpreted as a requirement to renumber or exclude E35–E40. It should be replaced by explicit downstream distinction checks for E36/E226, E37/E227, E39/E229 and E40/E241, while preserving E35–E40 as canonical authored nodes.

## Engine gate

This clarification does not authorize engine implementation by itself. Producer/consumer validation, delayed-consequence normalization, replay metadata inventory, ending path coverage and full causal reachability remain required before production schema and runtime promotion.
