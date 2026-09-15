# Choice Kingdom — Scenario QA S04 Semantic Closure 02

Scope: E111–E150. This batch continues from `docs/SCENARIO_QA_S04_E111_E150_INVENTORY.md` and does not repeat the verified source inventory.

## Findings

### 1. E130 has an unnamed state mutation
E130 is triggered by `infrastructure_concession` and both choices change the economic/power outcome, but neither choice writes a named canonical fact. This is acceptable only if the production contract treats the result as direct numeric state mutation. No downstream predicate may infer a hidden fact from the prose outcome.

**Status:** OPEN — production contract must distinguish numeric mutation from named fact production.

### 2. E143 has the same contract shape
E143's army-budget choice changes state without a named flag. It must remain a numeric state mutation unless a later consumer is explicitly authored against a canonical machine fact.

**Status:** OPEN — no silent predicate inference permitted.

### 3. E131 is replay/meta-state, not ordinary run state
E131 explicitly describes a replay callback based on information unavailable to the current save. The contract must identify the exact `meta.*` producer/key and guarantee that ordinary run-local `all_voices_heard` cannot cross the replay boundary implicitly.

**Status:** OPEN — exact meta producer/key inventory remains a global S11 gate.

### 4. E141 emergency-renewal vocabulary is not source-closed by repository search
A repository search for `emergency_renewal` and `emergency_renewal_possible` returned no matching source occurrence at this checkpoint. Therefore the concept must not be promoted into a canonical predicate or producer without an authored source.

**Status:** OPEN / undefined-producer candidate if the concept is referenced by later machine contracts.

### 5. E144 is safely canonicalized
Both E144 choices explicitly produce `history.guild_representation`. This is a valid convergence marker and is not a duplicate contradiction merely because both branches write the same history fact.

**Status:** CLOSED at source level; runtime idempotence remains an engine concern.

### 6. E148 must not be promoted directly to coalition qualification
E148-A produces `history.cross_faction_package`; E148-B provides selective coalition support. Neither choice alone proves the stronger `pred.coalition_cooperation` qualification used by late endgame nodes. The stronger predicate must remain derived from its independent upstream requirements.

**Status:** CLOSED as a hard-negative rule; final dependency graph remains open.

### 7. E139 remains infrastructure-only
E139 is not a producer of `pred.border_crisis`. The border-crisis predicate remains tied to the explicit E271 declaration bridge and E272 resolution/clear bridge.

**Status:** CLOSED as a negative producer rule.

## S04 disposition
- Source inventory: verified.
- Canonical convergence markers: verified for E136/E144/E148.
- Silent semantic writer hazards: identified.
- Replay boundary: identified and kept open for exact meta producer/key closure.
- Undefined emergency-renewal vocabulary: flagged; no invented producer added.
- `pred.coalition_cooperation` self-satisfaction: explicitly prohibited.

S04 remains **70% / IN PROGRESS**. No global Scenario QA increase is claimed because global duplicate/contradiction, predicate-cycle, replay-key and reachability gates remain open.
