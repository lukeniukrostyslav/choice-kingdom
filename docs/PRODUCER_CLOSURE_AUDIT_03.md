# Choice Kingdom — Producer Closure Audit 03

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — NOT PRODUCTION SCHEMA**
Scope: E01–E110 producer backfill against the canonical route/predicate namespaces.

## Purpose

Audit early and mid-campaign authored outputs that can legitimately activate the route families later consumed by E111–E270. This closes the gap where late events had canonical consumers but their earliest durable producers were not yet enumerated.

## Rules

- A relationship score is not a route activation by itself.
- A thematic graph edge is not a producer.
- Numeric resources remain resources; derived pressures are predicates, not new resources.
- A marker is canonical only when an authored choice explicitly establishes durable meaning.
- Existing source semantics are preserved; this audit does not invent new player choices.

## Producer families

| Canonical family | Early source evidence | Status | Required follow-up |
|---|---|---|---|
| `thread.mara_audit` | E01–E03 audit/institutional choices; later E81/E85 | PARTIAL | enumerate exact first activation marker and continuation rule |
| `thread.rowan_security` | early guard/security decisions; E77/E88/E96 | PARTIAL | freeze route activation separately from `resource.security` |
| `thread.seris_houses` | early noble/council decisions; E74/E89/E97 | PARTIAL | freeze first durable house-route markers |
| `thread.ivo_market` | E75/E79/E84/E94 | PARTIAL | distinguish merchant route from generic gold/market pressure |
| `thread.amara_civic` | E80/E90/E103 | PARTIAL | distinguish civic route from generic trust |
| `thread.toma_information` | E82/E84/E93/E98 | PARTIAL | distinguish information route from raw evidence count |
| `thread.ledger_investigation` | E81/E85/E86/E91/E93/E94/E99/E100 | STRONG CANDIDATE | enumerate independent evidence IDs and exact chain activation |
| `thread.winter_crisis` | E101–E103/E109 | PARTIAL | define winter severity and crisis-history producers |
| `thread.border_crisis` | E92/E107/E110 and border events | PARTIAL | separate border tension/escalation from security |
| `thread.archive` | E91/E93/E99/E100 | PARTIAL | define durable archive access marker |
| `thread.coalition` | E110 and later E146/E148 | PARTIAL | define first coalition state without conflating character count |
| `thread.succession` | E37-era/Act V succession material and later E197 | OPEN | reconcile canonical Act V source before engine freeze |
| `thread.budget_reform` | E76/E81/E94/E95 institutional/ledger decisions | PARTIAL | distinguish budget reform from audit/institutional reform |
| `thread.document_audit` | E81/E85/E99/E100 | STRONG CANDIDATE | exact durable audit marker still needs canonical naming |

## High-value verified outputs from E71–E110

The source catalog contains explicit authored outputs that can serve as durable history/evidence producers, including:

- E81: `handwriting_public` / `handwriting_secret`
- E82: `source_protection` / `source_demanded`
- E83: `reform_guarantee` / `reform_uncertainty`
- E84: `humanitarian_smuggling` / `total_smuggling_ban`
- E85: `auditor_family_trust` / `official_reassurance`
- E86: `paid_silence` / `silence_recorded`
- E87: `durable_bridge` / `cheap_bridge_repair`
- E88: `patrol_transparency` / `patrol_secret`
- E89: `equal_advisory_vote` / `land_weighted_council`
- E90: `medical_neutrality` / `noble_medical_priority`
- E91: `archive_search` / `house_archive_request`
- E92: `night_ferry_inspected` / `night_ferry_observed`
- E93: `duplicate_invoice_witness` / `duplicate_invoice_arrest`
- E94: `merchant_books_open` / `guild_confiscation`
- E95: `mara_independence` / `mara_personal_loyalty`
- E96: `law_bound_guard` / `personal_guard_oath`
- E97: `equal_house_inquiry` / `selective_house_punishment`
- E98: `protected_testimony` / `open_testimony`
- E99: `seal_comparison_public` / `seal_pressure`
- E100: `systemic_truth_public` / `conspiracy_narrative`
- E101: `military_icebreakers` / `guild_icebreakers`
- E102: `palace_kitchens` / `food_vouchers`
- E103: `relief_bell_repaired` / `runner_relief`
- E104: `soldier_charter` / `mutiny_suppressed`
- E105: `noble_shelter_public` / `noble_shelter_patronage`
- E106: `merchant_restraint` / `merchant_accusation`
- E107: `child_returned` / `child_leverage`
- E108: `ash_ledger_preserved` / `ash_ledger_selective`
- E109: `lantern_independence` / `lantern_centralized`
- E110: `three_letters_public` / `three_letters_private`

These are **source facts**, not automatic canonical namespaces. Each must be mapped only where its semantics are consumed downstream.

## Critical early-route closure tasks

### Investigation
E81/E85/E91/E93/E94/E99/E100 provide a credible authored investigation chain. The remaining work is to assign immutable evidence IDs and define which combinations satisfy `pred.evidence_routes_3` and ultimately `pred.systemic_explanation_verified`.

### Winter
E101–E103 clearly author winter-response decisions, but the existence of a winter event does not itself establish `pred.winter_severe`. The severity rule must be defined from source state/history and remain deterministic.

### Border
E92/E107 and later E171–E195 support a border route, but border pressure must remain separate from `resource.security` and military relationship values.

### Civic / Amara
E90/E103/E109 provide civic and humanitarian outputs. These should activate `thread.amara_civic` only through explicit route semantics, not merely because trust increased.

### Market / Ivo
E94/E101/E106 provide strong merchant-route evidence. `rel.ivo` can support narrative affinity but cannot by itself satisfy `pred.guild_influence_strong` or `pred.guild_logistics_cooperation`.

### Institutional / Mara
E81/E85/E95 establish audit-related decisions. They support `thread.mara_audit`, while `thread.institutional_reform` and `pred.budget_reform` require separate downstream qualification.

## Unresolved / deliberately not closed

- exact first producer of every route thread;
- food pressure/stability predicate formulas;
- winter severity threshold/history formula;
- border escalation predicate;
- military readiness versus security;
- evidence cardinality and independence rules;
- constitutional preparation threshold;
- replay-to-current-run transfer rules;
- E35–E40 legacy-ending reference migration;
- ending reachability simulations.

## Gate result

Early producer coverage is materially improved, but this is still **not sufficient for production schema freeze**. The next required artifact is a single E01–E270 producer/consumer registry with one row per canonical predicate/thread/history key and explicit source IDs.
