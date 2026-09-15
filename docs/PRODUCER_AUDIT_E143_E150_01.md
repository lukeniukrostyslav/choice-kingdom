# Choice Kingdom — Producer Audit E143–E150 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — VERIFIED SUBSET**
Scope: authored E143–E150.

## Purpose

Freeze only durable state/history outputs explicitly supported by the authoritative authored catalog. Relationship values and numeric resource changes are not promoted into route predicates without an independent contract.

## Findings

| Event | Choice | Durable output(s) | Status | Downstream meaning |
|---|---|---|---|---|
| E143 | A | none | VERIFIED — RESOURCE ONLY | +4 trust, -2 security; no durable reserve marker is authored |
| E143 | B | none | VERIFIED — RESOURCE ONLY | +4 security, -3 trust; no durable reserve marker is authored |
| E144 | A | `history.guild_representation`; `guild_representation_separated_from_judiciary` | VERIFIED | representation history plus institutional separation outcome |
| E144 | B | `history.guild_representation`; `guild_representation_with_disclosure` | VERIFIED | same immutable representation history plus disclosure outcome |
| E145 | A | `regional_courts` | VERIFIED | regional independent-court outcome |
| E145 | B | `noble_courts_expanded` | VERIFIED | noble-court expansion outcome |
| E146 | A | `six_signatures_public` | VERIFIED | public cross-route constitutional-signature outcome |
| E146 | B | `six_signatures_private` | VERIFIED | private cross-route constitutional-signature outcome |
| E147 | A | `institutional_credit` | VERIFIED | institutional rather than heroic attribution |
| E147 | B | `heroic_reform_credit` | VERIFIED | named political architect outcome; relationship/resource effect is separate |
| E148 | A | `history.cross_faction_package`; `coalition_candidate_package` | VERIFIED | immutable coalition-package source; does not alone satisfy `pred.coalition_cooperation` |
| E148 | B | `history.selective_coalition`; `selective_coalition` | VERIFIED | selective coalition outcome; distinct from cooperation predicate |
| E149 | A | `coalition_cost_public` | VERIFIED | public-cost outcome |
| E149 | B | `coalition_cost_hidden` | VERIFIED | hidden-cost outcome |
| E150 | A | `constitution_bad_ruler_test` | VERIFIED | constitutional stress-test outcome |
| E150 | B | `constitution_good_ruler_model` | VERIFIED | good-leadership model outcome |

## Predicate boundaries

1. `history.guild_representation` is closed by E144-A/B; the legacy trigger `guild_political_representation` remains an alias until trigger normalization.
2. `history.cross_faction_package` is a source marker only. `pred.coalition_cooperation` still requires distinct faction evidence and absence of a collapse blocker.
3. E145's court outcomes are institutional facts, but they do not by themselves establish `pred.constitutional_prepared_strong`.
4. E146's signature outcomes establish a cross-character convergence fact, but do not by themselves establish coalition cooperation.
5. E147's relationship change to the highest relationship is not a substitute for a faction or constitutional predicate.
6. E150's constitutional-choice outputs are explicit outcomes, not proof that the player has already satisfied a final-charter prerequisite.
7. E143 intentionally has no invented durable marker: the authored source changes resources only.

## QA result

E143–E150 no longer require a direct producer-source ambiguity pass for the outputs listed above. Remaining endgame predicate contracts still require multi-event qualification and must not be closed merely because candidate inputs exist.

## Still open after this pass

- `pred.guild_influence_strong`
- `pred.systemic_explanation_verified`
- `pred.coalition_cooperation`
- `pred.constitutional_prepared_strong`
- `pred.budget_reform`
- `pred.final_charter_prerequisites`
- exact graph/reachability verification
- delayed/replay identity and exactly-once verification

This document is QA evidence only and is not runtime data or a production validator.
