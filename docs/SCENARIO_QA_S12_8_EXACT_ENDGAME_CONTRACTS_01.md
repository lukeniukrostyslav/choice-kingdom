# Choice Kingdom — S12.8 Exact Endgame Contract Extraction 01

Date: 2026-09-15
Status: **MACHINE CONTRACT QA — AUTHORITATIVE SOURCE EXTRACTION**
Frozen production scope: **E01–E272**. E273–E277 excluded.

## 1. Purpose

Convert the authoritative authored rows E197–E210 into explicit producer/consumer boundaries and deterministic evidence requirements without inventing missing producers.

## 2. E197 — Succession Test

**Trigger:** `pred.constitutional_prepared_strong`.

E197 is consumer-only for this predicate.

Outputs:
- E197-A → `emergency_powers_expire`
- E197-B → `emergency_powers_inherit`

Hard rule: E197 cannot create, strengthen, or substitute for `pred.constitutional_prepared_strong`.

## 3. E198 — Budget Lock

**Trigger:** audit reform.

- E198-A → `legislative_budget_lock`
- E198-B → `executive_budget_override_retained`

Canonical budget-reform source layer:
`E142-A auditor_independence` + `E154-A crown_audited`/`E155-A full_crown_audit_published` + `E198-A legislative_budget_lock`.

E198 alone does not prove `pred.budget_reform`.

## 4. E199 — Army Oath Rewritten

**Trigger:** military constitutional route.

- E199-A → `army_constitution_oath`
- E199-B → `army_crown_oath`

E199-A is constitutional military evidence, but is not by itself equivalent to `pred.constitutional_prepared_strong`.

## 5. E200 — Merchant Oath

**Trigger:** `pred.guild_influence_strong`.

E200 is consumer-only for strong guild influence.

- E200-A → `merchant_political_separation`
- E200-B → `merchant_influence_disclosed`

Hard rule: E200 cannot manufacture `pred.guild_influence_strong` from its own execution. Strong guild influence must be qualified from independent institutional domains upstream.

## 6. E201 — Coalition's Weakest Promise

**Trigger:** `pred.coalition_cooperation`.

E201 is consumer-only for coalition cooperation.

- E201-A → `coalition_renegotiated`
- E201-B → `coalition_shortfall_hidden`

Neither output creates the consumed predicate.

## 7. E202–E206 — Final faction votes

These nodes consume upstream route/thread state:
- E202 consumes `history.house_assembly`.
- E203 consumes `history.guild_representation`.
- E204 consumes `thread.military_constitutional`.
- E205 consumes `thread.amara_civic`.
- E206 consumes `thread.toma_information`.

Their branch outputs are consequence markers only; none may retroactively manufacture the consumed route.

## 8. E207 — Founder Question

**Trigger:** `pred.systemic_explanation_verified` AND `pred.coalition_cooperation`.

Authored qualification requires four distinct evidence families before E207:
1. warehouse/financial evidence;
2. document/language evidence;
3. witness/organizational evidence;
4. explicit convergence decision.

Each family must carry immutable evidence identity in the machine graph. Relationship scores, raw event counts, or the E207 consumer event itself cannot substitute.

Outputs:
- E207-A → `founder_authority_refused`
- E207-B → `founder_authority_accepted`

E207 is consumer-only for both predicates.

## 9. E208 — Empty Chair Again

**Trigger:** `thread.final_constitutional_phase`.

- E208-A → `empty_chair_memorial`
- E208-B → `permanent_emergency_chair`

It does not create the final constitutional phase thread by itself.

## 10. E209 — Dawn Charter

**Trigger:** `pred.final_charter_prerequisites`.

Authored prerequisite families are explicit:
- civic/commons legitimacy;
- institutional/audit legitimacy;
- faction/house/guild representation;
- required military/security constitutional route;
- information/evidence legitimacy;
- coalition cooperation;
- absence of unresolved mandatory crisis blockers.

E209 is strictly consumer-only. Its outputs are:
- E209-A → `charter_publicly_ratified`
- E209-B → `charter_council_ratified`

No E209 branch may create missing prerequisite families.

## 11. E210 — Last Decision Is Not a Choice

**Trigger:** `thread.endgame_convergence`.

E210 is **convergence-only**. It resolves the ending from verified accumulated state and must not manufacture prerequisites, evidence, coalition cooperation, or route qualifications.

Candidate ending families authored at this point:
- Steward
- Iron Crown
- Golden Compact
- People's Charter
- Broken Diadem
- Quiet Throne
- Second Founder

The final ending registry must require independent incoming evidence for every production ending.

## 12. Machine acceptance rules

Reject any graph where:
- E197 creates `pred.constitutional_prepared_strong`;
- E200 creates `pred.guild_influence_strong`;
- E207 creates `pred.systemic_explanation_verified` or `pred.coalition_cooperation`;
- E209 creates `pred.final_charter_prerequisites`;
- E210 creates any prerequisite or route qualification;
- an authored evidence family is represented only by a generic relationship score;
- final ending qualification has no independent incoming path.

## 13. Gate

**S12.8: PASS for exact authored consumer/convergence boundaries; PARTIAL for composite formula closure and full graph reachability.**

Next: compile exact evidence IDs/formulas for composite predicates, then reconcile E218/E225 and E251–E272 lifecycle/delayed rows against the exhaustive graph.
