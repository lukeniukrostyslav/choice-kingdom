# Choice Kingdom — Graph ↔ Catalog Reconciliation 02

Date: 2026-09-14
Status: **SOURCE-VERIFIED AUDIT — NOT RUNTIME**
Scope: E111–E150, with explicit producer/consumer findings. This document does not promote design adjacency into runtime edges.

## Canonical edge rule
An edge is runtime-eligible only when the target consumes a durable flag/history/thread, explicitly counts source completion, receives a documented delayed consequence, or consumes a canonical derived predicate whose producer contract is defined. Shared characters, themes, or act placement are not enough.

## Verified producer → consumer relationships

| Source | Produced state | Consumer(s) | Disposition |
|---|---|---|---|
| E116 | `auditor_apprentices` | E134, E142, E151 | valid candidate dependency; producer and consumers match the same institutional route |
| E117 | `veterans_examined` / `veteran_patronage` | E125, E170, E182, E222, E245 | valid durable branch family; delayed E182 requires exact timing contract |
| E118 | `equal_estate_law` / `estate_exception` | E162, E183, E242 | valid; E183/E242 must preserve exclusive precedent semantics |
| E119 | `guild_whistleblower` / `guild_internal_review` | E168 | valid guild investigation dependency |
| E121 | `protected_sources` / `named_sources_only` | E180 and information descendants | valid information-route dependency |
| E122 | `tax_transparency` / `tax_private_bargain` | E159, E211, E216 | valid economic/institutional branch family |
| E124 | `public_trade_standards` / `guild_trade_standards` | E168 | valid guild/economic dependency |
| E126 | `river_compact` / `royal_toll_office` | E130, E181, E224 | valid infrastructure/economic family; E181 timing must be canonicalized |
| E127 | `privilege_renewal_refused` / `privilege_renewed_again` | noble-route descendants | valid route markers; exact consumers need full catalog extraction |
| E128 | `steel_replaced` / `steel_repaired` | E185 | valid military callback; E185 also requires later military-crisis condition |
| E131 | `emergency_language_compared` / `precedent_ignored` | E188 and replay/institutional descendants | valid historical-language route; E188 is a delayed/replay-style callback requiring explicit contract |
| E134 | `office_network_mapped` / `map_destroyed_after_copy` | E153, E190, E249 | valid investigation route; both variants must retain distinct information value |
| E135 | `conflicting_testimony_recorded` | E189 | valid evidence callback |
| E139 | `frontier_lantern_network` / `frontier_military_watch` | E171 and border descendants | valid border-route split; do not collapse civilian and military variants |
| E140 | `trade_risk_insurance` / `market_self_adjustment` | E220 | valid economic callback |
| E142 | `auditor_independence` / `auditor_crown_control` | E151, E154 | valid institutional fork |
| E154 | `crown_audited` / `crown_exempt_from_audit` | E155, E211 | valid constitutional/audit dependency |
| E155 | `full_crown_audit_published` / `audit_summary_only` | E211 | valid public-accountability dependency |

## Findings requiring predicate or source reconciliation

1. `food stability`, `winter`, `border crisis`, `road pressure`, `market pressure`, and `information pressure` must not be compiled as raw strings. They require canonical derived predicates or durable markers.
2. E128 → E185 is a genuine producer relationship, but E185 has a compound condition (`cheap_weapons` + later military crisis). The callback must not be treated as guaranteed solely because E128 completed.
3. E131 → E188 is a genuine historical marker relationship; exact delay/replay behavior must be represented explicitly.
4. E134 has two materially different outcomes. `office_network_mapped` and `map_destroyed_after_copy` must not collapse into one boolean because later investigation content depends on the distinction.
5. E139's civilian-lantern and military-watch choices must remain separate because later security/border logic intentionally distinguishes them.
6. Relationship shorthand and route shorthand remain noncanonical until compiled to `rel.*`, `flag.*`, `hist.*`, or `thread.*` identities.

## Consumer-only / unresolved categories

The following recurring prose consumers remain blocked until their producers are exhaustively identified across E01–E270:

- food shortage / food pressure / food crisis;
- winter pressure / severe winter;
- border crisis / border tension;
- low army readiness versus low security;
- market pressure / guild labor tension;
- high information pressure;
- deep investigation / evidence cardinality;
- institutional reform / audit reform;
- simultaneous multi-crisis conditions.

## Production gate impact

- E111–E150 graph reconciliation: **partial, source-verified**.
- Canonical production graph: **blocked** until all ranges are reconciled.
- Production catalog: **blocked** until source ID collision E35–E40 is resolved and trigger vocabulary is canonical.
- Automated reachability: **blocked** until machine-readable representation exists.
- Decision engine: **must not infer dependencies from this audit**; it may consume only the eventual canonical catalog.

## Next pass

1. Reconcile E151–E210 edge-by-edge.
2. Reconcile E211–E270 edge-by-edge.
3. Build a complete consumer-only token list.
4. Compare every producer against duplicate/semantic flag definitions.
5. Resolve E35–E40 source collision using downstream behavior rather than title matching.
6. Lock derived predicate inputs before schema generation.
