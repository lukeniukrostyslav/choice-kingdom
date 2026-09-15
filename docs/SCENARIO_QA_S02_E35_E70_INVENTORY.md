# Choice Kingdom — Scenario QA S02: E35–E70 Inventory

Date: 2026-09-15
Scope: E35–E70
Status: **IN PROGRESS — 70%, NOT CLOSED**

## Purpose

Direct source inventory for S02. The authoritative source is `docs/EVENT_CATALOG_ACT_V_EXPANSION.md`. This is a static QA artifact, not runtime implementation.

## Event inventory

| Event | Trigger | Outputs / ending state | Delayed / downstream | Status |
|---|---|---|---|---|
| E35 | E33 resolved | `emergency_expiry_announced` / `emergency_expiry_flexible` | ordinary-procedure recovery vs normalization of emergency rule | VERIFIED SOURCE |
| E36 | Mara <= -1 or emergency powers + weak audit | `mara_independent_mandate` / `mara_resigned` | institutional-ending effects | VERIFIED SOURCE |
| E37 | Rowan >=1 or military crisis | `army_law_oath` / `army_crown_oath` | Iron Crown pressure from crown oath | VERIFIED SOURCE |
| E38 | Seris >=0 | `hereditary_seats_limited` / `hereditary_seats_rejected` | constitutional bargaining | VERIFIED SOURCE |
| E39 | Ivo >=1 + treasury pressure | `guild_emergency_credit` / `civic_war_bonds` | commercial leverage / distributed-power effects | VERIFIED SOURCE |
| E40 | winter mortality risk or Amara >=1 | `local_relief_councils` / `central_relief` | relief resilience / administrative fragility | VERIFIED SOURCE |
| E41 | Toma recruited + investigation route | `crate_route_traced` / `customs_accused` | intermediary investigation / scapegoat risk | VERIFIED SOURCE |
| E42 | `crate_route_traced` or `seris_witness` | `witness_protected` / `witness_public` | testimony durability / credibility attack | VERIFIED SOURCE |
| E43 | two+ investigation sources agree | `ledger_network_public` / `ledger_network_compromised` | legitimacy vs institutional repair | VERIFIED SOURCE |
| E44 | `seris_witness` or `seris_exposed` | `houses_self_reconcile` / `house_arms_restricted` | faction stability | VERIFIED SOURCE |
| E45 | `public_bridge` or repeated toll policy | `public_infrastructure_trust` / `infrastructure_concession` | bridge ownership callback | VERIFIED SOURCE |
| E46 | `army_law_oath` + emergency crisis | `lawful_refusal_defended` / `lawful_refusal_punished` | constitutional/military legitimacy | VERIFIED SOURCE |
| E47 | E35–E46 milestone + 3 factions active | `constitution_first` / `crown_powers_first` | E48 / constitutional routes | VERIFIED SOURCE |
| E48 | `constitution_first` | `permanent_emergency_blocked` / `emergency_renewal_possible` | emergency permanence semantics | VERIFIED SOURCE |
| E49 | `guild_emergency_credit` or strong Ivo | `guild_political_representation` / `guild_political_exclusion` | commercial power center | VERIFIED SOURCE |
| E50 | `people_heard` or relief councils + high trust | `people_charter_endorsed` / `people_charter_delayed` | People's Charter ending | VERIFIED SOURCE |
| E51 | E47 complete | `mutual_veto` / `crown_veto` / `public_renewal_rule` | constitutional veto structure | VERIFIED SOURCE |
| E52 | Rowan arc active | `military_audit_final` / `military_patronage_final` | army institutional route | VERIFIED SOURCE |
| E53 | audit route or `ledger_network_public` | `full_ledger_published` / `verified_ledger_only` | truth/legitimacy ending effects | VERIFIED SOURCE |
| E54 | Seris arc active | `seris_constitutional_office` / `nobility_equal_under_law` | faction cooperation / equality | VERIFIED SOURCE |
| E55 | Ivo arc active | `guild_books_submitted` / `guild_books_sealed` | evidence vs private leverage | VERIFIED SOURCE |
| E56 | Amara arc active | `relief_guarantee` / `relief_discretion` | welfare policy / budget consequences | VERIFIED SOURCE |
| E57 | Toma recruited or street route | `systemic_corruption_confirmed` / `mastermind_hunt` | systemic vs personal conspiracy interpretation | VERIFIED SOURCE |
| E58 | unresolved severe crisis | `final_emergency_invoked` / `final_emergency_refused` | final crisis resolution | VERIFIED SOURCE |
| E59 | final emergency resolved | `mandate_renewed_legally` / `succession_limited` | succession/legitimacy | VERIFIED SOURCE |
| E60 | final constitutional conditions | `all_voices_heard` / `crown_decides_alone` | final decision framing | VERIFIED SOURCE |
| E61 | strong institutions + no permanent emergency + stable security | `STEWARD` ending | ending resolution | VERIFIED SOURCE |
| E62 | `emergency_power` + military dependency + `crown_powers_first` or repeated emergency | `IRON_CROWN` ending | ending resolution | VERIFIED SOURCE |
| E63 | strong treasury + commercial leverage + guild representation | `GOLDEN_COMPACT` ending | ending resolution | VERIFIED SOURCE |
| E64 | high trust + `people_charter_endorsed` + distributed institutions | `PEOPLES_CHARTER` ending | ending resolution | VERIFIED SOURCE |
| E65 | multiple unresolved crises + collapsed institutions + no settlement | `BROKEN_DIADEM` ending | ending resolution | VERIFIED SOURCE |
| E66 | strong personal survival + withdrawal + low institutional ambition | `QUIET_THRONE` ending | ending resolution | VERIFIED SOURCE |
| E67 | `constitutional_limit` + ledger truth + cross-faction cooperation + redesign + no permanent emergency | `SECOND_FOUNDER` ending | ending resolution | VERIFIED SOURCE |
| E68 | any ending | historical interpretation callback | replay/history interpretation | VERIFIED SOURCE |
| E69 | `public_infrastructure_trust` or `infrastructure_concession` | bridge-ownership callback | civic identity callback | VERIFIED SOURCE |
| E70 | investigation ending route | archive ledger callback | investigation-heavy replay reward | VERIFIED SOURCE |

## Direct semantic findings

### A. E61–E67 are ending consumers, not independent producers

The ending nodes consume previously authored state and resolve one of seven ending families. They must not be treated as producers of their own qualifying prerequisites.

### B. Existing cross-batch prerequisites are valid consumers

- E62 consumes `emergency_power`, authored earlier in E33.
- E67 consumes `constitutional_limit`, authored earlier in E33.
- E64 consumes `people_heard`, authored earlier in E34.
- E45 consumes `public_bridge`, authored earlier in E18.
- E42 consumes `seris_witness`, authored earlier in E26.

These are intentionally cross-catalog dependencies, not undefined producers.

### C. Branch pairs are generally mutually exclusive

E35–E60 use A/B (and E51 A/B/C) alternatives. Identical field names are not duplicated where branches represent alternative values or mutually exclusive choices. The final S08 global audit must still detect any semantic collisions across the entire catalog.

### D. No direct duplicate flag writer is claimed closed by this batch

The S02 source inventory is complete at event/trigger/output level, but the global semantic-writer gate remains open. A dedicated duplicate/contradiction scan across E35–E70 plus cross-catalog consumers is still required before S02 can be closed.

### E. Potential contract-sensitive trigger phrases

The following triggers require canonical machine contracts later and must not be implemented as free-form prose predicates:

- "treasury pressure"
- "winter mortality risk"
- "strong Ivo relationship"
- "two or more investigation sources agree"
- "at least three factions active"
- "strong institutions"
- "stable security"
- "military dependency"
- "distributed institutions"
- "cross-faction cooperation"
- "institutional redesign"
- "strong personal survival"
- "low institutional ambition"

These are not declared defects yet; they are contract-closure targets for the predicate and engine phases.

## S02 gate result

- Trigger inventory: **VERIFIED SOURCE-LEVEL**.
- Concrete output inventory: **VERIFIED SOURCE-LEVEL**.
- Cross-batch producer/consumer references: **IDENTIFIED**.
- Delayed/callback inventory: **VERIFIED SOURCE-LEVEL, runtime contract open**.
- Duplicate/contradictory writer closure: **OPEN**.
- Machine predicate normalization: **OPEN**.

**S02 progress: 70% — not complete.**

No global Scenario QA percentage increase is claimed from this inventory alone. Overall Scenario QA remains **65%** until the defined global gates are actually closed.
