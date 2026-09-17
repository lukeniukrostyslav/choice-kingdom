from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read_preview(name: str) -> str:
    return (ROOT / "design-preview" / name).read_text(encoding="utf-8")


def test_cross_screen_preview_declares_all_required_presentation_dimensions() -> None:
    html = _read_preview("premium-screen-state-matrix-v1.html")
    for marker in (
        "dir=\"rtl\"",
        "prefers-reduced-motion:reduce",
        "safe-area-inset-top",
        "safe-area-inset-bottom",
        "--scale",
        "Compact",
        "Medium",
        "Expanded",
        "data-reduced-motion",
    ):
        assert marker in html


def test_cross_screen_preview_keeps_shared_interaction_vocabulary() -> None:
    html = _read_preview("premium-screen-state-matrix-v1.html")
    for state in ("Default", "Focused", "Pressed", "Selected", "Disabled", "Pending", "Success", "Failure", "Error"):
        assert f"'{state}'" in html

    for screen in ("Event", "Realm", "History", "People", "Investigation", "Ending", "Settings"):
        assert f"{screen}:" in html


def test_consequence_preview_remains_explicitly_non_android_device_proof() -> None:
    html = _read_preview("premium-consequence-lab-v1.html")
    assert "not physical Android/device proof" in html
    assert "safe-area-inset-top" in html
    assert "prefers-reduced-motion:reduce" in html
