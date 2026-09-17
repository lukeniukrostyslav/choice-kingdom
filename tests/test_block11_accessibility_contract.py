from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "androidApp/app/src/main/AndroidManifest.xml"
MAIN = ROOT / "androidApp/app/src/main/java/com/choicekingdom/app/MainActivity.kt"

def test_rtl_is_enabled_at_application_boundary():
    text = MANIFEST.read_text(encoding="utf-8")
    assert 'android:supportsRtl="true"' in text

def test_screen_uses_safe_drawing_and_scalable_text():
    text = MAIN.read_text(encoding="utf-8")
    assert "WindowInsets.safeDrawing" in text
    assert ".sp" in text
    assert "fontSize =" in text
    assert "fontSize = 28.dp" not in text
    assert "fontSize = 30.dp" not in text
    assert "fontSize = 36.dp" not in text
    assert "fontSize = 42.dp" not in text
    assert "maxLines = 1" not in text

def test_accessibility_semantics_cover_navigation_and_dynamic_feedback():
    text = MAIN.read_text(encoding="utf-8")
    assert "role = Role.Button" in text
    assert "contentDescription" in text
    assert "stateDescription" in text
    assert "heading()" in text
    assert "liveRegion = LiveRegionMode.Polite" in text

def test_interactive_targets_have_large_text_safe_minimums():
    text = MAIN.read_text(encoding="utf-8")
    assert ".heightIn(min = 78.dp)" in text
    assert ".heightIn(min = 52.dp)" in text
    assert ".heightIn(min = 48.dp)" in text

def test_layout_is_direction_agnostic_at_source_level():
    text = MAIN.read_text(encoding="utf-8")
    forbidden = ("padding(left =", "padding(right =", "offset(x =", "layoutDirection = LayoutDirection.Ltr")
    assert not any(token in text for token in forbidden)
    assert "TextAlign.Start" in text

def test_release_ui_does_not_expose_non_core_locale_switches():
    text = MAIN.read_text(encoding="utf-8")
    for tag in ('"ar"', '"ja"', '"zh-CN"', '"zh-TW"'):
        assert tag not in text
