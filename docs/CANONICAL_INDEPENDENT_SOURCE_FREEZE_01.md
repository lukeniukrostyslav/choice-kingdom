# Choice Kingdom — Canonical Independent Source Freeze 01

Status: **SOURCE-LEVEL CONTRACT — PROVISIONAL FREEZE, NOT ENGINE IMPLEMENTATION**

## Purpose

Freeze candidate independent authored source identities for composite predicates without allowing route counts, repeated triggers, relationship scores, or downstream consumers to masquerade as independent evidence.

## `pred.guild_influence_strong`

The canonical contract requires at least two distinct institutional domains. Candidate source domains from the authored catalog are:

| Domain | Candidate authored source | Verified authored key / fact | What it proves | Exclusion |
|---|---|---|---|---|
| representation | E49 political guild representation | `guild_political_representation` | guild participation in political representation | `guild_political_exclusion` is the opposing outcome; relationship with Ivo alone does not count |
| tribunal | E168-A independent guild tribunal | `guild_tribunal_independent` | institutional dispute-resolution authority | E168 trigger does not count |
| market/credit | E165 credit-book disclosure path | `official_credit_disclosure` | commercial institutional disclosure/leverage | repeated market outcomes are not independent domains |
| market | E166 audited monopoly path | `audited_monopoly` | audited commercial oversight | E166 trigger does not count; same market domain as E165 |
| logistics | E136-B qualified upstream cooperation | `history.guild_logistics_cooperation` + `roads_guild_contract` | qualified institutional logistics cooperation source | E194 cannot self-produce the qualified predicate |

### E194 downstream qualification

E194-A establishes `guild_neutral_inspectors` and retains `history.guild_logistics_cooperation`, but its own trigger is already `history.guild_logistics_cooperation`. Therefore E194 is a **consumer/refinement**, not an independent producer of the upstream cooperation fact. The qualified downstream predicate requires the upstream cooperation marker, neutral inspectors, and absence of unresolved `guild_logistics_immunity_risk`.

### Provisional qualification rule

`pred.guild_influence_strong` may qualify only from **two distinct domain identities**, with each domain backed by an explicit authored state/history fact. Repeated events in one domain do not increase cardinality. `relationship.ivo` is never a domain by itself. E165 and E166 cannot be double-counted as two domains because both are commercial/market leverage.

### Current status

**PARTIAL — exact source keys are now frozen for E49/E144 representation, E168/E165/E166, and E136-B logistics. Full producer-before-consumer reconciliation across E01–E272 remains open.**

## `pred.constitutional_prepared_strong`

The canonical contract requires three independent preparation domains. Candidate domains are:

| Domain | Candidate source | Verified authored key / fact | Semantic role | Exclusion |
|---|---|---|---|---|
| civic/commons | E50 People's Charter | `people_charter_endorsed` | explicit civic/commons constitutional legitimacy | raw trust or `people_heard` alone does not count as the full preparation domain |
| institutional/audit | E154/E155 crown-audit lineage | `crown_audited`, `full_crown_audit_published` | establishes accountable institutional preparation | E258 is a consumer of budget reform, not its producer |
| factional/house | E161 house assembly | `house_assembly` | establishes factional constitutional preparation | Seris relationship alone does not count |
| military/law | E227 Rowan's Line | `military_red_line` | establishes military constitutional constraint | security score alone does not count |

E50 is the authoritative early civic/commons source identified in the E01–E70 producer inventory. It is a preparation-domain fact, not a raw trust threshold.

### Provisional qualification rule

At least three independent preparation domains must be represented by explicit authored state/history facts. Late stress tests (E256–E260) may test or consume preparation but must not retroactively manufacture missing preparation. E154 and E155 remain one institutional/audit domain, not two. E50 is one civic/commons domain and cannot be double-counted with later civic consequences derived from the same charter decision.

### Current status

**PARTIAL — exact civic, institutional, house and military source keys are now identified; full E01–E272 anti-double-counting and producer-before-consumer reconciliation remains open.**

## Non-circularity rules

1. A consumer cannot create the predicate it consumes.
2. A trigger condition is not evidence merely because it appears in the trigger text.
3. Relationship values are not institutional domains.
4. A downstream consequence cannot become an upstream prerequisite solely because it is narratively related.
5. One authored source may contribute to only one independent domain unless the canonical contract explicitly proves that it represents genuinely distinct facts.
6. No composite predicate is CLOSED until all producers and consumers are rechecked against E01–E272.

## Next required pass

- reconcile E49/E144 representation keys against all guild producers/consumers and trigger normalization;
- reconcile E50 civic/commons key against all constitutional-preparation consumers;
- update the derived-predicate contract and producer/consumer registry together;
- then run contradiction/cycle/reachability checks;
- only after those checks begin production schema design.
