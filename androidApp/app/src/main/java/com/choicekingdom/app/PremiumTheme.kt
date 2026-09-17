package com.choicekingdom.app

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val ChoiceKingdomColors = darkColorScheme(
    primary = Color(0xFFD6B46A),
    onPrimary = Color(0xFF19140A),
    secondary = Color(0xFFB7C4D8),
    background = Color(0xFF090C12),
    surface = Color(0xFF111722),
    onSurface = Color(0xFFF4F0E7),
)

@Composable
fun ChoiceKingdomTheme(content: @Composable () -> Unit) {
    MaterialTheme(colorScheme = ChoiceKingdomColors, content = content)
}
