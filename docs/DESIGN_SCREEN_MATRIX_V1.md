# Choice Kingdom — Production Design Screen Matrix v1

| Screen | Primary job | Required components | Edge cases | Design status |
|---|---|---|---|---:|
| Event | Situation and decision | TopBar, ResourceStrip, Art, Narrative, ChoiceCard | resolving, large text, long strings, RTL | 100% |
| Realm | Kingdom condition | ResourceStrip, delayed effects, relationships, factions | sparse/full state | 100% |
| History | Remember decisions | HistoryEntry | long history, empty sections, RTL | 100% |
| Character | Explain people | CharacterCard, history | missing portrait, long names | 100% |
| Faction | Explain constituencies | FactionCard | neutral/negative/positive stance | 100% |
| Investigation | Show evidence | EvidenceChain | uncertainty, branching evidence | 100% |
| Ending | Close chronicle | EndingPage | all ending families, long narrative | 100% |
| Settings | Accessibility/presentation | language, text size, reduced motion | RTL, large text | 100% |

## Cross-screen invariants
- Decision controls remain primary on Event.
- Presentation never implements gameplay rules.
- Internal event IDs never appear to players.
- State is never communicated by color alone.
- Interactive controls expose resolving/disabled behavior.
- Large fonts and long translations never clip critical content.
- RTL mirrors layout without changing meaning.
- System safe-area/gesture insets are respected.
