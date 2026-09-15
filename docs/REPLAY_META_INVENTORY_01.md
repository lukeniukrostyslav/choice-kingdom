# Choice Kingdom — Replay Meta-State Inventory 01

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — OPEN / PRE-RUNTIME**  
Scope: frozen E01–E272 replay boundary

## Purpose

The replay contract allows state to cross a completed-run boundary only through an explicitly authored `meta.*` transfer rule. This inventory checks whether the current authored catalog actually names those transfer values and their producers/consumers.

## Contract baseline

`docs/REPLAY_META_STATE_CONTRACT_01.md` closes the *isolation rule* but explicitly leaves the authored `meta.*` inventory OPEN. A new run must not inherit resources, relationships, active threads/predicates, unresolved crises, pending callbacks, callback markers, or temporary flags. Only an explicit `meta.*` transfer may seed replay variation.

## Source-level findings

### 1. No explicit `meta.*` producer was found in the current indexed repository search

GitHub code/file search was run for:

- `meta.`
- `meta_*`
- `meta replay`
- `meta transfer`
- `replay-exclusive`

No matching authored source result was returned.

This is **not treated as proof of absence**, because repository search coverage can be incomplete for narrative Markdown. It is therefore a verification lead, not a final negative claim.

### 2. Replay-dependent authored nodes exist without a closed transfer producer

The canonical E151–E210 and E211–E270 sources contain replay-oriented language/conditions, including:

- E186 — replay metadata may support a previous-run informational unlock;
- E247 — trigger is a second-run information route;
- E248 — trigger is a replay callback;
- E270 — ending qualification contract references replay-transfer metadata.

These references establish **consumer/trigger intent**, but they do not by themselves establish a canonical `meta.*` producer, transfer key, seed semantics, or current-run consumer contract.

### 3. Existing event flags are not automatically meta-state

Flags such as `warehouse_second_box`, `alternate_suspect_tested`, or `forgotten_favor_honored` are ordinary authored outcomes unless a separate replay contract explicitly promotes one of them into `meta.*`. They must not be silently copied between runs.

Likewise, `history.*` is not a substitute for `meta.*` at replay initialization.

## Required closure matrix

| Replay concept | Producer | Meta key | Consumer | Transfer timing | Status |
|---|---|---|---|---|---|
| replay-exclusive warehouse clue | **NOT IDENTIFIED** | **NOT IDENTIFIED** | E186 | new-run availability | OPEN |
| second-run alternative suspect | **NOT IDENTIFIED** | **NOT IDENTIFIED** | E247 | new-run availability | OPEN |
| replay callback / forgotten favor | **NOT IDENTIFIED** | **NOT IDENTIFIED** | E248 | new-run availability | OPEN |
| replay-exclusive evidence for ending | **NOT IDENTIFIED** | **NOT IDENTIFIED** | E270 / ending layer | ending qualification | OPEN |

## Hard rules for the future engine

1. Never infer `meta.*` from an ordinary flag/history marker.
2. Never transfer pending callbacks or active predicates across a replay boundary.
3. A replay consumer must declare the exact meta key it accepts.
4. A meta key must have an authored producer and explicit promotion rule.
5. A meta key may alter availability only through a declared consumer rule; it cannot directly satisfy an unrelated predicate.
6. Save/load within the same run must preserve meta seed data and active mutable state deterministically.

## Gate

**Replay isolation contract:** CLOSED at design level.  
**Exact `meta.*` producer/consumer inventory:** OPEN.  
**Current source evidence:** replay consumers/intents exist; explicit transfer producers are not yet source-closed.  
**Runtime implementation:** NOT STARTED.

This document deliberately does not invent missing meta keys or retroactively convert ordinary event flags into replay state.
