from pathlib import Path

import pytest

from runtime.android_runtime import ANDROID_SAVE_FILENAME, AndroidRuntime


def test_android_runtime_persists_and_resumes_canonical_state(tmp_path: Path) -> None:
    first = AndroidRuntime(tmp_path, "android-test-run")
    assert first.session.view().event_id == "E01"
    first.choose("E01-A")

    save_path = tmp_path / ANDROID_SAVE_FILENAME
    assert save_path.exists()
    assert first.session.view().turn == 2

    resumed = AndroidRuntime(tmp_path, "android-test-run")
    assert resumed.run_id == "android-test-run"
    assert resumed.session.view().turn == 2
    assert resumed.session.view().history == first.session.view().history
    assert resumed.session.view().event_id == first.session.view().event_id


def test_android_runtime_rejects_a_different_run_id_for_existing_save(tmp_path: Path) -> None:
    first = AndroidRuntime(tmp_path, "android-test-run")
    first.choose("E01-A")

    with pytest.raises(ValueError, match="different run"):
        AndroidRuntime(tmp_path, "different-run")


def test_android_runtime_recovers_from_primary_save_using_backup(tmp_path: Path) -> None:
    first = AndroidRuntime(tmp_path, "android-test-run")
    first.choose("E01-A")

    save_path = tmp_path / ANDROID_SAVE_FILENAME
    backup = save_path.with_name(save_path.name + ".bak")
    assert backup.exists()

    save_path.write_text("{broken", encoding="utf-8")
    resumed = AndroidRuntime(tmp_path, "android-test-run")

    assert resumed.session.view().turn == 1
