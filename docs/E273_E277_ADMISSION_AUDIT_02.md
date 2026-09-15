# Choice Kingdom — E273–E277 Admission Audit 02

Status: **NOT ADMITTED — pending frozen-catalog decision**

Date: 2026-09-15

## Scope

E273–E277 are authored producer-expansion candidates outside the frozen E01–E272 catalog. This audit checks whether they can be admitted without silently changing the semantics of the existing campaign.

## Findings

| Node | Producer role | Admission status | Reason |
|---|---|---|---|
| E273 | `pred.food_stable` | BLOCKED | Explicit producer exists, but the frozen E01–E272 catalog does not yet contain a complete food-disruption lifecycle and consumer/recovery contract. Admission would create a predicate whose active/clear semantics are incomplete. |
| E274 | `pred.market_pressure` | BLOCKED | Explicit producer exists, but no frozen producer/consumer lifecycle contract has been reconciled for the new predicate. |
| E275 | `pred.guild_labor_tension` | BLOCKED | Producer/clear semantics are explicit, but admission requires checking all guild-labor consumers and ensuring no existing event already encodes the same state under another flag. |
| E276 | `pred.information_pressure_high` | BLOCKED | Producer/clear semantics are explicit and correctly separated from `rel.toma`, but downstream consumer inventory and alias normalization are not yet frozen. |
| E277 | transport recovery | BLOCKED | E136-A/B are already the canonical recovery producers for the current transport-disruption cycle. E277 must not become a competing kingdom-wide recovery producer without an explicit lifecycle rule. |

## Important conclusions

1. No engine-side fallback should synthesize any of these predicates.
2. E276 correctly rejects relationship score as a substitute for the predicate.
3. E277 cannot be admitted merely because its narrative is useful; it overlaps an already canonical E136 recovery path.
4. E273–E276 require consumer inventories before admission.
5. Admission must be a deliberate catalog change, not an implicit runtime expansion.

## Required gate before admission

For each candidate, all of the following must be proven:

- exact trigger normalization;
- at least one reachable upstream path from the frozen campaign;
- complete consumer inventory;
- no duplicate or semantically competing producer;
- active-state semantics;
- clear/recovery semantics where applicable;
- save/load persistence semantics;
- replay isolation;
- deterministic same-turn ordering;
- compatibility with ending and final-charter contracts;
- source-level re-read after any catalog modification.

## Current decision

**Keep E273–E277 outside the production catalog.** Continue reconciling E01–E272 first. No validator or engine rule should consume these candidate predicates as if they were admitted production facts.
