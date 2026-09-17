# Choice Kingdom — Faction System Contract v1

Status: DESIGN-CLOSURE ARTIFACT
Scope: D9 Faction System

## Purpose

The Faction screen explains constituencies that matter to the kingdom and makes their current stance legible without reducing complex or uncertain politics to a simplistic good/evil visual.

## FactionCard anatomy

1. faction identity/name;
2. current stance label;
3. concise explanation of known position;
4. relevant relationship/context indicators;
5. linked history/evidence where available.

## Stance states

| State | Meaning |
|---|---|
| Positive | Current game state records a supportive stance. |
| Neutral | No positive or negative stance is currently recorded. |
| Negative | Current game state records an opposing stance. |
| Mixed | Available signals do not resolve to a single direction. |
| Uncertain | Evidence/state is insufficient to determine the stance. |
| Unavailable | The faction exists but its current stance cannot be exposed. |

The UI must not collapse `mixed` or `uncertain` into positive/negative.

## Visual language

Every stance has at least two semantic channels: explicit text/icon plus surface/border treatment. Accent color is supplementary. No faction identity may depend on a good/evil color convention.

## Content boundaries

- Show only player-facing information supplied by the game state.
- Do not reveal internal rule identifiers, hidden thresholds, or future outcomes.
- If a faction has no current actionable relationship, retain explanatory context rather than inventing an action.

## Responsive and localization behavior

- Faction names and descriptions wrap without clipping.
- At 360dp, secondary metadata stacks before primary text is reduced.
- RTL mirrors layout without changing the meaning of stance.
- CJK expansion and large-text mode increase vertical space as needed.
- Minimum interactive targets remain 48dp.

## Accessibility

- FactionCard is a semantic group.
- Stance is announced as text with its icon meaningfully labelled.
- Decorative faction art is not used as the only state carrier.
- Focus order is identity → stance → explanation → related actions/links.

## Acceptance criteria for D9 closure

- [x] FactionCard anatomy defined.
- [x] Positive/neutral/negative/mixed/uncertain/unavailable states defined.
- [x] Mixed and uncertain states protected from binary flattening.
- [x] Good/evil color coding explicitly prohibited.
- [x] Hidden-information boundary defined.
- [x] Responsive/RTL/CJK/large-text behavior defined.
- [x] Accessibility and focus semantics defined.

D9 closure evidence: this contract plus the production token contract and screen matrix completes the design-level Faction specification. Runtime implementation and device QA remain separate gates.
