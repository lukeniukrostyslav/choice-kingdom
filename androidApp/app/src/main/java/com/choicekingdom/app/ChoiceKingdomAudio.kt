package com.choicekingdom.app

import android.content.Context
import android.media.AudioAttributes
import android.media.AudioFocusRequest
import android.media.AudioManager
import android.media.ToneGenerator
import android.os.Build
import android.os.Handler
import android.os.Looper

/**
 * Foreground-only offline audio policy.
 *
 * Uses Android's platform tone for short interaction feedback, so no network
 * or bundled audio asset is required for the interaction layer. Authored music
 * and ambience remain separate product assets.
 */
class ChoiceKingdomAudio(private val context: Context) : AutoCloseable {
    private val audioManager = context.getSystemService(Context.AUDIO_SERVICE) as AudioManager
    private var focusRequest: AudioFocusRequest? = null
    private var focusGranted = false
    private var muted = false
    private var volume = 1f
    private var foreground = true
    private val mainHandler = Handler(Looper.getMainLooper())
    private var tone = ToneGenerator(AudioManager.STREAM_MUSIC, 80)

    fun setForeground(value: Boolean) {
        foreground = value
        if (!value) {
            tone.stopTone()
            abandonFocus()
        }
    }

    fun setMuted(value: Boolean) {
        muted = value
    }

    fun setVolume(value: Float) {
        volume = value.coerceIn(0f, 1f)
        tone.stopTone()
        tone.release()
        tone = ToneGenerator(AudioManager.STREAM_MUSIC, (volume * 100f).toInt().coerceIn(0, 100))
    }

    fun playChoiceFeedback() {
        if (!foreground || muted || volume <= 0f || !requestFocus()) return
        tone.startTone(ToneGenerator.TONE_PROP_BEEP, 45)
        mainHandler.postDelayed({ abandonFocus() }, 100)
    }

    private fun abandonFocus() {
        if (!focusGranted) return
        focusRequest?.let(audioManager::abandonAudioFocusRequest)
        focusGranted = false
    }

    private fun requestFocus(): Boolean {
        if (focusGranted) return true
        val attributes = AudioAttributes.Builder()
            .setUsage(AudioAttributes.USAGE_GAME)
            .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
            .build()
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val request = AudioFocusRequest.Builder(AudioManager.AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK)
                .setAudioAttributes(attributes)
                .setOnAudioFocusChangeListener { change ->
                    if (change == AudioManager.AUDIOFOCUS_LOSS || change == AudioManager.AUDIOFOCUS_LOSS_TRANSIENT) {
                        tone.stopTone()
                        focusGranted = false
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
            AudioManager.AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK,
        ) == AudioManager.AUDIOFOCUS_REQUEST_GRANTED
        return focusGranted
    }

    override fun close() {
        mainHandler.removeCallbacksAndMessages(null)
        tone.stopTone()
        tone.release()
        abandonFocus()
    }
}
