# Choice Kingdom — Scenario QA Replay Producer Provenance 01

## Purpose

Audit authoritative authored sources for persistent replay state required by E186, E247 and E248. This pass requires an explicit producer, key and promotion boundary; it never infers replay state from graph proximity or ordinary history.

## Frozen production scope

- Production events: E01–E272.
- E273–E277 are excluded.
- E33/E34 are unrelated to replay provenance and cannot manufacture replay evidence.

## Findings

| Consumer | Authoritative trigger | Explicit replay producer found | Key / marker | Status |
|---|---|---|---|---|
| E186 | `warehouse_arson` OR equivalent previous-run informational unlock supported by replay metadata | **None proven. E131 is a consumer, not a producer.** | E131 consumes candidate `all_voices_heard`; E186 does not bind to it | OPEN |
| E247 | second-run information route | No explicit producer/key binding found in inspected authored sources | none | OPEN |
| E248 | replay callback | No explicit producer/key binding found in inspected authored sources | none | OPEN |

## Source-backed evidence

### E131 — The Same Letter Twice

E131 explicitly consumes a previous-run condition containing `all_voices_heard`. The authored text therefore proves the existence of a named replay-condition concept, but E131 does **not** produce that meta-state. It is a replay consumer.

### E186 — The Same Warehouse

E186 allows an equivalent previous-run informational unlock when supported by replay metadata, but it does not name an exact persistent key. No in-scope producer is promoted on inference.

### E247 / E248

E247 names a second-run information route and E248 names a replay callback, but the inspected authored sources do not provide exact persistent producer/key tuples for either consumer.

## Hard negatives

- `history.*` markers are not automatically replay metadata.
- Archive state, clue counts and ordinary character state are not proof of a previous completed run.
- E131 cannot be classified as a replay producer merely because its trigger names `all_voices_heard`.
- E249/E250/E270 remain ordinary authored state and must not be promoted as replay producers.
- Graph edges into E186/E247/E248 do not create persistent cross-run state.

## Required closure tuple

A replay producer is source-closed only when authored evidence binds:

`producerEventId + producerChoiceId + persistentMetaKey + promotionTiming + persistenceScope + consumerBinding`

Until then, the producer remains OPEN/PARTIAL and no Decision Engine replay implementation may be promoted as canonical.

## Closure result

**Source provenance audit: OPEN.**

This correction removes the prior false-positive producer classification. The current source truth is that E131 is a replay consumer and no explicit E01–E272 replay producer/key tuple has been proven for E186/E247/E248. This is a quality improvement, not a percentage inflation.
