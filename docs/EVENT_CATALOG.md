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
**Trigger:** after E01.

Mara points out that the former chancellor left an unsigned emergency decree on the council table.

**A — Sign it provisionally**
- Immediate: +3 power, -2 trust.
- Flag: `emergency_decree_used`.
- Delayed: if another emergency occurs, Crown may act faster but institutional trust suffers.

**B — Archive it and investigate**
- Immediate: +2 Mara, -2 power.
- Flag: `decree_investigation`.
- Unlocks part of the hidden-ledger chain.

### E03 — Bread at Dawn
**Trigger:** food prices rise in the capital.

**A — Release grain reserves**
- Immediate: -8 gold, +6 trust.
- Delayed: if grain reserve later reaches zero, winter shortages become harsher.

**B — Let merchants import freely**
- Immediate: -2 trust, +4 Ivo.
- Flag: `free_grain_imports`.
- Delayed: can create prosperity if market oversight is later established; otherwise price fixing risk.

### E04 — The King's Funeral Debt
**Trigger:** after E03.

The previous ruler's funeral cost more than the treasury records suggest.

**A — Publish the accounts**
- Immediate: +3 trust, -2 reputation.
- Unlock: `ledger_public_scrutiny`.

**B — Quietly settle the discrepancy**
- Immediate: +2 power, +2 Seris, -3 trust if discovered.
- Flag: `quiet_accounts`.

### E05 — A Captain's Warning
**Trigger:** security < 55 or turn 4+.

Rowan reports missing patrol supplies.

**A — Audit the guard**
- Immediate: +2 security after one turn, -1 Rowan.
- Delayed: chance to expose procurement fraud.

**B — Give Rowan emergency authority**
- Immediate: +6 security, +2 Rowan, -2 power.
- Flag: `emergency_guard_authority`.
- Delayed: Rowan can later request expanded powers.

### E06 — Noble Pressure
**Trigger:** `court_first` or Seris relationship >= 1.

Three houses ask for hereditary tax exemptions.

**A — Refuse all exemptions**
- Immediate: +4 trust, -2 Seris, +1 power.
- Flag: `nobles_challenged`.

**B — Grant a temporary exemption**
- Immediate: +2 Seris, +3 gold.
- Delayed: after 4 turns, nobles demand renewal unless tax reform occurs.

### E07 — Market Whispers
**Trigger:** `open_petition_hall`.

Dock workers claim a guild warehouse is hiding grain.

**A — Raid it publicly**
- Immediate: +3 trust, -2 Ivo, +2 security.
- If innocent: later lose reputation.

**B — Investigate quietly**
- Immediate: +1 trust, +1 Ivo if handled discreetly.
- Flag: `quiet_market_inquiry`.
- Delayed: can reveal `ledger_fragment_a`.

### E08 — The Merchant's Charter
**Trigger:** early Act I milestone.

Ivo offers 18 gold for an exclusive river-trade charter.

**A — Grant the charter**
- Immediate: +18 gold, -3 trust, +2 Ivo.
- Flag: `merchant_charter`.
- Delayed: if no oversight, unlock `E19_price_fixing`.

**B — Refuse exclusivity but offer a public license**
- Immediate: +4 trust, +1 power, +1 Ivo.
- Delayed: slower treasury growth but unlocks `competitive_market`.

---

## Character / relationship network

### E09 — Mara's Ledger Lesson
**Trigger:** Mara >= 1 and `decree_investigation`.

Mara teaches the ruler how emergency spending is hidden through temporary offices.

**A — Create a permanent audit office**
- Immediate: -4 gold, +2 power, +2 Mara.
- Flag: `audit_office`.
- Delayed: increases chance of exposing the hidden ledger.

**B — Keep the system flexible**
- Immediate: +2 power, -1 Mara.
- Flag: `flexible_accounts`.
- Delayed: emergency response is faster but corruption is harder to detect.

### E10 — Rowan at the Bridge
**Trigger:** Rowan >= 1.

Rowan asks whether soldiers should answer to the Crown or to local lords.

**A — Centralize command**
- Immediate: +4 security, -1 Seris.
- Flag: `central_command`.

**B — Preserve local command**
- Immediate: +2 Seris, +1 trust.
- Flag: `local_command`.
- Delayed: border defense is cheaper but slower to coordinate.

### E11 — Seris's Dinner
**Trigger:** Seris >= 1.

Seris privately admits that several nobles fear losing relevance.

**A — Offer them advisory seats**
- Immediate: +2 Seris, +2 power, -1 trust.
- Flag: `noble_advisory_council`.

**B — Tell Seris the old order must adapt**
- Immediate: +2 trust, -1 Seris.
- If Seris later respects the ruler, unlocks reform alliance.

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

Bread merchants suddenly quote identical prices.

**A — Break the guild agreement**
- Immediate: -2 Ivo, +5 trust, -3 gold.
- Flag: `guild_broken`.

**B — Negotiate a temporary price ceiling**
- Immediate: +2 trust, +1 Ivo.
- Delayed: if supply falls, shortages intensify.

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

The player receives three simultaneous reports: hungry districts, a mutinous garrison, and nobles demanding emergency powers.

**A — Choose one priority publicly**
- Immediate: +5 power.
- The neglected crisis worsens sharply.

**B — Delegate all three**
- Requires at least two strong relationships.
- Immediate: -2 power, +3 trust.
- Flag: `shared_crisis_command`.

### E33 — The Emergency Crown
**Trigger:** `emergency_decree_used` or severe crisis.

Council offers unlimited emergency authority for thirty days.

**A — Accept**
- Immediate: +8 power, +5 security.
- Flag: `emergency_power`.
- Delayed: unless voluntarily surrendered, unlocks Iron Crown path.

**B — Refuse**
- Immediate: -4 power, +6 trust.
- Flag: `constitutional_limit`.
- If cross-faction relationships are strong, unlocks Second Founder path.

### E34 — The People's Queue
**Trigger:** trust >= 65 or welfare branch.

Thousands wait outside the palace with petitions during the winter crisis.

**A — Meet them**
- Immediate: +7 trust, -3 power.
- Flag: `people_heard`.

**B — Send written relief orders**
- Immediate: +3 trust, +2 power.
- If bureaucracy is weak, relief arrives late.

---

## Act V — The Crown's Answer

### E35 — The Last Council
**Trigger:** Act V.

Mara, Rowan, Seris, Ivo and Amara disagree over the kingdom's future.

The available proposals are determined by relationship and flags, not by a fixed menu.

Possible proposals:
- constitutional council;
- military emergency government;
- merchant-led reconstruction;
- popular charter;
- restored noble compact;
- direct royal rule.

**Rule:** at least two proposals must be viable in any normal run; one proposal may be locked by prior history.

### E36 — The Ledger Opens
**Trigger:** hidden-ledger chain completed.

The ruler can expose the old system, bury it, or transform it into a public financial institution.

**A — Full exposure**
- High trust gain; high short-term instability.
- Unlocks `public_reckoning`.

**B — Quiet purge**
- High power gain; lower trust.
- Unlocks `silent_reform`.

**C — Publish and reform**
- Requires audit office + evidence + at least two cross-faction relationships.
- Moderate immediate cost.
- Unlocks `second_founder_eligible`.

### E37 — The Choice of Heir
**Trigger:** late game if ruler has no clear succession.

The council asks whether succession should remain hereditary.

**A — Name a blood heir**
- +2 noble support, -3 reform momentum.

**B — Establish a succession charter**
- -2 power now, +5 institutional legacy.
- Flag: `succession_charter`.

### E38 — The Final Speech
**Trigger:** ending resolution.

The ruler addresses the capital. The speech is assembled from history tags: mercy, order, commerce, reform, secrecy, public trust, military authority.

No choice changes the ending by itself. It reveals the accumulated identity of the run.

### E39 — The Crown's Answer
**Trigger:** ending resolver.

Ending selection considers:

- final resource bands;
- unresolved crisis flags;
- relationship coalition;
- emergency-power history;
- constitutional flags;
- ledger outcome;
- succession choice;
- public trust trend rather than only final trust.

Possible endings: Steward, Iron Crown, Golden Compact, People's Charter, Broken Diadem, Quiet Throne, Second Founder.

### E40 — Epilogue: What Remains
**Trigger:** any ending.

The game shows three concrete legacy consequences rather than a generic score screen:

1. what changed in the kingdom;
2. what happened to the strongest relationship;
3. what future problem the ruler left behind.

A final replay prompt highlights one major path the player did not see.

---

# Cross-event delayed consequence table

| Origin | Condition | Later consequence |
|---|---|---|
| E03 grain release | reserve repeatedly spent | winter shortage becomes severe |
| E08 merchant charter | no audit/market oversight | price fixing |
| E05 emergency guard authority | security repeatedly prioritized | military faction demands more power |
| E06 noble exemption | renewed | noble debt to Crown becomes leverage |
| E12 welfare cut | winter arrives | trust collapse in poor districts |
| E17 cheap steel | not replaced | equipment failure during E31 |
| E22 festival | security low | assassination attempt can occur |
| E23 ledger public | noble support low | council obstruction |
| E24 auditor missing | Toma trusted | hidden route discovered |
| E28 forgery leverage | evidence later exposed | blackmail crisis |
| E33 emergency power | not surrendered | Iron Crown eligibility |
| E33 refusal | coalition strong | Second Founder eligibility |

# Character arc outcomes

## Mara
- trusted + reform: becomes institutional architect;
- trusted + emergency power: becomes reluctant constitutional opponent;
- repeatedly ignored: resigns and preserves records for future inquiry.

## Rowan
- empowered carefully: becomes protector of civilian rule;
- repeatedly given emergency powers: becomes military power broker;
- repeatedly denied funding: leaves the capital unless reconciled.

## Seris
- respected but challenged: becomes bridge between old houses and reformers;
- humiliated: becomes political rival;
- granted unchecked privilege: becomes central to Golden Compact or elite capture.

## Ivo
- regulated fairly: becomes growth partner;
- monopolized: becomes kingmaker;
- publicly betrayed after good-faith cooperation: can trigger economic retaliation.

## Amara
- supported: becomes public-trust anchor during winter;
- ignored: organizes independent relief networks;
- exploited politically: withdraws and damages Crown legitimacy.

## Toma
- recruited: information network reveals hidden routes and rumors;
- rejected: street network becomes unreliable;
- protected then betrayed: can reveal evidence against the Crown.

# Content quality checklist

Every new event must answer:

1. Why is this happening now?
2. Why would a reasonable ruler choose either option?
3. What changes immediately?
4. What can change later?
5. Which character or institution remembers it?
6. Can the player discover a new fact because of this choice?
7. Does it create a meaningful replay difference?
8. Is the outcome deterministic from state/history/seed?
9. Does it avoid being a disguised +resource / -resource button?
10. Can the event be localized without embedding text in logic?

A content validator should reject events missing stable IDs, localized keys, choice IDs, or valid effect/condition contracts.
