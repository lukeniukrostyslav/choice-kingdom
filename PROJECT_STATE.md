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

## Current QA checkpoint
Producer inventories and static reachability pre-audits cover the authored scope E01–E272. The consolidated reachability matrix remains **OPEN** and is not a proof of runtime reachability.

The authored producer bridge corrections for E136/E144/E148 and the later E151–E210 trigger/semantic corrections have been applied to the authoritative catalogs and re-read. E136-B supplies the upstream `history.guild_logistics_cooperation` marker and E194 consumes that upstream marker rather than self-consuming the qualified predicate. E29-A/B explicitly establish `pred.winter_severe` for the current severe-winter cycle while retaining `history.winter_severity_declared`. E32 explicitly establishes `pred.transport_disruption` for the compound-crisis cycle with `history.transport_disruption_declared`; E136-A/B are the primary recovery/clear sources and E192 is a consumer. The transport lifecycle is source-reconciled; cycle identity, expiry, persistence, same-turn ordering and runtime evaluation remain OPEN. See `docs/TRANSPORT_DISRUPTION_RECONCILIATION_01.md`.

P0 reconciliation freezes the guild-influence domain boundary, constitutional-preparation domain boundary, systemic-evidence qualification shape, coalition positive-outcome requirements, and budget-reform institutional layers. These remain source-level contracts, not runtime implementation. Guild influence cannot be manufactured from relationship score or duplicate representation events; constitutional preparation cannot count its consumer as its own prerequisite; coalition cooperation is distinct from package creation; and budget reform cannot collapse three institutional layers into one flag.

E273–E277 remain outside the frozen catalog. Follow-up audits record exact source semantics for E273–E276 and explicitly reject silent aliases such as `rel.toma` -> `pred.information_pressure_high` or generic guild/food/market prose -> the new predicates. E273–E276 still require frozen consumer/lifecycle/reachability checks; E277 overlaps the canonical E136 transport recovery path and remains blocked.

The border-crisis lifecycle is source-closed: E271-A declares the active crisis and E272-A/B resolve it while preserving historical declaration state. `thread.border` remains a legacy trigger context and must not be silently aliased to `thread.border_crisis`.

Delayed-consequence source extraction covers E127–E130/E141 plus E181–E185 and E242–E246. Producer identity is source-closed for E181 (E45-B), E182 (E117-B), E183 (E118-B), E185 (E17-A) and E244 (E09-B). E242 has an explicit E118-B source but its full producer set remains open. E184 remains source-open. E243 has a closed exact candidate source E18-B (`public_bridge`) but requires canonical vocabulary normalization. E245 has candidate sources E125-A (`border_compensation`) and E156-A (`requisition_compensation`), but the two meanings are distinct and no union has been silently declared. E246 has E160-A (`winter_rent_ceiling`) as its exact semantic candidate and requires explicit normalization before runtime. See `docs/DELAYED_PRODUCER_DECISION_MATRIX_01.md`.

Replay mutable-state isolation is contract-closed at the design level: a new run starts with empty pending callbacks, active-cycle predicates, unresolved crises and run-local state; only explicitly authored `meta.*` transfer data may cross the replay boundary. A fresh source pass narrowed E186: its normal `warehouse_arson` route is distinct from the previous-run informational unlock wording. E247, E248 and E270 remain consumer intents without source-closed meta producers/keys. No ordinary flag or history marker has been promoted into meta-state. See `docs/REPLAY_META_SOURCE_CLOSURE_02.md`.

The ending qualification design contract is established: endings must be deterministic, predicate-based and causal; relationship scores, route counts and the last event cannot manufacture prerequisites. The seven current ending families and E265–E270 qualification roles are defined. A new producer-gap register separates qualification prose from actual source closure. Broken Diadem and Quiet Throne remain especially open because their deterministic failure/withdrawal producers are not frozen. See `docs/ENDING_PRODUCER_GAP_REGISTER_01.md`, `docs/ENDING_QUALIFICATION_CONTRACT_01.md` and `docs/ENDING_PRECEDENCE_TEST_MATRIX_01.md`.

Canonical scope wording has been reconciled: E35–E40 are canonical authored nodes because Act V explicitly continues the E01–E34 catalog. Their remaining work is downstream distinction/graph QA, not renumbering or exclusion. See `docs/CANONICAL_SCOPE_RECONCILIATION_01.md`.

No validator has been introduced prematurely. Production schema and runtime implementation remain blocked until canonical contracts are frozen and the complete catalog reconciliation passes.

## Latest source-level commits
- `32742d189975f70b29c1d6d2284f5ae0ba751eac` — ending producer gap register.
- `deba396de3cc71cc90852f50c184d83b724a6aca` — delayed producer decision matrix.
- `a5993eb86688866f053f85af883832b94f3a044c` — replay meta source closure 02.
- `a3d6612fdffb6350b0a47861a50de8b817c83ea0` — PROJECT_STATE update after delayed normalization gate.
- `ca9c2a677565d5a37c18587413659312bdd1cd2e` — delayed graph edge audit for E243/E245.
- `2420934160b0b1ff724dcb603d25a8824775ca7f` — corrected delayed consequence source closure 05.
- `3174407794accbc8a3b3140cd8da58b89b546279` — delayed producer disambiguation audit 01.
- `bc81332c7de13ffd6f637f3cd57fc904df864744` — deterministic ending precedence test matrix 01.
- `c5a22d69069ecb975809b2468bf1e3ec9713e980` — replay meta-state producer/consumer inventory audit.

## Current honest progress
- Foundation / rules: **95%**
- Authored content: **90%**
- Canonical Event IDs / continuity: **100%**
- Producer / Consumer QA: **95%**
- Derived predicates / machine contracts: **83%**
- Delayed Consequences: **87%**
- Replay / Meta-state: **57%**
- Endings / precedence: **63%**
- Reachability / causal graph: **44%**
- Production data schema: **35%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+ languages: **5%**
- Android implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **53%**. The increases reflect actual narrowing/closure of source-level QA gates and explicit producer-gap classification; they do not imply runtime readiness. Engine, UI and Android work remain unimplemented.

## Next highest-value work
1. Close exact source/normalization for E184, E243, E245 and E246 without semantic aliasing.
2. Resolve exact authored `meta.*` replay transfer producers/keys/consumers; do not infer them from ordinary flags.
3. Complete ending producer/path coverage and author deterministic priority data/fixtures.
4. Re-run complete E01–E272 contradiction/cycle/reachability reconciliation.
5. Freeze production data contracts and only then build the static validator.
6. Implement the actual Decision Engine and runtime.
7. Proceed to UI, localization, Android QA and APK only after engine contracts are genuinely verified.

## Honest progress rule
Percentages represent actual state. Documentation alone does not make implementation complete. Source edits count only when the authoritative catalog is changed and re-read. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a readiness source for Choice Kingdom.
