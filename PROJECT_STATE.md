# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Android-first, one-time purchase target €2.99–€4.99, no ads/subscription/mandatory backend for core gameplay, 20+ locales including RTL. Frozen production catalog: **E01–E272**. E273–E277 remain excluded expansion-only events.

## Development order
**Content → canonical QA → machine-readable contracts → Decision Engine → UI → localization/tests → Android QA → APK → release.** No mock/stub gameplay and no premature readiness claims.

## Current phase
**Production runtime integration / Block 7 + premium presentation shell.** `GameSession` is the presentation-neutral gameplay seam. The runtime presentation layer now covers deterministic projection, explicit interaction states, engine-qualified event selection, Event + Choice, Consequence, Realm/History/People/Investigation/Ending/Settings, a composed premium journey, adaptive navigation, Main Menu, semantic motion, safe-content bounds, launcher-to-journey navigation, and a locale/RTL presentation policy. Android UI, production locale coverage, device QA, APK/AAB and store release remain open.

## Latest design/runtime evidence
- `runtime/premium_journey.py` composes Event/Choice, Consequence and the journey screen family behind one navigation boundary.
- `runtime/adaptive_navigation.py` maps available window width to Compact/Medium/Expanded presentation modes.
- `runtime/main_menu.py` provides Continue/New Run/History/Settings launcher projection without gameplay mutation.
- `runtime/navigation_shell.py` connects launcher and journey through one presentation navigation boundary while preserving the canonical `SessionPresenter/GameSession` mutation seam.
- `runtime/motion.py` provides semantic enter/focus/confirm/resolve/pending/error motion policy with reduced-motion support.
- `runtime/safe_area.py` provides a platform-neutral safe-content bounds contract for system bars, cutouts and gesture zones.
- `runtime/locale_layout.py` provides presentation-only LTR/RTL direction, navigation mirroring, wrapping and large-text reflow policy.
- `tests/test_locale_layout.py` verifies RTL and large-text policy behavior.
- `design-preview/premium-locale-lab-v1.html` provides representative visual proof for LTR, RTL, large text and long strings.
- `docs/LOCALE_LAYOUT_CONTRACT_V1.md` records the locale/RTL/long-string boundary and keeps localization outside gameplay semantics.
- Current Android guidance confirms that adaptive work should be driven by app-window size classes, preserve state during resize/fold/unfold/multi-window transitions, and protect interactive content with safe insets. citeturn0search0turn0search1turn0search2turn0search4

## Existing runtime verification baseline
- Full regression baseline: **184 passed** at the last verified runtime checkpoint.
- Production catalog: **PASS**, 272 events / 520 choices / 13 no-choice special nodes.
- Structural graph: **PASS**, 305 edges / 140 roots / 272 structurally reachable / 0 structurally unreachable.
- Deterministic campaign audit: **66 unique events executed / 206 remaining / 0 execution errors**, stopping at E230 under currently implemented trigger/routing semantics.
- Runtime trigger semantics audit: **PASS**, 272 triggers classified; **138 opaque/partial** expressions remain explicitly open.
- Newest locale/design tests are committed but are not claimed CI-green until an actual GitHub Actions run is reported.

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
- **UI / UX Runtime Implementation: 25%** — presentation projection, interaction states, Event + Choice, Consequence, journey screen family, composed journey, adaptive navigation, Main Menu, motion policy, safe-content contract, launcher-to-journey presentation shell, and locale/RTL presentation policy are implemented. Actual Android screen binding and full visual regression remain open.
- Localization 20+ / RTL: **10%** — presentation policy and representative RTL/large-text/long-string proof exist; real 20+ translated locale rendering remains open.
- Android Implementation: **0%**
- Runtime / Android QA: **22%**
- APK / AAB: **0%**
- Release / Store: **0%**

## Premium Design P1–P25
Canonical percentages are tracked in `docs/PREMIUM_DESIGN_MASTER_P1_P25.md`. Current aggregate: **56.92%**. The latest evidence advances P18/P19/P20/P21/P22/P24, but no block is treated as 100% without representative visual proof, responsive behavior, accessibility requirements and regression evidence.

## Honest progress rule
Documentation never makes implementation complete. Every percentage requires authoritative evidence and applicable verification. Source/contract GREEN must never be reported as runtime gameplay GREEN. Owner-controlled physical Android QA, production signing and store publication remain open until actually performed.
