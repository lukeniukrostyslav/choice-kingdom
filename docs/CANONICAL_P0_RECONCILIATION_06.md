# Choice Kingdom — Canonical P0 Reconciliation 06

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — NOT ENGINE INPUT**  
Scope: E01–E272 frozen production catalog, with E273–E277 treated only as admission candidates.

## 1. Guild influence — anti-double-counting contract

The authoritative source separates guild influence into institutional domains rather than relationship strength:

- representation: `history.guild_representation` (E49/E144 are one semantic domain, not two);
- commercial tribunal: E168-A/B, with independent vs guild-controlled outcomes;
- commercial/market governance: E166 and related merchant-governance choices;
- qualified logistics cooperation: E136-B upstream marker followed by E194-A neutral-inspection qualification and absence of `guild_logistics_immunity_risk`.

`pred.guild_influence_strong` is consumed by E200 and must never be manufactured from `rel.ivo`, raw event count, or duplicated E49/E144 evidence.

### Contract result
**DOMAIN SET: CONDITIONALLY CLOSED.**

A machine contract must count distinct institutional domains, not source-event count. Negative outcomes in the same domain cannot simultaneously qualify that domain. E194 cannot self-create the qualified logistics predicate without the upstream E136-B cooperation marker.

The exact minimum-domain threshold remains a schema decision and therefore is still **OPEN** until the complete E01–E272 producer inventory is compiled.

## 2. Constitutional preparation — independent domain boundary

Current authored evidence provides four distinct upstream domains:

1. civic/commons legitimacy — `people_charter_endorsed`;
2. institutional/audit legitimacy — `crown_audited` or the explicitly published full Crown audit route;
3. factional legitimacy — `house_assembly`;
4. military/security constitutional legitimacy — `military_red_line` / constitutional military route.

Cross-faction preparation (`history.cross_faction_package`) is important but cannot silently replace all other domains. E197 is a consumer and cannot create its own prerequisite.

### Contract result
**DEPENDENCY DOMAINS: CLOSED; QUALIFICATION FORMULA: OPEN.**

At least three independent domains are currently specified by the canonical closure record. The eventual production contract must define whether the required set is exactly three or a stricter four-domain gate, and must reject double counting of multiple events from the same domain.

## 3. Systemic explanation — evidence families

E207 explicitly requires four distinct qualification components:

- warehouse/financial evidence;
- document/language evidence;
- witness/organizational evidence;
- explicit convergence decision.

Existing authored examples include warehouse/arson evidence, emergency-language comparison, conflicting testimony / office-network evidence and the final convergence decision. However, narrative similarity is not enough for runtime qualification.

### Contract result
**SHAPE CLOSED; SOURCE-ID COMPILATION OPEN.**

Every evidence family must receive an immutable source/evidence ID. A replay-only informational unlock cannot satisfy a current-run evidence family unless an authored cross-run promotion rule explicitly says so.

## 4. Coalition cooperation — positive outcome vs package creation

E148-A establishes a six-participant cross-faction package. This is necessary cooperation evidence, not an automatic perpetual predicate. E201 consumes `pred.coalition_cooperation`; later coalition events may strengthen or invalidate the qualification.

The production contract therefore requires:

- explicit participant/faction identities;
- positive cooperation outcome, not merely a meeting/package flag;
- no unresolved coalition-collapse blocker;
- deterministic invalidation/supersession semantics.

### Contract result
**SOURCE CHAIN STRONG; RUNTIME QUALIFICATION OPEN.**

`history.cross_faction_package` must not be aliased directly to `pred.coalition_cooperation`.

## 5. Budget reform — no shortcut

The authored source separates:

- `auditor_independence` (E142-A);
- `crown_audited` / `full_crown_audit_published` (E154-A/E155-A);
- `legislative_budget_lock` (E198-A).

Negative alternatives are also explicit and must remain observable (`crown_exempt_from_audit`, `executive_budget_override_retained`).

### Contract result
**SOURCE LAYERS CLOSED; QUALIFYING FORMULA OPEN.**

No generic `audit_reform=true` field may replace the three institutional facts. The final predicate must specify exact positive requirements and whether negative blockers are terminal or reversible.

## 6. E273–E277 admission gate

E273–E277 remain outside the frozen E01–E272 catalog. They may fill explicit producer gaps, but admission requires:

1. upstream reachability into the existing graph;
2. downstream consumer compatibility;
3. no semantic duplicate producer;
4. no contradictory writer without lifecycle semantics;
5. no break to the E136 transport-recovery contract;
6. deterministic current-cycle invalidation/expiry;
7. no new circular prerequisite.

Until that graph pass succeeds, these nodes are **candidate source material only**.

## 7. Delayed consequences — extraction gate

The canonical delay contract requires globally unique delay ID, exact source event/choice, earliest turn, resolution target, exactly-once key, cancellation/supersession, persistent save/load behavior and deterministic same-turn ordering. fileciteturn71file0

Known authored callback groups include E181–E185 and E242–E246, plus earlier catalog callbacks. Prose such as “5+ turns later” or “during a later crisis” cannot be promoted to production data until exact source-choice identity and resolution semantics are extracted.

### Contract result
**DESIGN CONTRACT CLOSED; AUTHORED DATA EXTRACTION OPEN.**

## P0 gate

| Contract | Result |
|---|---|
| guild influence | **CONDITIONAL — domain boundary closed, threshold open** |
| constitutional preparation | **CONDITIONAL — domains closed, formula open** |
| systemic explanation | **PARTIAL — shape closed, source IDs open** |
| coalition cooperation | **PARTIAL — source chain strong, runtime qualification open** |
| budget reform | **PARTIAL — source layers closed, formula open** |
| E273–E277 admission | **BLOCKED pending graph pass** |
| delayed consequences | **DESIGN CLOSED / DATA OPEN** |

**Production schema: BLOCKED.**  
**Decision Engine: BLOCKED by canonical contract gate.**  
**Runtime reachability: NOT VERIFIED.**
