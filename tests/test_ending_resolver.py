import pytest

from runtime.endings import (
    END_BROKEN_DIADEM,
    END_GOLDEN_COMPACT,
    END_IRON_CROWN,
    END_PEOPLES_CHARTER,
    END_QUIET_THRONE,
    END_STEWARD,
    EndingResolutionError,
    EndingResolver,
)
from runtime.state import GameState, SaveStore


def terminal_state() -> GameState:
    state = GameState.fresh("ending-test")
    state.terminal = True
    return state


def test_single_authored_positive_ending_is_resolved_and_immutable():
    state = terminal_state()
    result = EndingResolver().resolve(state, qualified_endings=[END_STEWARD])
    assert result.ending_id == END_STEWARD
    assert state.ending_identity == END_STEWARD

    repeat = EndingResolver().resolve(state, qualified_endings=[END_STEWARD])
    assert repeat.ending_id == END_STEWARD

    with pytest.raises(EndingResolutionError, match="immutable"):
        EndingResolver().resolve(state, qualified_endings=[END_PEOPLES_CHARTER])


def test_collapse_failure_precedes_positive_ending():
    state = terminal_state()
    result = EndingResolver().resolve(
        state,
        qualified_endings=[END_STEWARD],
        collapse_failure=True,
    )
    assert result.ending_id == END_BROKEN_DIADEM


def test_multiple_positive_endings_require_authored_pairwise_priority():
    state = terminal_state()
    with pytest.raises(EndingResolutionError, match="missing authored priority"):
        EndingResolver().resolve(
            state,
            qualified_endings=[END_STEWARD, END_PEOPLES_CHARTER],
        )

    result = EndingResolver().resolve(
        state,
        qualified_endings=[END_STEWARD, END_PEOPLES_CHARTER],
        authored_priority={(END_STEWARD, END_PEOPLES_CHARTER): END_STEWARD},
    )
    assert result.ending_id == END_STEWARD


def test_quiet_throne_does_not_invent_precedence_over_positive_ending():
    state = terminal_state()
    with pytest.raises(EndingResolutionError, match="missing authored priority"):
        EndingResolver().resolve(
            state,
            qualified_endings=[END_GOLDEN_COMPACT],
            explicit_withdrawal=True,
        )

    result = EndingResolver().resolve(
        state,
        qualified_endings=[END_GOLDEN_COMPACT],
        explicit_withdrawal=True,
        authored_priority={(END_GOLDEN_COMPACT, END_QUIET_THRONE): END_GOLDEN_COMPACT},
    )
    assert result.ending_id == END_GOLDEN_COMPACT


def test_unknown_ending_id_cannot_enter_resolver():
    state = terminal_state()
    with pytest.raises(EndingResolutionError, match="non-canonical"):
        EndingResolver().resolve(state, qualified_endings=["END_STEWARD_FAKE"])


def test_ending_identity_survives_save_load():
    state = terminal_state()
    EndingResolver().resolve(state, qualified_endings=[END_IRON_CROWN])
    restored = GameState.from_snapshot(state.snapshot())
    assert restored.ending_identity == END_IRON_CROWN


def test_save_store_round_trip_preserves_ending_identity(tmp_path):
    state = terminal_state()
    EndingResolver().resolve(state, qualified_endings=[END_STEWARD])
    path = tmp_path / "ending.json"
    SaveStore.save(state, path)
    restored = SaveStore.load(path)
    assert restored.ending_identity == END_STEWARD


def test_non_terminal_state_cannot_resolve_or_carry_ending_identity():
    state = GameState.fresh("not-terminal")
    with pytest.raises(EndingResolutionError, match="terminal"):
        EndingResolver().resolve(state, qualified_endings=[END_STEWARD])

    payload = state.snapshot()
    payload["ending_identity"] = END_STEWARD
    with pytest.raises(ValueError, match="non-terminal"):
        GameState.from_snapshot(payload)
