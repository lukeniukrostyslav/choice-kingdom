# Choice Kingdom — Scenario QA Replay Producer Provenance 01

## Purpose

Audit the authoritative authored sources for the persistent replay state required by E186, E247 and E248. This pass is intentionally narrower than replay semantic classification: it looks for an explicit producer, key and promotion boundary rather than inferring replay state from graph proximity or ordinary history.

## Frozen production scope

- Production events: E01–E272.
- E273–E277 are excluded.
- E33/E34 remain quarantined and cannot be used as replay evidence.

## Findings

| Consumer | Authoritative trigger | Explicit replay producer found | Key / marker | Status |
|---|---|---|---|---|
| E186 | `warehouse_arson` OR equivalent previous-run informational unlock supported by replay metadata | E131 is the only explicit previous-run informational producer found in the inspected authored catalogs | `all_voices_heard` is named by E131, but E186 does not explicitly bind to that key | PARTIAL_SOURCE_EVIDENCE |
| E247 | second-run information route | No explicit producer/key binding found in inspected authored sources | none | OPEN |
| E248 | replay callback | No explicit producer/key binding found in inspected authored sources | none | OPEN |

## Source-backed evidence

### E131 — The Same Letter Twice

E131 explicitly says its trigger is a replay with `all_voices_heard` from a previous run unavailable to the current save and calls itself an informational callback flag. This is authoritative evidence that the authored design contains a persistent previous-run concept and a named candidate marker.

### E186 — The Same Warehouse

E186 explicitly allows an equivalent previous-run informational unlock when supported by replay metadata, but it does not name `all_voices_heard` or any other exact persistent key. Therefore E131 cannot safely be promoted as E186's producer without an authored binding.

### E247 / E248

E247 names a second-run information route and E248 names a replay callback, but the inspected authored sources do not provide an exact persistent producer/key tuple for either consumer.

## Hard negatives

- `history.*` markers are not automatically replay metadata.
- Archive state, clue counts and ordinary character state are not proof of a previous completed run.
- E249/E250/E270 remain ordinary authored state and must not be promoted as replay producers.
- Graph edges into E186/E247/E248 do not create persistent cross-run state.
- E33/E34 cannot be used to manufacture missing replay semantics.

## Required closure tuple

A replay producer is considered source-closed only when the authored evidence binds:

`producerEventId + producerChoiceId + persistentMetaKey + promotionTiming + persistenceScope + consumerBinding`

Until then, the producer remains OPEN or PARTIAL and no Decision Engine replay implementation may be promoted as canonical.

## Closure result

**Source provenance audit: PARTIAL.**

This pass materially narrows the search: E131/`all_voices_heard` is the only explicit previous-run producer candidate found in the inspected authoritative catalogs, while E186 remains unbound to it and E247/E248 remain open. No replay semantics are invented.
