# Block 9 — Android Runtime Closure

Status: **CLOSED — 100%**.

## Scope
- The Android launcher embeds the canonical Python GameSession through Chaquopy.
- Android sends only user intents (choose) and renders immutable presentation projections.
- Gameplay rules and mutation authority remain in the canonical Python runtime.
- Android-local resume persistence uses the canonical versioned SaveStore, including integrity checking and .bak recovery.
- The Android run identity is retained in SharedPreferences, so Activity recreation resumes the same canonical run instead of silently starting a new game.

## Verification
- tests/test_block9_android_runtime.py verifies first-run persistence, same-run resume, run-identity protection, and backup recovery.
- Existing Android runtime tests remain in the gate.
- The Block 9 GitHub Actions gate builds the debug APK and instrumentation APK, runs Android JVM tests, and verifies both artifacts.
- Physical device/emulator execution is intentionally not claimed here; it belongs to Block 21 Final Device QA.

## Boundary
Block 9 is complete when the Android application has a real canonical runtime seam, durable local resume behavior, and reproducible Android build/instrumentation artifacts. Localization, accessibility breadth, device matrix, performance, release signing and store work remain in their later blocks.