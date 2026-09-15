# Choice Kingdom — Canonical Delay Cancellation / Supersession Matrix 01

Status: **QA EXTRACTION — BOUNDARY AUDIT**
Scope: high-risk delayed consumers E181–E185 and E242–E246.

A delayed consequence is not production-ready until its canonical row can resolve:
`sourceEventId + sourceChoiceId + consequenceId + earliestTurn + resolutionTarget + exactlyOnceKey + cancellation/supersessionRule`

| Consumer | Source identity | Timing evidence | Cancellation / supersession | Exactly-once | Status |
|---|---|---|---|---|---|
| E181 | E45-B | 5+ turns after toll concession | Not extracted | Not extracted | PARTIAL — lifecycle open |
| E182 | E117-B / veteran_patronage | 4+ turns later | Not extracted | Not extracted | PARTIAL — lifecycle open |
| E183 | E118-B / estate_exception | 5+ turns later | Not extracted | Not extracted | PARTIAL — lifecycle open |
| E184 | No safe canonical producer alias | 4+ turns later / secret evidence route | Producer unresolved | Not extracted | OPEN |
| E185 | E17-A / cheap_weapons + later military crisis | Delayed branch authored; executable timing not normalized | A prevents later failure; B schedules severe delayed loss; supersession unresolved | Not extracted | PARTIAL / OPEN |
| E242 | E118-B candidate | Long-delay callback; scheduler open | Selection/lifecycle unresolved | Not extracted | PARTIAL / OPEN |
| E243 | E18-B / public_bridge | 5+ turns later | Not extracted | Not extracted | PARTIAL — lifecycle open |
| E244 | E09-B / flexible_accounts | 5+ turns later | Not extracted | Not extracted | PARTIAL — lifecycle open |
| E245 | E20-A / soldier_compensation | 6+ turns later | Absolute cancellation/supersession unresolved | Not extracted | PARTIAL — lifecycle open |
| E246 | E160-A / winter_rent_ceiling | Relative timing; scheduler open | Not extracted | Not extracted | PARTIAL — lifecycle open |

## Hard negatives

1. No absolute due turn is inferred from relative prose.
2. A consumer cannot manufacture its own prerequisite.
3. E245 cannot silently union E20/E125/E156 without an authored rule.
4. Cancellation cannot be inferred from narrative likelihood.
5. Replay/meta-state is not cancellation without an explicit promotion contract.
6. E273–E277 are excluded from production semantics.

## S10.4 verification addendum — 2026-09-15

Verified against the current canonical producer/consumer registry and bounded contract audit. E181/E182/E183/E243/E244/E245/E246 have source identities but remain lifecycle-open; E184 has no safe canonical producer alias; E185 retains the explicit A/B distinction; E242 remains a candidate-source case; no E273–E277 source was promoted.

**Result: S10.4 source-boundary verification PASS; runtime lifecycle gate remains OPEN.**

This is a QA boundary artifact, not an executable production contract.
