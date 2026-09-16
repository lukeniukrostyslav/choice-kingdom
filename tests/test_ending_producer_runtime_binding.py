from pathlib import Path

from runtime.engine import AUTHORED_COALITION_PARTICIPANTS, DecisionEngine
from runtime.ending_sources import EndingSourceCompiler
from runtime.state import GameState


E148_SOURCE = Path("docs/EVENT_CATALOG_EXPANSION_111_150.md")


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


def test_e148_runtime_participants_feed_the_coalition_predicate_without_aliases() -> None:
    state = GameState.fresh("e148-predicate")
    state.history.add("history.cross_faction_package")
    state.flags.add("coalition_candidate_package")
    DecisionEngine._apply_authored_participant_effects(state, "E148-A")

    facts = EndingSourceCompiler.compile_state(state)
    assert "pred.coalition_cooperation" in facts.predicates

    state.history.add("four_way_bargain")
    state.coalition_participants.clear()
    state.coalition_participants.update({"commons", "guild", "houses"})
    facts = EndingSourceCompiler.compile_state(state)
    assert "pred.coalition_cooperation" not in facts.predicates


def test_non_producer_choices_cannot_create_coalition_participants() -> None:
    state = GameState.fresh("e148-negative")
    DecisionEngine._apply_authored_participant_effects(state, "E148-B")
    DecisionEngine._apply_authored_participant_effects(state, "E261-A")
    assert state.coalition_participants == set()


def test_e148_producer_mapping_matches_the_authored_source_names() -> None:
    text = E148_SOURCE.read_text(encoding="utf-8")
    marker = "records participation from Mara, Rowan, Seris, Ivo, Amara and Toma"
    assert marker in text
    assert AUTHORED_COALITION_PARTICIPANTS == {
        "E148-A": ("mara", "rowan", "seris", "ivo", "amara", "toma")
    }
