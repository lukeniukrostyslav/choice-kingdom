# Choice Kingdom — S12.10 Composite Predicate Contract Delta 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA — COMPOSITE CONTRACT NORMALIZATION
Frozen production scope: E01–E272.

## Purpose
Normalize composite predicate formulas sufficiently supported by authoritative source contracts without promoting undocumented prose into runtime semantics.

## 1. pred.guild_influence_strong

Independent domains:
1. representation: guild_political_representation / history.guild_representation;
2. tribunal: guild_tribunal_independent;
3. commercial: official_credit_disclosure OR audited_monopoly (one commercial domain);
4. logistics: qualified pred.guild_logistics_cooperation.

Qualification: count(distinct qualifying domains) >= 2.

Rules: same-domain flags count once; rel.ivo never counts as a domain; representation aliases are one domain; commercial alternatives are one domain; consumers cannot manufacture missing domains; evidence must be producer-before-consumer valid.

Status: FORMULA FROZEN AT CONTRACT LEVEL; chronology still requires exhaustive graph verification.

## 2. pred.systemic_explanation_verified

Required independent evidence families:
- warehouse/financial evidence;
- document/language evidence;
- witness/organizational evidence;
- explicit convergence decision.

Qualification: warehouse_financial >= 1 AND document_language >= 1 AND witness_organizational >= 1 AND explicit_convergence = true.

Evidence is counted by immutable source identity. E207 cannot provide convergence merely by being reached. E270 may contribute evidence only if a future explicit source mapping admits dual_witness_account; it cannot itself satisfy the complete predicate.

Status: FORMULA FROZEN AT CONTRACT LEVEL; exact immutable source IDs and chronology remain open.

## 3. pred.coalition_cooperation

Qualification requires explicit positive cooperation outcome, canonical participant/faction identities, and no unresolved coalition-collapse blocker. four_way_bargain is insufficient by itself. Route count is not cooperation semantics.

Status: FORMULA FROZEN AT CONTRACT LEVEL; authoritative positive producer requires exact source mapping.

## 4. pred.constitutional_prepared_strong

Independent preparation domains:
- civic/commons: people_charter_endorsed;
- institutional/audit: crown_audited OR full_crown_audit_published;
- factional/house: house_assembly;
- military/law: military_red_line.

Qualification: count(distinct qualifying preparation domains) >= 3.

full_crown_audit_published is downstream of crown_audited and cannot count as a second institutional domain. E197 is consumer-only.

Status: FORMULA FROZEN AT CONTRACT LEVEL; chronology/reachability remains open.

## 5. pred.budget_reform

Exact qualifying domains:
- auditor_independence from E142-A;
- crown_audited from E154-A;
- legislative_budget_lock from E198-A.

Qualification: auditor_independence AND crown_audited AND legislative_budget_lock.

Negative blockers: E142-B auditor_crown_control; E154-B crown_exempt_from_audit; E198-B executive_budget_override_retained. full_crown_audit_published is downstream of E154 and is not an independent substitute. E258 consumes the predicate and cannot manufacture it.

Status: FORMULA FROZEN AT CONTRACT LEVEL; chronology and reachability require graph verification.

## 6. pred.final_charter_prerequisites

Convergence contract requiring established upstream domains for civic/commons legitimacy, institutional/audit legitimacy, faction/house/guild representation, military/security constitutional route, information/evidence legitimacy, coalition cooperation, and absence of unresolved mandatory crisis blockers.

No consumer may manufacture a missing domain. E209 remains consumer-only and E210 remains convergence-only.

Status: PARTIAL — domain identity and deterministic precedence require full graph reconciliation.

## Acceptance / rejection rules
Reject production promotion if relationship score substitutes for institutional evidence; same-domain aliases are double-counted; downstream consequences count as independent upstream evidence; a consumer manufactures its prerequisite; E273–E277 contributes production evidence; replay metadata leaks into ordinary state; a negative branch satisfies a positive domain; or a later producer retroactively satisfies an earlier consumer.

## Gate
S12.10: PASS for contract-level composite formula normalization; PARTIAL for executable graph closure. Production schema remains blocked until immutable source IDs, chronology, reachability and ending precedence are reconciled across E01–E272.
