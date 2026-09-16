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
