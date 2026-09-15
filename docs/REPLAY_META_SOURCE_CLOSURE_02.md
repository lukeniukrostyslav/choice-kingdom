# Choice Kingdom — Replay Meta Source Closure 02

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — OPEN / NARROWED**  
Scope: frozen E01–E272

## Purpose

Resolve replay-transfer producer candidates without inventing `meta.*` keys. Ordinary flags and `history.*` markers remain run-local unless an explicit authored promotion rule exists.

## Consumer inventory re-checked

| Consumer | Authored trigger / intent | Candidate source evidence | Current closure |
|---|---|---|---|
| E186 | `warehouse_arson` or equivalent previous-run informational unlock | current source names `warehouse_arson` as ordinary current-run route and separately references previous-run metadata | **OPEN** |
| E247 | `second-run information route` | no explicit `meta.*` key or producer found in indexed source | **OPEN** |
| E248 | `replay callback` | no explicit `meta.*` key or producer found in indexed source | **OPEN** |
| E270 | ending qualification references replay-transfer metadata | E270 itself produces `dual_witness_account`, not replay metadata | **OPEN** |

## Important source distinction

E186 contains two intentionally different concepts: a normal `warehouse_arson` route and an equivalent previous-run informational unlock when replay metadata supports it. The normal route must not be promoted automatically into replay state.

E247 and E248 are consumer-intent nodes. Their generic trigger wording does not identify a machine-safe transfer key. No authored source currently justifies inventing names such as `meta.second_run`, `meta.warehouse_clue`, or `meta.forgotten_favor`.

E270 is an ending-layer consumer/qualification reference. Its own choice outcome is ordinary current-run state and therefore cannot be treated as a replay producer.

## Producer search result

Repository search for replay/meta terms returned no explicit authored producer. Because narrative Markdown search coverage is not sufficient to prove absence, this is a narrowed verification result, not a global negative assertion.

## Closure rules

1. A replay meta key requires an explicit authored producer or a deliberate source edit adding one.
2. An ordinary event flag cannot become `meta.*` by convention.
3. A history marker cannot cross the completed-run boundary unless explicitly promoted.
4. A consumer cannot be considered runtime-ready while its exact meta key and producer are unknown.
5. No replay percentage increase is granted merely for documenting an unresolved candidate.

## Gate result

**Replay isolation:** CLOSED at design level.  
**Exact producer/key inventory:** OPEN.  
**E186:** narrowed; ordinary `warehouse_arson` and replay unlock remain distinct.  
**E247/E248:** no source-closed producer/key.  
**E270:** no source-closed replay producer.  
**Runtime implementation:** NOT STARTED.
