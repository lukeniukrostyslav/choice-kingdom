# Choice Kingdom — Canonicalization Backlog

## Scope

Current authored scope: **E01–E272**.

This backlog tracks canonical production readiness. Documentation completion alone does not constitute implementation or runtime readiness.

- [x] Authored source ranges inventoried.
- [x] Stable event IDs inventoried through E01–E272.
- [x] E35–E40 confirmed as canonical authored nodes; downstream distinctions remain separate QA work.
- [x] Duplicate-title / semantic-collision review initiated.
- [x] Canonical namespaces reviewed.
- [x] Semantic collision policy recorded.
- [x] Exact-source compare E73/E156 completed; source-level distinction confirmed.
- [x] Exact-source compare E99/E173 completed; source-level distinction confirmed.
- [x] Border-crisis producer discovery completed at source level through E271–E272; graph integration remains open.
- [x] Safe prose-trigger normalization pass recorded for predicate families already defined by the canonical matrix.
- [x] E243 delayed trigger normalized exactly from E18-B `public_bridge`; stale graph-audit wording corrected.
- [ ] Machine-readable trigger token inventory fully reconciled.
- [ ] Flag/history/thread producers fully enumerated.
- [ ] Relationship mutations and gates fully enumerated.
- [ ] Delayed-consequence source/consumer registry fully reconciled.
- [ ] Legacy → canonical ID mapping fully reconciled where historical comparison documents still use old wording.

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
- [x] Apply and verify E55/E269 resolution in canonical catalog.
- [x] Apply and verify E36/E226 resolution in canonical catalog.
- [ ] Verify downstream distinctions E37/E227, E39/E229, E40/E241.

E35–E40 are not a renumbering/exclusion problem. The authoritative Act V source explicitly continues E01–E34, and E38-A is a verified producer of `hereditary_seats_limited`. See `docs/CANONICAL_SCOPE_RECONCILIATION_01.md`.

## Delayed consequences / replay

- [ ] Stable consequence IDs.
- [ ] Source → consequence mapping.
- [ ] Earliest/latest turn constraints.
- [ ] Exactly-once semantics.
- [ ] Replay metadata and second-run conditions.
- [ ] Invalidated / superseded consequence handling.
- [x] E243 producer correction and exact `public_bridge` normalization recorded.
- [ ] E245 compensation-route producer decision.
- [ ] E184 secret-evidence producer closure.
- [ ] E246 explicit price-ceiling vocabulary normalization.

## Pacing / balance

- [ ] Resource-pressure audit.
- [ ] Choice-impact audit.
- [ ] Early/mid/late callback distribution.
- [ ] Replay divergence audit.
- [ ] Ending-path simulation.
- [ ] Critical-prerequisite simulation.

## Production catalog gate

**BLOCKED until the remaining producer/consumer, graph, delayed-consequence, reachability, ending, and source-ID audits are implemented and their results recorded.**

The authoritative source-comparison record is `docs/LEGACY_SOURCE_COMPARISON_02.md`. The semantic-collision status is recorded in `docs/SEMANTIC_COLLISION_RESOLUTION_01.md`. The latest safe trigger-normalization pass is `docs/CANONICAL_TRIGGER_NORMALIZATION_03.md`. E243's correction record is `docs/DELAYED_GRAPH_EDGE_CORRECTION_01.md`.
