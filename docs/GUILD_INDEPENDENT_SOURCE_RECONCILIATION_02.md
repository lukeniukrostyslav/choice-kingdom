# Choice Kingdom — Guild Independent Source Reconciliation 02

Status: **P0 SOURCE-LEVEL QA — PROVISIONAL, NOT ENGINE IMPLEMENTATION**
Scope: canonical guild-influence predicate inputs.

## Reconciled domain set

`pred.guild_influence_strong` requires at least two distinct institutional domains. The following authored facts are accepted as candidate domain identities:

| Domain | Source fact | Qualification rule |
|---|---|---|
| Representation | `history.guild_representation` | Counts once for the representation domain. Relationship with Ivo never substitutes for this fact. |
| Tribunal | `guild_tribunal_independent` from E168-A | Counts once for independent dispute-resolution authority. E168 trigger text alone does not count. |
| Market / credit | explicit institutional leverage from E165/E166 | Must be an authored leverage/oversight fact, not merely a commercial relationship or repeated market outcome. |
| Logistics | `history.guild_logistics_cooperation` from qualified E194-A | Counts only with neutral-inspection cooperation; immunity-only E194-B does not qualify. |

## Anti-double-counting

- `history.guild_representation` and later representation consequences remain one domain.
- E165 and E166 may not be counted as two domains merely because they are separate events if both prove only market/commercial leverage.
- E194-A cooperation is a logistics domain; E194-B immunity is explicitly excluded.
- `rel.ivo` is not an institutional domain.
- A consumer such as E200 cannot create missing guild-influence evidence.

## Current verdict

**PARTIAL → source identities reconciled, but not CLOSED.** The authoritative E01–E272 catalog still needs event-by-event confirmation that each referenced key is actually written exactly as contracted and that no later consumer relies on an absent/renamed key.

## Required closure checks

1. Exact key match for E49/E144 representation facts.
2. Exact key match for E165/E166 market-credit institutional facts.
3. Exact key match for E168-A independent tribunal.
4. Exact key match for E194-A qualified logistics cooperation.
5. Producer-before-consumer ordering through E200 and all later consumers.
6. No duplicate-domain counting.
7. No route-count or relationship-score substitution.

Only after these checks pass may the derived predicate be promoted to CLOSED and admitted to production schema design.
