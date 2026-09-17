# Choice Kingdom — Investigation / Evidence Design Closure v1

Status: CLOSED DESIGN CONTRACT

## Evidence states

| State | Presentation |
|---|---|
| discovered | Evidence is clearly identified and distinguishable from confirmed facts |
| uncertain | Uncertainty is explicit; confidence is not represented by color alone |
| corroborated | Supporting links/relationships are visible without overwhelming the primary clue |
| contradicted | Conflict is explicit and both relevant evidence paths remain inspectable |
| resolved | The evidence chain shows what was established and what remains unknown |

## Evidence chain rules

- Evidence is ordered from observation to interpretation to conclusion.
- The UI must not visually imply certainty that the underlying narrative state does not have.
- Branching evidence paths remain inspectable and cannot be silently collapsed into one answer.
- Internal identifiers never appear as player-facing evidence labels.
- Empty evidence state explains what the player can do next rather than presenting a blank panel.
- Long evidence descriptions wrap and preserve the chain structure.
- RTL mirrors layout without changing evidence relationships or meaning.
- CJK and large text use vertical expansion rather than truncation.
- Reduced motion cannot hide the appearance or resolution of evidence.

## Accessibility

Every evidence item exposes a semantic name, state, and relationship context to assistive technology. State communication uses at least two channels such as label + icon or label + border/surface.

## Closure evidence

- D10 Investigation / Evidence: 98% -> 100% design contract closure.
- Runtime evidence rendering and device QA remain separate gates.
