# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Android-first, one-time purchase target €2.99–€4.99, no ads/subscription/mandatory backend for core gameplay, 20+ locales including RTL. Frozen production catalog: **E01–E272**. E273–E277 remain excluded expansion-only events.

## Development order
**Content → canonical QA → machine-readable contracts → Decision Engine → UI → localization/tests → Android QA → APK → release.** No mock/stub gameplay and no premature readiness claims.

## Current phase
**Production runtime integration / Block 7 + premium presentation shell.** `GameSession` is the presentation-neutral gameplay seam. The runtime presentation layer now covers deterministic projection, explicit interaction states, engine-qualified event selection, Event + Choice, Consequence, Realm/History/People/Investigation/Ending/Settings, composed premium journey, adaptive navigation, Main Menu, semantic motion, safe-content bounds, launcher-to-journey navigation, locale/RTL policy, Android adaptive contract, accessibility semantics, audio/haptic vocabulary, composed premium feedback and a canonical cross-screen premium state vocabulary. Android UI binding, production locale coverage, device QA, APK/AAB and store release remain open.

## Latest design/runtime evidence
- `runtime/premium_journey.py` composes Event/Choice, Consequence and the journey screen family behind one navigation boundary.
- `runtime/adaptive_navigation.py` maps available window width to Compact/Medium/Expanded presentation modes.
- `runtime/android_adaptive_contract.py` maps the adaptive model to Android single/supporting/two-pane presentation strategies and safe-content bounds.
- `runtime/main_menu.py` provides Continue/New Run/History/Settings launcher projection without gameplay mutation.
- `runtime/navigation_shell.py` connects launcher and journey through one presentation navigation boundary while preserving the canonical `SessionPresenter/GameSession` mutation seam.
- `runtime/motion.py` provides semantic enter/focus/confirm/resolve/pending/error motion policy with reduced-motion support.
- `runtime/audio_haptics.py` provides semantic sound/haptic tokens independent of gameplay.
- `runtime/premium_feedback.py` composes motion and audio/haptic semantics into one presentation-only feedback projection.
- `runtime/premium_screen_states.py` defines the shared state vocabulary across Event, Realm, History, People, Investigation, Ending and Settings.
- `runtime/safe_area.py` provides a platform-neutral safe-content bounds contract for system bars, cutouts and gesture zones.
- `runtime/accessibility_semantics.py` provides explicit action role/label/hint/state/enabled semantics and a 48dp minimum touch-target contract.
- `runtime/locale_layout.py` provides presentation-only LTR/RTL direction, navigation mirroring, wrapping and large-text reflow policy.
- `tests/test_premium_feedback.py`, `tests/test_premium_screen_states.py`, `tests/test_android_adaptive_contract.py` and `tests/test_accessibility_semantics.py` cover the presentation contracts.
- `design-preview/premium-locale-lab-v1.html` provides representative visual proof for LTR, RTL, large text, long strings, semantic choice/consequence states, focus and reduced motion.
- `design-preview/premium-screen-state-matrix-v1.html` provides representative visual state proof across seven key screens with RTL and large-text toggles.
- `docs/ANDROID_ADAPTIVE_DESIGN_CONTRACT_V1.md`, `docs/AUDIO_HAPTICS_DESIGN_CONTRACT_V1.md`, `docs/PREMIUM_FEEDBACK_INTEGRATION_V1.md` and `docs/PREMIUM_SCREEN_STATE_CONTRACT_V1.md` document the cross-platform presentation contracts.
- Current Android guidance confirms window-size-class-driven adaptation, state continuity during resize/fold/unfold/multi-window, responsive layouts and Material 3 Adaptive navigation/pane primitives. citeturn0search0turn0search1turn0search5turn0search7

## Existing runtime verification baseline
- Full regression baseline: **184 passed** at the last verified runtime checkpoint.
- Production catalog: **PASS**, 272 events / 520 choices / 13 no-choice special nodes.
- Structural graph: **PASS**, 305 edges / 140 roots / 272 structurally reachable / 0 structurally unreachable.
- Deterministic campaign audit: **66 unique events executed / 206 remaining / 0 execution errors**, stopping at E230 under currently implemented trigger/routing semantics.
- Runtime trigger semantics audit: **PASS**, 272 triggers classified; **138 opaque/partial** expressions remain explicitly open.
- Newest design tests are committed but are not claimed CI-green until an actual GitHub Actions run is reported.

## Major blocks
- Foundation / Rules: **100%**
- Authored Content: **90%**
- Canonical IDs / Continuity: **100%**
- Producer / Consumer QA: **100% source-level**
- Derived Predicates / Machine Contracts: **100% source-level**
- Delayed Consequences: **100% runtime-verified**
- Replay / Meta-state: **100% runtime-verified**
- Endings / precedence: **100% runtime-verified at executable boundary**
- Reachability / Causal Graph: **100% source-level; full gameplay reachability remains open**
- Production Data Schema: **50%**
- Runtime State / Persistence Foundation: **100% current foundation**
- Decision Engine / Application Runtime: **42%**
- **Design Specification: 100%** — canonical visual language and design contracts are closed; this does not imply rendered Android UI completion.
- **UI / UX Runtime Implementation: 31%** — presentation projection, interaction states, Event + Choice, Consequence, journey screen family, composed journey, adaptive navigation, Main Menu, motion policy, safe-content contract, launcher-to-journey presentation shell, locale/RTL policy, Android adaptive presentation contract, accessibility semantics, composed premium feedback and canonical cross-screen state vocabulary are implemented. Actual Android screen binding and full visual regression remain open.
- Localization 20+ / RTL: **11%** — presentation policy and representative RTL/large-text/long-string proof exist; real 20+ translated locale rendering remains open.
- Android Implementation: **0%**
- Runtime / Android QA: **25%** — platform-neutral adaptive/safe-area/state contracts exist; physical device verification remains open.
- APK / AAB: **0%**
- Release / Store: **0%**

## Premium Design P1–P25
Canonical percentages are tracked in `docs/PREMIUM_DESIGN_MASTER_P1_P25.md`. Current aggregate: **59.12%**. The latest evidence advances the cross-screen state language and representative visual matrix; no block is treated as 100% without representative visual proof, responsive behavior, accessibility requirements and regression evidence.

## Honest progress rule
Documentation never makes implementation complete. Every percentage requires authoritative evidence and applicable verification. Source/contract GREEN must never be reported as runtime gameplay GREEN. Owner-controlled physical Android QA, production signing and store publication remain open until actually performed.
