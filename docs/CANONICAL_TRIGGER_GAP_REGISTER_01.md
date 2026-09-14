# Choice Kingdom — Canonical Trigger Gap Register 01

Date: 2026-09-15
Status: **ACTIVE QA REGISTER — NOT ENGINE INPUT**
Scope: E01–E270

## Purpose

This register consolidates the remaining trigger phrases that cannot yet be safely compiled into the production event schema. It is intentionally conservative: an item is not marked closed merely because a related graph edge or relationship exists.

## A. Contextual pressure gaps

| Trigger family | Canonical target | Current evidence | Status |
|---|---|---|---|
| food shortage / food pressure | `pred.food_pressure` | E03/E29/E157/E192/E218/E225/E251/E254/E255 | OPEN — exact producer/mitigation formula |
| severe food pressure / food crisis | `pred.food_severe` / `pred.food_crisis` | E225/E254/E255 | OPEN — severity/escalation rule |
| food stability | `pred.food_stable` or durable history | E192 choice B | OPEN — must not become hidden resource |
| winter / severe winter | `pred.winter_pressure` / `pred.winter_severe` | E29/E160/E175/E251/E252 | OPEN — explicit activation marker/window |
| winter illness | `pred.winter_illness` | E175/E252 | OPEN — producer contract |
| road pressure / low transport | `pred.winter_transport_disruption` or transport state | E192/E251 | OPEN — canonical transport identity |
| border tension / escalation | `pred.border_tension` / `pred.border_crisis` | E10/E16/E31/E172/E195/E253 | OPEN — escalation boundary |
| low army readiness | `pred.army_readiness_low` | E173/E193/E259 | OPEN — readiness-specific producer |
| security high/low | `pred.security_high` / `pred.security_low` | resource thresholds + military history | PARTIAL — threshold calibration |

## B. Route and faction gaps

| Trigger phrase | Canonical target | Status |
|---|---|---|
| institutional reform | `thread.institutional_reform` | PARTIAL — exact minimum marker set |
| audit reform | `thread.budget_reform` or `thread.document_audit` depending on source | OPEN — semantic split |
| late constitutional route | `thread.constitutional_endgame` + explicit timing/history | OPEN |
| strong constitutional preparation | derived constitutional predicate | OPEN — minimum combination |
| military constitutional route | dedicated constitutional military marker/thread | OPEN |
| military route | `thread.rowan_security` plus explicit military-history marker | OPEN — must not be relationship-only |
| strong guild influence | `thread.guild` + explicit leverage marker | OPEN |
| guild cooperation | `pred.guild_logistics_cooperation` / `thread.guild` | OPEN |
| guild representation | canonical guild representation history | OPEN |
| Amara civic route | `thread.amara_civic` | PARTIAL — route producer compilation |
| Toma information route | `thread.toma_information` | PARTIAL — route producer compilation |
| cross-faction cooperation | `thread.coalition` | PARTIAL — exact formation marker |
| cross_faction_package | canonical coalition package marker | OPEN — unique producer |

## C. Investigation/evidence gaps

| Trigger | Canonical target | Status |
|---|---|---|
| at least two procurement clues | `pred.procurement_clues_2` | PARTIAL — distinct evidence IDs required |
| three or more related clues | `pred.evidence_fragments_3` | PARTIAL — distinct evidence IDs required |
| high information pressure | `pred.information_pressure_high` | OPEN — pressure/cardinality rule |
| conflicting testimony | `history.conflicting_testimony_recorded` | CLOSED as producer identity; consumer mapping remains |
| witness route | `thread.toma_information` + witness history | PARTIAL |
| systemic explanation verified | `pred.systemic_explanation_verified` | OPEN — convergence rule |
| unresolved warehouse/market crisis | composed warehouse + market crisis predicate/thread | OPEN |
| final charter prerequisites | explicit conjunction of authored prerequisites | OPEN |

## D. Endgame gaps

| Consumer | Required canonical inputs | Status |
|---|---|---|
| E261 four-way bargain | four distinct faction route identities | DESIGN CLOSED / producer closure open |
| E263 coalition audit | explicit coalition package + benefit/cost histories | OPEN |
| E265 coalition holds | coalition trust + final-text prerequisites | OPEN |
| E266 Mara convergence | institutional + Mara history, not relationship alone | OPEN |
| E267 military convergence | military/border history + constitutional constraints | OPEN |
| E268 noble convergence | noble constitutional + precedent history | OPEN |
| E269 commercial convergence | guild/commercial + information legitimacy history | OPEN |
| E270 systemic convergence | investigation + systemic explanation + coalition + constitutional redesign | OPEN |

## E. ID/reconciliation gaps

1. Production E35–E270 uses Act V/expansion numbering; legacy original E35–E40 remain review aliases only.
2. Every remaining E35–E40 textual reference must be classified as production event or `LEGACY-END-*` material before schema freeze.
3. E73/E156 and E99/E173 remain semantic-duplicate candidates until downstream effects are compared.
4. E212 `clerk_discipled` remains a source typo to correct during schema migration; no runtime schema should preserve the misspelling.

## Closure rule

A gap becomes **CLOSED** only when all are known:

- canonical identifier;
- exact source producer(s);
- exact persistence namespace;
- deterministic consumer semantics;
- true and false reachable states;
- delayed/replay behavior where applicable;
- no competing meaning under the same identifier.

Documentation alone does not close a gap. Runtime implementation is not authorized by this register.

## Next machine-verifiable work

1. Complete E71–E110 producer extraction.
2. Finish E191–E270 canonical trigger mapping.
3. Build the exhaustive producer/consumer index.
4. Compile boundary cases for every derived predicate.
5. Resolve legacy E35–E40 textual references.
6. Only then generate the machine-readable production catalog.
