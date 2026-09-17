from __future__ import annotations

from pathlib import Path

from runtime.presentation import GameSessionPresentationBridge
from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_bridge_projects_real_game_session_view_without_mutation():
    session = GameSession.new(ROOT, "presentation-bridge")
    before = session.state.snapshot()

    projection = GameSessionPresentationBridge.snapshot(session.view())

    assert projection.schema_version == 1
    assert projection.run_id == "presentation-bridge"
    assert projection.event_id == session.state.current_event_id
    assert projection.turn == session.state.turn
    assert projection.title
    assert projection.choices
    assert projection.terminal is False
    assert session.state.snapshot() == before


def test_bridge_tracks_real_runtime_after_choice():
    session = GameSession.new(ROOT, "presentation-bridge-choice")
    session.choose("E01-A")

    projection = GameSessionPresentationBridge.snapshot(session.view())

    assert projection.turn == session.state.turn
    assert projection.event_id == session.state.current_event_id
    assert projection.event_id == session.view().event_id
    assert tuple(choice.id for choice in projection.choices) == tuple(
        choice_id for choice_id, _, _ in session.view().choices
    )


def test_bridge_json_is_deterministic_and_ui_safe():
    session = GameSession.new(ROOT, "presentation-bridge-json")
    first = GameSessionPresentationBridge.snapshot_json(session.view())
    second = GameSessionPresentationBridge.snapshot_json(session.view())

    assert first == second
    assert '"schema_version":1' in first
    assert '"event_id":"E01"' in first
    assert '"choices":[{"id":"E01-A"' in first
    assert "GameState" not in first
    assert "DecisionEngine" not in first
