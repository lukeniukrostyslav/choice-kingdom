# CONTINUATION — Choice Kingdom

## Purpose

This file is the fast handoff for any future ChatGPT session or developer. Read this file first, then `AGENTS.md`, `PROJECT_STATE.md` (when present), `PLAN.md`, and `DECISION_LOG.md`.

## Repository

- GitHub: `lukeniukrostyslav/choice-kingdom`
- Project: **Choice Kingdom**
- Status: specification/initialization stage
- This project is separate from `rulebreak8`.

## What we are building

An original premium Android-first decision-and-consequence game set in an original kingdom. The player repeatedly receives short situations with two meaningful opposing choices. Choices change resources, relationships, flags, and future event availability. Some consequences appear much later and may depend on several earlier decisions.

The game should feel systemic rather than like a fixed linear novel.

## Reference boundary

The high-level genre/formula may be inspired by decision-driven games such as Reigns, but **do not copy** its world, characters, text, artwork, UI, event wording, distinctive presentation, or protected creative expression. The project must have its own identity and mechanics.

## Product target

- Android first
- Premium one-time purchase
- Target price approximately €2.99–€4.99
- Offline core gameplay
- No ads
- No subscription
- No mandatory backend
- Short sessions and high replayability

## Core state candidates

- Gold / economy
- Public trust
- Security / military
- Political power
- Reputation
- Character relationships
- Decision history / flags
- Pending delayed consequences

These are candidates, not final balance values.

## Required first playable slice

Do not jump straight to a huge catalog. First prove this real loop:

`event → two choices → immediate state change → decision recorded → delayed consequence scheduled → later event triggers it → save/load preserves state`

The vertical slice should also include at least one character relationship, one resource threshold, one history-dependent event, one delayed consequence, and one ending condition.

## Development order

1. Product contract
2. Architecture and data contracts
3. Decision/state engine
4. Event schema and loader
5. Persistence
6. Minimal presentation/UI
7. Vertical slice content
8. Automated contract + deterministic replay tests
9. Android build
10. Physical Android QA
11. Content expansion
12. Release/store preparation

## Important rule

Never report a percentage based merely on planned work. A percentage increase requires implementation and appropriate verification. Owner-only gates such as production signing and physical device testing must remain explicitly separate.

## Current known commits

- Product direction: `7b6a527a1f0c901724560f76af01411f0046dce0`
- Engineering rules: `774d3d7175c4efa2e9a42ad8a95a2a88e849fa9c`

## Current next action

Create the architecture/data-contract plan and then implement the minimal real decision engine. Do not modify `rulebreak8` from this repository.
