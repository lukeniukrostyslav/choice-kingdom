# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Meaningful choices, recurring characters, delayed consequences, hidden information, systemic event chains, multiple endings and replayable paths.

## Release target
- Android-first premium one-time purchase, approximately €2.99–€4.99.
- No ads, no subscription, no mandatory backend for core gameplay.
- 20+ locales including RTL and long-string validation.
- Full authored campaign target: approximately 250–350+ meaningful nodes and 8–12 recognizable endings.

## Frozen authored scope
Production catalog is **E01–E272**. E273–E277 are expansion candidates and are excluded from production semantics, producer/consumer edges and reachability.

## Development order
**Content → canonical QA → machine-readable contracts → Decision Engine → UI → localization/tests → Android QA → APK → release.**

No mock/stub gameplay or premature production-readiness claims.

## Current phase
**Scenario QA remains the active phase. S01–S12 are source/contract closed, including S06 replay/meta-state. The scenario-wide source/contract integration gate is implemented and is the next verification gate. Decision Engine remains intentionally blocked until runtime scenario verification is implemented and verified.** Authored checkpoint E01–E272.

## Current verified S01–S12 scorecard
- S01 **100%** — frozen E01–E272 catalog closure, source inventory exhaustiveness and canonical structural reachability gate are GREEN. Source-level only; runtime gameplay reachability remains downstream.
- S02 **100%** — authored choice → state/effect transition closure is source-level closed and CI-verified. Runtime Decision Engine execution remains downstream.
- S03 **100%** — source-level producer/consumer closure closed.
- S04 **100%** — production predicate contracts source-closed; explicit frozen exclusions are machine-gated.
- S05 **100%** — ten frozen high-risk delayed callbacks E181–E185 and E242–E246 are source/contract closed with exact identities, deterministic relative/condition-bound timing, unique lifecycle identity, cancellation classification, explicit supersession, persistent save/load policy and run-scoped replay policy. Runtime lifecycle execution is not claimed.
- S06 **100% source/contract** — replay/meta-state surface E186/E247/E248 is contract-closed with explicit reset boundary, immediately-completed-prior-run import boundary and exactly-once import. Dedicated GitHub Actions run `35105326553` completed **success** on 2026-09-16. Runtime replay execution/reset/isolation remains downstream.
- S07 **100%** — source-level causal graph closed and CI-verified.
- S08 **100%** — source/producer QA closed and CI-verified.
- S09 **100%** — canonical graph source closure closed and CI-verified.
- S10 **100%** — frozen high-risk delayed lifecycle source/contract surface E181–E185 and E242–E246 is source-closed. Production runtime execution is not claimed.
- S11 **100%** — ending qualification, precedence and exact runtime-identifier alias boundary are implemented and CI-verified. Runtime ending execution remains downstream.
- S12 **100%** — scope/integrity gates closed.

**Scenario QA source/contract status: 100%.** This is not 100% runtime scenario completion. Fresh-run gameplay, replay execution, save/load gameplay equivalence, runtime ending resolution and Decision Engine execution remain hard runtime blocks.

## Latest verified work
### S06 — REPLAY / META-STATE SOURCE/CONTRACT CLOSURE: 100%
- Added `docs/S06_REPLAY_META_STATE_CLOSURE_01.md`.
- Added `tools/validate_s06_replay_meta_state_closure.py` and `.github/workflows/s06-replay-meta-state-closure.yml`.
- Frozen replay surface is exactly E186, E247 and E248.
- Contract enforces run reset, import only from the immediately completed prior run, exactly-once import, terminal-state isolation and preservation of E186 same-run `warehouse_arson` routing.
- Dedicated GitHub Actions run `35105326553` completed **success** on 2026-09-16.
- Runtime replay execution/reset/isolation is deliberately not claimed.

### Scenario-wide integration gate — IMPLEMENTED
- Added `tools/validate_scenario_wide_gate.py` to cross-check frozen E01–E272 scope, canonical graph boundary, source-level causal reachability, S06 replay/meta-state and frozen S05/S10 delayed lifecycle targets.
- Added `.github/workflows/scenario-wide-gate.yml` for CI verification.
- The gate explicitly keeps Decision Engine promotion blocked while runtime blocks remain open.
- Runtime hard blocks: Decision Engine execution, fresh-run gameplay reachability, replay gameplay reachability, runtime ending resolution and save/load gameplay equivalence.

### S05 — DELAYED LIFECYCLE SOURCE/CONTRACT CLOSURE: 100%
- Added `docs/S05_DELAYED_LIFECYCLE_CLOSURE_01.md`, `tools/validate_s05_delayed_lifecycle_closure.py` and `.github/workflows/s05-delayed-lifecycle-closure.yml`.
- Locked E181–E185 and E242–E246 to exact authored source choices: E45-B, E117-B, E118-B, E25-B, E17-A, E118-B, E18-B, E09-B, E20-A and E160-A.
- Required unique lifecycle identities, explicit timing, resolution target, cancellation classification, supersession, persistent save/load, run-scoped replay and deterministic priority.
- No authored cancellation/supersession edges were invented; `none_authored`/`null` are explicit.

### S01 — SCENARIO SOURCE CLOSURE: 100% SOURCE-LEVEL
- Added `tools/validate_s01_scenario_closure.py` and `.github/workflows/s01-scenario-source-closure.yml`.
- Frozen production scope E01–E272; E273–E277 excluded.
- S01 verifies exhaustive frozen catalog coverage, no unexpected duplicate headings, inventory 272/272 and causal reachability closure.
- GitHub Actions check `35104747355` completed **success** on 2026-09-16.

### S10 — Delayed Lifecycle: SOURCE/CONTRACT CLOSED 100%
- `docs/MACHINE_DELAY_CONTRACT_01.json` and `docs/MACHINE_CANONICAL_GRAPH_01.json` were hardened around the ten frozen delayed consumers.
- E185 uses exact E17-A producer identity and remains condition-bound to a later military crisis with `earliestTurn=null`; no invented turn was introduced.

### S02 — Choice → State Transition: SOURCE-CLOSED 100%
- Added `docs/S02_CHOICE_STATE_TRANSITION_CLOSURE_01.md` and `tools/validate_s02_choice_state_transition_closure.py`.
- Frozen source cardinality is 272 events / 259 normal / 13 special / 520 choice rows.
- GitHub Actions S02 run `35100082164` completed **success** on 2026-09-16.

### S11 — Ending / Replay QA: SOURCE-CLOSED 100%, CI GREEN
- Added machine-readable ending qualification and precedence contracts and exact alias-boundary validation.
- GitHub Actions manual workflow run #6, commit `847502b`, completed **Success**.

## Major downstream blocks
- Foundation / Rules: **95%**
- Authored Content: **90%**
- Canonical Event IDs / Continuity: **100%**
- Producer / Consumer QA: **100%**
- Derived Predicates / Machine Contracts: **90%**
- Delayed Consequences: **100% source/contract closure for frozen high-risk surface; runtime not implemented**
- Replay / Meta-state: **100% source/contract closure; runtime not implemented**
- Endings / precedence: **100% source-level + CI GREEN; runtime ending execution remains**
- Reachability / Causal Graph: **100% source-level**
- Production Data Schema: **36%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **61%**. Source/contract closure is not runtime/gameplay completion.

## NEXT ACTION
**Run and verify the scenario-wide source/contract integration gate on GitHub. If GREEN, begin runtime scenario verification for fresh-run isolation, replay/meta transfer, delayed consequences, ending resolution and save/load equivalence. Do not promote the Decision Engine to production readiness until those runtime gates are GREEN.**

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes. Source/contract GREEN must never be reported as runtime gameplay GREEN.
