# Choice Kingdom — Scenario QA S05 E151–E210 Inventory

Scope: frozen production candidates E151–E210. Source: `docs/EVENT_CATALOG_EXPANSION_151_210.md`, blob SHA `69013de34f2d2436f8d3483b014821afa05fa75e`.

This is a direct source inventory, not proof of runtime reachability.

## E151–E180 — primary authored nodes

| Event | Trigger | Authored outputs / effects |
|---|---|---|
| E151 | `auditor_independence` or `audit_office` | `clerks_oath_public` / `clerks_oath_private`; trust/power |
| E152 | document audit route | `unsigned_decree_void` / `unsigned_decree_accepted`; trust/power |
| E153 | `office_network_mapped` | `archive_access_shared` / `archive_access_restricted`; gold/power/security/trust |
| E154 | `auditor_independence` + institutional trust | `crown_audited` / `crown_exempt_from_audit`; trust/power |
| E155 | `crown_audited` | `full_crown_audit_published` / `audit_summary_only`; trust/reputation |
| E156 | high trust or civic relief | `requisition_compensation` / `requisition_tax_credit`; gold/income/trust |
| E157 | food shortage | `public_mill_trust` / `mill_guild_sale`; gold/trust/Ivo |
| E158 | `schoolhouse_vote` or high civic trust | `night_school_funded` / `guild_night_school`; gold/trust/Ivo |
| E159 | `tax_transparency` or `clerks_oath_public` | `law_notices_public` / `law_notices_local`; gold/trust/power |
| E160 | severe winter | `winter_rent_ceiling` / `heating_vouchers`; trust/gold |
| E161 | Seris route | `house_assembly` / `crown_confiscation_power`; Seris/trust/power |
| E162 | `equal_estate_law` or `house_assembly` | `estate_map_audit` / `targeted_estate_audit`; trust/Seris/power |
| E163 | Seris evidence route | `family_seal_testimony` / `family_seal_protected`; power/Seris/trust |
| E164 | high noble influence + low security | `private_army_rejected` / `private_army_licensed`; trust/Seris/security/power |
| E165 | guild leverage | `official_credit_disclosure` / `private_credit_protected`; trust/Ivo/gold |
| E166 | strong market oversight + merchant charter | `audited_monopoly` / `monopoly_broken_on_principle`; gold/trust |
| E167 | `free_grain_imports` | `import_risk_guarantee` / `import_risk_refused`; gold/trust/power |
| E168 | `guild_whistleblower` or `public_trade_standards` | `guild_tribunal_independent` / `guild_tribunal_controlled`; trust/Ivo/gold |
| E169 | guild labor tension | `apprentice_safety_law` / `apprentice_strike_broken`; trust/Ivo/security |
| E170 | veteran patronage or border pressure | `veteran_fortification_wages` / `veteran_land_grants`; gold/security/trust/Rowan |
| E171 | `frontier_military_watch` or military route | `border_public_trial` / `military_border_trial`; trust/security |
| E172 | border tension | `civilian_signal_authority` / `military_signal_control`; trust/security |
| E173 | low army readiness | `barracks_rebuilt` / `barracks_shelter`; gold/security/trust |
| E174 | Amara >= 1 | `lantern_universal_pass` / `lantern_local_approval`; trust/Amara/power |
| E175 | winter illness | `humane_quarantine` / `hard_quarantine`; gold/trust/security |
| E176 | `humane_quarantine` or strong Amara route | `medical_requisition_inquiry` / `medical_testimony_suppressed`; trust/security/Amara |
| E177 | Toma >= 1 | `licensed_courier_network` / `courier_surveillance`; Toma/trust/security |
| E178 | information route | `unsent_letter_traced` / `unsent_letter_replaced`; power/Toma/trust |
| E179 | low information trust | `verified_market_notices` / `rumor_sellers_punished`; trust/power/security |
| E180 | protected-source route | `informant_family_relocated` / `informant_guard`; gold/trust/security |

## E181–E185 — delayed callbacks

| Event | Trigger / timing | Authored outputs |
|---|---|---|
| E181 | 5+ turns after toll concession | `toll_terms_enforced` / `toll_escalation_sold` |
| E182 | `veteran_patronage`, 4+ turns | `veteran_positions_examined` / `veteran_positions_granted` |
| E183 | `estate_exception`, 5+ turns | `exception_precedent_closed` / `exception_precedent_extended` |
| E184 | secret evidence route, 4+ turns | `quiet_evidence_published` / `quiet_evidence_kept` |
| E185 | `cheap_weapons` + later military crisis | `steel_failure_prevented` / `steel_failure_delayed`; delayed loss on B |

## E186–E190 — replay/information nodes

| Event | Trigger | Authored outputs |
|---|---|---|
| E186 | `warehouse_arson` or replay informational unlock | `warehouse_second_box` / `warehouse_fire_focus` |
| E187 | multiple evidence fragments | `payment_date_crosscheck` / `payment_omission_assumed` |
| E188 | `emergency_language_compared` | `necessity_phrase_history` / `necessity_phrase_dismissed` |
| E189 | conflicting testimony recorded | `witness_reopened` / `witness_new_lead_only` |
| E190 | office network mapped | `beneficiary_network_followed` / `formal_responsibility_only` |

## E191–E195 — crisis escalation

| Event | Trigger | Authored outputs |
|---|---|---|
| E191 | unresolved warehouse/market crisis | `warehouse_crisis_people_first` / `warehouse_crisis_evidence_first` |
| E192 | `pred.transport_disruption` | `food_logistics_unstable` / `food_logistics_stabilized`; both affect downstream routes |
| E193 | low gold + high security | `civilian_bread_shared` / `military_bread_reserved` |
| E194 | `history.guild_logistics_cooperation` | A repeats cooperation marker + `guild_neutral_inspectors`; B `guild_convoy_immunity` + `guild_logistics_immunity_risk` |
| E195 | `pred.border_crisis` | `refugee_shelter` / `border_closed` |

E194 has an explicit hard-negative rule: it must not self-produce `pred.guild_logistics_cooperation`; the qualified predicate requires the upstream cooperation marker, neutral inspectors, and absence of unresolved immunity risk.

## E196–E210 — constitutional/endgame nodes

| Event | Trigger | Authored outputs / contract |
|---|---|---|
| E196 | late constitutional route | `five_questions_public` / `five_questions_private` |
| E197 | `pred.constitutional_prepared_strong` | `emergency_powers_expire` / `emergency_powers_inherit` |
| E198 | audit reform | `legislative_budget_lock` / `executive_budget_override_retained` |
| E199 | military constitutional route | `army_constitution_oath` / `army_crown_oath` |
| E200 | `pred.guild_influence_strong` | `merchant_political_separation` / `merchant_influence_disclosed` |
| E201 | `pred.coalition_cooperation` | `coalition_renegotiated` / `coalition_shortfall_hidden` |
| E202 | `history.house_assembly` | `noble_veto_rejected` / `noble_limited_veto` |
| E203 | `history.guild_representation` | `guild_advisory_seat` / `guild_binding_seat` |
| E204 | `thread.military_constitutional` | `military_constitutional_refusal` / `military_crown_obedience` |
| E205 | `thread.amara_civic` | `medical_neutrality_protected` / `medical_neutrality_overridden` |
| E206 | `thread.toma_information` | `press_protection` / `emergency_censorship` |
| E207 | `pred.systemic_explanation_verified` + `pred.coalition_cooperation` | founder authority accept/refuse; requires distinct evidence domains + explicit convergence |
| E208 | `thread.final_constitutional_phase` | `empty_chair_memorial` / `permanent_emergency_chair` |
| E209 | `pred.final_charter_prerequisites` | `charter_publicly_ratified` / `charter_council_ratified`; explicit multi-domain prerequisite contract |
| E210 | `thread.endgame_convergence` | convergence-only; must not create missing prerequisites or route qualification |

## QA findings from S05 inventory

1. **Delayed lifecycle remains open:** E181–E185 have authored source identity, but exact callback identity, persistence, ordering, cancellation/supersession and exactly-once semantics remain S10 gates.
2. **Replay boundary remains open:** E186 is explicitly replay-aware; exact `meta.*` producer/key closure remains S11 work. E187–E190 are ordinary information callbacks unless later contracts promote them to meta state.
3. **Qualified predicate hard negatives are explicit:** E194 cannot self-satisfy `pred.guild_logistics_cooperation`; E197 cannot self-create `pred.constitutional_prepared_strong`; E201/E207 cannot manufacture coalition cooperation; E209 cannot manufacture its own prerequisites; E210 cannot invent missing route qualification.
4. **E192 is a state-convergence hazard:** both branches mutate logistics state without a conventional named flag schema. The machine contract must distinguish direct state mutation from predicate production.
5. **E199 preserves the military constitutional domain:** `army_constitution_oath` and `army_crown_oath` are explicit outputs; the stronger constitutional qualification must not be inferred from E199 alone.
6. **E207 has explicit multi-domain qualification text:** one evidence domain is insufficient; warehouse/financial, document/language, witness/organizational and explicit convergence evidence are distinct requirements.
7. **E209 has explicit prerequisite domains:** civic legitimacy, institutional/audit legitimacy, faction representation, military/security constitutional route, information/evidence legitimacy, coalition cooperation, and no mandatory crisis blocker.
8. **E210 is convergence-only:** it is not a producer of missing ending prerequisites.

## S05 status
Direct source inventory is complete for E151–E210. Semantic/machine closure, delayed contracts, replay keys, ending precedence and reachability remain open.

**S05: 60% / IN PROGRESS.** No global Scenario QA percentage increase is claimed from this inventory alone.
