# Choice Kingdom — Delayed Producer Decision Matrix 01

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — OPEN / DECISION-READY**  
Scope: E184, E243, E245, E246

## Purpose

Freeze what can be safely normalized from authored evidence and explicitly preserve unresolved choices where multiple semantic producers exist.

| Consumer | Exact trigger wording | Strong candidate producer(s) | Safe normalization now? | Reason |
|---|---|---|---|---|
| E184 | `secret evidence route` | none source-closed | **NO** | No exact authored flag is established as the canonical secret-evidence producer. |
| E243 | `public bridge investment` | E18-B → `public_bridge` | **YES, source-equivalent** | E18-B explicitly establishes the public bridge state; no second canonical public-bridge investment marker is required by current evidence. |
| E245 | `compensation route` | E125-A → `border_compensation`; E156-A → `requisition_compensation` | **NO** | Both are compensation outcomes but are semantically distinct. Unioning them silently would broaden the callback trigger. |
| E246 | `price ceiling` | E160-A → `winter_rent_ceiling` | **CONDITIONAL** | The source meaning is specific to a winter rent ceiling. Renaming it to generic `price_ceiling` would be a semantic broadening. Prefer an explicit vocabulary alias only if the canonical contract defines that alias as exact-equivalent. |

## Required policy

### E243

A production contract may define E243's canonical trigger as `public_bridge` when it is explicitly documented as the exact normalized vocabulary for E18-B. This is not a generic `public_infrastructure` alias.

### E245

Do not implement `compensation_route = border_compensation OR requisition_compensation` without an explicit authored design decision. The two sources describe different compensation contexts. A safe implementation must either:

- select one exact source and keep the other separate; or
- introduce an explicitly authored composite predicate with named constituent evidence.

### E246

Do not treat every future price-control event as equivalent to E160-A. The current authored evidence is specifically `winter_rent_ceiling`. A generic `price_ceiling` consumer requires a documented normalization contract before runtime use.

### E184

No runtime prerequisite should be created until an exact source producer is identified or authored.

## Gate result

- E243: **candidate closure ready for canonical contract update**.
- E245: **semantic ambiguity intentionally preserved**.
- E246: **normalization required before runtime**.
- E184: **producer unresolved**.

No runtime code is changed by this document.
