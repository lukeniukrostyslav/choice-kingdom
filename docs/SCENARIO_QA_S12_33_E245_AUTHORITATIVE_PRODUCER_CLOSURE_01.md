# Choice Kingdom — S12.33 E245 Authoritative Producer Closure

Date: 2026-09-15
Scope: E245 and candidate compensation producers
Status: **SOURCE-CLOSED**

## Authored consumer

E245 — **The Soldier's Son Returns**:

- Trigger: `compensation route, 6+ turns later`.
- Outcome: **the compensated family member joins the civil service**.

## Candidate producers re-read

### E20-A — The Soldier's Son
E20-A explicitly concerns a soldier who dies during training and his son asking why the army cannot provide proper equipment. The A choice is:

- publicly compensate the family;
- flag: `soldier_compensation`.

This is an exact semantic and narrative identity match for E245's **Soldier's Son** title and its singular **compensated family member** callback.

### E125-A — Border Families
E125-A compensates **border families** after years of military requisitions and writes `border_compensation`. This is a distinct plural family-compensation route and has no authored identity tying it to E245's soldier's-son character.

### E156-A — The Widow's Petition
E156-A compensates a widow after soldiers requisition her winter animals and writes `requisition_compensation`. This is a distinct civilian/requisition route and does not identify the E245 returning family member as its downstream subject.

## Closure decision

Canonical producer for E245 is:

**E20-A → `soldier_compensation` → E245**

E125-A and E156-A remain independent compensation outcomes and do not satisfy E245.

No generic compensation union is introduced.

## Delayed identity requirement

E245 remains subject to the existing delayed callback contract:

`sourceEventId + sourceChoiceId + consequenceId + earliestTurn + resolutionTarget + exactlyOnceKey + cancellation/supersession rule`

This closure resolves **producer identity only**. It does not invent an absolute due turn from the authored `6+ turns later` wording.

## Gate

**E245 producer identity: CLOSED.**

**E245 executable delayed lifecycle: PARTIAL/OPEN until exact timing, target and cancellation/supersession are represented in the runtime contract.**

**Generic compensation union: FORBIDDEN.**
