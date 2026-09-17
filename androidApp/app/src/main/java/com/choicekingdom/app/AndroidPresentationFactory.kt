package com.choicekingdom.app

/** Explicit boundary: Android can render runtime projections, but cannot create them. */
object AndroidPresentationFactory {
    fun event(
        eventId: String,
        title: String,
        turn: Int,
        choices: List<AndroidChoice>,
        terminal: Boolean,
    ): AndroidEventProjection = AndroidEventProjection(eventId, title, turn, choices.toList(), terminal)
}
