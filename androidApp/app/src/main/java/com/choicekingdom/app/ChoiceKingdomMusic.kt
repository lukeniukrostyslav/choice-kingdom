package com.choicekingdom.app

import android.content.Context
import androidx.media3.common.AudioAttributes
import androidx.media3.common.C
import androidx.media3.common.MediaItem
import androidx.media3.common.Player
import androidx.media3.exoplayer.ExoPlayer

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

    init {
        player.setMediaItem(MediaItem.fromUri("android.resource://" + context.packageName + "/" + com.choicekingdom.app.R.raw.ambient_avelune))
        player.prepare()
        player.volume = volume
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
        player.volume = if (muted) 0f else volume
    }

    fun setVolume(value: Float) {
        volume = value.coerceIn(0f, 1f)
        player.volume = volume
    }

    fun setScene(sceneKey: String) {
        scene = sceneKey
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
        player.release()
    }
}
