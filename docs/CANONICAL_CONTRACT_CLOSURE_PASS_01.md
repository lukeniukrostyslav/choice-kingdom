# Choice Kingdom — Canonical Contract Closure Pass 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — CONTRACT CLOSURE WORKING RECORD**
Scope: **E01–E277**

## Purpose

This pass consolidates the current canonical closure audit into an actionable contract table. It does not create runtime state, thresholds, or hidden fallback behavior. A contract is marked CLOSED only where the authoritative authored source already establishes an unambiguous producer and semantic identity.

## Closure table

| Contract | Current state | Canonical decision / blocker |
|---|---|---|
| `history.guild_representation` | CLOSED | E144 is authoritative producer; E49 is the earlier exact representation source. E49/E144 are one representation domain, not two independent domains. |
| `history.guild_logistics_cooperation` | CLOSED | E136-B is the upstream immutable producer; E194 consumes it and adds later neutral-inspection qualification. |
| `pred.border_crisis` | CLOSED at source lifecycle | E271 declares; E272 resolves; active predicate is derived from declaration minus resolution. Security alone cannot create it. |
| `pred.guild_logistics_cooperation` | CLOSED at source chain | Requires E136-B history plus E194-A neutral-inspection qualification and no immunity-risk blocker. |
| `pred.food_stable` | PARTIAL | E273-A is an explicit current-cycle producer candidate. Active-cycle invalidation/expiry and full consumer ordering remain open. |
| `pred.transport_disruption` | PARTIAL | E32 is now an explicit active producer; E136/E277 provide recovery/clear semantics. Full lifecycle persistence/reconciliation remains open. |
| `pred.winter_severe` | PARTIAL | E29-A/E29-B are explicit severe-winter producers; immutable history is retained. Deterministic active-cycle validity/expiry remains open. |
| `pred.market_pressure` | PARTIAL | E19 provides an early explicit producer and E274 a later producer; clear/invalidation and cross-cycle ordering remain open. |
| `pred.guild_labor_tension` | PARTIAL | E275-B provides an explicit active producer and E275-A a clear path; persistence/order against earlier guild events remains open. |
| `pred.information_pressure_high` | PARTIAL | E276-B provides an explicit active producer and E276-A a clear path; exact cardinality and upstream evidence ordering remain open. |
| `pred.guild_influence_strong` | PARTIAL | Independent domains are frozen: representation, tribunal, commercial/market, qualified logistics. E49/E144 cannot double-count. Exact producer-before-consumer machine-checkable compilation remains open. |
| `pred.systemic_explanation_verified` | PARTIAL | Requires distinct warehouse/financial, document/language, and witness/organizational evidence IDs plus explicit convergence choice; exact authored source IDs remain to be compiled. |
| `pred.coalition_cooperation` | PARTIAL | E148-A is the authoritative cooperation-package source with named participation; E261-A supplies later explicit cooperation evidence. Machine-readable membership, positive-outcome compilation and collapse/invalidation semantics remain open. |
| `pred.constitutional_prepared_strong` | PARTIAL | Frozen domains: civic=`people_charter_endorsed`; institutional=`crown_audited`/`full_crown_audit_published`; factional=`house_assembly`; military=`military_red_line`. At least three independent domains are required; full ordering/anti-double-counting remains open. |
| `pred.budget_reform` | OPEN | Audit independence, crown audit and legislative budget lock must remain distinct; exact authored qualifying combination is not frozen. |
| `thread.military_constitutional` | STRONG | E199-A provides explicit constitutional army-oath evidence; final machine-readable activation compilation remains open. |
| `thread.coalition` | STRONG | E148-A provides authored cross-faction package and participation evidence; exact immutable membership/package representation remains open. |
| `thread.amara_civic` | PARTIAL | Multiple authored Amara choices exist; one explicit route activation contract remains necessary. |
| `thread.toma_information` | PARTIAL | Multiple authored Toma/information choices exist; explicit activation contract remains necessary. |
| `thread.final_constitutional_phase` | OPEN | Must activate deterministically before E208 without using late consumers as producers. |
| `pred.final_charter_prerequisites` | OPEN | Exact prerequisite set and mandatory-crisis blockers must be frozen before E209. |
| Delayed consequence identity | OPEN | Every prose delay needs source choice, exact identity, timing window/condition, cancellation/supersession and exactly-once semantics. |
| Replay metadata | OPEN | Only `meta.*` facts intentionally persistent across runs may qualify future replay behavior. |
| Ending qualification | OPEN | E61–E67 are distinct ending resolvers; independent prerequisites and precedence still require explicit contract. |
| Route identity | CLOSED as semantic rule | Relationship values cannot substitute for explicit historical/flag/thread route identity. Exact machine-readable route producer inventory remains part of schema compilation. |
| Evidence convergence | PARTIAL | Required evidence families are fixed conceptually; exact source IDs and convergence-choice representation still require compilation. |

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

The production schema remains blocked until these are resolved and reconciled against the expanded authored source set:

- food stability invalidation/expiry and ordering;
- transport disruption lifecycle/recovery reconciliation;
- winter active-cycle validity/expiry;
- market pressure clear/invalidation semantics;
- guild labor tension ordering/persistence;
- information pressure cardinality/evidence ordering;
- exact guild influence machine-readable domain compilation;
- independent evidence source IDs and systemic convergence;
- coalition machine-readable membership, positive outcome and collapse/invalidation semantics;
- constitutional preparation producer ordering and anti-double-counting;
- budget reform qualifying combination;
- final charter prerequisite closure;
- delayed consequence source identity/timing/cancellation/exactly-once extraction;
- replay meta-state contract;
- ending qualification and precedence.

## Gate result

**Canonical contract closure: IN PROGRESS.**

**Production schema: BLOCKED.**

**Validator: intentionally not implemented yet.**

**Decision Engine/runtime: intentionally not implemented yet.**

The next pass is to convert the remaining PARTIAL/OPEN contracts into exact producer/consumer inventories from the authoritative event catalog, then perform contradiction/cycle/reachability checks before schema freeze.
