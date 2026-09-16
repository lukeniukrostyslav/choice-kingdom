from __future__ import annotations

from runtime.delays import (
    CANONICAL_DELAY_SPECS,
    due_delays,
    resolve_condition_bound_delay,
    resolve_due_delay,
    schedule_authored_delay,
)
from runtime.state import GameState, PendingDelay, SaveStore


def test_all_ten_frozen_delay_specs_have_canonical_identity():
    assert len(CANONICAL_DELAY_SPECS) == 10
    assert {spec.resolution_target for spec in CANONICAL_DELAY_SPECS} == {
        "E181", "E182", "E183", "E184", "E185", "E242", "E243", "E244", "E245", "E246"
    }
    assert len({spec.exactly_once_key for spec in CANONICAL_DELAY_SPECS}) == 10


def test_authored_choice_schedules_relative_delay_after_source_turn():
    state = GameState.fresh("delay-schedule")
    state.turn = 7
    delay = schedule_authored_delay(state, "E45", "E45-B")

    assert delay is not None
    assert delay.exactly_once_key == "delay.E45B.E181.second_toll_increase"
    assert delay.scheduled_turn == 12
    assert delay.status == "pending"


def test_due_delay_resolves_only_at_earliest_turn_and_only_once():
    state = GameState.fresh("delay-due")
    state.turn = 7
    delay = schedule_authored_delay(state, "E20", "E20-A")
    assert delay is not None
    assert due_delays(state) == ()

    state.turn = delay.scheduled_turn - 1
    assert due_delays(state) == ()
    state.turn = delay.scheduled_turn
    assert due_delays(state)[0].exactly_once_key == delay.exactly_once_key

    resolved = resolve_due_delay(state, delay.exactly_once_key)
    assert resolved.status == "resolved"
    assert due_delays(state) == ()


def test_condition_bound_delay_requires_explicit_resolution_condition():
    state = GameState.fresh("delay-condition")
    delay = schedule_authored_delay(state, "E17", "E17-B")
    assert delay is not None
    assert delay.condition_bound is True
    assert delay.scheduled_turn is None
    assert due_delays(state) == ()

    try:
        resolve_condition_bound_delay(state, delay.exactly_once_key, False)
    except ValueError as exc:
        assert "condition not satisfied" in str(exc)
    else:
        raise AssertionError("condition-bound delay resolved without its authored condition")

    resolved = resolve_condition_bound_delay(state, delay.exactly_once_key, True)
    assert resolved.status == "resolved"


def test_cancellation_is_observable_and_blocks_resolution():
    state = GameState.fresh("delay-cancel")
    delay = PendingDelay(
        exactly_once_key="delay.test.cancel",
        source_event_id="E45",
        source_choice_id="E45-B",
        resolution_target="E181",
        scheduled_turn=4,
    )
    state.schedule(delay)
    cancelled = state.cancel_delay(delay.exactly_once_key)
    assert cancelled.status == "cancelled"

    state.turn = 10
    assert due_delays(state) == ()
    try:
        state.resolve_delay(delay.exactly_once_key)
    except ValueError as exc:
        assert "not pending" in str(exc)
    else:
        raise AssertionError("cancelled delay resolved")


def test_supersession_marks_prior_delay_without_silent_deletion():
    state = GameState.fresh("delay-supersede")
    old = PendingDelay(
        exactly_once_key="delay.test.old",
        source_event_id="E45",
        source_choice_id="E45-B",
        resolution_target="E181",
        scheduled_turn=4,
    )
    new = PendingDelay(
        exactly_once_key="delay.test.new",
        source_event_id="E118",
        source_choice_id="E118-B",
        resolution_target="E242",
        scheduled_turn=5,
        supersedes=old.exactly_once_key,
    )
    state.schedule(old)
    state.schedule(new)
    assert state.pending_delays[old.exactly_once_key].status == "superseded"
    assert state.pending_delays[new.exactly_once_key].status == "pending"


def test_pending_delay_survives_save_load_and_replay_runs_are_isolated(tmp_path):
    first = GameState.fresh("delay-save-a")
    schedule_authored_delay(first, "E09", "E09-B")
    path = tmp_path / "delay.json"
    SaveStore.save(first, path)
    restored = SaveStore.load(path)
    assert restored.snapshot() == first.snapshot()

    second = GameState.fresh("delay-save-b")
    assert second.pending_delays == {}
    assert restored.run_id != second.run_id
