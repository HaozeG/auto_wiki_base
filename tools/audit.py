"""Audit log writer for research sessions."""

import json
import os
from datetime import datetime, timezone
from pathlib import Path


class AuditLog:
    def __init__(self, session_id: str, query: str, scope: dict):
        self._session_id = session_id
        self._query = query
        self._scope = scope
        self._invocations: list[dict] = []
        self._summary = {
            "candidates_found": 0,
            "candidates_evaluated": 0,
            "pages_written": 0,
            "pages_rejected_by_subagent": 0,
            "pages_rejected_by_pipeline": 0,
            "schema_validation_failures": 0,
        }

        audit_dir = Path(__file__).parent.parent / "wiki" / "audit"
        audit_dir.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        self.path = audit_dir / f"research_{session_id}_{date_str}.json"

    def _now(self) -> str:
        return datetime.now(timezone.utc).isoformat()

    def record_invocation(self, subagent_type: str, manifest: dict) -> int:
        """Record a subagent invocation. Returns the invocation index."""
        entry = {
            "subagent_type": subagent_type,
            "timestamp": self._now(),
            "input_manifest": manifest,
            "raw_response": None,
            "schema_valid": None,
            "pipeline_results": [],
            "pages_written": [],
            "skipped_reason": None,
        }
        self._invocations.append(entry)
        self._flush()
        return len(self._invocations) - 1

    def record_response(self, invocation_idx: int, raw_response: str, schema_valid: bool) -> None:
        self._invocations[invocation_idx]["raw_response"] = raw_response
        self._invocations[invocation_idx]["schema_valid"] = schema_valid
        if not schema_valid:
            self._summary["schema_validation_failures"] += 1
        self._flush()

    def record_pipeline_result(
        self,
        invocation_idx: int,
        filename: str,
        layer1_pass: bool,
        layer2_pass: bool,
        layer3_triggered: bool,
        final_decision: str,
        rejection_detail: str | None = None,
    ) -> None:
        self._invocations[invocation_idx]["pipeline_results"].append({
            "filename": filename,
            "layer1_pass": layer1_pass,
            "layer2_pass": layer2_pass,
            "layer3_triggered": layer3_triggered,
            "final_decision": final_decision,
            "rejection_detail": rejection_detail,
        })
        if final_decision == "rejected":
            self._summary["pages_rejected_by_pipeline"] += 1
        self._flush()

    def record_page_written(self, invocation_idx: int, filename: str) -> None:
        self._invocations[invocation_idx]["pages_written"].append(filename)
        self._summary["pages_written"] += 1
        self._flush()

    def record_skip(self, invocation_idx: int, reason: str) -> None:
        self._invocations[invocation_idx]["skipped_reason"] = reason
        if "subagent_reject" in reason:
            self._summary["pages_rejected_by_subagent"] += 1
        self._flush()

    def set_candidates_found(self, count: int) -> None:
        self._summary["candidates_found"] = count
        self._flush()

    def set_candidates_evaluated(self, count: int) -> None:
        self._summary["candidates_evaluated"] = count
        self._flush()

    def _flush(self) -> None:
        data = {
            "session_id": self._session_id,
            "timestamp": self._now(),
            "query": self._query,
            "scope": self._scope,
            "invocations": self._invocations,
            "session_summary": self._summary,
        }
        self.path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
