package com.choicekingdom.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
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
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
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
private data class AndroidScreenState(val title: String)
private val screens = listOf(
    AndroidScreenState("Event"), AndroidScreenState("Realm"), AndroidScreenState("History"),
    AndroidScreenState("People"), AndroidScreenState("Investigation"), AndroidScreenState("Ending"),
    AndroidScreenState("Settings"),
)

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { ChoiceKingdomApp() }
    }
}

@Composable
private fun ChoiceKingdomApp() {
    var selectedScreen by remember { mutableStateOf("Event") }
    val presentation = remember { AndroidPresentationPort.fromSnapshot(sampleProjection()) }
    ChoiceKingdomTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            BoxWithConstraints(modifier = Modifier.fillMaxSize().windowInsetsPadding(WindowInsets.safeDrawing)) {
                val mode = when {
                    maxWidth < 600.dp -> WindowMode.COMPACT
                    maxWidth < 840.dp -> WindowMode.MEDIUM
                    else -> WindowMode.EXPANDED
                }
                AdaptiveJourney(
                    mode = mode,
                    selectedScreen = screens.first { it.title == selectedScreen },
                    presentation = presentation,
                    onScreenSelected = { selectedScreen = it },
                )
            }
        }
    }
}

private fun sampleProjection(): AndroidEventProjection = AndroidEventProjection(
    eventId = "E01-A",
    title = "The First Choice",
    turn = 1,
    choices = listOf(
        AndroidChoice("E01-A-C1", "Approach", "Step toward the stranger.", "idle"),
        AndroidChoice("E01-A-C2", "Wait", "Watch before revealing your intent.", "idle"),
        AndroidChoice("E01-A-C3", "Leave", "Walk away while the road is clear.", "idle"),
    ),
    terminal = false,
)

@Composable
private fun AdaptiveJourney(
    mode: WindowMode,
    selectedScreen: AndroidScreenState,
    presentation: AndroidPresentationPort,
    onScreenSelected: (String) -> Unit,
) {
    val horizontal = when (mode) {
        WindowMode.COMPACT -> 16.dp
        WindowMode.MEDIUM -> 28.dp
        WindowMode.EXPANDED -> 48.dp
    }
    val titleSize = when (mode) {
        WindowMode.COMPACT -> 30.sp
        WindowMode.MEDIUM -> 36.sp
        WindowMode.EXPANDED -> 42.sp
    }
    if (mode == WindowMode.EXPANDED) {
        Row(
            modifier = Modifier.fillMaxSize().padding(horizontal = horizontal),
            horizontalArrangement = Arrangement.spacedBy(24.dp),
        ) {
            NavigationRailLike(onScreenSelected, Modifier.weight(0.34f))
            JourneyContent(selectedScreen, presentation, titleSize, Modifier.weight(0.66f))
        }
    } else {
        Column(modifier = Modifier.fillMaxSize()) {
            JourneyContent(
                selectedScreen,
                presentation,
                titleSize,
                Modifier.weight(1f).padding(horizontal = horizontal),
            )
            ScreenNavigation(onScreenSelected, Modifier.fillMaxWidth())
        }
    }
}

@Composable
private fun JourneyContent(
    screen: AndroidScreenState,
    presentation: AndroidPresentationPort,
    titleSize: TextUnit,
    modifier: Modifier,
) {
    val snapshot = presentation.snapshot()
    LazyColumn(
        modifier = modifier,
        contentPadding = PaddingValues(top = 24.dp, bottom = 28.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp),
    ) {
        item {
            Text("CHOICE KINGDOM · AVELUNE", color = MaterialTheme.colorScheme.primary, fontSize = 12.sp, fontWeight = FontWeight.Bold)
            Text(screen.title, color = MaterialTheme.colorScheme.onSurface, fontSize = titleSize, fontWeight = FontWeight.SemiBold)
            Text(snapshot.title, color = MaterialTheme.colorScheme.onSurface, fontSize = 20.sp, fontWeight = FontWeight.Medium)
            Text("Turn ${snapshot.turn} · ${snapshot.eventId}", color = MaterialTheme.colorScheme.secondary, fontSize = 14.sp)
        }
        if (screen.title == "Event") {
            item {
                Text(
                    if (snapshot.terminal) "Event complete" else "Choose your next action",
                    color = MaterialTheme.colorScheme.secondary,
                    fontSize = 14.sp,
                )
            }
            items(snapshot.choices, key = { it.id }) { choice ->
                ChoiceButton(choice)
            }
        }
    }
}

@Composable
private fun ChoiceButton(choice: AndroidChoice) {
    var selected by remember(choice.id) { mutableStateOf(choice.state == "selected") }
    val enabled = choice.state != "disabled"
    Button(
        onClick = { selected = true },
        enabled = enabled,
        modifier = Modifier.fillMaxWidth().heightIn(min = 56.dp).semantics {
            role = Role.Button
            contentDescription = "${choice.label}: ${choice.text}"
            stateDescription = if (selected) "Selected" else "Available"
        },
        colors = ButtonDefaults.buttonColors(
            containerColor = if (selected) MaterialTheme.colorScheme.surfaceVariant else MaterialTheme.colorScheme.surface,
        ),
    ) {
        Column(modifier = Modifier.fillMaxWidth()) {
            Text(choice.label, fontWeight = FontWeight.SemiBold)
            Text(choice.text, textAlign = TextAlign.Start, modifier = Modifier.fillMaxWidth(), fontSize = 14.sp)
        }
    }
}

@Composable
private fun ScreenNavigation(onSelect: (String) -> Unit, modifier: Modifier) {
    Row(modifier = modifier.padding(12.dp), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
        screens.take(4).forEach { screen ->
            Button(onClick = { onSelect(screen.title) }, modifier = Modifier.weight(1f).heightIn(min = 52.dp), contentPadding = PaddingValues(horizontal = 4.dp)) {
                Text(screen.title, fontSize = 11.sp, maxLines = 1)
            }
        }
    }
}

@Composable
private fun NavigationRailLike(onSelect: (String) -> Unit, modifier: Modifier) {
    Card(modifier = modifier.padding(vertical = 24.dp)) {
        Column(modifier = Modifier.padding(12.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Text("Avelune", fontWeight = FontWeight.Bold, modifier = Modifier.padding(8.dp))
            screens.forEach { screen ->
                Button(onClick = { onSelect(screen.title) }, modifier = Modifier.fillMaxWidth().heightIn(min = 52.dp)) {
                    Text(screen.title)
                }
            }
        }
    }
}
