# Choice Kingdom — Producer → Consumer Inventory 04

Date: 2026-09-14
Status: **CANONICALIZATION WORKING INVENTORY — NOT ENGINE INPUT**
Scope: unresolved producer families exposed by E151–E270 reconciliation.

## Canonical route families requiring closure

| Canonical family | Candidate producers | Known consumers | Required closure |
|---|---|---|---|
| `thread.institutional_reform` | audit/clerks/appointment/budget decisions | E214, E216, E258, E263, endgame | define exact qualifying markers |
| `thread.document_audit` | E152/E154/E155 and earlier audit nodes | E213/E260 and investigation nodes | distinguish document audit from crown audit |
| `thread.noble` | E161/E162/E163/E183/E228/E238/E242 | E265/E268 and noble callbacks | preserve exception/assembly/evidence distinctions |
| `thread.guild` | E165–E169/E194/E219/E239 | E219/E261/E263/E269 | distinguish leverage, labor tension, logistics and credibility |
| `thread.veteran` | E117/E170/E182/E222 | E225/E227/E245/endings | distinguish patronage, readiness and constitutional route |
| `thread.border` | E139/E164/E171/E172/E240/E253 | E195/E255/E259/endings | distinguish tension, crisis, intelligence and military authority |
| `thread.amara` | E174–E176/E223/E230/E241 | E252/E262/E270/endings | distinguish relationship from institutional credibility |
| `thread.toma` | E177–E180/E231 | E231/E236/E247/E269/E270 | separate relationship, information pressure and verified evidence |
| `thread.archive` | E153/E190/E249/E260 | E249/E250/E256/E265 | distinguish access from archive reform |
| `thread.coalition` | E237/E261/E262/E263 | E263/E265/E269/E270 | require explicit coalition formation and audit markers |
| `thread.succession` | E197/E256/E257 | E265–E270 | define constitutional succession qualification |
| `thread.budget_reform` | E198/E258 and earlier fiscal reform | E216/E258/E263 | distinguish budget reform from generic institutional reform |
| `thread.archive_reform` | E260 and earlier archive decisions | E265/endings | distinguish access law from evidence discovery |

## Compound predicate families

### Food
Canonical state must derive food pressure from authored causes and effects rather than introduce a new resource. Required distinctions:
- normal food pressure;
- severe food pressure;
- food crisis;
- food stability/resilience;
- temporary shortage caused by a single logistics event.

Known consumers include E157, E167, E192, E218, E225, E251, E254 and E255.

### Winter
Required distinctions:
- winter pressure;
- severe winter;
- winter illness;
- transport disruption during winter.

Known consumers include E160, E173, E175, E192, E251 and E252.

### Border/security
Do not collapse these:
- `pred.border_tension`;
- `pred.border_crisis`;
- `pred.security_low`;
- `pred.security_high`;
- `pred.army_readiness_low`;
- military constitutional route;
- border intelligence route.

Known consumers include E164, E170–E172, E185, E195, E227, E240, E253, E255 and E259.

### Market/guild
Required distinctions:
- market pressure;
- strong market oversight;
- guild leverage;
- guild labor tension;
- guild logistics cooperation;
- trade-risk insurance.

Known consumers include E165–E169, E194, E218–E220, E239, E246 and E261.

### Information/evidence
Required deterministic state:
- information pressure;
- evidence fragment set/cardinality;
- witness route;
- protected-source route;
- forgery route;
- payment-pattern evidence;
- procurement clue count;
- systemic explanation verified.

Known consumers include E178–E190, E231–E236, E247–E250 and E270.

### Multi-crisis
`pred.multi_crisis_3` should require explicit simultaneous satisfaction of the three authored pressure predicates (food + border + civic), with deterministic evaluation at event eligibility time. It must not be manually toggled by UI or inferred from event order.

## Data-integrity warnings

1. A graph edge is not a producer.
2. A relationship value is not automatically a route.
3. A thematically related event is not automatically a callback.
4. A replay fact is not ordinary current-run history.
5. A delayed effect must carry source identity, target effect, due turn/window and exact-once resolution semantics.
6. Any choice that claims a later consequence but emits no durable marker must be resolved before production schema freeze.

## Next closure order

1. Extract all route producers from E01–E270.
2. Assign every route consumer to exactly one canonical namespace.
3. Build predicate threshold table with source evidence and no circular definitions.
4. Define evidence cardinality representation.
5. Define ending qualification predicates for E265–E270.
6. Re-run graph reconciliation after canonicalization.
