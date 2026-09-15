# Choice Kingdom — Canonical Independent Source Freeze 01

Status: **SOURCE-LEVEL CONTRACT — PROVISIONAL FREEZE, NOT ENGINE IMPLEMENTATION**

## Purpose

Freeze candidate independent authored source identities for composite predicates without allowing route counts, repeated triggers, relationship scores, or downstream consumers to masquerade as independent evidence.

## `pred.guild_influence_strong`

The canonical contract requires at least two distinct institutional domains. Candidate source domains from the authored catalog are:

| Domain | Candidate authored source | What it proves | Exclusion |
|---|---|---|---|
| representation | E49 political guild representation | guild participation in political representation | relationship with Ivo alone does not count |
| tribunal | E168-A independent guild tribunal | institutional dispute-resolution authority | E168 trigger does not count |
| market/credit | E165 guild credit disclosure path / E166 audited market path | commercial institutional leverage | repeated market outcomes are not independent domains |
| logistics | qualified `history.guild_logistics_cooperation` consumed by E194 | institutional logistics cooperation | E194 cannot self-produce the qualified predicate |

### Provisional qualification rule

`pred.guild_influence_strong` may qualify only from **two distinct domain identities**, with each domain backed by an explicit authored state/history fact. Repeated events in one domain do not increase cardinality. `relationship.ivo` is never a domain by itself.

### Current status

**PARTIAL — source identities identified, authoritative event-by-event reconciliation still required before CLOSED.**

## `pred.constitutional_prepared_strong`

The canonical contract requires three independent preparation domains. Candidate domains are:

| Domain | Candidate source | Semantic role | Exclusion |
|---|---|---|---|
| civic/commons | people/civic charter preparation nodes | establishes civic participation in constitutional preparation | raw trust does not count |
| institutional/audit | E154/E155 crown-audit lineage and related institutional reform | establishes accountable institutional preparation | E258 is a consumer of budget reform, not its producer |
| factional/house | E161 house assembly / E47 constitutional table | establishes factional constitutional preparation | Seris relationship alone does not count |
| military/law | E37 `army_law_oath` / E227 `military_red_line` | establishes military constitutional constraint | security score alone does not count |

### Provisional qualification rule

At least three independent preparation domains must be represented by explicit authored state/history facts. Late stress tests (E256–E260) may test or consume preparation but must not retroactively manufacture missing preparation.

### Current status

**PARTIAL — candidate domains identified, exact canonical source IDs and anti-double-counting exclusions still require full catalog reconciliation.**

## Non-circularity rules

1. A consumer cannot create the predicate it consumes.
2. A trigger condition is not evidence merely because it appears in the trigger text.
3. Relationship values are not institutional domains.
4. A downstream consequence cannot become an upstream prerequisite solely because it is narratively related.
5. One authored source may contribute to only one independent domain unless the canonical contract explicitly proves that it represents genuinely distinct facts.
6. No composite predicate is CLOSED until all producers and consumers are rechecked against E01–E272.

## Next required pass

- reconcile exact E49/E165/E168/E194 and constitutional candidates against the authoritative catalog;
- identify whether any candidate is duplicated semantically;
- freeze exact state/history keys;
- then update the derived-predicate contract and producer/consumer registry together;
- only after that begin production schema design.
