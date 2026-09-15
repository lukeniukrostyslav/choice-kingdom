# Choice Kingdom — Delayed Producer Candidate Closure 01

Status: **SOURCE-LEVEL QA — CANDIDATE SET RECONCILIATION**
Scope: E243, E245, E246.

## Purpose

This pass narrows unresolved delayed callbacks to the smallest authored producer sets visible in the canonical catalog. It does **not** promote semantic candidates into runtime prerequisites. Exact normalization remains an authored-contract decision.

## E243 — The Old Bridge

**Authored trigger:** `public bridge investment`, 5+ turns later.

### Candidate source

- **E18-B — The River Toll / Keep the bridge public** establishes `public_bridge` and spends treasury on keeping the bridge public.
- E45-A establishes `public_infrastructure_trust`, but that marker describes public infrastructure legitimacy rather than the bridge investment itself and is therefore **not** an exact producer.
- E45-B establishes `infrastructure_concession`, which is the opposite ownership/concession route and is **not** an exact producer.
- E224 concerns bridge safety barriers and is downstream safety investment, not the original public bridge investment.

### Closure decision

E18-B is the **sole exact authored semantic candidate identified** for E243's public-bridge prerequisite. The production contract should normalize E243 to an explicit machine-readable source such as `public_bridge` rather than retain the prose trigger `public bridge investment`.

This is a source-normalization decision, not permission to treat every public-infrastructure event as equivalent.

## E245 — The Soldier's Son Returns

**Authored trigger:** `compensation route`, 6+ turns later.

### Candidate producer set

- **E125-A — Border Families / Compensate them** establishes `border_compensation`.
- **E156-A — The Widow's Petition / Pay full compensation** establishes `requisition_compensation`.

These are distinct authored compensation facts. No evidence supports collapsing them into one generic `compensation_route` fact.

### Closure decision

E245 currently has a **closed candidate producer set but no single producer**. The production contract must choose one of two explicit models:

1. E245 consumes exactly one canonical compensation fact; or
2. E245 consumes an authored union of `border_compensation` and `requisition_compensation`.

The second model must be explicitly authored because a generic semantic alias would otherwise broaden reachability silently.

## E246 — The Price Ceiling Memory

**Authored trigger:** `price ceiling`, 5+ turns later.

### Candidate source

- **E160-A — The Price of a Warm Room / Temporary rent ceiling** establishes `winter_rent_ceiling`.

No other exact `price ceiling` producer is currently source-closed in the inspected catalog.

### Closure decision

E160-A is the exact semantic candidate, but the source vocabulary still needs normalization. The production catalog should either:

- rename the E160-A marker to an explicitly canonical price-control fact, or
- change E246's trigger to consume `winter_rent_ceiling`.

The runtime must not silently alias `price ceiling` to `winter_rent_ceiling`.

## Result

| Node | Producer status | Exact next action |
|---|---|---|
| E243 | Candidate set closed to E18-B | Normalize trigger to `public_bridge` |
| E245 | Candidate set closed to E125-A / E156-A | Author exact single-source or explicit union semantics |
| E246 | Candidate identified as E160-A | Normalize `price ceiling` vocabulary |

## Hard gate

These findings improve producer coverage but do not make any callback runtime-ready. Delay identity, exactly-once behavior, cancellation/supersession, resolution conditions, save/load policy and deterministic priority remain required before engine implementation.
