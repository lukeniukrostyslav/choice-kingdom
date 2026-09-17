package com.choicekingdom.app

import org.junit.Assert.assertEquals
import org.junit.Assert.assertSame
import org.junit.Test

class PresentationContractTest {
    @Test fun adapterPreservesImmutableRuntimeProjection() {
        val projection = AndroidPresentationFactory.event(
            eventId = "E01",
            title = "Avelune",
            turn = 1,
            choices = listOf(AndroidChoice("E01-A", "A", "Choose A", "idle")),
            terminal = false,
        )
        val port = AndroidPresentationPort.fromSnapshot(projection)
        assertEquals(projection, port.snapshot())
    }

    @Test fun adapterDoesNotInventGameplayState() {
        val projection = AndroidPresentationFactory.event("E02", "The Crossing", 2, emptyList(), false)
        val port = AndroidPresentationPort.fromSnapshot(projection)
        assertSame(projection, port.snapshot())
    }

    @Test fun factoryCopiesChoiceCollectionAtBoundary() {
        val source = mutableListOf(AndroidChoice("E01-A", "A", "Choose A"))
        val projection = AndroidPresentationFactory.event("E01", "Avelune", 1, source, false)
        source.clear()
        assertEquals(1, projection.choices.size)
    }
}
