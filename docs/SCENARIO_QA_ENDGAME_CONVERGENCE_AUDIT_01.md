# Choice Kingdom — Scenario QA Endgame Convergence Audit 01

Status: **SOURCE-LEVEL QA — BOUNDED ENDGAME AUDIT**  
Scope: E01–E272 production semantics only.  
Date: 2026-09-15.

## Purpose

Strengthen the scenario foundation around the endgame without inventing missing ending contracts. This audit reconciles the authored event graph with the current canonical producer/consumer boundaries and identifies exactly what can and cannot yet be promoted to deterministic ending qualification.

## 1. Canonical ending families currently authored

The campaign graph names seven ending families:

- Steward
- Iron Crown
- Golden Compact
- People's Charter
- Broken Diadem
- Quiet Throne
- Second Founder

The graph describes these as endgame outcomes and identifies their thematic support conditions, but it does **not** by itself constitute an executable ending predicate or precedence contract.

Therefore the existence of seven authored families is CLOSED at narrative-description level, while executable ending qualification remains OPEN.

## 2. Endgame convergence spine

The current design graph establishes the following authored convergence sequence:

`E261 -> E262/E263/E264/E265`

`E263 -> E265/E266`

`E264 -> E265/E267`

`E265 -> ending qualification`

and separately:

`E266/E267/E268/E269/E270 -> ending qualification / ending support families`

This proves that the endgame is intentionally convergent rather than seven isolated linear campaigns. It does **not** prove that every ending is reachable in a fresh run, nor that every prerequisite combination is satisfiable.

## 3. Hard separation: support vs qualification

The following are treated as **support evidence only** until explicit contracts are authored:

- `E267` support for Iron Crown / Steward / People's Charter depending on history;
- `E268` support for Steward / Golden Compact / People's Charter depending on history;
- `E269` support for Golden Compact / Second Founder / legitimacy;
- `E270` support for Second Founder / coalition / information qualification.

A support marker must not silently become a final ending predicate.

Similarly, `four_way_bargain` from E261 cannot by itself satisfy `pred.coalition_cooperation`; the existing hard-negative remains authoritative.

## 4. Existing blockers that directly affect ending qualification

### 4.1 Final charter prerequisites

`pred.final_charter_prerequisites` remains OPEN. E209 is explicitly consumer-only. Candidate upstream events are not an executable convergence contract.

### 4.2 Coalition cooperation

`pred.coalition_cooperation` remains PARTIAL. It requires positive cooperation, participant identity, and absence of an unresolved collapse blocker. No generic faction count may substitute for this contract.

### 4.3 Systemic explanation

`pred.systemic_explanation_verified` remains PARTIAL / producer-open. E232–E236 expose evidence domains, but no single explicit convergence producer/key has been established.

### 4.4 Replay qualification

Replay callbacks E186/E247/E248/E270 remain isolated from ordinary history until an explicit `meta.*` producer contract exists.

### 4.5 Reachability

The design graph is explicitly a causal candidate map, not a proof of fresh-run or replay reachability. No ending may be declared reachable solely because an incoming design edge exists.

## 5. Required deterministic ending contract before engine promotion

For each ending family, the canonical contract must eventually identify:

1. `ending_id`;
2. positive prerequisite predicates/facts;
3. mandatory negative blockers;
4. whether prerequisites are current-state, historical, replay-meta, or delayed-state facts;
5. minimum evidence/route requirements;
6. precedence when multiple endings qualify simultaneously;
7. whether the ending is mutually exclusive with another family;
8. fresh-run reachability proof;
9. representative replay reachability where replay is required;
10. deterministic fallback for unresolved/failed qualification.

Until all ten are source-backed and verified, ending readiness remains below production-engine threshold.

## 6. Branch-protection rule preserved

The existing narrative rule remains: critical endings should have at least two independent ways to satisfy major prerequisites. This is a design requirement, not yet a verified reachability result.

No single character choice, single event, or single delayed callback may be assumed to make an ending reachable or unreachable without simulation evidence.

## 7. E33/E34 isolation

No ending contract in this audit depends on inventing E33/E34 semantics. Their authoritative headings/effects remain quarantined under the existing source-recovery audit.

## 8. Promotion decision

| Area | Current status | Promotion decision |
|---|---|---|
| Seven ending families named | CLOSED at narrative-description level | May remain canonical as authored families |
| Endgame convergence map | SOURCE-VISIBLE | Keep as design-level causal candidates |
| Ending predicates | OPEN | Do not promote |
| Ending precedence | OPEN | Do not promote |
| Fresh-run ending reachability | OPEN | Do not promote |
| Replay ending reachability | OPEN | Do not promote |
| Final charter prerequisite | OPEN | Do not promote |
| Coalition cooperation | PARTIAL | Do not promote as final ending gate |
| Systemic explanation | PARTIAL | Do not promote as final ending gate |

## QA conclusion

The endgame narrative structure is materially defined, but deterministic ending qualification is not yet closed. This audit narrows the remaining work to explicit ending contracts, precedence, and reachability rather than allowing design-level support edges to masquerade as runtime-ready ending logic.

No Decision Engine implementation is authorized by this document.
