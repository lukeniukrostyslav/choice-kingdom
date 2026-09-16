# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Android-first, one-time purchase target €2.99–€4.99, no ads/subscription/mandatory backend for core gameplay, 20+ locales including RTL. Frozen production catalog: **E01–E272**. E273–E277 remain excluded expansion-only events.

## Development order
**Content → canonical QA → machine-readable contracts → Decision Engine → UI → localization/tests → Android QA → APK → release.** No mock/stub gameplay and no premature readiness claims.

## Current phase
**Production runtime integration / Block 7.** Blocks 1–6 have implementation/verification closure at their defined boundaries. `GameSession` is the application-facing presentation-neutral seam. Deterministic full-campaign and trigger-semantics audits are now in place. Android UI, localization, device QA, APK/AAB and store release remain open.

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

## Latest local verification
- Full regression: **184 passed**.
- Production catalog: **PASS**, 272 events / 520 choices / 13 no-choice special nodes.
- Runtime session boundary: **PASS**, 272-event catalog.
- Structural graph: **PASS**, 305 edges / 140 roots / 272 structurally reachable / 0 structurally unreachable.
- Deterministic campaign audit: **66 unique events executed / 206 remaining / 0 execution errors**, stopping at E230 under currently implemented trigger/routing semantics.
- Runtime trigger semantics audit: **PASS**, 272 triggers classified; **138 opaque/partial** expressions remain explicitly open. The audit separately identifies 2 explicit after-event prerequisites and 14 safe source-level canonical alias phrases.
- Canonical predicate trigger integration: **PASS** in GitHub Actions run 402 (`a8a83c1f...`).
- E199 constitutional producer boundary: **PASS** in GitHub Actions run 777 (`f9491f2f...`). The runtime now requires the authored `army_constitution_oath` producer for `pred.constitutional_prepared_strong`; supporting `military_red_line` evidence cannot substitute for E199-A.

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
- Decision Engine / Application Runtime: **41%** — core authored effects, routing, delayed execution, ending boundary, persistence, replay transfer, session lifecycle, and structured boolean evaluation of already-canonical trigger atoms are implemented; the E199 constitutional producer boundary is now runtime-verified; exhaustive production trigger/semantic execution remains open.
- UI / UX: **0%**
- Localization 20+ / RTL: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **22%** — headless runtime and deterministic audits verified; Android/device gameplay remains open.
- APK / AAB: **0%**
- Release / Store: **0%**

## Latest runtime closure

Canonical predicate trigger atoms now use the same `EndingSourceCompiler` as ending qualification. This removes the duplicated `pred.food_stable` trigger special case and preserves the authored E192-B producer / E192-A invalidation semantics in one source-closed compiler. New tests cover both positive and invalidated food-stability states plus trigger evaluation through the shared compiler.

The centralized canonical predicate trigger integration is **IMPLEMENTED / VERIFIED** by GitHub Actions run 402 on commit `a8a83c1febb49b9a0cc14452ff2408135caf755d`.

The E199 constitutional producer boundary is **IMPLEMENTED / VERIFIED** by GitHub Actions run 777 on commit `f9491f2f00a582d129241a943c5e307fe996296b`. The runtime contract requires the authored `army_constitution_oath` marker for the military constitutional domain and explicitly rejects `military_red_line` as a substitute.

This is a genuine incremental closure for Block 12, so its progress is raised from **40% to 41%**. This does not imply that the broader production trigger/semantic execution gap is closed.

## Current Block 7 target
Close authoritative trigger/producer semantics only where authored source and canonical contracts define them; bind verified semantics into the runtime; rerun the full regression and campaign audit; then make E01–E272 executable through one `GameSession` lifecycle.

## Latest work saved to GitHub
- `runtime/ending_sources.py` — source-closed predicate compilation including E192 food-stability lifecycle and canonical E199 military-law producer semantics.
- `runtime/catalog.py` — all canonical `pred.*` trigger atoms now route through `EndingSourceCompiler` instead of maintaining a separate `pred.food_stable` special case.
- `tests/test_runtime_source_closed_predicates.py` — source-closed predicate, hard-negative, invalidation, shared-trigger-compiler, and E199 producer-boundary coverage.
- `docs/RUNTIME_SOURCE_CLOSED_PREDICATE_CLOSURE_01.md` — verified implementation checkpoint.
- `tools/audit_runtime_campaign.py`
- `tests/test_runtime_campaign_audit.py`
- `.github/workflows/runtime-campaign-audit.yml`
- `docs/RUNTIME_CAMPAIGN_AUDIT_01.md`
- `tools/audit_runtime_trigger_semantics.py` — refined source classification for explicit prerequisites and safe canonical aliases.
- `tests/test_runtime_trigger_semantics_audit.py`
- `.github/workflows/runtime-trigger-semantics-audit.yml`
- `docs/MACHINE_RUNTIME_TRIGGER_SEMANTICS_AUDIT_01.json`
- `docs/RUNTIME_STRUCTURED_BOOLEAN_TRIGGER_CLOSURE_01.md`

## Honest progress rule
Documentation never makes implementation complete. Every percentage requires authoritative evidence and applicable verification. Source/contract GREEN must never be reported as runtime gameplay GREEN. Owner-controlled physical Android QA, production signing and store publication remain open until actually performed.
