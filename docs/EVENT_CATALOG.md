# Choice Kingdom — First Campaign Event Catalog

This is the narrative source of truth for the first campaign. It is intentionally written before implementation so the engine serves the story rather than forcing the story into a shallow UI loop.

## State vocabulary

Base resources use a 0–100 scale unless otherwise noted:

- **gold** — treasury liquidity;
- **trust** — public confidence;
- **security** — ability to prevent or respond to threats;
- **power** — political capacity of the Crown;
- **reputation** — international and elite perception.

Character relationships use -3 to +3.

Flags and history markers are more important than raw numbers for major branches.

---

## Prologue / Act I — The Empty Throne

### E01 — The First Petition
**Trigger:** first turn.

A delegation asks whether the new ruler will hear ordinary petitioners before the nobles.

**A — Open the Hall**
- Immediate: +4 trust, -1 power.
- Flag: `open_petition_hall`.
- Delayed: after 3 turns, unlock `E07_market_whispers` because petitioners begin bringing useful information.

**B — Follow Court Protocol**
- Immediate: +2 power, +1 Seris.
- Flag: `court_first`.
- Delayed: after 3 turns, unlock `E06_noble_pressure`.

**Design purpose:** establishes whether access to the ruler is a privilege or a public institution.

### E02 — The Empty Chair

### E03 — The Grain Reserve
**Trigger:** early food pressure.

The royal grain reserve is lower than expected.

### E04 — The Public Accounts
**Trigger:** treasury pressure.

Mara asks whether the Crown will publish its accounts.

### E05 — Missing Patrol Supplies
**Trigger:** border/security pressure.

Patrol units report missing supplies.

### E06 — Noble Pressure
**Trigger:** `court_first` or delayed E01 consequence.

The old houses ask for priority access to the Crown.

### E07 — Market Whispers
**Trigger:** delayed E01 consequence.

Petitioners bring rumors about merchant practices.

### E08 — Merchant Charter
**Trigger:** market route.

Ivo proposes a formal merchant charter.

### E09 — Flexible Accounts
**Trigger:** audit route.

Mara proposes flexible emergency accounts with audit safeguards.

### E10 — Local Command
**Trigger:** security pressure.

Rowan asks whether border commanders should receive more local authority.

### E11 — Civic Charter
**Trigger:** civic route.

Commons representatives ask for a written charter.

### E12 — Amara's Patients
**Trigger:** trust < 60 or food shortage.

Amara asks for medicine funding while the treasury is being squeezed.

**A — Fund the House of Lanterns**
- Immediate: -5 gold, +4 trust, +2 Amara.
- Flag: `lantern_funded`.

**B — Require it to become fee-based**
- Immediate: +3 gold, -4 trust, -2 Amara.
- Delayed: if winter hits, mortality rises unless another welfare policy exists.

### E13 — Toma's Coin
**Trigger:** Toma unlocked through dock events.

Toma returns a purse he could have stolen and asks for protection from a dock gang.

**A — Offer legal work**
- Immediate: +2 Toma, -2 power.
- Flag: `toma_recruited`.
- Unlocks information network events.

**B — Arrest him for theft**
- Immediate: +2 security, -2 Toma.
- Flag: `toma_rejected`.
- Delayed: dock rumors become less reliable.

### E14 — Ivo's Joke
**Trigger:** Ivo >= 2.

Ivo jokes that the Crown could make a fortune taxing luxury umbrellas during a storm.

**A — Ask him for serious proposals**
- Immediate: +2 Ivo, unlock `market_reform`.

**B — Tax umbrellas**
- Immediate: +5 gold, -3 trust.
- Flag: `petty_tax_policy`.
- Delayed: becomes a recurring joke; later choices can turn it into a reputation advantage or political embarrassment.

---

## Act II — The Price of Peace

### E15 — The Veyran Envoy
**Trigger:** Act II.

Veyra sends a polite envoy after a patrol incident.

**A — Receive them publicly**
- Immediate: +3 reputation, +1 trust.
- Flag: `public_diplomacy`.

**B — Receive them privately**
- Immediate: +2 power, -1 reputation.
- Unlocks a more candid diplomatic branch.

### E16 — The Border Marker
**Trigger:** security < 60 or `local_command`.

A border stone has been moved by a few meters.

**A — Send soldiers to replace it**
- Immediate: +4 security, -2 reputation.
- Delayed: increases military escalation.

**B — Invite a joint survey**
- Immediate: -1 security, +4 reputation.
- If public diplomacy: unlocks peaceful border settlement.

### E17 — The Cheap Steel
**Trigger:** security < 65.

A contractor offers cheap weapons made from inferior metal.

**A — Buy them**
- Immediate: +8 security now, hidden durability flag.
- Delayed: during a later crisis, lose 8 security if not replaced.

**B — Reject the contract**
- Immediate: -4 gold, +2 Rowan.
- Flag: `quality_armaments`.

### E18 — The River Toll
**Trigger:** `merchant_charter` or `competitive_market`.

The guild asks for toll rights on a rebuilt bridge.

**A — Grant the toll**
- Immediate: +8 gold, -3 trust, +2 Ivo.
- Delayed: if granted twice, unlock `E19_price_fixing`.

**B — Keep the bridge public**
- Immediate: -5 gold, +4 trust.
- Flag: `public_bridge`.

### E19 — Price Fixing
**Trigger:** `merchant_charter` + no `audit_office`.

Bread merchants suddenly quote identical prices. This is the authored market-pressure incident itself; the pressure must not be inferred later from the trigger alone.

**A — Break the guild agreement**
- Immediate: -2 Ivo, +5 trust, -3 gold.
- Flag: `guild_broken`.
- Resolution: clears any active `pred.market_pressure` for the current market-pressure cycle; historical evidence of the price-fixing incident remains available.

**B — Negotiate a temporary price ceiling**
- Immediate: +2 trust, +1 Ivo.
- Flag: `market_pressure_declared`.
- Producer: establishes `pred.market_pressure` for the current market-pressure cycle; history records `market_pressure_declared`.
- Delayed: if supply falls, shortages intensify.

A later authored event may establish a new market-pressure cycle after the active cycle has been cleared. The predicate is therefore cycle-scoped state, not a permanent global flag.

### E20 — The Soldier's Son
**Trigger:** Rowan >= 1.

A soldier dies during training. His son asks why the army can afford banners but not proper equipment.

**A — Compensate the family publicly**
- Immediate: -3 gold, +3 trust, +2 Rowan.
- Flag: `soldier_compensation`.

**B — Treat it as a private matter**
- Immediate: +1 power, -3 Rowan, -2 trust.

### E21 — A Letter Without a Seal
**Trigger:** Toma >= 1 or `quiet_market_inquiry`.

A letter suggests someone in the court is moving emergency funds through shell offices.

**A — Trust the evidence and investigate**
- Immediate: +2 power, unlock `ledger_fragment_a`.

**B — Destroy the letter**
- Immediate: +2 reputation among elites, -1 Toma if recruited.
- Flag: `evidence_destroyed`.
- Delayed: hidden-ledger route becomes harder.

### E22 — The Festival Vote
**Trigger:** trust >= 55.

The capital asks for a festival after a good harvest. Council says it is wasteful.

**A — Hold the festival**
- Immediate: -4 gold, +5 trust.
- Delayed: festival can become cover for an assassination attempt if security is low.

**B — Cancel it**
- Immediate: +2 gold, -3 trust, +2 Mara.

---

## Act III — The Hidden Ledger

### E23 — Fragment A
**Trigger:** `ledger_fragment_a`.

The evidence links emergency offices to a dead royal treasurer.

**A — Publish the fragment**
- Immediate: +5 trust, -3 reputation.
- Flag: `ledger_public`.
- Delayed: nobles demand a formal inquiry.

**B — Keep it confidential**
- Immediate: +2 power.
- Flag: `ledger_secret`.
- Delayed: better tactical options, worse public legitimacy if exposed.

### E24 — The Missing Auditor
**Trigger:** `audit_office`.

The new auditor disappears before presenting findings.

**A — Announce the disappearance**
- Immediate: +3 trust, -2 power.
- Flag: `auditor_missing_public`.

**B — Search quietly**
- Immediate: +2 power, +1 security.
- If Toma >= 1, unlocks `E25_dock_route`.

### E25 — Dock Route
**Trigger:** Toma >= 1 and `auditor_missing_public` or quiet search.

Toma traces sealed crates from the palace district to an abandoned customs house.

**A — Raid the customs house**
- Immediate: +4 security, +2 Toma.
- Risk: if evidence is incomplete, innocent merchants are harmed.

**B — Follow the route one more night**
- Immediate: -1 security.
- Delayed: unlocks stronger evidence and a hidden character reveal.

### E26 — Seris's Confession
**Trigger:** Seris >= 2 and ledger chain active.

Seris admits her family benefited from the old emergency system but says she did not design it.

**A — Offer immunity for testimony**
- Immediate: +2 Seris, -2 trust if public.
- Flag: `seris_witness`.

**B — Demand public confession**
- Immediate: +4 trust, -3 Seris.
- Flag: `seris_exposed`.

### E27 — The False Culprit
**Trigger:** ledger chain active.

A convincing dossier accuses a minor clerk.

**A — Arrest immediately**
- Immediate: +3 security, +1 power.
- Delayed: if dossier was false, trigger institutional scandal.

**B — Test the dossier against the accounts**
- Immediate: -1 power.
- If audit office: reveals that the clerk is a decoy.

### E28 — The Old King's Seal
**Trigger:** `decree_investigation` + ledger chain.

The original emergency decree bears the old royal seal, but the signature is wrong.

**A — Reveal the forgery**
- Immediate: +5 trust, +3 power.
- Flag: `royal_forgery_proven`.

**B — Use the forgery as leverage secretly**
- Immediate: +4 power.
- Flag: `forgery_leverage`.
- Delayed: can secure cooperation but makes the Crown vulnerable to blackmail.

---

## Act IV — The Winter of Three Fires

### E29 — First Snow
**Trigger:** late campaign; at least two unresolved pressures.

A brutal winter begins early.

**A — Open royal granaries**
- Immediate: -10 gold, +7 trust.
- If grain was previously wasted, supplies are insufficient.
- Producer: establishes `pred.winter_severe` for the current winter cycle; history records `winter_severity_declared`.

**B — Ration by market price**
- Immediate: +5 gold, -7 trust.
- If market reform exists, loss is reduced.
- Producer: establishes `pred.winter_severe` for the current winter cycle; history records `winter_severity_declared`.

The winter-severity predicate is an authored environmental state, not a consumer-side inference from E160/E175/E251. A future recovery rule may explicitly clear or expire the active winter cycle, while historical declaration remains queryable.

### E30 — Fire at the Warehouse
**Trigger:** winter + market tension.

A warehouse burns. Someone may have set it deliberately.

**A — Focus on rescue**
- Immediate: +4 trust, -2 security.
- Delayed: arsonist may escape.

**B — Seal the district**
- Immediate: +4 security, -4 trust.
- If public trust is high, citizens may accept the measure.

### E31 — The Border Night
**Trigger:** winter + security < 60 or military escalation.

Veyran troops appear across the river after a patrol disappears.

**A — Mobilize**
- Immediate: -8 gold, +10 security, -3 reputation.
- Flag: `war_mobilization`.

**B — Send Rowan under a white banner**
- Immediate: -2 security, +6 reputation.
- If diplomatic branch exists, unlocks negotiated withdrawal.

### E32 — Three Fires
**Trigger:** E29 + E30 + E31 unresolved.

The kingdom enters a compound crisis. Winter roads and military movement have disrupted the transport network; medicine, grain, and official messages can no longer move reliably between districts.

**Source-level producer:** E32 establishes `pred.transport_disruption` for the current compound-crisis cycle and records `history.transport_disruption_declared`. This is an explicit authored crisis state, not an inference from gold, security, border pressure, or the E192 consumer trigger. A later authored recovery event may clear the active predicate while retaining the historical declaration.

## Canonical content boundary

E01–E32 in this file are the foundational first-campaign source. Later authored expansions live in their dedicated expansion catalogs and are subject to canonical integration, producer/consumer, reachability, delayed-consequence, replay and ending QA before becoming production data.