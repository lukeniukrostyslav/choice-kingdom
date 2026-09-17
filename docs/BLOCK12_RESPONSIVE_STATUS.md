# Block 12 — Responsive / Safe Areas / Devices

Status: CLOSED — 100% at the defined source/integration boundary.

## Verified implementation

- The root Compose surface uses BoxWithConstraints, so layout decisions use the space actually allocated to the app rather than physical-device assumptions.
- Three responsive width modes are explicit: compact below 600dp, medium from 600dp to below 840dp, and expanded at 840dp and above.
- Expanded content is capped at 720dp but remains fillMaxWidth(), preventing fixed-width overflow on smaller expanded windows.
- Compact and medium layouts use full-width content with proportional horizontal spacing.
- Expanded layout uses a navigation rail and a centered content column.
- WindowInsets.safeDrawing is applied at the app root to protect content from system UI and display cutouts.
- Navigation callbacks use stable screen keys rather than localized titles, so responsive navigation remains correct across locales.
- The manifest keeps android:supportsRtl=true.

## Verification

The dedicated contract is tests/test_block12_responsive_contract.py.
The contract is source-level; physical phone/tablet/foldable and split-screen execution remains part of Block 21.

## Scope boundary

Block 12 closes the implementation/integration contract for responsive layout, safe drawing insets, and device-size adaptation. It does not claim physical-device visual QA, which is intentionally measured later.
