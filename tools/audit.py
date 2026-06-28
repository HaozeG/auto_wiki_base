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
        self._keyword_recommendations: list[dict] = []
        self._keyword_recommender_model: str | None = None
        self._discovery_queries_used: list[str] = []
        self._suppressed_repeat_urls: list[str] = []
        self._theme_profile: dict | None = None

        audit_dir = Path(__file__).parent.parent / "wiki" / "audit"
        audit_dir.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        self.path = audit_dir / f"research_{session_id}_{date_str}.json"
        if self.path.exists():
            try:
                existing = json.loads(self.path.read_text(encoding="utf-8"))
                self._invocations = existing.get("invocations", [])
                self._summary.update(existing.get("session_summary", {}))
                self._keyword_recommendations = existing.get("keyword_recommendations", [])
                self._keyword_recommender_model = existing.get("keyword_recommender_model")
                self._discovery_queries_used = existing.get("discovery_queries_used", [])
                self._suppressed_repeat_urls = existing.get("suppressed_repeat_urls", [])
                self._theme_profile = existing.get("theme_profile")
            except (OSError, json.JSONDecodeError):
                pass

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

    def set_keyword_plan(self, keyword_plan: dict) -> None:
        self._keyword_recommendations = keyword_plan.get("recommended_keywords", [])
        self._keyword_recommender_model = keyword_plan.get("model")
        self._flush()

    def set_discovery_metadata(self, discovery_metadata: dict) -> None:
        self._discovery_queries_used = discovery_metadata.get("queries_used", [])
        self._suppressed_repeat_urls = discovery_metadata.get("suppressed_repeat_urls", [])
        self._flush()

    def set_theme_profile(self, theme_profile: dict | None) -> None:
        self._theme_profile = theme_profile or None
        self._flush()

    def log_skip_pre_eval(self, url: str, reason: str, qmd_matches: list[dict] | None = None) -> None:
        """Record a candidate skipped before the eval subagent was called."""
        self._invocations.append({
            "subagent_type": "pre_eval_skip",
            "timestamp": self._now(),
            "url": url,
            "skipped_reason": reason,
            "qmd_matches": qmd_matches or [],
            "pages_written": [],
        })
        self._summary["pages_rejected_by_pipeline"] = (
            self._summary.get("pages_rejected_by_pipeline", 0) + 1
        )
        self._flush()

    def log_escalation(self, at_candidate: int) -> None:
        self._summary["depth_escalated_at"] = at_candidate
        self._flush()

    def _flush(self) -> None:
        data = {
            "session_id": self._session_id,
            "timestamp": self._now(),
            "query": self._query,
            "scope": self._scope,
            "keyword_recommendations": self._keyword_recommendations,
            "keyword_recommender_model": self._keyword_recommender_model,
            "discovery_queries_used": self._discovery_queries_used,
            "suppressed_repeat_urls": self._suppressed_repeat_urls,
            "theme_profile": self._theme_profile,
            "invocations": self._invocations,
            "session_summary": self._summary,
        }
        self.path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
