from pathlib import Path

from runtime.engine import AUTHORED_COALITION_PARTICIPANTS, DecisionEngine
from runtime.state import GameState


def test_e148_a_runtime_binding_records_only_canonical_authored_participants() -> None:
    state = GameState.fresh("e148-runtime")
    DecisionEngine._apply_authored_participant_effects(state, "E148-A")

    assert state.coalition_participants == {
        "mara",
        "rowan",
        "seris",
        "ivo",
        "amara",
        "toma",
    }


def test_non_producer_choices_cannot_create_coalition_participants() -> None:
    state = GameState.fresh("e148-negative")
    DecisionEngine._apply_authored_participant_effects(state, "E148-B")
    DecisionEngine._apply_authored_participant_effects(state, "E261-A")
    assert state.coalition_participants == set()


def test_e148_producer_mapping_is_exact_and_rooted_in_the_frozen_choice() -> None:
    assert AUTHORED_COALITION_PARTICIPANTS == {
        "E148-A": ("mara", "rowan", "seris", "ivo", "amara", "toma")
    }
    assert Path("docs/EVENT_CATALOG_EXPANSION_111_150.md").exists()
