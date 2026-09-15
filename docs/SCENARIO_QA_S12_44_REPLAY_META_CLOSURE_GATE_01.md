# Choice Kingdom — Scenario QA S12.44 — Replay Meta Closure Gate 01

Date: 2026-09-15  
Status: **OPEN — NO INVENTION GATE**  
Frozen production scope: **E01–E272**

## Purpose

Turn the replay-meta findings into a machine-facing closure gate while preserving the hard distinction between current-run history and cross-run metadata.

## Consumer matrix

| Consumer | Current authored meaning | Safe producer/key | Result |
|---|---|---|---|
| E186 | normal `warehouse_arson` route plus previous-run informational unlock | no explicit `meta.*` producer identified | OPEN |
| E247 | second-run information route | no explicit `meta.*` key identified | OPEN |
| E248 | replay callback | no explicit `meta.*` key identified | OPEN |
| E270 | ending qualification references replay transfer | E270 produces ordinary `dual_witness_account`, not replay meta | OPEN |

## Hard isolation rules

- Ordinary `history.*` is run-local unless an explicit promotion rule exists.
- Ordinary event flags are never promoted to `meta.*` by convention.
- A consumer with only generic replay wording is not runtime-ready.
- No synthetic names such as `meta.second_run` are admitted without authoritative source evidence.
- E273–E277 cannot provide replay producers for frozen production.

## Gate result

Replay isolation is **CLOSED at design level**. Exact producer/key inventory remains **OPEN**. This document is a closure gate, not a claim that replay implementation is ready.

No replay percentage increase is granted.
