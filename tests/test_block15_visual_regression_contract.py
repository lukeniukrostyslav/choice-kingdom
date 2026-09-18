from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "androidApp/app/src/main/java/com/choicekingdom/app/MainActivity.kt"
THEME = ROOT / "androidApp/app/src/main/java/com/choicekingdom/app/PremiumTheme.kt"
MANIFEST = ROOT / "tests/visual_regression_baseline.json"

def test_visual_regression_manifest_matches_runtime_surfaces():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    main = MAIN.read_text(encoding="utf-8")
    for surface in data["surfaces"]:
        assert f"private fun {surface}(" in main
    assert "WindowMode.COMPACT" in main
    assert "WindowMode.MEDIUM" in main
    assert "WindowMode.EXPANDED" in main

def test_visual_regression_manifest_matches_theme_contract():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    theme = THEME.read_text(encoding="utf-8")
    for token in data["requiredTheme"]:
        assert f"{token} =" in theme
    assert "darkColorScheme" in theme

def test_visual_regression_baseline_requires_approved_references():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert data["baselinePolicy"] == "approved-reference-required"
    assert data["physicalDeviceValidationBlock"] == 21


def test_visual_regression_ci_uses_available_gradle_distribution():
    workflow = (ROOT / ".github/workflows/block15-visual-regression-gate.yml").read_text(encoding="utf-8")
    assert 'gradle-version: "8.9"' in workflow
    assert "./gradlew" not in workflow
    assert "updateDebugScreenshotTest" in workflow
    assert "validateDebugScreenshotTest" in workflow


def test_visual_regression_host_rendering_heap_is_explicit():
    props = (ROOT / "androidApp/gradle.properties").read_text(encoding="utf-8")
    assert "android.compose.screenshot.maxHeapSize=4g" in props


def test_visual_regression_covers_core8_and_large_text():
    test = (ROOT / "androidApp/app/src/screenshotTest/kotlin/com/choicekingdom/app/VisualRegressionScreenshotTest.kt").read_text(encoding="utf-8")
    for locale in ["ru", "uk", "it", "de", "fr", "es", "pt"]:
        assert f'locale = "{locale}"' in test
    assert "fontScale = 1.3f" in test
    assert "Configuration.UI_MODE_NIGHT_YES" in test
    assert "LoadingCompactScreenshot" in test
