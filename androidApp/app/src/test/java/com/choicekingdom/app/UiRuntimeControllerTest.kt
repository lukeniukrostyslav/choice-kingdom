package com.choicekingdom.app

import org.junit.Assert.assertEquals
import org.junit.Test

class UiRuntimeControllerTest {
    @Test fun navigationIsDeterministicAcrossAllPrimarySurfaces() {
        var state = UiRuntimeState()
        PrimarySurface.entries.forEach { surface ->
            state = reduceUiState(state, UiIntent.Navigate(surface))
            assertEquals(surface, state.surface)
        }
    }

    @Test fun transientChoiceStatesNeverLeakIntoEachOther() {
        var state = UiRuntimeState()
        state = reduceUiState(state, UiIntent.FocusChoice("c1"))
        assertEquals(ChoiceVisualState.FOCUSED, choiceVisualState(state, "c1", false))
        state = reduceUiState(state, UiIntent.PressChoice("c1"))
        assertEquals(ChoiceVisualState.PRESSED, choiceVisualState(state, "c1", false))
        state = reduceUiState(state, UiIntent.BeginResolve("c1"))
        assertEquals(ChoiceVisualState.RESOLVING, choiceVisualState(state, "c1", false))
        state = reduceUiState(state, UiIntent.ResolveSuccess("c1"))
        assertEquals(ChoiceVisualState.RESOLVED, choiceVisualState(state, "c1", false))
    }

    @Test fun failureAndBlockedStatesAreExplicit() {
        var state = reduceUiState(UiRuntimeState(), UiIntent.BlockChoice("c2"))
        assertEquals(ChoiceVisualState.BLOCKED, choiceVisualState(state, "c2", false))
        state = reduceUiState(state, UiIntent.ResolveFailure("c3"))
        assertEquals(ChoiceVisualState.ERROR, choiceVisualState(state, "c3", false))
    }

    @Test fun terminalStateAlwaysDisablesChoices() {
        val state = reduceUiState(UiRuntimeState(), UiIntent.SelectChoice("c1"))
        assertEquals(ChoiceVisualState.DISABLED, choiceVisualState(state, "c1", true))
    }
}
