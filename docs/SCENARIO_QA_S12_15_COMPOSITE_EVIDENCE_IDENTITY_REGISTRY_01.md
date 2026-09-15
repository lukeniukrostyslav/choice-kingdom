# Choice Kingdom — S12.15 Composite Evidence Identity Registry 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA
Frozen production scope: E01–E272.

## Purpose

Promote only exact authored evidence identities into a machine-contract registry. This pass does not invent runtime state, turn windows, or evidence where the catalog has not supplied it.

## 1. `pred.systemic_explanation_verified`

Required independent evidence classes:

1. warehouse/financial;
2. document/language;
3. witness/organizational;
4. explicit convergence decision.

Current authored candidates:

| Class | Source | Authored marker/fact | QA status |
|---|---|---|---|
| warehouse/financial | E232 | `intermediary_chain_traced` | candidate; canonical class identity requires final normalization |
| document/language | E233 | `seal_forensics` | candidate |
| warehouse/financial | E234-A/B | payment-pattern evidence | candidate; branch-specific key required |
| witness/organizational | E236 | witness/payment ledger route | candidate; durable evidence key required |
| document/archive | E235 | `middleman_family_archive` | supporting only until class assignment is frozen |

Hard result: no inspected source establishes an unambiguous authored convergence decision that joins all three required classes. Therefore the predicate remains **PARTIAL**, not CLOSED.

## 2. `pred.coalition_cooperation`

Exact positive source candidates:

- E148-A: `history.cross_faction_package`, `thread.coalition`, explicit participant identities and mutual-concession package.
- E261-A: `four_way_bargain`, explicit balanced package across Commons/Houses/Guilds/Border.

E148-B and E261-B are not positive cooperation producers.

Required normalized state:

`cooperationDeclared=true` + canonical participant identities + positive cooperation outcome + no unresolved exclusive/broken/collapse blocker.

`four_way_bargain` alone is not sufficient. E261-A is a source candidate for explicit cooperation evidence, but downstream promotion still requires canonical positive outcome and invalidation semantics.

Result: **PARTIAL**.

## 3. `pred.budget_reform`

Canonical three-source contract:

- E142-A → `auditor_independence`;
- E154-A → `crown_audited`;
- E198-A → `legislative_budget_lock`.

Negative branches:

- E142-B blocks auditor independence;
- E154-B blocks crown audit;
- E198-B retains executive override and therefore blocks legislative budget lock.

E155-A (`full_crown_audit_published`) remains downstream audit evidence in the same institutional/audit domain and must not double-count E154.

E258 is consumer/stress-test only and cannot manufacture budget reform.

Result: **SOURCE CLOSED / EXECUTABLE QUALIFICATION PARTIAL** pending producer ordering, reachability and deterministic blocker reconciliation.

## 4. `pred.constitutional_prepared_strong`

Independent preparation domains remain:

- civic/commons → E50 `people_charter_endorsed`;
- institutional/audit → E154-A `crown_audited` (E155-A is same domain);
- faction/house → E161-A `house_assembly`;
- military/law → E227 `military_red_line`.

Qualification requires at least three distinct domains. No downstream consumer may manufacture a missing domain.

Result: **PARTIAL** pending exhaustive ordering and reachability.

## 5. Acceptance gate

PASS:
- exact source event/choice identities recorded where authored evidence is available;
- negative branches preserved;
- same-domain evidence cannot double-count;
- E210 and other consumers cannot manufacture prerequisites;
- E273–E277 excluded from production semantics.

OPEN:
- immutable durable evidence-key normalization for E232–E236;
- explicit convergence producer for systemic explanation;
- final positive coalition state/lifecycle;
- exhaustive producer-before-consumer graph and reachability.

No runtime schema promotion is authorized by this artifact alone.
