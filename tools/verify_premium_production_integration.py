from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRESENTATION = ROOT / "runtime" / "presentation.py"
SESSION = ROOT / "runtime" / "session.py"
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
REQUIRED_PROJECTIONS = {
    "history",
    "threads",
    "pending_delays",
    "ending_evidence",
}


def main() -> None:
    presentation = PRESENTATION.read_text(encoding="utf-8")
    session = SESSION.read_text(encoding="utf-8")
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

    missing_projections = [name for name in REQUIRED_PROJECTIONS if name not in session or name not in presentation]
    assert not missing_projections, f"narrative presentation projections missing: {missing_projections}"

    assert "class SessionPresenter" in presentation
    assert "GameSession" in presentation
    assert "self.session.choose(choice_id)" in presentation
    assert "never" not in presentation.lower() or "gameplay" in presentation.lower()
    assert "tuple(DelayPresentation(*delay) for delay in view.pending_delays)" in presentation
    assert "history=tuple(sorted(self.state.history))" in session
    assert "threads=tuple(sorted(self.state.threads))" in session
    assert "ending_evidence=tuple(sorted(self.state.ending_evidence_families))" in session

    print("Premium production integration contract: PASS")
    print(f"Runtime states: {len(REQUIRED_STATES)}")
    print(f"Representative screens: {len(REQUIRED_SCREENS)}")
    print(f"Narrative projections: {len(REQUIRED_PROJECTIONS)}")
    print("Adaptive/accessibility token contract: PASS")
    print("GameSession mutation boundary: PASS")


if __name__ == "__main__":
    main()
