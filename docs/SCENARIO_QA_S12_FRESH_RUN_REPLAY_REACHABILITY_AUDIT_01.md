# Choice Kingdom — Scenario QA S12 Fresh-Run / Replay Reachability Audit 01

Date: 2026-09-15  
Status: **PARTIAL PASS — SOURCE/CONTRACT QA**  
Frozen production scope: **E01–E272**  
Expansion candidates: **E273–E277 excluded**

## Purpose

Audit the causal reachability boundary for a fresh run and for a representative replay without promoting unresolved narrative assumptions into runtime truth.

S12 answers four separate questions:

1. Can the campaign start from a clean initial state without inherited mutable state?
2. Can representative downstream consumers be reached through an admitted upstream source path?
3. Can a replay start clean while retaining only explicitly authored `meta.*` information?
4. Can unreachable, self-satisfying, or excluded-source paths be detected before runtime implementation?

This is a source-level reachability audit, not a runtime execution test.

## Fresh-run invariant

A fresh run MUST begin with:

- no pending delayed callbacks;
- no active border/transport/crisis predicate inherited from another run;
- no unresolved callback execution state;
- no prior-run-only relationship or route flags;
- no E273–E277 production state;
- only the canonical initial state explicitly admitted by the production contract.

The existing replay contract already establishes this isolation boundary; S12 treats it as a required reachability invariant rather than as evidence that every downstream path is reachable. 

## Closed source-backed reachability anchors

The normalized graph provides the following admitted path anchors:

| Path | Status | Reachability disposition |
|---|---|---|
| E18-B → `public_bridge` → E243 | CLOSED SOURCE EDGE | reachable candidate; full route reachability still requires upstream choice availability |
| E09-B → `flexible_accounts` → E244 | CLOSED SOURCE EDGE | reachable candidate; full route reachability still requires upstream choice availability |
| E117-B → `veteran_patronage` → E182 | CLOSED SOURCE EDGE | reachable candidate |
| E118-B → `estate_exception` → E183/E242 | CLOSED SOURCE EDGE / PARTIAL TARGET | source path admitted; exact delayed target semantics remain open |
| E17-A → cheap weapons → E185 | CLOSED SOURCE EDGE | reachable candidate |
| E136-B → `history.guild_logistics_cooperation` → E194 | CLOSED SOURCE EDGE | reachable candidate; inspection/negative blockers remain runtime-open |
| E29-A/B → `pred.winter_severe` | CLOSED PRODUCER | downstream reachability depends on branch availability |
| E32 → `pred.transport_disruption` → E192 | CLOSED ACTIVE PRODUCER EDGE | active lifecycle path admitted; persistence/expiry remains open |
| E136-A/B → transport recovery/clear | CLOSED RECOVERY EDGE | recovery path admitted; reactivation remains unresolved |
| E271-A → `pred.border_crisis` → E195/E253/E255 | CLOSED DECLARATION EDGE | active-cycle reachability admitted; resolution ordering remains runtime-open |
| E272-A/B → border resolution histories | CLOSED RESOLUTION EDGE | historical outcomes admitted |
| E199-A → military constitutional evidence | CLOSED SOURCE EDGE | downstream ending qualification remains partial |

## Reachability blockers

The following cannot currently be declared reachable merely because an event ID exists:

- `pred.food_stable`: no in-scope producer is source-closed;
- `pred.guild_influence_strong`: complete executable producer set and thresholds remain open;
- `pred.constitutional_prepared_strong`: independent-domain chronology and anti-double-counting remain open;
- `pred.systemic_explanation_verified`: exact producer set remains open;
- `pred.coalition_cooperation`: exact positive cooperation producer set remains open;
- `pred.final_charter_prerequisites`: complete upstream producer set remains open;
- E247/E248/E270 replay/meta consumers: source-closed `meta.*` producers/keys remain open;
- Broken Diadem / Quiet Throne: deterministic negative/failure producer sets remain open;
- late E251–E272 callback targets and exact timing: source lifecycle is bounded, executable callback identity is not fully frozen.

## Hard rejection rules

S12 rejects the following as false reachability proofs:

1. Event existence alone proves reachability.
2. A consumer event produces its own prerequisite.
3. E210 convergence manufactures missing upstream state.
4. E261 `four_way_bargain` alone proves coalition cooperation.
5. Generic relationship/resource/route counts substitute for explicit predicates.
6. E136 recovery can silently reactivate `pred.transport_disruption`.
7. E272 resolution can remain simultaneously active as `pred.border_crisis`.
8. E273–E277 can contribute production edges to the frozen campaign.
9. A previous replay can leak pending callbacks or active-cycle predicates into a new run.

## Replay reachability contract

For every representative replay:

`newRunState = canonicalInitialState + explicitlyAuthoredReplaySeed(meta.* only)`

No previous mutable callback queue, unresolved crisis, active predicate, or run-local relationship state may cross the boundary unless an explicit authored replay seed says so.

E247/E248/E270 therefore remain **OPEN** for executable replay reachability until their concrete `meta.*` producers and keys are source-closed.

## Preliminary path classification

### Class A — source-backed candidate paths

The paths listed in the closed anchor table have sufficient producer evidence to enter a future machine reachability graph. They are not yet proven executable end-to-end because the catalog must still verify choice availability, chronology, branch guards and any blocking consequences.

### Class B — contract-defined but producer-incomplete paths

Composite predicates and ending routes belong here. They may have a defined consumer contract but cannot be called reachable until all independent producers and negative conditions are enumerated.

### Class C — intentionally blocked paths

`pred.food_stable`, unresolved replay meta producers, unresolved Broken Diadem / Quiet Throne failure routes and any E273–E277 production path are blocked from production reachability.

## Machine-check requirements before S12 closure

The eventual validator must prove, for every E01–E272 node:

- canonical ID uniqueness;
- every incoming edge references an admitted producer or explicit initial-state source;
- every outgoing edge references an admitted consumer;
- no edge crosses into E273–E277;
- no producer→consumer cycle exists where the cycle requires self-satisfaction;
- temporal order is valid for delayed edges;
- cancellation/supersession rules prevent duplicate execution;
- replay reset removes run-local mutable state;
- every ending has at least one independently qualified incoming path;
- no ending depends solely on an unresolved/open producer;
- unreachable nodes are explicitly classified rather than silently ignored.

## Gate result

**S12 PARTIAL PASS.** Fresh-run and replay isolation invariants are now translated into explicit reachability rules, and the currently admitted source-backed path anchors are enumerated. Full closure is blocked by incomplete composite predicate producers, replay meta producers, delayed target/timing contracts, negative ending producers and the absence of an exhaustive event-by-event machine graph.

**S12 remains 20%. Scenario QA remains 65%.**

## Next autonomous block

1. Reconcile S11 ending incoming paths against the S12 reachability classes.
2. Continue S10 direct source extraction for E218/E225 and E251–E272 where authoritative catalog evidence is available.
3. Build the first machine-readable canonical reachability inventory only after source rows are sufficiently closed.
4. Do not promote production schema or Decision Engine until the canonical QA gate is materially closed.
