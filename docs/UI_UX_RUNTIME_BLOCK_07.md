# Block 7 — UI/UX Runtime

Status: ACTIVE

## Scope

Block 7 owns the real presentation runtime: primary surfaces, deterministic navigation, choice interaction states, terminal/disabled behavior, responsive composition, safe-area handling, semantics, and the Android-facing projection seam. Gameplay rules remain outside Android.

## Implemented in this checkpoint

- Android Compose application with Compact / Medium / Expanded layouts.
- Safe-drawing insets and minimum touch-target contracts.
- Seven primary surfaces: Event, Realm, History, People, Investigation, Ending, Settings.
- Immutable `AndroidPresentationPort` projection boundary.
- Deterministic UI-only state reducer covering focus, selection, press, resolving, resolved, blocked, error and terminal/disabled states.
- JVM tests covering navigation and all transient choice-state transitions.
- Existing instrumentation tests cover projection rendering, selection semantics and primary-surface navigation.

## Remaining gate

The launcher still uses an explicitly named development projection (`sampleProjection`) because the canonical runtime is Python and the repository does not yet contain a production Android runtime bridge that can execute `GameSession` directly on-device. Replacing that development source with the production runtime feed is required before Block 7 can honestly be marked 100%.

A source-level UI state machine does not substitute for the production session feed. No gameplay semantics are duplicated in Android.

## Verification rule

Block 7 reaches 100% only after:

1. production `GameSession` projection is consumed by Android;
2. every choice intent reaches the canonical runtime through the presentation seam;
3. navigation and all defined UI states remain deterministic;
4. JVM and Android instrumentation checks are green;
5. no development/sample projection remains in the production launch path.
