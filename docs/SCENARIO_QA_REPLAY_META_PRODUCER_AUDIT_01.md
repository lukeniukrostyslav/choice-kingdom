# Choice Kingdom — Scenario QA Replay Meta Producer Audit 01

Status: **SOURCE-LEVEL QA — REPLAY PRODUCER BOUNDARY**  
Scope: replay-sensitive E186, E247, E248, E249, E250, E270; frozen production E01–E272.  
Date: 2026-09-15.

## Purpose

Determine whether replay-sensitive nodes have an explicit authored producer for persistent `meta.*` state. Ordinary history and flags are deliberately excluded unless an authored promotion contract exists.

## Required producer tuple

A replay producer must explicitly identify:

`metaKey + sourceEvent/sourceChoice + promotionTiming + isolationRule + persistenceScope`

A consumer reference, narrative phrase, or ordinary history marker is not sufficient.

## Audit

| Node | Replay-sensitive behavior | Explicit meta producer/key | Status |
|---|---|---|---|
| E186 | previous-run informational unlock | not closed | OPEN |
| E247 | second-run information route | not closed | OPEN |
| E248 | replay callback | not closed | OPEN |
| E249 | replay-sensitive divergence support | not closed | OPEN |
| E250 | systemic-information/Second Founder support | not closed | OPEN |
| E270 | replay-transfer qualification reference | not closed | OPEN |

## Hard isolation rules

1. Ordinary `history.*` is not automatically persistent replay `meta.*`.
2. A completed run must not leak pending delayed callbacks into a fresh run unless explicitly authored.
3. Replay metadata must not satisfy a fresh-run prerequisite unless the ending contract explicitly allows it.
4. A replay consumer cannot manufacture the meta-state it consumes.
5. E33/E34 remain quarantined and cannot supply replay semantics.
6. E273–E277 remain outside production semantics.

## Findings

The current repository contains authored replay-sensitive narrative nodes and explicit design intent for replay separation, but no complete machine-closed producer/key inventory satisfying the required five-field tuple was identified in the current source-level contracts.

Therefore replay design is **not** promoted to executable meta-state semantics.

## Closure result

**Replay meta producer audit: conservative PASS with OPEN producer inventory.**

This closes a false-positive class: ordinary history, graph proximity and replay wording cannot silently become persistent meta-state.

## Remaining blockers

- exact meta keys;
- source event/choice for each promotion;
- promotion timing;
- persistence scope;
- fresh-run isolation test;
- replay reachability;
- ending qualification using replay state;
- runtime save/load semantics.

**No Decision Engine promotion is authorized.**
