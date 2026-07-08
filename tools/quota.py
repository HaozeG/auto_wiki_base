"""Session quota tracking for the research harness."""

from dataclasses import dataclass, field


# Hard caps that are not configurable per §12.8
MAX_API_CALLS_PER_SESSION = 50
# Ceiling for any subagent call. Per-model limits are set in research_config:
#   eval subagent (deepseek-v4-flash via CLAUDE_CODE_SUBAGENT_MODEL) needs ~8-12k for
#   multi-page draft output. Keyword recommender now defaults to the same
#   flash-tier model (see _keyword_recommender_model in orchestrator.py) rather
#   than a "thinking" model, so it no longer needs reasoning-trace headroom —
#   see max_keyword_recommender_tokens in CLAUDE.md's [research_config].
MAX_TOKENS_PER_SUBAGENT_OUTPUT = 16000
MIN_SECONDS_BETWEEN_CALLS = 1.0


@dataclass
class QuotaManager:
    max_candidates: int = 20
    max_new_pages: int = 10

    _candidates_evaluated: int = field(default=0, init=False)
    _pages_written: int = field(default=0, init=False)
    _api_calls: int = field(default=0, init=False)

    def record_api_call(self) -> None:
        self._api_calls += 1

    def record_candidate_evaluated(self) -> None:
        self._candidates_evaluated += 1

    def record_page_written(self) -> None:
        self._pages_written += 1

    def api_calls_exceeded(self) -> bool:
        return self._api_calls >= MAX_API_CALLS_PER_SESSION

    def candidates_exceeded(self) -> bool:
        return self._candidates_evaluated >= self.max_candidates

    def pages_exceeded(self) -> bool:
        return self._pages_written >= self.max_new_pages

    def any_exceeded(self) -> bool:
        return self.api_calls_exceeded() or self.candidates_exceeded() or self.pages_exceeded()

    def status(self) -> dict:
        return {
            "candidates_evaluated": self._candidates_evaluated,
            "max_candidates": self.max_candidates,
            "pages_written": self._pages_written,
            "max_new_pages": self.max_new_pages,
            "api_calls": self._api_calls,
            "max_api_calls": MAX_API_CALLS_PER_SESSION,
        }
