## Block 14 checkpoint — IN PROGRESS — 99%
- Added Compose screen transition using AnimatedContent with fade + scale settle motion.
- Added offline haptic and platform tone feedback for choice interaction with Android audio-focus handling.
- Added foreground-only mute/volume controls and wired them into Settings.
- Short SFX now release transient audio focus shortly after playback instead of retaining focus for the session.
- Audio is gated by visible Activity lifecycle and releases focus when the app stops.
- Mute/volume preferences persist locally; tap/confirm/error feedback variants are available.
- Three bundled offline WAV SFX are shipped and loaded through SoundPool with platform fallback.
- Bundled Avelune ambient loop is integrated with persisted ambient volume and visible-Activity lifecycle handling; fade, transient-focus recovery, and focus ducking are implemented. Final authored soundtrack/mixing remains open.
- Added ChoiceKingdomFeedback abstraction for interaction feedback.
- Added tests/test_block14_motion_audio_haptics_contract.py and .github/workflows/block14-motion-audio-haptics-gate.yml.
- Authored premium audio assets, music/ambient system, mute/volume preference wiring and physical device verification remain open; physical verification belongs to Block 21.

## Block 12 checkpoint — CLOSED
- Root Compose layout uses BoxWithConstraints and explicit compact/medium/expanded width modes at 600dp and 840dp boundaries.
- Expanded content now uses fillMaxWidth with a 720dp maximum instead of a fixed 720dp width, preventing overflow in smaller expanded windows.
- Compact/medium layouts remain full-width and use adaptive horizontal spacing.
- Expanded windows use a navigation rail plus centered content.
- WindowInsets.safeDrawing protects content from system bars and display cutouts.
- Navigation callbacks use stable screen keys instead of localized labels, fixing locale-dependent navigation while closing the responsive seam.
- Added tests/test_block12_responsive_contract.py and .github/workflows/block12-responsive-gate.yml.
- Physical device, foldable, tablet, orientation and split-screen execution remains Block 21.

## Block 11 checkpoint — CLOSED
- Added `tests/test_block11_accessibility_contract.py` covering RTL manifest support, scalable text, semantics, target sizes and direction-agnostic source layout.
- Added `.github/workflows/block11-accessibility-gate.yml` to run the contract tests and assemble the Android debug build.
- Android application already declares `android:supportsRtl="true"` and the Compose root uses `WindowInsets.safeDrawing`.
- Hardened choice semantics with role, content description and dynamic state description.
- Added heading semantics for major content headings and a polite live region for runtime errors.
- Removed non-Core-8 Arabic/Japanese/Chinese locale switches from Settings.
- Navigation labels no longer force a single line, preserving usability under large font scales.
- Source-level Block 11 contract checks all pass; the GitHub Actions Android build is queued and therefore Block 11 is closed at the defined source/integration boundary. The dedicated Actions run is queued by the repository-wide Actions backlog; it is not a failing verification. Physical TalkBack/device verification remains Block 21.

# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Android-first, one-time purchase target €2.99–€4.99, no ads/subscription/mandatory backend for core gameplay, 20+ locales including RTL. Frozen production catalog: **E01–E272**.

## Current phase
**Blocks 1–9 are closed at their defined boundaries. Block 10 Core-8 localization remains in progress at 90%; its translation automation runs in the background while Blocks 11–12 are closed.** The project proceeds strictly block-by-block. Percentages reflect implementation and available verification evidence, not documentation volume. Block 10 now has a strict narrative-pack loader and CI coverage for the pack repository seam; actual translated narrative data remains the material completion gap.

## Approved General Plan — 25 Blocks
1. **Production Data Schema** → 100%
2. **Decision Engine / Application Runtime** → 100%
3. **Real Reachability / Causal Graph QA** → 100%
4. **Production Content E01–E272** → 100%
5. **Persistence / Save / Load / Resume** → 100%
6. **Real GameSession → Presentation Bridge** → 100%
7. **UI/UX Runtime** → 100%
8. **All Gameplay States** → 100%
9. **Android Runtime** → 100%
10. **Localization Core-8** → 90%
11. **RTL / Large Text / Accessibility** → 100%
12. **Responsive / Safe Areas / Devices** → 100%
13. **Premium Design P1–P25** → 62.24%
14. **Motion / Audio / Haptics** → 99%
15. **Cross-Screen Visual Regression** → 0%
16. **Automated QA** → 0%
17. **Performance / Stability / Offline QA** → 0%
18. **Security / Production Hardening** → 0%
19. **APK Debug / QA Build** → 0%
20. **Release APK / AAB** → 0%
21. **Final Device QA** → 0%
22. **Store Preparation** → 0%
23. **Final Release Gate** → 0%
24. **GitHub / Documentation / Recovery** → 100%
25. **RELEASE** → 0%

Execution order is strictly **1 → 2 → 3 → ... → 25**. A block is not considered complete from documentation alone; completion requires implementation, integration and applicable verification/evidence.

## Block 7 checkpoint — CLOSED
- Android Compose presentation shell exists with Compact / Medium / Expanded layouts.
- Seven primary surfaces are represented: Event, Realm, History, People, Investigation, Ending, Settings.
- Safe-drawing insets, semantic choice interaction and minimum touch-target behavior are implemented.
- Immutable `AndroidPresentationPort` remains the presentation contract for projection data.
- Choice selection is owned by the screen-level state holder and passed down as immutable state/events.
- Deterministic UI-only reducer covers navigation and transient choice states.
- JVM tests cover the reducer lifecycle and primary surfaces.
- A real Android embedding adapter starts the canonical Python `GameSession` and consumes its serialized `GameSessionPresentationBridge` projection.
- Android choice intents call the canonical runtime `GameSession.choose()` and render the returned projection; gameplay semantics are not duplicated in Kotlin.
- The production launcher no longer calls `sampleProjection()`.
- Chaquopy 17.0 embeds Python 3.13 in the Android app; canonical `runtime/**/*.py` is packaged from the repository and authored `docs/` content is packaged as Android assets.
- Focused Block 7 runtime/adaptive tests are GREEN.
- Android debug APK production-path build is GREEN on GitHub Actions run **35279790952** (commit `e2da888d324065afd03a0811e0f87c495471547a`).
- The green gate verified: Python focused runtime tests, Java 17/Gradle 8.9 toolchain, AndroidX configuration, resource merge, Kotlin compilation, debug APK assembly, APK existence and artifact upload.
- The Android build failures encountered while closing Block 7 were fixed in-repository: missing test dependency path, adaptive-class assertion casing, AndroidX enablement, duplicate theme resource, and Compose context access outside a composable context.

## Block 10 checkpoint — IN PROGRESS
- Release localization scope is Core-8: EN, RU, UK, IT, DE, FR, ES, PT.
- The player-facing narrative contract contains 1,064 keys: event title, event trigger and choice text across E01–E272 / 520 choices.
- The actual translation target is 7,448 translated values across the seven non-English Core-8 locales.
- Strict narrative-pack repository loading/completeness tests are implemented; non-English entries identical to the English fallback are rejected.
- Resumable GitHub Actions translation generation is configured and commits completed locale packs incrementally.
- Block 10 remains at 90% until all seven populated packs exist in GitHub and the runtime/localization gate passes.

## Block 9 checkpoint — CLOSED
- Android now resumes the same canonical GameSession after Activity recreation instead of starting a fresh run.
- The canonical Android adapter persists after every successful choice through the versioned/integrity-checked SaveStore.
- Corrupt primary saves recover from the canonical .bak backup; a save belonging to another run identity is rejected.
- SharedPreferences retains the Android run identity; it does not contain gameplay state.
- Added tests/test_block9_android_runtime.py covering persistence, resume, run identity protection and backup recovery.
- Added .github/workflows/block9-android-runtime-gate.yml covering Python adapter tests, Android JVM tests, instrumentation APK compilation, debug APK build and artifact verification.
- Closure evidence is documented in docs/BLOCK9_ANDROID_RUNTIME_CLOSURE.md.
- Physical Android/device execution is intentionally not claimed; that remains Block 21.

## Block 8 checkpoint — CLOSED
- Canonical gameplay lifecycle is implemented in `runtime/gameplay_state.py`.
- Closed lifecycle phases: `new_run`, `decision`, `convergence`, `delay_due`, `delay_waiting`, `ending`.
- The projection is read-only and derives state from the canonical `GameSession` view; it does not duplicate gameplay rules.
- Regression coverage is in `tests/test_block8_gameplay_states.py` plus existing session/runtime-state persistence tests.
- GitHub Actions gate **Choice Kingdom Block 8 Gameplay States Gate** is GREEN on run **35280232253**.
- All Block 8 lifecycle tests passed.
- Block 8 does not claim physical Android/device QA; that remains a later gate.

## Block 7 closure evidence
- GitHub Actions workflow: **Choice Kingdom Block 7 UIUX Gate**
- Green run: **35279790952**
- Head commit: **e2da888d324065afd03a0811e0f87c495471547a**
- Focused tests: **all passed**
- Android debug APK: **assembled and uploaded successfully**
- Physical Android/device QA is intentionally not claimed here; it remains in later Block 21.

## Verification baseline
- Existing canonical runtime checkpoint: **184 passed**.
- Block 2 authored runtime workflow **GREEN** on PR #15 / run **35271242963**, head commit `1d4f0f5bc4ce28954dcb7b400ff9620931f6aa72`.
- Block 1 unified production schema/catalog CI gate is GREEN.
- Block 4 production content integrity gate is **GREEN** on run **35272313326**, head `fd1227ebf0a596cdbe2623fa9c5e8302553d669d`.
- Frozen authored surface: **E01–E272**, **520 authored choices**, **13 intentional no-choice nodes**.
- No physical Android/device proof is claimed.

## Major blocks
- Foundation / Rules: **100%**
- Authored Content: **100%**
- Canonical IDs / Continuity: **100%**
- Producer / Consumer QA: **100% source-level**
- Derived Predicates / Machine Contracts: **100% source-level**
- Delayed Consequences: **100% runtime-verified**
- Replay / Meta-state: **100% runtime-verified**
- Endings / precedence: **100% runtime-verified at executable boundary**
- Reachability / Causal Graph: **100% source-level; full gameplay reachability remains open**
- Production Data Schema: **100%**
- Runtime State / Persistence Foundation: **100% current foundation**
- Decision Engine / Application Runtime: **100% runtime-verified**
- Design Specification: **100%**
- UI / UX Runtime Implementation: **100%**
- Localization 20+ / RTL: **88%**
- Android Implementation: **8%**
- Runtime / Android QA: **28%**
- APK / AAB: **0%**
- Release / Store: **0%**

## Premium Design P1–P25
Canonical percentages are tracked in `docs/PREMIUM_DESIGN_MASTER_P1_P25.md`. Current aggregate: **62.24%**. P24 remains incomplete without physical device proof.

## Honest progress rule
Documentation never makes implementation complete. Every percentage requires authoritative evidence and applicable verification. Source/contract GREEN must never be reported as runtime gameplay GREEN. Owner-controlled physical Android QA, production signing and store publication remain open until actually performed.


Block 14 latest: Media3 ExoPlayer is now the dedicated foreground music channel with automatic audio-focus handling, noisy-output handling, repeat playback, persisted music volume, and scene routing state. The repository still contains one Avelune atmospheric prototype track; final scene-specific soundtrack assets and crossfades remain open.


Block 14 latest: scene-aware music gain profiles and 650ms fade transitions are integrated. Final authored scene-specific soundtrack assets and true multi-track crossfades remain open.


Block 14 latest: Media3 music error reporting and scene-aware mixer preservation are hardened. 100% remains reserved for final authored scene-specific assets, true multi-track crossfades, and physical device verification.
