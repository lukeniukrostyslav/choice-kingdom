# Choice Kingdom — S12.1 Reachability Anchor Inventory 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — PARTIAL MACHINE INVENTORY**
Scope: frozen production catalog E01–E272.

## Purpose

This artifact converts the currently verified source-level producer chains into an explicit machine-oriented anchor inventory without claiming exhaustive reachability. It is an intermediate S12 artifact: every row below is evidence-backed, while unenumerated events remain unresolved until the complete catalog can be mapped.

## Canonical anchors

| Source | Choice | Durable output / lifecycle | Consumer / target | Status |
|---|---|---|---|---|
| E18 | B | `public_bridge` | E243 delayed callback | SOURCE-CLOSED |
| E09 | B | `flexible_accounts` | E244 delayed callback | SOURCE-CLOSED |
| E117 | B | `veteran_patronage` | E182 delayed callback | SOURCE-CLOSED |
| E118 | B | `estate_exception` | E183 / E242 delayed callbacks | SOURCE-CLOSED / E242 PARTIAL |
| E17 | A | `cheap_weapons` | E185 delayed callback | SOURCE-CLOSED |
| E136 | B | `history.guild_logistics_cooperation` | E194 | SOURCE-CLOSED |
| E29 | A/B | `pred.winter_severe` | winter-dependent consumers | SOURCE-CLOSED |
| E32 | canonical active branch | `pred.transport_disruption` / active lifecycle | E192 and later crisis consumers | ACTIVE-PRODUCER IDENTITY PARTIAL |
| E136 | A/B | transport recovery / clear | clears active transport disruption | SOURCE-CLOSED |
| E142 | A | `auditor_independence` | budget reform candidate | SOURCE-CLOSED |
| E154 | A | `crown_audited` | budget reform candidate | SOURCE-CLOSED |
| E198 | A | `legislative_budget_lock` | budget reform candidate | SOURCE-CLOSED |
| E144 | A/B | `history.guild_representation` | E203+ | SOURCE-CLOSED |
| E271 | A | `border_crisis_declared`, active `thread.border_crisis` | E195/E253/E255 family | SOURCE-CLOSED |
| E272 | A/B | border crisis resolution + historical record | post-crisis consumers | SOURCE-CLOSED |
| E199 | A | `army_constitution_oath` | military-constitutional route | STRONG SOURCE CANDIDATE |
| E146/E148 | authored choices | coalition package/signature evidence | coalition consumers | PARTIAL |

## Hard rules

1. An anchor proves a source-backed causal edge, not end-to-end runtime reachability.
2. A consumer cannot manufacture its own prerequisite.
3. A downstream result cannot be promoted to an independent producer when it is semantically derived from the same source.
4. E273–E277 are excluded from the frozen production graph.
5. Recovery/clear edges cannot reactivate the predicate they clear.
6. Replay state cannot satisfy current-run predicates unless an explicit authored `meta.*` seed contract exists.
7. Relative timing (`4+`, `5+`, `6+` turns, etc.) is not an executable earliest-turn value until normalized.

## Current open reachability classes

- `pred.food_stable`: source/marker contract unresolved.
- `pred.transport_disruption`: recovery is closed; active producer identity remains incomplete in this audit surface.
- `pred.guild_influence_strong`: exact independent domain set unresolved.
- `pred.systemic_explanation_verified`: evidence-ID set and convergence rule unresolved.
- `pred.coalition_cooperation`: cooperation membership must remain distinct from route count.
- `pred.constitutional_prepared_strong`: independent prerequisite set unresolved.
- `pred.final_charter_prerequisites`: full incoming path and blockers unresolved.
- replay/meta producers for E247/E248/E270 unresolved.
- deterministic negative/failure producer sets for Broken Diadem / Quiet Throne unresolved.
- late E251–E272 callback timing/targets remain only partially source-closed.

## S12 gate

**PARTIAL PASS.** The anchor inventory is machine-oriented and source-backed, but it is not exhaustive.

## Next closure pass

1. Enumerate all E01–E272 choice outputs.
2. Normalize every output into canonical token vocabulary.
3. Map every consumer trigger to exact producer choices.
4. Flag zero-producer, multi-producer, contradictory and cyclic tokens.
5. Add delayed identity/timing/cancellation columns.
6. Reconcile every ending prerequisite against an independent incoming path.
7. Run the fresh-run graph from canonical initial state.

Production schema and Decision Engine remain blocked until this evidence is sufficiently complete.
