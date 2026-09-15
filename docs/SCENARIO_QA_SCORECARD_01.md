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
| S03 — Producer / Consumer Closure | 70% | OPEN — undefined consumer set remains; source-closed manifest producers now have a dedicated green verification gate |
| S04 — Predicate Contracts | 73% | ADVANCED — predicate parity, source closure and zero-cycle checks are green; undefined predicate lifecycle/runtime closure remains |
| S05 — Delayed Consequences | 60% | OPEN — complete consequence and cancellation closure remains |
| S06 — Replay / Meta State | 60% | OPEN — explicit replay producer/key and reset semantics remain |
| S07 — Event Graph / Causality | 83% | ADVANCED — canonical graph gate is green; full causal reachability remains |
| S08 — Source / Producer QA | 97% | ADVANCED — 29 declared source-closed producers pass authored-event/choice verification; stale/prose border rejection gate is green |
| S09 — Canonical Graph | 92% | ADVANCED — canonical graph, predicate parity and contract-readiness gates are green |
| S10 — Delayed Lifecycle | 83% | ADVANCED — delayed lifecycle gate is green; exact cancellation/supersession/save-load semantics remain |
| S11 — Replay / Ending QA | 72% | OPEN — deterministic ending precedence and replay reachability remain |
| S12 — Scope / Integrity Gates | 99% | ADVANCED — E01–E272 scope, scope boundary, contract readiness and integrity gates are green |

## Aggregate scenario score

**79% — scenario QA / verification progress.**

The exact arithmetic mean is **78.58%**, rounded to the nearest whole percent. This remains separate from runtime readiness and project completion.

## Verified autonomous work — latest block

### S24 — source-closed producer verification
- Added `tools/validate_source_closed_producers.py`.
- Added `Choice Kingdom Source-Closed Producer Verification` CI gate.
- Hardened authored A/B choice detection to match the canonical catalog's actual heading format.
- Final PR CI result: **PASS**.
- Verified: **272 events in scope, 29 declared source-closed producers, 0 errors**.

### S25 — noncanonical border rejection gate repair
- Repaired the rejection gate so stale/prose forms are preserved as audit evidence in the classification document rather than required to remain in canonical authored triggers.
- Corrected the canonical assertion to require `pred.border_crisis` as the executable trigger form.
- Final PR CI result: **PASS**.

### S23 — canonical border trigger normalization
- E271 canonical trigger: `pred.border_tension` + corroborated frontier-warning infrastructure.
- E272 canonical trigger: `pred.border_crisis` + `border_crisis_declared = true` + resolution route.
- Legacy/prose forms remain audit evidence, not executable canonical triggers.

### S22 — stale/prose border trigger classification
- `thread.border` frozen as stale alias.
- `thread.border_crisis = active` frozen as prose predicate expression.
- Canonical lifecycle remains `pred.border_crisis`.

### S21 — semantic writer collision closure
- E194-A reaffirmation of `history.guild_logistics_cooperation` was explicitly classified as idempotent reaffirmation of E136-B rather than an independent semantic writer.
- Fresh inventory previously verified `semantic_writer_collisions=0`.

### S20 — exhaustive E01–E272 source inventory
- 272/272 events verified.
- 243 unique output tokens.
- 90 trigger tokens.
- 3 duplicate output tokens.
- 2 same-event shared-writer findings.
- 59 undefined consumers.
- 8 undefined predicate consumers.
- 0 predicate cycles.

## Latest verified CI set

On the latest scenario QA PR head, the following gates completed **SUCCESS**:

- Choice Kingdom Source-Closed Producer Verification — run #9
- Choice Kingdom Noncanonical Consumer Rejection Gate — run #9
- Choice Kingdom Scenario Source Closure — run #32
- Choice Kingdom Canonical Graph — run #320
- Choice Kingdom Predicate Contract Parity — run #228
- Choice Kingdom Contract Readiness — run #251
- Choice Kingdom Delayed Lifecycle Gate — run #247
- Choice Kingdom Scope Boundary — run #278

These are source/structural gates. They do not claim runtime gameplay, fresh-run reachability, replay reachability or APK readiness.

## Remaining gates to 100%

1. Authoritative closure of the remaining undefined consumers.
2. Full choice/state transition closure across E01–E272.
3. Remaining predicate producer/lifecycle/clear/resolve contracts.
4. Delayed source identity, cancellation/supersession, persistence and exactly-once semantics.
5. Explicit replay producer/key bindings for E186/E247/E248.
6. Exact ending positive prerequisites, negative blockers and deterministic precedence.
7. Fresh-run and replay causal reachability verification.
8. Final graph/catalog semantic equality and production-contract freeze.

## Explicit exclusions

The scenario score does not claim a working Decision Engine, runtime persistence, Android implementation, UI, localization, APK or release readiness. Those are downstream gates.

## Frozen scope rule

E01–E272 are the production denominator. E273–E277 are expansion candidates and cannot silently contribute producers, consumers, predicates, delayed sources or reachability edges.

## Truth rule

A source document is evidence of QA work, not proof of runtime behavior. A block reaches 100% only after its authoritative source is checked and its required verification is actually green.
