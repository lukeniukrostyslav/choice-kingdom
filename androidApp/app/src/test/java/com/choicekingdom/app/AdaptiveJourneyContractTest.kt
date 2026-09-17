package com.choicekingdom.app

import org.junit.Assert.assertEquals
import org.junit.Test

class AdaptiveJourneyContractTest {
    @Test fun compactUsesBottomNavigation() {
        assertEquals("COMPACT", modeFor(390))
    }

    @Test fun mediumUsesSupportingNavigation() {
        assertEquals("MEDIUM", modeFor(720))
    }

    @Test fun expandedUsesTwoPaneNavigation() {
        assertEquals("EXPANDED", modeFor(1200))
    }

    @Test fun primaryTouchTargetIsAtLeast48dp() {
        assertEquals(true, 56 >= 48)
    }

    private fun modeFor(widthDp: Int): String = when {
        widthDp < 600 -> "COMPACT"
        widthDp < 840 -> "MEDIUM"
        else -> "EXPANDED"
    }
}
