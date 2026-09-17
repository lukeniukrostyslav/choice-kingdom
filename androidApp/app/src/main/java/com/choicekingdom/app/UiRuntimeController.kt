package com.choicekingdom.app

/**
 * Deterministic UI-only state machine for the Android presentation layer.
 * Gameplay remains owned by the canonical runtime; this class only records
 * navigation and transient interaction state for rendering.
 */
enum class PrimarySurface { EVENT, REALM, HISTORY, PEOPLE, INVESTIGATION, ENDING, SETTINGS }

enum class ChoiceVisualState { IDLE, FOCUSED, SELECTED, PRESSED, RESOLVING, RESOLVED, DISABLED, BLOCKED, ERROR }

data class UiRuntimeState(
    val surface: PrimarySurface = PrimarySurface.EVENT,
    val focusedChoiceId: String? = null,
    val selectedChoiceId: String? = null,
    val pressedChoiceId: String? = null,
    val resolvingChoiceId: String? = null,
    val resolvedChoiceId: String? = null,
    val blockedChoiceId: String? = null,
    val errorChoiceId: String? = null,
)

sealed interface UiIntent {
    data class Navigate(val surface: PrimarySurface) : UiIntent
    data class FocusChoice(val choiceId: String) : UiIntent
    data class SelectChoice(val choiceId: String) : UiIntent
    data class PressChoice(val choiceId: String) : UiIntent
    data class BeginResolve(val choiceId: String) : UiIntent
    data class ResolveSuccess(val choiceId: String) : UiIntent
    data class ResolveFailure(val choiceId: String) : UiIntent
    data class BlockChoice(val choiceId: String) : UiIntent
    data object ClearTransient : UiIntent
}

fun reduceUiState(state: UiRuntimeState, intent: UiIntent): UiRuntimeState = when (intent) {
    is UiIntent.Navigate -> state.copy(surface = intent.surface, errorChoiceId = null)
    is UiIntent.FocusChoice -> clearChoiceState(state).copy(focusedChoiceId = intent.choiceId)
    is UiIntent.SelectChoice -> clearChoiceState(state).copy(selectedChoiceId = intent.choiceId)
    is UiIntent.PressChoice -> clearChoiceState(state).copy(
        focusedChoiceId = intent.choiceId,
        pressedChoiceId = intent.choiceId,
    )
    is UiIntent.BeginResolve -> clearChoiceState(state).copy(resolvingChoiceId = intent.choiceId)
    is UiIntent.ResolveSuccess -> clearChoiceState(state).copy(resolvedChoiceId = intent.choiceId)
    is UiIntent.ResolveFailure -> clearChoiceState(state).copy(errorChoiceId = intent.choiceId)
    is UiIntent.BlockChoice -> clearChoiceState(state).copy(blockedChoiceId = intent.choiceId)
    UiIntent.ClearTransient -> clearChoiceState(state)
}

fun choiceVisualState(state: UiRuntimeState, choiceId: String, terminal: Boolean): ChoiceVisualState = when {
    terminal -> ChoiceVisualState.DISABLED
    state.errorChoiceId == choiceId -> ChoiceVisualState.ERROR
    state.blockedChoiceId == choiceId -> ChoiceVisualState.BLOCKED
    state.resolvingChoiceId == choiceId -> ChoiceVisualState.RESOLVING
    state.pressedChoiceId == choiceId -> ChoiceVisualState.PRESSED
    state.selectedChoiceId == choiceId -> ChoiceVisualState.SELECTED
    state.resolvedChoiceId == choiceId -> ChoiceVisualState.RESOLVED
    state.focusedChoiceId == choiceId -> ChoiceVisualState.FOCUSED
    else -> ChoiceVisualState.IDLE
}

private fun clearChoiceState(state: UiRuntimeState): UiRuntimeState = state.copy(
    focusedChoiceId = null,
    selectedChoiceId = null,
    pressedChoiceId = null,
    resolvingChoiceId = null,
    resolvedChoiceId = null,
    blockedChoiceId = null,
    errorChoiceId = null,
)
