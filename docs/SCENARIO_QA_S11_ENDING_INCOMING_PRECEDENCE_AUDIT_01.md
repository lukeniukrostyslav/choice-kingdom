# Choice Kingdom — Scenario QA S11 Ending Incoming-Path / Precedence Audit 01

Date: 2026-09-15  
Status: **PARTIAL PASS — SOURCE/CONTRACT QA**  
Frozen production scope: **E01–E272**  
Expansion candidates: **E273–E277 excluded**

## Purpose

Audit ending qualification as a causal consumer graph before runtime implementation. This pass does not invent ending producers or turn unresolved narrative relationships into predicates.

## Non-negotiable ending rule

An ending is a consumer of independently qualified state. It cannot manufacture its own prerequisites merely because its event is reachable.

Required qualification dimensions remain distinct:

- civic/commons preparation;
- institutional/audit preparation;
- faction/house/guild preparation;
- military/security preparation where applicable;
- information/evidence legitimacy;
- explicit coalition cooperation and positive outcome;
- unresolved mandatory crisis blockers;
- deterministic precedence where multiple endings are simultaneously eligible.

## Canonical hard negatives

| Candidate shortcut | Disposition |
|---|---|
| E209 produces `pred.final_charter_prerequisites` for itself | **REJECTED** — consumer-only |
| E210 convergence/reachability manufactures missing prerequisites | **REJECTED** — convergence-only |
| E261 `four_way_bargain` automatically proves coalition cooperation | **REJECTED** |
| generic relationship score substitutes for institutional qualification | **REJECTED** |
| generic resource/route count substitutes for an explicit ending prerequisite | **REJECTED** |
| unresolved border crisis silently ignored by ending evaluation | **REJECTED** unless the authored ending explicitly permits it |
| E273–E277 supplies an ending prerequisite in frozen production | **REJECTED** |

## Known source-backed upstream layers

The currently closed graph contains independently sourced institutional layers such as E199-A military constitutional evidence, E142-A auditor independence, E154-A crown audited and E198-A legislative budget lock. These are upstream evidence only; they do not automatically constitute the complete final-charter or ending contract.

The canonical QA state also identifies E144-A/B guild representation, E148-A cross-faction package and E136-B guild logistics cooperation as source-backed domains. Their use in an ending requires the authored ending consumer to name the appropriate predicate/domain rather than relying on generic route counts.

## Broken Diadem / Quiet Throne

These endings remain **OPEN** because deterministic failure/withdrawal producer sets are not frozen. The audit therefore forbids promoting a generic low-score, relationship collapse or unreachable route into an ending producer without authoritative catalog evidence.

## Incoming-path matrix status

| Ending gate | Incoming-path status | Current disposition |
|---|---|---|
| final charter / positive constitutional ending | partial | exact complete upstream producer set still open |
| coalition-positive ending | partial | explicit coalition cooperation producer set still open |
| military/security ending | partial | E199-A is source-backed evidence; full consumer qualification open |
| audited/institutional ending | partial | E142-A/E154-A/E198-A source layers exist; complete ending rule open |
| Broken Diadem | open | deterministic failure/withdrawal producers not frozen |
| Quiet Throne | open | deterministic withdrawal/negative qualification not frozen |

## Precedence requirements

Before runtime implementation, each ending must define a deterministic precedence relation or mutually exclusive eligibility contract. The engine must not resolve simultaneous eligibility by file order, event ID order, dictionary iteration, random choice, or UI ordering.

Required precedence evidence:

1. explicit authored priority where supplied;
2. otherwise mutually exclusive predicates;
3. otherwise an explicit deterministic tie-break contract approved during canonical freeze.

No implicit priority is inferred in this pass.

## Replay interaction

Ending evaluation is run-local unless an ending predicate is explicitly authored as `meta.*`. A new replay must not inherit unresolved crises, pending callbacks or active ending prerequisites from the previous run. E247/E248/E270 remain meta/open consumers and cannot be used as hidden ending prerequisites without source-closed meta producers.

## Gate result

**S11 PARTIAL PASS.** The causal ending boundary is now explicit and the major self-satisfaction/alias shortcuts are rejected. Complete incoming-path enumeration and deterministic precedence remain open, especially for final-charter, coalition-positive, Broken Diadem and Quiet Throne routes.

**S11 remains 55%. Scenario QA remains 65%.**

## Next autonomous block

1. Build S12 fresh-run causal reachability audit from the normalized dependency surface.
2. Enumerate ending incoming paths and precedence only where authoritative catalog evidence can close them.
3. Return to S10 unresolved late-crisis rows where direct source evidence is available.
4. Do not promote production schema or Decision Engine until the canonical contract gate is closed.
