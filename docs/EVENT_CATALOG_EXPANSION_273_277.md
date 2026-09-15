# Choice Kingdom — Canonical Producer Expansion E273–E277

Status: **AUTHORED SOURCE PATCH — P0 PREDICATE PRODUCERS**

These nodes give previously inferred contextual states explicit authored producers. They are real narrative decisions, not hidden engine mutations.

## E273 — The Bread Ledger
**Trigger:** `food_logistics_stabilized` or severe food pressure.

Avelune's millers, granary keepers and local councils present a consolidated food ledger. The ruler must decide whether to establish a durable kingdom-wide supply standard.

**A — Establish the public reserve standard**
- Immediate: -5 gold, +5 trust.
- Flag: `food_stability_standard`.
- State: `pred.food_stable = active` for the current food cycle.
- History: `history.food_stability_established`.
- A later explicit food-disruption event clears the active predicate without erasing the history marker.

**B — Leave reserves decentralized**
- Immediate: +3 power, -3 trust.
- Flag: `food_stability_decentralized`.
- Does not establish `pred.food_stable`.

## E274 — The Market Shock
**Trigger:** `merchant_charter` or `price_fixing` or `market_reform`.

A sudden shortage causes merchants to raise prices, delay contracts and demand guarantees. The Crown must decide whether the pressure must be formally managed.

**A — Declare a market-pressure emergency**
- Immediate: -3 gold, +3 trust, -2 power.
- Flag: `market_pressure_declared`.
- State: `pred.market_pressure = active`.
- History: `history.market_pressure_declared`.

**B — Let prices reset without intervention**
- Immediate: +3 power, -4 trust.
- Flag: `market_pressure_unmanaged`.
- Does not establish the predicate.

A later explicit stabilization policy may clear the active state while retaining its historical declaration.

## E275 — The Apprentices' Bell
**Trigger:** guild route, unsafe-work evidence, or commercial standards.

Apprentices from several guilds stop work after repeated injuries. The dispute becomes a kingdom-wide labor question.

**A — Recognize a protected labor standard**
- Immediate: -3 gold, +5 trust, -2 Ivo.
- Flag: `guild_labor_standard`.
- Clears `pred.guild_labor_tension` if active.
- History: `history.guild_labor_reform`.

**B — Order the guilds back to work**
- Immediate: +3 security, -5 trust.
- Flag: `guild_labor_ordered_back`.
- State: `pred.guild_labor_tension = active`.
- History: `history.guild_labor_tension_declared`.

## E276 — The Information Office
**Trigger:** Toma route, protected-source route, or repeated information instability.

Contradictory reports arrive faster than the Crown can verify them. Toma proposes an independent verification office.

**A — Establish independent verification**
- Immediate: -4 gold, +5 trust, -2 power.
- Flag: `information_verification_office`.
- Clears `pred.information_pressure_high` if active.
- History: `history.information_pressure_reformed`.

**B — Suppress unverified reports**
- Immediate: +4 security, -6 trust.
- Flag: `information_pressure_suppressed`.
- State: `pred.information_pressure_high = active`.
- History: `history.information_pressure_declared`.

High information pressure is therefore authored explicitly and cannot be manufactured from `rel.toma` alone.

## E277 — The Road Census
**Trigger:** `transport_disruption_active` or `roads_guild_contract`.

Surveyors report that roads, bridges and carts are failing in different districts. The ruler must decide whether the Crown will maintain a minimum transport network.

**A — Establish the royal road standard**
- Immediate: -5 gold, +4 security, +3 trust.
- Flag: `road_maintenance_standard`.
- State: `transport_network_stable`; clears `transport_disruption_active`.
- History: `history.transport_recovery_established`.

**B — Leave routes to local contracts**
- Immediate: +2 power, +2 Ivo, -3 trust.
- Flag: `local_transport_contracts`.
- Clears `transport_disruption_active` only where local contracts are already active; does not claim kingdom-wide stability.

## Producer contract

- E273 explicitly produces `pred.food_stable`.
- E274 explicitly produces `pred.market_pressure`.
- E275 explicitly produces `pred.guild_labor_tension`.
- E276 explicitly produces `pred.information_pressure_high`.
- E277 explicitly defines transport recovery/clear semantics.

These nodes remain subject to full catalog reconciliation, reachability, trigger normalization, delayed-consequence and consumer QA before production schema freeze.
