package com.choicekingdom.app

import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.hasStateDescription
import androidx.compose.ui.test.hasText
import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.compose.ui.test.performClick
import org.junit.Rule
import org.junit.Test

class ChoiceKingdomAppTest {
    @get:Rule
    val composeRule = createAndroidComposeRule<MainActivity>()

    @Test
    fun eventProjectionIsRenderedAsChoices() {
        composeRule.onNode(hasText("The First Choice")).assertIsDisplayed()
        composeRule.onNode(hasText("Approach")).assertIsDisplayed()
        composeRule.onNode(hasText("Wait")).assertIsDisplayed()
        composeRule.onNode(hasText("Leave")).assertIsDisplayed()
        composeRule.onNode(hasText("YOUR DECISION")).assertIsDisplayed()
    }

    @Test
    fun selectingChoiceChangesAccessibleState() {
        composeRule.onNode(hasText("Approach")).performClick()
        composeRule.onNode(hasStateDescription("Selected").and(hasText("Approach"))).assertIsDisplayed()
        composeRule.onNode(hasText("SELECTED")).assertIsDisplayed()
    }

    @Test
    fun navigationRevealsEveryPrimarySurface() {
        listOf("Realm", "History", "People", "Investigation", "Ending", "Settings").forEach { destination ->
            composeRule.onNode(hasText(destination, substring = false)).performClick()
            composeRule.onNode(hasText(destination.uppercase())).assertIsDisplayed()
        }
    }

    private infix fun androidx.compose.ui.test.SemanticsMatcher.and(other: androidx.compose.ui.test.SemanticsMatcher): androidx.compose.ui.test.SemanticsMatcher =
        androidx.compose.ui.test.SemanticsMatcher("($this) and ($other)") { node ->
            this.matches(node) && other.matches(node)
        }
}
