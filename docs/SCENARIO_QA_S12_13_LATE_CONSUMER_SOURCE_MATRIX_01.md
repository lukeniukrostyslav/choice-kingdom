# Choice Kingdom — S12.13 Late Consumer Source Matrix 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA
Frozen production scope: E01–E272.

## Late consumer matrix

E218/E225 consume food-pressure states and do not create `pred.food_stable`.
E242–E246 are delayed consumers whose source identity and timing must remain exact.
E247/E248 are replay-only candidates and require explicit `meta.*` isolation.
E249/E250 consume ordinary evidence routes and clue cardinality.
E251/E252 are winter/illness crisis consumers.
E253 consumes active border crisis and cannot create `pred.border_crisis`.
E254 consumes food crisis + local governance.
E255 consumes simultaneous food, border and civic pressure.
E256–E260 are constitutional/archive stress consumers.
E261 creates `four_way_bargain` package evidence, but that is not coalition cooperation.
E262 consumes that package and cannot qualify cooperation.
E263 audits the coalition route; E264/E265 are negative/positive coalition continuations, with exact producer semantics still requiring reconciliation.
E266–E268 consume active character routes.
E269 is a late commercial evidence handoff and is distinct from E55.
E270 creates `dual_witness_account` or `single_witness_account`; neither alone satisfies systemic explanation.
E271-A is the canonical positive `pred.border_crisis` producer; E271-B is explicit non-crisis.
E272 remains the lifecycle resolution node; exact authored branch tokens still require extraction.

## Negative contracts

- `food_logistics_stabilized` is not silently aliased to `pred.food_stable`.
- E253 cannot create border crisis.
- `four_way_bargain` is not cooperation proof.
- E262 cannot manufacture cooperation.
- E270 cannot by itself satisfy systemic explanation.
- E273–E277 contribute no production evidence.

## Delayed identity requirement

For E242–E246 the executable identity must preserve `sourceEventId + sourceChoiceId + consequenceId + earliestTurn + resolutionTarget + exactlyOnceKey + cancellation/supersession rule`.

Natural-language timing such as “6+ turns later” is not sufficient for runtime implementation.

## Gate

S12.13 PASS for source-level late consumer classification. Executable closure remains PARTIAL pending exact delayed identities, E272 extraction, replay meta keys, graph reachability and ending precedence.
