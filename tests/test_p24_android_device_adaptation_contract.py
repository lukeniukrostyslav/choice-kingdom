from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / 'androidApp/app/src/main/java/com/choicekingdom/app/MainActivity.kt'
MANIFEST = ROOT / 'androidApp/app/src/main/AndroidManifest.xml'
GRADLE = ROOT / 'androidApp/app/build.gradle.kts'

def test_p24_manifest_declares_rtl_and_launcher():
    text = MANIFEST.read_text()
    assert 'android:supportsRtl="true"' in text
    assert 'android.intent.action.MAIN' in text
    assert 'android.intent.category.LAUNCHER' in text

def test_p24_main_activity_uses_safe_drawing_and_adaptive_widths():
    text = MAIN.read_text()
    assert 'WindowInsets.safeDrawing' in text
    assert 'BoxWithConstraints' in text
    assert 'maxWidth < 600.dp' in text
    assert 'maxWidth < 840.dp' in text
    assert 'widthIn(max = 720.dp)' in text

def test_p24_touch_and_text_scaling_contract_is_preserved():
    text = MAIN.read_text()
    assert 'heightIn(min = 48.dp)' in text
    assert 'heightIn(min = 52.dp)' in text
    assert 'heightIn(min = 78.dp)' in text
    assert 'lineHeight = 20.sp' in text

def test_p24_android_target_and_abi_contract():
    text = GRADLE.read_text()
    assert 'compileSdk = 36' in text
    assert 'targetSdk = 35' in text
    assert 'abiFilters += listOf("arm64-v8a", "x86_64")' in text
    assert 'jvmToolchain(17)' in text