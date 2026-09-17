from runtime.premium_screen_states import (
    PremiumScreen,
    ScreenState,
    required_states,
    screen_state_contract,
)


def test_every_screen_has_shared_interaction_states() -> None:
    for screen in PremiumScreen:
        states = required_states(screen)
        assert ScreenState.DEFAULT in states
        assert ScreenState.FOCUSED in states
        assert ScreenState.PRESSED in states
        assert ScreenState.DISABLED in states


def test_event_and_ending_keep_semantic_outcomes_explicit() -> None:
    event_states = required_states(PremiumScreen.EVENT)
    ending_states = required_states(PremiumScreen.ENDING)
    assert ScreenState.PENDING in event_states
    assert ScreenState.ERROR in event_states
    assert ScreenState.SUCCESS in ending_states
    assert ScreenState.FAILURE in ending_states


def test_state_contract_is_presentation_only_and_never_color_only() -> None:
    contract = screen_state_contract(PremiumScreen.HISTORY, ScreenState.SELECTED)
    assert contract.semantic_label_required is True
    assert contract.visual_indicator_required is True
    assert contract.color_only_forbidden is True
