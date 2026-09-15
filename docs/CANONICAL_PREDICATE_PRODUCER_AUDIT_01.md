# Choice Kingdom — Canonical Predicate Producer Audit 01

Status: **SOURCE-LEVEL QA — NOT ENGINE IMPLEMENTATION**
Scope: E151–E225 plus existing derived-predicate contract.

## Purpose

Audit authored candidates before assigning any missing derived predicate a producer. A trigger phrase is not automatically a producer. A producer must create an explicit canonical state fact whose semantic meaning matches the predicate and whose invalidation/clear rule is deterministic.

## Findings

| Predicate | Candidate authored evidence | Verdict |
|---|---|---|
| `pred.food_stable` | E157 `food shortage` is a consumer condition; E218 `grain_contract_inspected` proves inspection only; E225 `severe food pressure` is a consumer condition | **NO SAFE PRODUCER YET** |
| `pred.transport_disruption` | E167 import risk and E170 border logistics touch movement, but neither establishes a canonical transport-disruption fact | **NO SAFE PRODUCER YET** |
| `pred.winter_severe` | E160 uses `severe winter`; E175 uses `winter illness`, but neither choice currently writes an explicit severity marker | **NO SAFE PRODUCER YET** |
| `pred.market_pressure` | E166 `strong market oversight` is a trigger; E219 `strong market oversight` is also a trigger; choices create oversight outcomes but no explicit pressure lifecycle | **NO SAFE PRODUCER YET** |
| `pred.guild_labor_tension` | E169 consumes `guild labor tension`; its choices resolve the strike but no explicit producer in the inspected range establishes the tension fact | **NO SAFE PRODUCER YET** |
| `pred.information_pressure_high` | E179 consumes `low information trust`; E231 consumes `high information pressure`; Toma route markers exist, but no deterministic high-pressure state source is explicit here | **NO SAFE PRODUCER YET** |
| `pred.guild_influence_strong` | E165 `guild leverage`, E168 tribunal, E166 market oversight/merchant charter and related route material provide distinct institutional domains | **PARTIAL — requires exact source-set freeze** |
| `pred.constitutional_prepared_strong` | E161 house assembly, E154/E155 crown audit, E227 military red line and earlier civic preparation provide candidate domains | **PARTIAL — requires independent-source cardinality freeze** |
| `pred.budget_reform` | E154/E155 establish crown audit legitimacy; later budget/ledger events exist, but legislative budget lock is not yet an exact frozen source | **OPEN** |
| `pred.final_charter_prerequisites` | Late narrative has civic, institutional, factional, military, information, evidence and crisis material, but convergence is not yet an executable non-circular predicate | **OPEN** |

## Hard conclusions

1. Do not promote an event's trigger into a producer merely because the wording is similar.
2. Do not use `food shortage`, `severe winter`, `guild labor tension`, `high information pressure`, or similar prose as machine state until an authored choice explicitly establishes the corresponding fact.
3. Do not derive `pred.market_pressure` from `pred.guild_influence_strong` or relationship scores.
4. Do not count repeated use of one condition as independent evidence.
5. Any future producer patch must be a semantic source edit in the authoritative event catalog and must be followed by a producer/consumer re-audit.

## Result

This pass prevents false closure. The six major missing producer gaps remain genuinely open rather than being closed by trigger-name inference. The strongest current closure candidates are guild influence and constitutional preparation, but both still require exact independent-source sets.

## Next required work

- inspect earlier E01–E150 sources for safe authored choices that can establish missing predicates;
- inspect E226–E272 for late producers/resolution semantics;
- freeze exact independent source IDs for guild influence and constitutional preparation;
- only then patch authoritative catalog state and update the derived-predicate contract.
