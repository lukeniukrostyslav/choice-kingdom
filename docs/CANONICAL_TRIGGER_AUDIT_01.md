# Choice Kingdom — Canonical Trigger Audit 01

Date: 2026-09-15  
Scope: E01–E272  
Status: **IN PROGRESS — NOT RUNTIME**

This is a conservative trigger audit. A trigger is not considered valid merely because a similarly named phrase exists somewhere in prose.

## A. Explicit producer-backed examples

| Fact | Known producer examples | Consumers/examples |
|---|---|---|
| `open_petition_hall` | E01-A | E07, E72 |
| `court_first` | E01-B | E06 |
| `audit_office` | E09-A | E24, E73, E81, E85 |
| `merchant_charter` | E08-A | E18, E166 |
| `competitive_market` | E08-B | E18, E126 |
| `toma_recruited` | E13-A | E82, E121, E177 |
| `public_bridge` | E18-B | E45, E75, E87, delayed E243 |
| `quality_armaments` | E17-B | later military route |
| `cheap_weapons` | E17-A | E128, E185 |
| `ledger_public` | E23-A | later transparency routes |
| `evidence_destroyed` | E21-B | later investigation weakening |
| `royal_forgery_proven` | E28-A | E99 and later evidence routes |
| `emergency_renewal_possible` | E48-B | E141, E257 |
| `local_relief_councils` | E40-A | E111, E50 |
| `ledger_network_public` | E43-A | E113 |
| `people_charter_endorsed` | E50-A | E114, E122, E145 |
| `infrastructure_concession` | E45-B | E130 |
| `crown_audited` | E154-A | E155 |
| `full_crown_audit_published` | E155-A | E211 |
| `regional_courts` | E145-A | E213 |
| `payment_date_crosscheck` | E187-A | E234 |
| `intermediary_chain_traced` | E232-A | E235 |
| `history.guild_logistics_cooperation` | E136-B | E194-qualified downstream route |
| `pred.winter_severe` | E29-A/B | downstream winter routes |
| `pred.transport_disruption` | E32; clear E136-A/B | E192 |
| `pred.border_crisis` | E271-A; clear E272-A/B | E195 and border endgame routes |

This table is still **not exhaustive**. It is the verified producer-backed inventory currently available for canonical QA.

## B. Known unresolved or underspecified triggers

These require canonical definitions before engine data can be generated:

- `full_ledger_published` — consumer observed; exact producer/alias unresolved.
- `temporary_noble_exemption` — producer/alias reconciliation required.
- `infrastructure_concession` — producer exists; lifetime/renewal behavior unresolved.
- `all_voices_heard` — replay metadata, not ordinary run state.
- `mastermind_hunt` — investigation hypothesis requiring explicit canonical representation.
- `warehouse_arson` — replay/current-run representation must be explicit.
- `document audit route`, `institutional reform`, `commercial route`, `veteran route` — prose route phrases require explicit canonical predicates/threads.
- `Amara route`, `Toma route`, `Seris route`, `Rowan route` — shorthand route phrases require canonical mapping.
- food/winter pressure phrases — deterministic derived conditions required.
- border tension/pressure phrases — deterministic derived conditions required.
- guild leverage/labor-tension/market-oversight phrases — deterministic derived conditions required.
- information pressure/trust route phrases — deterministic definitions required.
- simultaneous food/border/civic pressure — explicit conjunction contract required.
- E184 `secret evidence route` — no source-closed producer.
- E245 `compensation route` — intentionally unresolved across distinct compensation facts.
- E246 `price ceiling` — exact candidate is `winter_rent_ceiling`; generic alias not frozen.

## C. Canonicalization rule

Every executable trigger must resolve to exactly one of:

1. stable `flag.*` fact;
2. immutable `history.*` marker;
3. active `thread.*` route;
4. deterministic derived predicate over canonical resources/state;
5. versioned `meta.*` replay knowledge;
6. explicit event completion/turn-window condition.

Free-form prose such as “strong route”, “later”, “commercial route” or “winter pressure” cannot remain executable specification.

## D. QA status

- Producer/consumer examples: **started and expanded through E272**.
- Exhaustive E01–E272 extraction: **not complete**.
- Undefined-trigger scan: **not complete**.
- Duplicate-semantic scan: **not complete**.
- Predicate dependency-cycle scan: **not complete**.
- Reachability simulation: **not started**.

The detailed machine-inventory gate is recorded in `docs/MACHINE_INVENTORY_PASS_01.md`. The E243 normalization correction is recorded in `docs/DELAYED_GRAPH_EDGE_CORRECTION_01.md` and `docs/DELAYED_GRAPH_EDGE_AUDIT_01.md`.

This file is an audit artifact, not runtime data.
