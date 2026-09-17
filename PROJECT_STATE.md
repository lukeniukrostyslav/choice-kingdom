# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Android-first, one-time purchase target €2.99–€4.99, no ads/subscription/mandatory backend for core gameplay, 20+ locales including RTL. Frozen production catalog: **E01–E272**.

## Current phase
**General execution plan approved; Block 1 is the active workstream.** The project proceeds strictly block-by-block. Design is preserved and intentionally deferred until the real gameplay/runtime exists, then P1–P25 will be taken to real 100% with implementation and evidence.

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
10. **Localization 20+** → 100%
11. **RTL / Large Text / Accessibility** → 100%
12. **Responsive / Safe Areas / Devices** → 100%
13. **Premium Design P1–P25** → 100%
14. **Motion / Audio / Haptics** → 100%
15. **Cross-Screen Visual Regression** → 100%
16. **Automated QA** → 100%
17. **Performance / Stability / Offline QA** → 100%
18. **Security / Production Hardening** → 100%
19. **APK Debug / QA Build** → 100%
20. **Release APK / AAB** → 100%
21. **Final Device QA** → 100%
22. **Store Preparation** → 100%
23. **Final Release Gate** → 100%
24. **GitHub / Documentation / Recovery** → 100%
25. **RELEASE** → 100%

Execution order is strictly **1 → 2 → 3 → ... → 25**. A block is not considered complete from documentation alone; completion requires implementation, integration and applicable verification/evidence.

## Evidence
- `androidApp/` contains the first real Android Compose application module.
- `.github/workflows/android-presentation.yml` adds a Gradle Android build gate.
- `runtime/premium_screen_states.py`, `runtime/premium_surface_projection.py` and `runtime/premium_regression_matrix.py` remain the canonical platform-neutral presentation contracts.
- `design-preview/premium-screen-state-matrix-v1.html` provides rendered cross-screen proof for responsive density, RTL, large text, reduced motion, safe-area and focus behavior.
- No physical Android/device proof is claimed yet.

## Verification baseline
- Existing canonical runtime checkpoint: **184 passed**.
- Recent authored-choice / graph / delayed lifecycle gates have successful runs.
- Android build gate has been added; its Actions result must be checked before claiming Android CI GREEN.

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
- Design Specification: **100%**
- UI / UX Runtime Implementation: **38%**
- Localization 20+ / RTL: **11%**
- Android Implementation: **8%**
- Runtime / Android QA: **28%**
- APK / AAB: **0%**
- Release / Store: **0%**

## Premium Design P1–P25
Canonical percentages are tracked in `docs/PREMIUM_DESIGN_MASTER_P1_P25.md`. Current aggregate: **62.24%**. P24 remains incomplete without physical device proof.

## Honest progress rule
Documentation never makes implementation complete. Every percentage requires authoritative evidence and applicable verification. Source/contract GREEN must never be reported as runtime gameplay GREEN. Owner-controlled physical Android QA, production signing and store publication remain open until actually performed.
