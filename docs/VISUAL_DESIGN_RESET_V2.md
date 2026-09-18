# Choice Kingdom — Visual Design Reset v2

Status: **ACTIVE — CANONICAL PREMIUM VISUAL RESET**

Date: 2026-09-18

## Purpose

Visual Design Reset v2 restarts the **premium visual implementation track P1–P25** without restarting Choice Kingdom itself.

The approved reference recorded in `design-reference/FINAL_DESIGN_VISION_V1.md` is the sole visual north star for this track. Legacy visual surfaces are frozen as historical/technical material; they are not treated as the source of truth for new visual decisions.

## What is preserved

- canonical gameplay/runtime and session logic
- Android foundation and build infrastructure
- tests and CI infrastructure
- reusable technical presentation contracts where they do not dictate obsolete visual styling
- Git history and existing repository structure

## What is reset

- premium visual styling
- visual tokens and material language
- typography hierarchy
- layout composition
- screen-by-screen visual treatment
- responsive visual composition
- motion/feedback language
- visual accessibility treatment
- cross-screen visual consistency

## Non-negotiable visual direction

Every new P1–P25 implementation must converge on the approved Avelune reference:

- cinematic medieval-fantasy atmosphere
- monumental castle/city, mountains, water, forests, roads and regional-world depth
- deep blue-black / charcoal foundation
- restrained warm-gold metal accents
- elegant high-contrast serif display typography
- highly readable supporting text
- layered refined panels with controlled translucency/opacity
- authored atmosphere without sacrificing readability
- choices presented as consequential decisions
- generous spacing and strong information hierarchy
- cinematic consequence, investigation, history and ending presentation
- calm premium settings/accessibility surfaces
- compact phone, medium tablet/foldable and expanded layouts that reflow rather than become unrelated designs
- RTL, large text, long strings, safe areas and reduced motion are part of the visual contract

## Implementation order

1. P1 — visual foundation / art direction
2. P2–P5 — shared visual system
3. P6–P12 — core gameplay-facing surfaces
4. P13–P19 — supporting narrative/navigation surfaces
5. P20–P25 — motion, accessibility, localization, Android adaptation and final QA

Work is intentionally grouped into meaningful visual passes instead of accumulating isolated cosmetic patches.

## Percentage policy

The previous P1–P25 percentages are **retired for the V2 visual implementation track**. They measured a mixed legacy state and therefore must not be carried forward as if the new visual reset had already been completed.

V2 percentages measure only demonstrable progress toward the new visual implementation. A block reaches 100% only after implementation, responsive behavior, accessibility requirements and regression evidence are present.

## Current V2 baseline

- P1–P14: 100% — rebuilt on the V2 visual foundation and closed with executable regression evidence
- P15: 90% — V2 implementation complete at the surface-contract level; V15 regression verification pending
- P16–P25: 0% — next blocks to rebuild sequentially

## Rule against invention

Do not invent a competing visual direction. Where the reference does not specify a detail, choose the smallest neutral implementation that preserves its hierarchy, material language and atmosphere; do not introduce unrelated themes, palettes or dashboard-like patterns.
