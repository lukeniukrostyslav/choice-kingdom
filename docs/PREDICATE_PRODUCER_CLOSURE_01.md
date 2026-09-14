# Choice Kingdom — Predicate Producer Closure 01

Date: 2026-09-15
Status: **QA WORKING CONTRACT — NOT ENGINE INPUT**
Scope: E01–E270

## Purpose

Close the highest-risk contextual predicates before production-schema freeze. A predicate is not valid for runtime merely because its name appears in prose. Each predicate must have explicit authored producers, deterministic inputs, a canonical persistence model, and no circular dependency.

## Canonical rule

Every derived predicate must be computed from canonical `resource.*`, `rel.*`, `flag.*`, `history.*`, `thread.*`, `delay.*`, or explicitly permitted `meta.*` inputs. A predicate must never create its own prerequisite state.

## 1. Food pressure

### Canonical families
- `pred.food_pressure`
- `pred.food_severe`
- `pred.food_crisis`
- `pred.food_stable`

### Verified producer evidence
- E03 changes grain/reserve state and imports.
- E29 changes granary/market-rationing state.
- E157 responds to food shortage and changes public mill ownership.
- E167 creates import-risk policy.
- E192 can worsen food pressure or improve food stability.
- E218 consumes food pressure and creates a grain-contract decision.
- E225 consumes severe food pressure.
- E251/E254/E255 consume winter/food crisis combinations.

### Closure requirement
Food must remain a derived condition or durable history/thread state. It must not become a sixth numeric resource.

Provisional deterministic representation:
- `food_pressure` is true when unresolved authored food-loss/shortage markers exceed authored mitigation markers.
- `food_severe` is true only when food pressure is active plus a severe-pressure producer is present.
- `food_crisis` is true only when an explicit crisis producer is active or a validated severe-pressure escalation occurs.

**OPEN:** exact weighted producer/mitigation formula must be selected from the authored effects before schema freeze.

## 2. Winter

### Canonical families
- `pred.winter_pressure`
- `pred.winter_severe`
- `pred.winter_illness`
- `pred.winter_transport_disruption`

### Verified producer evidence
- E29 first snow / granary decisions establish winter context.
- E160 explicitly consumes severe winter.
- E173 consumes low army readiness for a winter/civic alternative.
- E175 consumes winter illness.
- E192 combines road pressure with medicine/grain logistics.
- E251 consumes winter + low transport.
- E252 consumes illness + Amara route.

**OPEN:** exact winter activation window and producer markers must be explicit in machine-readable data; prose `winter` is not sufficient.

## 3. Border and security

These are deliberately separate:
- `pred.border_tension`
- `pred.border_crisis`
- `pred.security_low`
- `pred.security_high`
- `pred.army_readiness_low`

Verified producer anchors include E10/E16/E31, E37/E52, E164/E170–E172, E195, E227/E240/E253/E255/E259.

Rules:
1. `security_low` is computed from `resource.security` only.
2. `border_tension` requires authored border-history/thread inputs; it cannot be inferred from security alone.
3. `border_crisis` requires escalation beyond ordinary tension.
4. `army_readiness_low` is not identical to `security_low`; it needs readiness-specific authored inputs.
5. Military constitutional choices cannot silently satisfy border-crisis predicates.

## 4. Market and guild

Canonical predicates:
- `pred.market_pressure`
- `pred.market_oversight_strong`
- `pred.guild_labor_tension`
- `pred.guild_logistics_cooperation`
- `pred.trade_risk_active`

Producer anchors include E08/E14/E18/E19, E165–E169, E167, E194 and later economic callbacks.

Rules:
- `rel.ivo` is never market pressure.
- Guild route activation is explicit and distinct from a relationship value.
- `guild_labor_tension` requires an authored labor-conflict producer such as E169, not merely low trust.
- `trade_risk_active` requires explicit insurance/guarantee setup before E220 can fire.

## 5. Information and evidence

Canonical predicates/sets:
- `pred.information_pressure_high`
- `pred.evidence_fragments_2`
- `pred.evidence_fragments_3`
- `pred.procurement_clues_2`
- `pred.witness_route`
- `pred.systemic_explanation_verified`

Verified evidence anchors include E21/E23/E28, E41–E43, E53/E57, E178–E190 and E231–E250.

Evidence cardinality must be represented as a deterministic set/count of distinct evidence identities, not as repeated generic `evidence=true` flags. Duplicate evidence cannot inflate cardinality.

`pred.systemic_explanation_verified` must require explicit authored convergence, not simply three clues.

## 6. Institutional and budget reform

Canonical separation:
- `pred.institutional_reform`
- `pred.budget_reform`
- `pred.document_audit`
- `pred.archive_reform`

Producer anchors:
- institutional: E09, E35–E36, E46–E48, E151/E154/E155/E214/E226.
- budget: E198/E216/E258 and earlier fiscal reform decisions.
- document audit: E09/E21/E23/E152/E154/E155.
- archive reform: E260 plus prior archive-access decisions.

No one predicate may be defined as another predicate's existence. Each requires its own minimum authored marker combination.

## 7. Multi-crisis

`pred.multi_crisis_3` is true only when all three are simultaneously true at eligibility evaluation time:

- `pred.food_pressure`;
- `pred.border_tension` or validated border crisis;
- explicit civic/public-pressure predicate.

It must not be toggled by UI or inferred merely because E255 follows three unrelated events.

## 8. Four-faction cardinality

E261 requires four distinct faction route identities, not four events and not four relationship values. Candidate set:
- Commons;
- Houses;
- Guilds;
- Border.

Each route must have an explicit producer. Repeated activation of one route does not increase cardinality.

## 9. Ending predicates

E265–E270 must consume canonical history/thread/predicate inputs. Character relationships alone cannot qualify an ending.

The seven designed ending families remain:
- Steward
- Iron Crown
- Golden Compact
- People's Charter
- Broken Diadem
- Quiet Throne
- Second Founder

Ending simulation remains open until production data exists.

## 10. Closure status

| Predicate family | Status |
|---|---|
| food | PARTIAL — producers known, exact formula open |
| winter | PARTIAL — producers known, explicit runtime markers open |
| border/security | PARTIAL — separation locked, crisis/readiness producers open |
| market/guild | PARTIAL — route separation locked, thresholds open |
| information/evidence | PARTIAL — cardinality model defined, producer enumeration open |
| institutional | PARTIAL — producers known, minimum combination open |
| budget | OPEN — exact producer set requires full E191–E210 review |
| multi-crisis | DESIGN CLOSED, source predicates open |
| four-faction | DESIGN CLOSED, runtime route set open |
| endings | DESIGN CLOSED, simulations open |

No predicate is production-ready yet. This document is a QA closure artifact and must be translated into machine-readable contracts only after the remaining source-level producer audit passes.
