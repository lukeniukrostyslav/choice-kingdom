# Choice Kingdom — Project State

Status: ACTIVE — canonical narrative/content QA before runtime implementation.

## Current position

The project is an original premium offline-first Android decision-and-consequence game set in Avelune. The authored first-campaign checkpoint is E01–E272; E273–E277 exists as a source patch/spec and is not part of the canonical production catalog freeze.

E33/E34 source recovery and canonical integration are CLOSED at source/graph level. E33 `emergency_decree_used` is canonically connected to E35, E34 `people_heard` is consumed by E50, and E33 `emergency_power` / `constitutional_limit` are explicit authored components for downstream requirements. These flags remain contract-gated and are not silently promoted into stronger runtime predicates.

The ending-precedence source boundary is corrected, but runtime ending order remains OPEN: exact positive/negative prerequisite sets, deterministic tie-breaks, fresh-run evaluation, replay evaluation and terminal selection are not yet implemented or verified.

The source-level derived-predicate contract is now frozen wherever an in-scope authored producer exists. This includes guild influence, systemic explanation, coalition cooperation, constitutional preparation and budget reform. The contract explicitly keeps `pred.food_stable`, `pred.guild_labor_tension` and `pred.information_pressure_high` OPEN/BLOCKED because no E01–E272 producer is source-closed.

Replay provenance was corrected conservatively: E131 is not promoted as an E186 producer/key binding. E186 remains partial source evidence; E247 and E248 remain open until an explicit persistent producer/key tuple is authored.

## Active P0 work sequence

1. Exhaustively enumerate concrete producers and consumers across the frozen E01–E272 authored catalog.
2. Resolve undefined producers/consumers, duplicate semantic writers and contradictory writers without inventing semantics.
3. Run machine token extraction and full predicate dependency-cycle validation.
4. Close remaining delayed source identity, lifecycle, cancellation/supersession, exactly-once and save/load contracts.
5. Freeze explicit replay producer/key contracts for E186/E247/E248.
6. Resolve exact ending prerequisite sets, negative blockers, deterministic tie-break order, fresh-run order and replay order.
7. Run fresh-run and replay causal reachability plus graph/catalog parity.
8. Freeze the production contracts and machine validators only after all remaining evidence is clean.

## Scenario QA score

See `docs/SCENARIO_QA_SCORECARD_01.md` for the reproducible block scorecard. Current aggregate scenario QA is **75%**, calculated as the arithmetic mean of twelve scenario blocks. This is not runtime readiness.

## Runtime gate

Decision Engine, persistence, scheduler, replay runtime, UI, art, localization, Android build and release gates remain unimplemented. Documentation progress does not count as runtime implementation.

## Rules

- Never mark a consumer as a producer merely because its trigger mentions the same concept.
- History markers are not current predicates unless the contract explicitly says so.
- Recovery/clear events do not retroactively establish the condition they resolve.
- Relationship scores do not qualify route identity without explicit authored milestones.
- Canonical delay source IDs must exist in the authoritative production catalog or an explicitly integrated expansion boundary.
- No runtime implementation begins until the canonical content contracts are sufficiently frozen.
- E273–E277 cannot contribute production semantics while the frozen scope is E01–E272.
