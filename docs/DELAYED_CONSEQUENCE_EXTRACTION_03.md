# Choice Kingdom — Delayed Consequence Extraction 03

Status: **SOURCE CLOSURE PASS**

## E130 — The Bridge Toll Returns

**Delayed trigger:** `infrastructure_concession`, 4+ turns later.

The producer identity is now **verified** against the authoritative Act V source:

- **Producer:** E45-B
- **Producer marker:** `infrastructure_concession`
- **Consumer:** E130
- **Secondary consumer:** E181 / E224 families may consume the same infrastructure/economic context, but their timing contracts remain separate.

### Canonical interpretation

`infrastructure_concession` is an authored historical/policy marker, not a generic relationship score and not an inferred state from `river_compact` or `royal_toll_office`.

The 4+ turn delay belongs to E130's callback contract. The producer itself does not establish the callback schedule.

### Remaining implementation gates

The production delayed-consequence record still needs:

- immutable `delayId`;
- `sourceEventId=E45`;
- `sourceChoiceId=B`;
- `earliestTurn` derived from the canonical turn model;
- `resolutionTarget=E130`;
- exactly-once identity;
- cancellation/supersession semantics if the concession is later revoked or replaced;
- save/load persistence;
- replay isolation.

## E141 — The Emergency Clause Returns

**Delayed trigger:** `emergency_renewal_possible`, 5+ turns later.

The producer identity is now **verified** against the authoritative Act V source:

- **Producer:** E48-B
- **Producer marker:** `emergency_renewal_possible`
- **Consumers:** E141 and E257

### Canonical interpretation

`emergency_renewal_possible` is an explicit emergency-lifecycle marker. It must not be reconstructed from `emergency_decree_used`, power score, or generic crisis state alone.

E141's 5+ turn delay is a callback contract. E257 must not share E141's exactly-once key merely because both consume the same producer marker; each authored callback is a distinct resolution target unless the final schema explicitly proves a shared callback identity.

### Remaining implementation gates

- immutable callback identity for E141;
- immutable callback identity for E257;
- source/choice linkage to E48-B;
- exact earliest-turn semantics;
- cancellation/supersession if emergency authority is explicitly blocked before callback resolution;
- save/load persistence;
- replay isolation;
- deterministic same-turn ordering with other delayed callbacks.

## Closure result

The producer-identity gap for **E130 and E141 is closed at source level**. This increases Producer/Consumer QA confidence, but does **not** close the runtime delayed-consequence contract. Timing identity, cancellation, persistence and replay remain implementation/contract work.
