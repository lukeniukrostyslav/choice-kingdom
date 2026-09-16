from __future__ import annotations

from pathlib import Path

import pytest

from runtime.ending_contract import EndingQualification
from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_exposes_source_closed_ending_facts_without_inference() -> None:
    session = GameSession.new(ROOT, "ending-session")
    session.state.flags.update({
        "people_charter_endorsed",
        "crown_audited",
        "army_constitution_oath",
    })
    session.state.history.update({"history.house_assembly"})

    facts = session.ending_source_facts()
    assert "pred.constitutional_prepared_strong" in facts.predicates

    session.state.relationships["seris"] = 3
    assert "pred.coalition_cooperation" not in session.ending_source_facts().predicates


def test_game_session_ending_resolution_requires_a_terminal_boundary() -> None:
    session = GameSession.new(ROOT, "ending-resolution")
    qualification = EndingQualification("END_STEWARD", frozenset())

    resolution = session.resolve_ending(qualification)
    assert session.state.terminal is True
    assert resolution.ending_id == "END_STEWARD"
    assert session.state.ending_identity == "END_STEWARD"

    with pytest.raises(ValueError):
        session.resolve_ending(EndingQualification("END_IRON_CROWN", frozenset()))
