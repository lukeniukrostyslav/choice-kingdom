# Choice Kingdom — Canonical P0 Reconciliation 04

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA PASS — NOT RUNTIME IMPLEMENTATION**

## Purpose

This pass converts the remaining high-priority producer/consumer ambiguities into explicit source-level decisions without inventing runtime state.

## 1. Border crisis lifecycle — CLOSED

Canonical lifecycle:

1. `E271-A` declares the crisis.
2. `pred.border_crisis` is active only after that declaration.
3. `E272-A/B` resolve the active crisis.
4. `border_crisis_declared` remains historical after resolution.
5. `border_crisis_resolved` is the lifecycle marker used to invalidate the active predicate.

`thread.border` is therefore **not** a canonical runtime alias for `thread.border_crisis`. E271 is the upstream reconciliation point and must require the authored frontier-warning context before declaration.

## 2. Food stability — PRODUCER NOW EXPLICIT, REACHABILITY OPEN

`E273-A` is an authored source candidate for `pred.food_stable` and records `history.food_stability_established`.

Decision: treat this as a **candidate producer outside the frozen E01–E272 production scope** until the event is explicitly admitted into the canonical catalog and has a valid upstream trigger and downstream consumer set.

No engine contract may silently include E273 merely because the source exists.

## 3. Market pressure — PRODUCER NOW EXPLICIT, REACHABILITY OPEN

`E274-A` explicitly establishes `pred.market_pressure` and `history.market_pressure_declared`.

Decision: same boundary rule as E273. The producer is source-verified, but production inclusion remains blocked until catalog-scope reconciliation is complete.

## 4. Guild labor tension — PRODUCER NOW EXPLICIT, REACHABILITY OPEN

`E275-B` explicitly establishes `pred.guild_labor_tension`; `E275-A` clears the active condition and records reform history.

This is a valid lifecycle shape: declaration → active state → authored repair. It must not be replaced by an inferred relationship score.

## 5. Information pressure — PRODUCER NOW EXPLICIT, REACHABILITY OPEN

`E276-B` explicitly establishes `pred.information_pressure_high`; `E276-A` clears it and records reform history.

`rel.toma` alone is explicitly insufficient to manufacture the predicate.

## 6. Transport disruption — CANONICAL SOURCE CLOSED

The existing source contract remains:

- E32 establishes the active disruption cycle.
- E136-A/B provide authored recovery/clear semantics.
- E277 is a later authored recovery candidate and must not create a second competing canonical producer until the catalog scope is reconciled.

Decision: **do not add E277 to the frozen producer registry yet**. First determine whether E277 is an expansion of E136's recovery semantics or a distinct later transport cycle.

## 7. Systemic explanation — still OPEN

`pred.systemic_explanation_verified` requires distinct evidence identities and an explicit convergence rule. Relationship strength, route count, or reaching E270 are not sufficient.

Minimum production contract still required:

- unique evidence IDs;
- source event for each evidence item;
- no duplicate evidence identity counted twice;
- minimum cardinality/convergence rule;
- explicit invalidation rule for contradicted evidence;
- deterministic evaluation.

## 8. Coalition cooperation — still OPEN

`history.cross_faction_package` is an authored input, but it does not automatically prove `pred.coalition_cooperation`.

The canonical predicate needs explicit participant identity, positive cooperation outcome and absence of a collapse blocker. `four_way_bargain` remains a narrative label, not an implicit machine predicate.

## 9. Constitutional preparedness — still OPEN

`pred.constitutional_prepared_strong` must be built from independent institutional domains. A single broad route label or relationship score cannot satisfy multiple prerequisites.

## 10. Budget reform — source set identified, formula still OPEN

Candidate institutional inputs remain:

- E142-A: auditor independence;
- E154-A: audited Crown;
- E198-A: legislative budget lock.

The final contract still needs ordering, independence rules and negative blockers before engine implementation.

## 11. Final charter prerequisites — OPEN / ACYCLICITY REQUIRED

E209 is a consumer. It must not create the prerequisites that it consumes. Every prerequisite must have an upstream authored producer and a deterministic source identity.

## 12. Delayed consequences — extraction gate

The catalog contains many delayed narrative statements, but prose is not yet production data. Each executable delay requires source event/choice, timing, resolution target, exactly-once identity and cancellation/supersession semantics.

## Gate result

**Canonical source continuity:** CLOSED  
**Explicit producer coverage:** IMPROVED / PARTIAL  
**Scope admission for E273–E277:** NOT YET CLOSED  
**Reachability:** NOT VERIFIED  
**Production schema:** BLOCKED  
**Runtime engine:** NOT STARTED BY DESIGN

No runtime readiness is claimed by this document.