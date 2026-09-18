# Block 18 — Performance / Optimization

## Objective
Establish a repeatable runtime performance baseline before adding advanced systems.

## Current contract
- Benchmark the canonical Python runtime through `DecisionEngine`.
- Exercise fresh-run creation, authored choice execution, snapshot creation, and availability projection.
- Run the benchmark deterministically in CI with a fixed iteration count and explicit wall-clock budget.
- Keep the benchmark separate from gameplay correctness tests: it measures a representative hot path without changing canonical game semantics.

## Gate
The Block 18 CI gate runs compilation plus the performance benchmark. The initial CI budget is 250 representative iterations in <= 5 seconds on the GitHub-hosted runner.

## Closure rule
This block is not 100% merely because the benchmark exists. 100% requires:
1. green CI benchmark evidence;
2. a documented baseline;
3. no benchmark-induced gameplay semantic changes;
4. representative Android performance profiling and physical-device evidence before final production closure.

The current work establishes the first repeatable baseline layer; device profiling remains an explicit later closure item.
