# Choice Kingdom — Consequence Feedback Contract v1

Status: DESIGN-CLOSURE ARTIFACT
Scope: D5 Consequence Feedback

## Purpose

Consequence feedback must tell the player what changed without revealing hidden future logic, internal event IDs, or outcomes that are intentionally deferred. Feedback is informational presentation, not gameplay-rule authority.

## Canonical feedback states

| State | Player-facing meaning | Required presentation |
|---|---|---|
| `immediate_positive` | A beneficial effect is now visible | state icon + explicit label + concise effect text |
| `immediate_negative` | A harmful effect is now visible | state icon + explicit label + concise effect text |
| `immediate_neutral` | A measurable change is neutral or mixed | neutral icon + explicit label + concise effect text |
| `delayed_pending` | The choice created a future consequence | pending/future label + no fabricated result |
| `relationship_shift` | A known relationship changed | affected subject + direction label + value-free explanation |
| `faction_shift` | A faction stance changed | faction identity + direction label + explanation |
| `resource_shift` | A visible realm/resource value changed | resource name + signed change + resulting state when safe to expose |
| `unresolved` | The game cannot yet expose a final consequence | unresolved label + neutral explanation |

## Ordering rules

1. Show the decision acknowledgement first.
2. Show immediate consequences second.
3. Show delayed/pending consequences separately from immediate effects.
4. Group related effects; never produce a noisy list of repeated micro-events.
5. Never imply that a delayed consequence has already happened.
6. If multiple systems change, preserve deterministic ordering: realm/resources → relationships → factions → narrative/pending.

## Information boundaries

- Do not expose internal IDs, debug keys, implementation names, or rule-engine terminology.
- Do not expose hidden future values when the design intentionally withholds them.
- Do not convert uncertainty into certainty through color, animation, wording, or iconography.
- A pending effect must remain visibly pending until the game state resolves it.
- Presentation must not invent consequences that are absent from the resolved game state.

## Interaction states

### Resolving

- Decision controls become non-interactive.
- The selected decision remains visibly selected.
- Feedback area reserves space before content arrives to avoid layout jump.
- Non-essential motion may be used only under the default motion policy.

### Resolved

- Controls return to the appropriate navigation state.
- Every displayed consequence has a textual label.
- Pending consequences remain distinct from completed consequences.
- Focus moves to the first newly available meaningful content rather than disappearing.

### Disabled / unavailable

Disabled controls must explain the condition when explanation is available. Disabled appearance cannot rely on opacity alone; label, semantics, and state must remain explicit.

## Visual semantics

State is never communicated by color alone. Each consequence uses at least two channels from:

- textual state label;
- semantic icon;
- border/surface treatment;
- optional motion for emphasis.

Color is supplementary and must use the semantic tokens defined in `DESIGN_TOKENS_V1.json`.

## Responsive behavior

- Consequence rows wrap vertically before reducing readable text size.
- Minimum interactive target remains 48dp; decision cards prefer 56dp minimum height.
- Long consequence text wraps without clipping.
- At 360dp content width, secondary metadata yields space to the primary consequence message.
- RTL mirrors the layout while preserving semantic ordering.

## Reduced motion

When reduced motion is enabled, consequence arrival uses instant or minimal fade/state replacement. No information may depend on animation to be understood.

## Acceptance criteria for D5 closure

- [x] Immediate positive/negative/neutral states defined.
- [x] Delayed/pending state explicitly separated from resolved state.
- [x] Relationship, faction, and resource consequence categories defined.
- [x] Hidden-future information boundary defined.
- [x] Resolving/resolved/disabled behavior defined.
- [x] Non-color state communication defined.
- [x] Responsive, RTL, long-text, and reduced-motion behavior defined.
- [x] Presentation explicitly separated from gameplay-rule authority.

D5 closure evidence: this contract plus the production token contract provides the complete design-level consequence feedback specification. Runtime implementation and device QA remain separate engineering gates.
