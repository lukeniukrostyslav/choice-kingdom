# Choice Kingdom — Producer Audit E111–E180 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — VERIFIED SUBSET**
Scope: exact durable outputs in E111–E180 that are directly visible in the authoritative authored catalog. This is not an engine-input artifact and does not infer missing producers.

## Verified durable producers

| Event | Choice | Exact durable output(s) | Downstream role | Status |
|---|---|---|---|---|
| E111 | A | `local_recall_allowed` | civic participation / later local-governance routes | VERIFIED |
| E111 | B | `royal_review_required` | centralized local governance | VERIFIED |
| E112 | A | `bread_records_public` | evidence / food-policy transparency | VERIFIED |
| E112 | B | `bread_records_private` | weaker later evidence | VERIFIED |
| E113 | A | `verified_names_policy` | controlled attribution | VERIFIED |
| E113 | B | `broad_accusations` | reputation / retaliation risk | VERIFIED |
| E114 | A | `local_budget_vote` | E122 commons route | VERIFIED |
| E114 | B | `central_budget_control` | centralized budget route | VERIFIED |
| E115 | A | `tax_audit_first` | institutional response to tax refusal | VERIFIED |
| E115 | B | `tax_enforcement` | security / treasury route | VERIFIED |
| E116 | A | `auditor_apprentices` | E134/E142 audit route | VERIFIED |
| E116 | B | `palace_auditors` | palace-controlled audit route | VERIFIED |
| E117 | A | `veterans_examined` | civil-service military route | VERIFIED |
| E117 | B | `veteran_patronage` | E182 delayed veteran callback | VERIFIED |
| E118 | A | `equal_estate_law` | E162 noble investigation | VERIFIED |
| E118 | B | `estate_exception` | E127/E183/E242 delayed precedent route | VERIFIED |
| E119 | A | `guild_whistleblower` | E168 tribunal route | VERIFIED |
| E119 | B | `guild_internal_review` | internal guild route | VERIFIED |
| E120 | A | `lanterns_protected` | civic/Amara institutional route | VERIFIED |
| E120 | B | `lanterns_dependent` | dependency on Crown grants | VERIFIED |
| E121 | A | `protected_sources` | Toma/source-protection route | VERIFIED |
| E121 | B | `named_sources_only` | information-control route | VERIFIED |
| E122 | A | `tax_transparency` | E159/E203-style institutional transparency | VERIFIED |
| E122 | B | `tax_private_bargain` | private political bargain | VERIFIED |
| E123 | A | `noble_grain_public` | public food distribution | VERIFIED |
| E123 | B | `noble_grain_private` | private noble relief | VERIFIED |
| E124 | A | `public_trade_standards` | E168 commercial tribunal trigger | VERIFIED |
| E124 | B | `guild_trade_standards` | guild-controlled standards | VERIFIED |
| E125 | A | `border_compensation` | border legitimacy / compensation | VERIFIED |
| E125 | B | `border_tax_exemption` | border fiscal concession | VERIFIED |
| E126 | A | `river_compact` | E224 river consequence | VERIFIED |
| E126 | B | `royal_toll_office` | centralized toll route | VERIFIED |
| E127 | A | `privilege_renewal_refused` | delayed noble-precedent closure | VERIFIED |
| E127 | B | `privilege_renewed_again` | delayed noble-precedent extension | VERIFIED |
| E128 | A | `steel_replaced` | security consequence | VERIFIED |
| E128 | B | `steel_repaired` | security / Rowan consequence | VERIFIED |
| E129 | A | `festival_reported` | transparency route | VERIFIED |
| E129 | B | `festival_secret` | secrecy / legitimacy route | VERIFIED |
| E130 | A | `infrastructure_concession`-related resolution | toll consequence | **SOURCE REVIEW NEEDED** |
| E131 | A | `emergency_language_compared` | E188 repeated-phrase investigation | VERIFIED |
| E131 | B | `precedent_ignored` | replay/information divergence | VERIFIED |
| E132 | A | `redaction_reconstructed` | evidence chain | VERIFIED |
| E132 | B | `uncertainty_preserved` | uncertainty/reputation route | VERIFIED |
| E133 | A | `form_pattern_tested` | systemic-vs-mastermind investigation | VERIFIED |
| E133 | B | `pattern_arrest` | single-coordinator theory | VERIFIED |
| E134 | A | `office_network_mapped` | E153/E190 investigation route | VERIFIED |
| E134 | B | `map_destroyed_after_copy` | secrecy route | VERIFIED |
| E135 | A | `conflicting_testimony_recorded` | E189 witness callback | VERIFIED |
| E135 | B | `clean_testimony_selected` | evidence-selection route | VERIFIED |
| E136 | A | `transport_network_stable`, clears `transport_disruption_active` | recovery/clear | VERIFIED |
| E136 | B | `transport_network_stable`, clears `transport_disruption_active`, `roads_guild_contract`, `history.guild_logistics_cooperation` | recovery + guild logistics source | VERIFIED |
| E137 | A | `civilian_watch_training` | civic security | VERIFIED |
| E137 | B | `royal_patrol_expansion` | security route | VERIFIED |
| E138 | A | `grain_recount` | food evidence / reserve verification | VERIFIED |
| E138 | B | `targeted_grain_recount` | targeted food evidence | VERIFIED |
| E139 | A | `frontier_lantern_network` | border-warning infrastructure | VERIFIED |
| E139 | B | `frontier_military_watch` | military border route | VERIFIED |
| E140 | A | `trade_risk_insurance` | E220 delayed economic consequence | VERIFIED |
| E140 | B | `market_self_adjustment` | market policy route | VERIFIED |
| E141 | A | `emergency_public_vote` | constitutional restraint | VERIFIED |
| E141 | B | `emergency_council_renewal` | emergency normalization risk | VERIFIED |
| E142 | A | `auditor_independence` | E154 audit-of-Crown route | VERIFIED |
| E142 | B | `auditor_crown_control` | executive audit control | VERIFIED |
| E143 | A | reserve budget publication | military transparency | **DURABLE TOKEN NAME REVIEW NEEDED** |
| E143 | B | classified reserve budget | military secrecy | **DURABLE TOKEN NAME REVIEW NEEDED** |
| E144 | A/B | `history.guild_representation` | E203+ | VERIFIED |
| E145 | A/B | constitutional convergence outputs | E213/E260 candidates | **SOURCE REVIEW NEEDED** |
| E146 | A/B | coalition package/signature outputs | E149/E201 | **SOURCE REVIEW NEEDED** |
| E147 | A/B | constitutional preparation outputs | E265 | **SOURCE REVIEW NEEDED** |
| E148 | A/B | `history.cross_faction_package` plus route-specific package semantics | E149/E201/E261+ | VERIFIED |
| E149 | A/B | coalition decision outputs | E216/E263 candidates | **SOURCE REVIEW NEEDED** |
| E150 | A/B | final constitutional preparation outputs | E256/E257 candidates | **SOURCE REVIEW NEEDED** |
| E151 | A/B | `clerks_oath_public` / `clerks_oath_private` | E154/E159/E211 | VERIFIED |
| E152 | A/B | `unsigned_decree_void` / `unsigned_decree_accepted` | constitutional legality | VERIFIED |
| E153 | A/B | `archive_access_shared` / `archive_access_restricted` | E190 archive/network route | VERIFIED |
| E154 | A/B | `crown_audited` / `crown_exempt_from_audit` | E155 / institutional endgame | VERIFIED |
| E155 | A/B | `full_crown_audit_published` / `audit_summary_only` | E211 public ledger route | VERIFIED |
| E156 | A/B | `requisition_compensation` / `requisition_tax_credit` | E245 callback / civic legitimacy | VERIFIED |
| E157 | A/B | `public_mill_trust` / `mill_guild_sale` | food/economic governance | VERIFIED |
| E158 | A/B | `night_school_funded` / `guild_night_school` | civic/guild route | VERIFIED |
| E159 | A/B | `law_notices_public` / `law_notices_local` | E215 / public-law route | VERIFIED |
| E160 | A/B | `winter_rent_ceiling` / `heating_vouchers` | E221 / winter callback | VERIFIED |
| E161 | A/B | `history.house_assembly` / `crown_confiscation_power` | E162/E202/E261+ | VERIFIED |
| E162 | A/B | `estate_map_audit` / `targeted_estate_audit` | noble investigation | VERIFIED |
| E163 | A/B | `family_seal_testimony` / `family_seal_protected` | evidence / Seris route | VERIFIED |
| E164 | A/B | `private_army_rejected` / `private_army_licensed` | security/noble route | VERIFIED |
| E165 | A/B | `official_credit_disclosure` / `private_credit_protected` | E187/E217/E269 economic evidence | VERIFIED |
| E166 | A/B | `audited_monopoly` / `monopoly_broken_on_principle` | market oversight | VERIFIED |
| E167 | A/B | `import_risk_guarantee` / `import_risk_refused` | food/market route | VERIFIED |
| E168 | A/B | `guild_tribunal_independent` / `guild_tribunal_controlled` | guild institutional route | VERIFIED |
| E169 | A/B | `apprentice_safety_law` / `apprentice_strike_broken` | guild labor route | VERIFIED |
| E170 | A/B | `veteran_fortification_wages` / `veteran_land_grants` | E182/E240 security route | VERIFIED |
| E171 | A/B | `border_public_trial` / `military_border_trial` | border legitimacy | VERIFIED |
| E172 | A/B | `civilian_signal_authority` / `military_signal_control` | border-warning route | VERIFIED |
| E173 | A/B | `barracks_rebuilt` / `barracks_shelter` | security/civic route | VERIFIED |
| E174 | A/B | `lantern_universal_pass` / `lantern_local_approval` | Amara civic route | VERIFIED |
| E175 | A/B | `humane_quarantine` / `hard_quarantine` | E176 / medical legitimacy | VERIFIED |
| E176 | A/B | `medical_requisition_inquiry` / `medical_testimony_suppressed` | evidence/Amara route | VERIFIED |
| E177 | A/B | `licensed_courier_network` / `courier_surveillance` | E178/E180 information route | VERIFIED |
| E178 | A/B | `unsent_letter_traced` / `unsent_letter_replaced` | document-tracing route | VERIFIED |
| E179 | A/B | `verified_market_notices` / `rumor_sellers_punished` | information/market route | VERIFIED |
| E180 | A/B | `informant_family_relocated` / `informant_guard` | witness protection | VERIFIED |

## Important non-closure findings

- E136 proves recovery/clear semantics for `transport_disruption_active`; it does **not** identify a later active-disruption producer.
- E138 proves grain recount outcomes but does not by itself establish `pred.food_stable`.
- E167 proves import-risk outcomes but does not by itself establish `pred.food_stable`.
- E194's qualified guild-logistics predicate remains dependent on the upstream E136-B marker plus neutral inspection and absence of immunity risk.
- Relationship values remain numeric state, not substitutes for route predicates.
- The E143–E150 section requires another direct source pass before those outputs can be used to close endgame predicates.

## Gate

This audit increases source-level producer coverage only. It does not freeze the production schema and does not imply runtime reachability.
