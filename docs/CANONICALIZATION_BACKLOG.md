# Choice Kingdom — Canonicalization Backlog

## Scope

Current authored scope: **E01–E272**.

This backlog tracks canonical production readiness. Documentation completion alone does not constitute implementation or runtime readiness.

## Source inventory

- [x] Authored source ranges inventoried.
- [x] Stable event IDs inventoried through E01–E272.
- [x] Duplicate-title / semantic-collision review initiated.
- [x] Canonical namespaces reviewed.
- [x] Semantic collision policy recorded.
- [x] Exact-source compare E73/E156 completed; source-level distinction confirmed.
- [x] Exact-source compare E99/E173 completed; source-level distinction confirmed.
- [x] Border-crisis producer discovery completed at source level through E271–E272; graph integration remains open.
- [ ] Machine-readable trigger token inventory fully reconciled.
- [ ] Flag/history/thread producers fully enumerated.
- [ ] Relationship mutations and gates fully enumerated.
- [ ] Delayed-consequence source/consumer registry fully reconciled.
- [ ] E35–E40 legacy source-ID conflict fully resolved in canonical catalog.
- [ ] Legacy → canonical ID mapping fully reconciled.

## Consistency audit

- [ ] Producer → consumer validation across E01–E272.
- [ ] Duplicate semantic flag detection.
- [ ] Undefined trigger detection.
- [ ] Impossible prerequisite detection.
- [ ] Incoming-edge audit.
- [ ] Outgoing-edge audit.
- [ ] Branch rejoin audit.
- [ ] Mutually-exclusive branch audit.
- [ ] Full graph ↔ catalog reconciliation.
- [ ] Apply and verify E55/E269 resolution in canonical catalog.
- [ ] Apply and verify E36/E226 resolution in canonical catalog.
- [ ] Verify downstream distinctions E37/E227, E39/E229, E40/E241.

## Delayed consequences / replay

- [ ] Stable consequence IDs.
- [ ] Source → consequence mapping.
- [ ] Earliest/latest turn constraints.
- [ ] Exactly-once semantics.
- [ ] Replay metadata and second-run conditions.
- [ ] Invalidated / superseded consequence handling.

## Pacing / balance

- [ ] Resource-pressure audit.
- [ ] Choice-impact audit.
- [ ] Early/mid/late callback distribution.
- [ ] Replay divergence audit.
- [ ] Ending-path simulation.
- [ ] Critical-prerequisite simulation.

## Production catalog gate

**BLOCKED until the remaining producer/consumer, graph, delayed-consequence, reachability, ending, and source-ID audits are implemented and their results recorded.**

The authoritative source-comparison record is `docs/LEGACY_SOURCE_COMPARISON_02.md`. The semantic-collision status is recorded in `docs/SEMANTIC_COLLISION_RESOLUTION_01.md`.
