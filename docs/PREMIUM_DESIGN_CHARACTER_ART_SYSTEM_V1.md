# Choice Kingdom — Premium Character Art System v1

Status: **P2 IN PROGRESS — VISUAL PROOF 20%**

## Purpose

This document turns the premium Art Bible into a production-facing character system. Character quality is treated as a repeatable identity system, not a collection of attractive one-off portraits.

The system follows a reference-first workflow: fixed identity anchors must survive pose, expression, costume, lighting and scene variation. Mobile readability is a first-class constraint; silhouette and proportion must remain legible at small portrait sizes.

## 1. Character hierarchy

### Tier A — Hero / recurring principal
- Highest facial and costume fidelity.
- Strong silhouette readable before facial detail.
- Multiple approved views and expressions required.
- Receives the strongest lighting and material treatment.

### Tier B — Recurring secondary
- Distinct identity silhouette.
- Stable face, hair and costume anchors.
- Reduced micro-detail compared with Tier A.

### Tier C — Named supporting character
- One dominant identity cue plus stable palette/costume family.
- Must remain distinguishable from other characters at thumbnail size.

### Tier D — Background / incidental
- Simplified identity treatment.
- Must respect faction, culture and world-material rules without competing with the narrative focal point.

## 2. Fixed identity anchors

Every Tier A/B character must define:

1. Face geometry / landmark relationship.
2. Hair silhouette and signature feature.
3. Body proportion and shoulder/head relationship.
4. Signature costume element.
5. Signature accessory or emblem where applicable.
6. Primary and secondary identity colors.
7. Age-range and social-status visual cues.
8. Faction/cultural construction logic.

These are fixed. A new pose or illustration must not silently redesign them.

## 3. Controlled variables

The following may vary when explicitly requested:

- pose;
- facial expression;
- hand position;
- camera distance;
- environment/background;
- weather and atmosphere;
- costume layer when story permits;
- controlled damage/weathering;
- scene lighting within the Art Bible lighting grammar.

Only a small number of variables should change per iteration so visual drift remains observable and reversible.

## 4. Character sheet minimum

A production-ready Tier A/B reference sheet should contain:

- front neutral;
- three-quarter neutral;
- side/profile;
- full-body proportion reference;
- close face crop;
- minimum six expressions;
- default costume layers;
- signature accessory callouts;
- palette/material callouts;
- crop-safe portrait framing;
- prohibited drift examples.

A turnaround is the reference source, not automatically final in-game art.

## 5. Expression system

Required baseline expression vocabulary:

- neutral / listening;
- controlled confidence;
- concern;
- anger / confrontation;
- grief / loss;
- surprise / discovery;
- guarded suspicion;
- relief / resolution.

Expressions must modify eyes, brows, mouth and body tension together.

## 6. Portrait composition

Default mobile portrait:

- eyes/facial landmarks remain inside the crop-safe zone;
- head and shoulders dominate the frame for narrative portraits;
- hands enter frame only when they communicate story information;
- background contrast remains below the face;
- one dominant light direction;
- controlled rim light only where it improves separation;
- no decorative effects crossing eyes, mouth or critical costume anchors.

At 360dp and 412dp, the character must remain identifiable without zooming.

## 7. Material and costume logic

Character materials inherit Avelune's world grammar: worn wood, aged metal, stone, woven cloth, leather, wax/seal materials, parchment/paper, and restrained precious-metal accents for status.

Avoid universal glossy surfaces, generic fantasy armor, arbitrary neon accents and faction-coded good/evil visual shortcuts.

## 8. Lighting lock

Default lighting follows the Art Bible: one dominant key direction, soft environmental fill, restrained rim light, face-first readability, and quieter backgrounds. Dramatic lighting may vary by narrative state but must preserve identity anchors.

## 9. Mobile quality gates

Reject a variant when silhouette becomes generic, facial landmarks drift, signature identity cues disappear without narrative reason, faction/cultural construction contradicts the world bible, face loses thumbnail readability, lighting obscures expression, localization/UI overlays obscure the focal area, or the character becomes visually louder than the decision surface without narrative justification.

## 10. Consistency test protocol

For each important character, compare variants side by side at identical display size. Check silhouette, face geometry, hair mass, eye spacing, costume layers, accessory placement, body proportions, palette, lighting direction and expression readability. Two or more material identity failures block approval.

## 11. Design-system relationship

Character art plugs into:

`Character Identity → Portrait Crop → Narrative Context → Decision Surface → State Feedback`

The character is never decorative filler. In Event and Consequence surfaces, art supports the story beat while the decision/feedback hierarchy remains dominant.

## 12. Current P2 evidence

Saved:

- production character hierarchy;
- fixed vs controlled identity rules;
- Tier A/B reference-sheet minimum;
- expression vocabulary;
- mobile portrait composition rules;
- material/costume grammar;
- lighting lock;
- rejection criteria;
- repeatable consistency QA protocol;
- **first visual anchor sheet with front / three-quarter / profile proof;**
- **eight-state expression grid;**
- **compact mobile crop proof;**
- **P2 character-anchor QA record.**

Visual artifact: `docs/visual/premium-character-anchor-sheet-v1.svg`

QA artifact: `docs/PREMIUM_DESIGN_P2_CHARACTER_ANCHOR_QA_V1.md`

## Remaining P2 work

- replace the vector proof with authored-quality production character artwork;
- assign the production anchor to a canonical People character;
- expand expression proof from system glyphs to authored facial studies;
- create costume/material callouts;
- run final visual-drift QA against the Art Bible;
- validate actual Vercel/mobile rendering and later Android screenshots;
- record production artwork provenance/licensing.

## Gate impact

The first visual-proof milestone is complete. P2 advances from 10% to **20%**. No further percentage increase is allowed until the next listed evidence exists.
