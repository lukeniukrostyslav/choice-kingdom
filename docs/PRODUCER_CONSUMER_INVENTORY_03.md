# Choice Kingdom — Producer → Consumer Inventory 03

Date: 2026-09-14
Status: **QA EXTRACTION CHECKPOINT — NOT PRODUCTION SCHEMA**

## Purpose

Consolidate the source-verified E111–E150 relationships from the graph/catalog reconciliation pass. This inventory is intentionally conservative: an item is marked verified only when the authored catalog names a durable effect that a later event consumes.

## Verified durable relationships

- `auditor_apprentices` → E134, E142, E151.
- `veterans_examined` / `veteran_patronage` → E125, E170, E182, E222, E245.
- `equal_estate_law` / `estate_exception` → E162, E183, E242.
- `guild_whistleblower` / `guild_internal_review` → E168.
- `protected_sources` / `named_sources_only` → E180 and information descendants.
- `tax_transparency` / `tax_private_bargain` → E159, E211, E216.
- `public_trade_standards` / `guild_trade_standards` → E168.
- `river_compact` / `royal_toll_office` → E130, E181, E224.
- `privilege_renewal_refused` / `privilege_renewed_again` → noble-route descendants.
- `steel_replaced` / `steel_repaired` → E185.
- `emergency_language_compared` / `precedent_ignored` → E188 and institutional/replay descendants.
- `office_network_mapped` / `map_destroyed_after_copy` → E153, E190, E249.
- `conflicting_testimony_recorded` → E189.
- `frontier_lantern_network` / `frontier_military_watch` → E171 and border descendants.
- `trade_risk_insurance` / `market_self_adjustment` → E220.
- `auditor_independence` / `auditor_crown_control` → E151, E154.
- `crown_audited` / `crown_exempt_from_audit` → E155, E211.
- `full_crown_audit_published` / `audit_summary_only` → E211.

## Important semantic distinctions

1. `office_network_mapped` and `map_destroyed_after_copy` are separate outcomes; they cannot be represented as one boolean.
2. `frontier_lantern_network` and `frontier_military_watch` are separate route markers because civilian and military authority have different downstream consequences.
3. `veterans_examined` and `veteran_patronage` are separate histories; the latter creates the delayed promise callback E182.
4. `equal_estate_law` and `estate_exception` create opposite precedent paths and must remain mutually distinguishable.
5. `crown_audited` and `crown_exempt_from_audit` are constitutional opposites, not generic audit status.
6. `steel_replaced` / `steel_repaired` do not by themselves guarantee E185; E185 also requires the later military-crisis condition.

## Consumer-only families still requiring global extraction

- food pressure / food crisis;
- winter severity;
- border crisis/tension;
- market pressure;
- guild labor tension;
- information pressure;
- evidence-route cardinality;
- institutional reform;
- reform spending;
- simultaneous three-crisis pressure.

## Gate

This inventory improves canonical confidence but does not authorize engine implementation. Full E01–E270 producer/consumer extraction, source collision resolution, predicate locking and reachability simulation remain mandatory.
