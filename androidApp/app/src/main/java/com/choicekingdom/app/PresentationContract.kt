package com.choicekingdom.app

/** Presentation-only seam for the canonical runtime.
 *
 * The Android layer consumes immutable projections and emits user intents.
 * It deliberately does not implement gameplay rules, routing, persistence,
 * consequence scheduling, or authored-content semantics.
 */
data class AndroidChoice(
    val id: String,
    val label: String,
    val text: String,
    val state: String = "idle",
)

data class AndroidEventProjection(
    val eventId: String,
    val title: String,
    val turn: Int,
    val choices: List<AndroidChoice>,
    val terminal: Boolean,
)

fun interface AndroidPresentationPort {
    fun snapshot(): AndroidEventProjection
}

/** Pure adapter from an already-produced runtime projection into Android data.
 * No gameplay computation or mutation is permitted here.
 */
fun AndroidPresentationPort.fromSnapshot(snapshot: AndroidEventProjection): AndroidPresentationPort = AndroidPresentationPort { snapshot }
