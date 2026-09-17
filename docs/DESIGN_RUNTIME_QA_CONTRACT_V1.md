# Choice Kingdom — Runtime Design QA Contract V1

## Purpose

This contract defines the minimum runtime evidence required before a visual/design block can be marked GREEN. It complements the static design contract and prevents a visually complete screen from being counted as complete when browser runtime defects remain.

## Gate A — document integrity

Every registered preview surface must:

- return HTTP 200 from the local static server;
- expose a non-empty document body;
- expose a document title;
- render without horizontal overflow at all registered viewports.

## Gate B — browser runtime integrity

Every registered preview surface must render with:

- zero uncaught `pageerror` events;
- zero browser `console.error` messages;
- zero failed network requests;
- zero broken `<img>` elements after network idle.

A failure in any of these categories keeps the visual regression gate RED.

## Gate C — authored artwork integrity

The five canonical authored assets must remain directly addressable:

1. `artwork/event-empty-granary.svg`
2. `artwork/queen-elira.svg`
3. `artwork/lord-cael.svg`
4. `artwork/river-compact.svg`
5. `artwork/ending-chronicle.svg`

Each asset must return successfully from the preview server. Main-flow references must use repository-local assets rather than external image dependencies.

## Gate D — responsive evidence

The regression matrix must include:

- 360×800 — narrow mobile;
- 412×915 — modern mobile;
- 412×1000 — tall mobile;
- 1440×900 — desktop review.

The narrow mobile cases are the primary anti-overflow gate. Desktop evidence is a layout sanity check and is not a substitute for mobile evidence.

## Gate E — accessibility presentation

The main game-flow surface must retain:

- a skip-to-content mechanism;
- meaningful heading targets for screens;
- visible keyboard focus states;
- live-region support for state/choice feedback;
- meaningful alternative text for authored artwork;
- reduced-motion handling;
- large-text and RTL presentation controls.

## Gate F — state continuity

Visual QA must not invalidate the interactive contract. A selected choice must remain represented across the consequence, Realm, People, History, and Ending surfaces. Presentation preferences must not mutate story state.

## Evidence policy

A block may be raised only when its completion rule has executable or auditable evidence. A green repository commit alone is not visual evidence. A successful architecture workflow alone is not visual evidence.

## Current implementation

The GitHub Actions visual regression workflow enforces Gates A–D and records a machine-readable manifest plus screenshots. The workflow also captures runtime console errors, page errors, failed requests, and broken-image counts so failures are actionable rather than purely visual.

Gates E–F remain part of the design review contract and must be retained during subsequent UI changes.
