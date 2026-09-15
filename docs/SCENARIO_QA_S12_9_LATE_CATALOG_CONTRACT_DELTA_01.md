# Choice Kingdom — S12.9 Late Catalog Contract Delta 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — LATE CATALOG NORMALIZATION**
Frozen production scope: **E01–E272**.

## 1. E218 / E225 food-pressure consumers

### E218 — Grain Contract
Trigger: food pressure.
- E218-A → `grain_contract_inspected`
- E218-B → `grain_contract_rushed`

E218 does not create `pred.food_stable` and does not create food pressure merely by being reached.

### E225 — Bread Queue
Trigger: severe food pressure.
- E225-A → `bread_queue_heard`
- E225-B → `bread_queue_dispersed`

E225 is a consumer/consequence node. It cannot create `pred.food_stable` or reinterpret `food_logistics_stabilized` as that predicate.

## 2. Delayed callbacks E242–E246

| Event | Trigger/source | Delay | Canonical QA boundary |
|---|---|---:|---|
| E242 | prior noble exception | >=6 turns | source identity must identify the originating exception; multiple valid producers must not retroactively satisfy earlier consumers |
| E243 | `public_bridge` | >=5 turns | source event/choice identity required |
| E244 | `flexible_accounts` | >=5 turns | source identity required; missing accounting trail is consequence state, not a new producer |
| E245 | compensation route | >=6 turns | exact compensation producer must be retained; generic compensation must not silently become union state |
| E246 | price ceiling | >=5 turns | source price-ceiling identity required; ending the temporary measure must be distinct from generic price control |

All five require exact-once callback identity, save/load persistence and replay isolation before engine promotion.

## 3. Replay nodes E247–E250

- E247 is explicitly second-run information route.
- E248 is explicitly replay callback.
- E249 archive route remains ordinary-run state unless a separate authored meta contract is proven.
- E250 consumes multiple related clues and produces `pattern_anomaly_preserved` or no durable marker on B.

Hard rule: only intentionally persistent cross-run facts belong under `meta.*`; ordinary run flags must not leak into replay state.

## 4. Late crisis nodes E251–E255

- E251 consumes winter + low transport; it is a consequence consumer and does not itself establish transport disruption.
- E252 consumes illness + Amara route; it does not create illness or Amara eligibility.
- E253 consumes canonical `pred.border_crisis`; it cannot create that predicate.
- E254 consumes food crisis + local governance; it cannot create food stability.
- E255 consumes simultaneous food, border and civic pressure; it cannot manufacture any missing crisis predicate.

## 5. Constitutional stress E256–E260

- E256 consumes succession route.
- E257 consumes emergency powers.
- E258 consumes `pred.budget_reform`.
- E259 consumes army constitutional route.
- E260 consumes archive reform.

Their outputs are consequence markers and do not retroactively qualify the route/predicate consumed by the node.

## 6. Coalition endgame E261–E265

E261 requires at least four faction routes. `four_way_bargain` is evidence of a package but **does not alone prove** `pred.coalition_cooperation`.

E262 consumes `four_way_bargain`.
E263 consumes coalition route.
E264 consumes low coalition trust.
E265 consumes high coalition trust.

Coalition qualification must remain based on explicit positive cooperation evidence and independent participant/faction identity, with unresolved collapse blockers represented deterministically.

## 7. Personal endgame E266–E270

E266–E270 are late consequence/evidence nodes:
- E266 consumes active Mara route;
- E267 consumes active Rowan route;
- E268 consumes active Seris route;
- E269 is a distinct late commercial evidence handoff and must not be conflated with E55;
- E270 requires both Amara and Toma active and can produce `dual_witness_account`.

E270 does not itself prove `pred.systemic_explanation_verified`; it may contribute an evidence artifact if the future formula explicitly accepts it.

## 8. Border bridge E271

E271-A is the canonical producer of active `pred.border_crisis` eligibility:
- `border_crisis_declared = true`;
- `border_crisis_resolved = false`;
- `thread.border_crisis = active`.

E271-B is an explicit non-crisis branch and must not satisfy the predicate.

E195/E253/E255 are consumers and cannot manufacture the border crisis.

## 9. E272 closure boundary

The canonical producer inventory already records E272-A/B as the resolution/clear path for active `pred.border_crisis`. The machine graph must normalize the closure as a lifecycle transition, not a second producer:

`E271-A -> pred.border_crisis(active)`
`E272-A/B -> border crisis resolved / active predicate cleared`

The exact authored E272 branch tokens must be preserved when the complete catalog source is reconciled; no guessed token is introduced by this artifact.

## 10. Late-catalog acceptance checks

Reject graph promotion if:
- E218/E225 are treated as food-stability producers;
- E253 is treated as a border-crisis producer;
- E261 is treated as sufficient coalition cooperation without independent evidence;
- replay nodes write ordinary run state into `meta.*` without explicit contract;
- E242–E246 lack exact source identity and timing;
- E271-B satisfies border crisis;
- E272 closure is represented as a new unrelated predicate instead of lifecycle resolution.

## 11. Gate

**S12.9: PASS for the extracted late-catalog consumer/producer boundaries; PARTIAL for exact E272 branch token extraction, composite predicate formulas, and exhaustive reachability.**
