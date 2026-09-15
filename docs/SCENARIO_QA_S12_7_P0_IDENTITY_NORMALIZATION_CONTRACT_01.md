# Choice Kingdom — S12.7 P0 Identity Normalization Contract 01

Date: 2026-09-15  
Status: **MACHINE CONTRACT QA — VERIFIED AGAINST CURRENT CANONICAL SOURCE/QA ARTIFACTS**  
Frozen production scope: **E01–E272**. E273–E277 excluded.

## 1. Purpose

Normalize the remaining P0 identity ambiguity before exhaustive producer/consumer graph construction. This document does not promote any unresolved predicate to CLOSED.

## 2. Canonical identity rules

### E144 guild representation

Authoritative authored branches E144-A and E144-B both establish the immutable marker `history.guild_representation`. The authored trigger `guild_political_representation` is treated as source-language legacy terminology, not as a second runtime producer.

Normalized graph:
- E144-A -> `history.guild_representation`
- E144-B -> `history.guild_representation`

### E148 cross-faction package

E148-A establishes `history.cross_faction_package` and `coalition_candidate_package`. The six authored participants are normalized to stable identities: `faction.mara`, `faction.rowan`, `faction.seris`, `faction.ivo`, `faction.amara`, `faction.toma`.

Participant presence is evidence attached to the package and is not equivalent to `pred.coalition_cooperation`. The machine contract requires explicit participant identity rather than inference from relationship scores or the generic phrase “six participants”.

### E136 guild logistics source

E136-B establishes `history.guild_logistics_cooperation`. This is an immutable historical source marker and is not identical to the qualified derived predicate consumed by E194.

### E194 qualified logistics

The qualified predicate remains derived from: (1) upstream `history.guild_logistics_cooperation`; (2) `guild_neutral_inspectors` from E194-A; and (3) absence of unresolved `guild_logistics_immunity_risk` from E194-B. E194 cannot satisfy its own prerequisite merely by firing.

### E192 food logistics

E192-A and E192-B are normalized as separate outcomes: `food_logistics_unstable` and `food_logistics_stabilized`. Neither token is renamed to `pred.food_stable`. `pred.food_stable` remains zero-verified-producer/open within E01–E272.

## 3. P0 identity separation matrix

| Authored term | Canonical identity | Producer | Status |
|---|---|---|---|
| guild political representation | `history.guild_representation` | E144-A/B | CLOSED source identity |
| six-person coalition package | `history.cross_faction_package` + participant identities | E148-A | CLOSED source identity / predicate OPEN |
| guild logistics cooperation history | `history.guild_logistics_cooperation` | E136-B | CLOSED source identity |
| qualified guild logistics cooperation | `pred.guild_logistics_cooperation` | derived | PARTIAL |
| food logistics stabilized | `food_logistics_stabilized` | E192-B | CLOSED source identity |
| food stable | `pred.food_stable` | none verified | OPEN/BLOCKED |

## 4. Rejected identity aliases

The following aliases are explicitly rejected unless a future authored contract proves equivalence:
- `food_logistics_stabilized` -> `pred.food_stable`
- `history.cross_faction_package` -> `pred.coalition_cooperation`
- `history.guild_logistics_cooperation` -> `pred.guild_logistics_cooperation`
- `rel.ivo` -> `pred.guild_influence_strong`
- border tension/security -> `pred.border_crisis`
- E197 -> `pred.constitutional_prepared_strong`
- E209 -> `pred.final_charter_prerequisites`
- E210 -> missing producer state

## 5. Machine acceptance criteria

A producer/consumer registry may accept a P0 edge only when:
- event ID is within E01–E272;
- choice identity is explicit where branch-specific;
- output token has exactly one canonical namespace/type;
- aliases resolve to an existing canonical token rather than creating a second token;
- derived predicates identify independent producer evidence;
- consumer events cannot become producers of their own prerequisite;
- historical markers are not silently treated as current-state predicates;
- replay metadata is isolated under `meta.*`;
- unresolved formulas remain OPEN instead of receiving guessed boolean semantics.

## 6. Verification

Verified against the current authoritative P0 reconciliation and machine-delta artifacts. No new producer was invented. No unresolved food-stability, coalition, guild-influence, constitutional-preparedness or final-charter formula was promoted.

## 7. Gate

**S12.7: PASS for P0 identity normalization; PARTIAL for full machine graph closure.**

Next work: exact E197/E200/E207/E209/E210 source extraction, then exhaustive E01–E272 producer/consumer inventory and ending/reachability reconciliation.
