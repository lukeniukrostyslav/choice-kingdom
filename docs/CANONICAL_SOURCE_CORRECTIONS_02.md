# Choice Kingdom — Canonical Source Corrections 02

Date: 2026-09-15
Status: SOURCE-LEVEL QA — APPLIED AND VERIFIED

## E136 / E194 guild-logistics cycle correction

### Problem found
E194 had `pred.guild_logistics_cooperation` as its trigger while E194-A itself established `history.guild_logistics_cooperation` and the neutral-inspector safeguard. This made the authored graph circular if the predicate were defined only by E194-A.

### Applied source correction
The authoritative E111–E150 catalog now has E136-B establish the immutable history marker:
- `history.guild_logistics_cooperation`

This marker means the guild has previously demonstrated durable logistics cooperation. It is not by itself the final qualified predicate.

The authoritative E151–E210 catalog now has E194 trigger on:
- `history.guild_logistics_cooperation`

E194 remains the later qualification/terms event:
- E194-A accepts the convoy under neutral inspection and establishes `guild_neutral_inspectors`.
- E194-B establishes `guild_convoy_immunity` and `guild_logistics_immunity_risk` and does not establish the qualified predicate.
- The qualified `pred.guild_logistics_cooperation` is derived downstream only when the upstream cooperation marker exists, `guild_neutral_inspectors` exists, and no unresolved `guild_logistics_immunity_risk` remains.

### Verification
Direct re-read of the authoritative catalog confirms:
1. E136-B contains `history.guild_logistics_cooperation`.
2. E194 triggers on `history.guild_logistics_cooperation` rather than `pred.guild_logistics_cooperation`.
3. E194 explicitly states that the qualified predicate is derived downstream and is not self-produced by its trigger.

### QA consequence
The identified E194 self-dependency is closed at the authored-source level without adding a new event, resource, or filler content. E136 now supplies the upstream history fact, while E194 qualifies the later convoy route.

## Scope boundary

This correction is source-level only. Runtime predicate evaluation, automated reachability, production schema, and engine execution remain unimplemented.

## Gate impact

- Guild logistics producer chain: **CYCLE IDENTIFIED → SOURCE CORRECTION APPLIED → VERIFIED**
- Runtime predicate: **NOT IMPLEMENTED**
- Automated reachability: **0%**
- Production schema: **BLOCKED**
