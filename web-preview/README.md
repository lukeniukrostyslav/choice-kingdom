# Choice Kingdom — Design Vertical Slice

A Vercel-ready static visual implementation of the production design contract.

## Scope

- Real authored E01 — The First Petition content from `docs/EVENT_CATALOG.md`.
- Event hierarchy: top bar → resources → art → title → narrative → character context → choices.
- Choice A/B states with immediate consequence feedback.
- Realm, History, People/Factions and Settings surfaces.
- Semantic dark/light themes.
- Large-text reflow.
- Reduced-motion mode.
- RTL layout preview.
- 48dp+ interaction target intent and 56dp+ choice surface intent.
- No hidden future consequences are displayed as current facts.

## Deployment

This directory is static and can be deployed directly to Vercel. Set the Vercel project root to `web-preview`.

## Boundary

This is the web visual vertical slice, not the Android runtime. It intentionally keeps the presentation contract separate from the Python `GameSession` implementation until the Android/web runtime bridge is built.
