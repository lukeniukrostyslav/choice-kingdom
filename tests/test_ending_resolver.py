import itertools
import json
from pathlib import Path

import pytest

from runtime.ending_precedence import AUTHORED_PRIORITY
from runtime.endings import (
    END_BROKEN_DIADEM,
    END_GOLDEN_COMPACT,
    END_IRON_CROWN,
    END_PEOPLES_CHARTER,
    END_QUIET_THRONE,
    END_SECOND_FOUNDER,
    END_STEWARD,
    EndingResolutionError,
    EndingResolver,
)
from runtime.state import GameState, SaveStore


POSITIVE = (
    END_SECOND_FOUNDER,
    END_PEOPLES_CHARTER,
    END_GOLDEN_COMPACT,
    END_STEWARD,
    END_IRON_CROWN,
)

DISPLAY_TO_ID = {
    "Second Founder": END_SECOND_FOUNDER,
    "People's Charter": END_PEOPLES_CHARTER,
    "Golden Compact": END_GOLDEN_COMPACT,
    "Steward": END_STEWARD,
    "Iron Crown": END_IRON_CROWN,
}


def terminal_state() -> GameState:
    state = GameState.fresh("ending-test")
    state.terminal = True
    return state


def load_precedence_source() -> dict:
    path = Path(__file__).resolve().parents[1] / "docs" / "MACHINE_ENDING_PRECEDENCE_TABLE_01.json"
    return json.loads(path.read_text(encoding="utf-8"))


def test_runtime_priority_is_exact_projection_of_authored_source_table():
    source = load_precedence_source()
    expected_order = tuple(DISPLAY_TO_ID[name] for name in source["positive_priority"])
    assert expected_order == POSITIVE

    expected_pairs = {
        (higher, lower): higher
        for index, higher in enumerate(expected_order)
        for lower in expected_order[index + 1 :]
    }
    assert AUTHORED_PRIORITY == expected_pairs


def test_source_pairwise_coverage_contains_every_positive_pair():
    source = load_precedence_source()
    expected_pairs = {
        frozenset((left, right))
        for left, right in itertools.combinations(POSITIVE, 2)
    }
    source_pairs = {
        frozenset((DISPLAY_TO_ID[left], DISPLAY_TO_ID[right]))
        for left, right in source["pairwise_coverage"]
        if left in DISPLAY_TO_ID and right in DISPLAY_TO_ID
    }
    assert expected_pairs <= source_pairs


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
        qualified_endings=[END_STEWARD, END_PEOPLES_CHARTER],
        collapse_failure=True,
    )
    assert result.ending_id == END_BROKEN_DIADEM


def test_machine_authored_priority_covers_every_positive_pair():
    assert len(AUTHORED_PRIORITY) == 10
    for left, right in itertools.combinations(POSITIVE, 2):
        winner = AUTHORED_PRIORITY.get((left, right), AUTHORED_PRIORITY.get((right, left)))
        assert winner in {left, right}


@pytest.mark.parametrize(
    "higher,lower",
    [
        (higher, lower)
        for index, higher in enumerate(POSITIVE)
        for lower in POSITIVE[index + 1 :]
    ],
)
def test_every_positive_pair_resolves_to_the_authored_higher_priority(higher, lower):
    state = terminal_state()
    result = EndingResolver().resolve(state, qualified_endings=[higher, lower])
    assert result.ending_id == higher


def test_machine_authored_priority_is_used_by_default():
    state = terminal_state()
    result = EndingResolver().resolve(
        state,
        qualified_endings=[END_SECOND_FOUNDER, END_IRON_CROWN],
    )
    assert result.ending_id == END_SECOND_FOUNDER


def test_explicit_priority_can_override_only_when_caller_supplies_authored_data():
    state = terminal_state()
    result = EndingResolver().resolve(
        state,
        qualified_endings=[END_STEWARD, END_PEOPLES_CHARTER],
        authored_priority={(END_STEWARD, END_PEOPLES_CHARTER): END_STEWARD},
    )
    assert result.ending_id == END_STEWARD


def test_quiet_throne_wins_only_when_no_positive_ending_qualifies():
    state = terminal_state()
    result = EndingResolver().resolve(state, explicit_withdrawal=True)
    assert result.ending_id == END_QUIET_THRONE

    positive_state = terminal_state()
    positive = EndingResolver().resolve(
        positive_state,
        qualified_endings=[END_GOLDEN_COMPACT],
        explicit_withdrawal=True,
    )
    assert positive.ending_id == END_GOLDEN_COMPACT


def test_quiet_throne_is_not_allowed_to_enter_positive_pairwise_priority():
    source = load_precedence_source()
    positive_pairs = {frozenset(pair) for pair in source["pairwise_coverage"]}
    for positive in POSITIVE:
        assert frozenset((END_QUIET_THRONE, positive)) in positive_pairs
    assert all(left != END_QUIET_THRONE and right != END_QUIET_THRONE for left, right in AUTHORED_PRIORITY)


def test_broken_diadem_is_a_failure_stage_not_a_positive_priority_entry():
    source = load_precedence_source()
    assert "Broken Diadem" not in source["positive_priority"]
    state = terminal_state()
    result = EndingResolver().resolve(
        state,
        qualified_endings=[END_SECOND_FOUNDER, END_PEOPLES_CHARTER],
        collapse_failure=True,
    )
    assert result.ending_id == END_BROKEN_DIADEM


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
