# Choice Kingdom — Premium Android Adaptation Contract V1

Status: ACTIVE design constraint; not physical-device completion.

## Purpose

Define the Android adaptation rules that the premium UI must satisfy before P24/P25 can close. This contract is derived from current Android guidance and the project's Avelune visual system.

## Compact phone

- Preserve the authored vertical decision hierarchy.
- Keep primary actions at least 48dp touch-target size.
- Respect status/navigation/gesture insets.
- Never place a primary action under the gesture navigation region.
- Keep body copy readable and avoid uncontrolled horizontal stretching.

## Medium / foldable

- Reflow rather than simply scale the compact layout.
- Preserve the focal-art → narrative → decision hierarchy.
- Allow secondary information such as resource detail, relationship context or pending consequences to reveal into a second column/pane when space permits.
- Preserve the active event, selected choice and pending presentation state across resize/fold transitions.

## Expanded / tablet / desktop window

- Use a bounded content width instead of stretching cards across the entire display.
- Prefer list/detail or two-pane compositions for navigation-heavy screens.
- Keep decision controls close to the narrative they act upon.
- Preserve the same actions and semantic states as compact presentation.

## System UI and configuration changes

- Use safe insets for system bars, cutouts and gesture navigation.
- Treat rotation, fold/unfold, split-screen and freeform resize as supported state changes rather than exceptional failures.
- Preserve gameplay/session state; screen recreation must not reset a decision.
- Avoid animation assumptions tied to one aspect ratio.

## Accessibility baseline

- Interactive targets: minimum 48dp.
- Verify contrast for text and meaningful foreground content.
- Maintain visible keyboard/D-pad focus where applicable.
- Reduced-motion mode removes decorative movement without removing information.
- Large-text mode must preserve access to every primary action.

## QA gate

P24 remains open until this contract has physical/emulator evidence across representative compact, medium/foldable and expanded configurations. Static HTML/CSS or Python projection tests alone cannot close the gate.

## Sources

- Android layout basics: https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-basics
- Android orientation, aspect ratio and resizability: https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability
- Android system bars: https://developer.android.com/design/ui/mobile/guides/foundations/system-bars
- Android core app quality: https://developer.android.com/develop/adaptive-apps/quality-guidelines/core-app-quality
