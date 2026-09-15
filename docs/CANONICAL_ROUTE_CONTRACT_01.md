# Choice Kingdom — Canonical Route Contract 01

Status: **PRODUCTION-CONTRACT DRAFT — NOT RUNTIME IMPLEMENTATION**

Purpose: define route identity independently from relationship numbers so late-game events cannot become reachable merely because a character score happens to be high.

## 1. Core rule

A relationship value (`rel.*`) is numeric state. A route identity is a separate canonical fact derived from authored route milestones/history. A route predicate must never be defined as `rel.character >= N` unless the event explicitly intends a purely numeric relationship gate.

## 2. Canonical route identities

| Route | Canonical identity | Minimum evidence of activation |
|---|---|---|
| Rowan / military-constitutional | `thread.military_constitutional` | At least one authored military-constitutional decision plus a qualifying follow-up/commitment; relationship score alone is insufficient. |
| Seris / noble-constitutional | `thread.seris_noble_constitutional` | House/nobility constitutional route milestone such as assembly/representation plus qualifying follow-up; Seris relationship alone is insufficient. |
| Ivo / guild-commercial | `thread.ivo_market` | Merchant/guild route milestone plus qualifying commercial/institutional decision; Ivo relationship alone is insufficient. |
| Mara / investigation-institutional | `thread.mara_institutional` | Independent audit/investigation route milestone; `mara_independence`, `mara_independent_mandate`, and late E226 stress are distinct facts. |
| Amara / civic-humanitarian | `thread.amara_civic` | Authored humanitarian/medical route milestone; Amara relationship alone is insufficient for institutional route gates. |
| Toma / information | `thread.toma_information` | Authored source/information-network milestone; Toma relationship alone is insufficient for information-route gates. |

## 3. Guild influence qualification

`pred.guild_influence_strong` is true only when at least **two distinct institutional domains** are established from the following canonical domains:

1. `history.guild_representation` or an equivalent permanent representation milestone;
2. `guild_binding_seat` or equivalent binding institutional seat;
3. `guild_tribunal_independent` / equivalent independent commercial adjudication;
4. documented market/credit leverage (`merchant_charter`, market oversight, credit/influence evidence);
5. `pred.guild_logistics_cooperation` after its own upstream qualification contract is satisfied.

`rel.ivo` by itself can never establish `pred.guild_influence_strong`.

## 4. Constitutional preparation

`pred.constitutional_prepared_strong` requires **three independent preparation domains** before E197:

- civic/commons legitimacy;
- audit/institutional legitimacy;
- factional/constitutional or military legitimacy.

Repeated flags from the same domain do not count as independent domains.

## 5. Coalition cooperation

`pred.coalition_cooperation` requires an authored cooperation package, not merely multiple active character routes. The package must identify participating factions and contain a positive cooperation/negotiation outcome. `four_way_bargain` is one valid authored package but must not be retroactively inferred from four relationship thresholds.

A failed, hidden, or explicitly exclusive coalition branch must not qualify cooperation.

## 6. Systemic explanation / evidence convergence

`pred.systemic_explanation_verified` requires independent evidence-source identities across:

- warehouse/financial evidence;
- document/language evidence;
- witness/organizational evidence;
- an explicit authored convergence decision.

Raw flag count is invalid when flags originate from the same evidence chain.

## 7. Final charter

`pred.final_charter_prerequisites` is a convergence predicate. It may consume already-established civic, institutional/audit, faction/house/guild, required military/security constitutional, information/evidence, coalition and crisis-resolution facts. It may not manufacture any missing prerequisite.

Mandatory unresolved crisis blockers invalidate the predicate until explicitly resolved.

## 8. Border crisis separation

The border lifecycle remains:

`E271-A` declaration → active crisis → `E272-A/B` resolution → resolved history retained + active predicate cleared.

E195/E253/E255 are consumers only. Security level, border tension, or a consumer event must never silently create `pred.border_crisis`.

## 9. Mara semantic separation

- `mara_independence` = earlier route fact (E95).
- `mara_independent_mandate` = institutional mandate outcome (E36/E226 contexts must remain distinct by source event).
- E226 = late accumulated institutional-stress consequence; it must not replay or overwrite the identity of E36/E95.

## 10. Ivo evidence separation

- E55 = earlier guild-books disclosure node.
- E269 = late commercial evidence handoff.

They are separate event identities and separate replay/history facts even if both expose financial evidence.

## 11. Gate

This document is a contract draft. It becomes engine input only after the full E01–E272 catalog is reconciled against it, all producers/consumers are rechecked, delayed/replay contracts are frozen, and the production schema is explicitly frozen.
