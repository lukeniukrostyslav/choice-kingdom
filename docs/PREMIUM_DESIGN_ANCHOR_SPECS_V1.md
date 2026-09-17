# Choice Kingdom — Premium Visual Anchor Specifications v1

Status: **P1 EVIDENCE / ANCHOR SPECIFICATION**

This document converts the Avelune Premium Art Bible into inspectable representative surface specifications. It is intentionally implementation-oriented: these anchors are the visual references that P2–P5 must preserve.

## 1. Anchor philosophy

The anchor set is deliberately small. It establishes a visual grammar before mass asset production:

- character portrait;
- secondary character portrait;
- faction mark;
- event illustration;
- realm/environment composition;
- consequence-state composition;
- ending composition.

An anchor is accepted only when it is readable at mobile size, respects the existing design tokens, preserves narrative hierarchy, and can survive light/dark, RTL and long-string conditions.

Industry mobile-art practice similarly emphasizes strong silhouette/proportion, controlled detail and consistency across large asset sets rather than maximizing raw fidelity everywhere. citeturn0search2turn0search8

## 2. Global art-direction acceptance

### Required
- Editorial + painterly + historical-fantasy tone.
- Warm parchment/stone neutral foundation.
- Deep charcoal-brown ink rather than pure black.
- Slate authority, aged amber warning, muted forest stability, restrained antique-gold chronicle accents.
- One dominant light direction per illustration.
- Quiet background behind the focal subject.
- Architectural/chronicle motifs used sparingly.
- No glossy F2P/gacha treatment.
- No decorative frame that competes with the decision.

### Forbidden drift
- generic fantasy card-game chrome;
- excessive gold trim;
- plastic gradients;
- random cinematic lighting changes between related assets;
- faction-as-good/evil color coding;
- portrait anatomy or costume changes that break recurring identity;
- text baked into localized artwork unless explicitly approved.

## 3. Anchor A — primary character portrait

**Purpose:** establish the recurring-character visual grammar.

### Composition
- Portrait-first vertical crop.
- Eyes and facial landmarks remain inside the protected crop zone.
- Head/shoulders occupy approximately the visual center; enough breathing room for UI overlays.
- Background communicates social environment without competing with the face.

### Rendering
- Painterly brush structure with controlled edges around eyes, mouth and key costume details.
- Skin remains natural and materially distinct from cloth/metal.
- One dominant key light plus soft environmental fill.
- Restrained rim light only when it improves silhouette separation.

### Identity anchors
- stable facial landmarks;
- stable age band;
- recognizable hairstyle/headwear;
- repeatable costume language;
- characteristic posture/expression family.

### Mobile test
At thumbnail scale the character must remain identifiable from silhouette, face placement and one costume cue.

## 4. Anchor B — secondary character portrait

**Purpose:** prove the system supports another person without visually copying Anchor A.

The secondary character must use the same lighting grammar, framing logic and rendering depth while differentiating identity through face shape, posture, costume materials and context.

Acceptance requires both portraits to look like inhabitants of the same world when viewed side-by-side.

## 5. Anchor C — faction mark

**Purpose:** establish institutional visual identity without moral coding.

Each future faction mark should define:
- primary geometric vocabulary;
- seal/emblem structure;
- material association;
- restrained accent;
- architectural/object motif.

The mark must work in:
- 24–32dp icon scale;
- character/faction card scale;
- history/investigation metadata;
- monochrome/accessibility contexts.

The mark must remain recognizable without relying on its faction accent color.

## 6. Anchor D — event illustration

**Purpose:** establish the cinematic decision surface.

### Composition
Eye path:
**character/situation → title → narrative → choice controls → consequence context.**

Artwork must leave a clean UI-safe region and a crop-safe focal region. Faces, hands carrying meaningful props and critical action must not sit inside likely text/button occlusion zones.

### Treatment
- Highest visual detail tier.
- Controlled atmospheric depth.
- Strong foreground/midground/background separation.
- Background detail decreases away from the focal subject.
- UI remains cleaner than the illustration.

## 7. Anchor E — realm/environment

**Purpose:** establish Avelune as a place rather than a menu background.

Environment should communicate:
- geography;
- social/economic condition;
- architectural identity;
- current pressure or stability;
- scale appropriate to the kingdom.

Environmental storytelling must remain subordinate to the current state information. Avoid empty fantasy landscapes with no authored relevance.

## 8. Anchor F — consequence state

**Purpose:** show that a choice changed the world without turning consequence feedback into reward spectacle.

Visual grammar:
- same world/lighting language as the event;
- visible state change;
- restrained transition cue;
- explicit semantic label/icon where required;
- no particle explosion or arcade reward language.

The player should feel that the chronicle has recorded a decision.

## 9. Anchor G — ending composition

**Purpose:** establish the highest emotional/cinematic treatment.

Ending art may use:
- stronger environmental scale;
- deeper negative space;
- more dramatic but still coherent lighting;
- a deliberate final focal symbol;
- reduced interface density.

It must still preserve text legibility and localization-safe regions.

## 10. Surface matrix

| Surface | Focal point | Detail tier | UI density | Crop risk | Main QA |
|---|---|---|---|---|---|
| Character | face/silhouette | A | medium | high | identity |
| Faction | emblem | B | low | medium | non-color semantics |
| Event | human action | A | high | high | decision hierarchy |
| Realm | place/state | B | medium | medium | environmental clarity |
| Consequence | changed state | A/B | medium | medium | semantic clarity |
| Ending | emotional/world symbol | A | low | high | cinematic hierarchy |

## 11. Light/dark behavior

Artwork must remain the visual focal point in both themes while UI semantic tokens retain their meaning. Do not simply invert artwork. Instead:

- preserve illustration contrast;
- prevent light UI cards from washing out dark artwork;
- prevent dark overlays from obscuring faces;
- keep authority/warning/stability semantics distinguishable;
- verify focus and state indicators independently of color.

## 12. RTL and localization behavior

No anchor may depend on left-to-right-only visual meaning unless the element is explicitly non-mirrored artwork.

- Directional UI composition mirrors.
- Character gaze may remain compositionally stable when mirroring would damage narrative intent.
- Text-safe regions must tolerate expansion.
- Arabic/Hebrew and CJK must not collide with focal artwork.
- Critical text should remain live UI text, not embedded lettering.

## 13. Visual inspection checklist

For every anchor, inspect at:
- 360dp portrait;
- 412dp portrait;
- large-text mode;
- light theme;
- dark theme;
- RTL layout;
- long-string stress;
- thumbnail scale.

Record PASS/FAIL and the concrete defect rather than a subjective score.

## 14. P1 evidence rule

P1 may advance beyond 35% only from actual representative visual surfaces or renderable previews. Written specifications alone do not constitute visual completion.

P1 reaches 100% only when all seven anchors have representative implementation/evidence and the inspection matrix passes.
