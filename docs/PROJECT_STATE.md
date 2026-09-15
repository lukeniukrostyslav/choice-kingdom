# Choice Kingdom — Project State

Status: ACTIVE — canonical narrative/content QA before runtime implementation.

## Current position

The project is an original premium offline-first Android decision-and-consequence game set in Avelune. The authored first-campaign checkpoint is E01–E272; E273–E277 exists as a source patch/spec and is not yet part of the canonical production catalog freeze.

E33/E34 source recovery and canonical integration are now CLOSED at source/graph level. E33 `emergency_decree_used` is canonically connected to E35, E34 `people_heard` is consumed by E50, and E33 `emergency_power` / `constitutional_limit` are explicit authored components for downstream E62/E67 requirements. These flags remain contract-gated and are not silently promoted into stronger runtime predicates.

The ending-precedence boundary has been corrected to remove the stale E33/E34 quarantine. Runtime ending order remains OPEN: exact positive/negative prerequisite sets, deterministic tie-breaks, fresh-run evaluation, replay evaluation, and terminal selection are not yet implemented or verified.

Recent source-level QA closed the market-pressure producer gap: E19-B explicitly establishes the current `pred.market_pressure` cycle and E19-A clears that active cycle while preserving historical evidence. E274-A remains a later producer candidate and requires cycle/reachability reconciliation before catalog integration.

The transport-disruption producer gap is source-level closed: authoritative E32 explicitly establishes `pred.transport_disruption` for the compound-crisis cycle and records `history.transport_disruption_declared`. A lifecycle contract freezes `pred.transport_disruption` as the only canonical active identity; `transport_disruption_active` is a legacy expansion-document alias and must not enter production state. E136 remains an authored recovery/clear outcome and E277 remains a later recovery candidate outside the E01–E272 freeze. Lifecycle clear/expiry, save/load identity, delayed identity and replay isolation are still open.

## Active P0 work sequence

1. Close exact source/key reconciliation for `pred.guild_influence_strong`.
2. Freeze independent source domains and executable ordering for `pred.constitutional_prepared_strong`.
3. Reconcile coalition participant/outcome qualification and systemic evidence convergence.
4. Close `pred.final_charter_prerequisites` producer contract and E209 consumer chain.
5. Reconcile delayed consequence identity, timing, cancellation/supersession, save/load and replay isolation.
6. Freeze replay producer/key contracts for E186/E247/E248.
7. Resolve exact ending prerequisite/blocker sets and deterministic precedence.
8. Freeze remaining derived-predicate contracts and only then define the production schema/validator.

## Runtime gate

Decision Engine, persistence, scheduler, replay runtime, UI, art, localization, Android build and release gates remain unimplemented. Documentation progress does not count as runtime implementation.

## Rules

- Never mark a consumer as a producer merely because its trigger mentions the same concept.
- History markers are not current predicates unless the contract explicitly says so.
- Recovery/clear events do not retroactively establish the condition they resolve.
- Relationship scores do not qualify route identity without explicit authored milestones.
- Canonical delay source IDs must exist in the authoritative production catalog or an explicitly integrated expansion boundary.
- No runtime implementation begins until the canonical content contracts are sufficiently frozen.
