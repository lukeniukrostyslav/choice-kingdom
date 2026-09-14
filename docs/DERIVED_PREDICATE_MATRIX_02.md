# Choice Kingdom — Derived Predicate Matrix 02

Date: 2026-09-14
Status: **CANONICALIZATION WORKING SPEC — THRESHOLDS NOT ALL BALANCE-LOCKED**

## Purpose
Normalize recurring prose triggers into deterministic predicate names without pretending final numerical balance is already proven. A predicate is production-ready only when its inputs have verified producers, its threshold/cardinality is explicit, and reachability tests prove intended true and false states.

## Canonical namespaces
- `pred.*` — deterministic derived predicates.
- `hist.*` — immutable decision/history markers.
- `thread.*` — active/completed causal route.
- `rel.*` — character relationship values.
- `meta.*` — replay-only metadata.

## Predicate candidates

| Canonical predicate | Source phrases normalized | Inputs | Status |
|---|---|---|---|
| `pred.trust_high` | high civic/public trust | `resources.trust` | provisional threshold; balance validation open |
| `pred.trust_low` | low trust / public distrust | `resources.trust` | threshold requires authored consumer validation |
| `pred.security_low` | low security / low defensive capacity | security resource + explicit security history where required | provisional; not equivalent to military route |
| `pred.security_high` | strong security | `resources.security` | calibration open |
| `pred.gold_low` | low gold / treasury pressure | `resources.gold` | provisional; check E216/economic routes |
| `pred.power_high` | high political power | `resources.power` | provisional |
| `pred.reputation_high` | high reputation | `resources.reputation` | provisional |
| `pred.food_pressure` | food shortage / food-price pressure / food pressure | food/grain history + delayed outcomes | producer inventory + exact definition required |
| `pred.food_severe` | severe food pressure / food crisis | `pred.food_pressure` + severity source | exact severity rule required |
| `pred.winter_severe` | severe winter / winter pressure | winter history markers | canonical producer required |
| `pred.border_tension` | border tension / pressure / escalation | border markers + security/diplomatic history | must preserve diplomacy vs military distinction |
| `pred.army_readiness_low` | low army readiness | military readiness markers/resources | not equivalent to `pred.security_low` |
| `pred.market_pressure` | market pressure / strong market oversight | market policy history + economic state | canonical producer set required |
| `pred.guild_labor_tension` | guild labor tension / apprentice pressure | guild labor markers/thread | producer set incomplete |
| `pred.information_pressure_high` | high information pressure | information thread/history | cardinality rule required |
| `pred.evidence_routes_3` | at least three independent evidence routes | independent evidence set | independence must be machine-checkable |
| `pred.faction_routes_4` | at least four faction routes | canonical faction-route completions | cardinality rule required |
| `pred.multi_crisis_3` | simultaneous food + border + civic pressure | three canonical predicates | explicit conjunction; E255 consumer |
| `pred.reform_spending_high` | high reform spending | immutable spending history / cost ledger | aggregate accounting contract required |
| `pred.institutional_reform` | institutional reform / audit reform / document audit route | canonical institutional thread | must replace prose shorthand |
| `pred.investigation_deep` | deep/advanced investigation | evidence cardinality + investigation thread | exact route definition required |

## Hard separation rules
1. `pred.security_low` is not `pred.army_readiness_low`.
2. `pred.border_tension` is not equivalent to `pred.security_low`.
3. `pred.market_pressure` is not equivalent to `rel.ivo`.
4. `pred.information_pressure_high` is not equivalent to `rel.toma`.
5. `pred.institutional_reform` is not equivalent to generic high trust.
6. `pred.food_pressure` must not become an implicit sixth resource.
7. `meta.*` replay evidence cannot satisfy ordinary current-run predicates without an explicit replay-transfer rule.
8. Relationship thresholds such as `Mara >= 1` compile to `rel.mara >= 1`, never generic event counters.

## Producer requirements
Before production schema lock, identify every producer, consumer, exclusivity/combinability rule, save/load behavior, delayed-effect behavior, replay interaction, and whether both predicate truth values are reachable.

## Current blockers
- Food and winter severity are not fully defined.
- Border/security vocabulary remains partially normalized.
- Market/guild pressure needs canonical producers.
- Information/evidence cardinality needs machine-readable independence identities.
- Reform-spending aggregation lacks a final state contract.
- E35–E40 source collision can affect ending/reachability predicates.

## Gate
This is a normalization specification, not implementation. Production schema remains blocked until producer/consumer extraction and reachability simulation are complete.
