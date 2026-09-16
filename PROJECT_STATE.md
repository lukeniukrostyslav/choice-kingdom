# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Android-first, one-time purchase target €2.99–€4.99, no ads/subscription/mandatory backend for core gameplay, 20+ locales including RTL. Frozen production catalog: **E01–E272**. E273–E277 are expansion-only and excluded from production semantics/reachability.

## Development order
**Content → canonical QA → machine-readable contracts → Decision Engine → UI → localization/tests → Android QA → APK → release.** No mock/stub gameplay and no premature readiness claims.

## Current phase
**Scenario QA → runtime scenario verification → delayed consequence lifecycle.** S01–S12 are source/contract closed. Scenario-wide source/contract integration is GREEN. Runtime state/persistence, representative authored-choice execution, deterministic immediate routing, and the delayed lifecycle core are CI-verified. Broader deterministic routing, full delayed consequence gameplay integration, replay/meta, endings, and complete save/load/determinism remain downstream.

## S01–S12 source/contract scorecard
- S01 **100%** — frozen E01–E272 catalog/source inventory/structural reachability closure.
- S02 **100%** — authored choice → state/effect transition closure, CI-verified; representative runtime execution and immediate-routing boundary are GREEN.
- S03 **100%** — producer/consumer source closure.
- S04 **100%** — predicate contracts source-closed; frozen exclusions machine-gated.
- S05 **100%** — ten frozen delayed callbacks E181–E185 and E242–E246 source/contract closed; runtime lifecycle core now CI-verified, full gameplay resolution downstream.
- S06 **100% source/contract** — E186/E247/E248 replay/meta contract closed; runtime replay downstream.
- S07 **100%** — source causal graph closed and CI-verified; runtime reachability downstream.
- S08 **100%** — source/producer QA closed and CI-verified.
- S09 **100%** — canonical graph source closure closed and CI-verified.
- S10 **100%** — delayed lifecycle source/contract surface closed; runtime lifecycle core CI-verified, full authored resolution downstream.
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
- `runtime/state.py` — versioned `GameState`, canonical five resources/six relationships, flags/history/threads, run-local pending delays, exactly-once delay resolution, observable cancellation/supersession state, E273–E277 rejection, JSON save/load boundary.
- `tests/test_runtime_state.py` — fresh-run isolation, save/load equivalence, exactly-once delays, condition-bound delay discipline, excluded-event rejection.
- `.github/workflows/runtime-scenario-core.yml`

GitHub Actions run **`35107430687`** completed **success** on 2026-09-16.

### Authored choice execution — REPRESENTATIVE RUNTIME GATE GREEN
Added:
- `runtime/catalog.py` — data-driven loader reading the catalog sources declared by `docs/MACHINE_CANONICAL_GRAPH_01.json`, frozen E01–E272 scope enforcement, authored A/B/C choice parsing, explicit immediate numeric deltas, relationship deltas, state tokens and conservative trigger checks. Special authored nodes without explicit player choices are preserved rather than fabricated.
- `runtime/engine.py` — real immediate authored choice execution against `GameState`, state/history/relationship/resource mutation, authored token clearing, choice history, explicit routing extraction, and canonical delayed scheduling after successful choice effects.
- `tests/test_authored_choice_execution.py` — frozen catalog load, representative E01→E02 routing, E51-C three-way choice execution, E108-C shorthand preservation, excluded-event rejection, delayed-unlock leakage protection, and prerequisite route guards.
- `.github/workflows/runtime-authored-choice-execution.yml` — source contract gate plus representative runtime execution tests and explicit immediate-routing assertion.
- `.github/workflows/runtime-authored-choice-reverification.yml` — explicit PR/push re-verification gate retained after the special-node fix.

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
- PR #8 merged as **`50f1c63d7d6bbc0fac6273bf21d6c260d17ec5c9`**.

**Block 2 result: 🔒 100% runtime-verified.** This closes the deterministic authored prerequisite routing boundary represented by the current runtime contract; it does not claim that the entire 272-event graph is already a fully executable production engine.

### Delayed consequence lifecycle — BLOCK 3 RUNTIME CORE GREEN / BROADER INTEGRATION OPEN
Implemented:
- `runtime/delays.py` — ten canonical delay specifications for E181–E185 and E242–E246, exact source-choice identities, relative earliest-turn offsets, exactly-once keys, condition-bound E185, and deterministic due ordering.
- `runtime/state.py` — persistent pending-delay representation plus observable cancellation and supersession statuses.
- `runtime/engine.py` — authored delay scheduling after successful choice state mutation, with no invented timing for condition-bound delays.
- `tests/test_delayed_lifecycle_runtime.py` — ten-row identity, source-choice parity, relative scheduling, earliest-turn resolution, condition-bound resolution, cancellation, supersession, save/load persistence, and fresh-run isolation.
- `.github/workflows/delayed-lifecycle-gate.yml` — canonical source gate plus runtime lifecycle tests.

Verification:
- PR **#9** runtime gate executed against merge commit `385905ab8aa7ce90b1ff2f0f7c78926be759e9e9`.
- GitHub Actions run **`35117949659`**, job **`104868082250`**, completed **success** on 2026-09-16.
- Source gate: `{"errors": 0, "readiness": "CLOSED", "warnings": 0}`.
- Runtime lifecycle gate: **13 passed in 0.04s**.
- Canonical graph gate on the same PR completed **success** as run `35117949564`, job `104868081473`.
- PR #9 merged as **`da68b49c1edb2bbcb21ba13b3df39595fb0bb1e4`**.

**Important boundary:** Block 3 is not marked fully closed yet. The verified runtime core proves lifecycle mechanics and the ten frozen identities, but full gameplay integration still requires executing the actual authored source choices for the affected events and resolving the target consequences under their authored qualification conditions. No guessed cancellation or timing semantics are permitted.

## Major blocks
- Foundation / Rules: **95%**
- Authored Content: **90%**
- Canonical IDs / Continuity: **100%**
- Producer / Consumer QA: **100%**
- Derived Predicates / Machine Contracts: **90%**
- Delayed Consequences: **80%** — canonical ten-row lifecycle identity + runtime scheduling/resolution mechanics are GREEN; full authored gameplay integration remains open.
- Replay / Meta-state: **100% source/contract; runtime transfer pending**
- Endings / precedence: **100% source/contract + CI; runtime resolution pending**
- Reachability / Causal Graph: **100% source-level**
- Production Data Schema: **36%**
- Runtime State / Persistence Foundation: **40%** — state boundary, authored execution, deterministic routing boundary, delayed scheduling/lifecycle core are verified; full runtime determinism remains open.
- Decision Engine: **12%** — real representative immediate execution, deterministic prerequisite routing, and delayed lifecycle core exist and are CI-verified; full production engine semantics are not closed.
- UI / UX: **0%**
- Localization 20+: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **12%** — headless authored execution/routing and delayed lifecycle core are GREEN; full gameplay and Android verification remain open.
- APK: **0%**
- Release: **0%**

Overall project progress is approximately **64%**. This remains an engineering estimate relative to the full production plan, not an arithmetic average of block percentages. It increased only after the verified runtime routing and delayed-lifecycle core gates.

## NEXT ACTION
**Complete Block 3 authored gameplay integration: execute each of the ten canonical delayed source choices through the real `DecisionEngine`, verify the pending-delay record against the machine contract, advance to exact earliest-turn eligibility where applicable, resolve each target without duplicate execution, and verify E185 only through its authored later-military-crisis condition. Then add explicit negative tests for premature resolution and cross-run delay leakage. Only after that GREEN should Block 3 be closed and Block 4 Replay / Meta-State runtime transfer begin.**

## Honest progress rule
Documentation alone never makes implementation complete. Every percentage requires authoritative evidence and the applicable verification. Source/contract GREEN must never be reported as runtime gameplay GREEN.
