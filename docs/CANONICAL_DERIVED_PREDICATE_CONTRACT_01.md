# Choice Kingdom — Canonical Derived Predicate Contract 01

Status: **SOURCE-LEVEL CONTRACT — NOT ENGINE IMPLEMENTATION**
Production scope: **E01–E272 only**  
Expansion candidates: **E273–E277 excluded from production semantics**

## Purpose

Freeze deterministic semantic inputs for contextual conditions before production schema work. These conditions are not sixth resources and may not be inferred from relationship scores, consumer reachability, or prose alone.

## Production contract matrix

| Predicate | Canonical source inputs | Current status |
|---|---|---|
| `pred.border_crisis` | `border_crisis_declared = true` AND `border_crisis_resolved != true`; lifecycle declaration E271-A, resolution E272-A/B | CLOSED at source level; runtime lifecycle open |
| `pred.guild_logistics_cooperation` | upstream `history.guild_logistics_cooperation` AND E194-A `guild_neutral_inspectors` AND no unresolved `guild_logistics_immunity_risk` | CLOSED at source level; runtime qualification open |
| `pred.food_stable` | No E01–E272 producer currently verified; E273-A is expansion-only | OPEN / BLOCKED |
| `pred.transport_disruption` | E32 explicit active disruption producer; E136-A/B explicit recovery/clear | CLOSED at source level; runtime lifecycle open |
| `pred.winter_severe` | E29-A/B explicitly establish severe winter for current winter cycle; history retained | CLOSED at source level; runtime cycle expiry open |
| `pred.market_pressure` | E19-B establishes current market-pressure cycle; E19-A clears active cycle | CLOSED at source level; runtime cycle lifecycle open |
| `pred.guild_labor_tension` | No E01–E272 producer currently verified; E275-B is expansion-only | OPEN / BLOCKED |
| `pred.information_pressure_high` | No E01–E272 producer currently verified; E276-B is expansion-only | OPEN / BLOCKED |
| `pred.guild_influence_strong` | At least two distinct domains from: representation=`guild_political_representation`/`history.guild_representation`; tribunal=`guild_tribunal_independent`; commercial=`official_credit_disclosure`/`audited_monopoly`; qualified logistics=`history.guild_logistics_cooperation` + E194-A qualification | SOURCE CONTRACT CLOSED; executable aggregation/reachability open |
| `pred.systemic_explanation_verified` | warehouse/financial evidence + document/language evidence + witness/organizational evidence + explicit E270-A convergence decision | SOURCE CONTRACT CLOSED by E270-A; runtime evidence aggregation/reachability open |
| `pred.coalition_cooperation` | E148-A `history.cross_faction_package` with named participants, positive mutual-concession outcome, and no unresolved coalition-collapse blocker; E261-A is not sufficient by itself | SOURCE CONTRACT CLOSED; runtime blocker evaluation/reachability open |
| `pred.constitutional_prepared_strong` | Any 3 of 4 independent domains: civic=`people_charter_endorsed` (E50); institutional=`crown_audited` (E154); factional=`house_assembly` (E161); military/law=`army_constitution_oath` (E199) | SOURCE CONTRACT CLOSED; executable aggregation/reachability open |
| `pred.budget_reform` | E142-A `auditor_independence` + E154-A `crown_audited` + E198-A `legislative_budget_lock`; E142-B/E154-B/E198-B negative blockers; E155-A same-domain downstream evidence | SOURCE CONTRACT CLOSED; runtime invalidation/reachability open |
| `pred.final_charter_prerequisites` | convergence of civic, institutional, faction/house/guild, military/security, information/evidence, coalition and crisis-resolution facts, with mandatory blockers cleared | OPEN / BLOCKED — consumer E209 remains downstream |

## Hard derivation rules

1. A consumer event cannot create the predicate it consumes.
2. A relationship score cannot qualify a route or contextual predicate unless the authored contract explicitly defines that numeric gate.
3. Historical evidence does not automatically imply current stability; current predicates require current validity rules.
4. Resolution invalidates an active predicate without erasing immutable historical evidence.
5. Evidence cardinality is evaluated by independent source identity, not by counting flags from one chain.
6. Coalition qualification requires explicit cooperation semantics, not four-way/five-way route cardinality.
7. Derived predicates require deterministic inputs and deterministic invalidation/clear behavior before entering production schema.
8. A producer outside E01–E272 cannot satisfy a production producer/consumer lookup.
9. A later producer must not retroactively satisfy an earlier consumer; cycle identity is required once runtime exists.

## Current source-level production closures

- `pred.market_pressure`: E19-B producer, E19-A clear.
- `pred.transport_disruption`: E32 producer, E136-A/B clear.
- `pred.winter_severe`: E29-A/B producer.
- `pred.border_crisis`: E271-A producer, E272-A/B clear.
- `pred.guild_logistics_cooperation`: upstream E136-B cooperation marker + E194-A neutral inspection + no immunity-risk blocker.
- `pred.guild_influence_strong`: canonical domain set frozen; E49/E144 representation is one domain only.
- `pred.systemic_explanation_verified`: E270-A is the explicit convergence producer; it cannot manufacture missing evidence families.
- `pred.coalition_cooperation`: E148-A is the authoritative package source; participant identity is explicit; E261-A alone is not qualification.
- `pred.constitutional_prepared_strong`: any three independent domains from E50/E154/E161/E199; downstream consequences do not silently create a fourth independent domain.
- `pred.budget_reform`: E142-A/E154-A/E198-A are the three independent institutional layers; negative blockers are explicit.
- `pred.food_stable`: no E01–E272 producer verified.
- `pred.guild_labor_tension`: no E01–E272 producer verified.
- `pred.information_pressure_high`: no E01–E272 producer verified.

## Expansion quarantine — E273–E277

E273–E277 remain authored expansion candidates and are **not production inputs**:

- E273-A `food_stability_standard` — cannot produce production `pred.food_stable`.
- E274-A market-pressure producer — cannot satisfy production chronology.
- E275-A/B guild-labor clear/producer pair — expansion-only.
- E276-A/B information-pressure clear/producer pair — expansion-only.
- E277 transport recovery — expansion-only.

Expansion admission requires an explicit scope change and re-running event-ID, trigger, contradiction, cycle, delay, save/load and reachability audits.

## Frozen composite source identities

### Guild influence

E49's `guild_political_representation` and E144's `history.guild_representation` are one representation domain. Additional independent domains are guild tribunal, commercial/credit evidence, and qualified logistics cooperation. `rel.ivo` alone is forbidden.

### Constitutional preparation

E50 → `people_charter_endorsed`; E154 → `crown_audited`; E161 → `house_assembly`; E199 → `army_constitution_oath`. Any three distinct domains qualify the source-level predicate. E227 `military_red_line` is supporting evidence and is not substituted for E199.

### Budget reform

E142-A → `auditor_independence`; E154-A → `crown_audited`; E198-A → `legislative_budget_lock`. E155-A is same-domain downstream evidence and cannot count twice.

### Systemic explanation

E232–E236 provide candidate evidence families. E270-A explicitly records `systemic_explanation_convergence` after the contract requires the three evidence families to already exist. The trigger `Amara and Toma both active` is not evidence.

### Coalition cooperation

E148-A records the cross-faction package and named participation from Mara, Rowan, Seris, Ivo, Amara and Toma. The qualification requires that package plus positive mutual-concession semantics and absence of an unresolved collapse blocker. `four_way_bargain` is not an alias.

## Gate

Source-level composite predicate semantics are now frozen wherever an in-scope authored producer exists. Runtime lifecycle, persistence, contradiction invalidation and fresh-run/replay reachability remain downstream gates. No production schema or Decision Engine implementation is authorized by this document alone.
