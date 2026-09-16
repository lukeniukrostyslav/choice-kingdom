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
**Scenario QA remains the active phase. S01 and S05 delayed-lifecycle source/contract closure are now 100%; S10 delayed-lifecycle source/contract closure is also 100%. Decision Engine remains intentionally blocked until the remaining scenario blocks are closed.** Authored checkpoint E01–E272. Source-level canonical graph, causal closure, S01 source closure, S02 choice/state transition closure and S05 delayed lifecycle closure are green. S11 qualification, precedence and exact alias-boundary validation are green in the dedicated workflow.

## Current verified S01–S12 scorecard
- S01 **100%** — frozen E01–E272 catalog closure, source inventory exhaustiveness and canonical structural reachability gate are GREEN. Dedicated GitHub Actions run `35104747355` completed **success** on 2026-09-16. This is source-level scenario closure; Decision Engine execution, fresh-run gameplay reachability and replay reachability remain downstream.
- S02 **100%** — authored choice → state/effect transition closure is source-level closed and CI-verified. Runtime Decision Engine execution, persistence and gameplay reachability remain downstream.
- S03 **100%** — source-level producer/consumer closure closed.
- S04 **100%** — production predicate contracts source-closed; explicit frozen exclusions are machine-gated.
- S05 **100%** — all ten canonically identified frozen high-risk delayed callbacks E181–E185 and E242–E246 are source/contract closed with exact source identity, deterministic relative/condition-bound timing, unique lifecycle identity, explicit cancellation classification, explicit supersession (`null` where no authored supersession exists), persistent save/load policy and run-scoped replay policy. Dedicated S05 GitHub Actions check `s05-delayed-lifecycle-closure` on commit `a8a66859037aa02bba440382b3102056d8f1d6ee` completed **success** on 2026-09-16. Runtime lifecycle execution is deliberately not claimed.
- S06 **65%** — replay/meta source contracts advanced; runtime replay execution/reset/isolation remain.
- S07 **100%** — source-level causal graph closed and CI-verified.
- S08 **100%** — source/producer QA closed and CI-verified.
- S09 **100%** — canonical graph source closure closed and CI-verified.
- S10 **100%** — frozen high-risk delayed lifecycle source/contract surface E181–E185 and E242–E246 is source-closed with exact source identities, deterministic relative/condition-bound timing, unique exactly-once keys, persistent save/load policy and run-scoped replay policy. Production runtime execution is explicitly not claimed.
- S11 **100%** — final CI verification GREEN. Ending qualification, precedence and exact runtime-identifier alias boundary are implemented and verified by GitHub Actions workflow run #6 on commit `847502b`.
- S12 **100%** — scope/integrity gates closed.

**Scenario QA aggregate: S01, S05 and S10 source closure are now 100%; broader scenario completion remains below 100% because S06 still contains explicitly open replay/runtime gates, and runtime gameplay verification remains downstream.**

## Latest verified work
### S05.1 — DELAYED LIFECYCLE SOURCE/CONTRACT CLOSURE: 100%
- Added `docs/S05_DELAYED_LIFECYCLE_CLOSURE_01.md` defining the frozen S05 delayed callback surface and lifecycle rules.
- Added `tools/validate_s05_delayed_lifecycle_closure.py` as the executable S05 gate.
- Added `.github/workflows/s05-delayed-lifecycle-closure.yml` for dedicated CI verification.
- Locked the ten canonical delayed consumers E181–E185 and E242–E246 to their exact authored source choices: E45-B, E117-B, E118-B, E25-B, E17-A, E118-B, E18-B, E09-B, E20-A and E160-A respectively.
- Required unique `id` and `exactlyOnceKey`, explicit timing form, resolution target, cancellation classification, explicit `supersedes`, persistent save/load, run-scoped replay policy and deterministic priority.
- Closed the cancellation/supersession source ambiguity conservatively: current authored source provides no later-decision cancellation or supersession for these ten callbacks, so the machine contract explicitly records `none_authored` and `null` instead of inventing edges.
- Dedicated S05 GitHub Actions check `s05-delayed-lifecycle-closure` completed **success** on 2026-09-16 for commit `a8a66859037aa02bba440382b3102056d8f1d6ee`.
- This is source/contract closure only. Production Decision Engine execution, runtime cancellation, runtime supersession, duplicate-resolution prevention, save/load execution and replay execution remain downstream.

### S01.1 — SCENARIO SOURCE CLOSURE: 100% SOURCE-LEVEL
- Added `tools/validate_s01_scenario_closure.py` as the dedicated S01 closure gate.
- Added `.github/workflows/s01-scenario-source-closure.yml` to compile the authoritative source inventory, validate canonical causal reachability, validate canonical graph closure and enforce the S01 contract.
- Frozen production scope is enforced as **E01–E272**, with E273–E277 excluded.
- S01 gate verifies exhaustive frozen catalog coverage, no unexpected duplicate catalog headings, source inventory cardinality **272/272**, and canonical causal reachability closure.
- GitHub Actions check `s01-scenario-source-closure` run **35104747355**, head `bde8d9756cbf09da0b81c9a9d77216a27e35264d`, completed **success** on 2026-09-16.
- This closure does not claim production Decision Engine execution, fresh-run gameplay reachability, replay execution, save/load gameplay equivalence or Android runtime readiness.

### S10.6 — Delayed Lifecycle: SOURCE/CONTRACT CLOSED 100%
- Re-read `docs/MACHINE_DELAY_CONTRACT_01.json`, `docs/MACHINE_CANONICAL_GRAPH_01.json`, `tools/validate_delayed_lifecycle_gate.py` and `tools/validate_machine_delay_contract.py` before changing the gate.
- Closed the final high-risk source ambiguity: E185 uses exact E17-A producer identity and remains condition-bound to a later military crisis with `earliestTurn=null`; no invented turn was introduced.
- Updated `docs/MACHINE_CANONICAL_GRAPH_01.json` so all ten frozen delayed consumers E181–E185 and E242–E246 are status `CLOSED`.
- Hardened delayed lifecycle validators to require all ten identities, exact source candidates, unique `exactlyOnceKey`, persistent save/load, run-scoped replay, deterministic relative timing, and the explicit condition-bound E185 rule.
- Existing reference-runtime QA model covers E185's negative/positive military-crisis condition, duplicate scheduling, save/load pending-state preservation and fresh-run reset; it remains a reference model and not the production Decision Engine.

### S02 — Choice → State Transition: SOURCE-CLOSED 100%
- Added `docs/S02_CHOICE_STATE_TRANSITION_CLOSURE_01.md` defining the frozen S02 source contract.
- Added `tools/validate_s02_choice_state_transition_closure.py` as an executable S02 closure gate.
- Frozen source cardinality is **272 events / 259 normal / 13 special / 520 choice rows**.
- GitHub Actions S02 run **35100082164** completed **success** on 2026-09-16.
- This is source-level closure only; runtime Decision Engine execution remains downstream.

### S11 — Ending / Replay QA: SOURCE-CLOSED 100%, CI GREEN
- Added machine-readable ending qualification and precedence contracts and exact alias-boundary validation.
- GitHub Actions manual workflow run **#6**, commit **847502b**, completed **Success**.
- Runtime ending execution, fresh-run reachability, replay reachability and save/load equivalence remain deliberately downstream.

## S11 remaining downstream gates
1. Decision Engine execution of the exact prerequisite/blocker contract;
2. runtime deterministic ending selection;
3. fresh-run gameplay reachability;
4. replay gameplay reachability and meta transfer execution;
5. save/load equivalence at ending resolution.

## Major downstream blocks
- Foundation / Rules: **95%**
- Authored Content: **90%**
- Canonical Event IDs / Continuity: **100%**
- Producer / Consumer QA: **100%**
- Derived Predicates / Machine Contracts: **90%**
- Delayed Consequences: **100% source/contract closure for frozen high-risk surface; runtime not implemented**
- Replay / Meta-state: **65%**
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

Overall project progress remains approximately **61%**. This deliberately does not treat source-level QA closure as runtime/gameplay completion.

## NEXT ACTION
**Continue scenario closure before Decision Engine: close the remaining S06 source-level gaps using only authoritative E01–E272 catalog evidence, then perform the scenario-wide fresh-run/replay/reachability verification gate. Do not start Decision Engine yet.**

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.
