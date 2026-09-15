# Choice Kingdom — Delayed Graph Edge Correction 01

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — CORRECTION APPLIED**  
Scope: stale graph-audit wording for E243; E245 remains intentionally unresolved.

## Why this correction exists

`docs/DELAYED_GRAPH_EDGE_AUDIT_01.md` was authored before the later delayed-producer decision matrix. It still reports E243 as producer **OPEN**. The newer source-level decision matrix establishes that E18-B explicitly produces `public_bridge` and that this is safe to use as the canonical normalized vocabulary for E243's `public bridge investment` callback.

This correction does **not** change E245, E184 or E246.

## E243 — canonical normalization

- Consumer: **E243 Old Bridge**
- Authored callback wording: `public bridge investment`, 5+ turns later.
- Exact source producer: **E18-B**.
- Authored source fact: `public_bridge`.
- Normalization: `public_bridge` is the canonical machine vocabulary for this callback trigger.
- Scope: exact-equivalent normalization only; it must not be broadened to `public_infrastructure`, `river_safety_barriers`, `infrastructure_concession`, or any generic bridge-related fact.

The existing candidate graph edges remain design-level causal relationships only. They do not become exact trigger producers merely because they point into E243.

## E245 — unchanged

E245 consumes `compensation route`, but current authored evidence contains distinct compensation facts including E125-A `border_compensation` and E156-A `requisition_compensation`. These cannot be silently unioned into one generic trigger. E245 remains **OPEN** pending an explicit authored normalization decision or a single exact source selection.

## E184 / E246 — unchanged

- E184 `secret evidence route`: no source-closed producer; remains OPEN.
- E246 `price ceiling`: E160-A `winter_rent_ceiling` is an exact semantic candidate, but generic `price_ceiling` normalization remains conditional until explicitly contracted.

## Required graph rule

Design-level EVENT_GRAPH edges are not runtime prerequisites by themselves. Runtime trigger satisfaction must reference the canonical producer vocabulary and its exact source event/choice identity.

## Gate result

- E243 producer: **SOURCE-CLOSED / NORMALIZATION READY** via E18-B → `public_bridge`.
- E245 producer: **OPEN / AMBIGUOUS**.
- E184 producer: **OPEN**.
- E246 normalization: **CONDITIONAL**.
- Runtime delayed-consequence implementation: **NOT STARTED**.
