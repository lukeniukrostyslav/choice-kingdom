# Choice Kingdom — Canonical Source Corrections 02

Date: 2026-09-15
Status: SOURCE-LEVEL QA — CYCLE CLOSURE SPECIFICATION

## E136 / E194 guild-logistics cycle correction

### Problem found
E194 currently has `pred.guild_logistics_cooperation` as its trigger while E194-A itself establishes `history.guild_logistics_cooperation` and the neutral-inspector safeguard. This makes the authored graph circular if the predicate is defined only by E194-A.

### Verified upstream candidate
E136-B — Contract guild transport — is an earlier authored logistics-cooperation choice. It already establishes `transport_network_stable` and `roads_guild_contract`. This is a materially different event from E194: E136 is infrastructure cooperation; E194 is the later political/inspection terms of a convoy.

### Required source correction
E136-B must additionally establish the immutable history marker:
- `history.guild_logistics_cooperation`

This marker means the guild has previously demonstrated durable logistics cooperation. It is not by itself the final qualified predicate.

E194 trigger must be changed from:
- `pred.guild_logistics_cooperation`

to:
- `history.guild_logistics_cooperation`

E194 then becomes the qualification/terms event:
- E194-A accepts the convoy under neutral inspection and establishes `guild_neutral_inspectors`; with the prior cooperation marker and no active immunity-risk blocker, this establishes the qualified `pred.guild_logistics_cooperation` state for downstream consumers.
- E194-B establishes `guild_convoy_immunity` and `guild_logistics_immunity_risk`; it must not establish the qualified predicate.

### Canonical predicate rule
`pred.guild_logistics_cooperation` requires:
1. `history.guild_logistics_cooperation = true` from an earlier cooperation source such as E136-B;
2. `guild_neutral_inspectors = true` from the qualifying convoy choice;
3. no unresolved `guild_logistics_immunity_risk`.

The predicate is therefore downstream of E136-B + E194-A rather than self-produced by the event that consumes it.

## QA consequence

This removes the identified E194 self-dependency without adding a new event, new resource, or filler content. It preserves E194's narrative role as a later negotiation over convoy immunity and inspection while giving the logistics route a real upstream producer.

## Scope boundary

This is a source correction specification, not yet the production event schema. The authoritative E111–E150 and E151–E210 catalog files must be edited only after preserving their complete existing authored text; no reconstructed partial catalog may replace them.

## Gate impact

- Guild logistics producer chain: **CYCLE IDENTIFIED → CORRECTION SPECIFIED**
- Runtime predicate: **NOT IMPLEMENTED**
- Automated reachability: **0%**
- Production schema: **BLOCKED**
