# Choice Kingdom — Scenario QA Replay Semantic Classification 01

## Purpose

Separate genuinely replay-dependent authored semantics from ordinary in-run investigation/state routes. This prevents replay `meta.*` producer work from being incorrectly demanded for events that do not require prior-run state.

## Frozen production scope

E01–E272 only. E33/E34 remain quarantined. E273–E277 remain outside production semantics.

## Classification

| Node | Authored trigger | Replay dependency | Meta producer required | Classification |
|---|---|---|---|---|
| E186 | `warehouse_arson` OR equivalent previous-run informational unlock explicitly supported by replay metadata | **required for the previous-run branch** | YES | REPLAY_DEPENDENT |
| E247 | second-run information route | **required** | YES | REPLAY_DEPENDENT |
| E248 | replay callback | **required** | YES | REPLAY_DEPENDENT |
| E249 | archive route | no explicit previous-run requirement | NO | ORDINARY_STATE |
| E250 | three or more related clues | no explicit previous-run requirement | NO | ORDINARY_STATE |
| E270 | Amara and Toma both active | no explicit previous-run requirement | NO | ORDINARY_STATE |

## Consequences for replay QA

1. The persistent replay producer/key inventory is required only for E186, E247 and E248 from this six-node set.
2. E249/E250/E270 remain valid authored support/state nodes but must not be used as evidence that replay metadata exists.
3. E249/E250/E270 must not be blocked by the absence of a replay producer when evaluated on an ordinary fresh run.
4. E186 retains a split boundary: its ordinary `warehouse_arson` route is not itself proof of replay, while the explicitly previous-run informational branch requires replay metadata.
5. Replay metadata still cannot be invented from `history.*`, archive state, clue counts, character state, or graph proximity.

## Closure result

**Replay semantic classification: CLOSED for the six audited nodes.**

This is a source-level semantic classification only. It does not verify replay runtime, save/load persistence, cross-run isolation, or replay reachability.

## Remaining replay blockers

- exact producer/key tuple for E186 previous-run branch;
- exact producer/key tuple for E247;
- exact producer/key tuple for E248;
- promotion timing and persistence scope;
- fresh-run isolation;
- replay reachability;
- save/load isolation;
- ending qualification using genuine replay state.

No Decision Engine promotion is authorized by this document.
