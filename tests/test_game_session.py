from pathlib import Path

import pytest

from runtime.ending_contract import EndingQualification
from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_session_exposes_current_event_without_duplicating_rules():
    session = GameSession.new(ROOT, "session-1")
    view = session.view()
    assert view.event_id == "E01"
    assert len(view.choices) == 2
    assert session.available_choices() == ("E01-A", "E01-B")


def test_session_choose_delegates_to_engine_and_exposes_qualified_events():
    session = GameSession.new(ROOT, "session-2")
    result = session.choose("E01-A")
    assert result.event_id == "E01"
    assert session.state.turn == 2
    assert "E01" in session.state.history
    assert "E02" in session.available_events()
    session.select_event("E02")
    assert session.view().event_id == "E02"


def test_session_save_load_preserves_exact_runtime_state(tmp_path):
    session = GameSession.new(ROOT, "session-3")
    session.choose("E01-A")
    before = session.snapshot_digest()
    path = tmp_path / "save.json"
    session.save(path)
    restored = GameSession.load(ROOT, path)
    assert restored.state.snapshot() == session.state.snapshot()
    assert restored.snapshot_digest() == before


def test_session_load_recovery_uses_backup(tmp_path):
    session = GameSession.new(ROOT, "session-4")
    session.choose("E01-A")
    path = tmp_path / "save.json"
    session.save(path)
    session.select_event("E02")
    session.choose("E02-A")
    session.save(path)
    path.write_text("corrupt", encoding="utf-8")
    recovered = GameSession.load_with_recovery(ROOT, path)
    assert recovered.state.run_id == "session-4"
    assert recovered.state.turn == 2


def test_session_rejects_selecting_an_unqualified_event():
    session = GameSession.new(ROOT, "session-5")
    with pytest.raises(ValueError, match="not currently available"):
        session.select_event("E272")


def test_session_ending_boundary_is_atomic_on_invalid_qualification():
    session = GameSession.new(ROOT, "session-6")
    with pytest.raises(Exception):
        session.resolve_ending(EndingQualification.build())
    assert session.state.terminal is False


def test_ending_source_facts_are_derived_from_live_state():
    session = GameSession.new(ROOT, "ending-facts")
    session.state.flags.update({"crown_audited", "systemic_explanation_convergence", "military_red_line", "coalition_candidate_package"})
    session.state.history.update({"history.house_assembly", "history.cross_faction_package", "history.guild_representation"})
    session.state.threads.add("thread.military_constitutional")
    for family in ("warehouse_or_financial", "document_or_language", "witness_or_organizational"):
        session.state.record_ending_evidence(family)
    for participant in ("mara", "rowan", "seris"):
        session.state.record_coalition_participant(participant)

    facts = session.ending_source_facts()
    assert "pred.constitutional_prepared_strong" in facts.predicates
    assert "pred.systemic_explanation_verified" in facts.predicates
    assert "pred.coalition_cooperation" in facts.predicates
