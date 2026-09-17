# Choice Kingdom — P1 Rendered Inspection Gate v1

Status: **P1 IN PROGRESS — RENDERED INSPECTION PROTOCOL LOCKED**

## Purpose

This gate converts the P1 Art Direction rules into a repeatable rendered-surface inspection before P1 can be marked complete.

## Target surfaces

1. Event + Choice
2. People / Character
3. Realm / Environment
4. Consequence State
5. Ending

## Mobile inspection sizes

- 360dp portrait — minimum reference width
- 412dp portrait — expanded reference width
- Large text / long-string pass
- RTL mirror pass

## Inspection order

### 1. Focal hierarchy

- Human/story focal point is immediately identifiable.
- Decision or state change is the second visual priority.
- Supporting information does not compete with the focal point.
- Navigation remains visually subordinate.

### 2. Character quality

- Face remains inside the protected crop region.
- Silhouette remains recognizable at mobile size.
- Costume/material cues survive reduction.
- Lighting direction matches the Art Bible.
- Expression communicates narrative state without relying on text alone.

### 3. Environment quality

- Environment establishes place without overpowering the subject.
- Detail density is lower away from the focal region.
- Materials follow the Avelune vocabulary.
- No generic fantasy/gacha ornament is introduced.

### 4. Decision surface

- Choice controls are visually dominant when a decision is available.
- Touch targets remain at least 48dp.
- Selected/resolving/disabled states remain distinguishable without color alone.
- Long localized labels do not destroy hierarchy.

### 5. Consequence surface

- Consequence reads as a recorded state change, not a reward explosion.
- The affected realm/person/history context is visually connected to the outcome.
- Motion, if present, is restrained and purposeful.

### 6. Ending surface

- Ending art has stronger cinematic scale than ordinary event art.
- Negative space protects narrative/title content.
- The final state feels cumulative and authored.

## Theme pass

### Light

- Ink remains readable against warm neutral surfaces.
- Accent colors retain semantic meaning.
- Art and UI remain visually coherent.

### Dark

- Focal art remains separated from UI.
- Secondary information does not become visually dominant.
- Contrast remains sufficient for critical text and controls.

## Localization / RTL pass

- RTL mirrors composition without reversing narrative meaning.
- No text is baked into final art where translation is required.
- CJK/Arabic/Hebrew expansion has safe space.
- Long strings do not clip, overlap or force decorative elements over content.

## Critical defects

Any of the following blocks P1 closure:

- focal character obscured by UI;
- unreadable decision control;
- identity inconsistency between character anchors;
- localization collision or clipping;
- state communicated only through color;
- lighting/material grammar visibly drifting between anchor surfaces;
- decorative treatment overpowering the narrative decision;
- provenance/licensing record absent for an asset claimed as final.

## Evidence rule

P1 reaches 100% only when the rendered/runtime surfaces have been inspected and the evidence is saved alongside the design system. A specification, mockup, or written checklist alone cannot close this gate.

## Current status

**P1 remains 70%.** This document locks the final inspection procedure; it does not claim the inspection has already passed.

After the actual rendered inspection and provenance gate pass, P1 may close and P2 Character Art System becomes the active block.
