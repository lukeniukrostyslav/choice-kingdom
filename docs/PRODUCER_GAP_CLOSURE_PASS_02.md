# Choice Kingdom — Producer Gap Closure Pass 02

**Status:** SOURCE-LEVEL QA / CANONICAL DESIGN CLOSURE PLAN  
**Runtime:** not implemented  
**Production schema:** intentionally not frozen

## Purpose

This pass converts the remaining P0 producer gaps into explicit authored closure requirements without inventing runtime state, deriving durable history from relationships, or treating graph edges as producers.

The campaign already contains enough material for the required full-game scale. The remaining problem is not lack of events; it is that several endgame/route predicates are named by consumers before an exact authored choice or deterministic rule establishes them.

## Closure rules

1. A producer is valid only when an authored choice explicitly establishes a durable marker or a deterministic state rule is defined against existing state.
2. A relationship value is never a substitute for route/history state.
3. A graph edge is not a producer by itself.
4. `food_stable`, `transport_disruption`, and similar pressures remain derived predicates/markers; no sixth resource is introduced.
5. Replay metadata under `meta.*` cannot satisfy current-run predicates without an explicit transfer rule.
6. Ending qualification remains downstream of canonical producers; ending nodes never manufacture their own prerequisites.

## P0 closure matrix

| Gap | Current source evidence | Closure action | Status |
|---|---|---|---|
| `hist.guild_representation` | E144 explicitly offers `guild_political_representation` | Treat E144-A as the canonical producer; preserve the marker as immutable history | **CLOSED — source verified** |
| `pred.food_stable` | E192 can explicitly improve food stability; E138/E157/E167/E193 expose food pressure | Define canonical predicate from existing food-pressure/stability marker(s); no new resource | **DESIGN REQUIRED** |
| `pred.transport_disruption` | E136 frozen road and E192 broken cart expose road pressure | Define durable road/transport pressure marker from E136/E192 choices and exact clear rule | **DESIGN REQUIRED** |
| `pred.border_crisis` | E139/E170–E172 establish border escalation ingredients; E195 consumes border escalation | Add an explicit escalation marker at the authored escalation point; security alone is invalid | **DESIGN REQUIRED** |
| `pred.guild_logistics_cooperation` | E124 trade standards, E140 market oversight, E194 guild convoy | Freeze the minimum authored combination and designate the E194 cooperation choice as the final durable producer | **DESIGN REQUIRED** |
| `pred.guild_influence_strong` | E165–E169 expose guild leverage/institutional influence | Define an authored combination with at least two distinct guild institutions/choices; `rel.ivo` alone is forbidden | **DESIGN REQUIRED** |
| `pred.systemic_explanation_verified` | E132–E135 and E186–E190 create investigation evidence | Require a distinct evidence-ID set plus explicit convergence choice; raw evidence count is insufficient | **DESIGN REQUIRED** |
| `pred.coalition_cooperation` | E146 six signatures and E148 coalition package | Use authored cross-faction cooperation plus `hist.cross_faction_package`; four active routes alone is insufficient | **DESIGN REQUIRED** |
| `pred.constitutional_prepared_strong` | E142/E145/E146/E148/E150 provide preparation choices | Freeze a non-circular minimum set; preparation cannot depend on final ending qualification | **DESIGN REQUIRED** |
| `pred.final_charter_prerequisites` | E197–E209 provide succession, budget, military, civic, guild and information routes | Define an explicit prerequisite set upstream of E210; E210 remains convergence only | **DESIGN REQUIRED** |

## Canonical source decisions

### Guild representation
E144 is the exact authored source that establishes guild political representation. This closes the previously open producer gap without creating a new event or inferring representation from Ivo's relationship.

### Guild logistics cooperation
The canonical closure must distinguish **guild cooperation** from merely having market influence. E194's neutral-inspector branch is the strongest authored candidate for the durable cooperation marker. Earlier E124/E140 choices are prerequisites/evidence, not automatic producers unless the final rule explicitly requires them.

### Coalition cooperation
`history.cross_faction_package` is already produced by E148-A. `pred.coalition_cooperation` must therefore be a deterministic qualification built from explicit cross-faction evidence and the authored E148 package, not a count of four active character routes.

### Systemic explanation
The investigation chain must identify distinct evidence IDs. A validator must reject a definition such as `evidence_count >= 3` when the same evidence can be counted repeatedly. The final convergence choice must establish `pred.systemic_explanation_verified` explicitly.

### Constitutional preparation
The preparation predicate must be upstream of E197–E210. It may consume civic, audit, coalition and constitutional choices, but it may not consume any ending result or E210 itself. This prevents circular ending qualification.

## Required follow-up insertion points

If the existing choices cannot be made to establish the above semantics without overloading unrelated markers, the next authored pass should add small, meaningful bridge choices rather than hidden engine inference. Candidate insertion points:

- after the border escalation decision, explicitly record a border-crisis state;
- after the food/road crisis resolution, explicitly record stable/unstable food logistics;
- after the guild convoy resolution, explicitly record logistics cooperation;
- at the investigation convergence, explicitly record verified systemic explanation;
- at the constitutional preparation convergence, explicitly record strong preparation;
- immediately before final charter convergence, explicitly record the final prerequisite package.

These are **content decisions**, not runtime implementation tasks.

## Forbidden shortcuts

- Do not derive `hist.guild_representation` from `rel.ivo`.
- Do not derive `pred.border_crisis` from `resource.security`.
- Do not invent a sixth food resource.
- Do not equate four active faction routes with coalition cooperation.
- Do not equate evidence count with systemic proof.
- Do not use E210 as an ending resolver.
- Do not reuse legacy E35–E40 as runtime IDs.
- Do not let replay-only `meta.*` silently satisfy current-run route predicates.

## Gate result

The producer graph is materially tighter than the previous audit because `hist.guild_representation` now has an exact source producer (E144-A). The other nine P0 items remain intentionally open until their authored semantics are frozen. This is the correct state: unresolved semantics are visible instead of being hidden inside a future engine.

**Next engineering gate:** finish canonical predicate definitions and authored producers, then build the machine-readable catalog against those verified semantics. Do not build the decision engine before that gate passes.
