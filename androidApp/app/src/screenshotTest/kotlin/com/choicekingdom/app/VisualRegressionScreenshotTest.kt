package com.choicekingdom.app

import androidx.compose.runtime.Composable
import androidx.compose.ui.tooling.preview.Preview
import com.android.tools.screenshot.PreviewTest

import com.android.tools.screenshot.PreviewTest

@PreviewTest
@Preview(name = "event-compact", widthDp = 360, heightDp = 760, showBackground = true)
@Composable
fun EventCompactScreenshot() = VisualRegressionEventPreview()

@PreviewTest
@Preview(name = "event-expanded", widthDp = 840, heightDp = 900, showBackground = true)
@Composable
fun EventExpandedScreenshot() = VisualRegressionEventPreview()

@PreviewTest
@Preview(name = "choices-compact", widthDp = 360, heightDp = 760, showBackground = true)
@Composable
fun ChoicesCompactScreenshot() = VisualRegressionChoicePreview()

@PreviewTest
@Preview(name = "ending-medium", widthDp = 600, heightDp = 760, showBackground = true)
@Composable
fun EndingMediumScreenshot() = VisualRegressionEndingPreview()

@PreviewTest
@Preview(name = "navigation-expanded", widthDp = 1024, heightDp = 900, showBackground = true)
@Composable
fun NavigationExpandedScreenshot() = VisualRegressionNavigationPreview()

@PreviewTest
@Preview(name = "settings-medium", widthDp = 600, heightDp = 900, showBackground = true)
@Composable
fun SettingsMediumScreenshot() = VisualRegressionSettingsPreview()
