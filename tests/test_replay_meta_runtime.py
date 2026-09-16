from __future__ import annotations

import pytest

from runtime.catalog import AuthoredCatalog
from runtime.state import GameState, SaveStore, REPLAY_META_KEYS


META_BY_EVENT = {
    "E186": "meta.replay.warehouse_investigation_unlock",
    "E247": "meta.replay.second_run_information_route",
    "E248": "meta.replay.callback_forgotten_favor",
}


def test_completed_run_exports_only_canonical_replay_meta():
    state = GameState.fresh("run-1")
    state.flags.update({"ordinary_history_flag", "warehouse_arson"})
    state.history.add("E131")
    state.record_replay_meta(META_BY_EVENT["E186"])
    state.terminal = True

    export = state.export_completed_run_meta()

    assert export["completed"] is True
    assert export["run_id"] == "run-1"
    assert export["meta_keys"] == [META_BY_EVENT["E186"]]
    assert "ordinary_history_flag" not in export["meta_keys"]


def test_incomplete_run_cannot_export_replay_meta():
    state = GameState.fresh("run-open")
    state.record_replay_meta(META_BY_EVENT["E247"])
    with pytest.raises(ValueError, match="completed run"):
        state.export_completed_run_meta()


def test_new_run_resets_run_state_and_imports_only_prior_meta():
    prior = GameState.fresh("run-1")
    prior.flags.add("active_crisis")
    prior.history.add("E186")
    prior.record_replay_meta(META_BY_EVENT["E186"])
    prior.record_replay_meta(META_BY_EVENT["E247"])
    prior.terminal = True
    export = prior.export_completed_run_meta()

    second = GameState.new_run_from_completed_prior("run-2", export)

    assert second.run_id == "run-2"
    assert second.turn == 1
    assert second.current_event_id == "E01"
    assert second.flags == set()
    assert second.history == set()
    assert second.pending_delays == {}
    assert second.activated_delayed_targets == set()
    assert second.terminal is False
    assert second.imported_meta_keys == {
        META_BY_EVENT["E186"], META_BY_EVENT["E247"]
    }


def test_fresh_run_has_no_replay_meta():
    state = GameState.new_run_from_completed_prior("run-fresh")
    assert state.imported_meta_keys == set()


def test_replay_meta_import_is_exactly_once():
    state = GameState.fresh("run-2")
    key = META_BY_EVENT["E248"]
    assert state.record_replay_meta(key) is True
    assert state.record_replay_meta(key) is False
    assert state.imported_meta_keys == {key}


def test_noncanonical_replay_meta_is_rejected():
    state = GameState.fresh("run-2")
    with pytest.raises(ValueError, match="non-canonical replay meta key"):
        state.record_replay_meta("meta.replay.invented_route")


def test_replay_meta_survives_save_load(tmp_path):
    state = GameState.fresh("run-save")
    state.record_replay_meta(META_BY_EVENT["E247"])
    path = tmp_path / "replay.json"
    SaveStore.save(state, path)
    restored = SaveStore.load(path)
    assert restored.snapshot() == state.snapshot()


def test_catalog_exposes_exact_replay_meta_routes(tmp_path):
    # Root is only used for source loading; use the checked-out repository path
    # supplied by pytest's current working directory in CI.
    root = tmp_path
    # This test is intentionally structural and uses the frozen key set directly.
    assert set(META_BY_EVENT.values()) == set(REPLAY_META_KEYS)


def test_catalog_replay_routes_require_imported_meta_key():
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    catalog = AuthoredCatalog.from_repository(root)
    state = GameState.fresh("run-2")

    for event_id, key in META_BY_EVENT.items():
        assert catalog.trigger_satisfied(event_id, state) is False
        state.record_replay_meta(key)
        assert catalog.trigger_satisfied(event_id, state) is True
