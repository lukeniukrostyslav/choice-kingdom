# Choice Kingdom — Scenario QA S07 — E271–E272 Border-Crisis Lifecycle

Date: 2026-09-15  
Frozen production scope: **E01–E272**  
Expansion candidates E273–E277 remain excluded.

## Purpose

Close the source-level QA gap around the late-authored border-crisis lifecycle and reconcile E271–E272 with the existing E01–E270 catalog and causal graph without inventing runtime semantics.

## 1. Authoritative source

`docs/EVENT_CATALOG_EXPANSION_271_280.md` is the authoritative authored source for E271–E272.

E271-A explicitly declares the active border crisis; E271-B resolves the warning without declaring a crisis. E272-A/B resolve an already-declared active crisis while preserving the historical declaration.

## 2. Canonical lifecycle

| Lifecycle fact | Producer | Choice | Result | Status |
|---|---|---|---|---|
| `border_crisis_declared = true` | E271 | A | historical declaration | SOURCE-CLOSED |
| `border_crisis_resolved = false` | E271 | A | active lifecycle remains unresolved | SOURCE-CLOSED |
| `thread.border_crisis = active` | E271 | A | active crisis thread | SOURCE-CLOSED |
| `pred.border_crisis = active` eligibility | E271 | A | downstream crisis consumers become eligible | SOURCE-CLOSED |
| warning resolved without declaration | E271 | B | `thread.border_crisis = resolved_without_declaration` | SOURCE-CLOSED |
| `border_crisis_resolved = true` | E272 | A/B | crisis resolution | SOURCE-CLOSED |
| `border_crisis_declared = true` retained | E272 | A/B | historical fact preserved | SOURCE-CLOSED |
| `thread.border_crisis = resolved` | E272 | A | diplomatic resolution | SOURCE-CLOSED |
| `thread.border_crisis = resolved_under_security_guarantee` | E272 | B | security-guarantee resolution | SOURCE-CLOSED |
| clear `pred.border_crisis` | E272 | A/B | active predicate cleared | SOURCE-CLOSED |
| `history.border_crisis_resolved_diplomatically` | E272 | A | historical resolution marker | SOURCE-CLOSED |
| `history.border_crisis_resolved_by_guarantee` | E272 | B | historical resolution marker | SOURCE-CLOSED |

## 3. Hard-negative rules

The following substitutions are forbidden:

- `thread.border` alone → active `pred.border_crisis`;
- `pred.border_tension` alone → active `pred.border_crisis`;
- security level alone → active `pred.border_crisis`;
- E195/E253/E255 consumer reach → producer of the crisis;
- E271-B → active `pred.border_crisis`;
- E272 resolution → retroactive erasure of `border_crisis_declared`;
- `border_crisis_resolved` → proof that the crisis never existed.

The authored source explicitly assigns production authority to E271-A and resolution/clear authority to E272-A/B.

## 4. Cross-catalog reconciliation

Existing E151–E270 material treats E195, E253 and E255 as downstream crisis consumers. They must therefore remain consumers rather than alternative producers.

The existing `EVENT_GRAPH.md` currently stops its explicit expansion map at E270. This is a design-level documentation gap, not evidence that the authored E271/E272 nodes are absent. The graph needs explicit candidate edges for the new lifecycle:

- `E271-A -> pred.border_crisis(active)`;
- `pred.border_crisis(active) -> E195/E253/E255`;
- `E271-A -> E272` through the active crisis route;
- `E271-B` must not enter the active crisis route;
- `E272-A/B -> clear pred.border_crisis`;
- E272 historical resolution markers remain available for later authored consumers only if those consumers are explicitly sourced later.

No new downstream consumer is invented by this reconciliation.

## 5. Reachability boundary

Source-level causal prerequisites are closed for the authored pair:

1. E271 requires the authored border-warning conditions.
2. E271-A establishes the active crisis lifecycle.
3. E272 requires an active declared crisis plus an available resolution route.
4. E272-A/B resolve the active crisis.

Runtime reachability is **NOT VERIFIED** until the future engine can execute trigger evaluation, state mutation, save/load, turn ordering and resolution deterministically.

## 6. State and ending boundary

E271/E272 do not themselves manufacture constitutional, coalition, guild or systemic-evidence prerequisites. E272's numeric effects are ordinary state mutations (+5 reputation/+3 trust/-2 security for A; +5 security/-3 gold/-3 reputation for B), not hidden ending flags.

The historical declaration remains queryable, but no ending qualification is assigned here without an explicit authored consumer contract.

## 7. Result

- E271/E272 source inventory: **CLOSED at source level**.
- Border-crisis producer/consumer boundary: **CLOSED at source level**.
- Cross-catalog graph representation: **RECONCILED as a documentation correction**.
- Runtime lifecycle: **OPEN**.
- Save/load and exactly-once semantics: **OPEN**.
- Ending/replay qualification: **OPEN until explicit consumer/key contracts exist**.

## S07 status

**80% / IN PROGRESS**

This batch percentage is a working indicator. It does not increase the global Scenario QA metric by itself.
