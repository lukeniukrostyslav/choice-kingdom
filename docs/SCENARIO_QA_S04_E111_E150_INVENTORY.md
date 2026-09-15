# Choice Kingdom — Scenario QA S04: E111–E150 Inventory

Date: 2026-09-15  
Scope: E111–E150  
Status: **IN PROGRESS — 70%, NOT CLOSED**

## Purpose

Direct source inventory for E111–E150. Authoritative source: `docs/EVENT_CATALOG_EXPANSION_111_150.md`.

## Event inventory

| Event | Trigger | Outputs / state | Delayed / downstream | Status |
|---|---|---|---|---|
| E111 | high trust / `local_relief_councils` | `local_recall_allowed` / `royal_review_required` | civic participation / resentment | VERIFIED SOURCE |
| E112 | food-price pressure | `bread_records_public` / `bread_records_private` | evidence strength | VERIFIED SOURCE |
| E113 | `full_ledger_published` / `ledger_network_public` | `verified_names_policy` / `broad_accusations` | retaliation risk | VERIFIED SOURCE |
| E114 | `people_charter_endorsed` / high civic trust | `local_budget_vote` / `central_budget_control` | local governance | VERIFIED SOURCE |
| E115 | strong treasury pressure | `tax_audit_first` / `tax_enforcement` | trust/security effects | VERIFIED SOURCE |
| E116 | Mara >=1 / `mara_independent_mandate` | `auditor_apprentices` / `palace_auditors` | audit independence | VERIFIED SOURCE |
| E117 | Rowan >=1 | `veterans_examined` / `veteran_patronage` | border administration | VERIFIED SOURCE |
| E118 | Seris >=0 | `equal_estate_law` / `estate_exception` | legal equality / privilege | VERIFIED SOURCE |
| E119 | Ivo >=1 | `guild_whistleblower` / `guild_internal_review` | guild governance | VERIFIED SOURCE |
| E120 | Amara >=1 | `lanterns_protected` / `lanterns_dependent` | institutional independence | VERIFIED SOURCE |
| E121 | Toma route | `protected_sources` / `named_sources_only` | evidence access | VERIFIED SOURCE |
| E122 | `local_budget_vote` / `people_charter_endorsed` | `tax_transparency` / `tax_private_bargain` | fiscal legitimacy | VERIFIED SOURCE |
| E123 | noble cooperation + food shortage | `noble_grain_public` / `noble_grain_private` | faction legitimacy | VERIFIED SOURCE |
| E124 | commercial route | `public_trade_standards` / `guild_trade_standards` | market governance | VERIFIED SOURCE |
| E125 | strong security route | `border_compensation` / `border_tax_exemption` | border legitimacy | VERIFIED SOURCE |
| E126 | `public_infrastructure_trust` / `competitive_market` | `river_compact` / `royal_toll_office` | infrastructure governance | VERIFIED SOURCE |
| E127 | delayed after hereditary privilege | `privilege_renewal_refused` / `privilege_renewed_again` | delayed privilege lifecycle | VERIFIED SOURCE |
| E128 | `cheap_weapons`, delayed | `steel_replaced` / `steel_repaired` | military reliability | VERIFIED SOURCE |
| E129 | festival, delayed | `festival_reported` / `festival_secret` | civic memory | VERIFIED SOURCE |
| E130 | `infrastructure_concession`, delayed | choice effect without named flag | toll/royal revenue | VERIFIED SOURCE |
| E131 | replay callback | `emergency_language_compared` / `precedent_ignored` | replay information | VERIFIED SOURCE |
| E132 | secret evidence route | `redaction_reconstructed` / `uncertainty_preserved` | evidence graph | VERIFIED SOURCE |
| E133 | `mastermind_hunt` | `form_pattern_tested` / `pattern_arrest` | conspiracy interpretation | VERIFIED SOURCE |
| E134 | `auditor_apprentices` / Mara route | `office_network_mapped` / `map_destroyed_after_copy` | institutional evidence | VERIFIED SOURCE |
| E135 | `witness_protected` | `conflicting_testimony_recorded` / `clean_testimony_selected` | testimony quality | VERIFIED SOURCE |
| E136 | winter severity | `transport_network_stable`, clears `transport_disruption_active`; B also `history.guild_logistics_cooperation` | transport lifecycle / E194 qualification | VERIFIED SOURCE |
| E137 | low security | `civilian_watch_training` / `royal_patrol_expansion` | local security | VERIFIED SOURCE |
| E138 | food shortage | `grain_recount` / `targeted_grain_recount` | warehouse truth | VERIFIED SOURCE |
| E139 | border tension + Amara route | `frontier_lantern_network` / `frontier_military_watch` | warning infrastructure; not border-crisis producer | VERIFIED SOURCE |
| E140 | strong market oversight | `trade_risk_insurance` / `market_self_adjustment` | trade resilience | VERIFIED SOURCE |
| E141 | `emergency_renewal_possible`, delayed | `emergency_public_vote` / `emergency_council_renewal` | emergency authority | VERIFIED SOURCE |
| E142 | `auditor_apprentices` / `audit_office` | `auditor_independence` / `auditor_crown_control` | institutional authority | VERIFIED SOURCE |
| E143 | military audit route | reserve-budget policy outputs | emergency reserve semantics | VERIFIED SOURCE |
| E144 | `guild_political_representation` | canonical `history.guild_representation` on both branches + branch-specific policy flags | guild representation | VERIFIED SOURCE |
| E145 | `people_charter_endorsed` | `regional_courts` / `noble_courts_expanded` | judicial structure | VERIFIED SOURCE |
| E146 | 4+ character routes | `six_signatures_public` / `six_signatures_private` | coalition legitimacy | VERIFIED SOURCE |
| E147 | multiple strong relationships | `institutional_credit` / `heroic_reform_credit` | leadership attribution | VERIFIED SOURCE |
| E148 | E146 / strong cross-faction cooperation | `history.cross_faction_package` + `coalition_candidate_package` / `history.selective_coalition` + `selective_coalition` | coalition qualification | VERIFIED SOURCE |
| E149 | `history.cross_faction_package` | `coalition_cost_public` / `coalition_cost_hidden` | coalition durability | VERIFIED SOURCE |
| E150 | late constitutional preparation | `constitution_bad_ruler_test` / `constitution_good_ruler_model` | constitutional design | VERIFIED SOURCE |

## Direct semantic findings

### 1. Canonical marker reuse is intentional where explicitly documented

E136, E144 and E148 contain explicit canonical markers. In particular, E144 A/B intentionally converge on `history.guild_representation`, and E148 A intentionally creates `history.cross_faction_package`. These must not be reported as accidental duplicate writers merely because both branches write the same immutable marker.

### 2. E139 is not a border-crisis producer

The source explicitly states that E139 establishes frontier-warning infrastructure only. It must not be used as evidence that `pred.border_crisis` exists or is resolved.

### 3. E130 has branch effects without named state keys

E130's A/B choices produce immediate economic/relationship effects but no explicit flag. This is acceptable only if those effects are represented by canonical state mutations in the future engine contract. If downstream content needs to distinguish “ceiling enforced” from “revenue renegotiated”, explicit facts must be added.

### 4. E143 has unnamed outputs

E143's two choices change trust/security but define no explicit flag. The engine may model these as numeric state changes, but no hidden predicate should be inferred from prose such as “permanent emergency reserve”. If later events consume the reserve decision, a canonical flag/predicate is required.

### 5. Delayed events require exact timing contracts later

E127, E128, E129, E130 and E141 use explicit turn delays. Source closure is sufficient for this inventory, but exact callback identity, cancellation/supersession and exactly-once behavior remain S10 work.

### 6. Replay node E131 requires meta-state separation

E131 explicitly references prior-run information unavailable to the current save. It must consume a canonical `meta.*` key rather than a normal run-local flag. The producer/key pair remains an S11 closure item.

## S04 gate result

- Direct trigger inventory: **VERIFIED SOURCE-LEVEL**.
- Direct output/state inventory: **VERIFIED SOURCE-LEVEL**.
- Canonical cross-catalog markers: **IDENTIFIED**.
- Delayed/replay semantics: **IDENTIFIED; runtime contract open**.
- Duplicate/contradictory writer closure: **OPEN**.
- Predicate normalization: **OPEN**.

**S04 progress: 70% — not complete.**

No global Scenario QA percentage increase is claimed from this inventory alone.
