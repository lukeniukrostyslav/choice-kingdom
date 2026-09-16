from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from .state import EXCLUDED_EVENTS, PRODUCTION_FIRST, PRODUCTION_LAST, REPLAY_META_KEYS
from .ending_sources import EndingSourceCompiler

HEADING_RE = re.compile(r"^### (E\d{2,3}) — (.+)$", re.M)
CHOICE_PATTERNS = (
    re.compile(r"^(?:-\s*)?\*\*([A-Z])\s*[—:]\s*(.+?)\*\*$", re.M),
    re.compile(r"^-\s*\*\*([A-Z])\s*[—:]\s*(.+)$", re.M),
    re.compile(r"^(?:-\s*)?\*\*([A-Z])\s*[—:]\s*(.+?)\*\*:\s*(.*)$", re.M),
    re.compile(r"^-\s*([A-Z])\s+(.*)$", re.M),
)
DELTA_RE = re.compile(r"([+-]\d+)\s+(gold|trust|security|power|reputation)\b", re.I)
REL_RE = re.compile(r"([+-]\d+)\s+(Mara|Rowan|Seris|Ivo|Amara|Toma)\b", re.I)
TOKEN_RE = re.compile(r"`([^`]+)`")
AFTER_EVENT_RE = re.compile(r"\bafter\s+(E\d{2,3})\b", re.I)
COMPLETED_EVENT_RE = re.compile(r"\b(E\d{2,3})\s+(?:complete|completed|resolved)\b", re.I)
EVENT_OR_RE = re.compile(r"\b(E\d{2,3})\s+or\b|\bor\s+(E\d{2,3})\b", re.I)
NUMERIC_RE = re.compile(r"\b(gold|trust|security|power|reputation)\s*(<=|>=|<|>)\s*(\d+)\b", re.I)
REL_COND_RE = re.compile(r"\b(Mara|Rowan|Seris|Ivo|Amara|Toma)\s*(<=|>=|<|>)\s*(-?\d+)\b", re.I)

REPLAY_META_BY_EVENT = {
    "E186": "meta.replay.warehouse_investigation_unlock",
    "E247": "meta.replay.second_run_information_route",
    "E248": "meta.replay.callback_forgotten_favor",
}


@dataclass(frozen=True)
class Choice:
    choice_id: str
    label: str
    text: str
    body: str
    resource_deltas: dict[str, int]
    relationship_deltas: dict[str, int]
    state_tokens: tuple[str, ...]
    clear_tokens: tuple[str, ...]


@dataclass(frozen=True)
class Event:
    event_id: str
    title: str
    trigger: str
    choices: tuple[Choice, ...]
    source: str


class CatalogError(ValueError):
    pass


class AuthoredCatalog:
    def __init__(self, root: Path, events: dict[str, Event]):
        self.root = root
        self.events = events

    @classmethod
    def from_repository(cls, root: Path) -> "AuthoredCatalog":
        import json
        manifest = json.loads((root / "docs" / "MACHINE_CANONICAL_GRAPH_01.json").read_text(encoding="utf-8"))
        first = int(manifest["scope"]["first_event"])
        last = int(manifest["scope"]["last_event"])
        excluded = set(manifest["scope"].get("excluded_events", [])) | set(EXCLUDED_EVENTS)
        expected = {f"E{i:02d}" for i in range(first, last + 1)} - excluded
        events: dict[str, Event] = {}
        for source in manifest["source_of_truth"]["catalog_sources"]:
            path = root / source
            if not path.exists():
                raise CatalogError(f"missing catalog source: {source}")
            text = path.read_text(encoding="utf-8")
            headings = list(HEADING_RE.finditer(text))
            for index, heading in enumerate(headings):
                event_id, title = heading.group(1), heading.group(2).strip()
                if event_id not in expected:
                    if event_id in excluded:
                        continue
                    raise CatalogError(f"event outside frozen scope: {event_id}")
                end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
                parsed = cls._parse_event(event_id, title, text[heading.start():end], source)
                existing = events.get(event_id)
                if existing is not None:
                    if event_id != "E271" or existing != parsed:
                        raise CatalogError(f"conflicting duplicate event block: {event_id}")
                    continue
                events[event_id] = parsed
        missing = expected - set(events)
        if missing:
            raise CatalogError("missing authored events: " + ", ".join(sorted(missing)))
        return cls(root, dict(sorted(events.items(), key=lambda item: int(item[0][1:]))))

    @staticmethod
    def _parse_event(event_id: str, title: str, block: str, source: str) -> Event:
        trigger_match = re.search(r"^\*\*Trigger:\*\* (.+)$", block, re.M)
        trigger = trigger_match.group(1).strip() if trigger_match else ""
        rows = []
        for pattern in CHOICE_PATTERNS:
            rows.extend(pattern.finditer(block))
        rows.sort(key=lambda match: match.start())
        choices: list[Choice] = []
        seen_labels: set[str] = set()
        for index, row in enumerate(rows):
            end = rows[index + 1].start() if index + 1 < len(rows) else len(block)
            body = block[row.start():end]
            label, text = row.group(1), row.group(2).strip()
            if label in seen_labels:
                continue
            seen_labels.add(label)
            resource_deltas = {resource.lower(): int(delta) for delta, resource in DELTA_RE.findall(body)}
            relationship_deltas = {name.lower(): int(delta) for delta, name in REL_RE.findall(body)}
            tokens: list[str] = []
            clears: list[str] = []
            for line in body.splitlines():
                for token in TOKEN_RE.findall(line):
                    low = line.lower()
                    if any(word in low for word in ("clear", "remove", "reset", "invalidate", "revoke", "cancel")):
                        clears.append(token)
                    else:
                        tokens.append(token)
            choices.append(Choice(
                choice_id=f"{event_id}-{label}", label=label, text=text, body=body,
                resource_deltas=resource_deltas, relationship_deltas=relationship_deltas,
                state_tokens=tuple(dict.fromkeys(tokens)), clear_tokens=tuple(dict.fromkeys(clears)),
            ))
        return Event(event_id, title, trigger, tuple(choices), source)

    def get(self, event_id: str) -> Event:
        if event_id in EXCLUDED_EVENTS:
            raise CatalogError(f"excluded event: {event_id}")
        return self.events[event_id]

    def validate(self) -> None:
        expected = {f"E{i:02d}" for i in range(PRODUCTION_FIRST, PRODUCTION_LAST + 1)} - set(EXCLUDED_EVENTS)
        if set(self.events) != expected:
            raise CatalogError("runtime catalog scope is not exactly E01-E272 excluding E273-E277")
        for event in self.events.values():
            labels = {choice.label for choice in event.choices}
            if labels and not {"A", "B"}.issubset(labels):
                raise CatalogError(f"incomplete authored choice set in {event.event_id}: {sorted(labels)}")

    def authored_prerequisites(self, event_id: str) -> tuple[str, ...]:
        """Return only event prerequisites explicitly authored in the trigger text."""
        event = self.get(event_id)
        refs = list(AFTER_EVENT_RE.findall(event.trigger)) + list(COMPLETED_EVENT_RE.findall(event.trigger))
        return tuple(dict.fromkeys(ref.upper() for ref in refs))

    def trigger_satisfied(self, event_id: str, state) -> bool:
        event = self.get(event_id)
        if event_id in state.history:
            return False

        # Replay metadata is an explicit producer boundary. It is not inferred
        # from ordinary history, flags, trigger prose, or same-run evidence.
        replay_key = REPLAY_META_BY_EVENT.get(event_id)
        if replay_key is not None and replay_key in REPLAY_META_KEYS and replay_key in state.imported_meta_keys:
            return True

        trigger = event.trigger
        low = trigger.lower().strip().rstrip(".")
        if not trigger:
            return True
        if low == "severe winter":
            return _state_has_marker(state, "pred.winter_severe")

        # Evaluate boolean structure only for atoms the runtime can prove.
        # Unknown prose stays UNKNOWN rather than being guessed as a route.
        # This lets authored OR branches work (for example ``token or score``)
        # without silently converting narrative shorthand into gameplay truth.
        if " or " in low:
            # A direct authored event reference is an executable OR branch even
            # when the other branch remains narrative/opaque.
            for first, second in EVENT_OR_RE.findall(trigger):
                required = (first or second).upper()
                if required != event_id and required in state.history:
                    return True
            branches = re.split(r"\bor\b", trigger, flags=re.I)
            return any(
                _evaluate_trigger_branch(branch, state, self.authored_prerequisites(event_id)) is True
                for branch in branches
            )

        result = _evaluate_trigger_branch(trigger, state, self.authored_prerequisites(event_id))
        return result is True


def _state_has_marker(state, marker: str) -> bool:
    return marker in state.flags or marker in state.history or marker in state.threads


def _evaluate_trigger_branch(trigger: str, state, prerequisites: tuple[str, ...]) -> bool | None:
    """Evaluate one AND branch; return None when authored prose is unresolved."""
    clauses = [part.strip(" ,;:()") for part in re.split(r"(?:\band\b|\+)", trigger, flags=re.I)]
    values: list[bool] = []
    for clause in clauses:
        if not clause:
            continue
        value = _evaluate_trigger_atom(clause, state, prerequisites)
        if value is None:
            return None
        values.append(value)
    if not values:
        return None
    return all(values)


def _evaluate_trigger_atom(clause: str, state, prerequisites: tuple[str, ...]) -> bool | None:
    """Evaluate only canonical atoms; narrative residue deliberately remains unknown."""
    normalized = clause.strip().rstrip(".").strip()
    low = normalized.lower()
    if low == "first turn":
        return state.turn == 1
    if low == "severe winter":
        return _state_has_marker(state, "pred.winter_severe")

    # Source-closed composite predicates are evaluated through the same canonical
    # compiler used by ending qualification. This is deliberately limited to
    # predicates whose producer/evidence contracts are already frozen; unresolved
    # prose route names remain UNKNOWN.
    predicate_atom = low.strip("`")
    if predicate_atom.startswith("pred.") and re.fullmatch(r"pred\.[a-z0-9_]+", predicate_atom):
        facts = EndingSourceCompiler.compile_state(state).predicates
        if predicate_atom == "pred.food_stable":
            return "food_logistics_stabilized" in state.flags
        if predicate_atom == "pred.border_crisis":
            return "border_crisis_declared" in state.flags and "border_crisis_resolved" not in state.flags
        return predicate_atom in facts

    # Explicit completed/resolved/after-event prerequisites are canonical event facts.
    match = COMPLETED_EVENT_RE.fullmatch(normalized)
    if match:
        return match.group(1).upper() in state.history
    match = AFTER_EVENT_RE.fullmatch(normalized)
    if match:
        return match.group(1).upper() in state.history

    numeric = list(NUMERIC_RE.finditer(normalized))
    if numeric and " ".join(m.group(0) for m in numeric) == normalized:
        return all(_compare(state.resources[name.lower()], op, int(raw)) for name, op, raw in (m.groups() for m in numeric))

    relationships = list(REL_COND_RE.finditer(normalized))
    if relationships and " ".join(m.group(0) for m in relationships) == normalized:
        return all(_compare(state.relationships[name.lower()], op, int(raw)) for name, op, raw in (m.groups() for m in relationships))

    tokens = TOKEN_RE.fullmatch(normalized)
    if tokens:
        return _state_has_marker(state, tokens.group(1))

    # A bare canonical event prerequisite can occur in a compound authored branch
    # only when it is one of the already extracted explicit prerequisites.
    event_match = re.fullmatch(r"E\d{2,3}", normalized, flags=re.I)
    if event_match and event_match.group(0).upper() in prerequisites:
        return event_match.group(0).upper() in state.history

    return None


def _compare(value: int, op: str, target: int) -> bool:
    return {"<": value < target, "<=": value <= target, ">": value > target, ">=": value >= target}[op]
