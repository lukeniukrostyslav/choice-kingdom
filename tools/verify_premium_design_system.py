"""Static contract checks for the Premium Design System v2 preview."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "design-preview" / "premium-design-system-v2.html"
TOKENS = ROOT / "docs" / "DESIGN_TOKENS_V2.json"

REQUIRED_VIEWS = {"event", "realm", "history", "people", "investigation", "ending", "settings", "states"}
REQUIRED_STATES = {"selected", "pending", "resolved", "blocked", "risk", "error"}


def main() -> None:
    html = HTML.read_text(encoding="utf-8")
    tokens = json.loads(TOKENS.read_text(encoding="utf-8"))

    assert "<title>Choice Kingdom — Premium Design System v2</title>" in html
    assert "viewport-fit=cover" in html
    assert "min-height:48px" in html and "min-height:56px" in html
    assert "@media(min-width:600px)" in html and "@media(min-width:840px)" in html
    assert "prefers-reduced-motion" in html
    assert "[dir=rtl]" in html
    assert "classList.toggle('large'" in html
    assert all(f'id="{view}"' in html for view in REQUIRED_VIEWS)
    assert all(state in html for state in REQUIRED_STATES)

    assert tokens["touch_target_dp"]["minimum"] >= 48
    assert tokens["touch_target_dp"]["preferred_choice"] >= 56
    assert tokens["window_adaptation"]["compact_dp"] == "<600"
    assert tokens["window_adaptation"]["medium_dp"] == "600-839"
    assert tokens["window_adaptation"]["expanded_dp"] == ">=840"
    assert tokens["accessibility"]["state_not_color_only"] is True
    assert tokens["accessibility"]["rtl"] is True
    assert tokens["accessibility"]["large_text_reflow"] is True
    print("Premium Design System v2 static contract: PASS")


if __name__ == "__main__":
    main()
