# DECISION LOG — Choice Kingdom

## D001 — Separate project

Choice Kingdom is a separate repository and product. It must not be mixed into `rulebreak8`.

## D002 — Original game

The project may learn from the broad decision-game genre and market philosophy of Reigns, but it must not become a clone. World, characters, writing, visuals, UI, event content, and mechanics must be independently created.

## D003 — Premium model

Target a one-time purchase rather than ads, subscriptions, or mandatory online monetization.

## D004 — Offline-first

Core gameplay must remain playable without an internet connection.

## D005 — Systemic consequences

The core differentiator is a real state/history system in which decisions can cause delayed consequences. Consequences should emerge from data and rules rather than from a purely linear script.

## D006 — Data-driven content

Events, choices, conditions, effects, characters, and endings should be represented as data/contracts so the content catalog can scale without rewriting the engine.

## D007 — Early vertical-slice proof

A real vertical slice remains a required engineering proof, including persistence and delayed consequences. It must not be mistaken for the full-game content gate.

## D008 — Reusable engine

Architecture should allow the decision engine to support future original themes without coupling the engine to kingdom-specific story content.

## D009 — Evidence-based readiness

Completion percentages must reflect verified implementation, not intentions. Physical Android QA, production signing, and store publication remain owner-controlled gates.

## D010 — Content before engine, APK last

The project is now governed by a stricter development order: fully author and QA the campaign first, reconcile E01–E270 into a canonical production catalog, then freeze machine-readable contracts, then implement the decision engine and UI. Localization/tests follow the real content model. Android integration and APK are late gates, with production AAB/release last.

This decision supersedes the earlier workflow implication that architecture/vertical-slice implementation should precede substantial content expansion. The vertical slice is still required, but it must validate the real production contracts after the campaign is sufficiently stable; it is not a reason to build a shallow demo first.
