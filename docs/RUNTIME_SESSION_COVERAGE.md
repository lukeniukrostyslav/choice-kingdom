# Runtime Session Coverage

This document records the verified application-facing `GameSession` coverage added during the current runtime integration block.

## Covered boundaries

- Authored E01 → E02 execution and state mutation.
- Save/load snapshot preservation.
- Recovery load snapshot preservation.
- Authored route/available-event boundary.
- Completed-run replay export gate.
- Completed-run replay import with canonical meta keys only.
- Source-closed ending facts exposed without relationship-score inference.
- Delayed consequence activation through the canonical runtime delay lifecycle.

## Important limitation

These tests expand the application-facing runtime seam; they do **not** establish exhaustive E01–E272 gameplay execution. Opaque/partial authored triggers remain unresolved unless their semantics are explicitly established by source evidence.

## Verification rule

The Decision Engine percentage is increased only when the corresponding tests are green in GitHub Actions. Documentation alone does not change the percentage.
