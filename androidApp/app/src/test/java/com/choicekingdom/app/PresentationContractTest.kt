package com.choicekingdom.app

import org.junit.Assert.assertEquals
import org.junit.Assert.assertSame
import org.junit.Test

class PresentationContractTest {
    @Test fun adapterPreservesImmutableRuntimeProjection() {
        val projection = AndroidEventProjection(
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
        val projection = AndroidEventProjection("E02", "The Crossing", 2, emptyList(), false)
        val port = AndroidPresentationPort.fromSnapshot(projection)
        assertSame(projection, port.snapshot())
    }
}
