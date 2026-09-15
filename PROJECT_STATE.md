# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game. Working theme: ruling the kingdom of Avelune. The core appeal is meaningful choices, recurring characters, delayed consequences, hidden information, systemic event chains, multiple endings, and replayable paths.

## Full-release content target
This is a real full game, not a short card demo. The release target is approximately 250–350+ meaningful authored events/story nodes, with interconnected branches rather than filler repetition, plus approximately 8–12 recognizable endings and substantial replay variation.

## Commercial target
Android-first premium product, approximately €2.99–€4.99. No ads. No subscriptions. No mandatory backend or online service for core gameplay.

## Language requirement
Release must ship with localization from day one. Target is 20+ locales, including RTL and long-string validation.

## Engineering rule
No mock gameplay, fake completion, placeholder business logic presented as finished, or premature readiness claims. Every major block must progress through implementation, automated verification, runtime verification where applicable, and Android QA.

## Non-negotiable development order
Content and canonical QA come before production contracts, engine, UI, localization, automated/runtime verification and Android release.

## Current phase
**Narrative/content canonicalization and QA.** Authored checkpoint: E01–E272. Immediate goal: reconcile authored sources and causal graph into canonical production representation and prove internal consistency/reachability.

## Authored content checkpoints
- E01–E70: authored spine/endgame
- E71–E110: authored expansion
- E111–E150: authored expansion
- E151–E210: authored expansion
- E211–E270: authored expansion
- E271: border-crisis declaration producer bridge
- E272: border-crisis active-resolution producer bridge
- E273–E277: authored producer-expansion candidates, **not yet admitted to the frozen E01–E272 production catalog**
- Total frozen authored node identifiers: **E01–E272**.

## Scenario QA reporting metric
The dedicated scenario verification metric is frozen in `docs/SCENARIO_QA_SCORECARD_01.md`.

**Scenario QA / verification progress: 65%.**

This is the fixed reporting metric for the E01–E272 authored campaign. It measures closure of scenario QA gates (canonical continuity, producer/consumer closure, derived predicates, delayed consequences, replay boundaries, endings/precedence, causal reachability and exhaustive machine checks). It is intentionally distinct from the overall project percentage.

The 65% figure does not mean the engine, runtime, Android build, UI, localization or APK are complete. It also does not mean reachability has been proven.

## Latest QA work
- **S12** added `docs/SCENARIO_QA_S12_FRESH_RUN_REPLAY_REACHABILITY_AUDIT_01.md` in commit `4c867ff7884b1bce464d41a6bef7980a400bba41`; translated fresh-run/replay isolation into explicit reachability invariants, enumerated currently source-backed path anchors, classified blocked/open paths, and defined the machine-check requirements for E01–E272. S12 remains partial because exhaustive event-by-event reachability is not yet proven.
- **S11** added `docs/SCENARIO_QA_S11_ENDING_INCOMING_PRECEDENCE_AUDIT_01.md` in commit `8919e0acc3e0d93d35e647346cbe5a8da08fa07f`; audited ending qualification as a causal consumer graph, rejected consumer-as-producer and generic-score aliases, and left complete incoming-path/precedence closure open for final-charter, coalition-positive, Broken Diadem and Quiet Throne routes.
- **S10.5** added `docs/SCENARIO_QA_S10_5_DELAYED_LIFECYCLE_PERSISTENCE_AUDIT_01.md` in commit `acb51e3fd916c6acd433ccfd636730adadaad128`; closed the semantic QA boundary for transport lifecycle, food-pressure handling, late-crisis lifecycle, save/load persistence and replay isolation while keeping executable delayed contracts open pending exact source extraction.
- **S10.4** added `docs/SCENARIO_QA_S10_4_DELAYED_SOURCE_TARGET_RECONCILIATION_01.md` in commit `cefee161d039d6ec6a71914c29806847381a0847`; reconciles delayed source identities for E181–E185 and E242–E246 against producer chronology while keeping unresolved timing/exactly-once/cancellation semantics open.
- **S09.8** added `docs/SCENARIO_QA_S09_8_NORMALIZED_DEPENDENCY_GRAPH_AUDIT_01.md` in commit `28e62d38ff7846d654e9a4053872d79a274b548c`; normalized the closed producer→fact/lifecycle→consumer graph and hard-rejected self-satisfaction, alias leakage and E273–E277 contamination.
- **S09.7** added `docs/SCENARIO_QA_S09_7_CATALOG_PRODUCER_RECONCILIATION_01.md` in commit `46da737a74c3cd66b8deb9bfef710609385634fb`; re-read authoritative E01–E272 catalog surfaces and reconciled producer families and late consumer boundaries.
- S09.6 added `docs/SCENARIO_QA_S09_6_COMPOSITE_PREDICATE_PRODUCER_ENUMERATION_01.md`, commit `2668004a3a52b6c6d80ef7e45345b0d3fd6a41e1`.
- S09.5 added `docs/SCENARIO_QA_S09_5_NORMALIZED_DEPENDENCY_EDGE_INVENTORY_01.md`, commit `c505b79ef9dc1675be144a7db69f5a290db18e55`.
- S09.4 added `docs/SCENARIO_QA_S09_4_PREDICATE_CYCLE_SELF_SATISFACTION_AUDIT_01.md`, commit `f64a47baaeadd1c2a65006e4386c0b016d9eeeeb`.
- S09.3 reconciled `docs/CANONICAL_DERIVED_PREDICATE_CONTRACT_01.md`, commit `5cb193cfa5d97a340bbab202c842737342538262`.
- S09.2 added `docs/SCENARIO_QA_S09_2_SCOPE_CONTRADICTION_AUDIT_01.md`, commit `c4d58020e4202c5a5aea7fb454d3ee012d2e715a`.
- S09.1 predicate dependency pre-audit added as `docs/SCENARIO_QA_S09_1_PREDICATE_DEPENDENCY_PREAUDIT_01.md`, commit `3a9c2aaa9599671df3ef8410bbb4428b6798e17e`.
- S08.10 producer chronology pre-audit added as `docs/SCENARIO_QA_S08_10_PRODUCER_CHRONOLOGY_PREAUDIT_01.md`, commit `a8beccf42802a5664b7b990ff72c02ea540a0982`.

## Current QA checkpoint
The producer inventory is paired with `docs/MACHINE_INVENTORY_PASS_01.md`, which freezes the current source-closed fact set and separates runtime-safe normalization from unresolved producer ambiguity. This remains source-level QA, not runtime data.

The authored producer bridge corrections for E136/E144/E148 and later E151–E210 trigger/semantic corrections have been applied to authoritative catalogs and re-read. E136-B supplies `history.guild_logistics_cooperation`; E194 consumes that upstream marker rather than self-consuming the qualified predicate. E29-A/B establish `pred.winter_severe`; E32 establishes `pred.transport_disruption` and E136-A/B are the primary recovery/clear sources. Runtime lifecycle, persistence and ordering remain OPEN.

S09.8 provides a normalized closed dependency surface. The closed graph rejects consumer-as-producer, recovery-to-active leakage, unsafe aliases and all E273–E277 edges. Full transitive proof remains open because composite predicates, delayed identities and replay/meta nodes are not fully closed.

S10.4 materially narrowed delayed source ambiguity: E182 is tied to E117-B, E183 to E118-B, E185 to E17-A, E243 to E18-B, E244 to E09-B, and E246 to E160-A conditionally. E181 is retained as E45-B. E184 remains source-open; E242 partial; E245 open; E247/E248 replay/meta-open. Relative `4+`, `5+`, `6+` timing remains evidence only until executable earliest-turn/window semantics are frozen.

S10.5 established the semantic lifecycle/persistence boundary for E32/E136 transport, E218/E225 food pressure and E251–E272 late-crisis families. It requires callback identity, earliest-turn/window semantics, resolution target, exactly-once, cancellation/supersession, save/load persistence and replay reset before runtime closure. No guessed timing or target was promoted.

S11 established the ending causal boundary. Endings are consumers of independently qualified state; E209 remains consumer-only, E210 convergence-only, E261 does not automatically qualify coalition cooperation, generic relationship/resource/route counts cannot substitute for explicit prerequisites, and E273–E277 remain excluded. Complete incoming-path and deterministic precedence closure remains open, especially for final-charter, coalition-positive, Broken Diadem and Quiet Throne routes.

S12 established the fresh-run/replay reachability boundary. A fresh run starts without pending callbacks, active-cycle predicates, unresolved callback state or prior-run-only flags. Only explicitly authored `meta.*` replay seeds may cross the boundary. Source-backed anchors include E18-B→E243, E09-B→E244, E117-B→E182, E118-B→E183/E242, E17-A→E185, E136-B→E194, E32→E192, E271-A→border-crisis consumers and E272-A/B resolution history. These are candidate paths, not end-to-end runtime proof. Composite predicates, replay meta producers, negative ending routes and exact late-crisis callback timing remain blockers.

`pred.food_stable` remains blocked with no in-scope producer. `pred.transport_disruption` has E32 as active producer and E136-A/B as recovery/clear sources. Composite guild influence, constitutional preparation, systemic explanation, coalition cooperation and budget reform remain partial/open where exact source sets, thresholds, chronology or invalidation are not fully compiled.

No validator has been introduced prematurely. Production schema and runtime implementation remain blocked until canonical contracts are frozen and complete catalog reconciliation passes.

## Current honest progress
- Foundation / rules: **95%**
- Authored content: **90%**
- Canonical Event IDs / continuity: **100%**
- Producer / Consumer QA: **97%**
- Derived predicates / machine contracts: **84%**
- Delayed Consequences: **88%**
- Replay / Meta-state: **57%**
- Endings / precedence: **63%**
- Reachability / causal graph: **45%**
- Production data schema: **36%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+ languages: **5%**
- Android implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **53%**. The separate scenario QA metric is **65%** and must not be conflated with this overall project figure.

## Next highest-value work
1. Continue S10 delayed/lifecycle reconciliation for E218/E225 and E251–E272, with E32/E136 persistence/expiry semantics.
2. Complete S11 ending incoming-path enumeration and deterministic precedence where authoritative catalog evidence permits closure.
3. Expand S12 from source-backed anchors into an exhaustive machine-readable E01–E272 reachability inventory.
4. Finish derived predicate contracts and exact canonical vocabulary, including food stability, transport lifecycle, guild influence, constitutional preparation and coalition cooperation.
5. Freeze production contracts only after evidence is clean enough for machine validation.
6. Build the Decision Engine against frozen contracts, then UI, localization, automated/runtime verification and Android release gates.

## Honest progress rule
Percentages represent actual state. Documentation alone does not make implementation complete. Source edits count only when the authoritative catalog is changed and re-read. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a readiness source for Choice Kingdom.
