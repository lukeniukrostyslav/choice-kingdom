# Choice Kingdom — Canonical Trigger Audit 01

Date: 2026-09-14
Scope: E01–E270
Status: **IN PROGRESS — NOT RUNTIME**

This is a targeted trigger audit. It is deliberately conservative: a trigger is not considered valid merely because a similarly named phrase exists somewhere in prose.

## A. Explicit producer-backed examples

These are examples where the authored catalog visibly creates a same-named fact before later consumption and therefore form candidates for canonical producer/consumer mapping:

| Fact | Known producer examples | Consumers/examples |
|---|---|---|
| `open_petition_hall` | E01 A | E07, E72 |
| `court_first` | E01 B | E06 |
| `audit_office` | E09 A | E24, E73, E81, E85 |
| `merchant_charter` | E08 A | E18, E166 |
| `competitive_market` | E08 B | E18, E126 |
| `toma_recruited` | E13 A | E82, E121, E177 |
| `public_bridge` | E18 B | E45, E75, E87 |
| `quality_armaments` | E17 B | later military route |
| `cheap_weapons` | E17 A | E128, E185 |
| `ledger_public` | E23 A | later transparency routes |
| `evidence_destroyed` | E21 B | later investigation weakening |
| `royal_forgery_proven` | E28 A | E99 and later evidence routes |
| `emergency_renewal_possible` | E48 B | E141, E257 |
| `local_relief_councils` | E40 A | E111, E50 |
| `ledger_network_public` | E43 A | E113 |
| `people_charter_endorsed` | E50 A | E114, E122, E145 |
| `infrastructure_concession` | E45 B | E130 |
| `auditor_independence` | later audit/constitutional route | E151, E154 |
| `crown_audited` | E154 A | E155 |
| `full_crown_audit_published` | E155 A | E211 |
| `regional_courts` | E145 A | E213 |
| `payment_date_crosscheck` | E187 A | E234 |
| `intermediary_chain_traced` | E232 A | E235 |

This table is **not exhaustive**. It is a verified starting inventory from inspected catalog sections, not a claim that all E01–E270 producers are resolved.

## B. Known unresolved or underspecified triggers

These require canonical definitions before engine data can be generated:

- `local_relief_councils` — explicit producer exists, but semantics must be normalized as a durable civic fact.
- `full_ledger_published` — consumer observed; producer needs exact canonical source or replacement with `ledger_public` / `ledger_network_public` if that is the intended meaning.
- `ledger_network_public` — producer exists at E43, but downstream semantics need distinction from generic ledger publication.
- `people_charter_endorsed` — producer exists at E50, but ending/civic semantics need exact scope.
- `temporary_noble_exemption` — referenced by E127; producer/alias must be reconciled with the authored noble-exemption decision.
- `infrastructure_concession` — producer exists at E45 B; exact concession lifetime and renewal behavior need definition.
- `all_voices_heard` — replay metadata, not ordinary run state.
- `mastermind_hunt` — investigation hypothesis; must remain compatible with systemic-mystery canon.
- `warehouse_arson` — replay trigger needs a canonical current-run history/meta producer rather than an informal alternative.
- `document audit route` — derived route phrase; needs explicit predicate/thread.
- `institutional reform` — derived route phrase; needs explicit predicate/thread.
- `commercial route` — derived route phrase; needs explicit predicate/thread.
- `veteran route` — derived route phrase; needs explicit predicate/thread.
- `Amara route` / `Toma route` / `Seris route` / `Rowan route` — shorthand route predicates must map to canonical `thread.*` or explicit conditions.
- `food shortage`, `food pressure`, `severe winter`, `winter severity` — derived conditions requiring deterministic formulas.
- `border tension`, `border pressure`, `border crisis` — derived conditions requiring deterministic formulas.
- `guild leverage`, `guild labor tension`, `strong market oversight` — derived conditions requiring deterministic formulas.
- `information route`, `high information pressure`, `low information trust` — derived information-state predicates requiring deterministic definitions.
- `simultaneous food, border and civic pressure` — composite predicate requiring explicit conjunction rules.

## C. Canonicalization rule

Every trigger must resolve to exactly one of:

1. stable `flag.*` fact;
2. immutable `history.*` marker;
3. active `thread.*` route;
4. deterministic derived predicate over canonical resources/state;
5. versioned `meta.*` replay knowledge;
6. explicit event completion/turn-window condition.

Free-form prose such as “strong route”, “later”, “commercial route” or “winter pressure” cannot remain executable specification.

## D. QA status

- Initial producer/consumer examples: **started**.
- Exhaustive E01–E270 extraction: **not complete**.
- Undefined-trigger scan: **not complete**.
- Duplicate-semantic scan: **not complete**.
- Reachability simulation: **not started**.

This file is an audit artifact, not runtime data.
