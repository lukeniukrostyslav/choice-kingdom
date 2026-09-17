package com.choicekingdom.app

import android.content.Context
import android.os.Handler
import android.os.Looper
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import org.json.JSONObject
import java.io.File
import java.util.concurrent.Executors
import java.util.concurrent.atomic.AtomicBoolean

/**
 * Production Android adapter for the canonical GameSession.
 *
 * The Android layer sends only user intents and renders immutable projections.
 * Gameplay rules remain in the Python runtime and are never reimplemented here.
 */
class CanonicalAndroidRuntime(private val context: Context) {
    companion object { private const val KEY_RUN_ID = "run_id" }
    private val executor = Executors.newSingleThreadExecutor()
    private val main = Handler(Looper.getMainLooper())
    private val started = AtomicBoolean(false)
    private var runtime: com.chaquo.python.PyObject? = null
    private val preferences = context.getSharedPreferences("choice_kingdom_runtime", Context.MODE_PRIVATE)

    fun start(
        runId: String,
        onProjection: (AndroidEventProjection) -> Unit,
        onError: (Throwable) -> Unit,
    ) {
        executor.execute {
            try {
                val root = installCanonicalDocs()
                ensurePython()
                val module = Python.getInstance().getModule("runtime.android_runtime")
                val persistedRunId = preferences.getString(KEY_RUN_ID, null)
                val activeRunId = persistedRunId ?: runId
                runtime = module.callAttr("start", root.absolutePath, activeRunId)
                preferences.edit().putString(KEY_RUN_ID, activeRunId).apply()
                emitProjection(runtime!!.callAttr("snapshot_json").toString(), onProjection)
            } catch (error: Throwable) {
                main.post { onError(error) }
            }
        }
    }

    fun choose(
        choiceId: String,
        onProjection: (AndroidEventProjection) -> Unit,
        onError: (Throwable) -> Unit,
    ) {
        executor.execute {
            try {
                val active = runtime ?: error("canonical runtime has not started")
                emitProjection(active.callAttr("choose", choiceId).toString(), onProjection)
            } catch (error: Throwable) {
                main.post { onError(error) }
            }
        }
    }

    fun close() {
        executor.shutdownNow()
    }

    private fun ensurePython() {
        if (Python.isStarted()) return
        Python.start(AndroidPlatform(context.applicationContext))
    }

    private fun emitProjection(
        json: String,
        onProjection: (AndroidEventProjection) -> Unit,
    ) {
        val payload = JSONObject(json)
        val choicesJson = payload.getJSONArray("choices")
        val choices = buildList(choicesJson.length()) {
            for (index in 0 until choicesJson.length()) {
                val choice = choicesJson.getJSONObject(index)
                add(
                    AndroidChoice(
                        id = choice.getString("id"),
                        label = choice.getString("label"),
                        text = choice.getString("text"),
                        state = choice.optString("state", "idle"),
                    ),
                )
            }
        }
        val projection = AndroidEventProjection(
            eventId = payload.getString("event_id"),
            title = payload.getString("title"),
            turn = payload.getInt("turn"),
            choices = choices,
            terminal = payload.getBoolean("terminal"),
        )
        main.post { onProjection(projection) }
    }

    private fun installCanonicalDocs(): File {
        val target = File(context.filesDir, "choice-kingdom-canonical/docs")
        if (started.compareAndSet(false, true)) {
            target.mkdirs()
            copyAssetTree(context, "", target)
        }
        return target.parentFile ?: error("canonical runtime root unavailable")
    }

    private fun copyAssetTree(context: Context, assetPath: String, target: File) {
        val children = context.assets.list(assetPath).orEmpty()
        if (children.isEmpty()) {
            val destination = File(target, assetPath.substringAfterLast('/'))
            destination.parentFile?.mkdirs()
            context.assets.open(assetPath).use { input ->
                destination.outputStream().use { output -> input.copyTo(output) }
            }
            return
        }
        for (child in children) {
            val childPath = if (assetPath.isEmpty()) child else "$assetPath/$child"
            val childTarget = File(target, child)
            if (context.assets.list(childPath).orEmpty().isNotEmpty()) {
                childTarget.mkdirs()
                copyAssetTree(context, childPath, target)
            } else {
                childTarget.parentFile?.mkdirs()
                context.assets.open(childPath).use { input ->
                    childTarget.outputStream().use { output -> input.copyTo(output) }
                }
            }
        }
    }
}
