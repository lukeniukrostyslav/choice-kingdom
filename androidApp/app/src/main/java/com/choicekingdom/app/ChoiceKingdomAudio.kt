package com.choicekingdom.app

import android.content.Context
import android.media.AudioAttributes
import android.media.AudioFocusRequest
import android.media.SoundPool
import android.media.AudioManager
import android.media.ToneGenerator
import android.os.Build
import android.os.Handler
import android.os.Looper

/**
 * Foreground-only offline audio policy.
 *
 * Uses bundled offline WAV assets for authored interaction feedback and ambient
 * playback, with platform-tone fallback when an asset is unavailable. No network
 * audio is required; final soundtrack production remains a separate product layer.
 */
class ChoiceKingdomAudio(private val context: Context) : AutoCloseable {
    private val prefs = context.getSharedPreferences("choice_kingdom_audio", Context.MODE_PRIVATE)
    private val audioManager = context.getSystemService(Context.AUDIO_SERVICE) as AudioManager
    private var focusRequest: AudioFocusRequest? = null
    private var focusGranted = false
    private var muted = prefs.getBoolean("muted", false)
    private var volume = prefs.getFloat("volume", 1f)
    private var musicVolume = prefs.getFloat("music_volume", 0.55f)
    private var ambientVolume = prefs.getFloat("ambient_volume", 0.35f)
    private var foreground = true
    private val soundIds = mutableMapOf<String, Int>()
    private var pendingLoads = 0
    private var soundsReady = false
    private var ambientStreamId = 0
    private var ambientPausedByFocus = false
    private var ambientDuckedByFocus = false
    private val mainHandler = Handler(Looper.getMainLooper())
    private var tone = ToneGenerator(AudioManager.STREAM_MUSIC, 80)
    private val soundPool = SoundPool.Builder().setMaxStreams(4).setAudioAttributes(
        AudioAttributes.Builder().setUsage(AudioAttributes.USAGE_GAME).setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION).build()
    ).build()

    fun setForeground(value: Boolean) {
        foreground = value
        if (!value) {
            tone.stopTone()
            soundPool.autoPause()
            stopAmbient()
            abandonFocus()
        }
    }

    val isMuted: Boolean get() = muted
    val currentVolume: Float get() = volume
    val currentAmbientVolume: Float get() = ambientVolume
    val currentMusicVolume: Float get() = musicVolume

    fun setMuted(value: Boolean) {
        muted = value
        prefs.edit().putBoolean("muted", value).apply()
    }

    fun setVolume(value: Float) {
        volume = value.coerceIn(0f, 1f)
        prefs.edit().putFloat("volume", volume).apply()
        if (ambientStreamId != 0) soundPool.setVolume(ambientStreamId, ambientVolume * volume, ambientVolume * volume)
        tone.stopTone()
        tone.release()
        tone = ToneGenerator(AudioManager.STREAM_MUSIC, (volume * 100f).toInt().coerceIn(0, 100))
    }

    fun loadBundledSfx(resources: android.content.res.Resources, packageName: String) {
        if (soundsReady) return
        val names = listOf("choice_click", "choice_confirm", "choice_error", "ambient_avelune")
        pendingLoads = names.count { resources.getIdentifier(it, "raw", packageName) != 0 }
        names.forEach { name ->
            val id = resources.getIdentifier(name, "raw", packageName)
            if (id != 0) soundIds[name] = soundPool.load(context, id, 1)
        }
        soundPool.setOnLoadCompleteListener { _, _, status -> if (status == 0) { pendingLoads -= 1; if (pendingLoads <= 0) { soundsReady = true; startAmbient() } } }
    }

    fun setMusicVolume(value: Float) {
        musicVolume = value.coerceIn(0f, 1f)
        prefs.edit().putFloat("music_volume", musicVolume).apply()
    }

    fun setAmbientVolume(value: Float) {
        ambientVolume = value.coerceIn(0f, 1f)
        prefs.edit().putFloat("ambient_volume", ambientVolume).apply()
        if (ambientStreamId != 0) soundPool.setVolume(ambientStreamId, ambientVolume * volume, ambientVolume * volume)
    }

    fun startAmbient() {
        if (!foreground || muted || ambientVolume <= 0f || !soundsReady || ambientStreamId != 0) return
        val id = soundIds["ambient_avelune"] ?: return
        if (!requestFocus(permanent = true)) return
        ambientStreamId = soundPool.play(id, ambientVolume * volume, ambientVolume * volume, 0, -1, 1f)
    }

    fun fadeAmbientTo(targetVolume: Float, durationMs: Long = 500L) {
        if (ambientStreamId == 0) return
        val target = targetVolume.coerceIn(0f, 1f) * volume
        val steps = 10
        val start = ambientVolume * volume
        repeat(steps) { index ->
            mainHandler.postDelayed({
                if (ambientStreamId != 0) {
                    val fraction = (index + 1).toFloat() / steps
                    val level = start + (target - start) * fraction
                    soundPool.setVolume(ambientStreamId, level, level)
                }
            }, durationMs * (index + 1) / steps)
        }
    }

    fun stopAmbient() {
        if (ambientStreamId != 0) {
            soundPool.stop(ambientStreamId)
            ambientStreamId = 0
            ambientPausedByFocus = false
            ambientDuckedByFocus = false
        }
    }

    fun playChoiceFeedback() {
        playBundled("choice_click", ToneGenerator.TONE_PROP_BEEP, 45)
    }

    fun playConfirmFeedback() {
        playBundled("choice_confirm", ToneGenerator.TONE_PROP_ACK, 70)
    }

    fun playErrorFeedback() {
        playBundled("choice_error", ToneGenerator.TONE_PROP_NACK, 90)
    }

    private fun playBundled(name: String, fallbackTone: Int, durationMs: Int) {
        if (foreground && !muted && volume > 0f && soundsReady) {
            val id = soundIds[name]
            if (id != null) {
                if (requestFocus()) {
                    soundPool.play(id, volume, volume, 1, 0, 1f)
                    mainHandler.postDelayed({ abandonFocus() }, durationMs.toLong() + 40L)
                }
                return
            }
        }
        playTone(fallbackTone, durationMs)
    }

    private fun playTone(toneType: Int, durationMs: Int) {
        if (!foreground || muted || volume <= 0f || !requestFocus()) return
        tone.startTone(toneType, durationMs)
        mainHandler.postDelayed({ abandonFocus() }, 100)
    }

    private fun abandonFocus() {
        if (!focusGranted) return
        focusRequest?.let(audioManager::abandonAudioFocusRequest)
        focusGranted = false
    }

    private fun requestFocus(permanent: Boolean = false): Boolean {
        if (focusGranted) return true
        val attributes = AudioAttributes.Builder()
            .setUsage(AudioAttributes.USAGE_GAME)
            .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
            .build()
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val request = AudioFocusRequest.Builder(if (permanent) AudioManager.AUDIOFOCUS_GAIN else AudioManager.AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK)
                .setAudioAttributes(attributes)
                .setOnAudioFocusChangeListener { change ->
                    when (change) {
                        AudioManager.AUDIOFOCUS_LOSS -> {
                            tone.stopTone()
                            stopAmbient()
                            focusGranted = false
                        }
                        AudioManager.AUDIOFOCUS_LOSS_TRANSIENT -> {
                            tone.stopTone()
                            if (ambientStreamId != 0) {
                                soundPool.autoPause()
                                ambientPausedByFocus = true
                            }
                            focusGranted = false
                        }
                        AudioManager.AUDIOFOCUS_LOSS_TRANSIENT_CAN_DUCK -> {
                            if (ambientStreamId != 0 && !ambientDuckedByFocus) {
                                soundPool.setVolume(ambientStreamId, ambientVolume * volume * 0.35f, ambientVolume * volume * 0.35f)
                                ambientDuckedByFocus = true
                            }
                        }
                        AudioManager.AUDIOFOCUS_GAIN -> {
                            if (foreground && !muted) {
                                if (ambientPausedByFocus && ambientStreamId != 0) {
                                    soundPool.autoResume()
                                    ambientPausedByFocus = false
                                }
                                if (ambientDuckedByFocus && ambientStreamId != 0) {
                                    soundPool.setVolume(ambientStreamId, ambientVolume * volume, ambientVolume * volume)
                                    ambientDuckedByFocus = false
                                }
                            }
                        }
                    }
                }
                .build()
            focusRequest = request
            focusGranted = audioManager.requestAudioFocus(request) == AudioManager.AUDIOFOCUS_REQUEST_GRANTED
            return focusGranted
        }
        @Suppress("DEPRECATION")
        focusGranted = audioManager.requestAudioFocus(
            { change ->
                if (change <= 0) {
                    tone.stopTone()
                    focusGranted = false
                }
            },
            AudioManager.STREAM_MUSIC,
            if (permanent) AudioManager.AUDIOFOCUS_GAIN else AudioManager.AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK,
        ) == AudioManager.AUDIOFOCUS_REQUEST_GRANTED
        return focusGranted
    }

    override fun close() {
        mainHandler.removeCallbacksAndMessages(null)
        tone.stopTone()
        tone.release()
        soundPool.release()
        abandonFocus()
    }
}
