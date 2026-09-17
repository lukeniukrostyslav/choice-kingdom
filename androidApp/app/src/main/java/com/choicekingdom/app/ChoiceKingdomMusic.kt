package com.choicekingdom.app

import android.content.Context
import androidx.media3.common.AudioAttributes
import androidx.media3.common.C
import androidx.media3.common.MediaItem
import androidx.media3.common.Player
import androidx.media3.exoplayer.ExoPlayer
import android.os.Handler
import android.os.Looper

/**
 * Foreground-only authored music channel.
 *
 * Media3 owns audio-focus behavior for the music player. The current repository
 * contains one Avelune atmospheric prototype track; scene-aware track routing
 * remains open until the final authored soundtrack assets exist.
 */
class ChoiceKingdomMusic(context: Context) : AutoCloseable {
    private val player = ExoPlayer.Builder(context).build().apply {
        setAudioAttributes(
            AudioAttributes.Builder()
                .setUsage(C.USAGE_GAME)
                .setContentType(C.AUDIO_CONTENT_TYPE_MUSIC)
                .build(),
            true,
        )
        setHandleAudioBecomingNoisy(true)
        repeatMode = Player.REPEAT_MODE_ONE
    }

    private var foreground = true
    private var volume = 0.55f
    private var scene = "Event"
    private val handler = Handler(Looper.getMainLooper())
    private var fadeGeneration = 0L

    init {
        player.setMediaItem(MediaItem.fromUri("android.resource://" + context.packageName + "/" + com.choicekingdom.app.R.raw.ambient_avelune))
        player.prepare()
        player.volume = sceneGain(scene) * volume
    }

    fun setForeground(value: Boolean) {
        foreground = value
        if (value) {
            if (!player.isPlaying && player.playbackState != Player.STATE_ENDED) player.playWhenReady = true
        } else {
            player.playWhenReady = false
        }
    }

    fun setMuted(muted: Boolean) {
        player.volume = if (muted) 0f else sceneGain(scene) * volume
    }

    fun setVolume(value: Float) {
        volume = value.coerceIn(0f, 1f)
        player.volume = volume
    }

    fun setScene(sceneKey: String) {
        if (scene == sceneKey) return
        scene = sceneKey
        fadeTo(sceneGain(sceneKey) * volume, 650L)
    }

    private fun sceneGain(sceneKey: String): Float = when (sceneKey) {
        "Event" -> 1.0f
        "Realm" -> 0.78f
        "History" -> 0.68f
        "People" -> 0.72f
        "Investigation" -> 0.58f
        "Ending" -> 0.88f
        "Settings" -> 0.45f
        else -> 0.70f
    }

    private fun fadeTo(target: Float, durationMs: Long) {
        val generation = ++fadeGeneration
        val start = player.volume
        val steps = 13
        for (step in 1..steps) {
            handler.postDelayed({
                if (generation != fadeGeneration) return@postDelayed
                val progress = step / steps.toFloat()
                player.volume = start + (target - start) * progress
            }, durationMs * step / steps)
        }
    }

    val currentScene: String
        get() = scene

    fun play() {
        if (foreground) player.play()
    }

    fun pause() {
        player.pause()
    }

    override fun close() {
        ++fadeGeneration
        handler.removeCallbacksAndMessages(null)
        player.release()
    }
}
