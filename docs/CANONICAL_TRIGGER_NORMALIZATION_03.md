# Choice Kingdom — Canonical Trigger Normalization 03

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — SAFE NORMALIZATIONS RECORDED; AMBIGUOUS PREDICATES REMAIN OPEN**
Scope: recurring prose trigger expressions found in the authored E01–E210 expansion layer and their mapping to the existing canonical predicate vocabulary.

## Purpose

This pass converts only trigger phrases whose semantic meaning is already covered by the canonical predicate matrix and whose separation rules are explicit. It does **not** invent thresholds, new state facts, or runtime booleans.

## Safe normalization set

| Authored phrase family | Canonical form | Evidence / constraint | Status |
|---|---|---|---|
| `high trust`, `high civic trust`, `civic/public trust` when used as a threshold | `pred.trust_high` | Matrix explicitly defines this predicate over the trust resource | **NORMALIZE**; numerical threshold remains balance-open |
| `low trust`, `public distrust` | `pred.trust_low` | Matrix explicitly defines the low-trust predicate | **NORMALIZE**; numerical threshold remains balance-open |
| `low security` | `pred.security_low` | Matrix explicitly defines security-low; must not be substituted for army readiness | **NORMALIZE** |
| `strong security` | `pred.security_high` | Matrix explicitly defines security-high | **NORMALIZE**; calibration remains open |
| `low gold`, `treasury pressure`, `strong treasury pressure` when used as resource pressure | `pred.gold_low` | Matrix explicitly defines treasury/gold pressure | **NORMALIZE**; threshold remains balance-open |
| `high power` / strong political power | `pred.power_high` | Matrix explicitly defines political-power predicate | **NORMALIZE**; threshold remains balance-open |
| `high reputation` | `pred.reputation_high` | Matrix explicitly defines reputation predicate | **NORMALIZE**; threshold remains balance-open |
| `food shortage`, `food-price pressure`, `food pressure` | `pred.food_pressure` | Matrix explicitly groups these phrases; food is not a sixth numeric resource | **NORMALIZE** to predicate family, but producer contract remains open |
| `severe winter`, `winter pressure` | `pred.winter_severe` | Matrix explicitly defines the family; exact winter producer/severity still open | **NORMALIZE** to predicate family, producer remains open |
| `border tension`, `border pressure` | `pred.border_tension` | Matrix explicitly defines diplomatic/border pressure; must remain distinct from security-low | **NORMALIZE** |
| `low army readiness` | `pred.army_readiness_low` | Matrix explicitly separates readiness from security | **NORMALIZE** |
| `strong market oversight`, `market pressure` | `pred.market_pressure` | Matrix explicitly groups the market-pressure family; exact producer set remains open | **NORMALIZE** to predicate family, producer remains open |
| `guild labor tension`, `apprentice pressure` | `pred.guild_labor_tension` | Matrix explicitly defines guild-labor pressure | **NORMALIZE** to predicate family, producer remains open |
| `high information pressure` | `pred.information_pressure_high` | Matrix explicitly defines information pressure and forbids substitution with Toma relationship | **NORMALIZE** to predicate family, cardinality remains open |
| `at least three independent evidence routes` / `three or more related clues` when explicitly intended as independent evidence | `pred.evidence_routes_3` | Matrix requires machine-checkable route independence | **NORMALIZE** only when independence IDs are present |
| `at least four major character/faction routes active` | `pred.faction_routes_4` | Matrix defines four-route cardinality | **NORMALIZE**; route-completion contract remains open |
| `simultaneous food, border and civic pressure` | `pred.multi_crisis_3` | Matrix defines this as an explicit conjunction of canonical predicates | **NORMALIZE** |
| `high reform spending` | `pred.reform_spending_high` | Matrix defines aggregate spending predicate | **NORMALIZE** to predicate family, accounting contract remains open |
| `audit reform`, `document audit route`, `institutional reform` when referring to the institutional route | `pred.institutional_reform` | Matrix explicitly defines institutional-reform route | **NORMALIZE** only where source context is institutional rather than generic trust |
| `deep/advanced investigation` | `pred.investigation_deep` | Matrix defines deep investigation from evidence + investigation thread | **NORMALIZE** to predicate family, exact route definition remains open |

## Deliberately NOT normalized as simple aliases

The following expressions remain contract-open because their authored meaning is broader or ambiguous:

- `civic relief` — may describe a state outcome, a route, or a trust condition; do not equate automatically with `pred.trust_high`.
- `local civic participation` / `local_relief_councils` — needs an explicit civic-history/thread contract.
- `guild leverage`, `merchant charter`, `guild political representation`, `commercial route` — these are not interchangeable; guild influence needs distinct institutional evidence rather than a raw Ivo relationship threshold.
- `information route`, `secret evidence route`, and named evidence flags — route activation and evidence cardinality must remain separate concepts.
- `emergency renewal possible`, `late constitutional preparation`, and `final charter prerequisites` — these are endgame gates, not generic aliases for one predicate.
- `winter illness` — medical/civic event condition; it cannot be silently collapsed into `pred.winter_severe`.
- `strong noble influence` — must not be treated as a raw relationship threshold without a canonical noble-influence contract.

## Verified source examples

### E115
`strong treasury pressure` is compatible with `pred.gold_low`; the event should consume the canonical predicate after the threshold is locked.

### E136
`winter severity` is compatible with the `pred.winter_severe` family, but E136 itself is a recovery/repair producer and must not become the winter-severity producer merely because it consumes winter severity.

### E164
`high noble influence + low security` demonstrates why two predicates are required: noble influence is not `pred.security_low`, and no raw relationship alias is authorized yet.

### E173
`low army readiness` must compile to `pred.army_readiness_low`, not `pred.security_low`.

### E192
`pred.transport_disruption` remains its own canonical condition. Its consumer does not prove `pred.food_pressure`; E192's `food_logistics_unstable` and `food_logistics_stabilized` outputs remain current-run markers until the food predicate producer contract is frozen.

## QA consequence

This pass reduces prose-vocabulary ambiguity without pretending that the remaining producer contracts are solved. It is safe to use as the normalization layer when the production data schema is eventually frozen.

## Remaining blockers

1. Freeze numerical thresholds for resource predicates through authored consumer validation and balance simulation.
2. Identify durable producers for food, winter, market, guild-labor and information predicates.
3. Define independent evidence/faction route identities.
4. Define noble influence and guild influence contracts without collapsing them into relationship values.
5. Reconcile all normalized triggers against `EVENT_GRAPH.md` and the complete E01–E272 catalog.
6. Only after those contracts are frozen, encode them in production data and implement the validator/engine.

## Gate

**Canonical trigger normalization: improved at source level.**

**Production schema: BLOCKED.**

**Runtime/reachability: NOT VERIFIED.**
