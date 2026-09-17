# Block 15 — Cross-Screen Visual Regression

Status: **IN PROGRESS — 46%**

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


## Screenshot engine integration — 35%

- Compose screenshot testing engine 0.0.1-alpha16 is configured.
- The Android module now has a dedicated screenshotTest source set.
- Six deterministic visual surfaces are registered across compact, medium, and expanded widths.
- CI can generate approved references through an explicit manual approval input.
- Normal pushes and pull requests validate the committed references.
- Reference generation and validation follow the Android-documented Gradle tasks.

## Remaining

- Generate the first real reference-image set in CI.
- Review rendered references for unintended clipping or overflow.
- Expand coverage to all production surfaces and Core-8 locale variants.
- Keep physical device verification in Block 21.


## Baseline automation — 42%

- CI now detects whether approved PNG references exist.
- The first successful main-branch run will generate the initial reference set automatically and commit it through the GitHub Actions bot.
- Subsequent pushes and pull requests validate against the committed references.
- Manual `approve_baseline=true` remains available for intentional reference regeneration.
- This avoids treating a missing baseline as a passing regression test.


## CI execution hardening — 44%

- The repository does not contain a Gradle wrapper, so the screenshot workflow now provisions Gradle 8.9 explicitly instead of assuming `./gradlew` exists.
- A contract test prevents regression to a missing-wrapper invocation.
- The first completed screenshot workflow is still required before claiming reference PNG generation is verified.


## Host-rendering hardening — 46%

- Screenshot JVM heap is explicitly set to 4 GB for host-side rendering, matching Android's documented troubleshooting guidance for memory-intensive screenshot tests.
- The new contract test protects this setting.
- GitHub Actions runs for Block 15 are currently queued; no PNG baseline or validation result is counted until a run completes.
