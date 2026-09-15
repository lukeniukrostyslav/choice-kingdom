# Choice Kingdom — Delayed Graph Edge Audit 01

Status: **SOURCE-LEVEL QA — CORRECTED / E243 SOURCE-CLOSED, E245 OPEN**  
Scope: E243 and E245 delayed callbacks; compare design-level EVENT_GRAPH edges against exact authored producer semantics.

## Purpose

The event graph is a design-level causal candidate map. It must not be treated as proof that an upstream node produces the exact trigger consumed by a delayed callback. This audit checks graph edges against authored source vocabulary and distinguishes exact producers from merely related nodes.

## E243 — Old Bridge

**Callback trigger:** `public bridge investment`, 5+ turns later.

The graph contains candidate incoming edges:

- `E126 -> E243` — E126 produces `river_compact` or `royal_toll_office`; neither is the canonical public-bridge producer.
- `E129 -> E243` — E129 produces `festival_reported` or `festival_secret`; neither is the canonical public-bridge producer.
- `E181 -> E243` — E181 is itself a delayed toll callback and does not establish the public-bridge fact.
- `E224 -> E243` — E224 produces `river_safety_barriers`; this is bridge-related but is not the public-bridge investment fact.

**Source-closed producer:** E18-B explicitly establishes `public_bridge`.

**Canonical normalization:** E243's `public bridge investment` trigger may use `public_bridge` as its exact machine vocabulary. This is an explicit source-equivalent normalization, not a generic infrastructure/bridge alias.

**Gate:** producer identity is **SOURCE-CLOSED**. The graph edges above remain candidate causal relationships and must not be promoted to additional producers.

## E245 — Soldier's Son Returns

**Callback trigger:** `compensation route`, 6+ turns later.

The graph contains:

- `E117 -> E245` — E117-B produces `veteran_patronage`, not compensation.
- `E156 -> E245` — E156-A produces `requisition_compensation`, an explicit compensation fact in a specific requisition context.
- `E222 -> E245` — E222 is a veteran-family social-pressure event and does not itself produce a compensation marker.

Other authored compensation facts include:

- E20-A: `soldier_compensation`.
- E125-A: `border_compensation`.
- E156-A: `requisition_compensation`.

These must not be silently collapsed into a generic `compensation_route`.

**Gate:** producer identity remains **OPEN**. E156-A is a semantic candidate, not a confirmed exact producer for the generic callback.

## Consequence for production graph

1. Keep existing design-level edges as causal candidates unless contradicted by source.
2. Promote only exact source producers or explicitly contracted exact-equivalent normalizations into machine-readable prerequisites.
3. Preserve semantic distinctions between compensation contexts.
4. E243 may proceed to vocabulary-contract integration; E245 remains blocked from runtime delay registration until its producer semantics are closed.

## Verification rule

A delayed callback is source-closed only when an exact event ID + exact choice ID establishes the canonical trigger fact, or an explicit normalization contract intentionally maps an authored source fact to the callback trigger without semantic broadening.

## Gate result

- E243 producer: **SOURCE-CLOSED via E18-B → `public_bridge`**.
- E245 producer: **OPEN**.
- EVENT_GRAPH edges: **candidate relationships only**.
- Runtime implementation: **NOT STARTED**.

See `docs/DELAYED_GRAPH_EDGE_CORRECTION_01.md` for the correction record and `docs/DELAYED_PRODUCER_DECISION_MATRIX_01.md` for the source-level decision basis.
