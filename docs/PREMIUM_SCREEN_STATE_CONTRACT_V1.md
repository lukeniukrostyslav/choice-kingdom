# Choice Kingdom — Premium Screen State Contract V1

Status: ACTIVE — canonical cross-screen visual state vocabulary

## Purpose

Every production-facing screen must communicate interaction and outcome states consistently. This contract is presentation-only: it never calculates gameplay outcomes or mutates `GameSession`.

## Shared interaction states

Every screen supports the minimum vocabulary:

- default
- focused
- pressed
- disabled
- selected where applicable

Meaningful screens add outcome states:

- Event: selected, pending, error
- Investigation: selected, pending, success
- Ending: success, failure
- Settings: selected, error

## Premium rendering rules

1. Every state has both a visual indicator and an accessible semantic label.
2. Color alone must never carry state meaning.
3. Focus must remain visible with keyboard, switch, touch-accessibility and large-text configurations.
4. Pressed/confirmed feedback must use the existing semantic motion + audio/haptic vocabulary where appropriate.
5. Pending states remain readable without animation; reduced motion removes decorative movement but keeps the state visible.
6. Disabled states explain why an action is unavailable when the reason is useful to the player.
7. Long strings must reflow rather than clip or silently truncate critical meaning.
8. RTL mirrors directional layout while preserving icon semantics unless an icon is inherently directional.
9. Compact/Medium/Expanded layouts may reflow or reveal panes, but state meaning remains invariant.
10. No state contract may invoke gameplay logic or alter canonical session state.

## Cross-screen evidence target

Representative proof is required for Event, Realm, History, People, Investigation, Ending and Settings in compact, medium and expanded layouts, plus RTL, large text, reduced motion and keyboard-focus cases where supported.

## Exit gate

This contract contributes to P6/P7/P8/P9/P10/P11/P12/P13/P14/P15/P16/P18/P19/P20/P21/P22/P24/P25, but none of those blocks reaches 100% from this contract alone. Each requires rendered representative proof and regression evidence.
