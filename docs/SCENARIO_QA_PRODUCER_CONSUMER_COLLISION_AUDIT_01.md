# Choice Kingdom — Scenario QA Producer/Consumer Collision Audit 01

Status: **SOURCE-LEVEL QA — COLLISION SCREEN**  
Scope: frozen production semantics E01–E272.  
Date: 2026-09-15.

## Purpose

Perform the next foundation pass after delayed source-token extraction: identify places where a consumer trigger could be incorrectly treated as a producer, where multiple source writers could be silently merged, and where a delayed consumer has an explicit source identity but unresolved lifecycle semantics.

This audit is intentionally conservative. A graph edge is contextual evidence, not proof of an executable producer relation.

## Collision screen

| Consumer | Canonical producer | Collision risk | Result |
|---|---|---|---|
| E181 | E45-B / `infrastructure_concession` | toll/concession wording could widen source identity | **NO MERGE** |
| E182 | E117-B / `veteran_patronage` | none identified in current producer inventory | **CLOSED IDENTITY** |
| E183 | E118-B / `estate_exception` | broader noble-exception wording is downstream | **NO MERGE** |
| E184 | none | invented secret-evidence producer | **BLOCKED / OPEN** |
| E185 | E17-A / `cheap_weapons` | later military crisis could be mistaken for source token | **SEPARATE LIFECYCLE** |
| E242 | E118-B candidate | `any prior noble exception` could incorrectly collapse multiple producers | **PARTIAL / NO ALIAS** |
| E243 | E18-B / `public_bridge` | generic infrastructure wording could widen token | **NO MERGE** |
| E244 | E09-B / `flexible_accounts` | none identified | **CLOSED IDENTITY** |
| E245 | E20-A / `soldier_compensation` | E125-A and E156-A are distinct compensation producers | **HARD NEGATIVE ENFORCED** |
| E246 | E160-A / `winter_rent_ceiling` | generic price-control wording could widen source | **NO MERGE** |

## Predicate collision rules

The following are not allowed to become implicit producers:

- `food_logistics_stabilized` → `pred.food_stable`;
- `four_way_bargain` → `pred.coalition_cooperation`;
- ordinary history → replay `meta.*`;
- `rel.ivo` → `pred.guild_influence_strong`;
- security → `pred.border_crisis`;
- E209 consumer wording → `pred.final_charter_prerequisites`;
- same-domain downstream evidence → a second independent predicate domain.

## Findings

1. **E245 is the strongest collision boundary.** E20-A is the canonical source; E125-A and E156-A remain separate facts.
2. **E242 is not safely reducible to one producer.** E118-B is a verified candidate, but the consumer wording is broader.
3. **E185 has two semantic layers:** `cheap_weapons` source identity and a later military-crisis lifecycle. They must not be collapsed.
4. **E184 remains unresolved.** No producer alias is safe from current source evidence.
5. No current source evidence authorizes a general semantic-synonym merge across delayed facts.

## Closure result

**Source-level collision screening: PASS with explicit OPEN boundaries.**

No producer was invented. No broad consumer phrase was promoted to a producer. No compensation producers were merged. No replay metadata was inferred.

## Still open

- executable delayed scheduler anchors;
- cancellation/supersession and exactly-once keys;
- E184 producer identity;
- E242 full producer set;
- E185 military-crisis resolution;
- ending prerequisite satisfiability;
- fresh-run and replay reachability;
- semantic equality between graph context and source contracts.

No Decision Engine promotion is authorized by this audit.
