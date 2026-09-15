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

Delayed-consequence source extraction covers E127–E130/E141 plus E181–E185 and E242–E246. Producer identity is now source-closed for E127, E128, E129, E130 and E141: E127 is produced through E06-B (`temporary_noble_exemption`) and E38-A (`hereditary_seats_limited`); E128 through E17-A; E129 through E22-A; E130 through E45-B; E141 through E48-B. Remaining delayed work is executable delay identity/timing/cancellation/persistence rather than producer invention. See `docs/DELAYED_CONSEQUENCE_EXTRACTION_02.md` and `docs/DELAYED_PRODUCER_CLOSURE_01.md`.

Replay mutable-state isolation is contract-closed at the design level: a new run starts with empty pending callbacks, active-cycle predicates, unresolved crises and run-local state; only explicitly authored `meta.*` transfer data may cross the replay boundary. The exact authored `meta.*` transfer inventory remains OPEN. See `docs/REPLAY_META_STATE_CONTRACT_01.md` and `docs/CANONICAL_DELAY_REPLAY_ENDING_AUDIT_01.md`.

The ending qualification design contract is established: endings must be deterministic, predicate-based and causal; relationship scores, route counts and the last event cannot manufacture prerequisites. The seven current ending families and E265–E270 qualification roles are defined. A new source-level audit confirms E265–E270 are supporting endgame nodes rather than proof of ending reachability; complete producer/path coverage and final precedence tests remain OPEN. See `docs/ENDING_QUALIFICATION_CONTRACT_01.md` and `docs/ENDING_PATH_COVERAGE_AUDIT_01.md`.

Canonical scope wording has been reconciled: E35–E40 are canonical authored nodes because Act V explicitly continues the E01–E34 catalog. Their remaining work is downstream distinction/graph QA, not renumbering or exclusion. See `docs/CANONICAL_SCOPE_RECONCILIATION_01.md`.

No validator has been introduced prematurely. Production schema and runtime implementation remain blocked until canonical contracts are frozen and the complete catalog reconciliation passes.

## Latest source-level commits
- `89812501201e...` — ending path coverage audit E265–E270.
- `6ea98c0f34f069c59b26a113b6a52fefd45865ed` — canonicalization backlog scope clarification.
- `b04271583ac2ba29456e5619e644195e3a10d8c9` — canonical scope reconciliation E35–E40.
- `e597736d8ca48d357e5fb78dc4ea7c9712c84d61` — corrected delayed producer closure and project progress.
- `2a270b243fc286cd00ac851055eea2d8b24da53c` — corrected delayed consequence extraction E127–E141.
- `b4a4b8fe714e215ebcece5cd3917350ab09ec949` — freeze replay meta-state isolation contract.
- `4e674404a82149ef6c162b6955531dd35fae31fd` — delay/replay/ending contract audit.
- `9c11d84d1de42da409521f3b45f693e9aa203d4a` — E273–E277 admission audit 02.
- `0237626eef0d67066f64f2f90697cf728765a0f2` — transport disruption lifecycle reconciliation.
- `0b1d05edd18212355db1c475e7d5bbc3a7cb09b0` — canonical P0 reconciliation 06.

## Current honest progress
- Foundation / rules: **95%**
- Authored content: **90%**
- Canonical Event IDs / continuity: **100%**
- Producer / Consumer QA: **90%**
- Derived predicates / machine contracts: **82%**
- Delayed Consequences: **80%**
- Replay / Meta-state: **55%**
- Endings / precedence: **58%**
- Reachability / causal graph: **40%**
- Production data schema: **35%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+ languages: **5%**
- Android implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **50%**. Recent work closes documentation/source inconsistencies and sharpens QA gates; it does not count runtime implementation as complete.

## Next highest-value work
1. Normalize remaining executable delay fields for E127–E130/E141 and E181–E185/E242–E246.
2. Complete E273–E276 consumer/alias graph checks and decide admission without changing frozen semantics.
3. Inventory all authored `meta.*` replay transfer producers and consumers.
4. Complete ending producer/path coverage and deterministic precedence tests for E265–E270 and the seven ending families.
5. Re-run complete E01–E272 contradiction/cycle/reachability reconciliation.
6. Freeze production data contracts and only then build the static validator.
7. Implement the actual Decision Engine and runtime.
8. Proceed to UI, localization, Android QA and APK only after engine contracts are genuinely verified.

## Honest progress rule
Percentages represent actual state. Documentation alone does not make implementation complete. Source edits count only when the authoritative catalog is changed and re-read. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a readiness source for Choice Kingdom.
