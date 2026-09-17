from runtime.motion import MotionSemantic, motion_policy


def test_motion_semantics_have_explicit_durations():
    for semantic in MotionSemantic:
        policy = motion_policy(semantic)
        assert policy.enabled is True
        assert policy.duration_ms >= 0
        assert policy.decorative is True


def test_reduced_motion_preserves_semantic_feedback_without_decoration():
    for semantic in MotionSemantic:
        policy = motion_policy(semantic, reduced_motion=True)
        assert policy.enabled is True
        assert policy.duration_ms == 0
        assert policy.decorative is False


def test_motion_policy_does_not_change_semantic_identity():
    policy = motion_policy(MotionSemantic.CONFIRM, reduced_motion=True)
    assert policy.semantic is MotionSemantic.CONFIRM
