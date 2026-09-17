# Premium Cross-Screen Regression V1

## Purpose

The premium screen family must preserve semantic interaction states while adapting to available app-window width, RTL, large text and reduced motion.

## Matrix

The regression matrix covers:

- Event
- Realm
- History
- People
- Investigation
- Ending
- Settings

For every screen it expands the canonical state vocabulary into Compact, Medium, Expanded, RTL, large-text and reduced-motion cases.

## Hard invariants

1. Primary action remains preserved across every presentation dimension.
2. Screen state is presentation-only and never changes gameplay qualification.
3. Compact surfaces may remove secondary context but must not remove the primary decision/action.
4. Medium surfaces may expose supporting context where the screen benefits from it.
5. Expanded surfaces may expose supporting context and secondary actions without stretching controls indefinitely.
6. RTL and large text alter layout/presentation only.
7. Reduced motion removes decorative animation but preserves semantic state feedback.
8. Color is never the sole carrier of state.

## Android alignment

The contract uses app-window width rather than device identity. Android guidance recommends window-size-class-driven adaptation and testing across compact, medium and expanded widths, including resizing, fold/unfold and multi-window scenarios.

## Evidence

`runtime/premium_regression_matrix.py` generates the machine-readable matrix and validates the primary-action invariant. `tests/test_premium_regression_matrix.py` verifies screen, dimension and state coverage.

This is source-level regression evidence. It does not replace rendered Android screenshot/device proof.
