# Choice Kingdom — Canonical Derived Predicate Contract 01

Status: **SOURCE-LEVEL CONTRACT — NOT ENGINE IMPLEMENTATION**
Production scope: **E01–E272 only**  
Expansion candidates: **E273–E277 excluded from production semantics**

## Purpose

Freeze the semantic rule for contextual conditions before production schema work. These conditions are not sixth resources and may not be inferred from relationship scores, consumer reachability, or prose alone.

## Production contract matrix

| Predicate | Canonical source inputs | Current status |
|---|---|---|
| `pred.border_crisis` | `border_crisis_declared = true` AND `border_crisis_resolved != true`; lifecycle declaration E271-A, resolution E272-A/B | CLOSED |
| `pred.guild_logistics_cooperation` | `history.guild_logistics_cooperation` AND E194-A neutral-inspection outcome AND no unresolved immunity-risk blocker | CLOSED |
| `pred.food_stable` | **No E01–E272 producer currently verified**; E273-A is expansion-only and rejected from production | OPEN / BLOCKED |
| `pred.transport_disruption` | E32 explicit active disruption producer; E136-A/B recovery/clear | SOURCE PRODUCER CLOSED — lifecycle clear/expiry still OPEN |
| `pred.winter_severe` | E29-A/B explicitly establish severe winter for current winter cycle; history retained; explicit cycle expiry/recovery required | CLOSED — source producer verified |
| `pred.market_pressure` | E19-B `market_pressure_declared` establishes the current market-pressure cycle; E19-A explicitly clears an active cycle | CLOSED — lifecycle semantics still need authored reconciliation |
| `pred.guild_labor_tension` | No E01–E272 producer admitted from expansion-only E275-B; production source remains OPEN until an in-scope authored producer is verified | OPEN |
| `pred.information_pressure_high` | No E01–E272 producer admitted from expansion-only E276-B; production source remains OPEN until an in-scope authored producer is verified | OPEN |
| `pred.guild_influence_strong` | At least two distinct institutional domains from canonical guild-influence domain set: representation=`guild_political_representation`; tribunal=`guild_tribunal_independent`; market/credit=`official_credit_disclosure`/`audited_monopoly` as one commercial domain; logistics=`history.guild_logistics_cooperation` with qualified E194-A semantics | PARTIAL — source identities frozen; full producer-before-consumer and anti-double-counting reconciliation remains OPEN |
| `pred.systemic_explanation_verified` | Distinct warehouse/financial evidence + document/language evidence + witness/organizational evidence + explicit convergence decision | PARTIAL |
| `pred.coalition_cooperation` | Explicit cooperation package with identified participants and positive cooperation outcome; not route-count based | PARTIAL |
| `pred.constitutional_prepared_strong` | Three independent preparation domains: civic/commons=`people_charter_endorsed`; institutional/audit=`crown_audited`/`full_crown_audit_published`; factional/house=`house_assembly`; military/law=`military_red_line` | PARTIAL — exact source identities frozen; full E01–E272 anti-double-counting and producer-before-consumer reconciliation remains OPEN |
| `pred.budget_reform` | E142-A `auditor_independence` + E154-A `crown_audited` + E198-A `legislative_budget_lock`; E142-B/E154-B/E198-B are negative blockers; E155-A is same-domain downstream evidence and cannot count twice | **SOURCE-CLOSED — runtime lifecycle/invalidation/reachability still OPEN** |
| `pred.final_charter_prerequisites` | Convergence of already-established civic, institutional, faction/house/guild, military/security, information/evidence, coalition and crisis-resolution facts, with mandatory blockers cleared | OPEN |

## Hard derivation rules

1. A consumer event cannot create the predicate it consumes.
2. A relationship score cannot qualify a route or contextual predicate unless the authored contract explicitly defines that numeric gate.
3. Historical evidence does not automatically imply current stability; current predicates require current validity rules.
4. Resolution must invalidate an active predicate without erasing immutable historical evidence.
5. Evidence cardinality must be evaluated by independent source identity, not by counting flags from one chain.
6. Coalition qualification requires explicit cooperation semantics, not four-way/five-way route cardinality.
7. Derived predicates must have deterministic inputs and deterministic invalidation/clear behavior before they enter production schema.
8. A newly authored producer outside the E01–E272 production scope cannot be treated as reachable production content merely because its trigger text names an existing state.
9. A predicate may have multiple authored producers when each producer establishes a distinct valid current cycle; a later producer must not retroactively satisfy an earlier consumer.

## Current source-level production closures

- `pred.food_stable`: **no E01–E272 producer verified**. E273-A is explicitly excluded from production.
- `pred.market_pressure`: E19-B is the explicit early producer for the market-pressure cycle; E19-A explicitly clears the active cycle. Any later producer must be E01–E272 and independently verified.
- `pred.transport_disruption`: E32 is the explicit active producer for the first canonical compound-crisis cycle. E136-A/B are recovery/clear semantics and cannot be treated as producers.
- `pred.winter_severe`: E29-A/E29-B are the source-closed producers for the current winter cycle.
- `pred.budget_reform`: E142-A, E154-A and E198-A are independently source-closed institutional layers; E142-B/E154-B/E198-B are explicit negative blockers; E155-A is same-domain downstream evidence and is not an independent fourth input.

## Expansion quarantine — E273–E277

E273–E277 remain authored expansion candidates and are **not production inputs**. Their previously documented predicate producers are quarantined here and cannot satisfy any E01–E272 producer/consumer lookup:

- E273-A `food_stability_standard` — expansion-only; cannot produce production `pred.food_stable`.
- E274-A market-pressure producer — expansion-only; cannot satisfy production chronology.
- E275-A/B guild-labor clear/producer pair — expansion-only.
- E276-A/B information-pressure clear/producer pair — expansion-only.
- E277 transport recovery — expansion-only; cannot serve as production transport lifecycle evidence.

Expansion admission requires a separate explicit scope change and re-running event-ID, trigger, contradiction, cycle, delay, save/load and reachability audits.

## Frozen composite source identities

### Guild influence

E49 is confirmed by the authoritative E01–E70 producer inventory as `guild_political_representation`. The opposing E49-B outcome is `guild_political_exclusion`. E144 later normalizes the continuing representation history into `history.guild_representation`. These are related representation facts, not separate institutional domains.

### Constitutional preparation

E50 is confirmed by the authoritative E01–E70 producer inventory as `people_charter_endorsed`. It is the frozen civic/commons preparation source. Later civic consequences derived from the same charter must not be counted as independent domains.

### Budget reform

The source identity is now reconciled with `CANONICAL_PRODUCER_INVENTORY_01.md`: E142-A establishes auditor independence, E154-A establishes the Crown-audit layer, and E198-A establishes the legislative budget lock. The three inputs are independent institutional layers under the current contract. E155-A is explicitly downstream/same-domain and cannot create a second audit domain. Runtime invalidation, reachability and ordering remain open.

## Gate

Production schema and runtime remain blocked until the E01–E272 producer/consumer contracts are reconciled and all remaining source, lifecycle and reachability gates are explicitly mapped.
