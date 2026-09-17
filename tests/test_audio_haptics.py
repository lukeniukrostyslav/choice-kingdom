from runtime.audio_haptics import FeedbackSemantic, feedback_policy


def test_every_feedback_semantic_has_audio_and_haptic_tokens() -> None:
    for semantic in FeedbackSemantic:
        policy = feedback_policy(semantic)
        assert policy.sound_id
        assert policy.haptic_id
        assert 0.0 < policy.intensity <= 1.0


def test_player_can_disable_audio_or_haptics_without_changing_semantic() -> None:
    audio_off = feedback_policy(FeedbackSemantic.CHOICE_CONFIRM, sound_enabled=False)
    haptics_off = feedback_policy(FeedbackSemantic.CHOICE_CONFIRM, haptics_enabled=False)

    assert audio_off.semantic is FeedbackSemantic.CHOICE_CONFIRM
    assert audio_off.sound_id is None
    assert audio_off.haptic_id == "confirm_medium"
    assert haptics_off.sound_id == "choice_confirm"
    assert haptics_off.haptic_id is None


def test_ending_feedback_is_deliberately_stronger_than_navigation() -> None:
    ending = feedback_policy(FeedbackSemantic.ENDING_REVEAL)
    navigation = feedback_policy(FeedbackSemantic.NAVIGATE)
    assert ending.intensity > navigation.intensity
