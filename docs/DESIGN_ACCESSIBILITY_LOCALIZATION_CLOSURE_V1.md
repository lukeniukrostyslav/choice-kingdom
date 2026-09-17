# Choice Kingdom — Accessibility + Localization Design Closure v1

Status: CLOSED DESIGN CONTRACT

## Settings / accessibility controls

Settings exposes presentation controls as explicit controls with current-value feedback:

- language / locale;
- text size;
- reduced motion.

Controls use the same 48dp minimum interactive target, visible focus treatment, semantic labels, and non-color-only state communication as the rest of the product.

## RTL / localization-ready rules

- Layout direction is mirrored without changing narrative meaning.
- Text is never embedded in decorative images when it must be translated.
- Buttons and cards expand for longer translations.
- CJK line/glyph expansion is treated as a normal layout case.
- Plural/grammar-sensitive strings remain content-driven rather than concatenated UI fragments.
- Internal IDs, debug labels, and implementation terminology never leak into player-facing copy.

## Large text / responsive rules

- Base body size is 16sp; large-text scale is 1.25x from the token contract.
- Containers grow vertically rather than clipping or reducing text below the base size.
- At narrow widths, secondary content stacks before interactive targets are compressed.
- 360dp is the minimum responsive design checkpoint; 412dp is the primary wider checkpoint.
- Bottom content preserves safe-area inset plus the additional 16dp spacing token.

## Closure evidence

- D13 Settings / Accessibility Controls: 94% -> 100% design contract closure.
- D14 RTL / Localization-ready UI: 96% -> 100% design contract closure.
- D15 Large Text / Responsive Layout: 98% -> 100% design contract closure.
- D16 Accessibility / Semantics: 98% -> 100% design contract closure.
- Runtime implementation, screen-reader execution and physical-device QA remain separate verification gates.
