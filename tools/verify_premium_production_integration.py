from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRESENTATION = ROOT / "runtime" / "presentation.py"
TOKENS = ROOT / "docs" / "DESIGN_TOKENS_V2.json"
LAB = ROOT / "design-preview" / "premium-design-system-v2.html"

REQUIRED_STATES = {
    "IDLE",
    "FOCUSED",
    "SELECTED",
    "PRESSED",
    "RESOLVING",
    "RESOLVED",
    "DISABLED",
    "BLOCKED",
    "ERROR",
}
REQUIRED_SCREENS = {
    "event",
    "realm",
    "history",
    "people",
    "investigation",
    "ending",
    "settings",
}
REQUIRED_MODES = {
    "rtl",
    "large",
    "reduced",
}


def main() -> None:
    presentation = PRESENTATION.read_text(encoding="utf-8")
    tokens = TOKENS.read_text(encoding="utf-8")
    lab = LAB.read_text(encoding="utf-8")

    missing_states = [state for state in REQUIRED_STATES if state not in presentation]
    assert not missing_states, f"runtime presentation states missing: {missing_states}"

    for screen in REQUIRED_SCREENS:
        assert f'id="{screen}"' in lab, f"production design screen missing: {screen}"

    for mode in REQUIRED_MODES:
        assert mode in lab.lower(), f"design mode marker missing: {mode}"

    for token in ("touch", "safe", "compact", "medium", "expanded"):
        assert token in tokens.lower(), f"design token contract missing: {token}"

    assert "class SessionPresenter" in presentation
    assert "GameSession" in presentation
    assert "self.session.choose(choice_id)" in presentation
    assert "never" not in presentation.lower() or "gameplay" in presentation.lower()

    print("Premium production integration contract: PASS")
    print(f"Runtime states: {len(REQUIRED_STATES)}")
    print(f"Representative screens: {len(REQUIRED_SCREENS)}")
    print("Adaptive/accessibility token contract: PASS")
    print("GameSession mutation boundary: PASS")


if __name__ == "__main__":
    main()
