package com.choicekingdom.app

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.Typography
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp

private val ChoiceKingdomColors = darkColorScheme(
    primary = Color(0xFFD6B46A),
    onPrimary = Color(0xFF19140A),
    secondary = Color(0xFFB7C4D8),
    background = Color(0xFF090C12),
    surface = Color(0xFF111722),
    surfaceVariant = Color(0xFF242D3A),
    onSurface = Color(0xFFF4F0E7),
)

private val ChoiceKingdomTypography = Typography(
    headlineLarge = androidx.compose.ui.text.TextStyle(fontSize = 42.sp, lineHeight = 48.sp, fontWeight = FontWeight.SemiBold),
    headlineMedium = androidx.compose.ui.text.TextStyle(fontSize = 36.sp, lineHeight = 42.sp, fontWeight = FontWeight.SemiBold),
    headlineSmall = androidx.compose.ui.text.TextStyle(fontSize = 30.sp, lineHeight = 36.sp, fontWeight = FontWeight.SemiBold),
    bodyLarge = androidx.compose.ui.text.TextStyle(fontSize = 16.sp, lineHeight = 24.sp),
    bodyMedium = androidx.compose.ui.text.TextStyle(fontSize = 14.sp, lineHeight = 20.sp),
)

@Composable
fun ChoiceKingdomTheme(content: @Composable () -> Unit) {
    MaterialTheme(colorScheme = ChoiceKingdomColors, typography = ChoiceKingdomTypography, content = content)
}
