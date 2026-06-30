"""Durable checkpoint state for resumable research sessions."""

from __future__ import annotations

import datetime as _dt
import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class _DateEncoder(json.JSONEncoder):
    """Serialize date/datetime to ISO strings so checkpoint JSON stays clean."""
    def default(self, obj):
        if isinstance(obj, (_dt.datetime, _dt.date)):
            return obj.isoformat()
        return super().default(obj)


TERMINAL_STATES = {
    "skipped_similarity",
    "fetch_failed",
    "eval_rejected",
    "pipeline_rejected",
    "written",
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def candidate_id(candidate: dict) -> str:
    key = candidate.get("url") or json.dumps(candidate, sort_keys=True)
    return hashlib.sha1(str(key).encode()).hexdigest()[:12]


def write_key(url: str, filename: str) -> str:
    return hashlib.sha1(f"{url}\n{filename}".encode()).hexdigest()


@dataclass
class ResearchSessionState:
    session_id: str
    query: str
    scope: dict
    state_dir: Path
    candidates: list[dict[str, Any]] = field(default_factory=list)
    status: str = "running"
    effective_depth: str | None = None
    written_keys: list[str] = field(default_factory=list)
    keyword_plan: dict[str, Any] = field(default_factory=dict)
    discovery_metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=_now)
    updated_at: str = field(default_factory=_now)

    @property
    def checkpoint_path(self) -> Path:
        return self.state_dir / f"session_{self.session_id}.json"

    @property
    def event_path(self) -> Path:
        return self.state_dir / f"session_{self.session_id}.jsonl"

    @classmethod
    def create(cls, session_id: str, query: str, scope: dict, state_dir: Path) -> "ResearchSessionState":
        state = cls(
            session_id=session_id,
            query=query,
            scope=scope,
            state_dir=state_dir,
            effective_depth=scope.get("depth"),
        )
        state.save("session_created")
        return state

    @classmethod
    def load(cls, session_id: str, state_dir: Path) -> "ResearchSessionState":
        path = state_dir / f"session_{session_id}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        return cls(
            session_id=data["session_id"],
            query=data["query"],
            scope=data["scope"],
            state_dir=state_dir,
            candidates=data.get("candidates", []),
            status=data.get("status", "running"),
            effective_depth=data.get("effective_depth") or data.get("scope", {}).get("depth"),
            written_keys=data.get("written_keys", []),
            keyword_plan=data.get("keyword_plan", {}),
            discovery_metadata=data.get("discovery_metadata", {}),
            created_at=data.get("created_at", _now()),
            updated_at=data.get("updated_at", _now()),
        )

    def save(self, event_type: str | None = None, payload: dict | None = None) -> None:
        self.state_dir.mkdir(parents=True, exist_ok=True)
        self.updated_at = _now()
        data = {
            "session_id": self.session_id,
            "query": self.query,
            "scope": self.scope,
            "status": self.status,
            "effective_depth": self.effective_depth,
            "candidates": self.candidates,
            "written_keys": self.written_keys,
            "keyword_plan": self.keyword_plan,
            "discovery_metadata": self.discovery_metadata,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
        self.checkpoint_path.write_text(json.dumps(data, indent=2, ensure_ascii=False, cls=_DateEncoder), encoding="utf-8")
        if event_type:
            event = {"timestamp": self.updated_at, "event": event_type, "payload": payload or {}}
            with self.event_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(event, ensure_ascii=False, cls=_DateEncoder) + "\n")

    def set_candidates(self, candidates: list[dict]) -> None:
        existing = {c["id"]: c for c in self.candidates}
        for raw in candidates:
            cid = candidate_id(raw)
            existing.setdefault(
                cid,
                {
                    "id": cid,
                    "candidate": raw,
                    "state": "discovered",
                    "qmd_matches": [],
                    "skip_reason": None,
                    "drafts": [],
                    "written_files": [],
                    "error": None,
                },
            )
        self.candidates = list(existing.values())
        self.save("candidates_discovered", {"count": len(self.candidates)})

    def set_keyword_plan(self, keyword_plan: dict[str, Any]) -> None:
        self.keyword_plan = keyword_plan
        self.save("keyword_plan", keyword_plan)

    def set_discovery_metadata(self, discovery_metadata: dict[str, Any]) -> None:
        self.discovery_metadata = discovery_metadata
        self.save("discovery_metadata", discovery_metadata)

    def transition(self, candidate_entry: dict, state: str, **fields: Any) -> None:
        candidate_entry["state"] = state
        candidate_entry.update(fields)
        self.save("candidate_state", {"id": candidate_entry.get("id"), "state": state, **fields})

    def pending_candidates(self) -> list[dict]:
        return [c for c in self.candidates if c.get("state") not in TERMINAL_STATES]

    def mark_written_key(self, key: str) -> None:
        if key not in self.written_keys:
            self.written_keys.append(key)
            self.save("write_key_recorded", {"write_key": key})


def list_sessions(state_dir: Path) -> list[dict]:
    sessions = []
    for path in sorted(state_dir.glob("session_*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        sessions.append({
            "session_id": data.get("session_id", path.stem.removeprefix("session_")),
            "query": data.get("query"),
            "status": data.get("status"),
            "updated_at": data.get("updated_at"),
            "candidates": len(data.get("candidates", [])),
        })
    return sessions
