# Block 7 — UI/UX Runtime — Checkpoint 02

## Status
**65% — active, not closed.**

## Verified work in this checkpoint

- Choice selection state is now owned by the screen-level state holder instead of being independently stored inside every `ChoiceCard`.
- Selecting one choice now deterministically replaces the previous selected choice.
- Navigating to another primary surface clears the transient choice selection.
- `ChoiceCard` is now a state-rendering component: it receives `selected` and emits `onChoiceSelected` instead of owning gameplay-adjacent UI state.
- This follows Jetpack Compose state-hoisting guidance: state is kept at the lowest common owner that reads/writes it, while child composables receive immutable state and events.

## Existing Block 7 evidence

- Compact / Medium / Expanded layouts.
- Safe-drawing insets.
- Seven primary surfaces.
- Immutable Android presentation projection seam.
- Semantic interaction states and minimum touch targets.
- JVM and Android instrumentation coverage for existing UI behavior.
- Canonical Python `GameSessionPresentationBridge` with real-session projection tests exists on the runtime side.

## Remaining 35%

The Android production launch path still calls `sampleProjection()`. The canonical `GameSession` is Python-side. The repository therefore still lacks a production on-device runtime transport/embedding boundary that can consume the canonical session projection and send choice intents back without duplicating gameplay semantics.

Do **not** solve this by reimplementing the decision engine in Kotlin. The correct closure is a deliberate shared-runtime/embedding boundary compatible with the project's offline-first architecture.

## External verification reference

Android's current Compose guidance recommends hoisting UI state to the lowest common owner and exposing immutable state/events to child composables. Compose semantics are also the intended basis for accessibility-oriented UI testing. These principles were applied to this checkpoint.

## 100% exit gate

1. Production runtime projection reaches Android.
2. Android choice intent reaches canonical runtime.
3. `sampleProjection()` is absent from the production launch path.
4. Navigation and all defined interaction states remain deterministic.
5. JVM + Android instrumentation verification is green on the production path.
