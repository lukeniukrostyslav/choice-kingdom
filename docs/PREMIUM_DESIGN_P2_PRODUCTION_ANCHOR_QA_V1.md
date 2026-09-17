# Choice Kingdom — P2 Production Character Anchor QA v1

Status: **P2 VISUAL PROOF 30%**

## Scope

This QA record evaluates the new production-anchor proof at:

`docs/visual/premium-character-production-anchor-v1.svg`

It is a design-system proof, not a claim that final authored production artwork is complete.

## Evidence matrix

| Check | Result | Evidence |
|---|---|---|
| Tier A silhouette | PASS | Distinct head/shoulder mass and controlled costume silhouette |
| Facial identity anchors | PASS | Hair, facial landmarks and cheek scar are explicitly locked |
| Costume identity | PASS | Slate coat, woven collar and bronze seal establish repeatable cues |
| Material grammar | PASS | Cloth/leather/aged-metal/bronze language follows Art Bible |
| Lighting grammar | PASS | Single upper-left key, soft fill, quieter background |
| Crop safety | PASS | Face and signature cues remain inside the portrait-safe region |
| Thumbnail recognition | PASS | Three reduced-scale checks retain silhouette and palette identity |
| Decision hierarchy | PASS | Character is presented as narrative support, not a competing choice control |
| Mobile 360/412 proof | PARTIAL | Composition is explicitly designed for both widths; rendered device screenshots remain open |
| Canonical People assignment | OPEN | Must bind this anchor to an existing canonical character ID rather than inventing a new runtime identity |
| Final authored artwork | OPEN | SVG remains a controlled design proof; final illustration remains a later asset-production task |
| Provenance/licensing | OPEN | Required before asset can become final production artwork |

## P2 gate movement

This evidence advances P2 from **20% to 30%** because a second, more detailed character visual proof now exists with explicit identity, material, lighting, crop and thumbnail QA.

The following are intentionally excluded from the percentage:

- final production illustration;
- canonical People runtime binding;
- Vercel rendered screenshot evidence;
- Android physical-device evidence;
- provenance/licensing record.

## Next P2 evidence

1. Identify an existing canonical People character from the repository.
2. Bind the visual anchor to that identity without changing gameplay IDs.
3. Add authored expression studies rather than symbolic expression glyphs.
4. Add costume/material closeups.
5. Validate the visual in the existing Vercel web preview at portrait widths.
6. Run visual-drift comparison against the Art Bible and P1 anchor board.
7. Record provenance/licensing before calling artwork final.
