# Choice Kingdom — Art Production Bible V1
Status: ACTIVE — CANON-LOCKED ART DIRECTION / NO-INVENTION CONTRACT
Date: 2026-09-19

## 1. Purpose
This document defines the production-art rules for Choice Kingdom. It is derived only from the current repository canon: README.md, PROJECT_STATE.md, docs/STORY_BIBLE.md, docs/UI_DESIGN_SYSTEM.md, docs/CANONICAL_STATE_VOCABULARY.md, docs/EVENT_GRAPH.md, design-reference/FINAL_DESIGN_VISION_V1.md, docs/VISUAL_DESIGN_RESET_V2.md, docs/PREMIUM_DESIGN_MASTER_P1_P25.md, docs/BLOCK13_RELATIONSHIP_DESIGN_CLOSURE.md, and the existing web-preview character-study assets.

This is an art-production contract, not permission to invent lore.

## 2. Non-negotiable rule
No character, costume, location, faction symbol, prop, scene, relationship, event meaning, historical fact or visual lore may be invented merely to make an image look interesting.

When the repository does not specify a visual detail:
1. preserve the approved visual language;
2. choose the smallest neutral visual treatment;
3. record the unresolved field;
4. do not silently turn an assumption into canon.

Gameplay truth remains owned by the canonical runtime/session layer.

## 3. Canonical world
World: Avelune.
Core visual world: monumental castle/city, River Vale, mountains, water, forests, roads and regional-world depth.

Tone: political drama, human-scale fantasy, dry humor, occasional warmth, and consequences that may become tragic without gratuitous grimness.

Do not introduce unrelated fantasy races or monsters, supernatural lore not present in the story bible, cartoon villains, random medieval props, or visual symbols that imply unsupported factions or relationships.

## 4. Approved visual north star
The repository's sole visual north star is design-reference/FINAL_DESIGN_VISION_V1.md.

Required visual language:
- cinematic medieval-fantasy atmosphere
- deep blue-black / charcoal foundation
- restrained warm-gold metal accents
- elegant high-contrast serif display typography
- highly readable supporting text
- layered refined panels
- generous spacing
- authored atmosphere without sacrificing readability
- consequential choice presentation
- cinematic consequence/investigation/history/ending presentation
- responsive reflow
- RTL, large text, long strings and safe areas
- reduced motion support

The supplied People reference image is the composition target for the People surface: large cinematic character portraits, refined cards, kingdom atmosphere and restrained gold detailing.

## 5. Canonical characters — identity lock

### Mara Vey
Role: Chancellor.
Core identity: disciplined administrator; believes institutions matter more than personalities.
Backstory anchor: grew up during a famine and fears disorder more than unpopular laws.
Relationship axis: institutional trust.
Narrative behavior: rewards consistency; if repeatedly ignored, may resign, preserve evidence against the Crown, or help architect a constitutional settlement after a crisis.
Existing repository visual-study anchor: reserved gaze; calm/observant treatment.

### Rowan Hale
Role: Captain; commander of the river guard.
Core identity: brave, practical, suspicious of court politics.
Goals: soldiers properly paid; civilians protected.
Risk arc: repeated empowerment can move him toward militarism.
Relationship axis: security loyalty.
Existing repository visual-study anchor: strong jaw; alert/direct treatment.

### Seris Auren
Role: Lady / old noble.
Core identity: elegant publicly, ruthless bargaining privately.
Belief: old houses help prevent mob rule.
Possible narrative states: ally, rival, reformist convert, final political opponent.
Relationship axis: aristocratic respect.
Existing repository visual-study anchor: angular fringe; measured/composed treatment.

### Ivo Renn
Role: young guildmaster and merchant organizer.
Core identity: charming, funny, dangerously good at loopholes.
Systemic role: can enrich the kingdom or turn the economy into a private toll road.
Relationship axis: commercial leverage.
Existing repository visual-study anchor: swept hairline; polished/guarded treatment.

### Sister Amara
Role: healer; keeper of the House of Lanterns.
Core identity: trusted charitable figure; dislikes court politics.
Narrative role: repeatedly involved because policy decisions affect the poor first.
Relationship axis: public conscience.
Existing repository visual-study anchor: rounded fringe; warm/resolute treatment.

### Toma Reed
Role: courier and occasional smuggler from the docks.
Core identity: knows rumors before officials do.
Possible narrative states: information source, liability, unexpectedly loyal friend.
Relationship axis: street network.
Existing repository visual-study anchor: soft side part; young/attentive treatment.

## 6. Character art requirements
Every canonical character must be recognizable across every asset.

Before mass production, each character requires a locked master sheet containing only repository-supported identity plus explicitly approved neutral visual details:
- face identity
- approximate apparent age only if supported/approved
- hair identity
- silhouette
- clothing system
- material language
- recurring accessories only if canonically supported
- front / 3/4 / side reference
- neutral expression
- approved expression range
- lighting reference
- portrait crop reference
- full-body composition reference

The master sheet becomes the source for portrait -> expression set -> event scene -> investigation scene -> ending scene -> replay/variant asset.

Do not generate the same character independently for each scene.

## 7. Art asset families
Production is organized by dependency, not by random image count.

A. Character masters
B. Character portraits and expressions
C. Avelune environments and locations
D. Event/story scenes
E. Investigation evidence and props
F. Faction/institution visual language
G. Endings/resolution art
H. UI decorative assets
I. Integration crops/variants
J. Visual QA/reference captures

A large asset count is allowed, including 1,000+ assets if the authored campaign genuinely requires it. Quantity is not a completion criterion. Every asset must have a canonical owner/use.

## 8. Asset manifest requirement
Every production asset must have:
- stable asset ID
- family
- canonical subject
- source event/screen when applicable
- character/faction IDs when applicable
- intended crop/aspect ratio
- mobile resolution requirement
- light/dark treatment if needed
- RTL neutrality where relevant
- status: brief / concept / approved / production / integrated / QA
- rejection reason when rejected

No orphan images.

## 9. Visual consistency gate
An asset is not approved because it is individually attractive.

Approval requires:
- identity consistency
- world consistency
- material/lighting consistency
- composition consistency
- mobile readability
- correct narrative meaning
- correct canonical character/faction
- no invented lore
- correct integration target

## 10. Mobile production constraints
Choice Kingdom is Android-first.

Art must survive:
- compact phones
- tall phones
- tablet/foldable/expanded layouts
- safe areas
- large text
- long localized strings
- RTL

The mobile design must preserve one primary visual focus per screen and avoid clutter. Epic's mobile design guidance similarly emphasizes clear visual hierarchy, large touch targets, reduced clutter and safe-zone-aware UI. These are implementation constraints; they do not override Choice Kingdom's canonical visual direction.

## 11. Existing SVG artwork
The existing files web-preview/artwork/people-mara.svg, people-rowan.svg, people-seris.svg, people-ivo.svg, people-amara.svg and people-toma.svg are treated as temporary character-study / integration assets, not final production character art.

Their identity-anchor notes are retained as compatibility references:
- Mara — reserved gaze
- Rowan — strong jaw
- Seris — angular fringe
- Ivo — swept hairline
- Amara — rounded fringe
- Toma — soft side part

They must not be expanded into unsupported biography or lore.

## 12. First production pass
The first real art pass is NOT 1,000 independent images.

It is:
1. Lock six canonical character master sheets.
2. Approve one production portrait per character.
3. Approve a controlled expression set per character.
4. Test the six portraits together on the People screen against the approved reference.
5. Only then propagate the locked identities into story scenes.
6. Build environment/location masters.
7. Build event-scene families.
8. Build investigation/evidence families.
9. Build ending families.
10. Integrate and run visual regression.

## 13. First block status
A1 — Canonical Art Production Bible: 100% COMPLETE as a specification/constraint lock. This does NOT mean production artwork is complete.

A2 — Six Canonical Character Masters: 0% production artwork.
A3 — Production Portrait Set: 0%.
A4 — Expression Sets: 0%.
A5 — Avelune Environments: 0%.
A6 — Story/Event Scene Library: 0%.
A7 — Investigation / Evidence / Props: 0%.
A8 — Factions / Institutions: 0%.
A9 — Endings / Resolution Art: 0%.
A10 — Integration / Visual QA: 0%.

## 14. Acceptance rule
No A2–A10 block may be marked 100% from a document, placeholder image or generated preview alone.

A production-art block reaches 100% only after:
- assets exist;
- assets are canonical;
- assets are integrated;
- target screens render correctly;
- mobile/responsive behavior is checked;
- visual regression evidence exists.

## 15. Source discipline
The repository remains the source of truth for names, roles, relationships, story facts, events, factions, endings, state vocabulary and event graph.

External research is used only for production methodology, technical constraints and general art/UI practice. It must not be used to invent Choice Kingdom lore.
