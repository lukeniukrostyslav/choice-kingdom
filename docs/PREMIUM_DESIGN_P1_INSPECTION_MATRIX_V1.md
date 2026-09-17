# Choice Kingdom — P1 Art Direction Inspection Matrix v1

Status: **P1 EVIDENCE / INSPECTION PASS v1**

This matrix records the current static visual inspection of the premium anchor set. It is an evidence artifact, not a claim of physical-device or Android runtime completion.

## Inspection targets

| Anchor | 360dp | 412dp | Large text | Light | Dark | RTL | Long strings | Thumbnail |
|---|---|---|---|---|---|---|---|---|
| Primary character | PASS | PASS | PASS | PASS | PASS | PASS* | PASS* | PASS |
| Secondary character | PASS | PASS | PASS | PASS | PASS | PASS* | PASS* | PASS |
| Faction mark | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Event illustration | PASS | PASS | PASS | PASS | PASS | PASS* | PASS | PASS |
| Realm / environment | PASS | PASS | PASS | PASS | PASS | PASS* | PASS | PASS |
| Consequence state | PASS | PASS | PASS | PASS | PASS | PASS* | PASS | PASS |
| Ending | PASS | PASS | PASS | PASS | PASS | PASS* | PASS | PASS |

`*` Directional UI/text behavior is approved by design contract; final Android RTL rendering remains a later runtime gate.

## Concrete checks

### Composition
- Primary focal subject remains outside text/button occlusion zones.
- Decision controls retain primary hierarchy on the Event surface.
- Realm and consequence treatments communicate authored state rather than decorative scenery.
- Ending treatment uses reduced interface density and protected text-safe space.

### Character identity
- Portrait anchors use stable facial landmarks, silhouette and costume cues.
- Secondary character differentiates identity without leaving the same world grammar.
- Character treatment remains subordinate to narrative decision hierarchy where both coexist.

### Color and semantics
- Faction identity does not depend on a good/evil color code.
- State meaning is not communicated by color alone.
- Antique-gold accents remain restrained rather than becoming universal decoration.

### Mobile readability
- Key shapes survive thumbnail inspection.
- Choice labels remain readable in portrait composition.
- Long text is kept live rather than baked into artwork.
- Crop-safe regions protect faces and meaningful actions.

### Theme / localization
- Light and dark treatments preserve illustration focal priority.
- RTL mirrors interface composition while protected artwork can remain non-mirrored when narrative intent requires it.
- CJK/Arabic/Hebrew expansion is handled by protected live-text regions; final device validation remains open.

## Remaining P1 gate

P1 cannot be marked 100% until:

1. these static inspection results are reproduced against the actual rendered runtime;
2. Android 360dp/412dp screenshots are captured;
3. light/dark and RTL runtime screenshots are captured;
4. final production asset provenance/licensing records exist for every final asset;
5. the visual drift checklist passes on the rendered product.

## Evidence rule

This document advances P1 evidence coverage but deliberately does not convert static design evidence into physical-device QA. That separation is required by the project quality gate.

## External quality reference

Current mobile-game art practice emphasizes silhouette/proportion, controlled detail and consistency under mobile constraints rather than raw fidelity alone. citeturn0search2turn0search4
