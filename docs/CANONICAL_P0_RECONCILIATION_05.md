# Choice Kingdom — Canonical P0 Reconciliation 05

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — NOT ENGINE INPUT**  
Scope: E01–E272; exact producer/consumer semantics for late constitutional and coalition gates.

## 1. Coalition cooperation — source qualification narrowed

### Evidence
- E148-A explicitly records participation from Mara, Rowan, Seris, Ivo, Amara and Toma and establishes immutable `history.cross_faction_package` plus `coalition_candidate_package`.
- E148-B establishes a deliberately selective route and must not qualify as the same cooperative package.
- The catalog explicitly states that `history.cross_faction_package` alone does not satisfy `pred.coalition_cooperation`; the predicate additionally requires cooperation evidence from at least three distinct faction identities and no unresolved coalition-collapse marker.
- E201 consumes `pred.coalition_cooperation` and does not create it.

### Contract result
**SOURCE QUALIFICATION: STRONG / CONDITIONALLY CLOSED.**

The minimum participant cardinality is not an inferred count: E148-A already records six named participants. The remaining runtime contract is to represent participant identities explicitly and evaluate the unresolved-blocker condition. `pred.coalition_cooperation` must not be aliased to `history.cross_faction_package`, `pred.faction_routes_4`, or a raw route count.

## 2. Budget reform — three independent institutional layers

### Evidence
- E142-A establishes `auditor_independence`; E142-B explicitly chooses continued Crown control and therefore must not qualify the independence layer.
- E154-A establishes `crown_audited`; E154-B establishes the negative state `crown_exempt_from_audit`.
- E198-A establishes `legislative_budget_lock`; E198-B establishes `executive_budget_override_retained`.

### Contract result
**SOURCE SET: CLOSED AS THREE DISTINCT LAYERS; DERIVED PREDICATE FORMULA: OPEN.**

A future `pred.budget_reform` contract may distinguish:
1. audit-office independence;
2. completed/accepted Crown audit;
3. legislative budget lock.

These must remain separate facts. No single choice, relationship score, or generic "audit reform" flag may substitute for the three layers. The exact boolean/cardinality formula and negative-blocker semantics remain an engine-contract decision and are therefore not invented here.

## 3. Guild influence strong — candidate domain freeze

The current canonical evidence separates merchant/guild influence into multiple institutional domains:
- E144: formal guild representation;
- E165: official-credit disclosure/private-credit route;
- E168: independent vs guild-controlled commercial tribunal;
- E169: labor standards vs strike suppression;
- E194: logistics cooperation with explicit inspection-risk state;
- E200 consumes `pred.guild_influence_strong` but does not create it.

### Contract result
**SOURCE DOMAINS IDENTIFIED; EXACT QUALIFYING SET OPEN.**

No relationship threshold such as `rel.ivo >= N` may manufacture the predicate. The final contract must select a minimum set of distinct institutional domains and define whether adverse outcomes invalidate the qualification. Until that is frozen, `pred.guild_influence_strong` remains OPEN.

## 4. Constitutional preparation strong — anti-circularity pass

Candidate upstream layers are now clearly separated:
- E142-A: independent auditors;
- E146-A/B: cross-character constitutional signatures;
- E148-A: cross-faction package with named participants;
- E150-A/B: explicit constitutional design test;
- E197 consumes `pred.constitutional_prepared_strong`.

### Contract result
**UPSTREAM DOMAIN SET IDENTIFIED; FORMULA OPEN.**

E197 cannot be its own prerequisite. The eventual predicate must consume only upstream facts and must not count a relationship score or the E197 choice itself. E148-A may contribute coalition evidence but must not silently substitute for every constitutional-preparation domain.

## 5. Systemic explanation verified — evidence identity freeze

E207 contains an explicit qualification requirement with four distinct evidence families:
1. warehouse/financial evidence;
2. document/language evidence;
3. witness/organizational evidence;
4. an explicit convergence decision.

### Contract result
**QUALIFICATION SHAPE: CLOSED; EXACT EVIDENCE IDS: OPEN.**

The predicate cannot be implemented as a raw clue count. Each family needs immutable evidence identifiers and the convergence decision must be a distinct state transition. Replay metadata must not satisfy current-run evidence unless explicitly promoted by a canonical rule.

## 6. Final charter prerequisites — acyclic boundary

E209 explicitly consumes `pred.final_charter_prerequisites` and requires upstream establishment of:
- civic/commons legitimacy;
- institutional/audit legitimacy;
- faction/house/guild representation;
- required military/security constitutional route;
- information/evidence legitimacy;
- coalition cooperation;
- absence of unresolved mandatory crisis blockers.

### Contract result
**DEPENDENCY BOUNDARY: CLOSED; EXACT PRODUCER FORMULA: OPEN.**

E209 is a consumer only. It cannot create or repair missing prerequisites. The final predicate must be a DAG over upstream authored state and must not depend on `thread.endgame_convergence` or E210 as a backdoor qualification.

## 7. Transport disruption — lifecycle boundary retained

E136-A/B are verified recovery/clear producers for `transport_disruption_active`; E32 is the current authored active producer in the canonical E01–E272 scope. E192 consumes the active predicate. E277 remains outside the frozen catalog and therefore cannot be silently substituted as an additional production source.

### Contract result
**SOURCE LIFECYCLE: CLOSED AT AUTHORED-SCOPE LEVEL; RUNTIME EXPIRY/PERSISTENCE OPEN.**

The engine must preserve the distinction between active disruption, recovered network, and historical recovery evidence.

## 8. E273–E277 admission remains blocked pending graph pass

The new candidate producers are not promoted merely because they fill named predicate gaps. Admission still requires upstream reachability, downstream consumer compatibility, semantic duplicate detection, contradictory-writer analysis, and interaction with the frozen E01–E272 graph. In particular, E277 must not compete with the E136 recovery contract without an explicit lifecycle rule.

## P0 gate result

| Contract | Source status |
|---|---|
| `pred.coalition_cooperation` | **STRONG / CONDITIONAL** |
| `pred.budget_reform` | **SOURCE LAYERS CLOSED / FORMULA OPEN** |
| `pred.guild_influence_strong` | **DOMAINS OPEN** |
| `pred.constitutional_prepared_strong` | **DOMAINS OPEN** |
| `pred.systemic_explanation_verified` | **SHAPE CLOSED / IDS OPEN** |
| `pred.final_charter_prerequisites` | **BOUNDARY CLOSED / FORMULA OPEN** |
| `pred.transport_disruption` | **SOURCE LIFECYCLE CLOSED / RUNTIME OPEN** |

**Production schema: BLOCKED.**  
**Decision Engine: BLOCKED by canonical contract gate.**  
**Runtime reachability: NOT VERIFIED.**
