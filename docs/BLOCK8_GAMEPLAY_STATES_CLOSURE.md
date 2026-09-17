# Choice Kingdom — Block 8 Gameplay States Closure

Status: **CLOSED — 100%**

## Canonical lifecycle

Block 8 defines the gameplay lifecycle projection without duplicating gameplay rules:

1. `new_run` — a fresh run at E01 before the first decision.
2. `decision` — a non-terminal authored event exposes one or more choices.
3. `convergence` — a non-terminal authored event has no player choice; the state remains explicit instead of being confused with an empty/error screen.
4. `delay_due` — one or more persisted delayed consequences are pending and due at the current turn.
5. `delay_waiting` — a persisted condition-bound delayed consequence is pending but not yet eligible.
6. `ending` — the canonical session is terminal and may carry an immutable ending identity.

The projection is read-only. `GameSession` and `DecisionEngine` remain the only gameplay mutation authorities.

## Closure evidence

- Canonical implementation: `runtime/gameplay_state.py`
- Lifecycle regression suite: `tests/test_block8_gameplay_states.py`
- Regression coverage also includes session/view and full runtime-state persistence tests.
- GitHub Actions gate: `Choice Kingdom Block 8 Gameplay States Gate`
- Green run: **35280232253**
- All Block 8 lifecycle tests passed.

## Boundary

Block 8 does not claim physical Android/device QA, localization, accessibility certification, performance certification, release signing, or store readiness. Those are later blocks. The state lifecycle itself is now represented and regression-tested at the canonical runtime boundary.