# Choice Kingdom — Ending Qualification Contract 01

Status: **CANONICAL DESIGN CONTRACT — NOT ENGINE IMPLEMENTATION**
Scope: E265–E270 and the seven current ending families.

## Purpose

Ending nodes must not infer endings from vague route names, character relationships, or the last event alone. Each ending requires deterministic qualification from canonical state, immutable history and explicit route markers. Multiple independent paths should satisfy major prerequisites so one missed event does not silently make an ending unreachable.

## Canonical ending families

### Steward
Core identity: institutions survive the ruler.

Required families:
- `thread.institutional_reform`
- restrained emergency powers / constitutional expiry history
- stable or high public trust
- no terminal collapse condition

Supporting evidence may include:
- public audit;
- independent appointments;
- archive/public-record reform;
- balanced coalition decisions.

Negative blockers:
- permanent emergency authority;
- terminal institutional capture;
- severe unresolved multi-crisis collapse.

### Iron Crown
Core identity: security is maintained through concentrated executive/military power.

Required families:
- `thread.border_crisis` or an explicitly authored military route
- strong security / military dependency history
- emergency authority retained or constitutional limits weakened

Supporting evidence:
- military red line rejected;
- command authority strengthened;
- rapid mobilization repeatedly favored.

Negative blockers:
- fully independent military review plus strong distributed constitutional reform, unless another authored condition explicitly preserves the Iron Crown route.

### Golden Compact
Core identity: prosperity is preserved through commercial power and negotiated guild influence.

Required families:
- `thread.ivo_market`
- commercial/economic route
- durable evidence of guild leverage or trade-risk cooperation
- treasury/economic stability sufficient for the ending

Supporting evidence:
- trade guarantees;
- merchant/guild cooperation;
- commercial constitutional bargaining.

Negative blockers:
- terminal economic collapse;
- complete rejection of commercial route.

### People's Charter
Core identity: legitimacy is distributed through civic institutions and public participation.

Required families:
- high public trust / civic legitimacy
- `thread.institutional_reform` or an explicitly authored civic-governance route
- durable public/commons participation
- no terminal authoritarian or collapse state

Supporting evidence:
- public ledger access;
- tenant panels;
- public archive law;
- coalition transparency.

### Broken Diadem
Core identity: unresolved crises and institutional/relationship collapse.

Qualification should be based on a deterministic terminal failure predicate, not simply low trust.
Potential components:
- simultaneous unresolved major crises;
- institutional breakdown;
- severe security/economic pressure;
- insufficient recovery routes.

At least two independent failure paths must be possible.

### Quiet Throne
Core identity: ruler preserves personal survival or symbolic continuity while withdrawing from active constitutional leadership.

Required family:
- explicit withdrawal/abdication/low-intervention history
- absence of a stronger positive constitutional ending qualification

This must not trigger merely from low power or low trust.

### Second Founder
Core identity: the ruler discovers the systemic truth and redesigns the emergency system without permanently normalizing emergency power.

Required families:
- `thread.archive` / investigation evidence
- `pred.systemic_explanation_verified`
- `pred.coalition_cooperation`
- constitutional redesign
- emergency powers constrained/expired

Strong supporting evidence:
- procurement chain traced;
- payment/calendar evidence;
- archive/map comparison;
- replay-exclusive alternative evidence where explicitly transferred by the replay contract;
- `history.cross_faction_package` or another explicitly authored coalition marker.

The systemic explanation must be an evidence conclusion, not a relationship or faction label.

## Canonicalization rules applied in this contract

The following stale/noncanonical identifiers are prohibited as runtime state names:

- `thread.border` → use `thread.border_crisis`.
- `thread.guild` → use `thread.ivo_market` for the canonical commercial route; guild cooperation/influence must use its explicit `pred.*` predicates rather than a generic guild thread.
- `four_way_bargain` → do not use as an implicit alias. Coalition qualification uses `pred.coalition_cooperation`, with `history.cross_faction_package` as one verified authored input where applicable.
- `systemic_explanation_verified` → canonical predicate form is `pred.systemic_explanation_verified`.

No alias is considered a producer merely because it appears in older prose. Canonical names must have an explicit producer contract in the producer/consumer registry before engine implementation.

## E265–E270 qualification mapping

### E265 — institutional/civic endgame qualifier
Consumes canonical ending predicates and determines which of Steward, People's Charter, Golden Compact, or other legitimate endings remain eligible.

### E266 — personal/institutional convergence
Consumes character-arc and institutional history markers, especially Mara/constitutional decisions, without treating relationship scores as sufficient by themselves.

### E267 — security-authority qualifier
Evaluates military/border history, constitutional constraints and collapse predicates. Supports Iron Crown, Steward and People's Charter families where their full prerequisites are met.

### E268 — noble/stewardship qualifier
Evaluates noble constitutional route, precedent history, archive/investigation evidence and institutional durability. Supports Steward, Golden Compact and People's Charter families as authored conditions permit.

### E269 — commercial/information legitimacy qualifier
Evaluates guild/commercial route, information/evidence history and legitimacy. Supports Golden Compact and Second Founder families where explicit evidence and institutional conditions are met.

### E270 — systemic-truth/coalition qualifier
Evaluates systemic explanation, investigation depth, coalition, constitutional redesign and replay-transfer metadata. Primary support for Second Founder; other endings remain possible only when their independent qualification predicates are satisfied.

## Deterministic evaluation order

1. Validate terminal state and save version.
2. Evaluate collapse/failure predicates.
3. Evaluate explicit withdrawal/Quiet Throne condition.
4. Evaluate positive ending qualification predicates.
5. Apply authored priority only when multiple endings are simultaneously qualified; priority must be declared in data, not inferred from code order.
6. Record ending identity in immutable ending history.
7. Do not mutate prior decision history to manufacture qualification.

## Replay boundary

Replay discoveries may only influence current-run ending qualification through an explicit `meta.*` transfer rule. `meta.*` must never be silently treated as `hist.*`, `thread.*`, or `pred.*`.

## Validation gates

Before engine implementation, each ending must have:
- a complete positive qualification predicate;
- explicit negative blockers;
- at least two independent viable paths where appropriate;
- at least one authored test scenario;
- no dependency on a single character relationship value;
- deterministic result for identical state/history/seed/data;
- explicit interaction with delayed consequences and replay metadata.

This document is a design contract. It does not claim that E265–E270 are runtime implemented or that all required producers have already been authored and mapped.
