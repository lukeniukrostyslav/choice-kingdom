# Choice Kingdom — Scenario QA S12.37 — Qualification Matrix 01

Date: 2026-09-15  
Status: SOURCE-LEVEL QA — MATRIX COMPILED / RUNTIME CLOSURE OPEN  
Frozen production scope: E01–E272

## Objective

Compile the three highest-risk derived qualification predicates into explicit machine-oriented domain matrices without inventing producers. A qualification may consume evidence, but cannot manufacture missing evidence.

## 1. `pred.guild_influence_strong`

| Independent domain | Current source identity | Status | Anti-double-counting |
|---|---|---|---|
| guild representation | E144-A/B / E49 representation evidence | CLOSED at source identity | one representation domain |
| guild tribunal | authoritative tribunal evidence | PARTIAL | must remain distinct from representation |
| commercial / market | market-pressure/commercial evidence | PARTIAL | cannot be inferred from generic prosperity |
| logistics cooperation | E136-B `history.guild_logistics_cooperation` | CLOSED at source identity | E194 consumer cannot create it |

Qualification gate: the exact minimum-domain formula and canonical predicate key remain OPEN.

Hard negative: `rel.ivo` alone does not qualify as strong guild influence.

## 2. `pred.coalition_cooperation`

| Required component | Source candidate | Status |
|---|---|---|
| explicit participant identities | E148-A | PARTIAL / source candidate |
| positive cooperation outcome | E148-A | PARTIAL / source candidate |
| no unresolved collapse blocker | ending/collapse evidence | OPEN |
| four-way route | E261-A `four_way_bargain` | NOT SUFFICIENT |

Qualification gate remains OPEN. E261-A cannot be promoted merely because it makes a downstream ending reachable.

## 3. `pred.constitutional_prepared_strong`

| Independent domain | Canonical evidence | Status |
|---|---|---|
| civic | `people_charter_endorsed` | PARTIAL |
| institutional | `crown_audited` / `full_crown_audit_published` | SOURCE-CLOSED identity |
| factional | `house_assembly` | PARTIAL |
| military | `military_red_line` / E199-A constitutional oath route | STRONG source evidence |

Current authored contract requires at least three independent domains. Same-domain evidence must not double-count. Exact executable ordering, invalidation and producer-key normalization remain OPEN.

## 4. Machine QA invariants

1. Consumers never manufacture prerequisite state.
2. A downstream ending cannot be used as evidence for its own prerequisite.
3. Same-domain evidence cannot count twice unless an explicit authored contract says so.
4. `meta.*` remains isolated from fresh-run state.
5. E273–E277 remain excluded.
6. OPEN/PARTIAL source identity is never silently promoted to CLOSED runtime contract.

## Gate

S12.37 establishes a deterministic qualification-matrix boundary for guild influence, coalition cooperation and constitutional preparation. This is a QA artifact, not runtime implementation. Further progress requires authoritative source closure and/or verified machine compilation of exact formulas and lifecycle semantics.
