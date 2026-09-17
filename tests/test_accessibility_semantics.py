from __future__ import annotations

import pytest

from runtime.accessibility_semantics import ActionState, choice_semantics


def test_choice_exposes_button_semantics_and_touch_target() -> None:
    semantics = choice_semantics("Open the gate", hint="Commits the decision")
    assert semantics.role == "button"
    assert semantics.label == "Open the gate"
    assert semantics.hint == "Commits the decision"
    assert semantics.enabled is True
    assert semantics.min_touch_target_dp == 48


def test_disabled_state_cannot_remain_enabled() -> None:
    semantics = choice_semantics("Open the gate", state=ActionState.DISABLED)
    assert semantics.enabled is False


def test_empty_accessible_label_rejected() -> None:
    with pytest.raises(ValueError):
        choice_semantics("   ")
