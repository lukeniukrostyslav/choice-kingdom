# Choice Kingdom — S12.30 Machine Graph Compilation Gate

Date: 2026-09-15  
Frozen production scope: **E01–E272**  
Excluded: **E273–E277**

## Objective

S12.30 converts the existing source-level QA surface into a machine-readable contract without promoting design-level graph edges into runtime truth.

### Added
- `docs/MACHINE_CANONICAL_GRAPH_01.json` — frozen scope, source-closed producers, delayed consumer identities, composite predicate status, hard-negative rules and validation gates.
- `tools/validate_canonical_graph.py` — deterministic source-level validator for graph IDs, duplicate/self edges, producer scope, delayed ambiguity visibility and hard-negative coverage.
- `.github/workflows/canonical-graph.yml` — CI execution of the validator on every push / pull request.

## Validation contract

The validator checks:

1. frozen E01–E272 scope;
2. design-level `EVENT_GRAPH.md` event-chain IDs;
3. duplicate event edges;
4. self-loop event edges;
5. excluded expansion contamination in actual producer rows;
6. source-closed producer rows remain in scope;
7. delayed OPEN ambiguity is visible rather than silently unioned;
8. mandatory hard-negative rules remain present.

## Deliberate non-claims

This gate does **not** claim that the campaign graph is runtime-complete. The following remain open and continue to block production-schema freeze:

- exhaustive concrete producer/consumer token compilation;
- catalog ↔ graph equality;
- fresh-run reachability;
- replay reachability and exact `meta.*` producer keys;
- ending incoming-path / precedence simulation;
- delayed cancellation/supersession execution;
- Decision Engine implementation.

## Important disposition

E245 remains OPEN with candidates E20-A / E125-A / E156-A. No union is introduced. `pred.food_stable` remains OPEN/BLOCKED. E273–E277 remain outside production semantics.

## Gate result

**PASS for the new source-level machine-contract checks once CI executes successfully.**  
**Production schema remains BLOCKED.**
