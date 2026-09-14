# Choice Kingdom — Producer / Consumer Inventory 02

Date: 2026-09-14
Scope: verified initial spine E01–E34 and current Act V E35–E70 source text; reconciled against known inventory findings.
Status: **VERIFIED PARTIAL — EXHAUSTIVE INVENTORY STILL OPEN**

## Purpose

Close the previously missing producer/consumer coverage for the original spine and the current Act V source. This is still an audit artifact and must not be consumed as production data until all E01–E270 ranges are reconciled.

## E01–E34 explicit durable markers

| Producer | Marker | Observed downstream use / implication |
|---|---|---|
| E01 A | `open_petition_hall` | E07 market whispers; later civic/public-access routes |
| E01 B | `court_first` | E06 noble pressure; court/noble route |
| E02 A | `emergency_decree_used` | emergency-response and institutional consequences |
| E02 B | `decree_investigation` | E09, E28 hidden-ledger/forgery investigation |
| E03 A | grain reserves change | later winter/grain pressure; requires canonical food predicate rather than a new resource |
| E03 B | `free_grain_imports` | market/prosperity and later price-fixing risk |
| E04 A | `ledger_public` / `ledger_public_scrutiny` concept | public evidence/institutional scrutiny route |
| E04 B | `quiet_accounts` | secrecy/legitimacy route |
| E05 A | guard audit concept | procurement-fraud investigation; needs canonical audit thread marker |
| E05 B | `emergency_guard_authority` | later expanded military/emergency-power route |
| E06 A | `nobles_challenged` | noble conflict/constitutional route |
| E06 B | temporary noble exemption concept | E127 renewal chain; canonical marker must be explicit |
| E07 A | public raid / innocent-risk outcome | market/security/reputation consequence; durable marker only if later content depends on it |
| E07 B | `quiet_market_inquiry` | E13/Toma and E21/evidence routes |
| E08 A | `merchant_charter` | E18 toll, E19 price fixing, E63 Golden Compact and later commercial routes |
| E08 B | `competitive_market` | E18/E45/E126/E140 and later market-governance routes |
| E09 A | `audit_office` | E24, E142, E151 and institutional audit chain |
| E09 B | `flexible_accounts` | emergency flexibility vs corruption detection route |
| E10 A | `central_command` | security/military governance route |
| E10 B | `local_command` | E16 border marker and decentralized defense route |
| E11 A | `noble_advisory_council` | noble/constitutional representation route |
| E11 B | reform-alliance concept | requires explicit history/thread marker if consumed later |
| E12 A | `lantern_funded` | Amara/welfare route and winter resilience |
| E12 B | fee-based clinic concept | welfare/Amara negative route; requires marker if later content depends on it |
| E13 A | `toma_recruited` | Toma/information route; E21 and later information nodes |
| E13 B | `toma_rejected` | information reliability penalty; should be explicit history/state if later consumed |
| E14 A | `market_reform` | E140 and market governance routes |
| E14 B | `petty_tax_policy` | recurring callback/reputation route |
| E15 A | `public_diplomacy` | E16 peaceful border settlement and reputation route |
| E15 B | private diplomacy concept | candid diplomatic branch; requires durable marker if consumed |
| E16 A | military border replacement | military escalation pressure; requires canonical border marker |
| E16 B | joint survey concept | diplomatic border route; durable marker required if later consumed |
| E17 A | cheap weapons / durability | E128/E185 delayed failure chain; canonical `cheap_weapons` marker required |
| E17 B | `quality_armaments` | military procurement quality route |
| E18 A | toll grant | repeated toll policy / E19 and E130-style economic callbacks |
| E18 B | `public_bridge` | E45/E126/E243/E69 infrastructure route |
| E19 A | `guild_broken` | guild relationship/economic route |
| E19 B | temporary price ceiling | E246 policy-memory route; exact marker needed |
| E20 A | `soldier_compensation` | Rowan/security/social legitimacy route |
| E20 B | private handling | negative Rowan/trust route; marker needed only if later consumed |
| E21 A | ledger evidence investigation | `ledger_fragment_a` / hidden-ledger route |
| E21 B | `evidence_destroyed` | blocks/weakens investigation and replay information |
| E22 A | festival held | E129 delayed memory and possible security callback |
| E22 B | festival cancelled | trust/power branch; marker required if later consumed |
| E23 A | `ledger_public` | public inquiry / E113/E211 evidence-access routes |
| E23 B | `ledger_secret` | secret evidence route / reconstruction |
| E24 A | `auditor_missing_public` | E25 route |
| E24 B | quiet search concept | E25 if Toma; requires explicit canonical investigation marker |
| E25 A | raid customs house | security/evidence outcome; marker if later consumed |
| E25 B | follow route | stronger evidence + hidden reveal; needs exact delayed/thread marker |
| E26 A | `seris_witness` | E44, E42, investigation/constitutional routes |
| E26 B | `seris_exposed` | E44 and noble legitimacy route |
| E27 A | immediate arrest | false-dossier/institutional scandal route; exact marker needed if consumed |
| E27 B | dossier tested | decoy discovery; requires canonical evidence marker |
| E28 A | `royal_forgery_proven` | institutional/constitutional evidence and endings |
| E28 B | `forgery_leverage` | power/blackmail route |
| E29 A | granary release | winter/food resilience predicate |
| E29 B | market rationing | winter/food + market predicate |
| E30 A | rescue focus | arson investigation/security tradeoff |
| E30 B | district sealed | security/trust route |
| E31 A | `war_mobilization` | military escalation/endgame route |
| E31 B | white-banner diplomacy | diplomatic border route |
| E32 A | priority choice | neglected-crisis escalation; exact history required for downstream E255-style conditions |
| E32 B | `shared_crisis_command` | multi-character/cross-faction route |

## E35–E70 current Act V markers

The current Act V source contains a dense explicit marker network. Key verified producers include:

- E35: `emergency_expiry_announced`, `emergency_expiry_flexible`
- E36: `mara_independent_mandate`, `mara_resigned`
- E37: `army_law_oath`, `army_crown_oath`
- E38: `hereditary_seats_limited`, `hereditary_seats_rejected`
- E39: `guild_emergency_credit`, `civic_war_bonds`
- E40: `local_relief_councils`, `central_relief`
- E41: `crate_route_traced`, `customs_accused`
- E42: `witness_protected`, `witness_public`
- E43: `ledger_network_public`, `ledger_network_compromised`
- E44: `houses_self_reconcile`, `house_arms_restricted`
- E45: `public_infrastructure_trust`, `infrastructure_concession`
- E46: `lawful_refusal_defended`, `lawful_refusal_punished`
- E47: `constitution_first`, `crown_powers_first`
- E48: `permanent_emergency_blocked`, `emergency_renewal_possible`
- E49: `guild_political_representation`, `guild_political_exclusion`
- E50: `people_charter_endorsed`, `people_charter_delayed`
- E51: `mutual_veto`, `crown_veto`, `public_renewal_rule`
- E52: `military_audit_final`, `military_patronage_final`
- E53: `full_ledger_published`, `verified_ledger_only`
- E54: `seris_constitutional_office`, `nobility_equal_under_law`
- E55: `guild_books_submitted`, `guild_books_sealed`
- E56: `relief_guarantee`, `relief_discretion`
- E57: `systemic_corruption_confirmed`, `mastermind_hunt`
- E58: `final_emergency_invoked`, `final_emergency_refused`
- E59: `mandate_renewed_legally`, `succession_limited`
- E60: `all_voices_heard`, `crown_decides_alone`
- E61–E67: ending conditions rather than ordinary producer markers
- E68+: post-ending/replay material

## Reconciliation risks found in this pass

1. Some E01–E34 outcomes are described in prose but are later referenced as if they were stable markers. These must receive explicit history/thread identifiers before schema lock.
2. The current Act V marker vocabulary is much more explicit than the initial E01–E34 spine, so canonicalization must not invent equivalent flags merely from prose similarity.
3. E35–E40 current markers are valid only for the expanded Act V source; the legacy E35–E40 definitions remain separate until ID reconciliation is complete.
4. Resource-only consequences (gold/trust/security/power/reputation) are not automatically durable producers unless a later condition explicitly needs the decision itself.
5. The exact source of `emergency_power`, `military_dependency`, `distributed institutions`, `stable security`, and similar ending predicates is still not fully enumerated and requires derived-predicate definitions plus reachability simulation.

## Next gate

This closes a major missing inventory slice but does not make the producer/consumer audit exhaustive. Remaining source coverage must include E71–E110 and the complete E191–E210/E264–E270 ranges, followed by automated extraction/checks.
