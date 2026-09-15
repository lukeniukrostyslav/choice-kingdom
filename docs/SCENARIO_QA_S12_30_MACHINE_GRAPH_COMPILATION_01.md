# Choice Kingdom — S12.30 Machine Graph Compilation Gate

Date: 2026-09-15  
Frozen production scope: **E01–E272**  
Excluded: **E273–E277**

## Objective

S12.30 converts the existing source-level QA surface into a machine-readable contract without promoting design-level graph edges into runtime truth.

## Added
- `docs/MACHINE_CANONICAL_GRAPH_01.json` — frozen scope, authoritative catalog source set, source-closed producers, delayed consumer identities, composite predicate status and hard-negative rules.
- `tools/validate_canonical_graph.py` — deterministic source-level validator.
- `.github/workflows/canonical-graph.yml` — CI execution on push / pull request.

## Verified CI result

Commit `7626994392831a27004eb5a3007432d35eb6b3e9` produced a GitHub Actions run whose validation step completed **SUCCESS**.

Observed machine-contract metrics:

- unique design-level event edges: **296**;
- repeated design-document edges: **43** (documentation repetition, not automatically a runtime duplicate writer);
- event nodes referenced by outbound design graph: **216 / 272**;
- source-closed producer rows: **21**;
- delayed consumer rows: **10**;
- hard-negative rules: **7**.

The 56 event IDs not represented as outbound nodes are **not automatically treated as orphaned**: terminal nodes, consumer-only nodes and qualification nodes must be separated from genuine reachability gaps in the next pass.

## Catalog reconciliation finding

The authoritative catalog source set was reconciled against the frozen E01–E272 scope.

### Closed source-set correction
`docs/EVENT_EXPANSION_071_110.md` was removed from the machine authoritative source list because `docs/EVENT_CATALOG_EXPANSION_02.md` already carries the E71–E110 canonical range. Keeping both created a false duplicate-definition signal.

### Intentional bridge duplicate
E271 appears in the E211–E270 document as a documented post-catalog bridge and in the E271–E280 lifecycle source. This is now explicitly classified as an allowed bridge duplicate rather than silently ignored.

### Real unresolved source gap
The machine catalog scan found **no authoritative `### E33` or `### E34` heading** in the selected narrative catalog sources. However, `docs/SCENARIO_QA_S01_E01_E34_INVENTORY.md` independently records E33 and E34 as verified source-level events. This is therefore a **source-recovery/reconciliation blocker**, not permission to invent missing event text.

Known E33/E34 verified semantics from S01 remain only at QA-inventory level:
- E33: emergency decree / severe crisis → `emergency_power` or `constitutional_limit`;
- E34: trust >=65 or welfare branch → `people_heard`.

Exact authored prose, choices, effects and delayed semantics must be recovered from an authoritative source before catalog↔machine equality can be declared.

## Deliberate non-claims

This gate does **not** claim runtime-complete campaign logic. The following remain open:

- exhaustive concrete producer/consumer token compilation;
- exact E33/E34 authoritative source recovery;
- semantic catalog ↔ graph equality;
- fresh-run reachability;
- replay reachability and exact `meta.*` producer keys;
- ending incoming-path / precedence simulation;
- delayed cancellation/supersession execution;
- Decision Engine implementation.

## Important disposition

E245 remains OPEN with candidates E20-A / E125-A / E156-A. No union is introduced. `pred.food_stable` remains OPEN/BLOCKED. E273–E277 remain outside production semantics.

## Gate result

**PASS — source-level machine-contract CI gate is operational and verified.**  
**Catalog semantic equality: BLOCKED by the E33/E34 source gap and remaining producer/consumer closure work.**  
**Production schema remains BLOCKED.**
