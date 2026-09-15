# Choice Kingdom — E273–E277 Admission Reconciliation 01

Status: **GRAPH/CONSUMER GATE — NOT YET ADMITTED**

The authored E273–E277 expansion is intentionally kept outside the frozen E01–E272 production catalog until its graph position and lifecycle semantics are proven.

## Admission matrix

| Event | Candidate producer | Current role | Admission state | Blocking reason |
|---|---|---|---|---|
| E273 | `pred.food_stable` | food-stability producer | **BLOCKED** | active-cycle invalidation/expiry and all consumer ordering still require canonical reconciliation |
| E274 | `pred.market_pressure` | additional market-pressure producer | **BLOCKED** | must reconcile with the earlier market-pressure lifecycle and prove it does not retroactively satisfy earlier consumers |
| E275 | `pred.guild_labor_tension` | labor-tension producer/clearer | **BLOCKED** | must reconcile thread semantics, existing E169 consumer behavior and duplicate/alias vocabulary |
| E276 | `pred.information_pressure_high` | information-pressure producer/clearer | **BLOCKED** | must reconcile cardinality/evidence semantics and existing E231/E236 information consumers |
| E277 | `transport_network_stable` / disruption clear | transport recovery candidate | **BLOCKED** | E136 is already the canonical recovery bridge for the frozen cycle; E277 must not create a competing recovery path without explicit cycle precedence |

## E273 — food stability

E273-A is a real authored producer candidate for `pred.food_stable`.

It must not be admitted merely because the predicate was previously missing. Before admission, the catalog must define:

1. the active-cycle identity;
2. what event invalidates or expires the predicate;
3. whether E273 can satisfy consumers only after its own turn;
4. whether later food disruption clears the predicate without erasing historical evidence;
5. deterministic ordering when a food-disruption event and a consumer occur on the same turn.

`history.food_stability_established` is historical evidence and must remain distinct from the active predicate.

## E274 — market pressure

E274-A is a second authored producer candidate. Existing market-pressure semantics already have earlier source material, so admission must first reconcile producer precedence and lifecycle identity.

E274-A must not be treated as a replacement for an earlier canonical source if an earlier event already owns the current market-pressure cycle. It may represent a later independent cycle only if cycle identity is explicit.

## E275 — guild labor tension

E275-B explicitly activates `pred.guild_labor_tension`; E275-A explicitly clears it.

Admission remains blocked until the existing guild-labor thread and E169 route are reconciled so that:

- labor tension is not inferred from `rel.ivo`;
- a resolved strike is not silently converted into a permanent positive/negative predicate;
- active and historical markers remain distinct;
- duplicate producer aliases are normalized.

## E276 — information pressure

E276-B explicitly activates `pred.information_pressure_high`; E276-A explicitly clears it.

The existing information route contains evidence, Toma relationship and verification outcomes. None of these may be silently substituted for the explicit active pressure predicate.

Admission therefore requires a closed cardinality/evidence rule for any downstream consumer that asks for “high information pressure”.

## E277 — transport recovery

E277-A duplicates the conceptual recovery role already held by E136-A/B. This is the highest-risk candidate in the expansion.

Until a cycle/precedence rule exists, E277 must **not** be admitted as an additional generic producer of transport stability. Otherwise two authored recovery events could race to clear the same disruption without a canonical cycle identity.

E277-B is narrower: it clears disruption only where local contracts already exist and therefore cannot claim kingdom-wide stability.

## Admission rule

E273–E277 may enter the frozen production catalog only after all five events pass:

- trigger normalization;
- producer/consumer closure;
- duplicate-producer analysis;
- reachability/cycle analysis;
- delayed/replay/save-load semantics where applicable.

Until then, the frozen catalog remains **E01–E272**.
