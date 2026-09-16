from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_source_closed_ending_facts_are_deterministic() -> None:
    session = GameSession.new(ROOT, "ending-facts-v2")
    session.state.flags.update({"people_charter_endorsed", "crown_audited", "army_constitution_oath"})
    session.state.history.add("history.house_assembly")
    first = session.ending_source_facts().predicates
    second = session.ending_source_facts().predicates
    assert first == second
