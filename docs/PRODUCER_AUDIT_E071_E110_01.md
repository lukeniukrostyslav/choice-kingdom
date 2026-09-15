# Choice Kingdom — Producer / Consumer Audit E071–E110

Status: **SOURCE-LEVEL QA — NOT ENGINE INPUT**

Purpose: inventory authored durable outputs in E071–E110 and identify trigger contracts that must be frozen before machine-readable production data is created.

## Output inventory

| Event | Authored durable output(s) | Main downstream contract / risk |
|---|---|---|
| E071 | `baker_relief`; `price_enforcement` | delayed cooperation / black-market effects need canonical predicates |
| E072 | `clerk_protected`; `clerk_silenced` | protection semantics need exact-fact identity |
| E073 | `named_authority`; `overlapping_authority` | authority route needs explicit consumers |
| E074 | `noble_transition`; `hard_tax_reform` | noble transition/exception route needs canonicalization |
| E075 | `crossing_fund`; `guild_social_contract` | infrastructure/social-contract route mapping |
| E076 | `umbrella_repealed`; `umbrella_defended` | delayed reputation callback needs source identity |
| E077 | `shared_rations`; `command_discipline` | military readiness/character derivation |
| E078 | `old_border_map`; `map_secret` | evidence route distinct from active border crisis |
| E079 | `guild_apprenticeship`; `guild_autonomy` | guild route predicate needs explicit derivation |
| E080 | `lantern_network`; `volunteer_relief` | Amara/civic relief route derivation |
| E081 | `handwriting_public`; `handwriting_secret` | evidence counting must avoid double-counting |
| E082 | `source_protection`; `source_demanded` | delayed witness availability needs source-choice/due-turn identity |
| E083 | `reform_guarantee`; `reform_uncertainty` | institutional reform derivation remains open |
| E084 | `humanitarian_smuggling`; `total_smuggling_ban` | medicine/food route must stay distinct from generic food pressure |
| E085 | `auditor_family_trust`; `official_reassurance` | delayed private-letter callback needs exact source identity |
| E086 | `paid_silence`; `silence_recorded` | blackmail exposure must become real delayed state |
| E087 | `durable_bridge`; `cheap_bridge_repair` | transport stability/failure predicates need canonical derivation |
| E088 | `patrol_transparency`; `patrol_secret` | military-information predicates need explicit formulas |
| E089 | `equal_advisory_vote`; `land_weighted_council` | constitutional route distinction; E105 consumes latter |
| E090 | `medical_neutrality`; `noble_medical_priority` | Amara route / medical-neutrality predicate |
| E091 | `archive_search`; `house_archive_request` | independent evidence-source identity required |
| E092 | `night_ferry_inspected`; `night_ferry_observed` | delayed participant callback/source identity |
| E093 | `duplicate_invoice_witness`; `duplicate_invoice_arrest` | evidence cardinality and disappearance scheduling |
| E094 | `merchant_books_open`; `guild_confiscation` | commercial evidence distinct from guild influence |
| E095 | `mara_independence`; `mara_personal_loyalty` | must remain distinct from E36/E226 `mara_independent_mandate` |
| E096 | `law_bound_guard`; `personal_guard_oath` | military constitutional route mapping |
| E097 | `equal_house_inquiry`; `selective_house_punishment` | noble investigation route, not relationship alone |
| E098 | `protected_testimony`; `open_testimony` | witness protection and evidence counting |
| E099 | `seal_comparison_public`; `seal_pressure` | consumes unresolved forgery-route producers |
| E100 | `systemic_truth_public`; `conspiracy_narrative` | systemic-vs-mastermind semantic fork |
| E101 | `military_icebreakers`; `guild_icebreakers` | transport recovery; does not itself create active disruption |
| E102 | `palace_kitchens`; `food_vouchers` | mitigation must not redefine food-crisis severity implicitly |
| E103 | `relief_bell_repaired`; `runner_relief` | relief logistics route; no automatic Amara equivalence |
| E104 | `soldier_charter`; `mutiny_suppressed` | military constitutional/readiness route |
| E105 | `noble_shelter_public`; `noble_shelter_patronage` | noble/civic route identity |
| E106 | `merchant_restraint`; `merchant_accusation` | market oversight/influence derivation remains open |
| E107 | `child_returned`; `child_leverage` | diplomatic route; must not automatically create border crisis |
| E108 | `ash_ledger_preserved`; `ash_ledger_selective` | independent investigation evidence source |
| E109 | `lantern_independence`; `lantern_centralized` | Amara institutional route distinct from relationship |
| E110 | `three_letters_public`; `three_letters_private` | coalition/constitutional route; promise-keeping semantics required |

## High-priority findings

1. E095 has a semantic collision risk with E36/E226; the facts must remain separate.
2. E081/E091/E093/E094/E099/E100 contribute evidence, but later “two/three clues” predicates need independent source IDs rather than raw flag counts.
3. E071/E076/E082/E085/E086/E087/E092/E093 contain delayed consequences that require source-choice identity, due turn, cancellation and exactly-once semantics.
4. Guild, Amara, Rowan, Seris and institutional-reform routes are not safely derivable from relationship thresholds alone.
5. E087/E101 provide transport repair/response outputs but do not establish the separate active transport-disruption producer.
6. E102 mitigates food pressure but does not define the underlying crisis severity.
7. E099 consumes `royal_forgery_proven` / `forgery_leverage`; canonical producers must be identified in earlier events.
8. E110 proposal states are not equivalent to final coalition cooperation.

## Gate

Source-level output extraction: **PASS for this range**.

Canonical production schema: **BLOCKED pending contract freeze**.

Runtime reachability: **NOT VERIFIED**.

Validator: intentionally not created until canonical data contracts are frozen.
