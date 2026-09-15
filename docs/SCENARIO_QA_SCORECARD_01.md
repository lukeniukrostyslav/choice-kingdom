# Choice Kingdom — Scenario QA Scorecard 01

Date: 2026-09-15  
Frozen authored scope: **E01–E272**  
Status: **SCENARIO QA REPORTING CONTRACT — SOURCE LEVEL**

## Purpose

This scorecard measures only verified scenario QA closure. Percentages are not increased for plans, documentation volume, commits, or unexecuted runtime assumptions.

## Current 12-block scorecard

| Scenario block | Completion | Current gate |
|---|---:|---|
| S01 — Canonical Event Coverage | 84% | ADVANCED — E01–E272 exhaustive authored-event scope is structurally validated; semantic/reachability closure remains |
| S02 — Choice / State Transitions | 70% | OPEN — complete authored transition/effect closure remains |
| S03 — Producer / Consumer Closure | 100% | SOURCE-CLOSED — exhaustive inventory reports zero undefined consumers after frozen source contracts and canonical trigger normalization |
| S04 — Predicate Contracts | 90% | ADVANCED — all currently consumable composite predicates have frozen source contracts; blocked production predicates without in-scope producers remain OPEN/BLOCKED; runtime lifecycle remains open |
| S05 — Delayed Consequences | 60% | OPEN — complete consequence and cancellation closure remains |
| S06 — Replay / Meta State | 60% | OPEN — explicit replay producer/key and reset semantics remain |
| S07 — Event Graph / Causality | 83% | ADVANCED — canonical graph gate is green; full causal reachability remains |
| S08 — Source / Producer QA | 99% | ADVANCED — 307 producer contracts, zero semantic writer collisions and exhaustive authored-source inventory pass; final semantic equality remains |
| S09 — Canonical Graph | 95% | ADVANCED — canonical graph, predicate parity, contract-readiness and source inventory gates are green |
| S10 — Delayed Lifecycle | 83% | ADVANCED — delayed lifecycle gate is green; exact cancellation/supersession/save-load semantics remain |
| S11 — Replay / Ending QA | 72% | OPEN — deterministic ending precedence and replay reachability remain |
| S12 — Scope / Integrity Gates | 100% | CLOSED — E01–E272 scope, exclusions, contract readiness, source inventory and integrity gates are green |

## Aggregate scenario score

**83% — scenario QA / verification progress.**

The exact arithmetic mean is **83.00%**. This remains separate from runtime readiness and project completion.

## Verified autonomous work — latest blocks

### S29 — exhaustive producer/consumer closure
- Frozen canonical trigger normalization and source-backed derived producer contracts.
- Added explicit composite-predicate source contracts for coalition cooperation, constitutional preparation, guild influence and systemic explanation.
- Exhaustive CI inventory: **272/272 events**, **307 producer contracts**, **0 undefined consumers**, **0 undefined predicate consumers**, **0 predicate cycles**, **0 semantic writer collisions**, **2 same-event shared-writer cases**, **1 explicit idempotent reaffirmation family**.
- `undefined-consumer-source-inspection` confirms **0 unresolved consumers**.

### S28 — derived predicate closure
- `tools/compile_scenario_source_inventory.py` now consumes frozen source-closed and derived source contracts.
- Canonical trigger normalization is machine-enforced for stale/prose forms.
- `pred.final_charter_prerequisites` is frozen as a deterministic source-level gate consumed by E209; it does not claim runtime execution.

### S27 — exhaustive unresolved-consumer source inspection
- Added `tools/inspect_undefined_consumer_sources.py`.
- CI emits an authoritative occurrence map for every remaining undefined consumer; latest result is zero.

### S26 — frozen source-closed producer integration
- Seeded the machine inventory from `MACHINE_CANONICAL_GRAPH_01.json` source-closed producer contracts rather than relying only on markdown choice-line extraction.
- Added verified non-token producer contracts from the canonical source.

### S25 — noncanonical border rejection gate repair
- Stale/prose forms remain audit evidence but are no longer canonical executable producers.
- Canonical executable border form remains `pred.border_crisis`.

### S23 — canonical border trigger normalization
- E271 canonical trigger: `pred.border_tension` + corroborated frontier-warning infrastructure.
- E272 canonical trigger: `pred.border_crisis` + `border_crisis_declared` + resolution route.

### S21 — semantic writer collision closure
- E194-A is frozen as idempotent reaffirmation of E136-B for `history.guild_logistics_cooperation`.

## Latest verified CI set — PR #5

All relevant scenario gates completed successfully on the merged scenario-QA change set:

- Choice Kingdom Scenario Source Inventory — run #43
- Choice Kingdom Scenario Source Inventory V3 — run #3
- Choice Kingdom Source-Closed Producer Verification — run #29
- Choice Kingdom Noncanonical Consumer Rejection Gate — run #32
- Scenario Source Closure — run #57
- Choice Kingdom Canonical Graph — run #368
- Choice Kingdom Predicate Contract Parity — run #276
- Choice Kingdom Contract Readiness — run #299
- Choice Kingdom Delayed Lifecycle Gate — run #295
- Choice Kingdom Scope Boundary — run #326

The source-inventory run explicitly passed **272/272 events, 0 undefined consumers, 0 undefined predicate consumers, 0 predicate cycles and 0 semantic writer collisions**.

These are source/structural gates. They do not claim runtime gameplay, fresh-run reachability, replay reachability or APK readiness.

## Remaining gates to 100%

1. Complete authored choice/effect transition closure.
2. Close the three production predicates currently blocked by lack of an in-scope authored producer: `pred.food_stable`, `pred.guild_labor_tension`, `pred.information_pressure_high` — without admitting E273–E277.
3. Complete delayed consequence source identity, cancellation/supersession, persistence and exactly-once semantics.
4. Freeze explicit replay producer/key bindings for E186/E247/E248.
5. Complete exact ending positive prerequisites, negative blockers and deterministic precedence.
6. Prove fresh-run and replay causal reachability.
7. Prove final graph/catalog semantic equality and production-contract freeze.

## Explicit exclusions

The scenario score does not claim a working Decision Engine, runtime persistence, Android implementation, UI, localization, APK or release readiness. Those are downstream gates.

## Frozen scope rule

E01–E272 are the production denominator. E273–E277 are expansion candidates and cannot silently contribute producers, consumers, predicates, delayed sources or reachability edges.

## Truth rule

A source document is evidence of QA work, not proof of runtime behavior. A block reaches 100% only after its authoritative source is checked and its required verification is actually green.
