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

P0 reconciliation 06 freezes the guild-influence domain boundary, constitutional-preparation domain boundary, systemic-evidence qualification shape, coalition positive-outcome requirements, and budget-reform institutional layers. These remain source-level contracts, not runtime implementation. Guild influence cannot be manufactured from relationship score or duplicate representation events; constitutional preparation cannot count its consumer as its own prerequisite; coalition cooperation is distinct from package creation; and budget reform cannot collapse three institutional layers into one flag.

E273–E277 have now received a second admission audit. They remain outside the frozen catalog. E273–E276 have explicit authored producer semantics but still require complete consumer/lifecycle/alias checks; E277 overlaps the already canonical E136 transport-recovery route and cannot be admitted as a competing kingdom-wide recovery writer without an explicit lifecycle decision. See `docs/E273_E277_ADMISSION_AUDIT_02.md`.

The border-crisis lifecycle is source-closed: E271-A declares the active crisis and E272-A/B resolve it while preserving historical declaration state. `thread.border` remains a legacy trigger context and must not be silently aliased to `thread.border_crisis`.

Delayed-consequence source extraction covers E127–E130/E141 plus E181–E185 and E242–E246. E128 has verified upstream E17-A (`cheap_weapons`); E129 has verified upstream festival-held route; E130 is now closed to E45-B (`infrastructure_concession`); E141 is now closed to E48-B (`emergency_renewal_possible`). E127 still has one verified producer plus one unresolved alternate route. E181–E185 and E242–E246 have source/timing extraction but still require exact delay identity, cancellation/supersession, persistence and deterministic resolution contracts. See `docs/DELAYED_PRODUCER_CLOSURE_01.md`.

No validator has been introduced prematurely. Production schema and runtime implementation remain blocked until canonical contracts are frozen and the complete catalog reconciliation passes.

## Latest source-level commits
- `f2907e4e53ac4753c48b68801cc327c6c85671da` — closed source producer identities for E130/E141.
- `9c11d84d1de42da409521f3b45f693e9aa203d4a` — E273–E277 admission audit 02; candidates remain outside frozen production catalog.
- `d39970d64f019bf809ea83e9502afe6bcaa896fc` — previous project-state update.
- `0237626eef0d67066f64f2f90697cf728765a0f2` — transport disruption lifecycle reconciliation.
- `0f89f64c3d07bd01e7fb803f4a0198ef5de79c46` — delayed callback producer refinement.
- `0b1d05edd18212355db1c475e7d5bbc3a7cb09b0` — canonical P0 reconciliation 06.

## Current honest progress
- Foundation / rules: **95%**
- Authored content: **90%**
- Canonical Event IDs / continuity: **100%**
- Producer / Consumer QA: **85%**
- Derived predicates / machine contracts: **80%**
- Delayed Consequences: **73%**
- Replay / Meta-state: **42%**
- Endings / precedence: **52%**
- Reachability / causal graph: **38%**
- Production data schema: **35%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+ languages: **5%**
- Android implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress is approximately **47%**. This is still prerequisite-heavy work; no engine/UI/Android implementation is being counted as complete before the canonical contracts are genuinely verified.

## Next highest-value work
1. Complete E127 alternate producer reconciliation and remaining delayed lifecycle fields.
2. Finish E273–E276 consumer/alias graph checks and decide whether any candidate can be admitted without changing frozen semantics.
3. Freeze replay meta-state transfer/isolation rules and ending qualification/precedence.
4. Re-run complete E01–E272 contradiction/cycle/reachability reconciliation.
5. Freeze production data contracts.
6. Build the real static validator against the frozen schema.
7. Implement the actual Decision Engine and runtime.
8. Proceed to UI, localization, Android QA and APK only after the engine contracts are genuinely verified.

## Honest progress rule
Percentages represent actual state. Documentation alone does not make implementation complete. Source edits count only when the authoritative catalog is changed and re-read. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a source of readiness metrics.
