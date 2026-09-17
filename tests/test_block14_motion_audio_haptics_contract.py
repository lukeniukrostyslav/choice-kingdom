from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "androidApp/app/src/main/java/com/choicekingdom/app/MainActivity.kt"
FEEDBACK = ROOT / "androidApp/app/src/main/java/com/choicekingdom/app/ChoiceKingdomFeedback.kt"


def test_block14_motion_and_feedback_contract():
    main = MAIN.read_text(encoding="utf-8")
    feedback = FEEDBACK.read_text(encoding="utf-8")
    assert "AnimatedContent(" in main
    assert 'label = "journey-screen-transition"' in main
    assert "fadeIn()" in main and "fadeOut()" in main
    assert "scaleIn(initialScale = 0.98f)" in main
    assert "LocalHapticFeedback.current" in main
    assert "HapticFeedbackType.LongPress" in main
    assert "class ChoiceKingdomFeedback" in feedback
    assert "no network" in feedback


def test_block14_does_not_claim_authored_audio_assets():
    feedback = FEEDBACK.read_text(encoding="utf-8")
    assert "authored audio" in feedback
    assert "later asset/content concern" in feedback


def test_block14_audio_control_contract():
    audio = (ROOT / "androidApp/app/src/main/java/com/choicekingdom/app/ChoiceKingdomAudio.kt").read_text(encoding="utf-8")
    main = MAIN.read_text(encoding="utf-8")
    assert "AudioFocusRequest" in audio
    assert "USAGE_GAME" in audio
    assert "AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK" in audio
    assert "AUDIOFOCUS_LOSS" in audio
    assert "abandonAudioFocusRequest" in audio
    assert "postDelayed({ abandonFocus() }, 100)" in audio
    assert "removeCallbacksAndMessages(null)" in audio
    assert "setMuted" in audio
    assert "setVolume" in audio
    assert "Slider(" in main
    assert "Mute sound" in main


def test_block14_audio_foreground_lifecycle_contract():
    audio = (ROOT / "androidApp/app/src/main/java/com/choicekingdom/app/ChoiceKingdomAudio.kt").read_text(encoding="utf-8")
    main = MAIN.read_text(encoding="utf-8")
    assert "setForeground" in audio
    assert "if (!foreground || muted" in audio
    assert "LocalLifecycleOwner.current" in main
    assert "DefaultLifecycleObserver" in main
    assert "audio.setForeground(true)" in main
    assert "audio.setForeground(false)" in main
