package com.choicekingdom.app

import androidx.compose.runtime.Composable
import android.content.res.Configuration
import androidx.compose.ui.tooling.preview.Preview
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


@PreviewTest
@Preview(name = "event-ru", widthDp = 360, heightDp = 760, locale = "ru", showBackground = true)
@Preview(name = "event-uk", widthDp = 360, heightDp = 760, locale = "uk", showBackground = true)
@Preview(name = "event-it", widthDp = 360, heightDp = 760, locale = "it", showBackground = true)
@Preview(name = "event-de", widthDp = 360, heightDp = 760, locale = "de", showBackground = true)
@Preview(name = "event-fr", widthDp = 360, heightDp = 760, locale = "fr", showBackground = true)
@Preview(name = "event-es", widthDp = 360, heightDp = 760, locale = "es", showBackground = true)
@Preview(name = "event-pt", widthDp = 360, heightDp = 760, locale = "pt", showBackground = true)
@Composable
fun EventCoreLocalesScreenshot() = VisualRegressionEventPreview()

@PreviewTest
@Preview(name = "event-font-large", widthDp = 360, heightDp = 760, fontScale = 1.3f, showBackground = true)
@Composable
fun EventLargeTextScreenshot() = VisualRegressionEventPreview()

@PreviewTest
@Preview(name = "settings-font-large", widthDp = 600, heightDp = 900, fontScale = 1.3f, showBackground = true)
@Composable
fun SettingsLargeTextScreenshot() = VisualRegressionSettingsPreview()


@PreviewTest
@Preview(name = "loading-compact", widthDp = 360, heightDp = 760, showBackground = true)
@Composable
fun LoadingCompactScreenshot() = VisualRegressionLoadingPreview()

@PreviewTest
@Preview(name = "event-dark", widthDp = 360, heightDp = 760, uiMode = Configuration.UI_MODE_NIGHT_YES, showBackground = true)
@Composable
fun EventDarkModeScreenshot() = VisualRegressionEventPreview()

@PreviewTest
@Preview(name = "ending-dark", widthDp = 600, heightDp = 760, uiMode = Configuration.UI_MODE_NIGHT_YES, showBackground = true)
@Composable
fun EndingDarkModeScreenshot() = VisualRegressionEndingPreview()

@PreviewTest
@Preview(name = "settings-dark", widthDp = 600, heightDp = 900, uiMode = Configuration.UI_MODE_NIGHT_YES, showBackground = true)
@Composable
fun SettingsDarkModeScreenshot() = VisualRegressionSettingsPreview()
