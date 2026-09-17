# Choice Kingdom — Premium Visual Drift Checklist v1

Status: **P1 QA INSTRUMENT**

Purpose: prevent visual drift as premium artwork, portraits, faction marks and UI surfaces are produced.

## A. World identity

- [ ] Avelune reads as one coherent historical-fantasy world.
- [ ] Materials communicate age/use/status rather than universal gloss.
- [ ] Architectural motifs remain coherent across screens.
- [ ] Decorative chronicle motifs are restrained.

## B. Character identity

- [ ] Facial landmarks remain stable.
- [ ] Age/proportion family remains stable.
- [ ] Signature hair/headwear remains coherent.
- [ ] Costume language remains recognizable.
- [ ] Expression range changes without changing identity.
- [ ] Lighting direction matches the character family.

## C. Illustration hierarchy

- [ ] Focal subject is obvious at thumbnail scale.
- [ ] Background does not compete with face/action.
- [ ] UI-safe region is preserved.
- [ ] Crop-safe region is preserved.
- [ ] Detail is concentrated according to narrative tier.

## D. UI/art relationship

- [ ] UI belongs to the world without becoming decorative clutter.
- [ ] Choices remain visually primary on Event screens.
- [ ] Interactive states remain obvious without color alone.
- [ ] Typography remains live/scalable.
- [ ] Artwork never obscures the action the player must take.

## E. Theme/accessibility/localization

- [ ] Light theme preserves artwork hierarchy.
- [ ] Dark theme preserves artwork hierarchy.
- [ ] RTL mirrors interactive layout correctly.
- [ ] Long translations do not collide with focal artwork.
- [ ] Large text does not collapse the decision surface.
- [ ] 48dp minimum target remains intact.

## F. Mobile quality

- [ ] 360dp portrait reviewed.
- [ ] 412dp portrait reviewed.
- [ ] Thumbnail reviewed.
- [ ] Safe-area/gesture inset respected.
- [ ] Small-screen hierarchy remains intact.

## G. Final asset gate

- [ ] Stable asset ID.
- [ ] Usage documented.
- [ ] Crop behavior documented.
- [ ] Source/provenance documented.
- [ ] License status documented.
- [ ] Visual QA checkpoint recorded.

## Defect policy

A single critical defect blocks the anchor. Critical defects include identity break, unreadable decision control, focal-art occlusion, localization collision, or state communication that depends on color alone.

Cosmetic issues are recorded and corrected before the anchor is promoted to a production reference.
