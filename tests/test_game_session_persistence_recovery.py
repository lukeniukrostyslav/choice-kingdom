from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_load_with_recovery_preserves_snapshot(tmp_path: Path) -> None:
    session = GameSession.new(ROOT, "recovery-session")
    session.choose("E01-A")
    session.select_event("E02")
    session.choose("E02-B")
    path = tmp_path / "recovery.save"
    session.save(path)

    restored = GameSession.load_with_recovery(ROOT, path)
    assert restored.snapshot_digest() == session.snapshot_digest()
    assert restored.state.history == {"E01", "E02"}
    assert restored.state.current_event_id == "E02"
