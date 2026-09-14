# Choice Kingdom — Narrative Architecture Review

## Purpose

This review is the quality gate for the first campaign before event data is implemented. The objective is not to maximize event count; it is to make each run feel like a chain of decisions whose meaning changes as the player learns more.

## 1. Core dramatic engine

Every major situation must contain four layers:

1. **Visible problem** — what the player must decide now.
2. **Human claimant** — someone with a believable reason to want a particular outcome.
3. **Hidden trade-off** — the cost that is not obvious on first play.
4. **Future echo** — a later event that remembers the decision.

The player should frequently think: "I made the reasonable choice. Why did this create that problem?" rather than "I pressed the evil button."

## 2. The central mystery is systemic, not a whodunit

The hidden ledger must not reduce to one villain secretly controlling everything. The old emergency system became corrupt because it rewarded temporary offices, opaque procurement and favors during crises. Several respectable people benefited without considering themselves criminals.

The final reveal should therefore force a second question: **does the ruler destroy the people who exploited the system, or redesign the system that made exploitation profitable?**

The Second Founder ending requires the latter.

## 3. Character arcs

### Mara Vey — order without tyranny

Start: believes procedure prevents famine and chaos.

Middle: discovers that procedure itself was manipulated.

Possible arc: institutional reformer, resigned guardian of records, or authoritarian administrator if the ruler repeatedly sacrifices transparency for speed.

Key memory markers:
- whether the ruler investigates before acting;
- whether emergency powers are temporary;
- whether Mara's warnings are respected;
- whether the ruler protects evidence even when politically costly.

### Rowan Hale — protection without militarism

Start: wants competent soldiers and safe civilians.

Middle: emergency authority makes him effective and increasingly comfortable with command.

Possible arc: loyal constitutional commander, military strongman, or disillusioned protector.

Key memory markers:
- emergency authority;
- centralized command;
- treatment of soldiers' families;
- diplomacy versus mobilization.

### Seris Auren — privilege with a conscience

Start: defends inherited institutions because she genuinely fears social collapse.

Middle: discovers that her own family profited from the old system.

Possible arc: reformist aristocrat, compromised witness, political rival, or bridge between factions.

Key memory markers:
- whether the ruler humiliates or negotiates with nobles;
- whether Seris is offered a path to change;
- whether her testimony is protected;
- whether noble privilege is challenged consistently.

### Ivo Renn — prosperity with a price

Start: charming merchant who can solve shortages faster than government.

Middle: discovers that market power is itself political power.

Possible arc: responsible commercial partner, monopolist, or scapegoat for structural failures.

Key memory markers:
- exclusive charter;
- bridge tolls;
- market oversight;
- whether the Crown keeps promises to merchants.

### Sister Amara — conscience without naivety

Start: healer who distrusts court politics.

Middle: realizes charity cannot permanently compensate for bad institutions.

Possible arc: public-health reformer, opposition moral authority, or trusted crisis coordinator.

Key memory markers:
- funding of the House of Lanterns;
- winter welfare policy;
- whether civilians are sacrificed for political stability;
- whether Amara is consulted before humanitarian crises.

### Toma Reed — information has a cost

Start: courier/smuggler with access to rumors.

Middle: learns that information can save lives but can also destroy innocent people.

Possible arc: loyal intelligence network, black-market broker, or betrayed informant.

Key memory markers:
- whether the ruler protects him;
- whether evidence is verified;
- whether rumors are acted on blindly;
- whether his network is legalized or exploited.

## 4. Relationship design

Relationships are not friendship meters. A high relationship should unlock a person's preferred method of solving problems, while a low relationship should change what information or cooperation is available.

Example:

- High Mara: access to institutional evidence and audit solutions.
- High Rowan: access to disciplined military responses.
- High Seris: access to noble mediation.
- High Ivo: access to rapid commercial solutions.
- High Amara: access to civilian resilience solutions.
- High Toma: access to informal intelligence.

A run should never be able to maximize every relationship. Helping one faction should occasionally make another faction suspicious.

## 5. Event quality rules

An event is rejected if:

- one choice is obviously morally correct with no meaningful cost;
- both choices produce nearly identical state changes;
- the event never affects anything later;
- the consequence is only a number change with no narrative interpretation;
- the same character repeats the same argument without development;
- a branch can be solved by grinding one resource;
- the player can discover the entire mystery in one event;
- a late crisis ignores earlier preparation.

At least one major event in every campaign segment should have a consequence that is invisible when the choice is made.

## 6. Information asymmetry

The game should deliberately give incomplete information.

The player may know that a warehouse is suspicious without knowing whether it contains stolen grain, legal emergency reserves, or planted evidence. Investigation choices should improve information but consume time, gold, trust or political capital.

This makes information itself a strategic resource.

## 7. Replay structure

Run 1 should teach the player the surface system.

Run 2 should reveal that previous "bad outcomes" were not random: they were consequences of earlier patterns.

Run 3 should make the player capable of intentionally engineering a long-term strategy, including the hidden Second Founder route.

A replay should alter:

- which characters become reliable;
- which clues appear first;
- which emergency solutions are available;
- which factions believe the Crown;
- which late-game crisis begins first;
- which endings become reachable.

## 8. Pacing target

The campaign should feel like escalation rather than a checklist:

- Turns 1–6: personal legitimacy and basic institutions.
- Turns 7–14: economic and border pressure.
- Turns 15–22: relationships and first evidence of systemic corruption.
- Turns 23–30: investigation and faction conflict.
- Turns 31–36: winter and simultaneous crises.
- Turns 37–42: constitutional endgame.

A normal first run should be approximately 35–45 decisions, while a completionist or investigation-heavy run may reach 45–55.

## 9. Ending logic

Endings must be combinations of history, relationships and institutional conditions. Raw resources alone cannot determine an ending.

Examples:

- High security + low trust should not automatically mean Iron Crown; it requires a pattern of empowering coercive institutions.
- High trust + weak institutions should not automatically mean People's Charter; the player must have created durable civic mechanisms.
- High gold should not automatically mean Golden Compact; commercial dependence must also be present.
- The Second Founder requires cross-faction trust, verified evidence, limited emergency power, and explicit institutional reform.

## 10. Required content pass before engine lock

Before event JSON/data is frozen:

1. Every event receives a unique downstream consequence.
2. Every main character has at least one positive and one negative arc.
3. Every major faction gets at least one event where its reasonable position is correct.
4. Every act contains at least one event that reinterprets an earlier decision.
5. Every ending has a recognizable path rather than a surprise stat threshold.
6. At least 10 events must have delayed consequences of 3+ turns.
7. At least 6 events must have mutually exclusive future branches.
8. At least 4 events must reward investigation over immediate action.
9. At least 4 events must make an earlier seemingly bad decision useful later.
10. No critical path may depend on a single character being liked.
