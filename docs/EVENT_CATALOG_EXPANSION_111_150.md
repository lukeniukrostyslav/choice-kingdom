# Choice Kingdom — Expansion Events E111–E150

These are authored causal nodes around the existing campaign spine. They are not filler and remain subject to later reachability/contradiction QA.

## Civic life and legitimacy

### E111 — The Empty Bench
**Trigger:** high trust or `local_relief_councils`.
A village council asks whether ordinary people may remove a local official without palace approval.
- **A — Allow local recall:** +5 trust, -2 power; `local_recall_allowed`; delayed civic participation grows.
- **B — Require royal review:** +3 power, -2 trust; `royal_review_required`; delayed local resentment.

### E112 — The Baker's Ledger
**Trigger:** food-price pressure.
A baker has kept private records showing which policies actually changed flour prices.
- **A — Publish the records:** +4 trust, -1 reputation; `bread_records_public`.
- **B — Buy the records quietly:** +2 power, -2 trust; `bread_records_private`; later evidence is weaker.

### E113 — A Question of Names
**Trigger:** `full_ledger_published` or `ledger_network_public`.
Citizens ask whether minor officials should be publicly named alongside the architects of the emergency system.
- **A — Publish names only after proof:** +3 trust, +2 power; `verified_names_policy`.
- **B — Publish everyone involved:** +5 trust, -3 reputation; `broad_accusations`; innocent families may retaliate.

### E114 — The Schoolhouse Vote
**Trigger:** `people_charter_endorsed` or high civic trust.
A schoolhouse becomes the first place where villagers vote on a local budget.
- **A — Let the experiment stand:** +4 trust, -2 power; `local_budget_vote`.
- **B — Keep budgets centrally approved:** +3 power, -2 trust; `central_budget_control`.

### E115 — The Tax Collector's Road
**Trigger:** strong treasury pressure.
Collectors request soldiers after several villages refuse a new levy.
- **A — Send auditors instead:** -2 gold, +4 trust; `tax_audit_first`.
- **B — Send soldiers:** +3 gold, +4 security, -5 trust; `tax_enforcement`.

## Character crossroads

### E116 — Mara's Apprentice
**Trigger:** Mara >= 1 or `mara_independent_mandate`.
Mara proposes training clerks who can audit the Crown itself.
- **A — Fund independent training:** -4 gold, +4 Mara, +4 trust; `auditor_apprentices`.
- **B — Keep training inside the palace:** +2 power, -2 Mara; `palace_auditors`.

### E117 — Rowan's Recruits
**Trigger:** Rowan >= 1.
Veterans want guaranteed positions in the border administration.
- **A — Civil service examinations:** +3 trust, -2 Rowan; `veterans_examined`.
- **B — Reserve posts for veterans:** +4 security, +2 Rowan, -3 trust; `veteran_patronage`.

### E118 — Seris's Younger Brother
**Trigger:** Seris >= 0.
A younger Auren asks Seris to use the Crown's new rules to preserve the family's estate.
- **A — Apply the same law to him:** +4 trust, -2 Seris; `equal_estate_law`.
- **B — Create a transitional exception:** +3 Seris, +2 power, -3 trust; `estate_exception`.

### E119 — Ivo's Apprentice
**Trigger:** Ivo >= 1.
A young guild accountant discovers that his mentor's clever loopholes helped hide emergency profits.
- **A — Protect the whistleblower:** +4 trust, -2 Ivo; `guild_whistleblower`.
- **B — Let Ivo handle it internally:** +3 Ivo, +2 gold; `guild_internal_review`.

### E120 — Amara's Clinic
**Trigger:** Amara >= 1.
The House of Lanterns asks for permanent legal status instead of annual royal favors.
- **A — Grant protected civic status:** +5 trust, -2 power; `lanterns_protected`.
- **B — Keep annual royal grants:** +2 power, +2 Amara, -2 trust; `lanterns_dependent`.

### E121 — Toma's Price
**Trigger:** Toma route.
Toma asks for legal protection for informants who bring evidence before it is officially requested.
- **A — Create protected-source rules:** +3 trust, +2 Toma, -2 power; `protected_sources`.
- **B — Require informants to identify themselves:** +3 security, -3 Toma; `named_sources_only`.

## Faction pressure

### E122 — The Commons' Counteroffer
**Trigger:** `local_budget_vote` or `people_charter_endorsed`.
Commons representatives offer to support the Crown if taxation becomes transparent.
- **A — Publish tax schedules:** +5 trust, -2 power; `tax_transparency`.
- **B — Negotiate privately:** +2 power, -2 trust; `tax_private_bargain`.

### E123 — The Noble Granary
**Trigger:** noble cooperation + food shortage.
Several houses offer private grain reserves, but only to districts loyal to them.
- **A — Integrate reserves into public distribution:** +5 trust, -2 Seris; `noble_grain_public`.
- **B — Allow private distribution:** +5 gold-equivalent relief, +2 Seris, -4 trust; `noble_grain_private`.

### E124 — Guild Standards
**Trigger:** commercial route.
Merchants propose standardized weights, arguing that honest trade will become cheaper.
- **A — Make standards public law:** +4 trust, -2 Ivo; `public_trade_standards`.
- **B — Let guilds enforce them:** +3 Ivo, +2 gold; `guild_trade_standards`.

### E125 — Border Families
**Trigger:** strong security route.
Border families ask for compensation after years of military requisitions.
- **A — Compensate them:** -6 gold, +5 trust; `border_compensation`.
- **B — Offer tax exemptions:** -3 gold income, +2 security; `border_tax_exemption`.

### E126 — The River Compact
**Trigger:** `public_infrastructure_trust` or `competitive_market`.
River towns propose jointly governing tolls and maintenance.
- **A — Accept joint governance:** +5 trust, -2 power; `river_compact`.
- **B — Keep a royal toll office:** +5 gold, +2 power, -3 trust; `royal_toll_office`.

## Delayed consequence nodes

### E127 — The Renewal Petition
**Trigger:** 4+ turns after `hereditary_seats_limited` or `temporary_noble_exemption`.
The same houses return asking for the temporary privilege to become permanent.
- **A — Refuse:** +4 trust, -2 Seris; `privilege_renewal_refused`.
- **B — Renew once:** +3 Seris, +2 power, -3 trust; `privilege_renewed_again`.

### E128 — The Cheap Steel Bill
**Trigger:** `cheap_weapons`, 3+ turns later.
Weapons purchased cheaply begin failing during training.
- **A — Replace them:** -7 gold, +4 security; `steel_replaced`.
- **B — Repair them locally:** -3 gold, +1 security, -2 Rowan; `steel_repaired`.

### E129 — The Festival Memory
**Trigger:** festival was held, 3+ turns later.
Citizens remember whether the Crown protected them without ruining the celebration.
- **A — Publish the security report:** +3 trust; `festival_reported`.
- **B — Keep details secret:** +2 power, -2 trust; `festival_secret`.

### E130 — The Bridge Toll Returns
**Trigger:** `infrastructure_concession`, 4+ turns later.
The concessionaire raises tolls beyond the original promise.
- **A — Enforce the original ceiling:** +4 trust, -2 Ivo.
- **B — Renegotiate for more royal revenue:** +5 gold, -3 trust, +2 Ivo.

## Information and replay

### E131 — The Same Letter Twice
**Trigger:** replay with `all_voices_heard` from a previous run unavailable to current save; informational callback flag.
A letter appears to repeat wording seen in an earlier reign, revealing that emergency language predates the current Crown.
- **A — Compare archives:** +3 power; `emergency_language_compared`.
- **B — Ignore precedent:** +2 power; `precedent_ignored`.

### E132 — The Redacted Page
**Trigger:** any secret evidence route.
A missing page can be reconstructed from two independent fragments.
- **A — Combine fragments:** +4 power, +2 trust; `redaction_reconstructed`.
- **B — Preserve uncertainty:** +2 trust, +2 reputation; `uncertainty_preserved`.

### E133 — The False Pattern
**Trigger:** `mastermind_hunt`.
Three unrelated crimes appear connected because they used the same emergency form.
- **A — Test the common form:** +4 power, -1 security; `form_pattern_tested`.
- **B — Arrest the apparent coordinator:** +3 security, -4 trust; `pattern_arrest`.

### E134 — The Old Clerk's Map
**Trigger:** `auditor_apprentices` or Mara route.
An old clerk maps how temporary offices became permanent networks.
- **A — Preserve the map:** +4 power; `office_network_mapped`.
- **B — Destroy it after copying:** +3 power, -2 trust; `map_destroyed_after_copy`.

### E135 — The Second Witness
**Trigger:** `witness_protected`.
A second witness contradicts part of the first testimony but confirms the movement of documents.
- **A — Record both testimonies:** +4 trust; `conflicting_testimony_recorded`.
- **B — Choose the cleaner account:** +3 power, -3 trust; `clean_testimony_selected`.

## Crisis preparation

### E136 — The Frozen Road
**Trigger:** winter severity.
A blocked road isolates three villages and establishes a durable transport state.
- **A — Open a public labor effort:** -4 gold, +5 trust; `transport_network_stable`; clears `transport_disruption_active`.
- **B — Contract guild transport:** -2 gold, +2 Ivo, +3 security; `transport_network_stable`; clears `transport_disruption_active`; `roads_guild_contract`.

A later canonical disruption event may set `transport_disruption_active`; this choice is the explicit repair producer. `roads_public_labor` is retained only as a historical outcome alias and is not the predicate producer.

### E137 — The Night Watch Fund
**Trigger:** low security.
Towns offer to fund their own night watches if the Crown provides training.
- **A — Train civilian watches:** -2 gold, +4 trust; `civilian_watch_training`.
- **B — Expand royal patrols:** -5 gold, +5 security, -2 power; `royal_patrol_expansion`.

### E138 — The Grain Measure
**Trigger:** food shortage.
A new measuring standard reveals some warehouses have been overstating their reserves.
- **A — Recount everything:** -2 power, +5 trust; `grain_recount`.
- **B — Recount only suspect stores:** +2 power, +2 trust; `targeted_grain_recount`.

### E139 — The Border Lanterns
**Trigger:** border tension + Amara route.
Lantern houses on the frontier become informal warning stations.
- **A — Recognize them as civic infrastructure:** +4 trust, +2 Amara; `frontier_lantern_network`.
- **B — Replace them with soldiers:** +5 security, -3 Amara; `frontier_military_watch`.

E139 establishes frontier-warning infrastructure only; it does **not** by itself declare or resolve `pred.border_crisis`.

### E140 — The Quiet Market
**Trigger:** strong market oversight.
Prices stabilize, but merchants complain that predictable margins are too small to justify risky imports.
- **A — Offer temporary risk insurance:** -4 gold, +3 Ivo, +3 trust; `trade_risk_insurance`.
- **B — Let the market adjust:** +2 power, -2 trust; `market_self_adjustment`.

## Constitutional consequences

### E141 — The Emergency Clause Returns
**Trigger:** `emergency_renewal_possible`, 5+ turns later.
A council quietly asks to renew emergency authority because it was convenient.
- **A — Require a public vote:** +5 trust, -3 power; `emergency_public_vote`.
- **B — Renew through council:** +4 power, -4 trust; `emergency_council_renewal`.

### E142 — The Auditor's Independence
**Trigger:** `auditor_apprentices` or `audit_office`.
The new auditors ask whether the Crown can dismiss them.
- **A — No unilateral dismissal:** +5 trust, -2 power; `auditor_independence`.
- **B — Crown dismissal remains:** +4 power, -3 trust; `auditor_crown_control`.

### E143 — The Army Budget
**Trigger:** military audit route.
The army asks for a permanent emergency reserve.
- **A — Publish the reserve budget:** +4 trust, -2 security.
- **B — Keep it classified:** +4 security, -3 trust.

### E144 — The Guild Seat
**Trigger:** `guild_political_representation`.
The guild's first representative asks whether a merchant can hold a judicial office.
- **A — Separate commerce from judges:** +4 trust, -2 Ivo; `history.guild_representation`; `guild_representation_separated_from_judiciary`.
- **B — Permit it under disclosure rules:** +3 Ivo, +2 power, -3 trust; `history.guild_representation`; `guild_representation_with_disclosure`.

Both choices are producers of the same immutable canonical marker `history.guild_representation`. The legacy trigger `guild_political_representation` is retained as a source-language alias until trigger normalization; it is not a separate runtime fact.

### E145 — The Commons' Court
**Trigger:** `people_charter_endorsed`.
Citizens request a court independent of local nobles.
- **A — Create regional courts:** -4 gold, +6 trust; `regional_courts`.
- **B — Expand existing noble courts:** +2 power, -4 trust; `noble_courts_expanded`.

## Cross-character convergence

### E146 — Six Signatures
**Trigger:** at least four major character routes active.
A constitutional proposal requires signatures from people who normally disagree.
- **A — Publish the disagreement:** +5 trust, -2 power; `six_signatures_public`.
- **B — Collect signatures privately:** +4 power, +2 reputation; `six_signatures_private`.

### E147 — The Refusal to Choose a Hero
**Trigger:** multiple character relationships strong.
The court wants one person named as architect of the reforms.
- **A — Credit the institutions:** +5 trust; `institutional_credit`.
- **B — Name a political architect:** +3 power, +2 to highest relationship, -2 trust; `heroic_reform_credit`.

### E148 — The Last Coalition Meeting
**Trigger:** E146 or strong cross-faction cooperation.
Mara, Rowan, Seris, Ivo, Amara and Toma each demand one guarantee.
- **A — Build a package with mutual concessions:** -3 power, +7 trust; `history.cross_faction_package`; `coalition_candidate_package`; records participation from Mara, Rowan, Seris, Ivo, Amara and Toma.
- **B — Choose only the strongest allies:** +4 power, +2 security, -5 trust; `history.selective_coalition`; `selective_coalition`.

`history.cross_faction_package` is the immutable source marker for the coalition package. It does not by itself satisfy `pred.coalition_cooperation`; that predicate additionally requires cooperation evidence from at least three distinct faction identities and no unresolved coalition-collapse marker.

### E149 — The Cost of Agreement
**Trigger:** `history.cross_faction_package`.
The coalition's concessions are expensive and politically embarrassing.
- **A — Accept the cost openly:** -8 gold, +6 trust; `coalition_cost_public`.
- **B — Hide the cost in future budgets:** +6 gold, -5 trust; `coalition_cost_hidden`.

### E150 — The Question Before Dawn
**Trigger:** late constitutional preparation.
Before the final decision, the player is asked whether the kingdom should be designed to survive a good ruler or a bad one.
- **A — Design for a bad ruler:** -3 power, +6 trust; `constitution_bad_ruler_test`.
- **B — Design around good leadership:** +5 power, -4 trust; `constitution_good_ruler_model`.

## Expansion QA notes

E111–E150 deliberately create delayed consequences, replay information, faction legitimacy, and cross-character convergence. E136/E144/E148 now contain explicit canonical source markers, while legacy trigger aliases remain pending normalization. Border-crisis declaration/resolution is intentionally left open until an authored event with appropriate crisis semantics is selected; E139 is not misclassified as a crisis producer. All nodes remain subject to later reachability, contradiction, and pacing QA.
