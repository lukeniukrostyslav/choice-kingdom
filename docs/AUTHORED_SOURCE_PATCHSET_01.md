# Choice Kingdom — Authored Source Patchset 01

Date: 2026-09-15
Status: SOURCE PATCH SPEC — MUST BE APPLIED TO AUTHORITATIVE EVENT CATALOG

This patchset converts the previously identified P0 producer gaps into exact authored event blocks. It intentionally does not invent runtime behavior.

## 1. E136 — Frozen Road

Replace E136 with:

### E136 — The Frozen Road
**Trigger:** canonical winter-severity condition.
A blocked road isolates three villages. The repair choice creates a durable transport state; it does not create a border or food crisis by itself.
- **A — Open a public labor effort:** -4 gold, +5 trust; `roads_public_labor`, `transport_network_stable`; clears `transport_disruption_active` if currently active.
- **B — Contract guild transport:** -2 gold, +2 Ivo, +3 security; `roads_guild_contract`, `transport_network_stable`; clears `transport_disruption_active` if currently active.

## 2. E144 — Guild representation

Replace the trigger with canonical producer wording:

### E144 — The Guild Seat
**Trigger:** `history.guild_representation` established by the preceding guild-representation route.
The guild's first representative asks whether a merchant can hold a judicial office.
- **A — Separate commerce from judges:** +4 trust, -2 Ivo; `guild_judicial_separation`.
- **B — Permit it under disclosure rules:** +3 Ivo, +2 power, -3 trust; `guild_binding_commercial_access`.

## 3. E148 — Cross-faction package

Replace the authored outcome with:

### E148 — The Last Coalition Meeting
**Trigger:** E146 or a canonical cross-faction route.
Mara, Rowan, Seris, Ivo, Amara and Toma each demand one guarantee.
- **A — Build a package with mutual concessions:** -3 power, +7 trust; `history.cross_faction_package`, `thread.coalition`; records participating faction identities in the package.
- **B — Choose only the strongest allies:** +4 power, +2 security, -5 trust; `selective_coalition`; no coalition-cooperation qualification.

## 4. E192 — Broken Cart

Replace the undefined food-resource effect:

### E192 — The Broken Cart
**Trigger:** canonical `pred.transport_disruption` / road-pressure route.
A single broken cart delays medicine and grain simultaneously.
- **A — Prioritize medicine:** +4 trust; `food_logistics_unstable`; Amara relationship worsens; establishes no numeric food resource.
- **B — Prioritize grain:** `food_logistics_stabilized`; Amara relationship worsens; establishes no numeric food resource.

`pred.food_stable` is true only when `food_logistics_stabilized` is active and no explicit invalidation marker is active.

## 5. E194 — Guild Convoy

Replace with:

### E194 — The Guild Convoy
**Trigger:** `thread.ivo_market` plus a canonical guild logistics route.
Merchants offer a convoy but request immunity from certain inspections.
- **A — Accept with neutral inspectors:** +4 trust, +2 Ivo; `history.guild_logistics_cooperation`, `guild_convoy_neutral_inspection`.
- **B — Grant immunity:** +5 gold, -5 trust; `guild_convoy_immunity`; does not establish guild logistics cooperation.

## 6. Border-crisis declaration

The first event in the border-escalation chain must use this exact bridge:

`border_crisis_declared`, `thread.border_crisis`, `transport_or_border_pressure_active`.

A later successful resolution must use:

`border_crisis_resolved`, clear `border_crisis_declared`, clear the active border-crisis marker.

Security score alone never produces or clears the crisis.

## 7. E200 — Merchant Oath

Replace the trigger with a frozen institutional combination rule:

### E200 — The Merchant Oath
**Trigger:** `pred.guild_influence_strong`.
Major merchants are asked to swear that contracts cannot buy political office.
- **A — Accept the restriction:** +5 trust, -3 Ivo; `merchant_political_separation`.
- **B — Permit influence with disclosure:** +4 Ivo, +3 gold, -4 trust; `merchant_influence_disclosed`.

`pred.guild_influence_strong` requires at least two distinct institutional domains from:
1. `history.guild_representation`;
2. `guild_binding_seat`;
3. `guild_tribunal_independent` or another durable tribunal outcome;
4. market/credit institutional leverage;
5. `history.guild_logistics_cooperation`.

`rel.ivo` alone is never sufficient.

## 8. E207 — Founder Question

Replace the trigger with explicit evidence convergence:

### E207 — The Founder Question
**Trigger:** `pred.systemic_explanation_verified` AND `pred.coalition_cooperation`.
The player is offered a chance to become the indispensable founder of the new order.
- **A — Refuse permanent personal authority:** +7 trust, -4 power; `founder_authority_refused`.
- **B — Accept founder authority:** +6 power, -6 trust; `founder_authority_accepted`.

`pred.systemic_explanation_verified` requires distinct evidence IDs covering warehouse/financial evidence, document/language evidence, and witness/organizational evidence, followed by an explicit convergence choice. Raw evidence count is insufficient.

## 9. E197 — Succession Test

Freeze `pred.constitutional_prepared_strong` as an upstream condition:

It requires three independent domains before E197:
- civic/commons legitimacy;
- audit/institutional legitimacy;
- factional/constitutional or military legitimacy.

No E197–E210 outcome, ending state, or E210 convergence result may satisfy this predicate retroactively.

## 10. E209 — Dawn Charter

Freeze the trigger as `pred.final_charter_prerequisites`.

That predicate must already contain:
- civic/commons legitimacy;
- audit/institutional legitimacy;
- faction/house/guild representation;
- military/security constitutional route where applicable;
- information/evidence legitimacy;
- `pred.coalition_cooperation`;
- no unresolved mandatory crisis blocker.

E209 consumes this state. It does not manufacture missing prerequisites.

## 11. E210 — Last Decision

Keep E210 convergence-only. It may resolve ending qualification from already-established canonical state but must never manufacture a missing producer or prerequisite.

## 12. Producer closure requirement

After applying this patchset to the authoritative catalog, rerun:
- producer → consumer inventory;
- event-ID reconciliation;
- graph ↔ catalog reconciliation;
- trigger normalization;
- reachability pre-audit;
- contradiction/duplicate semantic audit.

Until those checks pass, P0 producer closure remains OPEN and production schema/engine work must not be declared ready.
