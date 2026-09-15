# Choice Kingdom — Campaign Event Graph

This is the causal map used to keep the campaign coherent. IDs describe narrative dependencies, not UI order. Expansion nodes remain authored candidates until exact prerequisites, turn windows, consequences and reachability are verified.

## Core spine
`E01 -> E02 -> E03 -> E04`

Preparation systems:
- Institutional: E02 -> E09 -> E24 -> E27 -> E28 -> E43 -> E53.
- Commercial: E03 -> E08 -> E18 -> E19 -> E45/E49 -> E55.
- Security/diplomacy: E05 -> E10 -> E16 -> E17 -> E31 -> E52/E58.
- Civic relief: E12 -> E40 -> E50 -> E56/E106.
- Information: E13 -> E21 -> E25 -> E41/E42 -> E43/E57.

## Canonical delayed-producer edges

The following edges are explicitly source-backed and reconcile delayed-consumer identity with the authored producer choice. They do **not** prove runtime scheduling, exactly-once delivery, cancellation/supersession, or gameplay reachability.

`E09-B -> E244`
`E17-A -> E185`
`E18-B -> E243`
`E20-A -> E245`
`E45-B -> E181`

Already represented in the broader graph and retained as canonical producer chains:
`E117-B -> E182`
`E118-B -> E183/E242`
`E160-A -> E246`
`E136-B -> E194`

Hard boundary: E184 has no safe canonical producer alias and remains OPEN. E242 remains only partially closed because its authored consumer wording refers to a broader noble-exception family than can safely be aliased universally.

## Expansion layer E71–E110

These nodes expand the spaces between the spine and endgame rather than forming a second linear campaign.

### Civilian/economic observation
`E71 -> E78 -> E102`
`E72 -> E81/E93`
`E73 -> E94/E105`
`E74 -> E79/E104`
`E76 -> E92/E101`

### Investigation reinforcement
`E75 -> E86`
`E81 -> E88 -> E89 -> E90`
`E82 -> E86 -> E89`
`E83 -> E89 -> E90`
`E84 -> E41 -> E42`
`E85 -> E103 -> E54`

E90 is an intentional fork: accept systemic corruption or pursue a single-mastermind theory. The latter carries evidence and coalition costs.

### Winter network
`E91 -> E97`
`E92 -> E96`
`E93 -> E100`
`E94 -> E105`
`E95 -> E103`
`E96 -> E104`
`E97 -> E101`
`E98 -> E99 -> E105`
`E100 -> E58`

### Constitutional network
`E101/E102 -> E50/E106/E107`
`E103 -> E54`
`E104 -> E49/E55`
`E105 -> E37/E46/E52`
`E106 -> E56`
`E107 -> E57`
`E108 -> E51`
`E109 -> E51/E59`
`E110 -> E53/E60`

## Expansion layer E111–E150

### Civic and character routes
`E111/E114 -> E122 -> E141/E145`
`E116 -> E142 -> E154/E155 -> E211/E212`
`E117 -> E182 -> E222/E245`
`E118 -> E162/E183/E242`
`E119 -> E165/E187/E229`
`E120 -> E223/E241/E262`
`E121 -> E177/E180/E231`

### Faction legitimacy
`E122 -> E159 -> E214/E215`
`E123 -> E138/E254`
`E124 -> E166/E168/E239`
`E125 -> E170/E195`
`E126 -> E181/E243`

### Delayed and information routes
`E127 -> E242`
`E128 -> E185 -> E253`
`E129 -> E243`
`E130 -> E181`
`E131 -> E188 -> E249`
`E132 -> E233/E250`
`E133 -> E247`
`E134 -> E153 -> E190`
`E135 -> E189 -> E236`

### Crisis preparation
`E136 -> E251/E253`
`E137 -> E240/E253`
`E138 -> E218/E254`
`E139 -> E241/E252`
`E140 -> E220/E246`

### Constitutional convergence
`E141 -> E257`
`E142 -> E258`
`E143 -> E259`
`E144 -> E168/E263`
`E145 -> E213/E260`
`E146 -> E261`
`E147 -> E265`
`E148 -> E261/E262/E264`
`E149 -> E216/E263`
`E150 -> E256/E257`

## Expansion layer E151–E210

### Institutional reform
`E151 -> E212/E214`
`E152 -> E213/E260`
`E153 -> E190/E249`
`E154 -> E155 -> E211/E216`

### Commons and daily life
`E156 -> E222/E245`
`E157 -> E224/E239`
`E158 -> E223/E260`
`E159 -> E214/E215/E260`
`E160 -> E242/E246`

### Noble and guild routes
`E161 -> E162/E228/E238`
`E162 -> E163 -> E235/E268`
`E164 -> E240/E259`
`E165 -> E187/E217/E269`
`E166 -> E219/E239`
`E167 -> E218/E220`
`E168 -> E239/E263`
`E169 -> E222/E227`

### Security and civic conscience
`E170 -> E182/E240`
`E171 -> E259`
`E172 -> E240/E253`
`E173 -> E251/E252`
`E174 -> E223/E252`
`E175 -> E252/E253`
`E176 -> E236/E267`

### Information network
`E177 -> E178/E180/E231`
`E178 -> E232/E249`
`E179 -> E234/E248`
`E180 -> E236/E270`
`E181 -> E216/E217/E243`
`E183 -> E228/E242`
`E184 -> E234/E244`
`E185 -> E253`
`E186 -> E247/E249`
`E187 -> E234/E250`
`E188 -> E249/E257`
`E189 -> E231/E236`
`E190 -> E232/E261`

### Crisis escalation
`E191 -> E225/E251/E255`
`E192 -> E252/E254`
`E193 -> E227/E255`
`E194 -> E219/E261`
`E195 -> E253/E255`

### Constitutional preparation
`E196 -> E263/E265`
`E197 -> E256/E257`
`E198 -> E258/E263`
`E199 -> E259/E260`
`E200 -> E261/E262`
`E201 -> E264/E265`
`E202 -> E266/E267/E268/E269`
`E203 -> E270`
`E204/E205 -> E261/E263`
`E206/E207 -> E264/E265`
`E208/E209 -> ending qualification families`
`E210 -> ending resolution meta-node`

## Expansion layer E211–E270

### Public institutions and transparency
`E211 -> E212/E216`
`E212 -> E213/E214`
`E213 -> E256/E260`
`E214 -> E215/E216`
`E215 -> E260`

### Economic and social consequences
`E216 -> E217`
`E218 -> E219/E220`
`E219 -> E239`
`E220 -> E248`
`E221 -> E224/E237`
`E222 -> E245`
`E223 -> E241/E252`
`E224 -> E243`
`E225 -> E255`

### Character pressure
`E226 -> E214/E266`
`E227 -> E259/E267`
`E228 -> E238/E268`
`E229 -> E219/E269`
`E230 -> E252/E267`
`E231 -> E236/E269/E270`

### Investigation and evidence
`E232 -> E233/E234/E235`
`E233 -> E249/E250`
`E234 -> E236/E250`
`E235 -> E238/E268`
`E236 -> E263/E269`

### Faction credibility
`E237 -> E261/E262`
`E238 -> E228/E265`
`E239 -> E219/E261`
`E240 -> E227/E259`
`E241 -> E223/E262`

### Delayed callbacks
`E242 -> E228/E238`
`E243 -> E224/E239`
`E244 -> E216/E258`
`E245 -> E222/E246`
`E246 -> E219/E257`

### Replay divergence
`E247 -> E232/E249/E250`
`E248 -> E231/E265`
`E249 -> E233/E250/E256`
`E250 -> systemic explanation / Second Founder support`

### Winter and crisis
`E251 -> E252/E254/E255`
`E252 -> E230/E241/E270`
`E253 -> E259/E267`
`E254 -> E237/E261`
`E255 -> E261/E264`

### Constitutional stress tests
`E256 -> E257/E265`
`E257 -> E260/E267`
`E258 -> E263`
`E259 -> E227/E267`
`E260 -> E265`

### Cross-faction endgame
`E261 -> E262/E263/E264/E265`
`E262 -> E263/E265`
`E263 -> E265/E266`
`E264 -> E265/E267`
`E265 -> ending qualification`

### Final personal convergence
`E266 -> ending qualification`
`E267 -> Iron Crown / Steward / People’s Charter support depending on history`
`E268 -> Steward / Golden Compact / People’s Charter support depending on history`
`E269 -> Golden Compact / Second Founder / legitimacy support depending on history`
`E270 -> Second Founder / coalition / information qualification depending on history`

## Expansion layer E271–E272 — border-crisis lifecycle

These two authored nodes close the border-crisis lifecycle at source level. They remain design-level causal candidates until the future engine verifies exact trigger evaluation and runtime persistence.

### Declaration route
`E271-A -> border_crisis_declared`
`E271-A -> thread.border_crisis(active)`
`E271-A -> pred.border_crisis(active)`
`pred.border_crisis(active) -> E195/E253/E255`

### Non-crisis route
`E271-B -> thread.border_crisis(resolved_without_declaration)`
`E271-B -X-> pred.border_crisis(active)`

### Resolution route
`E271-A -> E272`
`E272-A/B -> border_crisis_resolved`
`E272-A/B -> clear pred.border_crisis`
`E272-A -> thread.border_crisis(resolved)`
`E272-B -> thread.border_crisis(resolved_under_security_guarantee)`

Historical declaration is retained after E272; resolution clears the active predicate rather than erasing the historical fact. No new ending or replay prerequisite is inferred from E271/E272.

## Investigation routes

1. Mara: accounting structure and institutional records.
2. Toma: physical movement of documents and people.
3. Seris: elite/family records and political participation.
4. Direct comparison: decrees, dates, seals and invoices.
5. Expansion evidence: procurement chains, duplicate seals, payment calendars, witness ledgers, organizational maps and replay-exclusive anomalies.

The correct conclusion is systemic: emergency offices created incentives for distributed corruption. A single-mastermind theory is intentionally possible but less reliable.

## Delayed consequence families

- grain spending -> winter reserve pressure;
- free imports -> market resilience or price manipulation;
- temporary noble exemptions -> renewal demand;
- cheap steel -> later security loss;
- festival security -> assassination risk;
- quiet evidence handling -> weaker legitimacy when exposed;
- emergency authority -> normalized emergency governance;
- guild credit -> later political leverage;
- public infrastructure decisions -> later ownership dispute;
- constitutional secrecy -> later legitimacy dispute;
- public audit -> transparency demands;
- quiet borrowing -> creditor leverage;
- military shortcuts -> later constitutional limits;
- coalition concessions -> later budget and legitimacy pressure;
- replay information -> alternative evidence interpretation.

## Endgame convergence

The final act answers: **Who should be allowed to wield power after I am gone?**

- Steward: durable institutions + restrained emergency power + stability.
- Iron Crown: military dependency + emergency authority + weak civic trust.
- Golden Compact: commercial dependency + strong treasury + guild leverage.
- People's Charter: public trust + civic institutions + distributed political power.
- Broken Diadem: unresolved crises + collapsed relationships/institutions.
- Quiet Throne: personal survival with withdrawal from active constitutional leadership.
- Second Founder: verified ledger truth + cross-faction cooperation + institutional redesign + refusal to permanently normalize emergency powers.

## Branch protection

Critical endings must have at least two independent ways to satisfy major prerequisites. A single missed event or disliked character must not silently make the campaign unwinnable.

## Canonical-integration rule

The edges above are **design-level causal candidates**, not verified runtime edges. Before engine implementation, every edge must be translated into explicit prerequisite conditions, turn windows, state effects, flags/history markers and follow-up rules. Reachability, dead-end, contradiction, delayed-exactly-once and ending simulations must then verify the graph.

## Content status

E01–E272 are authored. E71–E272 are expansion layers pending canonical production integration. No expansion node is considered engine-integrated merely because an edge is written here.
