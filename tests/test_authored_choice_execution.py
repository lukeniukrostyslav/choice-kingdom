from pathlib import Path

import pytest

from runtime.catalog import AuthoredCatalog
from runtime.engine import DecisionEngine
from runtime.state import GameState

ROOT = Path(__file__).resolve().parents[1]


def test_frozen_catalog_loads_exactly_and_excludes_expansion_nodes():
    catalog = AuthoredCatalog.from_repository(ROOT)
    catalog.validate()
    assert len(catalog.events) == 272
    assert "E273" not in catalog.events
    assert "E277" not in catalog.events


def test_e01_a_executes_authored_immediate_state_transition():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("run-e01-a")
    result = engine.execute(state, "E01", "E01-A")

    assert state.resources["trust"] == 54
    assert state.resources["power"] == 49
    assert "open_petition_hall" in state.flags
    assert "E01" in state.history
    assert result.event_id == "E01"


def test_e51_c_executes_three_way_authored_choice_without_dropping_choice_c():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("run-e51-c")
    state.turn = 10
    state.history.add("E47")

    result = engine.execute(state, "E51", "E51-C")

    assert state.resources["trust"] == 55
    assert state.resources["power"] == 47
    assert "public_renewal_rule" in state.flags
    assert "E51" in state.history
    assert result.choice_id == "E51-C"


def test_e108_c_is_loaded_as_authored_even_where_source_uses_shorthand_effects():
    engine = DecisionEngine(ROOT)
    event = engine.event("E108")
    choice = next(choice for choice in event.choices if choice.choice_id == "E108-C")
    assert choice.text.startswith("distributed draft")
    assert "+trust -power" in choice.body

    state = GameState.fresh("run-e108-c")
    state.turn = 10
    engine.execute(state, "E108", "E108-C")
    # No numeric value is invented for the shorthand source expression; the authored
    # choice itself is still recorded as the executed history transition.
    assert "E108" in state.history


def test_excluded_event_cannot_execute():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("run-excluded")
    with pytest.raises(ValueError):
        engine.execute(state, "E273", "E273-A")
