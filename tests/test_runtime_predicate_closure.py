from pathlib import Path

from runtime.engine import DecisionEngine
from runtime.state import GameState

ROOT = Path(__file__).resolve().parents[1]


def test_constitutional_preparation_predicate_is_runtime_evaluable():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("predicate-constitutional")
    state.flags.update({"people_charter_endorsed", "crown_audited", "military_red_line"})
    state.history.add("history.house_assembly")
    assert engine.catalog.trigger_satisfied("E197", state) is True


def test_budget_reform_predicate_is_rejected_when_consumer_trigger_is_not_that_predicate():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("predicate-budget")
    state.flags.update({"auditor_independence", "crown_audited", "legislative_budget_lock"})
    # E198's authored trigger remains narrative "audit reform"; the runtime must
    # not silently alias that prose to pred.budget_reform.
    assert engine.catalog.trigger_satisfied("E198", state) is False


def test_coalition_predicate_requires_explicit_package_participants_and_no_blocker():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("predicate-coalition")
    state.flags.add("coalition_candidate_package")
    state.history.update({"history.cross_faction_package"})
    state.coalition_participants.update({"mara", "rowan", "seris"})
    assert engine.catalog.trigger_satisfied("E201", state) is True
    state.unresolved_coalition_blockers.add("open_dispute")
    assert engine.catalog.trigger_satisfied("E201", state) is False


def test_border_crisis_predicate_has_declared_resolved_lifecycle():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("predicate-border")
    state.flags.add("border_crisis_declared")
    assert engine.catalog.trigger_satisfied("E195", state) is True
    state.flags.add("border_crisis_resolved")
    assert engine.catalog.trigger_satisfied("E195", state) is False
