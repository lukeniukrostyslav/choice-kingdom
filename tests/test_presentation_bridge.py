from __future__ import annotations

from pathlib import Path

from runtime.presentation import GameSessionPresentationBridge
from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_bridge_projects_real_game_session_view_without_mutation():
    session = GameSession.new(ROOT, "presentation-bridge")
    before = session.state.snapshot()
    view = session.view()

    projection = GameSessionPresentationBridge.snapshot(view)

    assert projection.schema_version == 1
    assert projection.run_id == "presentation-bridge"
    assert projection.event_id == view.event_id == session.state.current_event_id
    assert projection.turn == view.turn == session.state.turn
    assert projection.title == view.title
    assert projection.choices
    assert projection.terminal is False
    assert session.state.snapshot() == before


def test_bridge_tracks_real_runtime_after_choice():
    session = GameSession.new(ROOT, "presentation-bridge-choice")
    initial = session.view()
    choice_id = initial.choices[0][0]

    session.choose(choice_id)
    view = session.view()
    projection = GameSessionPresentationBridge.snapshot(view)

    assert projection.turn == view.turn == session.state.turn
    assert projection.event_id == view.event_id == session.state.current_event_id
    assert tuple(choice.id for choice in projection.choices) == tuple(
        choice_id for choice_id, _, _ in view.choices
    )


def test_bridge_json_is_deterministic_and_ui_safe():
    session = GameSession.new(ROOT, "presentation-bridge-json")
    view = session.view()
    projection = GameSessionPresentationBridge.snapshot(view)

    first = GameSessionPresentationBridge.snapshot_json(view)
    second = GameSessionPresentationBridge.snapshot_json(view)

    assert first == second
    assert '"schema_version":1' in first
    assert f'"event_id":"{projection.event_id}"' in first
    assert '"choices":[' in first
    assert "GameState" not in first
    assert "DecisionEngine" not in first
