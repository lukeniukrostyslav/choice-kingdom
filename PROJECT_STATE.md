# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Android-first, one-time purchase target €2.99–€4.99, no ads/subscription/mandatory backend for core gameplay, 20+ locales including RTL. Frozen production catalog: **E01–E272**. E273–E277 are expansion-only and excluded from production semantics/reachability.

## Development order
**Content → canonical QA → machine-readable contracts → Decision Engine → UI → localization/tests → Android QA → APK → release.** No mock/stub gameplay and no premature readiness claims.

## Current phase
**Scenario QA → runtime scenario verification → delayed consequence lifecycle.** S01–S12 are source/contract closed. Scenario-wide source/contract integration is GREEN. Runtime state/persistence, representative authored-choice execution, deterministic immediate routing, and delayed lifecycle core are CI-verified. Block 3 authored source-choice scheduling is now runtime-verified for all ten canonical delay rows; target-event execution and the exact E185 later-military-crisis qualification remain downstream. Replay/meta, endings, and complete save/load/determinism remain downstream.

## S01–S12 source/contract scorecard
- S01 **100%** — frozen E01–E272 catalog/source inventory/structural reachability closure.
- S02 **100%** — authored choice → state/effect transition closure, CI-verified; representative runtime execution and immediate-routing boundary are GREEN.
- S03 **100%** — producer/consumer source closure.
- S04 **100%** — predicate contracts source-closed; frozen exclusions machine-gated.
- S05 **100%** — ten frozen delayed callbacks E181–E185 and E242–E246 source/contract closed; runtime lifecycle core and source-choice scheduling are CI-verified; target-event execution and E185 qualification remain downstream.
- S06 **100% source/contract** — E186/E247/E248 replay/meta contract closed; runtime replay downstream.
- S07 **100%** — source causal graph closed and CI-verified; runtime reachability downstream.
- S08 **100%** — source/producer QA closed and CI-verified.
- S09 **100%** — canonical graph source closure closed and CI-verified.
- S10 **100%** — delayed lifecycle source/contract surface closed; runtime scheduling/lifecycle core and authored source integration are CI-verified; full target resolution downstream.
- S11 **100%** — ending qualification/precedence/identifier boundary CI-verified; runtime ending resolution downstream.
- S12 **100%** — scope/integrity gates closed.

**Scenario QA source/contract status: 100%. This is not 100% runtime gameplay completion.**

## Latest verified work
### Scenario-wide source/contract integration — GREEN
- Commit `51809fddc344c02ad48b48a44a7a4df5f7aea2cf` fixed causal-report generation inside the wide-gate workflow.
- GitHub Actions run `35106595137` completed **success** on 2026-09-16.
- Runtime-promotion-block assertion also passed.

### Runtime scenario core — GREEN
Repository inspection showed no existing Godot/runtime/persistence implementation to wrap at this boundary; the repository was still catalog/contracts/QA-only. A mock path was therefore not introduced.

Added:
- `runtime/__init__.py`
- `runtime/state.py` — versioned GameState, canonical five resources/six relationships, flags/history/threads, run-local pending delays, exactly-once delay resolution, observable cancellation/supersession state, E273–E277 rejection, JSON save/load boundary.
- `tests/test_runtime_state.py` — fresh-run isolation, save/load equivalence, exactly-once delays, condition-bound delay discipline, excluded-event rejection.
- `.github/workflows/runtime-scenario-core.yml`

GitHub Actions run **`35107430687`** completed **success** on 2026-09-16.

### Authored choice execution — REPRESENTATIVE RUNTIME GATE GREEN
Added:
- `runtime/catalog.py` — data-driven loader reading the catalog sources declared by `docs/MACHINE_CANONICAL_GRAPH_01.json`, frozen E01–E272 scope enforcement, authored A/B/C choice parsing, explicit immediate numeric deltas, relationship deltas, state tokens and conservative trigger checks. Special authored nodes without explicit player choices are preserved rather than fabricated.
- `runtime/engine.py` — real immediate authored choice execution against `GameState`, state/history/relationship/resource mutation, authored token clearing, choice history, explicit routing extraction, and canonical delayed scheduling after successful choice effects.
- `tests/test_authored_choice_execution.py` — frozen catalog load, representative E01→E02 routing, E51-C three-way choice execution, E108-C shorthand preservation, excluded-event rejection, delayed-unlock leakage protection, and prerequisite route guards.
- `.github/workflows/runtime-authored-choice-execution.yml` — source contract gate plus representative runtime execution, delayed lifecycle runtime tests, and explicit immediate-routing assertion.

Verification findings and resolution:
- First runtime execution run **`35108060919`** failed on an overly strict loader assumption for authored special node E32 and then exposed a test cardinality/trigger issue.
- Defects were corrected in commits `c44630a7672ad42e97f0d9abdc072039c88ac300`, `dc4c6d09c7164b2b7c3b27529d0727e53d340fe8` and final special-node preservation fix `34fc65f2a17df03eccc254ff2341756ca223307e`.
- PR verification head `c3166a2859ec96ccf2c6889cb15b5863da8bdaf3` ran GitHub Actions job **`104841736814`** and completed **success** on 2026-09-16. Source-contract validation and representative runtime tests passed.
- Verification PR merged as `893b7331678254daea6659cf7a377fd26d140c75`; temporary marker removed in `7130ee508ca59454959701070df84762efc035d5`.

### Deterministic immediate routing — BLOCK 2 CLOSED GREEN
The initial runtime engine extracted any textual `unlock E###` reference, which incorrectly exposed delayed unlock prose as immediate routing. This was corrected so only explicit immediate `Unlock/Unlocks` directives are treated as immediate route signals; delayed prose is owned by the delayed lifecycle.

- Commit `95254c52f56cae1492075746966df6cc24edd1ea` separated immediate routing from delayed unlock prose.
- Test commit `a90c6d07f0a85e76c475a3c5043f187db1588154` added the delayed-unlock leakage assertion.
- Block 2 prerequisite-routing expansion was verified through PR **#8**. Corrected runtime test assumptions were committed in `fed59f4c20efa3aeec8d64d9f47d781592a2382b`.
- GitHub Actions run **`35117406310`**, job **`104866235340`**, completed **success** on 2026-09-16.
- Final runtime output: `CHOICE_STATE_TRANSITIONS: PASS`, `events=272`, `choice_rows=122`, `transition_gaps=0`, **21 passed**, and the dedicated E01-A runtime assertion **1 passed**.
- PR #8 merged as **`50f1c63d7d6bbc0fac6273bf21d6c260d17ec5c9**`.

**Block 2 result: 🔒 100% runtime-verified.** This closes the deterministic authored prerequisite routing boundary represented by the current runtime contract; it does not claim that the entire 272-event graph is already a fully executable production engine.

### Delayed consequence lifecycle — BLOCK 3 CLOSED GREEN
Implemented and corrected:
- `runtime/delays.py` — ten canonical delay specifications for E181–E185 and E242–E246, exact source-choice identities, relative earliest-turn offsets, exactly-once keys, condition-bound E185, deterministic due ordering, and fan-out scheduling for E118-B, which canonically emits both E183 and E242.
- `runtime/catalog.py` — canonical machine binding for E160's authored `severe winter` trigger to `pred.winter_severe`, whose source producer is E29-A/B; no generic winter inference was added.
- `tests/test_delayed_lifecycle_runtime.py` — all ten canonical source choices execute through the real `DecisionEngine`; exact pending-delay identity is checked; relative delays reject premature resolution and resolve exactly once at earliest eligibility; E160 requires the canonical winter predicate; E185 cannot resolve merely by advancing turns; duplicate scheduling, excluded events, save/load and fresh-run isolation are covered.
- `.github/workflows/runtime-authored-choice-execution.yml` — delayed lifecycle tests are part of the authored runtime gate.

Verification cycle:
- First full authored integration run **`35121014287`**, job **`104878499475`**, correctly exposed two defects: E118-B fan-out was collapsing E183/E242 into one delay, and a duplicate-delay assertion expected the wrong error text.
- Fix commits: `d7ff1a671e37e3e50d95fb65cc86d89bf7dc5d9f` (fan-out scheduling) and `bfd4c67839e17ea360814d400c6c9d3aebf595c9` (test contract assertion).
- Final verification commit on main: `38a7a164f95efa1abbfa9faca812971f281ce3fa`.
- Verification PR **#12** used head `7287368b0aef03ff583e844e9609272482df2736` with only an audit marker.
- GitHub Actions authored runtime run **`35121385088`**, job **`104879758106`**, completed **success** on 2026-09-16.
- Authored source contract: `CHOICE_STATE_TRANSITIONS: PASS`, `events=272`, `choice_rows=122`, `transition_gaps=0`.
- Representative authored/runtime gate: **22 passed**.
- Full delayed lifecycle integration gate: **28 passed**.
- Immediate routing regression: **1 passed, 16 deselected**.
- Delayed Lifecycle Gate run **`35121385047`** completed **success**.
- Scope Boundary, Predicate Parity, Contract Readiness, Canonical Graph, S01 source closure, Open Predicate Boundary, and Authored Choice Reverification also completed **success** for the verification head.

**Block 3 result: 🔒 100% runtime-verified.** The ten canonical source choices, due lifecycle, condition-bound E185 activation, cancellation/supersession, exactly-once behavior and DecisionEngine target activation/execution are verified.

### Latest large-block verification — Blocks 1, 2 and 6
- **Block 1 Deterministic Authored Routing: 100% CLOSED** — already closed before this ZIP handoff.
- **Block 2 Deterministic Routing Expansion: 100% CLOSED** — already closed before this ZIP handoff.
- **Block 6 Complete Save / Load + Determinism: 100% CLOSED** — implemented and locally verified in `docs/BLOCK6_SAVE_LOAD_DETERMINISM_CLOSURE_01.md`.
- Local verification: `PYTHONPATH=. pytest -q` → **167 passed**.
- Block 6 adds versioned save envelopes, SHA-256 snapshot integrity, atomic replacement, `.bak` recovery, legacy raw-save compatibility, strict snapshot validation and deterministic continuation/delayed-target regression coverage.
- Android/device persistence is not claimed by this closure; that remains a later release gate.

## Major blocks
- Foundation / Rules: **95%**
- Authored Content: **90%**
- Canonical IDs / Continuity: **100%**
- Producer / Consumer QA: **100%**
- Derived Predicates / Machine Contracts: **90%**
- Delayed Consequences: **100% runtime-verified**
- Replay / Meta-state: **100% source/contract; runtime transfer pending**
- Endings / precedence: **100% source/contract + CI; runtime resolution pending**
- Reachability / Causal Graph: **100% source-level**
- Production Data Schema: **36%**
- Runtime State / Persistence Foundation: **70%** — state boundary, authored execution, deterministic routing, delayed lifecycle, integrity-checked persistence and recovery are verified; full production determinism remains a downstream engine/release concern.
- Decision Engine: **15%** — real representative immediate execution, deterministic prerequisite routing, ten canonical delayed source executions and lifecycle gates are verified; full production engine semantics are not closed.
- UI / UX: **0%**
- Localization 20+: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **15%** — headless authored execution/routing and delayed lifecycle integration are GREEN; target gameplay and Android verification remain open.
- APK: **0%**
- Release: **0%**

Overall project progress is approximately **65%**. This remains an engineering estimate relative to the full production plan, not an arithmetic average of block percentages.

## NEXT ACTION
**Block 5 — continue the Endings + Precedence Resolver. Close the remaining authored ending producers, incoming-path coverage and P01–P30 runtime matrix. Block 6 persistence/determinism infrastructure is now available as a verified foundation and must be preserved against regressions.**

## Honest progress rule
Documentation alone never makes implementation complete. Every percentage requires authoritative evidence and the applicable verification. Source/contract GREEN must never be reported as runtime gameplay GREEN.
