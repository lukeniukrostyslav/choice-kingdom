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


def test_block14_persistent_audio_preferences_and_feedback_variants():
    audio = (ROOT / "androidApp/app/src/main/java/com/choicekingdom/app/ChoiceKingdomAudio.kt").read_text(encoding="utf-8")
    main = MAIN.read_text(encoding="utf-8")
    assert "getSharedPreferences" in audio
    assert '"muted"' in audio and '"volume"' in audio
    assert "playConfirmFeedback" in audio
    assert "playErrorFeedback" in audio
    assert "audio.playErrorFeedback()" in main
    assert "LaunchedEffect(audio)" in main


def test_block14_bundled_sfx_assets_exist():
    for name in ("choice_click.wav", "choice_confirm.wav", "choice_error.wav"):
        path = ROOT / "androidApp/app/src/main/res/raw" / name
        assert path.exists()
        assert path.stat().st_size > 44


def test_block14_ambient_audio_contract():
    audio = (ROOT / "androidApp/app/src/main/java/com/choicekingdom/app/ChoiceKingdomAudio.kt").read_text(encoding="utf-8")
    main = MAIN.read_text(encoding="utf-8")
    assert '"ambient_avelune"' in audio
    assert "startAmbient" in audio
    assert "stopAmbient" in audio
    assert "ambientVolume" in audio
    assert "AUDIOFOCUS_GAIN" in audio
    assert "play(id, ambientVolume * volume" in audio
    assert "audio.startAmbient()" in main
    ambient = ROOT / "androidApp/app/src/main/res/raw/ambient_avelune.wav"
    assert ambient.exists() and ambient.stat().st_size > 44


def test_block14_audio_fade_and_focus_recovery_contract():
    audio = (ROOT / "androidApp/app/src/main/java/com/choicekingdom/app/ChoiceKingdomAudio.kt").read_text(encoding="utf-8")
    assert "fadeAmbientTo" in audio
    assert "soundPool.setVolume" in audio
    assert "AUDIOFOCUS_GAIN" in audio
    assert "autoResume()" in audio
    assert "ambientPausedByFocus" in audio


def test_block14_audio_state_is_threaded_to_choice_and_settings():
    main = (ROOT / "androidApp/app/src/main/java/com/choicekingdom/app/MainActivity.kt").read_text(encoding="utf-8")
    assert "audio = audio" in main
    assert "audioMuted = audioMuted" in main
    assert "audioVolume = audioVolume" in main
    assert "ambientVolume = ambientVolume" in main
    assert "onAudioMutedChanged" in main
    assert "onAudioVolumeChanged" in main
    assert "onAmbientVolumeChanged" in main
