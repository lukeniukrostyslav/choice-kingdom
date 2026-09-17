# Choice Kingdom — Realm Dashboard Contract v1

Status: DESIGN-CLOSURE ARTIFACT
Scope: D6 Realm / Kingdom Dashboard

## Purpose

The Realm screen gives the player a compact, readable model of the kingdom's current condition. It summarizes state; it does not replace the Event decision flow and does not expose internal rule-engine details.

## Information hierarchy

1. Kingdom identity and current overall condition.
2. Primary resources / realm indicators.
3. Active delayed effects and their status.
4. Relationships and factions that materially affect the current realm state.
5. Secondary context and history links.

## Required states

| State | Required behavior |
|---|---|
| Sparse | Show only available indicators; never leave unexplained empty containers. |
| Full | Preserve hierarchy; group related indicators rather than shrinking typography. |
| Improving | Explicit positive state label/icon plus value/change where available. |
| Worsening | Explicit negative state label/icon plus value/change where available. |
| Stable | Explicit neutral/stable label; do not imply that no future change is possible. |
| Pending | Separate delayed effects from already-applied effects. |
| Unavailable | Explain why data is unavailable when that explanation is safe to expose. |

## Resource strip

- Minimum touch-safe height: 48dp.
- Indicators use icon + label + value/state; color is supplementary.
- Values must not be the only semantic signal.
- When width is constrained, secondary metadata wraps or moves below the primary value before the primary text is reduced.

## Delayed effects

Each delayed effect exposes:

- a player-facing name;
- current status (`pending`, `resolved`, or `unresolved`);
- a concise explanation of what is known;
- timing only when the game model actually exposes timing.

Do not invent dates, probabilities, or hidden outcomes.

## Relationships and factions

- Show the subject/faction identity before its state.
- Use explicit stance labels such as positive, neutral, or negative.
- Mixed or uncertain states must not be flattened into a binary good/bad presentation.
- Long names wrap without clipping.

## Empty and sparse state

An empty section is replaced by a concise explanatory empty state. The screen must not look broken because the realm currently has no active delayed effects, relationships, or faction changes.

## Responsive / RTL / accessibility

- Content margin: 16dp.
- Minimum interactive target: 48dp.
- Preferred choice/action height: 56dp where applicable.
- At 360dp, secondary content stacks before primary content becomes smaller.
- RTL mirrors layout without changing semantic order.
- Large text increases content height rather than shrinking below the token minimums.
- Screen-reader labels identify indicator, value, and state as one coherent semantic unit.
- State is communicated through text/icon plus surface or border treatment, never color alone.

## Acceptance criteria for D6 closure

- [x] Information hierarchy defined.
- [x] Sparse/full/improving/worsening/stable/pending/unavailable states defined.
- [x] Resource strip behavior defined.
- [x] Delayed-effect information boundary defined.
- [x] Relationship and faction presentation defined.
- [x] Empty/sparse behavior defined.
- [x] Responsive, RTL, large-text, and semantic behavior defined.
- [x] Design remains presentation-only and does not define gameplay authority.

D6 closure evidence: this contract plus `DESIGN_TOKENS_V1.json` and the screen matrix completes the design-level Realm specification. Runtime implementation and device QA remain separate gates.
