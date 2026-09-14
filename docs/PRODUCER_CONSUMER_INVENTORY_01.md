# Choice Kingdom — Producer / Consumer Inventory 01

Status: **PARTIAL VERIFIED INVENTORY — NOT PRODUCTION READY**
Scope verified in this pass: authored source excerpts E111–E190 and E211–E263; earlier spine/audit material remains separate.

## Purpose

This inventory records explicit producer→consumer relationships visible in the authored catalog. It is deliberately not marked exhaustive until all E01–E270 source ranges have been machine-extracted and checked.

## Verified durable producers and downstream consumers

| Producer event | Producer token | Consumer(s) observed | Notes |
|---|---|---|---|
| E116 | `auditor_apprentices` | E134, E142, E151 | Canonical thread candidate: Mara/institutional audit |
| E117 | `veterans_examined` / `veteran_patronage` | E125, E170, E182, E222, E245 | Two different veteran concepts must not be conflated |
| E118 | `equal_estate_law` / `estate_exception` | E162 / E183 / E242 | Exception has explicit delayed precedent chain |
| E119 | `guild_whistleblower` / `guild_internal_review` | E168 | Whistleblower path has downstream tribunal consequence |
| E121 | `protected_sources` / `named_sources_only` | E180 and information routes | Must be separated from generic Toma relationship |
| E122 | `tax_transparency` / `tax_private_bargain` | E159, E211, E216 | Tax transparency is an institutional producer, not merely trust |
| E124 | `public_trade_standards` / `guild_trade_standards` | E168, later guild route | Two distinct governance models |
| E126 | `river_compact` / `royal_toll_office` | E130/E181/E224 and river route | Toll consequences need exact delay identity |
| E127 | `privilege_renewal_refused` / `privilege_renewed_again` | noble route | Explicit delayed renewal source |
| E128 | `steel_replaced` / `steel_repaired` | E185 | E185 additionally needs exact military-crisis trigger |
| E131 | `emergency_language_compared` / `precedent_ignored` | E188 | Replay metadata must be separated from current-run state |
| E134 | `office_network_mapped` / `map_destroyed_after_copy` | E153, E190, E249 | Strong investigation chain |
| E135 | `conflicting_testimony_recorded` | E189 | Explicit callback relationship |
| E139 | `frontier_lantern_network` / `frontier_military_watch` | E171 and border descendants | Border + Amara intersection |
| E140 | `trade_risk_insurance` / `market_self_adjustment` | E220 | Explicit delayed economic consequence |
| E142 | `auditor_independence` / `auditor_crown_control` | E151, E154 | Strong producer→consumer chain |
| E154 | `crown_audited` / `crown_exempt_from_audit` | E155, E211 | Crown audit route |
| E155 | `full_crown_audit_published` / `audit_summary_only` | E211 | Publication depth changes later access |
| E156 | `requisition_compensation` / `requisition_tax_credit` | E245 | Delayed callback |
| E161 | `house_assembly` / `crown_confiscation_power` | E162 and noble route | Constitutional noble route |
| E162 | `estate_map_audit` / `targeted_estate_audit` | noble evidence routes | Investigation depth differs |
| E164 | `private_army_rejected` / `private_army_licensed` | border/security routes | Potential security/power contradiction to audit |
| E168 | `guild_tribunal_independent` / `guild_tribunal_controlled` | guild route | Institutional fork |
| E169 | `apprentice_safety_law` / `apprentice_strike_broken` | social/guild route | `guild labor tension` needs predicate mapping |
| E172 | `civilian_signal_authority` / `military_signal_control` | border crisis | `border tension` is currently prose-level |
| E173 | `barracks_shelter` | winter/civic route | `low army readiness` needs deterministic definition |
| E175 | `humane_quarantine` / `hard_quarantine` | E176 | Health-pressure state must remain explicit, not hidden resource |
| E177 | `licensed_courier_network` / `courier_surveillance` | information route | Strong Toma institutional fork |
| E178 | `unsent_letter_traced` / `unsent_letter_replaced` | information route | Evidence identity needed |
| E180 | `informant_family_relocated` / `informant_guard` | information route | Security/privacy fork |
| E181 | `toll_escalation_sold` | economic route | Explicit delayed callback |
| E182 | `veteran_positions_granted` | security/character route | Delayed patronage consequence |
| E183 | `exception_precedent_closed` / `exception_precedent_extended` | noble route | Delayed precedent chain |
| E184 | `quiet_evidence_published` / `quiet_evidence_kept` | evidence/reputation routes | Delayed secrecy consequence |
| E185 | `steel_failure_prevented` | later military crisis | Requires explicit exactly-once prevention semantics |
| E186 | `warehouse_second_box` / `warehouse_fire_focus` | replay investigation | Replay-only information must use `meta.*` |
| E187 | `payment_date_crosscheck` | E234 | Explicit investigation chain |
| E188 | `necessity_phrase_history` | replay/institutional investigation | Historical interpretation route |
| E189 | `witness_reopened` | evidence route | Callback validates earlier testimony |
| E211 | `public_ledger_room` / `ledger_summary_access` | civic/evidence routes | Publication-access fork |
| E212 | `clerk_protected` / `clerk_discipled` | institutional route | Typo `clerk_discipled` should be corrected before schema lock |
| E213 | `royal_appeal_override` | constitutional route | Distinct override state |
| E214 | `appointment_transparent` / `appointment_patronage` | institutional route | Appointment legitimacy fork |
| E215 | `free_law_copies` / `law_copy_fee` | civic route | Public access fork |
| E216 | `treasury_shortfall_public` / `quiet_treasury_loan` | E217 | Explicit financial delayed consequence |
| E217 | `creditor_advisor` | constitutional/economic route | Potential institutional capture marker |
| E218 | `grain_contract_inspected` / `grain_contract_rushed` | food/economic route | Food-pressure predicate required |
| E219 | `merchant_margin_disclosure` / `merchant_margin_tax` | economic route | Distinct market policies |
| E220 | `trade_guarantee_honored` / `trade_guarantee_challenged` | economic route | Explicit delayed insurance result |
| E221 | `tenant_panels` | civic route | Social representation |
| E223 | `competence_medical_license` / `house_medical_license` | civic/Amara route | Professional access fork |
| E224 | `river_safety_barriers` | river route | Infrastructure callback |
| E225 | `bread_queue_heard` / `bread_queue_dispersed` | civic/crisis route | Severe food pressure remains derived |
| E226 | `mara_independent_mandate` / `mara_resigned` | E116 and ending routes | Character institutional endpoint |
| E227 | `military_red_line` | constitutional/security routes | Strong constitutional marker |
| E229 | `ivo_shortcut_closed` / `ivo_shortcut_used` | economic/endgame routes | Explicit fiscal shortcut fork |
| E231 | `toma_verification_first` / `toma_immediate_release` | evidence/endgame | Information governance fork |
| E232 | `intermediary_chain_traced` / `visible_suppliers_charged` | E235 | Procurement chain |
| E233 | `seal_forensics` / `duplicate_seal_suppressed` | investigation route | Evidence handling fork |
| E234 | `payment_pattern_public` / `payment_pattern_private` | investigation/endgame | Disclosure fork |
| E235 | `middleman_family_archive` | investigation route | Noble/archive cross-link |
| E237–E241 | faction-specific credibility outcomes | endgame/faction routes | Should become canonical thread/history markers, not generic booleans |
| E242 | precedent close/extend | noble route | Explicit delayed precedent |
| E243 | public bridge investment callback | infrastructure route | Positive delayed payoff |
| E244 | `reconstructed_accounts` | accounting/investigation | Requires evidence-integrity semantics |
| E246 | price-ceiling end/extend | economic route | Delayed policy-memory condition |
| E247 | `alternate_suspect_tested` | replay investigation | Replay route |
| E248 | `forgotten_favor_honored` | replay/social route | Replay callback |
| E250 | `pattern_anomaly_preserved` | investigation | Explicit anomaly route |
| E254 | local warehouse vote | civic/food route | Food crisis predicate required |
| E255 | three-crisis prioritization | constitutional/endgame | Must use three canonical predicates |
| E256–E260 | constitutional stress-test choices | ending routes | Ending prerequisites still require reachability simulation |
| E261 | `four_way_bargain` / `two_faction_bargain` | E262/E263/endgame | Cross-faction route |

## Concrete normalization defects found

1. Relationship shorthand such as `Seris >= 0`, `Mara >= 1`, `Rowan >= 1`, `Ivo >= 1`, `Amara >= 1`, `Toma >= 1` must compile to canonical `rel.*` comparisons.
2. `food shortage`, `food-price pressure`, `severe food pressure`, and `food crisis` need deterministic canonical predicates/history/thread state.
3. `border tension`, `border pressure`, `border escalation`, and `border crisis` need one canonical predicate family.
4. `low security`, `low army readiness`, `strong security route`, and `military route` are not interchangeable conditions.
5. `institutional reform`, `audit reform`, `document audit route`, and `audit office` need canonical thread/flag identities.
6. `information route`, `high information pressure`, `secret evidence route`, `witness route`, and `replay callback` need explicit state namespaces.
7. `clerk_discipled` in E212 is a data typo and must be corrected before production schema generation.
8. `office_network_mapped` is reused by multiple consumers and must have one canonical producer identity.
9. `later`, `3+ turns later`, `5+ turns later`, and `6+ turns later` must become exact delayed contracts with deterministic boundaries.
10. A choice that has no durable marker is acceptable only if no later authored content depends on it; otherwise a history marker is required.

## Gate status

This is a QA artifact, not runtime data. It is not sufficient to mark canonicalization complete. The next pass must reconcile it against E01–E110 and the complete E191–E270 source text, then generate an exhaustive machine-readable inventory and automated producer/consumer checks.
