# Block 11 — RTL / Large Text / Accessibility

Status: CLOSED — 100% at the source/integration contract boundary.

## Verified implementation

- Android application declares android:supportsRtl="true".
- The main Compose surface consumes WindowInsets.safeDrawing.
- Player-facing text uses scalable sp sizing rather than dp font dimensions.
- Navigation text is allowed to wrap instead of forcing a single line.
- Interactive targets have explicit minimum heights of 48dp or greater.
- Choice controls expose role, dynamic state description and a complete content description to accessibility services.
- Screen navigation controls expose button semantics and localized labels.
- Major screen headings are marked with Compose heading() semantics.
- Runtime error feedback is exposed as a polite accessibility live region.
- Layout code avoids hard-coded left/right positioning and uses start-aligned text where directional alignment matters.
- Non-core locale buttons previously left in Settings (Arabic/Japanese/Chinese) were removed so Block 11 does not silently expand or contradict the Core-8 release localization contract.

## Verification

The Block 11 contract test is tests/test_block11_accessibility_contract.py.
Android compilation remains covered by the repository Android gates; physical TalkBack/device verification is intentionally deferred to Block 21.

## Scope boundary

Block 11 closes the source/integration accessibility contract. Physical-device TalkBack verification, visual regression across font-scale settings, and device matrix testing remain later release gates and are not falsely counted here.
