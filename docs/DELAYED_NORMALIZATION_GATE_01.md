# Choice Kingdom — Delayed Normalization Gate 01

Status: **SOURCE-LEVEL QA — NORMALIZATION GATE**  
Scope: E243, E245, E246; cross-check against E18, E125, E156, E160.

## Purpose

This gate converts the latest producer-candidate audit into explicit decisions that the future production catalog must satisfy. It does not silently rewrite authored semantics and does not mark delayed callbacks runtime-ready.

## E243 — The Old Bridge

Authored trigger: `public bridge investment`, 5+ turns later.

- E18-B is the exact authored source candidate: it creates `public_bridge` through the explicit choice to keep the bridge public.
- E45-A (`public_infrastructure_trust`) is not equivalent.
- E45-B (`infrastructure_concession`) is not equivalent.
- E224 (`river_safety_barriers`) is downstream safety investment and is not the original bridge-investment source.

**Required normalization:** E243 should consume an explicit canonical fact derived from E18-B, preferably `public_bridge` unless the production vocabulary deliberately chooses a more precise name. No generic public-infrastructure alias is allowed.

## E245 — The Soldier's Son Returns

Authored trigger: `compensation route`, 6+ turns later.

The current canonical catalog exposes two distinct compensation facts:

- E125-A → `border_compensation`
- E156-A → `requisition_compensation`

**Required authored decision:** choose exactly one of these models before production freeze:

1. E245 consumes one explicitly named compensation fact; or
2. E245 consumes an explicitly authored union of both facts.

The generic prose `compensation route` must not become a runtime wildcard. A relationship score, character route, or generic compensation wording cannot substitute for the declared producer set.

## E246 — The Price Ceiling Memory

Authored trigger: `price ceiling`, 5+ turns later.

- E160-A creates `winter_rent_ceiling`.
- No second exact price-control producer is currently source-closed.

**Required normalization:** either rename/normalize E160-A into the canonical price-control vocabulary or change E246's trigger to the exact `winter_rent_ceiling` fact. Silent aliasing is prohibited.

## Runtime lifecycle remains separate

Even after these normalization decisions, each callback still requires:

- stable `delayId`;
- source event + source choice;
- earliest turn;
- resolution target/condition;
- exactly-once key;
- priority;
- cancellation/supersession;
- save/load policy;
- replay isolation.

Producer identity alone does not make a delayed callback executable.

## Gate result

| Node | Current state | Production gate |
|---|---|---|
| E243 | exact source candidate E18-B | normalization required |
| E245 | exact candidate set E125-A/E156-A | authored single-source or union decision required |
| E246 | exact source candidate E160-A | vocabulary normalization required |

**Do not advance the Decision Engine gate from this document alone.** The canonical catalog and machine-readable contracts must be updated and re-read before runtime work begins.
