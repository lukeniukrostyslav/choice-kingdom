# Choice Kingdom — Character System Contract v1

Status: DESIGN-CLOSURE ARTIFACT
Scope: D8 Character System

## Purpose

The Character screen explains who a person is, why they matter, and what the player already knows about their relationship to the kingdom. It must never invent personality, motive, availability, or relationship state that is absent from game data.

## CharacterCard anatomy

1. portrait or explicit portrait-unavailable treatment;
2. player-facing name and role;
3. current relationship/stance state when known;
4. concise known context;
5. relevant history links;
6. availability/status only when provided by the game state.

## Portrait rules

- Missing portrait uses a deliberate neutral placeholder treatment, never a broken-image artifact.
- Portrait crop preserves face/identity priority.
- Asset provenance belongs to the asset system; the screen does not imply ownership or licensing.

## Relationship states

Supported presentation states:

- positive;
- neutral;
- negative;
- uncertain;
- unavailable.

Each state has an explicit label/icon. Color is supplementary.

## Long names and content

- Names wrap before truncation.
- Long roles/context wrap vertically.
- Large-text mode increases card height rather than reducing the required text size.
- CJK and RTL content must remain readable without clipping.

## Availability boundary

If a character is not currently available, the UI states only the player-facing reason supplied by the game state. It does not expose internal gating rules, debug identifiers, or hidden future requirements.

## Accessibility

- CharacterCard is one semantic group.
- Portrait has meaningful alternative text when it conveys identity; decorative art is marked decorative.
- Relationship state is read as text, not inferred from color.
- Focus order follows name → state → context → history/actions.
- Interactive actions meet the 48dp minimum target.

## Acceptance criteria for D8 closure

- [x] CharacterCard anatomy defined.
- [x] Missing portrait behavior defined.
- [x] Relationship state model defined.
- [x] Availability information boundary defined.
- [x] Long-name/large-text/CJK/RTL behavior defined.
- [x] Accessibility semantics and focus order defined.
- [x] Asset provenance separated from presentation.

D8 closure evidence: this contract plus `DESIGN_TOKENS_V1.json` and the screen matrix completes the design-level Character specification. Runtime implementation and device QA remain separate gates.
