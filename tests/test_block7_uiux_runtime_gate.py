from __future__ import annotations

from pathlib import Path

from runtime.android_adaptive_contract import android_adaptive_contract
from runtime.presentation import (
    GameSessionPresentationBridge,
    InteractionState,
    SessionPresenter,
    SessionView,
)
from runtime.session import GameSession


ROOT = Path(__file__).resolve().parents[1]


def test_block7_session_to_presentation_round_trip() -> None:
    session = GameSession.new(ROOT, "block7-gate")
    presenter = SessionPresenter(session)

    initial = presenter.snapshot()
    assert initial.run_id == "block7-gate"
    assert initial.turn == 1
    assert initial.event_id == "E01"
    assert initial.choices

    choice_id = initial.choices[0].choice_id
    presenter.focus_choice(choice_id)
    assert presenter.snapshot().choices[0].state is InteractionState.FOCUSED

    presenter.press_choice(choice_id)
    assert presenter.snapshot().choices[0].state is InteractionState.PRESSED

    presenter.begin_choice(choice_id)
    assert presenter.snapshot().choices[0].state is InteractionState.RESOLVING

    presenter.choose(choice_id)
    resolved = presenter.snapshot()
    assert resolved.turn == 2
    assert resolved.event_id == "E01"
    assert resolved.history[-1] == "E01"
    assert resolved.choices[0].state is InteractionState.RESOLVED

    bridge = GameSessionPresentationBridge.snapshot(session.view())
    assert bridge.schema_version == 1
    assert bridge.run_id == "block7-gate"
    assert bridge.turn == 2
    assert bridge.event_id == "E01"
    assert bridge.terminal is False


def test_block7_adaptive_layout_contract() -> None:
    for width, height, expected in (
        (360, 640, "COMPACT"),
        (600, 900, "MEDIUM"),
        (840, 1100, "EXPANDED"),
    ):
        projection = android_adaptive_contract(width, height)
        assert projection.width_class.value == expected
        assert projection.safe_content_width_dp > 0
        assert projection.safe_content_height_dp > 0
        assert projection.content_panes >= 1


def test_block7_terminal_projection_disables_choices() -> None:
    view = SessionView(
        run_id="block7-terminal",
        turn=9,
        event_id="E01",
        title="Terminal gate",
        trigger="gate",
        choices=(("E01-A", "A", "Choice A"), ("E01-B", "B", "Choice B")),
        resources=(),
        relationships=(),
        history=(),
        threads=(),
        pending_delays=(),
        ending_evidence=(),
        terminal=True,
        ending_identity="gate-test",
    )
    projection = GameSessionPresentationBridge.snapshot(view)
    assert projection.terminal is True
    assert all(choice.state == InteractionState.DISABLED.value for choice in projection.choices)
