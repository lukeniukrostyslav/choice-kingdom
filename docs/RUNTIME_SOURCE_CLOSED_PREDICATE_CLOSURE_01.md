# Runtime Source-Closed Predicate Closure 01

## Scope

This checkpoint records the next Block 7 runtime integration step for E01–E272.

## Implemented

- `pred.food_stable` is now compiled centrally from the authored E192-B producer marker `food_logistics_stabilized`, with the active-cycle invalidation marker `food_logistics_unstable` taking precedence.
- `runtime/catalog.py` continues to evaluate derived `pred.*` trigger atoms through the canonical `EndingSourceCompiler`; no narrative trigger text is promoted to truth.
- `runtime/engine.py` no longer maintains a separate food-stability predicate implementation. Typed authored effects remain in the engine, while derived predicate calculation is centralized.
- Added `tests/test_runtime_source_closed_predicates.py` covering positive source-closed predicate compilation, coalition hard-negative behavior, and food-stability producer/clear semantics.

## Source evidence

`docs/MACHINE_CANONICAL_GRAPH_01.json` identifies `pred.food_stable` as SOURCE-CLOSED, produced by E192-B and cleared by E192-A. The authored E192 block explicitly states that the predicate is a current-cycle state and that no numeric food resource is introduced.

## Verification status

GitHub Actions was triggered by the runtime changes. At checkpoint creation the relevant run was still queued/in progress, so this change is **IMPLEMENTED / VERIFICATION PENDING**, not runtime-verified closure.

No opaque prose trigger was promoted by this change. The remaining open trigger semantics are unchanged.
