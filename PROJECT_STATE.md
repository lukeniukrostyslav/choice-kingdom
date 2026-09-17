# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Android-first, one-time purchase target €2.99–€4.99, no ads/subscription/mandatory backend for core gameplay, 20+ locales including RTL. Frozen production catalog: **E01–E272**.

## Current phase
**Blocks 1–6 are closed at their defined boundaries. Block 7 UI/UX Runtime is the active workstream.** The project proceeds strictly block-by-block. Percentages reflect implementation and available verification evidence, not documentation volume.

## Approved General Plan — 25 Blocks
1. **Production Data Schema** → 100%
2. **Decision Engine / Application Runtime** → 100%
3. **Real Reachability / Causal Graph QA** → 100%
4. **Production Content E01–E272** → 100%
5. **Persistence / Save / Load / Resume** → 100%
6. **Real GameSession → Presentation Bridge** → 100%
7. **UI/UX Runtime** → 55%
8. **All Gameplay States** → 0%
9. **Android Runtime** → 0%
10. **Localization 20+** → 0%
11. **RTL / Large Text / Accessibility** → 0%
12. **Responsive / Safe Areas / Devices** → 0%
13. **Premium Design P1–P25** → 62.24%
14. **Motion / Audio / Haptics** → 0%
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

## Block 7 checkpoint
- Android Compose presentation shell exists with Compact / Medium / Expanded layouts.
- Seven primary surfaces are represented: Event, Realm, History, People, Investigation, Ending, Settings.
- Safe-drawing insets, semantic choice interaction and minimum touch-target behavior are implemented.
- Immutable `AndroidPresentationPort` is the Android-facing projection seam.
- New deterministic UI-only reducer covers navigation and focus/selection/press/resolving/resolved/blocked/error/terminal states.
- JVM tests cover the reducer's complete transient choice-state lifecycle and all primary surfaces.
- Existing Android instrumentation covers projection rendering, accessible selection and navigation.
- `docs/UI_UX_RUNTIME_BLOCK_07.md` records the remaining closure gate.

## Remaining Block 7 gate
The production launcher still consumes an explicitly named development `sampleProjection`. The canonical `GameSession` is Python-side; a production Android runtime feed/adapter is not yet present. Therefore Block 7 is **55%**, not 100%. The remaining work is to connect the real runtime projection and choice intents without duplicating gameplay semantics in Android, then run the applicable JVM and Android instrumentation verification.

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
- UI / UX Runtime Implementation: **55%**
- Localization 20+ / RTL: **11%**
- Android Implementation: **8%**
- Runtime / Android QA: **28%**
- APK / AAB: **0%**
- Release / Store: **0%**

## Premium Design P1–P25
Canonical percentages are tracked in `docs/PREMIUM_DESIGN_MASTER_P1_P25.md`. Current aggregate: **62.24%**. P24 remains incomplete without physical device proof.

## Honest progress rule
Documentation never makes implementation complete. Every percentage requires authoritative evidence and applicable verification. Source/contract GREEN must never be reported as runtime gameplay GREEN. Owner-controlled physical Android QA, production signing and store publication remain open until actually performed.
