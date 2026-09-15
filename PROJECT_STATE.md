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
**Narrative/content canonicalization and QA.** Authored checkpoint E01–E272. Production schema and Decision Engine remain blocked until canonical contracts and reachability are sufficiently closed.

## Scenario QA
Dedicated Scenario QA score is approximately **90%**. This is distinct from overall project completion and is not runtime/Android readiness.

### S01–S12 working indicators
- S01 **80%**
- S02 **70%**
- S03 **70%**
- S04 **70%**
- S05 **60%**
- S06 **58%** — authoritative choice-level closure for delayed E181–E183/E185/E243–E246 source evidence; runtime delayed lifecycle remains open.
- S07 **80%**
- S08 **78%**
- S09 **62%** — replay meta producer boundary audited; exact meta producer/key inventory remains open.
- S10 **74%** — authoritative source-choice closure for delayed E181/E243 routes; scheduler/runtime lifecycle remains open.
- S11 **60%** — ending prerequisite satisfiability screen plus conservative ending-precedence boundary contract; exact deterministic tie-break/terminal order remains open.
- S12 **90%** — machine scenario-QA gate matrix and predicate dependency/cycle boundaries are wired into canonical-graph CI. Runtime reachability remains unverified.

## Latest QA work
- **Ending Precedence Boundary 01:** added `docs/MACHINE_ENDING_PRECEDENCE_BOUNDARY_01.json`. It freezes conservative hard boundaries for all seven ending families, prevents support evidence from becoming final predicates, and explicitly leaves exact tie-break order, runtime evaluation order and terminal selection open. Commit `213289cf57dfbe6737043ea23c437f253c06dd87`.
- **Ending Precedence Boundary Validator:** added `tools/validate_ending_precedence_boundary.py`; fixed its list-comparison contract before CI wiring. Commit `e28ac148428db62c920978cbb868a22c792f97da`.
- **Canonical Graph CI:** `.github/workflows/canonical-graph.yml` now validates and uploads the ending-precedence boundary report. Commit `f0375fae6380fefc377eee82dbe6224af6e365e9`.
- **Machine Scenario QA Gate Matrix 01:** added `tools/validate_scenario_qa_gate_matrix.py` and `docs/MACHINE_SCENARIO_QA_GATE_MATRIX_01.json`. The validator freezes S01–S12 source-QA baselines, asserts hard runtime/reachability/precedence blockers, and prevents accidental promotion of scenario QA into runtime readiness. Commit `3aa46ab6a633968426f6691639b929c991d13c68`.
- **Canonical Graph CI Gate:** `.github/workflows/canonical-graph.yml` now executes the consolidated scenario-QA gate matrix and uploads its machine report together with predicate dependency validation. Commit `b665a7d80cd879165ef006315468e40c23013911`.
- **Predicate Dependency / Cycle Audit 01:** added `docs/SCENARIO_QA_PREDICATE_DEPENDENCY_CYCLE_AUDIT_01.md`. Screened composite predicates, delayed eligibility dependencies, replay boundaries and known hard negatives without promoting narrative consumers into producers. Commit `ccf68c83f5f128055bf56561ee04de7a545b9669`.
- **Machine Predicate Dependency Audit 01:** added `docs/MACHINE_PREDICATE_DEPENDENCY_AUDIT_01.json` with explicit open/closed predicate boundaries and delayed dependency identities. Commit `cf640dd0b8c1c43739f32727102ccf166004469c`.
- **Delayed Source Evidence Closure 02:** added `docs/SCENARIO_QA_DELAYED_SOURCE_EVIDENCE_CLOSURE_02.md`. Re-read authoritative E117/E118/E17/E20/E160 source entries and explicitly recorded exact choices for E182, E183, E185, E245 and E246, while preserving E184 as OPEN and E242 as PARTIAL. Commit `c69f41627473bb45ff56a3e68880edb981485213`.
- **Machine Delayed Source Tokens 01:** upgraded the delayed source-token contract to schema 1.1. Commit `b3b2b16dbd9ce219c4814abdfa051eed0682a2d5`.
- **Delayed Source Evidence Closure 01:** E181 source-choice closed to E45-B and E243 remains distinct at E18-B. Commit `4f19f59ff003824e3ebeb002475967b97095744e`.
- **Delayed Edge Closure Matrix 01:** promoted E181/E243 source-choice evidence while keeping runtime lifecycle fields open. Commit `20588cf8fbed14384d327cfdf1580cc52203d0f5`.
- **CI failure discovered and repaired:** `validate_delayed_inventory_scope.py` list/set bug repaired in commit `2982607b2ab0f23057c00984d9e7e4b89ca4bebf`.
- **Replay Meta Producer Audit 01:** E186/E247/E248/E249/E250/E270 audited against the five-field producer tuple; no complete producer promoted. Commit `546a1866c4a6d4eec4ccbf04738347e142cba2d0`.
- **Ending Prerequisite Satisfiability Audit 01:** all seven ending families audited for consumer-only prerequisites, circular/self-manufactured evidence, replay isolation and unsatisfied routes. Commit `e0cd54a247f2233ee4e4ee30e995c3dd0f2f9574`.

## Current canonical source status

### Source-closed delayed producers
- E18-B → `public_bridge` → E243
- E09-B → `flexible_accounts` → E244
- E117-B → `veteran_patronage` → E182
- E118-B → `estate_exception` → E183/E242
- E17-A → `cheap_weapons` → E185
- E160-A → `winter_rent_ceiling` → E246
- E136-B → `history.guild_logistics_cooperation` → E194
- **E20-A → `soldier_compensation` → E245**
- **E45-B → `infrastructure_concession` / toll-concession evidence → E181** (source-choice identity closed; executable lifecycle open)

### Predicate dependency status
- `pred.guild_influence_strong`: OPEN; explicit multi-domain producer remains required.
- `pred.systemic_explanation_verified`: OPEN; explicit convergence producer/key remains required.
- `pred.coalition_cooperation`: OPEN; support evidence cannot silently become final qualification.
- `pred.constitutional_prepared_strong`: OPEN; component ordering remains unresolved.
- `pred.budget_reform`: source-closed from three component predicates; runtime qualification remains open.
- `pred.final_charter_prerequisites`: OPEN/BLOCKED; E209 remains consumer-only.
- `pred.food_stable`: OPEN/BLOCKED; no safe producer alias is promoted.
- `pred.border_crisis`: source-closed lifecycle identity; runtime exactly-once/re-entry semantics remain open.

### Ending prerequisite status
- Steward: positive route candidates exist; blockers/precedence/fresh-run reachability OPEN.
- Iron Crown: authority/security support candidates exist; blockers/precedence/reachability OPEN.
- Golden Compact: economic/faction legitimacy candidates exist; blockers/precedence/reachability OPEN.
- People's Charter: **OPEN/BLOCKED** because E209 is consumer-only for `pred.final_charter_prerequisites`.
- Broken Diadem: failure routes exist; deterministic failure precedence OPEN.
- Quiet Throne: narrative withdrawal/stability route exists; blocker precedence OPEN.
- Second Founder: **OPEN/BLOCKED** by replay meta producer/key plus systemic convergence and fresh-run/replay separation.

### Replay meta status
Replay-sensitive nodes E186/E247/E248/E249/E250/E270 remain explicitly audited. No complete five-field replay producer tuple is currently closed; replay reachability and save/load isolation remain unverified.

## Major unresolved gates
- authoritative source recovery or explicit authored correction for E33/E34 exact headings/effects;
- `pred.food_stable` vs `food_logistics_stabilized`;
- exact executable producer compilation for `pred.guild_influence_strong`;
- explicit convergence producer/key for `pred.systemic_explanation_verified`;
- runtime qualification/invalidation for `pred.coalition_cooperation`;
- executable ordering for `pred.constitutional_prepared_strong`;
- `pred.final_charter_prerequisites`;
- replay `meta.*` producer/key inventory;
- remaining delayed cancellation/supersession rules;
- E184 producer closure and E185 crisis resolution;
- exact ending positive/negative prerequisite sets and deterministic tie-break/terminal order;
- exhaustive E01–E272 graph and fresh-run reachability;
- machine graph ↔ authoritative catalog semantic equality beyond ID parity.

## Current honest progress
- Foundation / rules: **95%**
- Authored content: **90%**
- Canonical Event IDs / Continuity: **100%**
- Producer / Consumer QA: **99%**
- Derived Predicates / Machine Contracts: **99%**
- Delayed Consequences: **98%**
- Replay / Meta-state: **67%**
- Endings / precedence: **74%**
- Reachability / Causal Graph: **64%**
- Production Data Schema: **36%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **60%**. Scenario QA remains approximately **90%**; S06 is **58%**, S09 is **62%**, S10 is **74%**, S11 is now **60%**, and S12 is **90%**. These source-QA percentages must not be conflated with overall project completion or runtime/Android readiness.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.
