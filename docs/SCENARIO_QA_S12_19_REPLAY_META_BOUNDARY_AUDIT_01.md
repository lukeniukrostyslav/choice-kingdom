# Choice Kingdom — S12.19 Replay / Meta Boundary Audit 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA — REPLAY ISOLATION AUDIT
Scope: frozen production E01–E272

## Purpose

Define the admissible boundary between ordinary run state and cross-run `meta.*` state for the replay-sensitive late events without inventing producers that are not explicitly authored.

## Replay-sensitive events

### E247 — Different Suspect

Authored trigger is explicitly a **second-run information route**. This is replay-sensitive by definition, but the catalog does not itself provide a canonical machine key for the prior-run unlock.

QA decision: E247 may consume only an explicitly persisted `meta.*` unlock once that key is authored/contracted. Ordinary first-run flags must not silently satisfy the second-run trigger.

### E248 — Forgotten Favor

Authored trigger is explicitly a **replay callback**. The callback may reference an early-run favor only through a declared cross-run identity. The ordinary run-state flag must not automatically persist into the next run.

QA decision: exact `meta.*` producer/key remains OPEN. No implicit persistence is admitted.

### E270 — Amara and Toma at Dawn

E270 is a late evidence event involving both active Amara and Toma routes. Its authored branch markers (`dual_witness_account` / `single_witness_account`) are ordinary run evidence unless the authored source explicitly promotes them to cross-run knowledge.

QA decision: E270 must not itself create replay `meta.*` state merely because it contains two witness identities. Dual-witness evidence also does not by itself satisfy `pred.systemic_explanation_verified`.

## Hard replay invariants

1. Ordinary `flag.*`, `history.*`, `thread.*` and resource state are run-local unless an explicit authored meta promotion exists.
2. `meta.*` must have a stable key and explicit producer.
3. A replay consumer cannot manufacture its own unlock.
4. A replay-only trigger cannot be satisfied by a first-run ordinary flag merely because the names are semantically similar.
5. Save/load must preserve current-run state but must not accidentally promote it to cross-run state.
6. A replay callback must remain isolated from unrelated historical evidence in the next run.
7. E273–E277 cannot create replay keys for production E01–E272.

## Current closure

- Replay isolation rule: **CLOSED at semantic level**.
- E247 exact `meta.*` key/producer: **OPEN**.
- E248 exact `meta.*` key/producer: **OPEN**.
- E270 replay promotion: **NOT ADMITTED** without authored source.
- Runtime persistence implementation: **BLOCKED** pending machine contract closure.

## Acceptance

This audit closes the negative boundary: ordinary run state cannot silently become replay state. It does not claim that the missing replay producers have been invented or implemented.

## Next gate

Recover or authoritatively identify exact replay meta keys/producers, then test fresh-run and second-run reachability separately. Only after that may replay edges enter the machine graph.
