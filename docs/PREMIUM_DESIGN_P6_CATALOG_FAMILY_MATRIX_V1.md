# Choice Kingdom — P6 Authored Choice Family Matrix v1

Status: **EXECUTABLE COVERAGE BASELINE**

## Purpose

P6 must cover the real frozen production choice catalog rather than only a representative event. This matrix is intentionally derived from `AuthoredCatalog`; it does not invent canonical IDs, characters, factions, outcomes, or visual assets.

## Source of truth

- Frozen production scope: E01–E272.
- Runtime catalog parser: `runtime/catalog.py`.
- Executable audit: `tools/audit_p6_choice_catalog_coverage.py`.
- Regression test: `tests/test_p6_choice_catalog_coverage.py`.

## Required visual families

| Family | Derived from authored data | Visual work required |
|---|---|---|
| Two-way decision | events with exactly two choices | Primary decision-card composition |
| Three-or-more decision | events with 3+ choices | Multi-option hierarchy without shrinking targets |
| Resource-changing choice | authored resource deltas | Immediate consequence affordance without revealing hidden consequences |
| Relationship-changing choice | authored relationship deltas | Human-stakes presentation without faction moral coding |
| State-token choice | authored state tokens | Persistent consequence language and transition treatment |
| Triggered event choice | authored event trigger | Contextual decision framing |
| Clear-token choice | authored clear/remove/reset/cancel semantics | Resolution/cleanup presentation |

## Completion rule

A family is not considered visually complete merely because its data exists. P6 requires:

1. an inspectable visual treatment;
2. interaction states for idle, focused, selected, pressed, resolving, blocked, disabled, resolved and error/fallback where applicable;
3. mobile-safe composition;
4. RTL-safe composition;
5. accessible semantics and touch targets;
6. rendered verification against representative authored members;
7. transition handoff into P7 Consequence Experience;
8. final production asset provenance where artwork is used.

The catalog audit is therefore a coverage gate, not a percentage shortcut.

## Current gate

The executable catalog-family baseline is saved in GitHub. P6 remains **46%** until the visual families themselves are rendered and verified across the production surface.
