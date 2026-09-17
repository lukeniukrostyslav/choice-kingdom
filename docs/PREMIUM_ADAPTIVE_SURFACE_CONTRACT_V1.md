# Premium Adaptive Surface Contract V1

## Purpose

Define one presentation-only rule for adapting the premium screen family to the actual available app-window width.

## Width contract

| Width | Surface | Premium behavior |
|---|---|---|
| `<600dp` | Compact | Primary action remains dominant; secondary actions/context collapse |
| `600–839dp` | Comfortable | Secondary actions become available; supporting context appears on information-heavy screens |
| `>=840dp` | Expanded | Full supporting context and secondary actions may coexist with primary content |

The contract uses available app-window width, not physical device identity. Android guidance recommends responsive/adaptive decisions from the current app window and window size classes, including during resize, fold/unfold and multi-window changes.

## Screen-state interaction

The width projection is independent from semantic state. Default, focused, pressed, selected, disabled, pending, success, failure and error states retain their meaning at every supported width.

## Premium rule

Adaptive layout may change density and information placement, but must not remove the primary player action or change gameplay semantics.

## Accessibility

State meaning must remain available through semantics and visual indicators; color is never the sole state channel. Large text and RTL are handled by the existing locale-layout contract.

## Verification

`tests/test_premium_surface_projection.py` verifies compact, medium and expanded projections and invalid-width handling.

Physical Android rendering remains an open evidence gate; this contract is not a substitute for device proof.
