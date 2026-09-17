# Choice Kingdom — P2 Authored Character Studies QA v1

Status: **P2 EVIDENCE PASS — PERCENTAGE UNCHANGED AT 30%**

## Scope

This gate verifies the next concrete P2 evidence after the production-anchor proof:
- authored facial-expression study board;
- costume/material study board;
- identity-anchor continuity;
- mobile-safe hierarchy;
- web-preview exposure.

This is a design-system evidence gate, not final production-art approval.

## Evidence

- `docs/visual/premium-character-facial-studies-elira-v1.svg`
- `docs/visual/premium-character-material-costume-study-elira-v1.svg`
- `web-preview/artwork-preview.html` now exposes both studies.

## Checks

| Check | Result | Notes |
|---|---|---|
| Six authored expression states | PASS | neutral, concern, confidence, suspicion, grief, relief |
| Fixed facial geometry | PASS | head shape, eye spacing and hair mass remain stable |
| Expression variable isolation | PASS | brow/eye/mouth changes are controlled rather than redesigns |
| Costume silhouette continuity | PASS | royal shoulder/head relationship remains stable |
| Material grammar | PASS | woven cloth, aged metal, leather and restrained precious-metal accent are explicit |
| Rejection rules | PASS | glossy universal surfaces / generic fantasy armor / neon faction coding excluded |
| Crop-safe composition | PASS | face and identity anchors remain central and uncluttered |
| Mobile hierarchy | PARTIAL | board is inspectable; actual 360dp/412dp rendered validation remains open |
| Canonical People binding | OPEN | repository search did not expose a verified canonical People record for the candidate name; no invented binding is allowed |
| Final authored production artwork | OPEN | current artifacts are study/proof SVGs |
| Vercel rendered validation | OPEN | requires actual deployed render inspection |
| Provenance/licensing record | OPEN | final production asset provenance remains required |

## Gate decision

The authored-study evidence is accepted into the P2 evidence set. **P2 stays at 30%** because the roadmap explicitly requires canonical People binding and actual rendered Vercel/mobile validation before the next percentage increase.

## Next P2 actions

1. Identify a verified canonical People character from repository data.
2. Bind the visual anchor without inventing IDs or replacing canonical data.
3. Validate the updated review surface on the Vercel deployment.
4. Run 360dp / 412dp / large-text / RTL visual checks.
5. Record final-art provenance/licensing when production artwork replaces proof SVGs.
