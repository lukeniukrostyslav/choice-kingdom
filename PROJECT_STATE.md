# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Android-first, one-time purchase target €2.99–€4.99, no ads/subscription/mandatory backend for core gameplay, 20+ locales including RTL. Frozen production catalog: **E01–E272**. E273–E277 remain excluded expansion-only events.

## Development order
**Content → canonical QA → machine-readable contracts → Decision Engine → UI → localization/tests → Android QA → APK → release.** No mock/stub gameplay and no premature readiness claims.

## Current phase
**Production runtime integration / Block 7.** Blocks 1–6 have implementation/verification closure at their defined boundaries. `GameSession` is the application-facing presentation-neutral seam. Deterministic full-campaign and trigger-semantics audits are in place. Android UI, localization, device QA, APK/AAB and store release remain open.

## Closed source/contract gates
- S01 **100%** — frozen E01–E272 catalog and source inventory.
- S02 **100%** — authored choice/state transition closure and deterministic routing boundary.
- S03 **100%** — producer/consumer source closure.
- S04 **100%** — predicate contract source closure.
- S05 **100%** — delayed lifecycle source/contract closure.
- S06 **100%** — replay/meta contract and runtime transfer boundary.
- S07 **100% source-level** — causal graph closure; exhaustive gameplay reachability remains downstream.
- S08 **100%** — source/producer QA closure.
- S09 **100%** — canonical graph closure.
- S10 **100%** — delayed lifecycle contract closure.
- S11 **100%** — ending qualification/precedence boundary.
- S12 **100%** — scope/integrity gates.

**Scenario QA source/contract status: 100%. This is not 100% runtime gameplay completion.**

## Latest verified evidence
- GitHub Actions run 777: **SUCCESS**, commit `f9491f2f00a582d129241a943c5e307fe996296b`.
- E199 constitutional producer boundary is source-closed: `army_constitution_oath` is required; `military_red_line` cannot substitute for the authored oath.
- The food predicate test was corrected to select an actual catalog event whose trigger is `pred.food_stable`, verifying both activation and invalidation.
- GitHub Actions for commit `b7999b10200695e5a697118b05b9d232bf289999`: S08 source-closure **SUCCESS** and Predicate Contract Parity **SUCCESS**.
- The new `tests/test_game_session_lifecycle.py` verifies an authored E01 → E02 route through `GameSession`, state mutations, and save/load snapshot preservation; its CI-triggered contract checks are green.

## Existing runtime verification baseline
- Full regression: **184 passed**.
- Production catalog: **PASS**, 272 events / 520 choices / 13 no-choice special nodes.
- Runtime session boundary: **PASS**, 272-event catalog.
- Structural graph: **PASS**, 305 edges / 140 roots / 272 structurally reachable / 0 structurally unreachable.
- Deterministic campaign audit: **66 unique events executed / 206 remaining / 0 execution errors**, stopping at E230 under currently implemented trigger/routing semantics.
- Runtime trigger semantics audit: **PASS**, 272 triggers classified; **138 opaque/partial** expressions remain explicitly open. The audit separately identifies 2 explicit after-event prerequisites and 14 safe source-level canonical alias phrases.
- Canonical predicate trigger integration: **PASS** in GitHub Actions run 402 (`a8a83c1f...`).

The campaign and trigger audits are diagnostic. Missing/opaque events are **not declared impossible**. No trigger threshold, route activation, relationship proxy, or graph edge is promoted into gameplay semantics without source evidence.

## Major blocks
- Foundation / Rules: **100%**
- Authored Content: **90%** — E01–E272 authored/frozen; narrative QA remains distinct from runtime implementation.
- Canonical IDs / Continuity: **100%**
- Producer / Consumer QA: **100% source-level**
- Derived Predicates / Machine Contracts: **100% source-level**
- Delayed Consequences: **100% runtime-verified**
- Replay / Meta-state: **100% runtime-verified**
- Endings / precedence: **100% runtime-verified at executable boundary**
- Reachability / Causal Graph: **100% source-level; full gameplay reachability remains open**
- Production Data Schema: **50%**
- Runtime State / Persistence Foundation: **100% current foundation**
- Decision Engine / Application Runtime: **42%** — core authored effects, routing, delayed execution, ending boundary, persistence, replay transfer, session lifecycle, canonical predicate evaluation, verified E199 producer semantics, and an authored E01→E02 GameSession lifecycle/save-load verification are implemented; exhaustive production trigger/semantic execution remains open.
- **Design Specification: 100%** — production visual language, semantic tokens, typography, screen/component contracts, interaction states, accessibility, RTL, localization design constraints, asset contract, screen matrix and visual-QA acceptance are closed in `docs/DESIGN_COMPLETION_V1.md`, `docs/DESIGN_TOKENS_V1.json`, `docs/DESIGN_SCREEN_MATRIX_V1.md`, `docs/DESIGN_ASSET_MANIFEST_V1.md` and `docs/DESIGN_VISUAL_QA_CHECKLIST_V1.md`.
- UI / UX Runtime Implementation: **0%** — separate from the now-closed design specification.
- Localization 20+ / RTL: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **22%** — headless runtime and deterministic audits verified; Android/device gameplay remains open.
- APK / AAB: **0%**
- Release / Store: **0%**

## Latest runtime closure

Canonical predicate trigger atoms use the same `EndingSourceCompiler` as ending qualification. E199 constitutional readiness is tied to its canonical authored producer `army_constitution_oath`; the later `military_red_line` evidence cannot silently substitute for that producer. The source-level negative/positive test locks this boundary.

The food predicate test now selects a real catalog event whose trigger is `pred.food_stable`; it verifies activation by `food_logistics_stabilized` and invalidation by `food_logistics_unstable`. This removes a false-positive assertion that previously used E192 itself even though E192's authored trigger is `pred.transport_disruption`.

The E199 change is verified by GitHub Actions run 777. The corrected food test is implemented in commit `e1fc14fbc2c541a9ba2bb4b0198c0471dad5fc17` and its follow-up CI verification is green.

A production-facing `GameSession` lifecycle test now verifies the canonical runtime boundary with authored E01 → E02 execution plus persistence round-trip. This is a verified application-runtime increment, raising Block 12 from 41% to 42%.

## Current Block 7 target
Close authoritative trigger/producer semantics only where authored source and canonical contracts define them; bind verified semantics into the runtime; rerun the full regression and campaign audit; then make E01–E272 executable through one `GameSession` lifecycle.

## Honest progress rule
Documentation never makes implementation complete. Every percentage requires authoritative evidence and applicable verification. Source/contract GREEN must never be reported as runtime gameplay GREEN. Owner-controlled physical Android QA, production signing and store publication remain open until actually performed.
