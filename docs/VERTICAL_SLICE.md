# Choice Kingdom — Vertical Slice Contract

The first playable slice is intentionally small but complete.

## Scenario
A ruler faces a merchant asking for an exclusive trade charter in exchange for gold.

## Required player-visible flow
1. New game creates a valid kingdom state.
2. Event appears with two meaningful choices.
3. Player can choose either option.
4. Choice is validated against current state.
5. Consequences are applied to resources and history.
6. A follow-up event can depend on the prior decision.
7. Save/load preserves the exact state.
8. At least one delayed consequence can trigger later.
9. A run can reach a real ending condition.
10. Player can start a replay without corrupting the previous run record.

## Minimum systemic proof
The slice must demonstrate that two players taking different choices can reach different future events and/or endings. This difference must come from engine state/history, not from a UI-only hard-coded branch.

## Acceptance criteria
- No fake buttons.
- No simulated save success.
- No placeholder consequence engine.
- No hidden global state required by the UI.
- Unit tests cover conditions and consequence application.
- Integration test covers event → choice → state mutation → next event.
- Save/load test covers the same sequence across serialization.
- Localization is exercised by the same vertical slice, not bolted on afterward.
