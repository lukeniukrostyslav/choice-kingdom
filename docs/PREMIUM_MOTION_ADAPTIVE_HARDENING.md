# Premium Motion + Adaptive Hardening

Status: ACTIVE design execution evidence

## Purpose

Harden P20, P21, P22 and P24 with concrete production-facing contracts rather than treating preview behavior as completion.

## Motion contract

- Every meaningful state change has an observable transition; avoid instantaneous replacement for primary navigation/state changes.
- Motion communicates causality: enter, confirm, pending, success, failure and escalation use distinct semantic patterns.
- Motion remains interruptible and must not block the next valid player action.
- Reduced-motion removes decorative movement while preserving state, hierarchy and causal information.
- Avoid unnecessary scale, spin, multi-axis and persistent peripheral motion for accessibility-sensitive states.
- Prefer responsive/spring-like interpolation for interactive movement where the runtime platform supports it.

## Adaptive layout contract

- Treat compact/medium/expanded widths as layout classes, not device-specific hacks.
- Preserve safe-area clearance and never allow primary controls to intersect system bars.
- Prevent stretched full-width components; constrain reading surfaces with a maximum content width.
- Long content must remain reachable through scrolling rather than being clipped.
- Preserve transient presentation state through window-size changes.
- RTL must mirror spatial relationships without reversing semantic meaning.
- Large-text mode must increase readability without hiding the primary action.

## Accessibility proof targets

- Interactive touch targets: minimum 48dp-equivalent on touch surfaces.
- Small text contrast: target at least 4.5:1; large text/graphics: at least 3:1.
- Every non-text interactive element has an accessible name/description.
- Reduced-motion mode is testable independently from normal motion.
- Focus/keyboard order follows visual reading order where keyboard input exists.

## Execution checklist

- [ ] Map semantic motion states to production-facing components.
- [ ] Add responsive stress cases for long strings and large text.
- [ ] Add RTL mirror assertions on key journey surfaces.
- [ ] Add safe-area/edge-to-edge assertions.
- [ ] Add motion-duration/non-zero transition assertions.
- [ ] Verify replay/crisis surfaces retain semantic state when motion is reduced.
- [ ] Keep P24 below 100% until real Android device-class evidence exists.
- [ ] Keep P25 below 100% until cross-screen regression evidence is complete.

## Benchmark sources

- Android quality: https://developer.android.com/quality/user-experience
- Android adaptive/resizability: https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability
- Android accessibility: https://developer.android.com/guide/topics/ui/accessibility/apps
