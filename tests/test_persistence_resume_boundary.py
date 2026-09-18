from __future__ import annotations

import json
from pathlib import Path

import pytest

from runtime.session import GameSession
from runtime.state import GameState, SaveStore


ROOT = Path(__file__).resolve().parents[1]


def _continue_from_e01(session: GameSession) -> None:
    assert "E02" in session.available_events()
    session.select_event("E02")
    session.choose("E02-B")


def test_game_session_save_load_resume_preserves_presentation_and_runtime(tmp_path):
    session = GameSession.new(ROOT, "resume-boundary")
    session.choose("E01-A")
    checkpoint = tmp_path / "resume.json"
    session.save(checkpoint)

    restored = GameSession.load(ROOT, checkpoint)
    assert restored.state.snapshot() == session.state.snapshot()
    assert restored.view() == session.view()
    assert restored.snapshot_digest() == session.snapshot_digest()

    _continue_from_e01(session)
    _continue_from_e01(restored)
    assert restored.state.snapshot() == session.state.snapshot()


def test_game_session_recovery_resumes_from_previous_atomic_checkpoint(tmp_path):
    session = GameSession.new(ROOT, "recovery-session")
    session.choose("E01-A")
    checkpoint = tmp_path / "resume.json"
    session.save(checkpoint)

    _continue_from_e01(session)
    session.save(checkpoint)
    checkpoint.write_text("{broken", encoding="utf-8")

    recovered = GameSession.load_with_recovery(ROOT, checkpoint)
    # The backup is the immediately previous atomic checkpoint, i.e. the
    # pre-second-save state. It must therefore resume at turn 2, not the
    # newer turn-3 state that was corrupted after the second save.
    assert recovered.state.turn == 2
    assert recovered.state.current_event_id == "E01"
    assert recovered.state.snapshot() != session.state.snapshot()


def test_legacy_raw_snapshot_remains_readable(tmp_path):
    state = GameState.fresh("legacy")
    path = tmp_path / "legacy.json"
    path.write_text(json.dumps(state.snapshot(), sort_keys=True), encoding="utf-8")

    restored = SaveStore.load(path)
    assert restored.snapshot() == state.snapshot()


def test_tampered_snapshot_digest_is_rejected(tmp_path):
    state = GameState.fresh("tamper")
    path = tmp_path / "tamper.json"
    SaveStore.save(state, path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["snapshot"]["turn"] = 99
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match="integrity check failed"):
        SaveStore.load(path)


def test_invalid_backup_does_not_mask_primary_corruption(tmp_path):
    state = GameState.fresh("bad-backup")
    path = tmp_path / "save.json"
    SaveStore.save(state, path)
    state.turn = 2
    SaveStore.save(state, path)
    path.write_text("{broken", encoding="utf-8")
    path.with_name("save.json.bak").write_text("{also broken", encoding="utf-8")

    with pytest.raises((ValueError, json.JSONDecodeError)):
        SaveStore.load_with_recovery(path)


def test_tampered_digest_format_is_rejected_before_snapshot_use(tmp_path):
    state = GameState.fresh("malformed-digest")
    path = tmp_path / "malformed.json"
    SaveStore.save(state, path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["snapshot_sha256"] = "not-a-sha256"
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match="integrity digest is malformed"):
        SaveStore.load(path)


def test_tampered_digest_with_wrong_hex_length_is_rejected(tmp_path):
    state = GameState.fresh("short-digest")
    path = tmp_path / "short.json"
    SaveStore.save(state, path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["snapshot_sha256"] = "0" * 63
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match="integrity digest is malformed"):
        SaveStore.load(path)


def test_tampered_digest_with_uppercase_hex_is_rejected_as_noncanonical(tmp_path):
    state = GameState.fresh("uppercase-digest")
    path = tmp_path / "uppercase.json"
    SaveStore.save(state, path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["snapshot_sha256"] = payload["snapshot_sha256"].upper()
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match="integrity digest is malformed"):
        SaveStore.load(path)
