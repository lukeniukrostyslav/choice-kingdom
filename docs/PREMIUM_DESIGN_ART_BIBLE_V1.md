# Choice Kingdom — Avelune Premium Art Bible v1

Status: **P1 IN PROGRESS — DIRECTION LOCK DRAFT**

This is the visual source of truth for the Premium Design phase. It extends the closed V1–V18 design specification; it does not replace it.

## 1. Creative north star

Choice Kingdom should feel like a **premium illustrated chronicle of a living kingdom** rather than a generic mobile card game.

The player should perceive three things immediately:

1. **People matter.** Faces, posture, costume and relationship context carry emotional weight.
2. **Decisions matter.** The choice surface is the visual climax of each situation.
3. **The kingdom remembers.** History, consequences and endings should feel authored and cumulative.

The visual language is therefore **editorial + painterly + historical-fantasy**, with restrained ornament and strong cinematic composition.

Avoid a glossy F2P/gacha look, generic fantasy UI packs, excessive gold decoration, plastic gradients, noisy particle effects, cartoonishly heroic faction coding, or UI that visually overwhelms the narrative.

## 2. Visual hierarchy

Every screen follows this priority:

**human/story focal point → decision or state change → supporting information → navigation.**

Decorative treatment must never compete with the decision, character expression or consequence.

For Event screens, the eye path is:

**art / face → situation title → narrative → choices → consequence context.**

For People screens:

**portrait → identity → relationship/context → history → secondary metadata.**

For Realm/History/Investigation:

**current state → causal information → supporting detail.**

## 3. Shape language

- Primary surfaces: quiet, architectural rectangles with restrained radius.
- Secondary surfaces: cards/panels with subtle framing, not ornamental boxes everywhere.
- Interactive controls: confident, tactile silhouettes; no toy-like bubbles.
- Decorative motifs: arches, ruled lines, seals, manuscript/chronicle geometry used sparingly.
- Character silhouettes: distinctive through clothing, posture and props rather than exaggerated anatomy.
- Faction marks: symbolic and culturally grounded; never default moral symbols.

Existing radius/touch rules remain authoritative: card/choice radius 12dp, minimum target 48dp, preferred choice height 56dp.

## 4. Palette direction

The existing semantic token palette is the foundation and must remain authoritative for interaction meaning.

Core roles:

- Canvas: warm parchment/stone neutral.
- Card: warm ivory / aged paper neutral.
- Elevated: clean light surface for modal emphasis.
- Primary ink: deep charcoal-brown rather than absolute black.
- Secondary ink: muted warm grey-brown.
- Authority: desaturated slate blue.
- Warning: aged amber/ochre.
- Stability: muted forest green.
- Chronicle/royal emphasis: restrained antique gold.

Existing token values remain the implementation source of truth; this bible defines their artistic role rather than introducing competing runtime values.

## 5. Lighting

Default illustration lighting:

- one readable dominant light direction per scene;
- soft environmental fill;
- controlled edge/rim light only when it improves separation;
- faces receive priority exposure;
- backgrounds are allowed to fall quieter than the focal subject;
- no arbitrary multi-direction lighting between assets in the same family.

Character portraits must preserve the same lighting grammar across the codex.

## 6. Materials

Avelune materials should communicate age, use and social status.

Preferred material vocabulary:

- worn wood;
- hammered or aged metal;
- stone with restrained surface variation;
- woven cloth and leather;
- wax/seal details;
- parchment/paper where narratively appropriate;
- occasional glass, enamel or precious metal for high-status objects.

Avoid universal polish. Wealth should change material quality, not turn every object into reflective fantasy chrome.

## 7. Illustration composition

Portrait mobile composition is primary.

Event illustrations must reserve a clean UI-safe region for title/narrative/choices and a crop-safe focal region for responsive layouts.

Character focal point:
- eyes/face must remain inside the protected region;
- costume silhouette should remain readable at thumbnail scale;
- hands/props may carry secondary narrative information;
- backgrounds should establish place without stealing the focal point.

Ending illustrations may use more cinematic negative space and stronger environmental scale.

## 8. Character identity rules

Every recurring character needs a stable visual identity anchor:

- facial landmarks;
- approximate age band;
- silhouette/proportion family;
- signature hairstyle/headwear where applicable;
- recurring costume language;
- faction/context cues;
- characteristic posture/expression range;
- consistent lighting and portrait framing.

Variation is allowed in pose, expression, clothing state and context, but the character must remain recognizable.

## 9. Faction visual rules

Factions communicate culture, institution and pressure — not morality.

Each faction should receive:

- a distinct geometric vocabulary;
- emblem/seal grammar;
- material preference;
- restrained accent treatment;
- architectural/object motifs;
- typography or label treatment where appropriate.

No faction gets a permanently heroic or villainous visual treatment.

## 10. UI relationship to artwork

UI must belong to the same world as the illustrations while remaining clearly interactive.

Therefore:

- UI may borrow material cues from Avelune;
- UI must remain cleaner and more legible than environmental art;
- interactive states must be obvious without relying on decoration;
- typography remains scalable and readable;
- choice cards receive the strongest interactive emphasis;
- decorative frames are subordinate to narrative content.

This follows the project rule that UI complements rather than duplicates the game-art rendering language. Industry guidance likewise recommends separating UI visual treatment enough to preserve interaction clarity while keeping it coherent with the underlying art direction. citeturn0search0

## 11. Detail budget

Detail is allocated by narrative importance:

**Tier A — maximum:** protagonist/major characters, key event illustrations, major ending art.

**Tier B — high:** recurring characters, faction identity art, realm moments, investigation anchors.

**Tier C — controlled:** secondary people, historical entries, supporting props.

**Tier D — quiet:** background decoration and non-interactive atmosphere.

The target is not maximum detail everywhere. Premium quality comes from controlled hierarchy and consistency.

## 12. Three-second mobile read

At target mobile size, a screen must communicate its primary subject and action almost immediately.

QA should test:

- focal subject recognition;
- decision/control recognition;
- separation between background and foreground;
- silhouette readability;
- text hierarchy;
- crop safety.

This is consistent with current game-art practice emphasizing readable focal hierarchy and testing assets at actual target size rather than only at full-resolution artwork size. citeturn0search11

## 13. Motion language

Motion is restrained and purposeful:

- 180ms default interaction feedback;
- 240ms emphasis where justified;
- subtle parallax/atmosphere only where it reinforces place;
- consequence feedback should feel like a state being recorded, not a reward explosion;
- reduced-motion mode removes non-essential motion.

## 14. Accessibility and localization are visual requirements

- Never communicate state by color alone.
- Preserve minimum 48dp targets.
- Keep narrative blocks fluid at large text sizes.
- Reserve safe regions for long translations.
- RTL mirrors composition without changing visual meaning.
- Avoid text embedded in final artwork when localization would require replacement.
- CJK/Arabic/Hebrew expansion must be considered before asset lock.

## 15. Asset acceptance gate

An asset cannot become final merely because it is attractive.

It must pass:

1. identity consistency;
2. palette/material consistency;
3. lighting consistency;
4. composition/crop safety;
5. target-size readability;
6. UI-safe region check;
7. localization/RTL impact check;
8. provenance/licensing record;
9. visual QA checkpoint.

## 16. Anchor set for P2–P5

The next blocks must establish a small visual anchor set before mass production:

- one primary recurring character portrait;
- one secondary recurring character portrait;
- one representative faction mark;
- one representative event illustration;
- one realm/environment composition;
- one consequence-state composition;
- one ending composition.

Every later asset family must be compared against these anchors before acceptance.

## 17. P1 completion criteria

P1 is complete only after the direction is applied to representative real surfaces and visually reviewed for consistency. A written bible alone is insufficient.

Required evidence before P1 = 100%:

- anchor set exists;
- at least one Event, People, Realm and Ending visual treatment follows the bible;
- mobile portrait composition reviewed;
- light/dark semantic mapping reviewed;
- RTL/long-string implications reviewed;
- visual drift checklist passes;
- evidence is saved to GitHub.

Current P1 status: **35% — direction system drafted and anchored to existing design tokens/contracts; representative visual application and inspection remain open.**
