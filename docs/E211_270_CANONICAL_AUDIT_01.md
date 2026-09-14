# Choice Kingdom — E211–E270 Canonical Audit 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA / PRE-SCHEMA
Scope: E211–E270 producer/consumer semantics and canonicalization readiness.

## Purpose

Audit the E211–E270 authored expansion against the canonical state vocabulary and producer/consumer rules. This document does **not** claim runtime readiness, engine readiness, reachability, or production-schema closure.

## Findings

### 1. E211–E215 — institutional outputs

The events contain useful durable markers (`public_ledger_room`, `ledger_summary_access`, `clerk_protected`, `appointment_transparent`, `law_notices_public`), but their triggers include prose aliases such as `institutional reform`. These must be mapped to exact canonical flags/history/thread predicates before schema freeze.

### 2. E216–E220 — economic pressure

`low gold`, `high reform spending`, `food pressure`, and `strong market oversight` are contextual conditions rather than standalone numeric resources. The canonical model permits only gold, trust, security, power and reputation as numeric resources. These triggers therefore require explicit derived predicates or durable markers.

E218's `food pressure` must not silently introduce a sixth resource. E219's market oversight needs a canonical producer/threshold rule before it can be consumed by later content.

### 3. E221–E231 — social and character routes

Character relationships are used as triggers in several nodes (`Mara`, `Rowan`, `Seris`, `Ivo`, `Amara`, `Toma`). Relationship values may qualify character availability, but they must not be treated as substitutes for institutional route activation, constitutional preparation, guild influence, or information-route evidence. Durable outputs from these events need exact producer/consumer extraction.

### 4. E232–E236 — investigation chain

These nodes provide strong evidence ingredients:

- E232: `intermediary_chain_traced`
- E233: `seal_forensics`
- E234: `payment_pattern_public` / `payment_pattern_private`
- E235: family-archive investigation
- E236: witness-ledger decision

These ingredients do not individually prove `pred.systemic_explanation_verified`. The canonical rule remains: distinct warehouse/financial evidence + document/language evidence + witness/organizational evidence + an explicit convergence decision.

### 5. E237–E241 — faction credibility

These events create useful credibility consequences but do not automatically establish a constitutional or coalition route. Faction identity must remain explicit. Relationship increases (`+Ivo`, `+Seris`, etc.) are not sufficient to satisfy `pred.guild_influence_strong` or `pred.coalition_cooperation`.

### 6. E242–E250 — delayed and replay callbacks

The authored callbacks are valuable but require stable source/consequence identity, earliest/latest turn constraints, exactly-once semantics, and explicit replay metadata where the trigger depends on a previous run. `second-run information route` and `replay callback` must be represented through `meta.*` rather than an implicit runtime condition.

### 7. E251–E255 — crisis consumers

E253 consumes `pred.border_crisis` but does not produce it. E251 consumes winter + transport disruption, and E254/E255 consume food/civic crisis combinations. These are consumers of canonical crisis predicates and must not be promoted to producers merely because their prose describes a crisis.

**Border crisis producer status remains OPEN.** No existing E211–E270 node is accepted as a declaration producer without an explicit authored declaration semantics. E253 is explicitly a downstream consumer.

### 8. E256–E260 — constitutional stress tests

These events are downstream stress tests for succession, emergency powers, budget independence, military appeals and archive access. They must not be used to retroactively manufacture `pred.constitutional_prepared_strong` or `pred.final_charter_prerequisites`.

### 9. E261–E265 — coalition layer

E261's `four_way_bargain` is a useful endgame marker, but it must remain distinct from `pred.coalition_cooperation`. The canonical cooperation predicate requires the cross-faction package plus cooperation evidence from at least three distinct faction identities and no unresolved coalition-collapse marker.

E264/E265 provide useful collapse/hold outcomes and should become explicit inputs to the coalition durability rule rather than replacing the initial cooperation qualification.

### 10. E266–E270 — personal endgame pressure

The final character nodes are authored endgame consequences. They must not independently create missing constitutional prerequisites. E270's `dual_witness_account` is useful evidence but is not by itself the systemic-explanation convergence decision.

## Frozen canonical combination contracts

### `pred.guild_logistics_cooperation`

Minimum source qualification:
1. E194-A must have occurred and established `history.guild_logistics_cooperation`.
2. `guild_neutral_inspectors` must remain active as the inspection safeguard.
3. A later authored guild-logistics outcome must not contain `guild_logistics_immunity_risk` as an unresolved blocker.
4. The predicate is durable history/route state, not `rel.ivo`.

### `pred.guild_influence_strong`

Minimum qualification requires at least two distinct institutional guild outcomes from the following semantic domains:
- guild political representation (`history.guild_representation`);
- commercial institutional influence (`guild_binding_seat` or equivalent authored marker, if present);
- market/credit leverage;
- guild tribunal outcome;
- durable guild logistics cooperation.

`rel.ivo` alone can never qualify the predicate.

### `pred.systemic_explanation_verified`

Qualification requires all four components:
1. warehouse/financial evidence;
2. document/language evidence;
3. witness/organizational evidence;
4. explicit authored convergence decision.

A raw clue count is insufficient. E207 consumes this predicate and cannot manufacture it.

### `pred.coalition_cooperation`

Qualification requires:
1. `history.cross_faction_package` from E148-A;
2. cooperation evidence from at least three distinct faction identities;
3. no unresolved coalition-collapse marker.

A four-way route count is not equivalent to cooperation, and E261 does not retroactively create the predicate.

### `pred.constitutional_prepared_strong`

Qualification requires three independent institutional domains established upstream of E197–E210:
- civic/commons legitimacy;
- audit/institutional legitimacy;
- cross-faction or constitutional legitimacy.

Downstream succession/endgame outcomes cannot be used as prerequisites for their own trigger.

### `pred.final_charter_prerequisites`

The pre-E209 qualification set must establish, as applicable:
- civic/commons legitimacy;
- institutional/audit legitimacy;
- faction/house/guild representation;
- military/security constitutional route where required;
- information/evidence legitimacy;
- coalition cooperation;
- no unresolved mandatory crisis blocker.

E209 consumes this qualification; E210 only converges into the ending layer.

## P0 gaps confirmed after E211–E270 audit

1. No exact authored producer for `border_crisis_declared` / `border_crisis_resolved` is currently verified.
2. Guild logistics source marker exists, but its durable qualification rule needs a canonical implementation point.
3. Guild influence requires exact authored domain producers to be enumerated.
4. Systemic evidence needs an explicit convergence-decision producer.
5. Coalition cooperation needs three distinct faction cooperation evidence producers plus collapse invalidation.
6. Strong constitutional preparation needs exact upstream producers for its three domains.
7. Final charter prerequisites need deterministic upstream producer enumeration.
8. E211–E270 still contains prose triggers that must be normalized before production schema freeze.
9. E35–E40 legacy aliases and duplicate semantic pairs E73/E156 and E99/E173 remain separate audit work.

## Gate

**E211–E270 authored content: 100% authored, not 100% canonicalized.**

**Production schema: BLOCKED.**

**Runtime/reachability: NOT VERIFIED.**

Next pass: enumerate exact durable producers for every P0 predicate, then reconcile the complete E01–E270 graph against this contract before writing runtime data schemas.
