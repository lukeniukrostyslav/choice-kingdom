from runtime.premium_feedback import PlayerFeedbackState, premium_feedback


def test_every_player_state_composes_motion_and_feedback() -> None:
    for state in PlayerFeedbackState:
        result = premium_feedback(state)
        assert result.feedback.semantic
        assert result.motion.semantic


def test_reduced_motion_removes_decoration_but_keeps_feedback() -> None:
    result = premium_feedback(PlayerFeedbackState.REVEAL, reduced_motion=True)
    assert result.motion.enabled
    assert result.motion.duration_ms == 0
    assert not result.motion.decorative
    assert result.feedback.sound_id == "consequence_reveal"
    assert result.feedback.haptic_id == "reveal_medium"


def test_settings_can_disable_sound_and_haptics_independently() -> None:
    result = premium_feedback(
        PlayerFeedbackState.CONFIRM,
        sound_enabled=False,
        haptics_enabled=True,
    )
    assert result.feedback.sound_id is None
    assert result.feedback.haptic_id == "confirm_medium"
