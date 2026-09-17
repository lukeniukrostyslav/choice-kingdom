# Block 15 — Cross-Screen Visual Regression

Status: **IN PROGRESS — 15%**

## Implemented

- Added a versioned visual-regression baseline manifest.
- Enumerated the production Compose surfaces that must be covered.
- Bound the baseline to the three responsive modes already defined by Block 12.
- Bound the baseline to Core-8 locales.
- Added a theme-token contract so visual baselines cannot silently drift from the production theme.
- Added a dedicated GitHub Actions contract gate.

## Important boundary

This is **not yet pixel-level screenshot validation**. No reference images are being invented or marked approved without actual rendered output.

The next implementation step is to introduce a supported Compose screenshot-test runner, generate real reference images, and validate diffs. Android's current documentation describes screenshot tests as rendered output compared against approved reference images and notes that the current AGP test-suite integration is experimental. citeturn0search0turn0search1

Physical-device visual verification remains Block 21.
