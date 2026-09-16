from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_executes_authored_route_and_preserves_state(tmp_path: Path) -> None:
    session = GameSession.new(ROOT, "session-lifecycle")

    first = session.view()
    assert first.event_id == "E01"
    assert first.turn == 1
    assert {choice[0] for choice in first.choices} == {"E01-A", "E01-B"}

    result = session.choose("E01-A")
    assert result.event_id == "E01"
    assert session.state.history == {"E01"}
    assert session.state.flags == {"open_petition_hall"}
    assert session.state.resources["trust"] == 54
    assert session.state.resources["power"] == 49

    session.select_event("E02")
    second = session.view()
    assert second.event_id == "E02"
    assert second.turn == 2

    session.choose("E02-B")
    assert session.state.history == {"E01", "E02"}
    assert "decree_investigation" in session.state.flags

    save_path = tmp_path / "choice-kingdom.save"
    digest_before = session.snapshot_digest()
    session.save(save_path)
    restored = GameSession.load(ROOT, save_path)
    assert restored.snapshot_digest() == digest_before
    assert restored.view().event_id == "E02"
    assert restored.state.history == session.state.history
    assert restored.state.flags == session.state.flags
