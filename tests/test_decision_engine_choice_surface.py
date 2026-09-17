from __future__ import annotations

from pathlib import Path

from runtime.engine import DecisionEngine
from runtime.state import EXCLUDED_EVENTS, PRODUCTION_FIRST, PRODUCTION_LAST, GameState

ROOT = Path(__file__).resolve().parents[1]


def test_every_authored_choice_can_cross_the_engine_effect_boundary(monkeypatch) -> None:
    """Exercise every authored choice through the real mutation/scheduling seam.

    Trigger truth is deliberately bypassed here: reachability is a separate
    contract. Authored route prerequisites remain enforced, while every choice
    must cross the production engine without parser/effect/lifecycle errors.
    """
    engine = DecisionEngine(ROOT)
    production_ids = {
        f"E{i:02d}" for i in range(PRODUCTION_FIRST, PRODUCTION_LAST + 1)
    } - set(EXCLUDED_EVENTS)
    executed = 0

    monkeypatch.setattr(engine.catalog, "trigger_satisfied", lambda _event_id, _state: True)

    for event_id in production_ids:
        event = engine.event(event_id)
        prerequisites = engine.catalog.authored_prerequisites(event_id)
        for choice in event.choices:
            state = GameState.fresh(f"choice-surface-{choice.choice_id}")
            state.history.update(prerequisites)
            state.current_event_id = prerequisites[-1] if prerequisites else event_id
            result = engine.execute(state, event_id, choice.choice_id)
            assert result.event_id == event_id
            assert result.choice_id == choice.choice_id
            assert result.state_snapshot["history"]
            assert result.state_snapshot["current_event_id"] == event_id
            executed += 1

    assert executed == 520
