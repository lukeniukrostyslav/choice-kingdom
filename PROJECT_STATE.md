# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Android-first, one-time purchase target €2.99–€4.99, no ads/subscription/mandatory backend for core gameplay, 20+ locales including RTL. Frozen production catalog: **E01–E272**. E273–E277 are expansion-only and excluded from production semantics/reachability.

## Development order
**Content → canonical QA → machine-readable contracts → Decision Engine → UI → localization/tests → Android QA → APK → release.** No mock/stub gameplay and no premature readiness claims.

## Current phase
**Scenario QA → runtime scenario verification.** S01–S12 are source/contract closed. Scenario-wide source/contract integration is GREEN. The first executable runtime state/persistence boundary is now implemented and CI-verified. Full Decision Engine promotion remains blocked until authored choice execution, delayed lifecycle, replay/meta transfer, ending resolution, save/load equivalence and determinism are verified.

## S01–S12 source/contract scorecard
- S01 **100%** — frozen E01–E272 catalog/source inventory/structural reachability closure.
- S02 **100%** — authored choice → state/effect transition closure, CI-verified; runtime execution downstream.
- S03 **100%** — producer/consumer source closure.
- S04 **100%** — predicate contracts source-closed; frozen exclusions machine-gated.
- S05 **100%** — ten frozen delayed callbacks E181–E185 and E242–E246 source/contract closed; runtime execution downstream.
- S06 **100% source/contract** — E186/E247/E248 replay/meta contract closed; runtime replay downstream.
- S07 **100%** — source causal graph closed and CI-verified; runtime reachability downstream.
- S08 **100%** — source/producer QA closed and CI-verified.
- S09 **100%** — canonical graph source closure closed and CI-verified.
- S10 **100%** — delayed lifecycle source/contract surface closed; runtime downstream.
- S11 **100%** — ending qualification/precedence/identifier boundary CI-verified; runtime ending resolution downstream.
- S12 **100%** — scope/integrity gates closed.

**Scenario QA source/contract status: 100%. This is not 100% runtime gameplay completion.**

## Latest verified work
### Scenario-wide source/contract integration — GREEN
- Commit `51809fddc344c02ad48b48a44a7a4df5f7aea2cf` fixed causal-report generation inside the wide-gate workflow.
- GitHub Actions run `35106595137` completed **success** on 2026-09-16.
- Runtime-promotion-block assertion also passed.

### Runtime scenario core — FIRST EXECUTABLE RUNTIME BOUNDARY GREEN
Repository inspection showed no existing Godot/runtime/persistence implementation to wrap at this boundary; the repository was still catalog/contracts/QA-only. A mock path was therefore not introduced.

Added:
- `runtime/__init__.py`
- `runtime/state.py` — versioned `GameState`, canonical five resources/six relationships, flags/history/threads, run-local pending delays, exactly-once delay resolution, E273–E277 rejection, JSON save/load boundary.
- `tests/test_runtime_state.py` — fresh-run isolation, save/load equivalence, exactly-once delays, condition-bound delay discipline, excluded-event rejection.
- `.github/workflows/runtime-scenario-core.yml`

GitHub Actions run **`35107430687`** (`Choice Kingdom Runtime Scenario Core`, #1) completed **success** on 2026-09-16. Runtime test step completed successfully.

This is **runtime foundation GREEN**, not full gameplay GREEN. The runtime does not yet execute all 520 authored choices or the complete event catalog.

## Major blocks
- Foundation / Rules: **95%**
- Authored Content: **90%**
- Canonical IDs / Continuity: **100%**
- Producer / Consumer QA: **100%**
- Derived Predicates / Machine Contracts: **90%**
- Delayed Consequences: **100% source/contract; runtime execution pending**
- Replay / Meta-state: **100% source/contract; runtime transfer pending**
- Endings / precedence: **100% source/contract + CI; runtime resolution pending**
- Reachability / Causal Graph: **100% source-level**
- Production Data Schema: **36%**
- Runtime State / Persistence Foundation: **15%**
- Decision Engine: **0%** — state boundary alone is not the engine.
- UI / UX: **0%**
- Localization 20+: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **0%** beyond headless runtime foundation
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **61%**; the new runtime foundation is intentionally too small to change the rounded overall estimate.

## NEXT ACTION
**Extend the real runtime boundary into authored choice execution. Build a data-driven event/choice loader against the frozen E01–E272 authored source/contracts, then verify representative immediate state transitions and route handling. Next integrate the ten frozen delayed lifecycle entries, replay/meta import boundary, ending resolver and complete save/load/determinism gates. Do not promote Decision Engine production readiness until the complete runtime scenario gate is GREEN.**

## Honest progress rule
Documentation alone never makes implementation complete. Every percentage requires authoritative evidence and the applicable verification. Source/contract GREEN must never be reported as runtime gameplay GREEN.
