# Choice Kingdom — Scenario QA S03: E71–E110 Inventory

Date: 2026-09-15
Scope: E71–E110
Status: **IN PROGRESS — 65%, NOT CLOSED**

## Purpose

Direct source inventory for S03. Authoritative source: `docs/EVENT_EXPANSION_071_110.md`. This artifact records static narrative QA only.

## Event inventory

| Event | Trigger | Outputs / state | Delayed / downstream | Status |
|---|---|---|---|---|
| E71 | E03 + grain policy | `baker_relief` / `price_enforcement` | rationing / black-market effects | VERIFIED SOURCE |
| E72 | `open_petition_hall` or `baker_relief` | `clerk_protected` / `clerk_silenced` | audit evidence / missing inventory trail | VERIFIED SOURCE |
| E73 | `audit_office` | `named_authority` / `overlapping_authority` | accountability vs emergency speed | VERIFIED SOURCE |
| E74 | `nobles_challenged` or temporary exemption | `noble_transition` / `hard_tax_reform` | faction/economic effects | VERIFIED SOURCE |
| E75 | `public_bridge` or `merchant_charter` | `crossing_fund` / `guild_social_contract` | guild legitimacy | VERIFIED SOURCE |
| E76 | `petty_tax_policy` | `umbrella_repealed` / `umbrella_defended` | reputation callback | VERIFIED SOURCE |
| E77 | `central_command` or `emergency_guard_authority` | `shared_rations` / `command_discipline` | army relationship | VERIFIED SOURCE |
| E78 | `public_diplomacy` or joint survey | `old_border_map` / `map_secret` | border settlement | VERIFIED SOURCE |
| E79 | Ivo >=1 | `guild_apprenticeship` / `guild_autonomy` | guild legitimacy | VERIFIED SOURCE |
| E80 | Amara >=1 | `lantern_network` / `volunteer_relief` | winter relief coordination | VERIFIED SOURCE |
| E81 | `audit_office` + `ledger_public_scrutiny` | `handwriting_public` / `handwriting_secret` | alternate evidence route | VERIFIED SOURCE |
| E82 | `toma_recruited` | `source_protection` / `source_demanded` | witness route | VERIFIED SOURCE |
| E83 | Seris >=1 | `reform_guarantee` / `reform_uncertainty` | reform alliance effects | VERIFIED SOURCE |
| E84 | `quiet_market_inquiry` or Toma route | `humanitarian_smuggling` / `total_smuggling_ban` | medicine/profiteering distinction | VERIFIED SOURCE |
| E85 | `audit_office` + missing auditor | `auditor_family_trust` / `official_reassurance` | private letter / credibility | VERIFIED SOURCE |
| E86 | `quiet_accounts` or `ledger_secret` | `paid_silence` / `silence_recorded` | blackmail exposure | VERIFIED SOURCE |
| E87 | `public_bridge` | `durable_bridge` / `cheap_bridge_repair` | supply-route resilience/failure | VERIFIED SOURCE |
| E88 | Rowan >=2 | `patrol_transparency` / `patrol_secret` | military transparency | VERIFIED SOURCE |
| E89 | `noble_advisory_council` or `noble_transition` | `equal_advisory_vote` / `land_weighted_council` | constitutional representation | VERIFIED SOURCE |
| E90 | `lantern_funded` or `lantern_network` | `medical_neutrality` / `noble_medical_priority` | faction/health legitimacy | VERIFIED SOURCE |
| E91 | any two ledger clues | `archive_search` / `house_archive_request` | payment/social beneficiary evidence | VERIFIED SOURCE |
| E92 | `old_border_map` or Toma route | `night_ferry_inspected` / `night_ferry_observed` | diplomatic/network participant | VERIFIED SOURCE |
| E93 | `archive_search` | `duplicate_invoice_witness` / `duplicate_invoice_arrest` | witness disappearance risk | VERIFIED SOURCE |
| E94 | Ivo >=2 + ledger chain | `merchant_books_open` / `guild_confiscation` | trade vs scheme | VERIFIED SOURCE |
| E95 | `flexible_accounts` + failed audit | `mara_independence` / `mara_personal_loyalty` | institutional/personal loyalty | VERIFIED SOURCE |
| E96 | `emergency_guard_authority` | `law_bound_guard` / `personal_guard_oath` | military constitutional route | VERIFIED SOURCE |
| E97 | `seris_witness` or `seris_exposed` | `equal_house_inquiry` / `selective_house_punishment` | house reform/justice | VERIFIED SOURCE |
| E98 | `source_protection` | `protected_testimony` / `open_testimony` | witness availability | VERIFIED SOURCE |
| E99 | `royal_forgery_proven` or `forgery_leverage` | `seal_comparison_public` / `seal_pressure` | coercion/evidence route | VERIFIED SOURCE |
| E100 | 3+ independent evidence routes | `systemic_truth_public` / `conspiracy_narrative` | reform vs control | VERIFIED SOURCE |
| E101 | winter + bridge/river route | `military_icebreakers` / `guild_icebreakers` | supply continuity | VERIFIED SOURCE |
| E102 | trust <60 or severe winter | `palace_kitchens` / `food_vouchers` | price-fixing interaction | VERIFIED SOURCE |
| E103 | `lantern_network` or `volunteer_relief` | `relief_bell_repaired` / `runner_relief` | relief logistics | VERIFIED SOURCE |
| E104 | `shared_crisis_command` or low security | `soldier_charter` / `mutiny_suppressed` | military/constitutional consequence | VERIFIED SOURCE; trigger requires reconciliation |
| E105 | `land_weighted_council` or Seris >=2 | `noble_shelter_public` / `noble_shelter_patronage` | shelter/patronage | VERIFIED SOURCE |
| E106 | guild route + winter | `merchant_restraint` / `merchant_accusation` | guild/winter legitimacy | VERIFIED SOURCE |
| E107 | diplomatic route + border crisis | `child_returned` / `child_leverage` | international reputation | VERIFIED SOURCE |
| E108 | warehouse fire + investigation | `ash_ledger_preserved` / `ash_ledger_selective` | investigation depth | VERIFIED SOURCE |
| E109 | winter + Amara <=0 | `lantern_independence` / `lantern_centralized` | welfare institutional structure | VERIFIED SOURCE |
| E110 | late Act IV + 2+ character routes | `three_letters_public` / `three_letters_private` | constitutional debate / coalition promises | VERIFIED SOURCE |

## Cross-catalog semantic findings

### 1. E95 introduces a near-semantic duplicate of the E36 Mara decision

- E36-A: `mara_independent_mandate`.
- E95-A: `mara_independence`.

These are distinct literal IDs but appear to express the same underlying concept: independent authority for Mara. This is a **semantic duplicate candidate**, not yet a proven contradiction. Canonical state vocabulary must decide whether they are intentionally different (mandate scope/time/authority) or one should be normalized.

### 2. E37 and E96 contain parallel military-oath concepts

- E37: `army_law_oath` / `army_crown_oath`.
- E96: `law_bound_guard` / `personal_guard_oath`.

They may represent separate army-vs-guard institutions, but the source does not currently encode that distinction explicitly. This is a semantic-collision candidate requiring canonical normalization before engine contracts.

### 3. E104 references `shared_crisis_command`

The trigger is explicit in the source, but no producer is established in the S03 source itself. A repository search did not return a matching occurrence at this checkpoint. This must be treated as **OPEN / potentially undefined producer** until the canonical catalog proves a producer or the trigger is rewritten.

### 4. E108 uses "investigation depth" as a state effect

This is not yet a canonical state key in the inventory. It must be normalized into the machine state vocabulary before engine implementation.

### 5. Predicate-like prose triggers remain contract work

Examples include "any two ledger clues", "three independent evidence routes", "severe winter", "diplomatic route", "border crisis", and "late Act IV". These are valid authored intentions but not yet executable contracts.

## S03 gate result

- Event/trigger/output inventory: **SOURCE-LEVEL VERIFIED** for E71–E110.
- Cross-catalog semantic collision scan: **PARTIAL**; E95/E36 and E96/E37 require explicit normalization.
- Undefined-producer scan: **OPEN**; E104 `shared_crisis_command` requires closure.
- Delayed/callback contract closure: **OPEN**, deferred to S10.
- Global producer/consumer closure: **OPEN**, S08.

**S03 progress: 65% — not complete.**

Overall Scenario QA remains **65%**; no global percentage increase is claimed from this source inventory alone.
