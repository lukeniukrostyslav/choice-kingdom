# Choice Kingdom — Android Adaptive Design Contract v1

## Purpose

Define the presentation boundary for Android window adaptation without duplicating gameplay semantics.

## Window strategy

| Window | Navigation | Content |
|---|---|---|
| Compact | Bottom bar | Single pane |
| Medium | Navigation rail | Single/supporting pane |
| Expanded | Two-pane | Related content may remain visible together |

The contract is based on the **current app window**, not a hard-coded device model. Android guidance recommends window-size-class-driven layouts and state continuity across resize, rotation, fold/unfold and multi-window transitions. citeturn0search2turn0search4

## Safe content

Interactive content must remain inside the safe-content bounds after system bars, cutouts and gesture insets are applied. The platform-neutral runtime contract is `runtime/safe_area.py`; Android-facing composition uses `runtime/android_adaptive_contract.py`.

## Continuity

Resizing or changing posture changes presentation policy only. `GameSession` remains the canonical gameplay state and must not be recreated merely because the window layout changes.

## Compose binding direction

The eventual Android layer should use the current Material 3 Adaptive primitives rather than maintaining separate device-specific screen trees. The library provides adaptive navigation and pane scaffolds, and current releases include support for larger window classes and saveable pane state. citeturn0search0turn0search11

## Exit evidence

- compact/medium/expanded contract implemented
- safe-content dimensions represented
- invalid window dimensions rejected
- presentation-only boundary preserved
- Android physical/device proof remains open
