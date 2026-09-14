# Choice Kingdom — Campaign Event Graph

This is the causal map used to keep the campaign coherent. IDs describe narrative dependencies, not UI order.

## Core spine

`E01 -> E02 -> E03 -> E04`

From there the campaign branches into three major preparation systems:

- **Institutional:** E02 investigation -> E09 audit -> E24 auditor -> E27 dossier -> E28 seal.
- **Commercial:** E03 imports -> E08 charter/license -> E18 bridge -> E19 fixing -> winter supply consequences.
- **Security/diplomacy:** E05 guard -> E10 command -> E16 border -> E17 steel -> E31 border night.

Character routes run alongside these systems and feed back into them.

## Act I causal links

### E01 First Petition
- Open Hall -> E07 and Toma route becomes easier.
- Court First -> E06 and stronger Seris route.

### E02 Empty Chair
- Investigate -> E09 and ledger route.
- Sign -> faster emergency actions but weaker institutional legitimacy later.

### E03 Bread at Dawn
- Grain reserves -> stronger immediate trust, weaker winter buffer.
- Imports -> Ivo route and later market risk.

### E04 Funeral Debt
- Publish -> public scrutiny; evidence arrives more openly.
- Quiet settlement -> political convenience; discovery creates sharper trust loss.

### E05 Captain's Warning
- Audit -> exposes procurement route and supports institutional branch.
- Emergency authority -> supports military branch but raises final Iron Crown pressure.

### E06 Noble Pressure
- Refusal -> reform route and Seris conflict.
- Exemption -> Seris trust and later privilege bargaining.

### E07 Market Whispers
- Raid -> immediate public confidence but creates false-positive risk.
- Investigate -> slower but stronger evidence route.

### E08 Merchant Charter
- Exclusive charter -> short-term treasury solution and monopoly risk.
- Public license -> slower money but resilient market route.

## Act II causal links

E15–E22 should not be a linear checklist. At least three events should be selected by current state/history.

### Border chain
`E10 -> E16 -> E17 -> E31`

Central command improves response speed but increases noble resistance. Local command preserves local legitimacy but creates coordination costs.

### Market chain
`E08 -> E18 -> E19`

The monopoly path is not automatically bad. If the player creates oversight, the same commercial power can become a controlled prosperity engine rather than price fixing.

### Information chain
`E13 -> E21 -> E23 -> E25 -> E27`

Toma provides access, not truth. The player must decide how much evidence is enough before acting.

## Act III mystery chain

`E23 -> E24/E25 -> E26 -> E27 -> E28`

There are deliberately multiple routes to the same underlying truth:

1. **Mara route:** audit records.
2. **Toma route:** physical movement of documents and crates.
3. **Seris route:** elite knowledge and family records.
4. **Direct investigation:** comparison of decrees and accounts.

No single route is mandatory for discovering the systemic problem. However, different routes reveal different motives and therefore alter the final choices.

## Act IV crisis graph

`E29 + E30 + E31 -> E32 -> E33+`

The winter crisis should use accumulated state rather than a fixed script.

Examples:

- Strong civilian institutions reduce hunger damage.
- Strong market oversight reduces price shock.
- Strong security reduces mutiny/border escalation.
- Strong diplomacy reduces war escalation.
- Strong relationships allow delegation.
- Excessive emergency powers make E33 easier immediately but increase the probability of an authoritarian ending.

## Endgame convergence

The final act must converge on a constitutional question, not merely a boss fight or resource check.

The player is effectively answering:

> "Who should be allowed to wield power after I am gone?"

The answer is calculated from the pattern of decisions:

- **Steward:** durable institutions + restrained emergency power + sufficient stability.
- **Iron Crown:** military dependency + emergency authority + weak civic trust.
- **Golden Compact:** commercial dependency + strong treasury + guild leverage.
- **People's Charter:** public trust + civic institutions + distributed political power.
- **Broken Diadem:** multiple unresolved crises + collapsed relationships/institutions.
- **Quiet Throne:** personal survival with withdrawal from active constitutional leadership.
- **Second Founder:** verified ledger truth + cross-faction cooperation + institutional redesign + refusal to permanently normalize emergency powers.

## Branch protection

Critical endings must have at least two independent ways to satisfy their major prerequisites. A single missed event or disliked character must not silently make the campaign unwinnable.

## Delayed-consequence inventory target

The final authored campaign must contain at least:

- 10 consequences delayed 3+ turns;
- 6 mutually exclusive branch locks;
- 6 callback events that explicitly reference earlier history;
- 4 cases where investigation changes the meaning of an earlier event;
- 4 cases where an earlier costly choice becomes strategically useful later.

## Narrative integrity check

When implementing the engine, every link in this document must be represented by data conditions/history/effects rather than hardcoded UI branches.
