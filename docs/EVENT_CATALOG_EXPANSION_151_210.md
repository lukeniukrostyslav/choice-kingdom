# Choice Kingdom — Expansion Events E151–E210

These nodes deepen replay divergence, delayed consequences, faction credibility and late-campaign pressure. They are authored content pending canonical integration and reachability QA.

## Institutional reform

### E151 — The Clerk's Oath
**Trigger:** `auditor_independence` or `audit_office`.
New auditors must swear loyalty to the law rather than the Crown.
- **A — Public oath:** +4 trust, -2 power; `clerks_oath_public`.
- **B — Private oath:** +2 power, -1 trust; `clerks_oath_private`.

### E152 — The Missing Signature
**Trigger:** document audit route.
A decree is valid in every respect except for one missing signature.
- **A — Treat it as invalid:** +4 trust, -2 power; `unsigned_decree_void`.
- **B — Accept the practical authority:** +3 power, -3 trust; `unsigned_decree_accepted`.

### E153 — The Archive Key
**Trigger:** `office_network_mapped`.
The old archive has one key shared among three offices.
- **A — Duplicate the key:** -2 gold, +3 power; `archive_access_shared`.
- **B — Keep one controlled key:** +3 security, -2 trust; `archive_access_restricted`.

### E154 — The First Audit of the Crown
**Trigger:** `auditor_independence` and high institutional trust.
The new office requests the ruler's own expenses.
- **A — Submit voluntarily:** +6 trust, -2 power; `crown_audited`.
- **B — Exempt the Crown:** +4 power, -5 trust; `crown_exempt_from_audit`.

### E155 — The Cost of Transparency
**Trigger:** `crown_audited`.
The audit finds embarrassing but legal expenses.
- **A — Publish the full result:** +5 trust, -2 reputation; `full_crown_audit_published`.
- **B — Publish a summary:** +2 trust, +2 reputation; `audit_summary_only`.

## Commons and daily life

### E156 — The Widow's Petition
**Trigger:** high trust or civic relief.
A widow asks for compensation after soldiers requisitioned her winter animals.
- **A — Pay full compensation:** -4 gold, +4 trust; `requisition_compensation`.
- **B — Offer tax credit:** -2 future income, +2 trust; `requisition_tax_credit`.

### E157 — The Millstone
**Trigger:** food shortage.
A communal mill is failing because its ownership is disputed.
- **A — Place it under public trust:** -3 gold, +5 trust; `public_mill_trust`.
- **B — Sell it to the guild:** +4 gold, +2 Ivo, -3 trust; `mill_guild_sale`.

### E158 — The Night School
**Trigger:** `schoolhouse_vote` or high civic trust.
Clerks and workers ask for evening literacy classes.
- **A — Fund them:** -3 gold, +4 trust; `night_school_funded`.
- **B — Let guilds sponsor them:** +2 Ivo, +2 gold, -2 trust; `guild_night_school`.

### E159 — The Public Notice
**Trigger:** `tax_transparency` or `clerks_oath_public`.
The Crown must choose how ordinary people receive new laws.
- **A — Post them everywhere:** -2 gold, +5 trust; `law_notices_public`.
- **B — Rely on local officials:** +2 power, -2 trust; `law_notices_local`.

### E160 — The Price of a Warm Room
**Trigger:** severe winter.
A landlord raises rents during the coldest week.
- **A — Temporary rent ceiling:** +4 trust, -2 gold; `winter_rent_ceiling`.
- **B — Emergency heating vouchers:** -5 gold, +5 trust; `heating_vouchers`.

## Noble route

### E161 — The House Assembly
**Trigger:** Seris route.
Nobles propose an assembly to prevent arbitrary confiscation of estates.
- **A — Accept a constitutional assembly:** +4 Seris, +4 trust, -2 power; `house_assembly`.
- **B — Keep confiscation powers:** +4 power, -4 Seris; `crown_confiscation_power`.

### E162 — The Estate Map
**Trigger:** `equal_estate_law` or `house_assembly`.
A public map reveals several noble properties acquired during emergencies.
- **A — Investigate all acquisitions:** +5 trust, -3 Seris; `estate_map_audit`.
- **B — Investigate only contested properties:** +2 power, +1 Seris; `targeted_estate_audit`.

### E163 — The Family Seal
**Trigger:** Seris evidence route.
A family seal appears on a document thought to be forged.
- **A — Ask Seris to testify:** +3 power, relationship stress; `family_seal_testimony`.
- **B — Protect the family from immediate exposure:** +3 Seris, -3 trust; `family_seal_protected`.

### E164 — The Noble Guard
**Trigger:** high noble influence + low security.
A house offers private troops to protect roads.
- **A — Reject private armies:** +5 trust, -2 Seris, +2 security; `private_army_rejected`.
- **B — License them temporarily:** +4 security, +3 Seris, -4 power; `private_army_licensed`.

## Guild and market route

### E165 — The Credit Book
**Trigger:** guild leverage.
A guild credit book shows that several officials owe merchants personal debts.
- **A — Require disclosure:** +5 trust, -2 Ivo; `official_credit_disclosure`.
- **B — Treat private debts as private:** +3 Ivo, +2 gold, -3 trust; `private_credit_protected`.

### E166 — The Honest Monopoly
**Trigger:** strong market oversight + merchant charter.
A monopoly claims it can deliver stable prices if audited monthly.
- **A — Permit audited monopoly:** +5 gold, +3 trust; `audited_monopoly`.
- **B — Break monopoly anyway:** -2 gold, +5 trust; `monopoly_broken_on_principle`.

### E167 — The Import Risk
**Trigger:** `free_grain_imports`.
Merchants will import food only if the Crown guarantees losses from storms.
- **A — Guarantee part of the risk:** -5 gold, +5 trust; `import_risk_guarantee`.
- **B — Refuse guarantees:** +3 power, -2 trust; `import_risk_refused`.

### E168 — The Guild Tribunal
**Trigger:** `guild_whistleblower` or `public_trade_standards`.
Guilds request a tribunal for commercial disputes.
- **A — Independent tribunal:** +4 trust, -2 Ivo; `guild_tribunal_independent`.
- **B — Guild-controlled tribunal:** +4 Ivo, +3 gold, -4 trust; `guild_tribunal_controlled`.

### E169 — The Apprentice Strike
**Trigger:** guild labor tension.
Apprentices stop work over unsafe conditions.
- **A — Mandate safety standards:** +5 trust, -2 Ivo; `apprentice_safety_law`.
- **B — Order immediate return:** +3 security, -5 trust; `apprentice_strike_broken`.

## Security and border route

### E170 — The Veteran's Wall
**Trigger:** veteran patronage or border pressure.
Veterans offer to build fortifications in exchange for permanent land grants.
- **A — Pay wages, no land grants:** -5 gold, +4 security, +3 trust; `veteran_fortification_wages`.
- **B — Grant land:** +5 security, +3 Rowan, -4 trust; `veteran_land_grants`.

### E171 — The Border Trial
**Trigger:** `frontier_military_watch` or military route.
A civilian is accused of helping foreign scouts.
- **A — Public trial:** +4 trust, -1 security; `border_public_trial`.
- **B — Military tribunal:** +4 security, -4 trust; `military_border_trial`.

### E172 — The Signal Fires
**Trigger:** border tension.
Villages want authority to light warning fires without waiting for soldiers.
- **A — Authorize civilian signals:** +4 trust, +2 security; `civilian_signal_authority`.
- **B — Reserve signals for soldiers:** +3 security, -3 trust; `military_signal_control`.

### E173 — The Empty Barracks
**Trigger:** low army readiness.
A barracks stands empty because its budget was redirected years ago.
- **A — Rebuild:** -6 gold, +6 security; `barracks_rebuilt`.
- **B — Convert it to a civilian shelter:** -3 gold, +5 trust; `barracks_shelter`.

## Amara and civic conscience

### E174 — The Medicine Cart
**Trigger:** Amara >= 1.
Lantern healers need permission to cross noble boundaries.
- **A — Give them a universal pass:** +5 trust, +3 Amara, -2 power; `lantern_universal_pass`.
- **B — Require local approval:** +2 power, -3 Amara; `lantern_local_approval`.

### E175 — The Quarantine Question
**Trigger:** winter illness.
A district may be isolated to prevent disease spread.
- **A — Isolate with food guarantees:** -5 gold, +5 trust; `humane_quarantine`.
- **B — Isolate without guarantees:** +4 security, -5 trust; `hard_quarantine`.

### E176 — The Healer's Testimony
**Trigger:** `humane_quarantine` or strong Amara route.
A healer reports that emergency requisitions caused preventable deaths.
- **A — Investigate openly:** +5 trust, -2 security; `medical_requisition_inquiry`.
- **B — Protect military reputation:** +3 security, -4 Amara; `medical_testimony_suppressed`.

## Toma and information

### E177 — The Courier Network
**Trigger:** Toma >= 1.
Toma proposes legalizing a network that carries official and private messages.
- **A — License it:** +3 Toma, +4 trust; `licensed_courier_network`.
- **B — Monitor every courier:** +4 security, -4 Toma; `courier_surveillance`.

### E178 — The Unsent Letter
**Trigger:** information route.
A letter exposing a minor official never reached its destination.
- **A — Trace its route:** +3 power, +2 Toma; `unsent_letter_traced`.
- **B — Replace the letter:** +2 trust, -2 power; `unsent_letter_replaced`.

### E179 — The Rumor Tax
**Trigger:** low information trust.
Merchants begin charging extra because rumors make contracts risky.
- **A — Publish verified market notices:** +4 trust, -2 power; `verified_market_notices`.
- **B — Punish rumor sellers:** +3 security, -4 trust; `rumor_sellers_punished`.

### E180 — The Informant's Daughter
**Trigger:** protected-source route.
An informant's family fears retaliation.
- **A — Relocate the family:** -4 gold, +4 trust; `informant_family_relocated`.
- **B — Offer a palace guard:** -2 gold, +3 security; `informant_guard`.

## Delayed callbacks

### E181 — The Second Toll Increase
**Trigger:** 5+ turns after a toll concession.
The same concessionaire asks for a second increase.
- **A — Enforce original terms:** +5 trust, -2 Ivo; `toll_terms_enforced`.
- **B — Sell the right to increase tolls:** +7 gold, -5 trust; `toll_escalation_sold`.

### E182 — The Veteran's Promise
**Trigger:** `veteran_patronage`, 4+ turns later.
Veterans demand the promised administrative positions.
- **A — Hold examinations:** +3 trust, -3 Rowan; `veteran_positions_examined`.
- **B — Honor the promise:** +4 Rowan, +3 security, -4 trust; `veteran_positions_granted`.

### E183 — The Noble Exception Returns
**Trigger:** `estate_exception`, 5+ turns later.
Another family cites the precedent and requests identical treatment.
- **A — End the exception:** +4 trust, -3 Seris; `exception_precedent_closed`.
- **B — Extend it:** +3 Seris, +2 power, -4 trust; `exception_precedent_extended`.

### E184 — The Quiet Evidence
**Trigger:** secret evidence route, 4+ turns later.
A witness asks why the Crown never published the evidence it promised to preserve.
- **A — Publish the preserved record:** +5 trust, -2 reputation; `quiet_evidence_published`.
- **B — Keep confidentiality:** +3 power, -3 trust; `quiet_evidence_kept`.

### E185 — The Cheap Steel Remembered
**Trigger:** `cheap_weapons` plus later military crisis.
A veteran recognizes the same flawed steel in a critical shipment.
- **A — Halt deployment:** -4 security now, prevents later disaster; `steel_failure_prevented`.
- **B — Deploy anyway:** +5 security now, schedules severe delayed loss; `steel_failure_delayed`.

## Replay-exclusive information

### E186 — The Same Warehouse
**Trigger:** `warehouse_arson` or equivalent previous-run informational unlock when supported by replay metadata.
The warehouse seen during one investigation contains a different ledger box under another manager.
- **A — Search for the box:** +4 power; `warehouse_second_box`.
- **B — Focus on the fire:** +3 security; `warehouse_fire_focus`.

### E187 — The Missing Name
**Trigger:** multiple evidence fragments.
A name absent from one list appears on a payment schedule.
- **A — Cross-reference dates:** +5 power; `payment_date_crosscheck`.
- **B — Assume omission was clerical:** +2 power, -1 trust; `payment_omission_assumed`.

### E188 — The Repeated Phrase
**Trigger:** `emergency_language_compared`.
The phrase “temporary necessity” appears in three generations of decrees.
- **A — Investigate institutional continuity:** +4 power; `necessity_phrase_history`.
- **B — Treat it as coincidence:** +2 power; `necessity_phrase_dismissed`.

### E189 — The Witness Who Was Right Twice
**Trigger:** conflicting testimony recorded.
A previously doubted witness correctly predicts a new document's location.
- **A — Reopen their earlier testimony:** +4 trust, +3 power; `witness_reopened`.
- **B — Use only the new lead:** +2 power, -1 trust; `witness_new_lead_only`.

### E190 — The Map Beneath the Map
**Trigger:** office network mapped.
A second organizational layer shows who benefited indirectly rather than who signed documents.
- **A — Follow beneficiaries:** +5 power, -2 security; `beneficiary_network_followed`.
- **B — Stop at formal responsibility:** +3 reputation, +2 security; `formal_responsibility_only`.

## Crisis escalation

### E191 — The Third Fire
**Trigger:** unresolved warehouse/market crisis.
A third fire threatens food distribution.
- **A — Protect people before evidence:** +5 trust, -2 power; `warehouse_crisis_people_first`.
- **B — Protect the evidence first:** +4 power, -3 trust; `warehouse_crisis_evidence_first`.

### E192 — The Broken Cart
**Trigger:** `pred.transport_disruption`.
A single broken cart delays medicine and grain simultaneously.
- **A — Prioritize medicine:** +4 trust; `food_logistics_unstable`, worsening food pressure and Amara's route.
- **B — Prioritize grain:** +4 trust; `food_logistics_stabilized`, while Amara's relationship worsens.

### E193 — The Soldiers' Bread
**Trigger:** low gold + high security.
The army asks for civilian bread reserves.
- **A — Share equally:** -3 security, +5 trust; `civilian_bread_shared`.
- **B — Protect military reserves:** +4 security, -5 trust; `military_bread_reserved`.

### E194 — The Guild Convoy
**Trigger:** `history.guild_logistics_cooperation`.
Merchants offer a convoy but request immunity from certain inspections.
- **A — Accept with neutral inspectors:** +4 trust, +2 Ivo; `history.guild_logistics_cooperation`, `guild_neutral_inspectors`.
- **B — Grant immunity:** +5 gold, -5 trust; `guild_convoy_immunity`, `guild_logistics_immunity_risk`.

The qualified downstream predicate `pred.guild_logistics_cooperation` is derived only when the prior cooperation marker from an upstream source (such as E136-B) exists, `guild_neutral_inspectors` has been established, and no unresolved `guild_logistics_immunity_risk` remains. E194 must not self-produce that qualified predicate from its own trigger.

### E195 — The Border Refugees
**Trigger:** `pred.border_crisis`.
Families flee toward Avelune.
- **A — Admit and shelter:** -7 gold, +7 trust; `refugee_shelter`.
- **B — Close the border:** +4 security, -7 trust; `border_closed`.

## Constitutional endgame preparation

### E196 — The Five Questions
**Trigger:** late constitutional route.
The council asks five questions about taxation, force, evidence, local power and emergency authority.
- **A — Publish all questions:** +5 trust, -2 power; `five_questions_public`.
- **B — Answer privately:** +4 power, -3 trust; `five_questions_private`.

### E197 — The Succession Test
**Trigger:** `pred.constitutional_prepared_strong`.
The ruler must decide whether the next ruler inherits emergency powers automatically.
- **A — Powers expire:** +6 trust, -3 power; `emergency_powers_expire`.
- **B — Powers transfer:** +5 power, -5 trust; `emergency_powers_inherit`.

### E198 — The Budget Lock
**Trigger:** audit reform.
The legislature asks for authority to block spending outside the published budget.
- **A — Grant budget lock:** +5 trust, -3 power; `legislative_budget_lock`.
- **B — Retain executive override:** +4 power, -4 trust; `executive_budget_override_retained`.

### E199 — The Army Oath Rewritten
**Trigger:** military constitutional route.
The army must choose whether its oath is to the ruler or the constitution.
- **A — Constitution:** +6 trust, -3 Rowan; `army_constitution_oath`.
- **B — Crown:** +5 security, +3 Rowan, -6 trust; `army_crown_oath`.

### E200 — The Merchant Oath
**Trigger:** `pred.guild_influence_strong`.
Major merchants are asked to swear that contracts cannot buy political office.
- **A — Accept the restriction:** +5 trust, -3 Ivo; `merchant_political_separation`.
- **B — Permit influence with disclosure:** +4 Ivo, +3 gold, -4 trust; `merchant_influence_disclosed`.

## Final coalition and endings

### E201 — The Coalition's Weakest Promise
**Trigger:** `pred.coalition_cooperation`.
One coalition promise is impossible to fund.
- **A — Admit it and renegotiate:** -3 power, +5 trust; `coalition_renegotiated`.
- **B — Hide the shortfall:** +4 power, -6 trust; `coalition_shortfall_hidden`.

### E202 — The Last Noble Vote
**Trigger:** `history.house_assembly`.
Seris must decide whether nobles can veto the final charter.
- **A — No veto:** +5 trust, -3 Seris; `noble_veto_rejected`.
- **B — Limited veto:** +3 Seris, +3 power, -4 trust; `noble_limited_veto`.

### E203 — The Last Guild Vote
**Trigger:** `history.guild_representation`.
Ivo asks for a permanent commercial seat.
- **A — Advisory only:** +4 trust, -2 Ivo; `guild_advisory_seat`.
- **B — Binding commercial seat:** +4 Ivo, +3 gold, -5 trust; `guild_binding_seat`.

### E204 — The Last Soldiers' Vote
**Trigger:** `thread.military_constitutional`.
Rowan asks whether the army may reject unlawful orders.
- **A — Constitutional refusal:** +6 trust, -3 Rowan; `military_constitutional_refusal`.
- **B — Obey the Crown:** +5 security, +3 Rowan, -6 trust; `military_crown_obedience`.

### E205 — The Last Lantern Vote
**Trigger:** `thread.amara_civic`.
Amara asks for permanent protection of emergency medical neutrality.
- **A — Protect neutrality:** +5 trust, +3 Amara, -2 power; `medical_neutrality_protected`.
- **B — Permit military override:** +4 security, -5 trust; `medical_neutrality_overridden`.

### E206 — The Last Courier Vote
**Trigger:** `thread.toma_information`.
Toma asks whether lawful journalists may publish evidence against the Crown.
- **A — Protect publication:** +6 trust, -3 power; `press_protection`.
- **B — Permit emergency censorship:** +5 power, -6 trust; `emergency_censorship`.

### E207 — The Founder Question
**Trigger:** `pred.systemic_explanation_verified` and `pred.coalition_cooperation`.
The player is offered a chance to become the indispensable founder of the new order.
**Qualification requirement:** the source must contain distinct warehouse/financial evidence, document/language evidence, witness/organizational evidence, and an explicit convergence decision before this node becomes eligible.
- **A — Refuse permanent personal authority:** +7 trust, -4 power; `founder_authority_refused`.
- **B — Accept founder authority:** +6 power, -6 trust; `founder_authority_accepted`.

### E208 — The Empty Chair Again
**Trigger:** `thread.final_constitutional_phase`.
The original empty chair is brought into the chamber as a reminder of how the crisis began.
- **A — Leave it empty as a warning:** +5 trust; `empty_chair_memorial`.
- **B — Fill it with a permanent emergency office:** +6 power, -7 trust; `permanent_emergency_chair`.

### E209 — The Dawn Charter
**Trigger:** `pred.final_charter_prerequisites`.
The completed constitutional text is read before dawn.
**Qualification requirement:** before E209, civic/commons legitimacy, institutional/audit legitimacy, faction/house/guild representation, required military/security constitutional route, information/evidence legitimacy, coalition cooperation, and absence of unresolved mandatory crisis blockers must all be established by upstream authored state.
- **A — Ratify publicly:** +7 trust, -3 power; `charter_publicly_ratified`.
- **B — Ratify through council:** +5 power, -5 trust; `charter_council_ratified`.

### E210 — The Last Decision Is Not a Choice
**Trigger:** `thread.endgame_convergence`.
The kingdom's future reflects the pattern of the reign rather than one final button. The engine later resolves the ending from verified history, institutional state, relationships, unresolved crises, evidence, emergency-power use and coalition structure.

**Rule:** E210 is convergence-only. It must not create missing prerequisites, manufacture evidence, create coalition cooperation, or directly invent a route qualification that was absent upstream.

Possible resolution families:
- Steward;
- Iron Crown;
- Golden Compact;
- People's Charter;
- Broken Diadem;
- Quiet Throne;
- Second Founder;
- additional ending variants to be authored only if QA finds a meaningful distinct constitutional outcome.

## Expansion QA notes

E151–E210 intentionally contain multiple independent paths, delayed callbacks, faction trade-offs, constitutional tests and replay information. They are authored nodes, not yet proof of reachability. Exact conditions, turn windows, consequence scheduling and ending qualification must be reconciled during the later graph/engine QA pass.
