# Choice Kingdom — Scenario QA Worklog

Frozen scope: **E01–E272**  
Expansion candidates: **E273–E277 excluded**  
Purpose: durable handoff ledger so completed QA work is not repeated.

## Latest continuation update — 2026-09-15

### S09.6 — composite predicate producer enumeration
- Added `docs/SCENARIO_QA_S09_6_COMPOSITE_PREDICATE_PRODUCER_ENUMERATION_01.md` in commit `2668004a3a52b6c6d80ef7e45345b0d3fd6a41e1`.
- Enumerated the currently source-supported producer domains for `pred.guild_influence_strong`, `pred.constitutional_prepared_strong`, `pred.systemic_explanation_verified`, `pred.coalition_cooperation`, `pred.budget_reform`, `pred.final_charter_prerequisites`, `pred.food_stable` and `pred.transport_disruption`.
- Explicitly preserved E209 as consumer-only, E210 as convergence-only, and rejected consumer-as-producer/self-satisfaction patterns.
- Preserved the E01–E272 production boundary and zero production contribution from E273–E277.
- Confirmed `pred.food_stable` remains BLOCKED because no E01–E272 producer is source-closed; E192 food logistics stabilization is not silently aliased into kingdom-wide food stability.
- Confirmed E32 as the active `pred.transport_disruption` producer and E136-A/B as recovery/clear sources; reactivation/lifecycle semantics remain open.
- Composite predicates remain PARTIAL/OPEN until exact authored source tokens, thresholds, chronology and invalidation semantics are exhaustively compiled.
- No percentage increase: S09 remains **60%** and global Scenario QA remains **65%**.

### S09.5 — normalized dependency edge inventory
- Added `docs/SCENARIO_QA_S09_5_NORMALIZED_DEPENDENCY_EDGE_INVENTORY_01.md` in commit `c505b79ef9dc1675be144a7db69f5a290db18e55`.
- Compiled the first normalized source-backed producer → fact/lifecycle → consumer edge surface using only already-admitted E01–E272 facts.
- Explicitly separated active predicate producers from clear/recovery edges and preserved historical-vs-current lifecycle boundaries.
- Hard-rejected E209/E200/E197/E207 self-satisfaction, coalition-thread self-qualification, recovery-to-active leakage and all E273–E277 production edges.
- Closed source edges include E18-B→public_bridge→E243, E09-B→flexible_accounts→E244, E117-B→veteran_patronage→E182, E118-B→estate_exception→E183, E136-B→guild logistics→E194, E148-A→cross-faction package, E19 market-pressure lifecycle, E29 winter producer, E32 transport producer/E136 recovery, E271/E272 border lifecycle, E199 military constitutional evidence, and E142/E154/E198 budget-reform source layers.
- Composite predicates remain partial/open where exact independent source IDs, thresholds, lifecycle or chronology are not fully compiled.
- `pred.final_charter_prerequisites` remains BLOCKED until its complete upstream producer set is exhaustively enumerated; E209 is explicitly consumer-only.
- No percentage increase: S09 remains **60%** and global Scenario QA remains **65%**.

### S09.4 — predicate cycle / self-satisfaction audit
- Added `docs/SCENARIO_QA_S09_4_PREDICATE_CYCLE_SELF_SATISFACTION_AUDIT_01.md` in commit `f64a47baaeadd1c2a65006e4386c0b016d9eeeeb`.
- Isolated the registry-level self-satisfaction risk caused by inclusive wording `E197/E198/E199/E202–E209 candidates` for `pred.final_charter_prerequisites`.
- Required disposition: E209 is consumer-only and cannot produce its own prerequisite.
- Preserved hard negatives for E200/E197/E207 and relationship/coalition aliases.
- Full token-level dependency extraction and machine cycle detection remain open.

### S09.2 — frozen-scope contradiction audit
- Added `docs/SCENARIO_QA_S09_2_SCOPE_CONTRADICTION_AUDIT_01.md` in commit `c4d58020e4202c5a5aea7fb454d3ee012d2e715a`.
- Found a material contradiction: the frozen producer registry/S08 chronology rejects E273-A as a production producer for `pred.food_stable`, while an older derived-predicate contract still listed E273-A as a closed producer and declared scope E01–E277.
- Confirmed the project-level scorecard and contract-closure records continue to freeze production at E01–E272; E273–E277 remain expansion candidates.
- Confirmed the P0 authored patchset is a specification/checklist and does not prove that the authoritative event catalog has been patched.
- Preserved the safe disposition: E273–E277 cannot satisfy E01–E272 producer lookups; `pred.food_stable` remains OPEN/BLOCKED until an in-scope producer is verified or the authoritative catalog is explicitly changed and re-read.
- No percentage was increased merely for documenting the contradiction. S09 remains **60%** and global Scenario QA remains **65%**.

### S09.1 — predicate dependency pre-audit
- Added `docs/SCENARIO_QA_S09_1_PREDICATE_DEPENDENCY_PREAUDIT_01.md`, commit `3a9c2aaa9599671df3ef8410bbb4428b6798e17e`.
- Started the predicate dependency gate using only source-closed facts; no design-level event-graph edge was promoted into runtime truth.
- Explicitly rejected self-satisfaction patterns for `pred.final_charter_prerequisites`, `pred.guild_influence_strong`, `pred.constitutional_prepared_strong`, `pred.systemic_explanation_verified` and `pred.coalition_cooperation` without an independently proven upstream seed.
- Preserved hard negatives for relationship aliases, coalition thread, security-vs-border-crisis, food stability and excluded E273–E277 sources.
- S09.1 is a PARTIAL PASS; exhaustive token-level dependency extraction and machine cycle detection remain open.

### S08.10 — producer chronology pre-audit
- Added `docs/SCENARIO_QA_S08_10_PRODUCER_CHRONOLOGY_PREAUDIT_01.md` in commit `a8beccf42802a5664b7b990ff72c02ea540a0982`.
- Converted source-closed producer families into explicit producer-before-consumer chronology gates.
- Confirmed source ordering for E32 → E192 transport consumption, E32 → E136 recovery, E136-B → E194 guild logistics qualification, E29-A/B → later winter consumers, and E271/E272 → downstream border-crisis lifecycle consumers.
- Marked guild influence, constitutional preparation, coalition cooperation and final-charter chronology as PARTIAL/OPEN because exact exhaustive source IDs and independent-domain qualification are not yet frozen.
- Added explicit duplicate/contradictory-writer boundaries and preserved hard E273–E277 rejection.
- S08.10 is a PARTIAL PASS, not an exhaustive closure claim.

### S08.9 — source reconciliation: food and transport lifecycle
- Added `docs/SCENARIO_QA_S08_9_SOURCE_RECONCILIATION_01.md` in commit `beb8c93e8e4e95c2fb62ab90e4cf36f0e46f7e4b`.
- Reconciled S08.8 against the authoritative late-predicate audit and prevented downstream consumers from being promoted into producers.
- Confirmed `pred.food_stable` remains OPEN: E167/E218 are response/consumer candidates and E192 writes logistics outcomes, not a safe kingdom-wide stability predicate.
- Confirmed `pred.transport_disruption` lifecycle is partially closed: E32 is the active producer and E136-A/B are recovery/clear sources; no later E01–E272 reactivation producer is source-closed.
- Preserved guild-influence, constitutional-preparation and coalition cooperation as partial independent-domain contracts with chronology/producer checks still required.
- S08/S09/S10 remain IN PROGRESS; production schema remains BLOCKED.

### S08.8 — source closure audit: food, transport and route activation
- Added `docs/SCENARIO_QA_S08_8_SOURCE_CLOSURE_AUDIT_01.md` in commit `1378318513cca1f88b8ee2c310b7228b5e145a2b`.
- Kept `pred.food_stable` OPEN: E192-B contains a food-stability effect, but no reusable canonical durable marker is source-closed; E273-A remains excluded.
- Confirmed transport recovery/clear through E136-A/B while keeping the later disruption producer OPEN.
- Reconciled endgame route activation families: military constitutional evidence is strong via E199-A; Amara/Toma/final constitutional activation remain partial/open pending exact authored route markers.
- Preserved hard negatives and the E01–E272 scope filter.
- S08 remains IN PROGRESS; production schema remains BLOCKED.

### S08.7 — domain qualification audit
- Added `docs/SCENARIO_QA_S08_7_DOMAIN_QUALIFICATION_AUDIT_01.md` in commit `90694d5529d3df89556d79d54fca386c5d67c99b`.
- Closed the qualification-domain boundaries for guild influence, constitutional preparation, systemic explanation, coalition cooperation, final charter prerequisites and four-faction route counting without inventing unresolved producers.
- Preserved hard negatives: `rel.ivo` alone cannot qualify guild influence; `thread.coalition`/`four_way_bargain` alone cannot qualify coalition cooperation; consumers cannot manufacture prerequisites; aliases cannot double-count one institutional domain.
- Confirmed `pred.budget_reform` source set: E142-A `auditor_independence`, E154-A `crown_audited`, E198-A `legislative_budget_lock`; chronology/reachability/negative-branch/replay verification remains open.
- S08 remains IN PROGRESS; production schema remains BLOCKED.

### S08.6 — closure matrix for remaining producer/consumer surface
- Added `docs/SCENARIO_QA_S08_CLOSURE_MATRIX_01.md` in commit `dc7de03cf29a20e6359d0feb3c63fa5c51b9c847`.
- Converted the current registry into an explicit closed/open matrix for the remaining canonical producer/consumer families.
- Confirmed source-closed families including guild representation, guild logistics cooperation, house assembly, cross-faction package, people charter endorsement, winter severity and the E271/E272 border-crisis lifecycle.
- Added mandatory machine-check gates for producer completeness, consumer completeness, frozen-scope integrity, duplicate semantic outputs, contradictory writers, legacy-vocabulary normalization, predicate cycles and delayed-source lifecycle completeness.

### S08.5 — canonical producer registry scope hardening
- Corrected `docs/CANONICAL_PRODUCER_CONSUMER_REGISTRY_01.md` in commit `5eb8f961deee382802bfd915c38cbb0b74181ebf`.
- Replaced the stale E273 food-stability producer reference with explicit **NO IN-SCOPE PRODUCER VERIFIED**.
