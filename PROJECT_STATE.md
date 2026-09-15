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

The authored producer bridge corrections for E136/E144/E148 and the later E151–E210 trigger/semantic corrections have been applied to the authoritative catalogs and re-read. E136-B supplies the upstream `history.guild_logistics_cooperation` marker and E194 consumes that upstream marker rather than self-consuming the qualified predicate. E29-A/B now explicitly establish `pred.winter_severe` for the current severe-winter cycle while retaining `history.winter_severity_declared`; this closes the winter-severity producer gap at source level. E32 now explicitly establishes `pred.transport_disruption` for the compound-crisis cycle with `history.transport_disruption_declared`; E136/E277 remain recovery/clear sources and E192 remains a consumer. Runtime predicate evaluation and deterministic cycle expiry remain unimplemented.

P0 reconciliation 06 further freezes the guild-influence domain boundary, constitutional-preparation domain boundary, systemic-evidence qualification shape, coalition positive-outcome requirements, and budget-reform institutional layers. These remain source-level contracts, not runtime implementation. Guild influence cannot be manufactured from relationship score or duplicate representation events; constitutional preparation cannot count its consumer as its own prerequisite; coalition cooperation is distinct from package creation; and budget reform cannot collapse three institutional layers into one flag.

The remaining high-risk producer gaps are still not allowed to be invented in the engine layer. Food stability, guild labor tension and high information pressure now have explicit authored source candidates in E273–E277, but those nodes remain outside the frozen catalog until scope admission, upstream reachability, downstream consumer and duplicate-producer checks are complete. Budget reform, final-charter convergence, delayed consequence identity/timing/cancellation, replay metadata and ending precedence also remain open.

The border-crisis lifecycle is source-closed: E271-A declares the active crisis and E272-A/B resolve it while preserving historical declaration state. `thread.border` remains a legacy trigger context and must not be silently aliased to `thread.border_crisis`.

The latest delayed-consequence extraction identifies explicit timed callback groups including E127–E130, E141, E181–E185 and E242–E246. These are QA candidates, not production delay records, until source choice IDs, resolution targets, exactly-once identities and cancellation/supersession rules are frozen.

No validator has been introduced prematurely. Production schema and runtime implementation remain blocked until the canonical contracts are frozen and the complete catalog reconciliation passes.

## Latest source-level commits
- `0b1d05edd18212355db1c475e7d5bbc3a7cb09b0` — canonical P0 reconciliation 06; guild/constitutional/evidence/coalition/budget boundaries and delayed-data gate.
- `a96a5182739db91341961a875156e89ae9c594f5` — canonical P0 reconciliation 05; narrowed coalition, budget, guild-influence, constitutional-preparation, systemic-evidence and final-charter contracts.
- `d60287e6dc0b954ff068f4042e592a9fbc2239c3` — canonical P0 reconciliation 04; formalized border lifecycle closure and E273–E277 admission boundaries.
- `f59537c6deb2a96eb1275cca255b152a93e6ee39` — delayed consequence extraction 01; identified explicit timed callback groups and remaining production-data gaps.
- `692a04f59abf38a41d58d780b027806a853a7f24` — E273–E277 scope admission gate 01.

## Next highest-value work
1. Compile exact authored source IDs for systemic evidence and final-charter prerequisites.
2. Extract delayed consequence identity/timing/cancellation/supersession event-by-event.
3. Reconcile E32 transport-disruption lifecycle, reachability and persistence semantics.
4. Complete E273–E277 admission/rejection graph pass.
5. Freeze replay meta-state and ending qualification/precedence.
6. Re-run complete E01–E272 contradiction/cycle/reachability reconciliation.
7. Freeze production data contracts.
8. Build the real static validator against the frozen schema.
9. Implement the actual Decision Engine and runtime.
10. Proceed to UI, localization, Android QA and APK only after the engine contracts are genuinely verified.

## Honest progress rule
Percentages represent actual state. Documentation alone does not make implementation complete. Source edits count only when the authoritative catalog is changed and re-read. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a source of readiness metrics.
