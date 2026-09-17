package com.choicekingdom.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.animation.AnimatedContent
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.scaleIn
import androidx.compose.animation.togetherWith
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.safeDrawing
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.layout.widthIn
import androidx.compose.foundation.layout.windowInsetsPadding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.appcompat.app.AppCompatDelegate
import androidx.core.os.LocaleListCompat
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.ui.res.stringResource
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.semantics.LiveRegionMode
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.error
import androidx.compose.ui.semantics.heading
import androidx.compose.ui.semantics.liveRegion
import androidx.compose.ui.semantics.role
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.semantics.stateDescription
import androidx.compose.ui.hapticfeedback.HapticFeedbackType
import androidx.compose.ui.platform.LocalHapticFeedback
import androidx.compose.ui.platform.LocalView
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.TextUnit
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

private enum class WindowMode { COMPACT, MEDIUM, EXPANDED }
private data class AndroidScreenState(val key: String, val title: String, val subtitle: String)

@Composable
private fun localizedScreens() = listOf(
    AndroidScreenState("Event", stringResource(R.string.event), stringResource(R.string.event_subtitle)),
    AndroidScreenState("Realm", stringResource(R.string.realm), stringResource(R.string.realm_subtitle)),
    AndroidScreenState("History", stringResource(R.string.history), stringResource(R.string.history_subtitle)),
    AndroidScreenState("People", stringResource(R.string.people), stringResource(R.string.people_subtitle)),
    AndroidScreenState("Investigation", stringResource(R.string.investigation), stringResource(R.string.investigation_subtitle)),
    AndroidScreenState("Ending", stringResource(R.string.ending), stringResource(R.string.ending_subtitle)),
    AndroidScreenState("Settings", stringResource(R.string.settings), stringResource(R.string.settings_subtitle)),
)

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { ChoiceKingdomApp() }
    }
}

@Composable
private fun ChoiceKingdomApp() {
    val screens = localizedScreens()
    var selectedScreen by rememberSaveable { mutableStateOf("Event") }
    var selectedChoiceId by remember { mutableStateOf<String?>(null) }
    var resolvingChoiceId by remember { mutableStateOf<String?>(null) }
    var projection by remember { mutableStateOf<AndroidEventProjection?>(null) }
    var errorMessage by remember { mutableStateOf<String?>(null) }
    val context = androidx.compose.ui.platform.LocalContext.current
    val runtime = remember(context) { CanonicalAndroidRuntime(context) }

    DisposableEffect(runtime) {
        runtime.start(
            runId = "android-production-${System.currentTimeMillis()}",
            onProjection = {
                projection = it
                selectedChoiceId = null
                resolvingChoiceId = null
                errorMessage = null
            },
            onError = {
                resolvingChoiceId = null
                errorMessage = it.message ?: it.javaClass.simpleName
            },
        )
        onDispose { runtime.close() }
    }

    ChoiceKingdomTheme {
        Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
            BoxWithConstraints(
                modifier = Modifier
                    .fillMaxSize()
                    .windowInsetsPadding(WindowInsets.safeDrawing),
            ) {
                val mode = when {
                    maxWidth < 600.dp -> WindowMode.COMPACT
                    maxWidth < 840.dp -> WindowMode.MEDIUM
                    else -> WindowMode.EXPANDED
                }
                if (projection == null) {
                    LoadingScreen(errorMessage)
                } else {
                    AdaptiveJourney(
                        mode = mode,
                        selectedScreen = screens.first { it.key == selectedScreen },
                        snapshot = projection!!,
                        selectedChoiceId = selectedChoiceId,
                        resolvingChoiceId = resolvingChoiceId,
                        errorMessage = errorMessage,
                        onScreenSelected = {
                            selectedScreen = it.key
                            selectedChoiceId = null
                            resolvingChoiceId = null
                            errorMessage = null
                        },
                        onChoiceSelected = { choiceId ->
                            if (resolvingChoiceId == null) {
                                selectedChoiceId = choiceId
                                resolvingChoiceId = choiceId
                                runtime.choose(
                                    choiceId = choiceId,
                                    onProjection = {
                                        projection = it
                                        selectedChoiceId = null
                                        resolvingChoiceId = null
                                        errorMessage = null
                                    },
                                    onError = {
                                        resolvingChoiceId = null
                                        errorMessage = it.message ?: it.javaClass.simpleName
                                    },
                                )
                            }
                        },
                    )
                }
            }
        }
    }
}

@Composable
private fun LoadingScreen(errorMessage: String?) {
    Column(
        modifier = Modifier.fillMaxSize().padding(24.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally,
    ) {
        Text(stringResource(R.string.avelune), color = MaterialTheme.colorScheme.primary, fontSize = 12.sp, fontWeight = FontWeight.Bold)
        Text(stringResource(R.string.preparing_journey), fontSize = 28.sp, fontWeight = FontWeight.SemiBold)
        Text(
            errorMessage ?: stringResource(R.string.starting_runtime),
            modifier = Modifier.padding(top = 10.dp),
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            textAlign = TextAlign.Center,
        )
    }
}

@Composable
private fun AdaptiveJourney(
    mode: WindowMode,
    selectedScreen: AndroidScreenState,
    snapshot: AndroidEventProjection,
    selectedChoiceId: String?,
    resolvingChoiceId: String?,
    errorMessage: String?,
    onScreenSelected: (String) -> Unit,
    onChoiceSelected: (String) -> Unit,
) {
    val horizontal = when (mode) {
        WindowMode.COMPACT -> 16.dp
        WindowMode.MEDIUM -> 28.dp
        WindowMode.EXPANDED -> 40.dp
    }
    val contentWidth = when (mode) {
        WindowMode.COMPACT -> Modifier.fillMaxWidth()
        WindowMode.MEDIUM -> Modifier.fillMaxWidth().padding(horizontal = 4.dp)
        WindowMode.EXPANDED -> Modifier.fillMaxWidth().widthIn(max = 720.dp)
    }
    val titleSize = when (mode) {
        WindowMode.COMPACT -> 30.sp
        WindowMode.MEDIUM -> 36.sp
        WindowMode.EXPANDED -> 42.sp
    }
    if (mode == WindowMode.EXPANDED) {
        Row(
            modifier = Modifier.fillMaxSize().padding(horizontal = horizontal),
            horizontalArrangement = Arrangement.spacedBy(28.dp),
        ) {
            NavigationRail(screens = localizedScreens(), onSelect = onScreenSelected, modifier = Modifier.width(220.dp))
            Box(modifier = Modifier.fillMaxWidth(), contentAlignment = Alignment.TopCenter) {
                TransitionedJourneyContent(selectedScreen, snapshot, selectedChoiceId, resolvingChoiceId, errorMessage, titleSize, contentWidth, onChoiceSelected)
            }
        }
    } else {
        Column(modifier = Modifier.fillMaxSize()) {
            TransitionedJourneyContent(
                selectedScreen,
                snapshot,
                selectedChoiceId,
                resolvingChoiceId,
                errorMessage,
                titleSize,
                Modifier.weight(1f).padding(horizontal = horizontal),
                onChoiceSelected,
            )
            ScreenNavigation(screens = localizedScreens(), onSelect = onScreenSelected, modifier = Modifier.fillMaxWidth())
        }
    }
}

@Composable
private fun TransitionedJourneyContent(
    screen: AndroidScreenState,
    snapshot: AndroidEventProjection,
    selectedChoiceId: String?,
    resolvingChoiceId: String?,
    errorMessage: String?,
    titleSize: TextUnit,
    modifier: Modifier,
    onChoiceSelected: (String) -> Unit,
) {
    AnimatedContent(
        targetState = screen.key,
        transitionSpec = {
            (fadeIn() + scaleIn(initialScale = 0.98f)).togetherWith(fadeOut())
        },
        label = "journey-screen-transition",
    ) {
        JourneyContent(
            screen = screen,
            snapshot = snapshot,
            selectedChoiceId = selectedChoiceId,
            resolvingChoiceId = resolvingChoiceId,
            errorMessage = errorMessage,
            titleSize = titleSize,
            modifier = modifier,
            onChoiceSelected = onChoiceSelected,
        )
    }
}

@Composable
private fun JourneyContent(
    screen: AndroidScreenState,
    snapshot: AndroidEventProjection,
    selectedChoiceId: String?,
    resolvingChoiceId: String?,
    errorMessage: String?,
    titleSize: TextUnit,
    modifier: Modifier,
    onChoiceSelected: (String) -> Unit,
) {
    LazyColumn(
        modifier = modifier,
        contentPadding = PaddingValues(top = 18.dp, bottom = 32.dp),
        verticalArrangement = Arrangement.spacedBy(14.dp),
    ) {
        item { Header(snapshot.turn, titleSize) }
        item { HeroCard(screen, snapshot) }
        if (errorMessage != null) item { ErrorCard(errorMessage) }
        when (screen.key) {
            "Event" -> {
                item { SectionLabel("YOUR DECISION") }
                items(snapshot.choices, key = { it.id }) { choice ->
                    ChoiceCard(
                        choice = choice,
                        selected = selectedChoiceId == choice.id,
                        resolving = resolvingChoiceId == choice.id,
                        disabledByResolution = resolvingChoiceId != null && resolvingChoiceId != choice.id,
                        onChoiceSelected = onChoiceSelected,
                    )
                }
            }
            "Realm" -> item { InfoGrid(listOf(stringResource(R.string.gold) to "120", stringResource(R.string.trust) to "64", stringResource(R.string.security) to "51", stringResource(R.string.power) to "43")) }
            "History" -> item { TimelineCard(snapshot.eventId, stringResource(R.string.journey_continues), stringResource(R.string.turn_event_format, snapshot.turn, snapshot.title)) }
            "People" -> item { InfoGrid(listOf("Mara" to stringResource(R.string.known), "Rowan" to stringResource(R.string.unknown), "Seris" to "Unknown", "Ivo" to "Unknown")) }
            "Investigation" -> item { TimelineCard(stringResource(R.string.thread_01), stringResource(R.string.thread_title), stringResource(R.string.thread_detail)) }
            "Ending" -> item { EndingCard(snapshot.terminal) }
            "Settings" -> item { SettingsCard() }
        }
    }
}

@Composable
private fun Header(turn: Int, titleSize: TextUnit) {
    Column(verticalArrangement = Arrangement.spacedBy(4.dp)) {
        Text(stringResource(R.string.brand_line), color = MaterialTheme.colorScheme.primary, fontSize = 12.sp, fontWeight = FontWeight.Bold)
        Row(verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            Text(stringResource(R.string.turn_format, turn), color = MaterialTheme.colorScheme.secondary, fontSize = 13.sp)
            Box(modifier = Modifier.size(4.dp).background(MaterialTheme.colorScheme.outline, RoundedCornerShape(50)))
            Text(stringResource(R.string.offline_journey), color = MaterialTheme.colorScheme.secondary, fontSize = 13.sp, fontWeight = FontWeight.Medium)
        }
        Text(
            stringResource(R.string.avelune),
            color = MaterialTheme.colorScheme.onBackground,
            fontSize = titleSize,
            fontWeight = FontWeight.SemiBold,
            modifier = Modifier.semantics { heading() },
        )
    }
}

@Composable
private fun HeroCard(screen: AndroidScreenState, snapshot: AndroidEventProjection) {
    Card(
        modifier = Modifier.fillMaxWidth(),
        shape = RoundedCornerShape(28.dp),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceVariant),
        border = BorderStroke(1.dp, MaterialTheme.colorScheme.outlineVariant),
    ) {
        Column(modifier = Modifier.padding(22.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
            Text(screen.title.uppercase(), color = MaterialTheme.colorScheme.primary, fontSize = 11.sp, fontWeight = FontWeight.Bold)
            Text(snapshot.title, color = MaterialTheme.colorScheme.onSurface, fontSize = 25.sp, fontWeight = FontWeight.SemiBold)
            Text(screen.subtitle, color = MaterialTheme.colorScheme.onSurfaceVariant, fontSize = 15.sp, lineHeight = 22.sp)
            Text(stringResource(R.string.turn_event_format, snapshot.eventId, snapshot.turn), color = MaterialTheme.colorScheme.secondary, fontSize = 12.sp)
        }
    }
}

@Composable
private fun SectionLabel(text: String) {
    Text(
        text,
        color = MaterialTheme.colorScheme.secondary,
        fontSize = 11.sp,
        fontWeight = FontWeight.Bold,
        modifier = Modifier.padding(horizontal = 4.dp).semantics { heading() },
    )
}

@Composable
private fun ErrorCard(message: String) {
    TimelineCard(
        stringResource(R.string.runtime_error),
        stringResource(R.string.journey_safe),
        message,
        modifier = Modifier.semantics {
            liveRegion = LiveRegionMode.Polite
            error(message)
        },
    )
}

@Composable
private fun ChoiceCard(
    choice: AndroidChoice,
    selected: Boolean,
    resolving: Boolean,
    disabledByResolution: Boolean,
    onChoiceSelected: (String) -> Unit,
) {
    val haptics = LocalHapticFeedback.current
    val view = LocalView.current
    val enabled = choice.state != "disabled" && !disabledByResolution && !resolving
    val state = when {
        resolving -> stringResource(R.string.resolving)
        selected -> stringResource(R.string.selected)
        !enabled -> stringResource(R.string.blocked)
        else -> stringResource(R.string.available)
    }
    Button(
        onClick = {
            haptics.performHapticFeedback(HapticFeedbackType.LongPress)
            view.playSoundEffect(android.view.SoundEffectConstants.CLICK)
            onChoiceSelected(choice.id)
        },
        enabled = enabled,
        modifier = Modifier
            .fillMaxWidth()
            .heightIn(min = 78.dp)
            .semantics {
                role = Role.Button
                contentDescription = "${choice.label}: ${choice.text}"
                stateDescription = state
            },
        shape = RoundedCornerShape(22.dp),
        border = BorderStroke(1.dp, if (selected || resolving) MaterialTheme.colorScheme.primary else MaterialTheme.colorScheme.outlineVariant),
        colors = ButtonDefaults.buttonColors(
            containerColor = if (selected || resolving) MaterialTheme.colorScheme.primaryContainer else MaterialTheme.colorScheme.surface,
            contentColor = MaterialTheme.colorScheme.onSurface,
            disabledContainerColor = MaterialTheme.colorScheme.surfaceVariant,
        ),
        contentPadding = PaddingValues(horizontal = 20.dp, vertical = 14.dp),
    ) {
        Column(modifier = Modifier.fillMaxWidth(), verticalArrangement = Arrangement.spacedBy(4.dp)) {
            Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween, verticalAlignment = Alignment.CenterVertically) {
                Text(choice.label, fontWeight = FontWeight.SemiBold, fontSize = 16.sp)
                Text(state.uppercase(), fontSize = 10.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.primary)
            }
            Text(choice.text, textAlign = TextAlign.Start, modifier = Modifier.fillMaxWidth(), fontSize = 14.sp, lineHeight = 20.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
        }
    }
}

@Composable
private fun InfoGrid(items: List<Pair<String, String>>) {
    Column(verticalArrangement = Arrangement.spacedBy(10.dp)) {
        items.chunked(2).forEach { rowItems ->
            Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                rowItems.forEach { (label, value) ->
                    Card(modifier = Modifier.weight(1f), shape = RoundedCornerShape(20.dp), border = BorderStroke(1.dp, MaterialTheme.colorScheme.outlineVariant)) {
                        Column(modifier = Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(6.dp)) {
                            Text(label, fontSize = 12.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
                            Text(value, fontSize = 20.sp, fontWeight = FontWeight.SemiBold)
                        }
                    }
                }
                if (rowItems.size == 1) Spacer(Modifier.weight(1f))
            }
        }
    }
}

@Composable
private fun TimelineCard(kicker: String, title: String, detail: String, modifier: Modifier = Modifier) {
    Card(modifier = modifier.fillMaxWidth(), shape = RoundedCornerShape(22.dp), border = BorderStroke(1.dp, MaterialTheme.colorScheme.outlineVariant)) {
        Column(modifier = Modifier.padding(20.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Text(kicker, fontSize = 10.sp, fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.primary)
            Text(title, fontSize = 19.sp, fontWeight = FontWeight.SemiBold)
            Text(detail, fontSize = 14.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
        }
    }
}

@Composable
private fun EndingCard(terminal: Boolean) {
    TimelineCard(if (terminal) "RESOLVED" else "IN PROGRESS", if (terminal) stringResource(R.string.journey_ended) else stringResource(R.string.ending_ahead), stringResource(R.string.ending_state))
}

@Composable
private fun SettingsCard() {
    Card(modifier = Modifier.fillMaxWidth(), shape = RoundedCornerShape(22.dp), border = BorderStroke(1.dp, MaterialTheme.colorScheme.outlineVariant)) {
        Column(modifier = Modifier.padding(18.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Text(stringResource(R.string.presentation_preferences), fontSize = 18.sp, fontWeight = FontWeight.SemiBold)
            Text(stringResource(R.string.settings_description), fontSize = 14.sp, color = MaterialTheme.colorScheme.onSurfaceVariant, lineHeight = 21.sp)
            TextButton(onClick = { AppCompatDelegate.setApplicationLocales(LocaleListCompat.forLanguageTags("en")) }, modifier = Modifier.heightIn(min = 48.dp)) { Text("English") }
            TextButton(onClick = { AppCompatDelegate.setApplicationLocales(LocaleListCompat.forLanguageTags("it")) }, modifier = Modifier.heightIn(min = 48.dp)) { Text("Italiano") }
            TextButton(onClick = { AppCompatDelegate.setApplicationLocales(LocaleListCompat.forLanguageTags("uk")) }, modifier = Modifier.heightIn(min = 48.dp)) { Text("Українська") }
            TextButton(onClick = { AppCompatDelegate.setApplicationLocales(LocaleListCompat.forLanguageTags("ru")) }, modifier = Modifier.heightIn(min = 48.dp)) { Text("Русский") }
            
        }
    }
}

@Composable
private fun ScreenNavigation(screens: List<AndroidScreenState>, onSelect: (String) -> Unit, modifier: Modifier) {
    Row(
        modifier = modifier.horizontalScroll(rememberScrollState()).padding(horizontal = 12.dp, vertical = 10.dp),
        horizontalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        screens.forEach { screen ->
            Button(
                onClick = { onSelect(screen.key) },
                modifier = Modifier
                    .heightIn(min = 52.dp)
                    .semantics {
                        role = Role.Button
                        contentDescription = screen.title
                    },
                contentPadding = PaddingValues(horizontal = 14.dp),
            ) {
                Text(screen.title, fontSize = 12.sp)
            }
        }
    }
}

@Composable
private fun NavigationRail(screens: List<AndroidScreenState>, onSelect: (String) -> Unit, modifier: Modifier) {
    Card(modifier = modifier.padding(vertical = 18.dp), shape = RoundedCornerShape(26.dp), border = BorderStroke(1.dp, MaterialTheme.colorScheme.outlineVariant)) {
        Column(modifier = Modifier.padding(12.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Text(stringResource(R.string.avelune), fontSize = 20.sp, fontWeight = FontWeight.Bold, modifier = Modifier.padding(10.dp))
            screens.forEach { screen ->
                TextButton(
                    onClick = { onSelect(screen.key) },
                    modifier = Modifier
                        .fillMaxWidth()
                        .heightIn(min = 52.dp)
                        .semantics {
                            role = Role.Button
                            contentDescription = screen.title
                        },
                ) {
                    Text(screen.title, modifier = Modifier.fillMaxWidth())
                }
            }
        }
    }
}
