# Choice Kingdom — E273–E276 Consumer / Alias Audit 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — ADMISSION STILL BLOCKED**

## Scope

E273–E276 explicitly introduce four predicate producers outside the frozen E01–E272 catalog. This pass checks the candidate semantics against the current canonical vocabulary and records what is proven without inventing consumers or aliases.

## E273 — `pred.food_stable`

Authored producer: E273-A.

- Active state is explicitly defined for the current food cycle.
- Historical marker: `history.food_stability_established`.
- The source requires a later explicit food-disruption event to clear the active predicate.
- No frozen E01–E272 consumer/lifecycle closure is established by this audit.
- Admission remains **BLOCKED** until a canonical food-disruption producer, consumer set, expiry/persistence semantics and reachable upstream path are frozen.

## E274 — `pred.market_pressure`

Authored producer: E274-A.

- Active state is explicit.
- Historical marker: `history.market_pressure_declared`.
- Source mentions a later stabilization policy as a possible clearer but does not identify a frozen event/choice producer.
- No canonical consumer/lifecycle closure is established here.

Admission: **BLOCKED**.

## E275 — `pred.guild_labor_tension`

Authored producers/clear semantics: E275-A clears; E275-B activates.

- This is a genuine state predicate, not a relationship-score alias.
- Existing canonical guild events use related concepts such as guild labor tension in triggers, but this audit does not equate prose trigger wording with the new predicate without an exact producer/consumer contract.
- A complete consumer inventory and duplicate-semantic check are still required.

Admission: **BLOCKED**.

## E276 — `pred.information_pressure_high`

Authored producers/clear semantics: E276-A clears; E276-B activates.

- The source explicitly states that `rel.toma` alone cannot manufacture the predicate.
- This correctly separates relationship state from systemic information pressure.
- Existing information-route events must be audited for exact predicate consumption before admission.

Admission: **BLOCKED**.

## Alias policy

The following substitutions are prohibited without an explicit canonical contract:

- `rel.toma` -> `pred.information_pressure_high`
- generic guild route / relationship score -> `pred.guild_labor_tension`
- generic food shortage prose -> `pred.food_stable`
- generic market pressure prose -> `pred.market_pressure`

A narrative trigger is not automatically an executable state predicate.

## Decision

E273–E276 remain outside the frozen E01–E272 production catalog. No runtime engine rule should consume them as production facts until consumer inventories, lifecycle semantics, reachability, persistence, replay isolation and same-turn ordering are reconciled.
