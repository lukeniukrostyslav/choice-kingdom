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
| S03 — Producer / Consumer Closure | 80% | ADVANCED — fresh inventory now has 14 unresolved consumers after explicit source-closed producer and derived-contract closure |
| S04 — Predicate Contracts | 80% | ADVANCED — 5 SOURCE-CLOSED composite predicates are represented as derived contracts; only 2 direct predicate consumers remain unresolved |
| S05 — Delayed Consequences | 60% | OPEN — complete consequence and cancellation closure remains |
| S06 — Replay / Meta State | 60% | OPEN — explicit replay producer/key and reset semantics remain |
| S07 — Event Graph / Causality | 83% | ADVANCED — canonical graph gate is green; full causal reachability remains |
| S08 — Source / Producer QA | 98% | ADVANCED — frozen source-closed producer contracts pass authored-source verification; semantic writer collisions remain at zero |
| S09 — Canonical Graph | 93% | ADVANCED — canonical graph, predicate parity and contract-readiness gates are green |
| S10 — Delayed Lifecycle | 83% | ADVANCED — delayed lifecycle gate is green; exact cancellation/supersession/save-load semantics remain |
| S11 — Replay / Ending QA | 72% | OPEN — deterministic ending precedence and replay reachability remain |
| S12 — Scope / Integrity Gates | 99% | ADVANCED — E01–E272 scope, scope boundary, contract readiness and integrity gates are green |

## Aggregate scenario score

**80% — scenario QA / verification progress.**

The exact arithmetic mean is **80.17%**, rounded to the nearest whole percent. This remains separate from runtime readiness and project completion.

## Verified autonomous work — latest blocks

### S28 — derived predicate closure
- Updated `tools/compile_scenario_source_inventory.py` so explicitly `SOURCE-CLOSED` multi-domain predicates are treated as derived contracts rather than false undefined direct producers.
- Latest PR inventory: **272/272 events**, **290 producer contracts**, **14 unresolved consumers**, **2 unresolved direct predicate consumers**, **0 predicate cycles**, **0 semantic writer collisions**.
- Final CI gates on the PR: PASS.

### S27 — exhaustive unresolved-consumer source inspection
- Added `tools/inspect_undefined_consumer_sources.py`.
- CI emits an authoritative occurrence map for every remaining undefined consumer.

### S26 — frozen source-closed producer integration
- Seeded the machine inventory from `MACHINE_CANONICAL_GRAPH_01.json` source-closed producer contracts rather than relying only on markdown choice-line extraction.
- Added verified non-token producer contracts from the canonical source: `history.house_assembly`, `people_charter_endorsed`, `guild_political_representation`.
- Inventory moved from 59 → 43 → 20 → 16 → 14 unresolved consumers through verified closures; no invented producers were used.

### S25 — noncanonical border rejection gate repair
- Repaired the rejection gate so stale/prose forms are preserved as audit evidence rather than required to remain in canonical authored triggers.
- Canonical executable border form remains `pred.border_crisis`.

### S24 — source-closed producer verification
- Added `tools/validate_source_closed_producers.py` and its CI gate.
- Final PR CI result: **PASS**.

### S23 — canonical border trigger normalization
- E271 canonical trigger: `pred.border_tension` + corroborated frontier-warning infrastructure.
- E272 canonical trigger: `pred.border_crisis` + `border_crisis_declared = true` + resolution route.

### S21 — semantic writer collision closure
- E194-A is frozen as idempotent reaffirmation of E136-B for `history.guild_logistics_cooperation`.
- Fresh inventories continue to report `semantic_writer_collisions=0`.

## Latest verified CI set

Latest scenario QA PR #4 completed the relevant scenario gates successfully:

- Choice Kingdom Scenario Source Inventory — run #33
- Choice Kingdom Canonical Graph — run #347
- Choice Kingdom Predicate Contract Parity — run #255
- Choice Kingdom Contract Readiness — run #278
- Choice Kingdom Delayed Lifecycle Gate — run #274
- Choice Kingdom Scope Boundary — run #305

Previous integrated scenario gates also remain green on main.

These are source/structural gates. They do not claim runtime gameplay, fresh-run reachability, replay reachability or APK readiness.

## Remaining gates to 100%

1. Close the remaining 14 consumer forms without inventing aliases or producers.
2. Close the remaining 2 direct predicate lifecycle contracts: `pred.border_tension` and `pred.final_charter_prerequisites`.
3. Resolve border resolution-route producer identities: `border_commander_report`, `joint_border_survey`, `negotiated_withdrawal`.
4. Resolve the shared/delayed evidence route `ledger_fragment_a` without creating a false semantic writer collision.
5. Resolve `schoolhouse_vote`, `temporary_noble_exemption`, remaining thread-family lifecycle contracts and `warehouse_arson` from authoritative sources.
6. Close delayed source identity, cancellation/supersession, persistence and exactly-once semantics.
7. Explicit replay producer/key bindings for E186/E247/E248.
8. Exact ending positive prerequisites, negative blockers and deterministic precedence.
9. Fresh-run and replay causal reachability verification.
10. Final graph/catalog semantic equality and production-contract freeze.

## Explicit exclusions

The scenario score does not claim a working Decision Engine, runtime persistence, Android implementation, UI, localization, APK or release readiness. Those are downstream gates.

## Frozen scope rule

E01–E272 are the production denominator. E273–E277 are expansion candidates and cannot silently contribute producers, consumers, predicates, delayed sources or reachability edges.

## Truth rule

A source document is evidence of QA work, not proof of runtime behavior. A block reaches 100% only after its authoritative source is checked and its required verification is actually green.
