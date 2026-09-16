# Choice Kingdom — Runtime Scenario Verification Plan 01

## Purpose

This document defines the first runtime verification gate after the scenario-wide source/contract gate. It does **not** implement the Decision Engine and does not convert source/contract closure into runtime completion.

## Frozen production boundary

- Production events: **E01–E272**.
- E273–E277 remain excluded from runtime production semantics, producer/consumer edges and reachability.
- Runtime verification must consume the frozen authored contracts rather than inventing missing producers, predicates, timings or ending routes.

## Runtime gate matrix

| Gate | Required evidence | Pass condition |
|---|---|---|
| Fresh-run isolation | New run starts from canonical initial state | No state, pending consequence, replay import or terminal marker leaks from a prior run |
| Choice/state execution | Representative authored choice transitions | Selected authored choice produces exactly its declared state/effect delta and routes to the declared next event |
| Delayed consequences | E181–E185 and E242–E246 | Each callback is scheduled once, resolves only under its authored timing/condition, persists across save/load, and cannot resolve twice |
| Replay/meta transfer | E186/E247/E248 | Only the immediately completed prior run is eligible; import is exactly once; terminal state does not leak into the new run |
| Ending resolution | S11 ending identifiers/precedence | Runtime resolves only qualified endings and applies the authored precedence boundary; no forbidden aliases are accepted |
| Save/load equivalence | Checkpoint before and after reload | Continuing from a saved state yields the same observable state/eligible choices/pending lifecycle as uninterrupted execution |
| Determinism | Same initial state + same authored choices | Identical state/event/lifecycle/ending outcome across repeated executions |

## Required negative cases

1. A second replay import attempt must be rejected or be a no-op according to the final runtime contract.
2. A fresh run must not inherit pending delayed callbacks from a previous run.
3. A delayed callback must not fire merely because its consumer exists; its authored condition/timing must be satisfied.
4. Save/load must not duplicate pending callbacks or replay imports.
5. An unqualified ending must not resolve by alias, partial identifier or consumer-side prerequisite manufacture.
6. E273–E277 must never become reachable through the production runtime graph.

## Required implementation order

1. Identify the actual runtime/engine entry point and persistence boundary in the repository.
2. Define a minimal executable runtime harness around those existing boundaries; no mock gameplay path.
3. Add fresh-run isolation and save/load equivalence tests first.
4. Add delayed lifecycle execution tests for the ten frozen callbacks.
5. Add replay/meta transfer tests for E186/E247/E248.
6. Add ending resolution/precedence tests using the exact S11 identifiers.
7. Run the complete runtime scenario gate repeatedly and record evidence.
8. Only after all runtime gates are GREEN may Decision Engine promotion begin.

## Evidence policy

A source/contract validator passing is insufficient for a runtime GREEN. Runtime GREEN requires executable tests against the real runtime boundaries and repeatable evidence. Any missing runtime entry point, persistence implementation or authored executable producer is a blocker, not an assumption.
