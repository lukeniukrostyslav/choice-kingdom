# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Android-first, one-time purchase target €2.99–€4.99, no ads/subscription/mandatory backend for core gameplay, 20+ locales including RTL. Frozen production catalog: **E01–E272**. E273–E277 are expansion-only and excluded from production semantics/reachability.

## Development order
**Content → canonical QA → machine-readable contracts → Decision Engine → UI → localization/tests → Android QA → APK → release.** No mock/stub gameplay and no premature readiness claims.

## Current phase
**Scenario QA → runtime scenario verification.** S01–S12 are source/contract closed. Scenario-wide source/contract integration is GREEN. Runtime state/persistence, representative authored-choice execution, and the immediate-routing boundary are CI-verified. Full deterministic routing, delayed lifecycle, replay/meta, endings, and complete save/load/determinism remain downstream.

## S01–S12 source/contract scorecard
- S01 **100%** — frozen E01–E272 catalog/source inventory/structural reachability closure.
- S02 **100%** — authored choice → state/effect transition closure, CI-verified; representative runtime execution and immediate-routing boundary are GREEN.
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

### Runtime scenario core — GREEN
Repository inspection showed no existing Godot/runtime/persistence implementation to wrap at this boundary; the repository was still catalog/contracts/QA-only. A mock path was therefore not introduced.

Added:
- `runtime/__init__.py`
- `runtime/state.py` — versioned `GameState`, canonical five resources/six relationships, flags/history/threads, run-local pending delays, exactly-once delay resolution, E273–E277 rejection, JSON save/load boundary.
- `tests/test_runtime_state.py` — fresh-run isolation, save/load equivalence, exactly-once delays, condition-bound delay discipline, excluded-event rejection.
- `.github/workflows/runtime-scenario-core.yml`

GitHub Actions run **`35107430687`** completed **success** on 2026-09-16.

### Authored choice execution — REPRESENTATIVE RUNTIME GATE GREEN
Added:
- `runtime/catalog.py` — data-driven loader reading the catalog sources declared by `docs/MACHINE_CANONICAL_GRAPH_01.json`, frozen E01–E272 scope enforcement, authored A/B/C choice parsing, explicit immediate numeric deltas, relationship deltas, state tokens and conservative trigger checks. Special authored nodes without explicit player choices are preserved rather than fabricated.
- `runtime/engine.py` — real immediate authored choice execution against `GameState`, state/history/relationship/resource mutation, authored token clearing, choice history and explicit routing extraction. Delayed prose is deliberately not converted into invented timing.
- `tests/test_authored_choice_execution.py` — frozen catalog load, E01-A transition, E51-C three-way choice execution, E108-C shorthand preservation, excluded-event rejection, and delayed-unlock leakage protection.
- `.github/workflows/runtime-authored-choice-execution.yml` — source contract gate plus representative runtime execution tests and an explicit immediate-routing assertion.
- `.github/workflows/runtime-authored-choice-reverification.yml` — explicit PR/push re-verification gate retained after the special-node fix.

Verification findings and resolution:
- First runtime execution run **`35108060919`** failed on an overly strict loader assumption for authored special node E32 and then exposed a test cardinality/trigger issue.
- Defects were corrected in commits `c44630a7672ad42e97f0d9abdc072039c88ac300`, `dc4c6d09c7164b2b7c3b27529d0727e53d340fe8` and final special-node preservation fix `34fc65f2a17df03eccc254ff2341756ca223307e`.
- PR verification head `c3166a2859ec96ccf2c6889cb15b5863da8bdaf3` ran GitHub Actions job **`104841736814`** and completed **success** on 2026-09-16. Source-contract validation and representative runtime tests passed.
- Verification PR merged as `893b7331678254daea6659cf7a377fd26d140c75`; temporary marker removed in `7130ee508ca59454959701070df84762efc035d5`.

### Deterministic immediate routing boundary — GREEN
The initial runtime engine extracted any textual `unlock E###` reference, which incorrectly exposed delayed unlock prose as immediate routing. This was corrected so only explicit immediate `Unlock/Unlocks` directives are treated as immediate route signals; delayed prose remains owned by the delayed-lifecycle runtime.

- Commit `95254c52f56cae1492075746966df6cc24edd1ea` separated immediate routing from delayed unlock prose.
- Test commit `a90c6d07f0a85e76c475a3c5043f187db1588154` added an assertion that E01-A does not immediately route to its authored three-turn E07 unlock.
- PR **#7** verification head `1da5eb78eb7c4d4b292dd26bee1ba40f95b4176a` ran GitHub Actions job **`104842916343`** (`authored-choice-runtime`) and completed **success**; the dedicated routing assertion also completed **success**.
- PR #7 was merged as `2fc626ad414da3d04ad0536589c26f5454fcf878`; temporary routing marker removed in `a1b7e316bfe6affa06a5c17a3a804b1239b59196`.

This is still a **representative runtime boundary**, not a full Decision Engine. The canonical graph itself explicitly remains a source/design contract until each runtime edge has executable prerequisites and verified reachability.

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
- Runtime State / Persistence Foundation: **30%** — state boundary, representative authored execution, and immediate routing boundary are verified; full lifecycle/routing/determinism remains open.
- Decision Engine: **8%** — real representative immediate execution/routing boundaries exist and are CI-verified; full production engine semantics are not closed.
- UI / UX: **0%**
- Localization 20+: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **8%** — headless representative execution and routing are GREEN; full gameplay and Android verification remain open.
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **62%**. The runtime block percentages increased only for the verified execution/routing boundaries; the overall percentage is intentionally held at 62% until larger runtime gates close.

## NEXT ACTION
**Build deterministic routing from the canonical source contract for a representative chain beyond E01, with explicit authored prerequisites and no inferred graph semantics. Verify fresh-run isolation and repeated execution. Then extend the same machinery across the broader routing surface, followed by the ten frozen delayed lifecycle entries, replay/meta import boundary, ending resolver and complete save/load/determinism gates. If any runtime gate fails, fix the concrete failure before adding the next semantic layer. Do not promote Decision Engine production readiness until the complete runtime scenario gate is GREEN.**

## Honest progress rule
Documentation alone never makes implementation complete. Every percentage requires authoritative evidence and the applicable verification. Source/contract GREEN must never be reported as runtime gameplay GREEN.
