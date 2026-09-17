from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "androidApp/app/src/main/java/com/choicekingdom/app/MainActivity.kt"
MANIFEST = ROOT / "androidApp/src/main/AndroidManifest.xml"

def test_block12_responsive_contract():
    main = MAIN.read_text(encoding="utf-8")
    manifest = (ROOT / "androidApp/app/src/main/AndroidManifest.xml").read_text(encoding="utf-8")
    assert "BoxWithConstraints(" in main
    assert "maxWidth < 600.dp" in main
    assert "maxWidth < 840.dp" in main
    assert "WindowMode.EXPANDED" in main
    assert "Modifier.fillMaxWidth().widthIn(max = 720.dp)" in main
    assert "WindowInsets.safeDrawing" in main
    assert ".windowInsetsPadding(WindowInsets.safeDrawing)" in main
    assert "onClick = { onSelect(screen.key) }" in main
    assert 'android:supportsRtl="true"' in manifest
    assert "Modifier.width(720.dp)" not in main
