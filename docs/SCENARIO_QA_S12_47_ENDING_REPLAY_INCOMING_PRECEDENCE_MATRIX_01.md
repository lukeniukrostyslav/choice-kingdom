# Scenario QA S12.47 — Ending / Replay Incoming-Path & Precedence Matrix 01

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — BOUNDED / OPEN**  
Scope: frozen E01–E272; endings E265–E270; replay candidates E247–E250 plus E186/E270 replay references.

## Purpose

Convert the existing ending-gap and replay-meta audits into one deterministic review boundary. This artifact does **not** invent missing producers, predicates, precedence, or replay keys. A row is only SOURCE-CLOSED when the authoritative authored source already identifies the producer and qualification semantics.

## Ending incoming-path matrix

| Ending | Required incoming qualification families | Current producer closure | Precedence status | Runtime gate |
|---|---|---|---|---|
| E265 Steward | institutional reform; emergency-power restraint/expiry; legitimacy; no collapse | PARTIAL | OPEN | BLOCKED |
| E266 Iron Crown | border/military route; concentrated authority; retained emergency authority / weak limits | PARTIAL | OPEN | BLOCKED |
| E267 Golden Compact | commercial thread; strong guild influence; economic stability | PARTIAL | OPEN | BLOCKED |
| E268 People's Charter | civic legitimacy/participation; institutional route; no authoritarian/collapse blocker | PARTIAL | OPEN | BLOCKED |
| E269 Broken Diadem | deterministic terminal failure predicate; at least two authored failure paths | OPEN | OPEN | BLOCKED |
| E270 Quiet Throne / ending-layer replay reference | explicit withdrawal/abdication/low-intervention history; replay reference remains distinct | OPEN | OPEN | BLOCKED |

## Second Founder / replay qualification boundary

The Second Founder ending remains outside a source-closed incoming-path contract because its prerequisite families are still only partially closed: systemic evidence convergence, coalition cooperation, constitutional preparation, constrained/expired emergency power, and replay-meta producer identity.

| Replay/late node | Required machine identity | Current evidence | Closure |
|---|---|---|---|
| E186 | explicit ordinary-run producer plus distinct previous-run promotion key | ordinary `warehouse_arson` is distinct from previous-run informational unlock | OPEN |
| E247 | explicit `meta.*` producer/key | no source-closed producer/key found | OPEN |
| E248 | explicit `meta.*` producer/key | no source-closed producer/key found | OPEN |
| E270 | ordinary ending-layer outcome must not become replay producer implicitly | produces ordinary `dual_witness_account`; replay reference is consumer/qualification context | OPEN |

## Deterministic precedence rules currently admissible

1. Positive ending precedence must be authored as data before runtime implementation.
2. Quiet Throne requires an explicit authored withdrawal/abdication/low-intervention producer; low scores or absence of positive flags cannot manufacture it.
3. Broken Diadem requires a real terminal-failure predicate; it cannot be a generic fallback for missing qualification.
4. A consumer cannot manufacture the prerequisite it consumes.
5. Ordinary history/flags cannot become `meta.*` across completed-run boundaries without an explicit promotion rule.
6. `four_way_bargain` cannot by itself satisfy `pred.coalition_cooperation`.
7. `rel.ivo` cannot by itself satisfy `pred.guild_influence_strong`.
8. E273–E277 remain excluded from all production ending/replay reachability.

## Gate interpretation

This pass closes the **review boundary**, not the runtime contract. It provides one authoritative QA matrix for incoming-path and precedence work while preserving all previously identified OPEN states.

### Still OPEN

- exact authored producers for Steward, Iron Crown, Golden Compact and People's Charter;
- Broken Diadem failure predicate and independent failure paths;
- Quiet Throne withdrawal producer and precedence against positive endings;
- exact `meta.*` producer/key inventory for E186/E247/E248/E270;
- systemic convergence producer/key;
- coalition cooperation executable ordering/invalidation;
- constitutional preparation executable ordering;
- fresh-run and replay reachability;
- catalog↔machine semantic equality.

## Verification basis

- `docs/ENDING_PRODUCER_GAP_REGISTER_01.md`
- `docs/REPLAY_META_SOURCE_CLOSURE_02.md`
- `docs/MACHINE_CANONICAL_GRAPH_01.json`
- `docs/SCENARIO_QA_S12_42_SCOPE_BOUNDARY_GATE_01.md`
- S12.46 CI hardening and canonical graph run #51 GREEN.

**Gate result: S12.47 = bounded incoming-path / precedence matrix GREEN; ending/replay runtime closure remains OPEN.**
