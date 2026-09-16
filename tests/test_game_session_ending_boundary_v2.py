from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_ending_source_facts_do_not_infer_coalition_from_relationships() -> None:
    session = GameSession.new(ROOT, "ending-session-v2")
    session.state.flags.update({"people_charter_endorsed", "crown_audited", "army_constitution_oath"})
    session.state.history.add("history.house_assembly")
    assert "pred.constitutional_prepared_strong" in session.ending_source_facts().predicates
    session.state.relationships["seris"] = 3
    assert "pred.coalition_cooperation" not in session.ending_source_facts().predicates


def test_game_session_ending_resolution_sets_terminal_identity() -> None:
    session = GameSession.new(ROOT, "ending-resolution-v2")
    resolution = session.resolve_ending("END_STEWARD")
    assert session.state.terminal is True
    assert resolution.ending_id == "END_STEWARD"
    assert session.state.ending_identity == "END_STEWARD"
