package com.choicekingdom.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.safeDrawing
import androidx.compose.foundation.layout.windowInsetsPadding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.role
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.semantics.stateDescription
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.TextUnit
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

private enum class WindowMode { COMPACT, MEDIUM, EXPANDED }

private data class AndroidScreenState(val title: String, val states: List<String>)

private val screens = listOf(
    AndroidScreenState("Event", listOf("Default", "Focused", "Pressed", "Selected", "Pending", "Error")),
    AndroidScreenState("Realm", listOf("Default", "Focused", "Pressed", "Disabled", "Selected")),
    AndroidScreenState("History", listOf("Default", "Focused", "Pressed", "Disabled", "Selected")),
    AndroidScreenState("People", listOf("Default", "Focused", "Pressed", "Disabled", "Selected")),
    AndroidScreenState("Investigation", listOf("Default", "Focused", "Pressed", "Selected", "Pending", "Success")),
    AndroidScreenState("Ending", listOf("Default", "Focused", "Pressed", "Disabled", "Success", "Failure")),
    AndroidScreenState("Settings", listOf("Default", "Focused", "Pressed", "Disabled", "Selected", "Error")),
)

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { ChoiceKingdomApp() }
    }
}

@Composable
private fun ChoiceKingdomApp() {
    var selectedScreen by mutableStateOf("Event")
    var selectedState by mutableStateOf("Default")
    val screen = screens.first { it.title == selectedScreen }

    MaterialTheme {
        Surface(modifier = Modifier.fillMaxSize(), color = Color(0xFF090C12)) {
            Box(modifier = Modifier.fillMaxSize().windowInsetsPadding(WindowInsets.safeDrawing).background(Color(0xFF090C12))) {
                AdaptiveJourney(screen, selectedState, { selectedScreen = it; selectedState = "Default" }, { selectedState = it })
            }
        }
    }
}

@Composable
private fun AdaptiveJourney(
    selectedScreen: AndroidScreenState,
    selectedState: String,
    onScreenSelected: (String) -> Unit,
    onStateSelected: (String) -> Unit,
) {
    BoxWithConstraints(modifier = Modifier.fillMaxSize()) {
        val mode = when { maxWidth < 600.dp -> WindowMode.COMPACT; maxWidth < 840.dp -> WindowMode.MEDIUM; else -> WindowMode.EXPANDED }
        val horizontal = when (mode) { WindowMode.COMPACT -> 16.dp; WindowMode.MEDIUM -> 28.dp; WindowMode.EXPANDED -> 48.dp }
        val titleSize = when (mode) { WindowMode.COMPACT -> 30.sp; WindowMode.MEDIUM -> 36.sp; WindowMode.EXPANDED -> 42.sp }
        if (mode == WindowMode.EXPANDED) {
            Row(modifier = Modifier.fillMaxSize().padding(horizontal = horizontal), horizontalArrangement = Arrangement.spacedBy(24.dp)) {
                NavigationRailLike(selectedScreen.title, onScreenSelected, Modifier.weight(0.34f))
                JourneyContent(selectedScreen, selectedState, onStateSelected, titleSize, Modifier.weight(0.66f))
            }
        } else {
            Column(modifier = Modifier.fillMaxSize()) {
                JourneyContent(selectedScreen, selectedState, onStateSelected, titleSize, Modifier.weight(1f).padding(horizontal = horizontal))
                ScreenNavigation(selectedScreen.title, onScreenSelected, Modifier.fillMaxWidth())
            }
        }
    }
}

@Composable
private fun JourneyContent(screen: AndroidScreenState, selectedState: String, onStateSelected: (String) -> Unit, titleSize: TextUnit, modifier: Modifier) {
    LazyColumn(modifier = modifier, contentPadding = PaddingValues(top = 24.dp, bottom = 28.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
        item {
            Text("CHOICE KINGDOM · AVELUNE", color = Color(0xFFD6B46A), fontSize = 12.sp, fontWeight = FontWeight.Bold)
            Text(screen.title, color = Color(0xFFF4F0E7), fontSize = titleSize, fontWeight = FontWeight.SemiBold)
            Text("Premium presentation · $selectedState", color = Color(0xFFAEB6C4), fontSize = 14.sp)
        }
        items(screen.states) { state ->
            val selected = state == selectedState
            Button(
                onClick = { onStateSelected(state) },
                modifier = Modifier.fillMaxWidth().height(56.dp).semantics {
                    role = Role.Button
                    contentDescription = "$state state"
                    stateDescription = if (selected) "Selected" else "Available"
                },
                colors = ButtonDefaults.buttonColors(containerColor = if (selected) Color(0xFF242D3A) else Color(0xFF151B25), contentColor = Color(0xFFF4F0E7)),
            ) { Text(state, textAlign = TextAlign.Start, modifier = Modifier.fillMaxWidth()) }
        }
    }
}

@Composable
private fun ScreenNavigation(current: String, onSelect: (String) -> Unit, modifier: Modifier) {
    Row(modifier = modifier.padding(12.dp), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
        screens.take(4).forEach { screen ->
            Button(onClick = { onSelect(screen.title) }, modifier = Modifier.weight(1f).height(52.dp), contentPadding = PaddingValues(horizontal = 4.dp)) { Text(screen.title, fontSize = 11.sp, maxLines = 1) }
        }
    }
}

@Composable
private fun NavigationRailLike(current: String, onSelect: (String) -> Unit, modifier: Modifier) {
    Card(modifier = modifier.padding(vertical = 24.dp)) {
        Column(modifier = Modifier.padding(12.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Text("Avelune", fontWeight = FontWeight.Bold, modifier = Modifier.padding(8.dp))
            screens.forEach { screen -> Button(onClick = { onSelect(screen.title) }, modifier = Modifier.fillMaxWidth().height(52.dp)) { Text(screen.title) } }
        }
    }
}
