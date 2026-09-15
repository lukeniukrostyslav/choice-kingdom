# Choice Kingdom — Scenario QA Worklog

Frozen scope: **E01–E272**  
Expansion candidates: **E273–E277 excluded**  
Purpose: durable handoff ledger so completed QA work is not repeated.

## Latest continuation update — 2026-09-15

### S14 — machine predicate dependency validation
- Extended `tools/compile_scenario_source_inventory.py` to build a predicate-only dependency graph from authored trigger/output tokens.
- Added deterministic DFS cycle detection; any authored `pred.* → pred.*` cycle is now a machine-failing source-QA condition rather than a documentation-only warning.
- Added explicit reporting of predicate consumers that have no extracted producer, without inventing missing producers.
- Preserved the distinction between unresolved source vocabulary and runtime reachability; no undefined predicate is silently promoted to a producer.
- Commit: `b8ca0599cbfc314353b98e504960c317e4e16be0`.
- CI verification is pending for this new gate; the scenario percentage is not raised until the machine result is green.

### S13 — composite source closure / replay provenance correction
- Re-verified the authoritative derived-predicate contract for `pred.guild_influence_strong`, `pred.systemic_explanation_verified`, `pred.coalition_cooperation`, `pred.constitutional_prepared_strong` and `pred.budget_reform`.
- Confirmed independent source domains, anti-double-counting rules and the E01–E272 scope boundary.
- Preserved `pred.food_stable`, `pred.guild_labor_tension` and `pred.information_pressure_high` as OPEN/BLOCKED because no E01–E272 producer is source-closed.
- Corrected replay provenance: E131 is not promoted as an E186 producer/key binding; E186 remains partial source evidence and E247/E248 remain OPEN until explicit persistent producer/key tuples exist.
- Machine replay provenance validation rejects invented producer/key tuples and excludes E249/E250/E270 from replay-producer scope.
- Result: **source composite closure PASS; replay provenance boundary corrected; runtime lifecycle/reachability remains OPEN.**

### S10.4 — delayed source-boundary verification
- Verified high-risk delayed consumers E181–E185 and E242–E246 against the canonical producer/consumer registry.
- Confirmed authored source identities where present without promoting narrative timing into executable scheduling.
- Preserved E184 as unresolved because no safe canonical producer alias is source-closed.
- Preserved the E185 A/B branch distinction and did not invent cancellation or exactly-once semantics.
- Preserved E242 as a candidate-source case with unresolved selection/lifecycle semantics.
- Result: **S10.4 source-boundary verification PASS; runtime lifecycle gate remains OPEN.**

### S11.1 — E33/E34 ending-boundary closure
- Verified current canonical E33/E34 source boundary.
- E33/E34 are canonical production events; their evidence/flags remain distinct from the still-open deterministic ending-consumer runtime order.
- Result: **source-level boundary CLOSED; runtime ending-order gate remains OPEN.**

### S08.11 — budget reform / coalition source closure
- Closed source-level budget reform layers around E142-A, E154-A and E198-A while preserving explicit negative branches.
- Bound E148-A as the authoritative cross-faction package source; cooperation qualification remains a separate contract.
- Added anti-double-counting and scope-negative checks.
- Result: **source closure PASS; executable qualification/reachability remains open.**

### S09.6 — composite predicate producer enumeration
- Enumerated source-supported producer domains for high-risk composite predicates.
- Preserved E209 as consumer-only and E210 as convergence-only.
- Preserved `pred.food_stable` as BLOCKED because no E01–E272 producer is source-closed.

### S09.5 — normalized dependency edge inventory
- Compiled source-backed producer → fact/lifecycle → consumer edges using only admitted E01–E272 facts.
- Preserved historical-vs-current lifecycle boundaries and rejected self-satisfaction and excluded expansion edges.
- Composite predicates remain partial/open where exact source IDs, thresholds, lifecycle or chronology are not frozen.

### S09.4 — predicate cycle / self-satisfaction audit
- Isolated the E209 self-satisfaction risk and froze E209 as consumer-only.
- Preserved hard negatives for E200/E197/E207 and relationship/coalition aliases.
- Full token-level dependency extraction and machine cycle detection remain open.

### S09.2 — frozen-scope contradiction audit
- Confirmed the E273-A food-stability contradiction is resolved in favor of frozen E01–E272 production scope.
- `pred.food_stable` remains OPEN/BLOCKED until an in-scope producer is verified.

### S09.1 — predicate dependency pre-audit
- Started predicate dependency gate using source-closed facts only.
- Rejected self-satisfaction without independently proven upstream seeds.
- Exhaustive token-level extraction and machine cycle detection remain open.

### S08.10 — producer chronology pre-audit
- Converted source-closed producer families into explicit producer-before-consumer chronology gates.
- Confirmed ordering for transport, guild logistics, winter and border-crisis lifecycle families.
- Composite endgame chronology remains PARTIAL/OPEN.

## Current QA position

The scenario is being driven toward 100% by evidence, not planned work. A block is promoted only when its source contract, machine checks, chronology/lifecycle requirements and required verification are actually closed. Runtime engine verification, fresh-run reachability and Android execution remain downstream gates and are not counted as closed by documentation alone.
