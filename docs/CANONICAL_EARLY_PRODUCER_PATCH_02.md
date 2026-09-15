# Choice Kingdom — Canonical Early Producer Patch 02

Status: **SOURCE PATCH SPEC — REQUIRES AUTHORITATIVE CATALOG APPLICATION**

Purpose: close producer gaps only where the existing authored event already contains the correct causal situation. No engine-side inference is permitted.

## 1. E19 — Price Fixing → active market pressure

The event already describes merchants quoting identical prices after market concentration. Therefore the authored situation is a valid source for market pressure.

- On entry, the event establishes the authored state `market_pressure_active` for the current pressure cycle.
- A — breaking the guild agreement may resolve the active pressure after the choice outcome is applied.
- B — temporary price ceiling does **not** resolve the pressure; it keeps `market_pressure_active` active until an explicit later stabilization policy resolves it.
- Preserve the historical outcome markers from E19.
- Do not infer the predicate from `merchant_charter`, relationship score, or the E19 trigger alone.

This gives a pre-E166 producer for `pred.market_pressure`.

## 2. E179 — Rumor Tax → information pressure

The event already describes contracts becoming risky because rumors are spreading.

- On entry, establish `information_pressure_high` as the active information-pressure state for this cycle.
- A — verified market notices explicitly resolves the active pressure after verification is established.
- B — punishing rumor sellers does not resolve the underlying information problem; retain the active pressure marker and record the coercive response separately.
- Preserve historical markers for both the pressure and the response.
- Do not use `rel.toma` as a substitute.

This gives a pre-E231 producer for `pred.information_pressure_high`.

## 3. Active transport disruption remains OPEN

Do **not** classify E136 or E277 as the missing active producer. Both are recovery/clear outcomes. An earlier authored event must explicitly describe a transport failure and leave the active disruption unresolved. The existing E192 consumer must never manufacture `pred.transport_disruption`.

## 4. Guild labor tension remains OPEN

E169 is a consumer. E275-B is an authored producer but occurs after E169. No earlier event has yet been accepted as a safe producer without changing its narrative semantics. Do not manufacture labor tension from a generic guild route, relationship value, or commercial standards alone.

## 5. Application gate

Before changing the authoritative catalog:

- verify E19's complete current wording and downstream consumers;
- verify E179's complete current wording and downstream consumers;
- ensure active-state resolution does not erase immutable history;
- check that no earlier consumer precedes the new producer;
- rerun producer/consumer and reachability audits;
- update the derived predicate contract only after source edits are actually applied.

No production/runtime percentage is increased merely by this patch specification.
