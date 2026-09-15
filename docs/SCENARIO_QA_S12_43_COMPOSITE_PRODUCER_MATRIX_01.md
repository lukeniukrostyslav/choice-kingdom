# Choice Kingdom — Scenario QA S12.43 — Composite Producer Matrix 01

Date: 2026-09-15  
Status: **GREEN — SOURCE-LEVEL MATRIX COMPILATION**  
Frozen production scope: **E01–E272**

## Purpose

Freeze the currently source-backed producer domains for the three highest-risk composite predicates without pretending that source enumeration is executable runtime qualification.

## 1. `pred.guild_influence_strong`

| Domain | Canonical source candidate | Status | Anti-double-counting rule |
|---|---|---|---|
| Representation | `guild_political_representation` / `history.guild_representation` | SOURCE-CLOSED | One institutional representation domain only |
| Tribunal | `guild_tribunal_independent` | SOURCE-CLOSED candidate | Must remain distinct from representation |
| Market / credit | `official_credit_disclosure` OR `audited_monopoly` | SOURCE-CLOSED candidate | These are one economic/market domain |
| Logistics | qualified guild logistics cooperation | SOURCE-CLOSED upstream family | Requires the separate cooperation/inspection chain |
| Relationship | `rel.ivo` | HARD NEGATIVE | Cannot satisfy institutional guild influence alone |

**Current qualification contract:** at least two distinct institutional domains. Exact executable producer keys, lifecycle invalidation and reachability remain OPEN.

## 2. `pred.coalition_cooperation`

| Requirement | Source candidate | Status |
|---|---|---|
| Positive cooperation | E148-A `history.cross_faction_package`; E261-A cooperation candidates | SOURCE CANDIDATES FROZEN |
| Participant identity | explicit participating factions/actors | PARTIAL |
| No unresolved collapse blocker | terminal/collapse lifecycle | OPEN |
| `four_way_bargain` alone | rejected | HARD NEGATIVE |

**Current qualification contract:** positive cooperation + participant identity + no unresolved collapse blocker. E148-A is not automatically sufficient without the participant/cooperation evidence being explicit.

## 3. `pred.constitutional_prepared_strong`

| Domain | Source candidate | Status | Anti-double-counting rule |
|---|---|---|---|
| Civic | `people_charter_endorsed` | SOURCE-CLOSED | One civic domain |
| Institutional | `crown_audited` / `full_crown_audit_published` | SOURCE-CLOSED candidate | One audit/institutional domain |
| Factional | `history.house_assembly` | SOURCE-CLOSED | One factional domain |
| Military | `military_red_line` / military constitutional evidence | SOURCE-CLOSED candidate | Must remain distinct from institutional audit |
| E197 itself | consumer | HARD NEGATIVE | Cannot manufacture its own prerequisite |
| E209 | consumer | HARD NEGATIVE | Cannot manufacture final charter prerequisites |

**Current qualification contract:** at least three distinct preparation domains. Runtime ordering, exact source keys and reachability remain OPEN.

## Cross-predicate rules

1. A consumer never manufactures its own prerequisite.
2. Relationship state is not automatically institutional evidence.
3. A package/bargain is not automatically cooperation qualification.
4. Distinct-domain counts must use semantic domains, not merely different event IDs.
5. QA summaries cannot substitute for missing authored evidence.
6. E273–E277 remain excluded from all production matrices.

## Gate result

**GREEN:** source domains and hard negatives are now represented as a deterministic QA matrix.  
**OPEN:** executable formula/order, lifecycle invalidation, exhaustive producer enumeration and fresh-run reachability.

No overall percentage increase is granted solely for this matrix because runtime qualification remains unimplemented.
