# Choice Kingdom — Canonical Contract Closure Pass 01

Date: 2026-09-16  
Status: **SOURCE-LEVEL QA — CONTRACT CLOSURE WORKING RECORD**  
Frozen production scope: **E01–E272**

## Purpose

This pass consolidates the current canonical closure audit into an actionable contract table. It does not create runtime state, thresholds, or hidden fallback behavior. A contract is marked CLOSED only where the authoritative authored source already establishes an unambiguous producer and semantic identity.

E273–E277 are retained only as **expansion candidates** and are not part of the frozen production denominator. Candidate observations from those nodes must never silently become E01–E272 production contracts.

## Closure table

| Contract | Current state | Canonical decision / blocker |
|---|---|---|
| `history.guild_representation` | CLOSED | E144 is authoritative producer; E49 is the earlier exact representation source. E49/E144 are one representation domain, not two independent domains. |
| `history.guild_logistics_cooperation` | CLOSED | E136-B is the upstream immutable producer; E194 consumes it and adds later neutral-inspection qualification. |
| `pred.border_crisis` | CLOSED at source lifecycle | E271 declares; E272 resolves; active predicate is derived from declaration minus resolution. Security alone cannot create it. |
| `pred.guild_logistics_cooperation` | CLOSED at source chain | Requires E136-B history plus E194-A neutral-inspection qualification and no immunity-risk blocker. |
| `pred.food_stable` | CLOSED at source level | E192-B is the frozen-scope authored producer for `food_logistics_stabilized`; E192-A explicitly clears that active marker and establishes the unstable-cycle marker. Runtime cycle expiry/invalidation remains open. |
| `pred.transport_disruption` | PARTIAL | E32 is an explicit active producer in the frozen scope; E136 recovery/clear semantics are source-closed, but full lifecycle persistence/reconciliation remains open. |
| `pred.winter_severe` | PARTIAL | E29-A/E29-B are explicit severe-winter producers; immutable history is retained. Deterministic active-cycle validity/expiry remains open. |
| `pred.market_pressure` | PARTIAL | E19 provides the frozen-scope explicit producer. Later expansion producers remain outside the frozen catalog. Clear/invalidation and cross-cycle ordering remain open. |
| `pred.guild_labor_tension` | OPEN in frozen scope | Expansion-candidate producer material exists outside E01–E272; it is not admitted to the frozen contract. A frozen-scope producer/consumer contract must be identified or the consumer must remain blocked. |
| `pred.information_pressure_high` | OPEN in frozen scope | Expansion-candidate producer material exists outside E01–E272; it is not admitted to the frozen contract. Exact frozen-scope evidence and cardinality remain to be closed. |
| `pred.guild_influence_strong` | PARTIAL | Independent domains are frozen: representation, tribunal, commercial/market, qualified logistics. E49/E144 cannot double-count. Exact producer-before-consumer machine-checkable compilation remains open. |
| `pred.systemic_explanation_verified` | SOURCE-CLOSED | E270-A is the frozen-scope explicit convergence producer for `systemic_explanation_convergence`, conditioned on the required distinct warehouse/financial, document/language and witness/organizational evidence families. Runtime aggregation, persistence, contradiction handling and reachability remain open. |
| `pred.coalition_cooperation` | PARTIAL | E148-A is the authoritative cooperation-package source with named participation. Any later expansion evidence remains outside the frozen catalog. Machine-readable membership, positive-outcome compilation and collapse/invalidation semantics remain open. |
| `pred.constitutional_prepared_strong` | PARTIAL | Frozen domains: civic=`people_charter_endorsed`; institutional=`crown_audited`/`full_crown_audit_published`; factional=`house_assembly`; military=`military_red_line`. At least three independent domains are required; full ordering/anti-double-counting remains open. |
| `pred.budget_reform` | PARTIAL | Source contract is now machine-frozen: E142-A audit independence + E154-A Crown audit + E198-A legislative budget lock. E155 is downstream only; negative branches are explicit. Ordering, reachability, save/replay preservation and contradiction/cycle checks remain open. |
| `thread.military_constitutional` | STRONG | E199-A provides explicit constitutional army-oath evidence; final machine-readable activation compilation remains open. |
| `thread.coalition` | STRONG | E148-A provides authored cross-faction package and participation evidence; exact immutable membership/package representation remains open. |
| `thread.amara_civic` | PARTIAL | Multiple authored Amara choices exist; one explicit route activation contract remains necessary. |
| `thread.toma_information` | PARTIAL | Multiple authored Toma/information choices exist; explicit activation contract remains necessary. |
| `thread.final_constitutional_phase` | OPEN | Must activate deterministically before E208 without using late consumers as producers. |
| `pred.final_charter_prerequisites` | OPEN | Exact prerequisite set and mandatory-crisis blockers must be frozen before E209. |
| Delayed consequence identity | OPEN | Every prose delay needs source choice, exact identity, timing window/condition, cancellation/supersession and exactly-once semantics. |
| Replay metadata | SOURCE-BOUNDARY CLOSED | E186/E247/E248 have explicit `completed_prior_run_meta_export` boundaries and canonical `meta.replay.*` keys; runtime import/reset/reachability remains open. |
| Ending qualification | OPEN | E61–E67 are distinct ending resolvers; independent prerequisites and precedence still require explicit contract. |
| Route identity | CLOSED as semantic rule | Relationship values cannot substitute for explicit historical/flag/thread route identity. Exact machine-readable route producer inventory remains part of schema compilation. |
| Evidence convergence | SOURCE-CLOSED | E270-A is the authored convergence decision; it requires the three distinct evidence families before establishing `systemic_explanation_convergence`. Executable evidence aggregation and reachability remain open. |

## Hard invariants carried forward

1. Five numeric resources only: gold, trust, security, power, reputation.
2. Contextual pressures such as food, winter, border, guild influence and information pressure are derived predicates or durable state, never silent sixth resources.
3. Historical decisions are immutable; current-state predicates cannot be satisfied merely by historical wording unless the contract explicitly says so.
4. Relationship values cannot substitute for route identity or institutional evidence.
5. Consumer events cannot manufacture their own prerequisites.
6. Endgame consumers cannot retroactively manufacture preparation predicates.
7. Replay metadata cannot satisfy current-run state unless the authored contract explicitly makes it a cross-run discovery mechanic.
8. Delayed consequences must survive save/load and resolve exactly once.
9. Coalition cooperation is distinct from route count and requires explicit authored cooperation evidence.
10. Evidence convergence requires distinct evidence families and an explicit convergence decision.

## Current P0 closure blockers

The production schema remains blocked until these are resolved and reconciled against the frozen E01–E272 authored source set:

- transport disruption lifecycle/recovery reconciliation;
- winter active-cycle validity/expiry;
- market pressure clear/invalidation semantics;
- guild labor tension frozen-scope producer/consumer closure;
- information pressure frozen-scope evidence/cardinality closure;
- exact guild influence machine-readable domain compilation;
- systemic explanation executable evidence aggregation, contradiction handling and reachability;
- coalition machine-readable membership, positive outcome and collapse/invalidation semantics;
- constitutional preparation producer ordering and anti-double-counting;
- budget reform producer-before-consumer ordering, reachability, preservation and contradiction/cycle checks;
- final charter prerequisite closure;
- delayed consequence source identity/timing/cancellation/exactly-once extraction;
- replay runtime import/reset/reachability verification;
- ending qualification and precedence.

## Gate result

**Canonical contract closure: IN PROGRESS.**

**Production schema: BLOCKED.**

**Validator: intentionally not implemented yet.**

**Decision Engine/runtime: intentionally not implemented yet.**

The next pass is to convert the remaining PARTIAL/OPEN contracts into exact producer/consumer inventories from the authoritative frozen E01–E272 event catalog, then perform contradiction/cycle/reachability checks before schema freeze.
