# Choice Kingdom — Canonical Derived Predicate Contract 01

Status: **SOURCE-LEVEL CONTRACT — NOT ENGINE IMPLEMENTATION**
Scope: E01–E277

## Purpose

Freeze the semantic rule for contextual conditions before production schema work. These conditions are not sixth resources and may not be inferred from relationship scores, consumer reachability, or prose alone.

## Contract matrix

| Predicate | Canonical source inputs | Current status |
|---|---|---|
| `pred.border_crisis` | `border_crisis_declared = true` AND `border_crisis_resolved != true`; lifecycle declaration E271-A, resolution E272-A/B | CLOSED |
| `pred.guild_logistics_cooperation` | `history.guild_logistics_cooperation` AND E194-A neutral-inspection outcome AND no unresolved immunity-risk blocker | CLOSED |
| `pred.food_stable` | E273-A `food_stability_standard`; explicit later food-disruption invalidation required | CLOSED — source producer verified; invalidation still needs authored source |
| `pred.transport_disruption` | Explicit disruption producer + not subsequently cleared by transport recovery | OPEN — active disruption producer still missing; E136/E277 are recovery/clear sources |
| `pred.winter_severe` | E29-A/B explicitly establish severe winter for current winter cycle; history retained; explicit cycle expiry/recovery required | CLOSED — source producer verified |
| `pred.market_pressure` | E274-A `market_pressure_declared`; explicit later stabilization/clear rule required | CLOSED — source producer verified; clear source still needs authored reconciliation |
| `pred.guild_labor_tension` | E275-B `guild_labor_tension_declared`; E275-A can clear active tension; exact persistence semantics to be validated | CLOSED — source producer verified |
| `pred.information_pressure_high` | E276-B `information_pressure_declared`; E276-A can clear active pressure; not `rel.toma` alone | CLOSED — source producer verified |
| `pred.guild_influence_strong` | At least two distinct institutional domains from canonical guild-influence domain set | PARTIAL |
| `pred.systemic_explanation_verified` | Distinct warehouse/financial evidence + document/language evidence + witness/organizational evidence + explicit convergence decision | PARTIAL |
| `pred.coalition_cooperation` | Explicit cooperation package with identified participants and positive cooperation outcome; not route-count based | PARTIAL |
| `pred.constitutional_prepared_strong` | Three independent preparation domains: civic/commons, audit/institutional, factional/constitutional or military | OPEN |
| `pred.budget_reform` | Independent audit legitimacy + crown-audit legitimacy + legislative budget lock; exact source set still to freeze | OPEN |
| `pred.final_charter_prerequisites` | Convergence of already-established civic, institutional, faction/house/guild, military/security, information/evidence, coalition and crisis-resolution facts, with mandatory blockers cleared | OPEN |

## Hard derivation rules

1. A consumer event cannot create the predicate it consumes.
2. A relationship score cannot qualify a route or contextual predicate unless the authored contract explicitly defines that numeric gate.
3. Historical evidence does not automatically imply current stability; current predicates require current validity rules.
4. Resolution must invalidate an active predicate without erasing immutable historical evidence.
5. Evidence cardinality must be evaluated by independent source identity, not by counting flags from one chain.
6. Coalition qualification requires explicit cooperation semantics, not four-way/five-way route cardinality.
7. Derived predicates must have deterministic inputs and deterministic invalidation/clear behavior before they enter production schema.
8. A newly authored producer outside the original E01–E272 scope cannot be treated as reachable merely because its trigger text names an existing state. Reachability and insertion point must be proven before the expanded catalog is frozen.

## Current source-level producer closures

- `pred.food_stable`: E273-A is an explicit producer. The active state is intentionally not considered fully lifecycle-closed until a canonical later disruption/expiry source is reconciled.
- `pred.market_pressure`: E274-A is an explicit producer. A later stabilization/clear source is still required for a complete lifecycle.
- `pred.guild_labor_tension`: E275-B is an explicit producer and E275-A is an explicit clear outcome.
- `pred.information_pressure_high`: E276-B is an explicit producer and E276-A is an explicit clear outcome.
- `pred.transport_disruption`: no active producer has been accepted yet; E277-A/B only define recovery/clear semantics and therefore cannot close this gap.

## Producer expansion gate

E273–E277 are authored source candidates outside the original E01–E272 freeze. Before treating them as production content:

1. insert them into a deterministic campaign position or define an explicit post-E272 continuation boundary;
2. verify every trigger has an upstream producer/reachable path;
3. verify no event consumes a predicate before its first possible producer;
4. verify delayed callbacks and save/load identity include the new events;
5. rerun event-ID uniqueness, trigger normalization, contradiction, cycle and reachability audits;
6. only then expand the canonical scope beyond E272.

## Gate

Production schema and runtime remain blocked until the expanded catalog is reconciled and all remaining producer/consumer contracts are explicitly mapped.
