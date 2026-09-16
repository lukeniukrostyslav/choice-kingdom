import pytest

from runtime.ending_contract import EndingContractError, EndingQualification
from runtime.endings import END_SECOND_FOUNDER, END_STEWARD, EndingResolver
from runtime.state import GameState


def terminal_state() -> GameState:
    state = GameState.fresh("ending-contract-test")
    state.terminal = True
    return state


def test_canonical_second_founder_predicates_are_namespace_exact():
    qualification = EndingQualification.build(
        positive_endings={END_SECOND_FOUNDER},
        predicates={
            "pred.systemic_explanation_verified",
            "pred.coalition_cooperation",
            "pred.constitutional_prepared_strong",
        },
    )
    assert "pred.systemic_explanation_verified" in qualification.predicates
    assert "pred.coalition_cooperation" in qualification.predicates


def test_validated_qualification_reaches_resolver_without_reinterpreting_tokens():
    qualification = EndingQualification.build(
        positive_endings={END_STEWARD},
        flags={"constitution_first", "constitutional_limit"},
    )
    result = EndingResolver().resolve_qualification(terminal_state(), qualification)
    assert result.ending_id == END_STEWARD


def test_history_cross_faction_package_does_not_alias_to_cooperation():
    qualification = EndingQualification.build(history={"history.cross_faction_package"})
    assert "pred.coalition_cooperation" not in qualification.predicates


def test_four_way_bargain_does_not_alias_to_cooperation():
    qualification = EndingQualification.build(flags={"four_way_bargain"})
    assert "pred.coalition_cooperation" not in qualification.predicates


def test_unscoped_systemic_explanation_cannot_satisfy_predicate():
    with pytest.raises(EndingContractError, match="systemic_explanation_verified"):
        EndingQualification.build(flags={"systemic_explanation_verified"})


def test_unscoped_coalition_cooperation_cannot_satisfy_predicate():
    with pytest.raises(EndingContractError, match="coalition_cooperation"):
        EndingQualification.build(flags={"coalition_cooperation"})


def test_stale_thread_alias_is_rejected():
    with pytest.raises(EndingContractError, match="non-canonical ending thread"):
        EndingQualification.build(threads={"thread.border"})


def test_stale_commercial_thread_alias_is_rejected():
    with pytest.raises(EndingContractError, match="non-canonical ending thread"):
        EndingQualification.build(threads={"thread.guild"})


def test_unknown_predicate_is_rejected_instead_of_inferred():
    with pytest.raises(EndingContractError, match="non-canonical ending predicate"):
        EndingQualification.build(predicates={"systemic_explanation_verified"})
