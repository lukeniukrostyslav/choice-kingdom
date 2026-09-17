from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHOICE_PREVIEW = ROOT / "web-preview" / "design-choice-experience-p6.html"


def test_p6_choice_preview_keeps_accessible_interaction_contract() -> None:
    html = CHOICE_PREVIEW.read_text(encoding="utf-8")

    # Both production-preview decision controls reference the live interaction
    # status and expose keyboard shortcuts without revealing hidden outcomes.
    assert html.count('aria-describedby="choice-state"') == 2
    assert 'aria-keyshortcuts="1 Enter"' in html
    assert 'aria-keyshortcuts="2 Enter"' in html
    assert 'role="status" aria-live="polite"' in html


def test_p6_choice_preview_keeps_large_interaction_targets_and_focus_proof() -> None:
    html = CHOICE_PREVIEW.read_text(encoding="utf-8")

    # The visual inspection controls are explicit interactive surfaces. The
    # choice controls themselves are larger than the project's 48px minimum.
    assert "min-height:76px" in html
    assert ".state-control{min-height:48px" in html
    assert ".tool{min-height:48px" in html
    assert ".choice:focus-visible" in html
    assert "b.focus();" in html


def test_p6_blocked_state_is_explicit_and_recoverable() -> None:
    html = CHOICE_PREVIEW.read_text(encoding="utf-8")

    assert "data-state=\"blocked\"" in html
    assert 'setAttribute(\'aria-disabled\',\'true\')' in html
    assert "clearChoices()" in html
    assert "applyState('idle')" in html
    assert "Escape" in html
