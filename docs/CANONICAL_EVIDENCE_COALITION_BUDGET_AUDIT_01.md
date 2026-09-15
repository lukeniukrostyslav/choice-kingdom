# Choice Kingdom — Evidence / Coalition / Budget Contract Audit 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — EXACT SOURCE INVENTORY IN PROGRESS**
Scope: E151–E277 plus frozen E49/E50 source identities.

## Purpose

Convert the remaining composite-contract candidates into explicit authored-source identities without allowing triggers, relationship values, downstream consumers, or repeated events to masquerade as independent evidence.

This document is an audit record, not engine schema and not runtime implementation.

## 1. `pred.systemic_explanation_verified`

Canonical requirement: three distinct evidence families plus explicit convergence:

1. warehouse/financial;
2. document/language;
3. witness/organizational;
4. an authored convergence decision that explicitly joins the three families.

### Verified candidate sources

| Evidence family | Candidate authored source | Exact authored fact currently visible | Status |
|---|---|---|---|
| warehouse/financial | E232 Procurement Chain | `intermediary_chain_traced` | CANDIDATE — financial/procurement lineage, semantic class still requires canonical confirmation |
| document/language | E233 Duplicate Seal | `seal_forensics` | CANDIDATE — document/forensic lineage |
| warehouse/financial | E234 Payment Calendar | `payment_pattern_public` / `payment_pattern_private` | CANDIDATE — payment-pattern evidence |
| witness/organizational | E236 Witness Ledger | witness/payment ledger route | CANDIDATE — exact durable evidence key needs normalization |
| document/archive | E235 Missing Middleman | `middleman_family_archive` | SUPPORTING ONLY until evidence-family classification is frozen |

### Hard finding

The currently inspected authored material establishes multiple evidence-producing choices, but this pass does **not** establish an explicit authored convergence choice that unambiguously joins all required evidence families. Therefore `pred.systemic_explanation_verified` remains PARTIAL and must not be promoted to CLOSED.

No relationship score, trigger, or downstream event may fill the missing convergence step.

## 2. `pred.coalition_cooperation`

### Verified sources

- E148-A is the early authoritative cooperation-package source: mutual concessions, `history.cross_faction_package`, `thread.coalition`, and explicit participation identities.
- E261-A is a later explicit cooperation package and therefore a second authored cooperation source.
- E148-B is explicitly selective and cannot qualify cooperation merely because several strong allies exist.

### Remaining machine-contract requirements

- canonical participant identity representation;
- positive cooperation outcome marker distinct from proposal/candidate status;
- blocker semantics for failed/hidden/exclusive branches;
- collapse/invalidation semantics after a previously successful cooperation package;
- ordering rule preventing E261 or later consumers from manufacturing an earlier missing cooperation fact.

Result: **PARTIAL**.

## 3. `pred.budget_reform`

### Verified preparation lineage

- E142-A: `auditor_independence`.
- E154-A: `crown_audited`.
- E155-A: `full_crown_audit_published`.
- E216-A: `treasury_shortfall_public` is a fiscal transparency consequence, not itself a budget-reform qualification.
- E258 is a consumer/stress-test node and cannot manufacture `pred.budget_reform`.

### Hard finding

The inspected authored source does not yet provide a separately verified legislative budget-lock source that can be combined with audit independence and crown-audit lineage into the canonical three-part qualifying combination.

E154 and E155 are one institutional/audit domain and cannot be counted as two independent domains merely because they are separate events.

Result: **OPEN**.

## 4. `pred.constitutional_prepared_strong`

The independent-source freeze remains authoritative:

- civic/commons: E50 `people_charter_endorsed`;
- institutional/audit: E154/E155 crown-audit lineage;
- factional/house: E161 `house_assembly`;
- military/law: E227 `military_red_line`.

At least three independent domains are required. E154 and E155 cannot double-count. Late stress tests cannot retroactively manufacture preparation.

Result: **PARTIAL** pending complete producer-before-consumer ordering and reachability reconciliation.

## 5. Composite-contract gate

Do not create production schema or runtime predicate code from this audit alone.

The next required pass is:

1. inspect the authoritative E01–E277 catalog for exact convergence/participant/budget-lock producers;
2. normalize exact state/history keys;
3. map every consumer after its earliest legal producer;
4. record negative/failed branch semantics;
5. run contradiction, cycle and reachability checks;
6. only then promote a contract to CLOSED.
