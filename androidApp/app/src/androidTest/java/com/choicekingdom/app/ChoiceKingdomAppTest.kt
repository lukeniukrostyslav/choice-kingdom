package com.choicekingdom.app

import androidx.compose.ui.test.assertIsDisplayed
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
    }

    @Test
    fun selectingChoiceChangesAccessibleState() {
        composeRule.onNode(hasText("Approach")).performClick()
        composeRule.onNode(hasText("Approach")).assertIsDisplayed()
        composeRule.onNode(hasText("Approach")).assertIsDisplayed()
    }
}
