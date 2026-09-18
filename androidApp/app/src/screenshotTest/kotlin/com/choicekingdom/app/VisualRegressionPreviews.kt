package com.choicekingdom.app

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

private val previewProjection = AndroidEventProjection(
    eventId = "E15",
    title = "The bell before dawn",
    turn = 15,
    choices = listOf(
        AndroidChoice("choice-a", "Open the gate", "Trust the messenger and let the dawn into Avelune."),
        AndroidChoice("choice-b", "Wait for proof", "Hold the line until the first light reveals the truth."),
        AndroidChoice("choice-c", "Send Mara", "Ask someone you trust to meet the stranger beyond the walls."),
    ),
    terminal = false,
)

@Composable
private fun PreviewShell(content: @Composable () -> Unit) {
    ChoiceKingdomTheme {
        Column(
            modifier = Modifier.padding(20.dp),
            verticalArrangement = Arrangement.spacedBy(14.dp),
        ) { content() }
    }
}

@Composable
fun VisualRegressionEventPreview() {
    PreviewShell {
        Text("AVELUNE", color = MaterialTheme.colorScheme.primary, fontSize = 12.sp, fontWeight = FontWeight.Bold)
        Text("The bell before dawn", style = MaterialTheme.typography.headlineMedium)
        Text("A decision arrives before the city wakes.", color = MaterialTheme.colorScheme.onSurfaceVariant)
        PreviewCard("EVENT", "A messenger waits beneath the eastern tower.")
    }
}

@Composable
fun VisualRegressionChoicePreview() {
    PreviewShell {
        Text("YOUR DECISION", color = MaterialTheme.colorScheme.secondary, fontSize = 12.sp, fontWeight = FontWeight.Bold)
        previewProjection.choices.forEach { choice ->
            PreviewCard(choice.label, choice.text)
        }
    }
}

@Composable
fun VisualRegressionEndingPreview() {
    PreviewShell {
        Text("ENDING", color = MaterialTheme.colorScheme.primary, fontSize = 12.sp, fontWeight = FontWeight.Bold)
        PreviewCard("Avelune remembers", "Your choices have left a mark on the kingdom.")
        Text("TURN 15 · E15", color = MaterialTheme.colorScheme.secondary, fontSize = 12.sp)
    }
}

@Composable
fun VisualRegressionNavigationPreview() {
    PreviewShell {
        Text("JOURNEY", style = MaterialTheme.typography.headlineSmall)
        PreviewCard("EVENT", "Current decision")
        PreviewCard("HISTORY", "What your choices changed")
        PreviewCard("PEOPLE", "Relationships and trust")
    }
}

@Composable
fun VisualRegressionSettingsPreview() {
    PreviewShell {
        Text("SETTINGS", style = MaterialTheme.typography.headlineSmall)
        PreviewCard("AUDIO", "Effects · Ambient · Music")
        PreviewCard("ACCESSIBILITY", "Large text · RTL · Reduced motion")
    }
}

@Composable
fun VisualRegressionLoadingPreview() {
    PreviewShell {
        Spacer(Modifier.height(160.dp))
        Text("AVELUNE", color = MaterialTheme.colorScheme.primary, fontSize = 12.sp, fontWeight = FontWeight.Bold)
        Text("Preparing your journey", style = MaterialTheme.typography.headlineSmall)
        Text("Loading the canonical story runtime.", color = MaterialTheme.colorScheme.onSurfaceVariant)
        Spacer(Modifier.height(160.dp))
    }
}

@Composable
private fun PreviewCard(title: String, body: String) {
    Card(
        modifier = Modifier.fillMaxWidth(),
        shape = RoundedCornerShape(24.dp),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceVariant),
    ) {
        Column(Modifier.padding(18.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Text(title, color = MaterialTheme.colorScheme.primary, fontWeight = FontWeight.Bold, fontSize = 12.sp)
            Text(body, color = MaterialTheme.colorScheme.onSurface, fontSize = 16.sp)
        }
    }
}
