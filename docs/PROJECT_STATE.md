# Choice Kingdom — Project State

Status: ACTIVE — canonical narrative/content QA before runtime implementation.

## Current position

The project is an original premium offline-first Android decision-and-consequence game set in Avelune. The authored first-campaign checkpoint is E01–E272; E273–E277 exists as a source patch/spec and is not yet part of the canonical production catalog freeze.

Recent source-level QA closed the market-pressure producer gap: E19-B explicitly establishes the current `pred.market_pressure` cycle and E19-A clears that active cycle while preserving historical evidence. E274-A remains a later producer candidate and requires cycle/reachability reconciliation before catalog integration.

A transport-disruption source audit was recorded separately. The current reviewed semantics do not yet justify a safe direct producer: E136/E277 are recovery/clear semantics and E192 is a consumer. No predicate may be inferred from generic military, border, toll, or resource pressure.

The delayed-consequence audit also found a source-ID scope mismatch: the inventory's older E31–E35 family must not be treated as canonical runtime references while the authoritative catalog boundary is E32. This has now been recorded as a P0 reconciliation rule; stale/draft event IDs must not enter engine, save-state, exactly-once, or replay identity.

Guild independent-source reconciliation is now documented provisionally: representation, tribunal, market/credit, and qualified logistics are separate candidate domains, with explicit anti-double-counting rules. This is not yet CLOSED because exact key matching and producer-before-consumer verification still remain.

## Active P0 work sequence

1. Establish a semantically correct upstream producer for `pred.transport_disruption`, or document a source-level correction only after re-reading the authoritative candidate events.
2. Close exact source/key reconciliation for `pred.guild_influence_strong`.
3. Freeze independent source domains for `pred.constitutional_prepared_strong`.
4. Reconcile coalition participant/outcome qualification and systemic evidence convergence.
5. Reconcile delayed consequence identity, timing, cancellation/supersession, save/load and replay isolation, including stale event-ID removal.
6. Freeze remaining derived-predicate contracts and only then define the production schema/validator.

## Runtime gate

Decision Engine, persistence, scheduler, replay runtime, UI, art, localization, Android build and release gates remain unimplemented. Documentation progress does not count as runtime implementation.

## Rules

- Never mark a consumer as a producer merely because its trigger mentions the same concept.
- History markers are not current predicates unless the contract explicitly says so.
- Recovery/clear events do not retroactively establish the condition they resolve.
- Relationship scores do not qualify route identity without explicit authored milestones.
- Canonical delay source IDs must exist in the authoritative production catalog or an explicitly integrated expansion boundary.
- No runtime implementation begins until the canonical content contracts are sufficiently frozen.
