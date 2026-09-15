# Choice Kingdom — Delayed Graph Edge Audit 01

Status: **SOURCE-LEVEL QA — OPEN / CONTRADICTION CANDIDATES**  
Scope: E243 and E245 delayed callbacks; compare design-level EVENT_GRAPH edges against exact authored producer semantics.

## Purpose

The event graph is a design-level causal candidate map. It must not be treated as proof that an upstream node produces the exact trigger consumed by a delayed callback. This audit checks the graph edges against the authored source vocabulary and deliberately preserves unresolved edges as OPEN.

## E243 — Old Bridge

**Callback trigger:** `public bridge investment`, 5+ turns later.

The current graph contains these candidate incoming edges:

- `E126 -> E243` — E126 produces `river_compact` or `royal_toll_office`; neither is an explicit `public bridge investment` fact.
- `E129 -> E243` — E129 produces `festival_reported` or `festival_secret`; neither is a bridge-investment fact.
- `E181 -> E243` — E181 is itself a delayed toll callback and does not establish a public bridge-investment fact.
- `E224 -> E243` — E224 concerns bridge safety barriers and produces `river_safety_barriers`; this is semantically related to a bridge but is not automatically a public-investment marker.

Known bridge/infrastructure facts include:

- E18-B: `public_bridge`.
- E45-A: `public_infrastructure_trust`.
- E45-B: `infrastructure_concession`.
- E126-A: `river_compact`.
- E224-A: `river_safety_barriers`.

None is silently promoted to `public bridge investment` in this audit.

**Gate:** producer identity remains **OPEN**. The graph edges above are candidate relationships, not source-closed producers.

## E245 — Soldier's Son Returns

**Callback trigger:** `compensation route`, 6+ turns later.

The graph contains:

- `E117 -> E245` — E117-B produces `veteran_patronage`, not compensation.
- `E156 -> E245` — E156-A produces `requisition_compensation`, which is an explicit compensation fact but concerns requisitioned winter animals.
- `E222 -> E245` — E222 is a veteran-family social-pressure event and does not itself produce a compensation marker.

Other authored compensation facts exist, including:

- E20-A: `soldier_compensation`.
- E125-A: `border_compensation`.
- E156-A: `requisition_compensation`.

These must not be collapsed into a generic `compensation_route` without an explicit authored normalization decision.

**Gate:** producer identity remains **OPEN**. E156-A is a semantic candidate, not a confirmed exact producer.

## Consequence for production graph

1. Do not delete the existing design-level edges solely because they are not source-closed.
2. Do not promote them into machine-readable prerequisites until exact source facts are identified.
3. The production graph must distinguish causal proximity from exact trigger satisfaction.
4. E243/E245 remain blocked from runtime delay registration until producer identity and callback lifecycle are closed.

## Verification rule

A delayed callback is source-closed only when an exact event ID + exact choice ID establishes the canonical trigger fact, or an explicit normalization contract intentionally maps an authored source fact to the callback trigger without semantic broadening.

## Gate result

- E243 producer: **OPEN**
- E245 producer: **OPEN**
- EVENT_GRAPH edges reviewed: **candidate only**
- Runtime implementation: **NOT STARTED**
