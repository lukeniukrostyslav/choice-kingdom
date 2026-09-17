# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Android-first, one-time purchase target €2.99–€4.99, no ads/subscription/mandatory backend for core gameplay, 20+ locales including RTL. Frozen production catalog: **E01–E272**.

## Current phase
**Android presentation foundation / premium runtime integration.** A real Android Compose module now provides the first production-facing premium presentation surface with adaptive Compact/Medium/Expanded layouts, safe-drawing insets and semantic interaction states. Canonical gameplay remains separate. Android runtime integration with the real `SessionPresenter`, physical device QA, production locale coverage, APK/AAB and store release remain open.

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
