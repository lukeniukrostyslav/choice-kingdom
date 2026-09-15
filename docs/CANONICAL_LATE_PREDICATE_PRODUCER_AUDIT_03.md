# Choice Kingdom — Canonical Late Predicate Producer Audit 03

Status: **SOURCE-LEVEL QA — NOT ENGINE IMPLEMENTATION**
Scope: E151–E272

## Purpose

Audit late authored nodes for safe producers of the remaining derived predicates. Trigger text and narrative pressure are not producers unless a choice writes a canonical state fact with matching semantics.

## Findings

| Predicate | Late candidates inspected | Verdict |
|---|---|---|
| `pred.food_stable` | E157 consumes food shortage; E167/E218 handle import/grain responses; E192 consumes transport disruption and writes `food_logistics_unstable` / `food_logistics_stabilized`; E225 consumes severe food pressure; E251/E254 consume food/winter crisis context | **NO SAFE DIRECT PRODUCER**. `food_logistics_stabilized` is not equivalent to kingdom-wide food stability. |
| `pred.transport_disruption` | E167 import risk, E170 border logistics, E192 consumes the predicate, E251 consumes winter + low transport | **NO SAFE DIRECT PRODUCER**. E192 must not manufacture the predicate it consumes. |
| `pred.winter_severe` | E160 consumes severe winter; E175 consumes winter illness; E251 consumes winter + low transport | **NO SAFE DIRECT PRODUCER**. Late consumers confirm the missing upstream state but do not establish it. |
| `pred.market_pressure` | E166/E219 consume strong market oversight; E181 toll callback and E220 insurance callback create commercial consequences | **NO SAFE DIRECT PRODUCER**. Commercial pressure must not be inferred from oversight, Ivo relationship, or downstream callbacks. |
| `pred.guild_labor_tension` | E169 consumes guild labor tension and resolves the strike; later guild events use route/leverage states | **NO SAFE PRODUCER**. E169 cannot self-produce its trigger condition. |
| `pred.information_pressure_high` | E179 consumes low information trust; E231 consumes high information pressure; E270 combines accounts; E247–E250 add replay evidence | **NO SAFE DIRECT PRODUCER**. Information activity/evidence count is not automatically high-pressure state. |
| `pred.guild_influence_strong` | E165 credit/debt domain, E168 independent tribunal, E166 market/merchant domain, E194 qualified logistics cooperation, E239 guild forecasting | **PARTIAL**. Multiple candidate institutional domains exist, but exact canonical source IDs and anti-double-counting rules remain to freeze. |
| `pred.constitutional_prepared_strong` | E154/E155 audit legitimacy, E161 house assembly, E227 military red line, E256–E260 constitutional stress tests | **PARTIAL**. Candidate domains exist; exact pre-E197 independent source set must be frozen and late stress tests must not retroactively manufacture preparation. |
| `pred.budget_reform` | E154/E155 crown audit, E216 treasury shortfall, E258 consumes budget reform | **OPEN**. E258 is a consumer and cannot establish the predicate; a legislative budget-lock source remains required. |
| `pred.coalition_cooperation` | E261 four-way bargain, E262 fifth voice, E263 audit, E264 break, E265 hold | **PARTIAL**. E261-A is explicit cooperation-package evidence; final qualification still requires canonical participant identity, positive outcome, and blocker semantics. |
| `pred.final_charter_prerequisites` | E256–E270 constitutional/endgame nodes, E271/E272 crisis lifecycle | **OPEN**. Late events provide convergence inputs but cannot manufacture missing upstream prerequisites. |

## Important semantic closures

1. `E192-A/B` produce logistics outcomes, not `pred.transport_disruption`; the predicate remains an upstream condition.
2. `E261-A` is explicit authored cooperation (`four_way_bargain`) and is stronger evidence than merely having four active routes, but it still requires the coalition contract's participant and outcome checks.
3. `E271-A` is a genuine explicit producer of `pred.border_crisis`; E271-B is an explicit non-crisis branch. E195/E253/E255 remain consumers.
4. E269 remains a late commercial evidence handoff and must stay distinct from E55.
5. E226 remains a late institutional-stress consequence and must stay distinct from E36.

## Result

The late catalog does not justify falsely closing the six missing core environmental/pressure producers. The correct next step is to inspect the earlier authoritative choices for an unambiguous semantic source. If none exists, a new authored producer node or an authoritative choice edit will be required before schema freeze; no predicate may be invented in the engine layer.

## Next work

- freeze exact independent guild-influence domains;
- freeze constitutional-preparation source IDs and exclusions;
- close coalition participant/outcome contract;
- identify or author explicit producers for the six missing predicates;
- extract exact delayed consequence identity/timing/cancellation/exactly-once rules;
- reconcile final-charter convergence and ending precedence;
- only then freeze production schema and implement the validator.
