# Choice Kingdom — Canonical Derived Predicate Contract 01

Status: **SOURCE-LEVEL CONTRACT — NOT ENGINE IMPLEMENTATION**
Scope: E01–E272

## Purpose

Freeze the semantic rule for contextual conditions before production schema work. These conditions are not sixth resources and may not be inferred from relationship scores, consumer reachability, or prose alone.

## Contract matrix

| Predicate | Canonical source inputs | Current status |
|---|---|---|
| `pred.border_crisis` | `border_crisis_declared = true` AND `border_crisis_resolved != true`; lifecycle declaration E271-A, resolution E272-A/B | CLOSED |
| `pred.guild_logistics_cooperation` | `history.guild_logistics_cooperation` AND E194-A neutral-inspection outcome AND no unresolved immunity-risk blocker | CLOSED |
| `pred.food_stable` | Explicit food-stability producer + explicit invalidation/expiry semantics | OPEN — producer still missing |
| `pred.transport_disruption` | Explicit disruption producer + not subsequently cleared by transport recovery | OPEN — active disruption producer still missing; E136-A/B are recovery/clear only |
| `pred.winter_severe` | E29-A/B explicitly establish the severe winter state for the current winter cycle; `history.winter_severity_declared` is retained; future recovery/expiry must explicitly clear only the active cycle | CLOSED — source producer verified |
| `pred.market_pressure` | Explicit market-pressure producer/marker with deterministic persistence/clear rule | OPEN — producer still missing |
| `pred.guild_labor_tension` | Explicit labor-tension producer + persistence/clear rule | OPEN — producer still missing |
| `pred.information_pressure_high` | Independent information-state evidence/markers and deterministic qualification; never `rel.toma` alone | OPEN — source/cardinality missing |
| `pred.guild_influence_strong` | At least two distinct institutional domains from the canonical guild-influence domain set | PARTIAL |
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

## Known producer gaps

The following remain P0 for schema freeze:

- food stability;
- active transport disruption;
- market pressure;
- guild labor tension;
- high information pressure;
- exact guild-influence producer set;
- constitutional preparation;
- budget reform;
- final-charter prerequisites.

Winter severity is no longer a producer gap: E29-A/B are the explicit authored source for the current severe-winter cycle.

## Gate

This contract does not authorize engine implementation yet. The complete E01–E272 catalog must be reconciled against this matrix and all remaining producers/consumers must be explicitly mapped before schema freeze and validator implementation.
