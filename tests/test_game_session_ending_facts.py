from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_ending_facts_ignore_relationship_shortcuts() -> None:
    session = GameSession.new(ROOT, "ending-facts")
    session.state.flags.update({"people_charter_endorsed", "crown_audited", "army_constitution_oath"})
    session.state.history.add("history.house_assembly")
    assert "pred.constitutional_prepared_strong" in session.ending_source_facts().predicates
    session.state.relationships["seris"] = 3
    assert "pred.coalition_cooperation" not in session.ending_source_facts().predicates
