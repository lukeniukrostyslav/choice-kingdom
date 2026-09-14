# Choice Kingdom — Producer Gap Closure Pass 07

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — P0 CLOSURE MATRIX REFRESH**  
Scope: canonical producer/consumer closure for E111–E270 before any production schema or engine work.

## Purpose

This pass consolidates the current authored evidence into one deterministic P0 matrix. It does **not** promote prose triggers into runtime predicates, and it does **not** claim engine/reachability/runtime verification.

## Verified authored producers

| Contract | Authored source | Current status |
|---|---|---|
| transport repair | E136-A/B | VERIFIED: `transport_network_stable`; disruption marker explicitly cleared |
| guild representation | E144-A/B | VERIFIED: `history.guild_representation` |
| cross-faction package | E148-A | VERIFIED: `history.cross_faction_package` plus six named participants |
| house assembly | E161-A | VERIFIED: `history.house_assembly` |
| food logistics state | E192-A/B | VERIFIED markers `food_logistics_unstable` / `food_logistics_stabilized` |
| guild logistics cooperation marker | E194-A | VERIFIED source marker `history.guild_logistics_cooperation`; qualification still needs canonical predicate implementation |

## P0 contracts that remain intentionally OPEN

### 1. Border crisis

Current authored material establishes border pressure, frontier warning infrastructure, refugee consequences and a late crisis consumer, but no single authoritative declaration/resolution pair has yet been verified.

- E139 is explicitly infrastructure/warning, not a crisis declaration.
- E195 consumes `pred.border_crisis`; it is therefore a consumer, not a producer.
- E253 consumes `border crisis`; it is also a consumer, not a producer.
- Required canonical state remains:
  - `border_crisis_declared`
  - `border_crisis_resolved`
- The engine must never infer declaration merely from `border tension`, military route, refugees, or warning signals.

**Gate: OPEN / P0.**

### 2. Guild logistics cooperation

E194-A provides the durable authored marker and neutral-inspector outcome. The canonical predicate still requires a deterministic qualification rule and invalidation handling.

Required minimum:
- `history.guild_logistics_cooperation = true`
- neutral inspection outcome established
- no unresolved `guild_logistics_immunity_risk`

**Gate: OPEN until the predicate contract is frozen.**

### 3. Strong guild influence

`rel.ivo` is not sufficient. The canonical predicate must consume at least two distinct institutional guild domains, for example representation, tribunal/institutional influence, commercial leverage or durable logistics cooperation. The exact accepted domain set must be frozen before production schema generation.

**Gate: OPEN / P0.**

### 4. Systemic explanation verified

Evidence fragments in E232–E236 and later nodes are ingredients, not proof by themselves. The final predicate requires four distinct evidence roles:

1. warehouse/financial evidence;
2. document/language evidence;
3. witness/organizational evidence;
4. explicit authored convergence decision.

E207 consumes this qualification and must not manufacture it.

**Gate: OPEN / P0.**

### 5. Coalition cooperation

`history.cross_faction_package` from E148-A is only the package foundation. Qualification requires cooperation evidence from at least three distinct faction identities and no unresolved coalition-collapse marker. Four relationship scores alone are not sufficient.

**Gate: OPEN / P0.**

### 6. Strong constitutional preparation

The predicate must be assembled from three independent upstream institutional domains:

- civic/commons legitimacy;
- audit/institutional legitimacy;
- cross-faction or constitutional legitimacy.

No late endgame event may retroactively create this prerequisite.

**Gate: OPEN / P0.**

### 7. Final charter prerequisites

Before E209 can qualify, the authored graph must establish, where applicable:

- civic/commons legitimacy;
- institutional/audit legitimacy;
- house/guild/faction representation;
- military/security constitutional route;
- information/evidence legitimacy;
- coalition cooperation;
- absence of mandatory unresolved crisis blockers.

E209 consumes this state. E210 is convergence-only and cannot manufacture missing prerequisites.

**Gate: OPEN / P0.**

## E211–E270 normalization rules

The expansion catalog is authored content, not yet a production contract. The following classes must be normalized before schema generation:

- prose triggers such as `institutional reform`, `food pressure`, `low gold`, `strong market oversight`, `veteran route`, `border route`, and `coalition route`;
- relationship thresholds versus durable route markers;
- delayed callbacks with stable source/consequence IDs and exactly-once semantics;
- replay callbacks restricted to `meta.*` unless an explicit persistent transfer is authored;
- evidence ingredients versus the final systemic convergence predicate;
- four-way bargain versus actual coalition cooperation;
- crisis consumers versus crisis producers.

No numeric sixth resource may be introduced for food, winter, transport, border tension or guild leverage.

## Legacy collision audit queue

The next source pass must explicitly reconcile:

- E35–E40 legacy aliases and any renamed state markers;
- duplicate semantic pairs E73/E156 and E99/E173;
- any remaining prose aliases that collide with canonical state vocabulary;
- delayed effects whose source IDs or consequence IDs are not stable.

## Current gate

**Production schema: BLOCKED.**  
**Decision engine: BLOCKED by design.**  
**Runtime reachability: NOT VERIFIED.**  
**APK/AAB: NOT STARTED.**

The correct next step is source-level P0 closure and deterministic producer/consumer enumeration, followed by graph/catalog reconciliation and reachability pre-audit. Only after those gates pass should machine-readable production data be introduced.
