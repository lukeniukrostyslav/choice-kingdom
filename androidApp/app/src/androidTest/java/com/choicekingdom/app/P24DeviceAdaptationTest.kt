package com.choicekingdom.app

import android.content.Context
import androidx.test.core.app.ActivityScenario
import androidx.test.ext.junit.runners.AndroidJUnit4
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class P24DeviceAdaptationTest {
    @Test
    fun mainActivityRendersInsideTargetWindowClass() {
        ActivityScenario.launch(MainActivity::class.java).use { scenario ->
            scenario.onActivity { activity ->
                val widthDp = activity.resources.configuration.screenWidthDp
                val heightDp = activity.resources.configuration.screenHeightDp
                assertTrue("window width must be positive", widthDp > 0)
                assertTrue("window height must be positive", heightDp > 0)
                assertEquals("com.choicekingdom.app", activity.packageName)
                assertTrue("P24 requires at least a compact phone window", widthDp >= 320)
            }
        }
    }
}