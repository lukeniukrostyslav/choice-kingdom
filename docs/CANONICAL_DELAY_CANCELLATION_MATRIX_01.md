# Choice Kingdom — Canonical Delay Cancellation / Supersession Matrix 01

Status: **QA EXTRACTION — BOUNDARY AUDIT**  
Scope: high-risk delayed consumers E181–E185 and E242–E246.

A delayed consequence is not production-ready until its canonical row can resolve:
`sourceEventId + sourceChoiceId + consequenceId + earliestTurn + resolutionTarget + exactlyOnceKey + cancellation/supersessionRule`

| Consumer | Source identity | Timing evidence | Cancellation / supersession | Exactly-once | Status |
|---|---|---|---|---|---|
| E181 | E45-B | 5+ turns after toll concession | Explicitly `none_authored`; runtime cancellation/supersession still open | `delay.E45B.E181.second_toll_increase` frozen | SOURCE-EXTRACTED / runtime open |
| E182 | E117-B / veteran_patronage | 4+ turns later | Explicitly `none_authored`; runtime cancellation/supersession still open | `delay.E117B.E182.veteran_promise` frozen | SOURCE-EXTRACTED / runtime open |
| E183 | E118-B / estate_exception | 5+ turns later | Explicitly `none_authored`; runtime cancellation/supersession still open | `delay.E118B.E183.noble_exception_return` frozen | SOURCE-EXTRACTED / runtime open |
| E184 | **E25-B / secret_evidence_route** | 4+ turns later | Source identity closed; authored cancellation is `none_authored`; runtime execution remains open | `delay.E25B.E184.quiet_evidence` frozen | SOURCE-CLOSED / runtime open |
| E185 | E17-A / cheap_weapons + later military crisis | Condition-bound; later military crisis is the authored trigger condition | A prevents later failure; B schedules severe delayed loss; no authored cancellation/supersession | `delay.E17A.E185.cheap_steel_failure` frozen | SOURCE-EXTRACTED / runtime open |
| E242 | **E118-B / estate_exception** | 6+ turns later | Source identity closed; authored cancellation is `none_authored`; runtime execution remains open | `delay.E118B.E242.renewed_exception` frozen | SOURCE-CLOSED / runtime open |
| E243 | E18-B / public_bridge | 5+ turns later | Explicitly `none_authored`; runtime cancellation/supersession still open | `delay.E18B.E243.old_bridge` frozen | SOURCE-EXTRACTED / runtime open |
| E244 | E09-B / flexible_accounts | 5+ turns later | Explicitly `none_authored`; runtime cancellation/supersession still open | `delay.E09B.E244.audit_comes_due` frozen | SOURCE-EXTRACTED / runtime open |
| E245 | E20-A / soldier_compensation | 6+ turns later | Explicitly `none_authored`; no authored absolute cancellation/supersession | `delay.E20A.E245.soldiers_son_returns` frozen | SOURCE-EXTRACTED / runtime open |
| E246 | E160-A / winter_rent_ceiling | 5+ turns later | Explicitly `none_authored`; runtime scheduler/cancellation still open | `delay.E160A.E246.price_ceiling_memory` frozen | SOURCE-EXTRACTED / runtime open |

## Hard negatives

1. No absolute due turn is inferred from relative prose.
2. A consumer cannot manufacture its own prerequisite.
3. E245 cannot silently union E20/E125/E156 without an authored rule.
4. Cancellation cannot be inferred from narrative likelihood.
5. Replay/meta-state is not cancellation without an explicit promotion contract.
6. E273–E277 are excluded from production semantics.

## S31/S32 source-identity and extraction reconciliation — 2026-09-16

The earlier artifact incorrectly described several delayed rows as having timing/exactly-once identity wholly unextracted. The canonical machine delay contract now freezes source identity, authored relative timing where explicit, condition-bound timing for E185, exactly-once identity, persistent save/load policy and run-scoped replay policy for **all ten high-risk delayed consumers E181–E185 and E242–E246**.

This does **not** close runtime scheduling, duplicate-resolution protection, cancellation/supersession execution, or save/load runtime behavior. Those remain downstream lifecycle gates.

**Result: source extraction boundary expanded; runtime lifecycle remains open.**

This is a QA boundary artifact, not an executable production contract.
