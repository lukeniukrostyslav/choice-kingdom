# Choice Kingdom — Premium Design P6 Choice Experience QA v1

Status: **P6 VISUAL + RUNTIME STATE PROOF — 46%**

Date: 2026-09-17

## Evidence

- Visual implementation: `web-preview/design-choice-experience-p6.html`
- Runtime presentation contract: `runtime/presentation.py`
- Event + Choice host: `runtime/event_screen.py`
- Runtime regression coverage: `tests/test_event_screen_runtime.py`

## Verified in source

- Choice is the dominant visual action surface.
- Two decision options have distinct action labels and trade-off descriptions.
- Choice targets are comfortably above the project minimum interactive target and use a preferred large decision surface.
- Idle, focused, selected, pressed, blocked and resolving states are explicit visual/runtime interaction concepts.
- Runtime `FOCUSED`, `SELECTED`, `PRESSED`, `BLOCKED`, and `RESOLVING` states are distinct rather than collapsing review, press, temporary lock and resolution into one state.
- The visual proof exposes `BLOCKED` as a first-class inspection state and keeps both actions visibly present while communicating temporary unavailability.
- Blocked controls expose an explicit accessibility state with `aria-disabled`, rather than relying only on opacity or visual styling.
- Choice controls reference the live interaction status for assistive technology without exposing hidden future consequences.
- Selection is a non-mutating review state; gameplay is not changed until the canonical choose operation.
- Focus/selection/press/begin/block transitions do not mutate the gameplay snapshot.
- A temporary `BLOCKED` state is available to the host for transition locks without inventing gameplay outcomes.
- Terminal-session choices are explicitly projected as disabled rather than silently disappearing.
- Resolved state is represented after canonical `GameSession.choose()` returns successfully.
- Error state is represented at the presentation boundary without converting an engine exception into a gameplay outcome; the original failure remains raised to the caller.
- Selection does not reveal hidden future consequences.
- Selected state remains reviewable rather than immediately mutating gameplay.
- Reset returns the visual surface to a clean idle state.
- Focus-visible treatment is explicit.
- Theme toggle demonstrates the same hierarchy in light/dark presentation.
- RTL mode mirrors the choice affordance and marker placement.
- Reduced-motion preview removes transition behavior.
- Small-width layout collapses detail panels and preserves choice hierarchy.
- The runtime presenter remains a presentation layer over `GameSession`; it does not calculate gameplay effects or routing.
- Regression coverage verifies focus/selection/press/begin/block do not mutate the gameplay snapshot and verifies the disabled terminal projection.
- No canonical IDs, factions, relationships, or gameplay effects are invented by the visual proof.

## Remaining P6 gates

- Complete authored choice-family coverage across the production catalog, rather than one proof surface.
- Full rendered verification of every runtime state against the visual state family.
- Consequence transition handoff to P7.
- Final production artwork and provenance/licensing.
- Full localization/long-string/CJK/Arabic/Hebrew validation.
- Android visual runtime integration.
- Rendered Vercel/mobile inspection and physical-device QA are deferred to their final gates.

## Percentage rule

P6 is **46%**: the choice surface now has explicit visual/runtime review, tactile, temporary-lock and resolution semantics, plus an accessible blocked-state presentation with live status semantics. Full authored catalog coverage, final artwork, localization, Android and rendered/device validation remain open.
