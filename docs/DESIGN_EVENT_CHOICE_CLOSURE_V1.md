# Choice Kingdom — Event + Choice Design Closure v1

Status: CLOSED DESIGN CONTRACT

This artifact closes the remaining design specification gaps for D3 Event Screen and D4 Choice System. It does not claim Android runtime implementation or physical-device QA.

## Event screen states

| State | Required visual behavior | Interaction rule |
|---|---|---|
| idle | Narrative, art, resources and available choices are fully readable | Choices are actionable |
| focused | Focus indicator is persistent and non-color-only | Keyboard/screen-reader focus must identify the choice |
| pressed | Choice acknowledges activation immediately | Prevent duplicate activation |
| resolving | Selected choice remains visually identifiable; other choices become unavailable | No second decision submission |
| resolved | Consequence feedback replaces decision affordance or clearly advances the flow | Resolved choice cannot be submitted again |
| unavailable | Choice remains understandable but visibly disabled | Explain unavailable state when meaningful |

## Event layout invariants

- Top bar never competes visually with the decision area.
- Narrative remains readable before decorative art is considered.
- Decision controls are grouped and ordered consistently.
- Critical controls respect minimum 48dp touch target and 56dp preferred choice height.
- Bottom controls respect safe-area inset plus 16dp extra spacing.
- At 360dp width, secondary content stacks before text or touch targets are compressed.
- Long narrative wraps; it never clips or overlays decision controls.
- RTL mirrors spatial layout while preserving semantic order.
- State is communicated by icon/label/border or surface treatment, not color alone.

## Choice interaction contract

1. Exactly one choice may enter `resolving` for an event decision.
2. Activation must transition `idle/focused -> pressed -> resolving -> resolved`.
3. During `resolving`, all sibling choices are disabled.
4. Repeated taps/clicks on the same choice must not create duplicate submissions.
5. Focus remains visible after state changes where the platform permits it.
6. Reduced-motion mode removes nonessential movement and uses immediate/fade transitions.
7. Large-text mode expands vertically; it must not reduce body text below the base token size.
8. The player-facing UI never exposes internal event IDs.

## Edge-case matrix

| Case | Expected design response |
|---|---|
| one choice | Keep full choice-card affordance; do not collapse into plain text |
| many choices | Preserve target size; allow vertical scrolling rather than shrinking controls |
| long choice | Wrap to multiple lines and grow card height |
| unavailable choice | Disabled state + accessible reason where available |
| consequence arrives | Replace/append feedback without losing context |
| RTL | Mirror layout, retain reading order and meaning |
| CJK | Allow glyph/line expansion without clipping |
| large text | Grow containers and scroll; never truncate critical decision text |
| reduced motion | No essential information may depend on animation |

## Closure evidence

- D3 Event Screen: 97% -> 100% design contract closure.
- D4 Choice System / States: 99% -> 100% design contract closure.
- Runtime implementation and device QA remain separate gates.
