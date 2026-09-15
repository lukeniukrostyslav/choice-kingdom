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

The authored producer bridge corrections for E136/E144/E148 and the later E151–E210 trigger/semantic corrections have been applied to the authoritative catalogs and re-read. E136-B supplies the upstream `history.guild_logistics_cooperation` marker and E194 consumes that upstream marker rather than self-consuming the qualified predicate. E29-A/B explicitly establish `pred.winter_severe` for the current severe-winter cycle while retaining `history.winter_severity_declared`. E32 explicitly establishes `pred.transport_disruption` for the compound-crisis cycle with `history.transport_disruption_declared`; E136-A/B are the primary recovery/clear sources and E192 is a consumer. The transport lifecycle is now source-reconciled; cycle identity, expiry, persistence, same-turn ordering and runtime evaluation remain OPEN. See `docs/TRANSPORT_DISRUPTION_RECONCILIATION_01.md`.

P0 reconciliation 06 freezes the guild-influence domain boundary, constitutional-preparation domain boundary, systemic-evidence qualification shape, coalition positive-outcome requirements, and budget-reform institutional layers. These remain source-level contracts, not runtime implementation. Guild influence cannot be manufactured from relationship score or duplicate representation events; constitutional preparation cannot count its consumer as its own prerequisite; coalition cooperation is distinct from package creation; and budget reform cannot collapse three institutional layers into one flag.

E273–E277 are now covered by a dedicated admission reconciliation. They remain **blocked from the frozen catalog** pending trigger normalization, producer/consumer closure, duplicate-producer analysis and full reachability/cycle verification. E277 is specifically blocked from becoming a competing generic transport-recovery producer while E136 remains the canonical frozen-cycle recovery bridge. See `docs/E273_E277_ADMISSION_RECONCILIATION_01.md`.

The border-crisis lifecycle is source-closed: E271-A declares the active crisis and E272-A/B resolve it while preserving historical declaration state. `thread.border` remains a legacy trigger context and must not be silently aliased to `thread.border_crisis`.

Delayed-consequence source extraction covers E127–E130/E141 plus E181–E185 and E242–E246 at the QA level. E128 has a verified upstream producer E17-A (`cheap_weapons`); E129 has a verified upstream producer E22-A (festival held); E127 has one verified upstream producer E06-B (`temporary_noble_exemption`) plus one unresolved alternate trigger route. E130 producer identity is now verified as E45-B (`infrastructure_concession`), and E141 producer identity is verified as E48-B (`emergency_renewal_possible`). Their delayed callback contracts still require immutable callback identity, exact timing semantics, cancellation/supersession, save/load persistence, replay isolation and deterministic ordering. E185 remains high-risk because its resolution depends on a later military crisis rather than a fixed turn count. See `docs/DELAYED_CONSEQUENCE_EXTRACTION_03.md`.

No validator has been introduced prematurely. Production schema and runtime implementation remain blocked until the canonical contracts are frozen and the complete catalog reconciliation passes.

## Latest source-level commits
- `e97d55aa7345048356b13da95a47f3bcdc5314fd` — E273–E277 admission/rejection reconciliation; all five candidates remain blocked pending graph/lifecycle gates.
- `9348e4530eb193d6e8fcf7d063e08aebe58370c6` — delayed consequence producer identity closure for E130/E141.
- `0237626eef0d67066f64f2f90697cf728765a0f2` — transport disruption lifecycle reconciliation E32/E136/E192 and E277 boundary.
- `0f89f64c3d07bd01e7fb803f4a0198ef5de79c46` — delayed callback producer refinement for E127–E130/E141.
- `c441a81a31261435748ef2679683e0fe2e6ac2aa` — delayed callback extraction 02; E181–E185 and E242–E246.
- `0b1d05edd18212355db1c475e7d5bbc3a7cb09b0` — canonical P0 reconciliation 06; guild/constitutional/evidence/coalition/budget boundaries and delayed-data gate.

## Current honest progress
- Foundation / rules: **95%**
- Authored content: **90%**
- Canonical Event IDs / continuity: **100%**
- Producer / Consumer QA: **83%**
- Derived predicates / machine contracts: **80%**
- Delayed Consequences: **70%**
- Replay / Meta-state: **42%**
- Endings / precedence: **52%**
- Reachability / causal graph: **36%**
- Production data schema: **35%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+ languages: **5%**
- Android implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress is approximately **46%**. This is not a simple average: prerequisite QA has advanced, but engine/UI/Android implementation has deliberately not started before the canonical contracts are safe to freeze.

## Next highest-value work
1. Finish delayed callback source extraction for the remaining unresolved producer/timing/cancellation cases, especially E127 alternate route and E185 conditional resolution.
2. Complete E273–E277 downstream consumer and cycle/reachability checks; admit only events that pass the gate.
3. Freeze replay meta-state transfer/isolation rules and ending qualification/precedence.
4. Re-run complete E01–E272 contradiction/cycle/reachability reconciliation and close dead-end/duplicate-trigger findings.
5. Freeze production data contracts.
6. Build the real static validator against the frozen schema.
7. Implement the actual Decision Engine and runtime.
8. Proceed to UI, localization, Android QA and APK only after the engine contracts are genuinely verified.

## Honest progress rule
Percentages represent actual state. Documentation alone does not make implementation complete. Source edits count only when the authoritative catalog is changed and re-read. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a source of readiness metrics.
