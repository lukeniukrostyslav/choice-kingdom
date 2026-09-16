from __future__ import annotations

import json

import pytest

from runtime.state import GameState, PendingDelay, SaveStore


def test_fresh_run_isolated_from_prior_state(tmp_path):
    first = GameState.fresh("run-1")
    first.flags.add("open_petition_hall")
    first.history.add("history.open_petition_hall")
    first.schedule(
        PendingDelay(
            exactly_once_key="delay.E45B.E181.second_toll_increase",
            source_event_id="E45",
            source_choice_id="B",
            resolution_target="E181",
            scheduled_turn=8,
        )
    )
    first.terminal = True
    SaveStore.save(first, tmp_path / "run1.json")

    second = GameState.fresh("run-2")
    assert second.run_id == "run-2"
    assert second.flags == set()
    assert second.history == set()
    assert second.pending_delays == {}
    assert second.imported_meta_keys == set()
    assert second.terminal is False


def test_save_load_preserves_gameplay_state(tmp_path):
    state = GameState.fresh("run-save")
    state.turn = 7
    state.current_event_id = "E45"
    state.apply_delta("trust", -4)
    state.set_relationship_delta("ivo", 2)
    state.flags.add("infrastructure_concession")
    state.history.add("history.public_infrastructure_trust")
    state.threads.add("thread.ivo_market")
    state.schedule(
        PendingDelay(
            exactly_once_key="delay.E45B.E181.second_toll_increase",
            source_event_id="E45",
            source_choice_id="B",
            resolution_target="E181",
            scheduled_turn=12,
        )
    )

    path = tmp_path / "checkpoint.json"
    SaveStore.save(state, path)
    restored = SaveStore.load(path)

    assert restored.snapshot() == state.snapshot()


def test_delay_is_exactly_once():
    state = GameState.fresh("run-delay")
    delay = PendingDelay(
        exactly_once_key="delay.E20A.E245.soldiers_son_returns",
        source_event_id="E20",
        source_choice_id="A",
        resolution_target="E245",
        scheduled_turn=10,
    )
    state.schedule(delay)
    resolved = state.resolve_delay(delay.exactly_once_key)
    assert resolved.status == "resolved"
    with pytest.raises(ValueError, match="not pending"):
        state.resolve_delay(delay.exactly_once_key)


def test_condition_bound_delay_does_not_invent_turn():
    state = GameState.fresh("run-condition")
    delay = PendingDelay(
        exactly_once_key="delay.E17A.E185.cheap_steel_failure",
        source_event_id="E17",
        source_choice_id="A",
        resolution_target="E185",
        scheduled_turn=None,
        condition_bound=True,
    )
    state.schedule(delay)
    assert state.pending_delays[delay.exactly_once_key].scheduled_turn is None


def test_excluded_events_are_rejected():
    with pytest.raises(ValueError):
        PendingDelay(
            exactly_once_key="bad",
            source_event_id="E273",
            source_choice_id="A",
            resolution_target="E01",
            scheduled_turn=2,
        )

    payload = GameState.fresh("run-excluded").snapshot()
    payload["current_event_id"] = "E273"
    with pytest.raises(ValueError):
        GameState.from_snapshot(payload)


def test_coalition_participant_state_is_canonical_and_rejects_unknown_identities():
    state = GameState.fresh("run-coalition")
    for participant in ("mara", "rowan", "seris"):
        assert state.record_coalition_participant(participant) is True
    assert state.record_coalition_participant("mara") is False
    with pytest.raises(ValueError, match="non-canonical coalition participant"):
        state.record_coalition_participant("commons")


def test_save_load_rejects_non_canonical_coalition_participant():
    payload = GameState.fresh("run-bad-coalition").snapshot()
    payload["coalition_participants"] = ["mara", "commons", "guild"]
    with pytest.raises(ValueError, match="non-canonical coalition participant"):
        GameState.from_snapshot(payload)


def test_save_format_has_integrity_digest_and_is_deterministic(tmp_path):
    state = GameState.fresh("run-digest")
    state.flags.update({"z_flag", "a_flag"})
    state.history.update({"E02", "E01"})
    path = tmp_path / "save.json"
    SaveStore.save(state, path)
    first = path.read_text(encoding="utf-8")
    digest = SaveStore.snapshot_digest(state)
    payload = json.loads(first)
    assert payload["format_version"] == 2
    assert payload["snapshot_sha256"] == digest
    assert SaveStore.load(path).snapshot() == state.snapshot()

    SaveStore.save(state, path)
    assert path.read_text(encoding="utf-8") == first
    assert SaveStore.snapshot_digest(SaveStore.load(path)) == digest


def test_save_load_continuation_is_deterministic(tmp_path):
    from pathlib import Path
    from runtime.engine import DecisionEngine

    engine = DecisionEngine(Path(__file__).resolve().parents[1])
    uninterrupted = GameState.fresh("deterministic")
    checkpointed = GameState.fresh("deterministic")

    engine.execute(uninterrupted, "E01", "E01-A")
    engine.execute(checkpointed, "E01", "E01-A")

    checkpoint = tmp_path / "midrun.json"
    SaveStore.save(checkpointed, checkpoint)
    restored = SaveStore.load(checkpoint)

    engine.execute(uninterrupted, "E02", "E02-B")
    engine.execute(restored, "E02", "E02-B")
    assert uninterrupted.snapshot() == restored.snapshot()


def test_corrupt_primary_save_recovers_from_previous_atomic_backup(tmp_path):
    state = GameState.fresh("recovery")
    path = tmp_path / "save.json"
    SaveStore.save(state, path)

    state.turn = 4
    state.flags.add("recovery_marker")
    SaveStore.save(state, path)
    backup = path.with_name("save.json.bak")
    assert backup.exists()

    path.write_text("{not valid json", encoding="utf-8")
    restored = SaveStore.load_with_recovery(path)
    assert restored.turn == 1
    assert "recovery_marker" not in restored.flags


def test_corrupt_save_without_backup_is_rejected(tmp_path):
    path = tmp_path / "save.json"
    path.write_text(
        json.dumps({
            "format_version": 2,
            "snapshot": GameState.fresh("corrupt").snapshot(),
            "snapshot_sha256": "0" * 64,
        }),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="integrity check failed"):
        SaveStore.load_with_recovery(path)


def test_save_load_preserves_complete_runtime_lifecycle_state(tmp_path):
    state = GameState.fresh("complete-state")
    state.turn = 42
    state.current_event_id = "E272"
    state.resources.update({"gold": 12, "trust": 87, "security": 41, "power": 66, "reputation": 73})
    state.relationships.update({"mara": 2, "rowan": -1, "seris": 3, "ivo": 0, "amara": 1, "toma": -2})
    state.flags.update({"flag.alpha", "flag.beta"})
    state.history.update({"E01", "E148", "history.alpha"})
    state.threads.update({"thread.border", "thread.ivo_market"})
    state.schedule(PendingDelay(
        "delay.complete.pending", "E18", "E18-B", "E243", 45, priority=2
    ))
    state.pending_delays["delay.complete.resolved"] = PendingDelay(
        "delay.complete.resolved", "E20", "E20-A", "E245", 20, status="resolved"
    )
    state.activated_delayed_targets.add("E243")
    state.record_replay_meta("meta.replay.warehouse_investigation_unlock")
    state.record_ending_evidence("warehouse_or_financial")
    state.record_coalition_participant("mara")
    state.set_coalition_blocker("blocker.trade", True)
    state.set_mandatory_crisis_blocker("blocker.border", False)
    state.terminal = True
    state.set_ending_identity("END_STEWARD")

    path = tmp_path / "complete.json"
    SaveStore.save(state, path)
    restored = SaveStore.load(path)
    assert restored.snapshot() == state.snapshot()
    assert SaveStore.snapshot_digest(restored) == SaveStore.snapshot_digest(state)


def test_save_load_determinism_survives_delayed_target_execution(tmp_path):
    from pathlib import Path
    from runtime.engine import DecisionEngine

    engine = DecisionEngine(Path(__file__).resolve().parents[1])
    def prepared():
        state = GameState.fresh("delay-deterministic")
        state.resources.update({name: 100 for name in state.resources})
        state.relationships.update({name: 3 for name in state.relationships})
        state.flags.update({"merchant_charter", "competitive_market"})
        state.current_event_id = "E18"
        engine.execute(state, "E18", "E18-B")
        return state

    uninterrupted = prepared()
    checkpointed = prepared()
    path = tmp_path / "delayed.json"
    SaveStore.save(checkpointed, path)
    checkpointed = SaveStore.load(path)

    key = "delay.E18B.E243.old_bridge"
    for state in (uninterrupted, checkpointed):
        state.turn = state.pending_delays[key].scheduled_turn
        engine.execute_delayed_target(state, key, "E243-A")

    assert uninterrupted.snapshot() == checkpointed.snapshot()


def test_snapshot_validation_rejects_non_canonical_runtime_shapes():
    payload = GameState.fresh("shape").snapshot()
    payload["resources"]["unknown"] = 1
    with pytest.raises(ValueError, match="non-canonical resource set"):
        GameState.from_snapshot(payload)

    payload = GameState.fresh("shape").snapshot()
    payload["turn"] = 0
    with pytest.raises(ValueError, match="invalid turn"):
        GameState.from_snapshot(payload)

    payload = GameState.fresh("shape").snapshot()
    payload["current_event_id"] = "E999"
    with pytest.raises(ValueError, match="excluded or non-production event"):
        GameState.from_snapshot(payload)

    payload = GameState.fresh("shape").snapshot()
    payload["pending_delays"] = {
        "outer-key": {
            "exactly_once_key": "inner-key",
            "source_event_id": "E18",
            "source_choice_id": "E18-B",
            "resolution_target": "E243",
            "scheduled_turn": 4,
        }
    }
    with pytest.raises(ValueError, match="delay key mismatch"):
        GameState.from_snapshot(payload)
