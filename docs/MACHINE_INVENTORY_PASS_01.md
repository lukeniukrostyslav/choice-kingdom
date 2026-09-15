# Choice Kingdom — Machine Inventory Pass 01

Date: 2026-09-15  
Scope: E01–E272  
Status: **QA WORKING REGISTER — NOT RUNTIME**

## Purpose

This pass converts the existing canonical trigger vocabulary into a stricter machine-inventory gate. It records what is already source-closed, what is only a candidate, and which classes must remain blocked before production schema generation.

The repository currently has 272 authored nodes, while the engine and reachability runtime are intentionally not yet implemented. The public project README explicitly keeps canonicalization and QA ahead of engine/UI/APK work.

## Source-closed facts currently safe for the production-contract queue

- `public_bridge` — E18-B. E243 is now explicitly normalized to this exact vocabulary.
- `flexible_accounts` — E09-B.
- `veteran_patronage` — E117-B.
- `estate_exception` — E118-B.
- `border_compensation` — E125-A.
- `requisition_compensation` — E156-A.
- `winter_rent_ceiling` — E160-A.
- `history.guild_logistics_cooperation` — E136-B.
- `history.guild_representation` — E144-A/B.
- `history.cross_faction_package` — E148-A.
- `pred.market_pressure` — E19-B; clear path E19-A.
- `pred.winter_severe` — E29-A/B.
- `pred.transport_disruption` — E32; recovery/clear E136-A/B.
- `pred.border_crisis` — declaration E271-A; resolution E272-A/B.
- military constitutional evidence — E199-A.

These are source-level facts only. They are not yet runtime schemas.

## Delayed callback gate

| Consumer | Canonical producer status | Runtime admission |
|---|---|---|
| E181 | source-closed producer candidate; lifecycle still open | BLOCKED |
| E182 | E117-B | BLOCKED pending delay contract |
| E183 | E118-B | BLOCKED pending delay contract |
| E184 | no source-closed producer | BLOCKED |
| E185 | E17-A | BLOCKED pending crisis lifecycle |
| E242 | explicit E118-B, complete producer set open | BLOCKED |
| E243 | E18-B → `public_bridge` | CONTRACT-READY; runtime still blocked |
| E244 | E09-B | BLOCKED pending delay contract |
| E245 | ambiguous: E125-A vs E156-A and other compensation facts | BLOCKED |
| E246 | E160-A → `winter_rent_ceiling`; generic alias not yet frozen | BLOCKED |

## Hard-negative rules carried into the machine pass

The following must not become implicit producers during schema generation:

- `rel.ivo` alone must not produce `pred.guild_influence_strong`.
- A consumer must not manufacture its own prerequisite.
- `thread.border` must not alias `thread.border_crisis`.
- Security alone must not produce `pred.border_crisis`.
- E197 must not manufacture `pred.constitutional_prepared_strong`.
- E209 must not manufacture `pred.final_charter_prerequisites`.
- `four_way_bargain` must not automatically equal qualified `pred.coalition_cooperation`.
- Ordinary `flag.*` or `history.*` must not become `meta.*` merely because a replay event references them.
- A generic price-control fact must not equal `winter_rent_ceiling`.
- Generic compensation must not be silently unioned from distinct compensation contexts.

## Remaining machine-check gates

1. Exhaustive E01–E272 trigger token extraction.
2. Exhaustive output/producer extraction for `flag.*`, `history.*`, `thread.*`, resources and predicates.
3. Consumer-to-producer resolution for every executable trigger.
4. Duplicate semantic writer detection.
5. Contradictory writer detection.
6. Undefined producer and undefined consumer detection.
7. Predicate dependency cycle detection.
8. Delayed source/target/exactly-once/cancellation inventory.
9. Ending incoming-path coverage and deterministic precedence matrix.
10. Replay `meta.*` producer/key closure.
11. Fresh-run reachability simulation.

## Gate decision

**Production schema: BLOCKED.**

This pass deliberately does not invent missing producers, aliases, formulas or replay keys. The next safe implementation step is a static validator built only after the remaining canonical inventory is sufficiently closed.
