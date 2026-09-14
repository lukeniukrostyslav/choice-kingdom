# Choice Kingdom — Canonical Source Corrections 01

Date: 2026-09-15
Status: **AUTHORED QA PATCH — PRE-RUNTIME**

This document is the explicit source correction register for defects found during Producer Gap Closure Pass 04. It is intentionally written as a correction specification so that no runtime implementation can silently reinterpret prose.

## E192 — Broken Cart

### Problem
The existing B choice says `+4 food stability`, but `food` is not a canonical numeric resource.

### Required authored replacement
- A — Prioritize medicine: `+4 trust`; establish `flag.food_logistics_unstable`; activate/continue the winter logistics pressure route.
- B — Prioritize grain: establish `flag.food_logistics_stabilized`; improve the food-pressure derived condition; apply the existing canonical relationship consequence to Amara rather than inventing a new resource.

### Canonical rule
`pred.food_stable` is true when `flag.food_logistics_stabilized` is active and no later explicit invalidation marker is active.

No `resource.food` may be introduced.

## E136 — Frozen Road

### Required bridge
The two outcomes must establish a durable transport state:
- public labor => `flag.transport_network_stable`;
- guild contract => `flag.transport_network_stable` plus `history.guild_transport_contract`.

If the route fails to restore the road, the canonical state must instead contain `flag.transport_disruption_active`.

### Clear rule
A later authored repair/road-opening outcome clears `flag.transport_disruption_active` and restores `flag.transport_network_stable`. Time alone does not clear the disruption.

## E144 — Guild Seat

### Required bridge
The constitutional representation choice that grants a guild political seat must explicitly establish:
- `history.guild_representation`.

The representation marker is an institutional fact and must not be inferred from `rel.ivo`.

## E148 — Last Coalition Meeting

### Required bridge
E148-A establishes:
- `history.cross_faction_package`;
- `thread.coalition`;
- the identities of participating factions/routes.

E148-B establishes selective coalition state and must not qualify as full coalition cooperation.

## E194 — Guild Convoy

### Required bridge
E194-A (neutral inspectors) establishes:
- `history.guild_logistics_cooperation`;
- `thread.ivo_market` remains active where appropriate.

E194-B establishes only `guild_convoy_immunity` and political-risk consequences; it does not establish cooperation.

## E195 — Border Refugees

### Required bridge
The upstream border escalation event must establish:
- `flag.border_crisis_declared`;
- `thread.border_crisis`.

E195-A (admit and shelter) records the humanitarian response and may establish `history.border_crisis_response_shelter`.

E195-B records closure and may establish `history.border_crisis_response_closed`.

Resolution of the border crisis must be authored explicitly later; neither E195 choice automatically means that the crisis never existed.

## E200 — Merchant Oath

### Required bridge
`pred.guild_influence_strong` requires independent institutional guild outcomes. Minimum candidate inputs:
1. `history.guild_representation`;
2. one independent commercial/institutional outcome such as `guild_binding_seat`, `guild_tribunal_independent`, durable logistics cooperation, or market/credit leverage.

Final threshold must be frozen after source/balance QA.

`rel.ivo` alone is never sufficient.

## E207 — Founder Question

### Required bridge
`pred.systemic_explanation_verified` requires distinct evidence classes:
- warehouse/financial evidence;
- document/language evidence;
- witness/organizational evidence;
- explicit convergence decision.

A raw number of flags is insufficient. E207 consumes this verified state and must not create it implicitly.

## E209 — Dawn Charter

### Required bridge
Before E209 becomes eligible, the run must have durable evidence for:
- civic/commons legitimacy;
- institutional/audit legitimacy;
- faction/house/guild representation;
- applicable military/security constitutional route;
- information/evidence legitimacy;
- coalition cooperation;
- no unresolved mandatory crisis blocker.

`pred.final_charter_prerequisites` is therefore a package predicate consumed by E209, not a value produced by E209.

## E210 — Last Decision Is Not a Choice

E210 remains convergence-only. It may evaluate already-established ending qualification facts, but it may not manufacture missing route evidence, retroactively create coalition cooperation, or directly assign an ending from an unverified predicate.

## QA gate

These corrections are now frozen as the authoritative patch specification. The underlying expansion catalogs remain marked pending until the exact event prose is reconciled against this register and the complete E01–E270 producer/consumer inventory is rerun.
