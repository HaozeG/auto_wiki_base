import json
import re
import sys
import types
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).parent.parent))

import frontmatter
import orchestrator
from qmd_runner import QmdMatch, QmdRunner, assess_candidate_similarity
from quota import QuotaManager
from research_state import ResearchSessionState


class DummyAudit:
    path = Path("dummy_audit.json")

    def set_candidates_found(self, count):
        self.candidates_found = count

    def set_candidates_evaluated(self, count):
        self.candidates_evaluated = count

    def log_skip_pre_eval(self, url, reason, qmd_matches=None):
        self.skip = {"url": url, "reason": reason, "qmd_matches": qmd_matches or []}

    def record_page_written(self, idx, filename):
        self.written = getattr(self, "written", []) + [filename]


class FakeQmdRunner:
    def update(self):
        return True, None

    def search(self, *args, **kwargs):
        raise AssertionError("approved resume should not re-run qmd search")


class EmptyQmdRunner:
    def update(self):
        return True, None

    def search(self, *args, **kwargs):
        return types.SimpleNamespace(ok=True, matches=[])


class FullDummyAudit(DummyAudit):
    path = Path("dummy_audit.json")

    def __init__(self):
        self.invocations = []
        self.responses = []
        self.pipeline = []

    def record_invocation(self, subagent_type, manifest):
        self.invocations.append({"subagent_type": subagent_type, "manifest": manifest})
        return len(self.invocations) - 1

    def record_response(self, idx, raw_response, schema_valid, usage=None):
        self.responses.append((idx, schema_valid))

    def record_skip(self, idx, reason):
        self.skip = {"idx": idx, "reason": reason}

    def record_pipeline_result(self, *args, **kwargs):
        self.pipeline.append(kwargs)

    def log_escalation(self, at_candidate):
        self.escalated_at = at_candidate


def _run_result(stdout_obj, returncode=0):
    result = MagicMock()
    result.returncode = returncode
    result.stdout = json.dumps(stdout_obj)
    result.stderr = ""
    return result


def test_qmd_runner_uses_uv_no_sync_command():
    with patch("subprocess.run", return_value=_run_result([])) as run:
        QmdRunner().search("SpacemiT K3", top=3)

    cmd = run.call_args.args[0]
    assert cmd[:4] == ["uv", "run", "--no-sync", "qmd"]
    assert cmd[4:8] == ["search", "SpacemiT K3", "-c", "_pages"]
    assert "--format" in cmd
    assert "json" in cmd


def test_qmd_failure_blocks_result():
    failed = MagicMock(returncode=1, stdout="", stderr="boom")
    with patch("subprocess.run", return_value=failed):
        result = QmdRunner().search("query")

    assert result.blocked is True
    assert result.error == "boom"


def test_similarity_gate_skips_high_score_match():
    decision = assess_candidate_similarity(
        {"title": "Gemmini RISC-V accelerator", "snippet": "systolic array"},
        [QmdMatch(rank=1, file="qmd://_pages/entity/gemmini.md", score=0.95)],
        {"near_duplicate_score": 0.90, "topic_similarity_min_score": 0.80},
    )

    assert decision["skip"] is True
    assert decision["reason"] == "near_duplicate_score"
    assert decision["matches"][0]["file"].endswith("gemmini.md")


def test_similarity_gate_uses_rank_only_duplicate_signal():
    decision = assess_candidate_similarity(
        {"title": "Gemmini RISC-V accelerator", "snippet": ""},
        [QmdMatch(rank=1, file="entity/gemmini.md", score=None)],
        {"title_overlap_threshold": 0.4},
    )

    assert decision["skip"] is True
    assert decision["reason"] == "rank_only_duplicate_signal"


def test_rank_only_signal_does_not_skip_single_vendor_overlap():
    decision = assess_candidate_similarity(
        {"title": "Tenstorrent Wormhole performance profiler", "snippet": ""},
        [QmdMatch(rank=1, file="entity/tenstorrent_tt_metal.md", score=None)],
        {},
    )

    assert decision["skip"] is False
    assert decision["reason"] is None


def test_title_overlap_is_hard_duplicate_not_stack_topic_overlap():
    assert orchestrator._title_word_overlap(
        "tenstorrent/tt-metal | Score 51 | AI / Machine Learning — GitFind",
        "tenstorrent_tt_metal",
    ) >= 0.8
    assert orchestrator._title_word_overlap("Gemmini", "gemmini") >= 0.8
    assert orchestrator._title_word_overlap("Milk-V Pioneer | Make native RISC-V", "milkv_pioneer_duo") >= 0.8

    assert orchestrator._title_word_overlap("Tenstorrent", "tenstorrent_tt_metal") < 0.8
    assert orchestrator._title_word_overlap("Tenstorrent TT-Metal profiler", "tenstorrent_tt_metal") < 0.8
    assert orchestrator._title_word_overlap(
        "TT-Metalium neural network model compilation guide",
        "tenstorrent_tt_metal",
    ) < 0.8


def test_similarity_gate_blocks_spacemit_same_family():
    decision = assess_candidate_similarity(
        {"title": "SpacemiT K3 AI SoC", "snippet": "60 TOPS"},
        [QmdMatch(rank=1, file="entity/spacemit_k1_soc.md", score=0.82)],
        {
            "topic_similarity_min_score": 0.80,
            "near_duplicate_score": 0.90,
            "topic_saturation_hit_threshold": 2,
        },
    )

    assert decision["skip"] is True
    assert decision["reason"] in {"same_product_family", "topic_saturation"}


def test_similarity_gate_treats_topic_saturation_as_merge_hint_not_skip():
    decision = assess_candidate_similarity(
        {"title": "ProjectNimbus vector optimization guide", "snippet": "compiler recipe"},
        [
            QmdMatch(rank=1, file="entity/nimbus_vector.md", score=0.83),
            QmdMatch(rank=2, file="entity/nimbus_compiler.md", score=0.82),
            QmdMatch(rank=3, file="entity/nimbus_sdk.md", score=0.81),
        ],
        {
            "topic_similarity_min_score": 0.80,
            "near_duplicate_score": 0.90,
            "topic_saturation_hit_threshold": 2,
        },
    )

    assert decision["skip"] is False
    assert decision["merge_hint"] == "topic_saturation"
    assert decision["reason"] is None


def test_qmd_block_stops_before_discovery_or_eval(tmp_path):
    with patch.object(orchestrator, "_generate_session_id", return_value="blocked1"), \
         patch.object(orchestrator, "_load_research_config", return_value={
             "qmd_command": ["uv", "run", "--no-sync", "qmd"],
             "research_state_dir": str(tmp_path),
         }), \
         patch.object(orchestrator, "_run_qmd_update", return_value=(False, "qmd unavailable")), \
         patch.object(orchestrator, "_ddg_discover") as discover, \
         patch.object(orchestrator, "_call_subagent") as call_subagent, \
         patch.object(orchestrator, "AuditLog", return_value=DummyAudit()):
        result = orchestrator.run_research_session("query", 2, 1, "shallow")

    assert result["status"] == "blocked_qmd"
    discover.assert_not_called()
    call_subagent.assert_not_called()


def test_keyword_recommender_model_defaults_to_cheap_flash_tier():
    with patch.dict(
        "os.environ",
        {
            "ANTHROPIC_MODEL": "deepseek-v4-pro[1m]",
            "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash",
            "CLAUDE_CODE_SUBAGENT_MODEL": "deepseek-v4-flash",
        },
        clear=True,
    ):
        model = orchestrator._keyword_recommender_model({})

    # Recommending search queries is no harder than eval/synthesis, which
    # already run on the cheap flash tier — no reason to default to the
    # stronger/"thinking" ANTHROPIC_MODEL tier just for this role.
    assert model == "deepseek-v4-flash"


def test_keyword_recommender_model_override_preserves_thinking_suffix():
    with patch.dict("os.environ", {}, clear=True):
        model = orchestrator._keyword_recommender_model(
            {"keyword_recommender_model": "deepseek-v4-pro[1m]"}
        )

    assert model == "deepseek-v4-pro[1m]"


def test_keyword_recommender_uses_anthropic_and_cheap_default_model(monkeypatch):
    calls = {}

    class FakeMessages:
        def create(self, **kwargs):
            calls.update(kwargs)
            response = MagicMock()
            block = MagicMock()
            block.text = json.dumps({
                "recommended_keywords": [
                    {"query": "ProjectNimbus latency benchmark", "reason": "Find implementation data"}
                ],
                "avoid_patterns": ["marketing"],
            })
            response.content = [block]
            return response

    class FakeAnthropic:
        def __init__(self):
            self.messages = FakeMessages()

    monkeypatch.setitem(sys.modules, "anthropic", types.SimpleNamespace(Anthropic=FakeAnthropic))
    with patch.dict(
        "os.environ",
        {"ANTHROPIC_MODEL": "deepseek-v4-pro[1m]", "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash"},
        clear=True,
    ):
        plan = orchestrator._call_keyword_recommender(
            {"base_query": "ProjectNimbus", "concept_gaps": [], "max_keywords": 3},
            {},
        )

    assert calls["model"] == "deepseek-v4-flash"
    assert calls["model"] != "deepseek-v4-pro[1m]"
    assert calls["max_tokens"] == 6000
    assert plan["source"] == "llm"
    assert plan["recommended_keywords"][0]["query"] == "ProjectNimbus latency benchmark"


def test_keyword_recommender_falls_back_on_malformed_json(monkeypatch):
    class FakeMessages:
        def create(self, **kwargs):
            response = MagicMock()
            block = MagicMock()
            block.text = "not json"
            response.content = [block]
            return response

    class FakeAnthropic:
        def __init__(self):
            self.messages = FakeMessages()

    monkeypatch.setitem(sys.modules, "anthropic", types.SimpleNamespace(Anthropic=FakeAnthropic))
    plan = orchestrator._call_keyword_recommender(
        {"base_query": "ProjectNimbus", "concept_gaps": [], "max_keywords": 2},
        {"keyword_recommender_model": "deepseek-v4-pro[1m]"},
    )

    assert plan["source"] == "fallback_error"
    assert plan["model"] == "deepseek-v4-pro[1m]"
    assert len(plan["recommended_keywords"]) == 2


def test_github_blob_markdown_fetches_raw_file(monkeypatch):
    calls = []

    def fake_fetch(url, retries=2):
        calls.append(url)
        return "# K230 RVV Optimization\n\n" + ("RVV vector optimization details. " * 20)

    monkeypatch.setattr(orchestrator, "fetch_resource", fake_fetch)

    content = orchestrator._fetch_github(
        "https://github.com/kendryte/k230_sdk/blob/main/docs/zh/01_software/board/rvv_optimization.md"
    )

    assert calls == [
        "https://raw.githubusercontent.com/kendryte/k230_sdk/main/docs/zh/01_software/board/rvv_optimization.md"
    ]
    assert content.startswith("[GitHub file: kendryte/k230_sdk/main/docs/zh/01_software/board/rvv_optimization.md]")
    assert "K230 RVV Optimization" in content


def test_github_repo_url_still_fetches_readme(monkeypatch):
    calls = []

    def fake_fetch(url, retries=2):
        calls.append(url)
        return "# README\n\n" + ("repository documentation " * 20)

    monkeypatch.setattr(orchestrator, "fetch_resource", fake_fetch)

    content = orchestrator._fetch_github("https://github.com/example/project")

    assert calls == ["https://raw.githubusercontent.com/example/project/HEAD/README.md"]
    assert content.startswith("[GitHub README: example/project]")
    assert "repository documentation" in content


def test_github_pr_url_still_uses_pr_path(monkeypatch):
    calls = []

    def fake_pr(owner, repo, pr_num):
        calls.append((owner, repo, pr_num))
        return "[GitHub PR #42: vector patch]\nbody"

    monkeypatch.setattr(orchestrator, "_fetch_github_pr", fake_pr)
    monkeypatch.setattr(orchestrator, "_fetch_github_readme", MagicMock())

    content = orchestrator._fetch_github("https://github.com/example/project/pull/42")

    assert calls == [("example", "project", "42")]
    assert content == "[GitHub PR #42: vector patch]\nbody"
    orchestrator._fetch_github_readme.assert_not_called()


def test_html_boilerplate_uses_enriched_snippet_before_eval(monkeypatch):
    html = (
        "<!doctype html><html><head><style>"
        + ".css{display:flex;box-sizing:border-box;font-family:sans-serif;}" * 200
        + "</style><script>window.__NEXT_DATA__={};document.addEventListener('x', function(){})</script>"
        + "</head><body><nav>Sign in</nav><main><h1>K230 RVV</h1><p>short note</p></main></body></html>"
    )
    monkeypatch.setattr(
        orchestrator,
        "_enrich_snippet",
        lambda title, snippet: f"[Search snippets for: {title}]\n{snippet}\n- K230 RVV optimization: substantive optimization details",
    )

    content = orchestrator._content_or_enriched_snippet(
        html,
        "K230 RVV optimization",
        "K230 RVV uses vector kernels",
        "https://example.com/rendered",
    )

    assert content.startswith("[Search snippets for: K230 RVV optimization]")
    assert "substantive optimization details" in content
    assert "display:flex" not in content


def test_recent_discovery_history_collects_previous_queries(tmp_path):
    audit_dir = tmp_path / "audit"
    audit_dir.mkdir()
    audit_file = audit_dir / "research_abc_2026-01-01.json"
    audit_file.write_text(json.dumps({
        "query": "ProjectNimbus latency",
        "discovery_queries_used": ["ProjectNimbus docs", "ProjectNimbus benchmark"],
        "keyword_recommendations": [
            {"query": "ProjectNimbus implementation repository", "reason": "new source"}
        ],
        "invocations": [],
    }), encoding="utf-8")

    with patch.object(orchestrator, "_audit_dir", return_value=audit_dir):
        history = orchestrator._load_recent_discovery_history({
            "recent_audit_sessions_for_discovery": 10,
        })

    assert history["previous_queries"] == [
        "ProjectNimbus latency",
        "ProjectNimbus docs",
        "ProjectNimbus benchmark",
        "ProjectNimbus implementation repository",
    ]


def test_recent_discovery_history_flags_zero_yield_sessions(tmp_path):
    """Regression coverage for the zero-yield feedback loop: sessions that
    evaluated a real candidate budget but wrote 0 pages (e.g. session
    e545ec7c in wiki/log.md, query drifted off-theme into formal verification)
    should surface in zero_yield_queries so the keyword recommender can steer
    away from repeating that query's angle.
    """
    audit_dir = tmp_path / "audit"
    audit_dir.mkdir()
    (audit_dir / "research_zero_2026-01-01.json").write_text(json.dumps({
        "query": "RISC-V verification formal methods hardware bug fuzzing",
        "session_summary": {
            "candidates_evaluated": 10,
            "pages_written": 0,
            "pages_rejected_by_subagent": 10,
        },
        "invocations": [],
    }), encoding="utf-8")
    (audit_dir / "research_ok_2026-01-02.json").write_text(json.dumps({
        "query": "ProjectNimbus GEMM benchmark",
        "session_summary": {"candidates_evaluated": 5, "pages_written": 2},
        "invocations": [],
    }), encoding="utf-8")
    # Below the 3-candidate threshold: a tiny/aborted session shouldn't count
    # as a confirmed unproductive angle.
    (audit_dir / "research_tiny_2026-01-03.json").write_text(json.dumps({
        "query": "ProjectNimbus tiny probe",
        "session_summary": {"candidates_evaluated": 1, "pages_written": 0},
        "invocations": [],
    }), encoding="utf-8")

    with patch.object(orchestrator, "_audit_dir", return_value=audit_dir):
        history = orchestrator._load_recent_discovery_history({
            "recent_audit_sessions_for_discovery": 10,
        })

    queries = [z["query"] for z in history["zero_yield_queries"]]
    assert queries == ["RISC-V verification formal methods hardware bug fuzzing"]
    assert history["zero_yield_queries"][0]["candidates_evaluated"] == 10


def test_early_exit_stops_after_escalation_keeps_failing(tmp_path):
    """After adaptive depth escalation, if candidates keep failing evaluation
    with 0 pages written, the session should stop rather than spend its whole
    candidate budget (see wiki/audit/research_e545ec7c_2026-07-02.json: 10/10
    candidates rejected, escalated at candidate 5, no early exit existed).
    """
    pages_dir = tmp_path / "wiki" / "_pages"
    pages_dir.mkdir(parents=True)
    index = tmp_path / "wiki" / "index.md"
    index.write_text(
        "# Wiki Index\n\nLast updated: 2020-01-01 | Pages: 0 | Sources: 0\n\n"
        "## Entity Pages\n\n| Page | Summary | Tags | Sources | Inbound |\n"
        "|------|---------|------|---------|---------|\n\n"
        "## Synthesis Pages\n\n| Page | Connected Entities | Status | Inbound |\n"
        "|------|--------------------|--------|---------|\n",
        encoding="utf-8",
    )
    log_path = tmp_path / "wiki" / "log.md"
    log_path.write_text("", encoding="utf-8")
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text("```yaml\n[system_state]\ngraph_maturity: true\n```\n", encoding="utf-8")

    # 8 candidates so escalation (halfway=4) fires, then early_exit_after=3
    # more rejections should stop the loop before candidate 8 is evaluated.
    candidates = [{"url": f"https://example.com/{i}", "title": f"Candidate {i}"} for i in range(8)]
    state = ResearchSessionState.create(
        "sess-early-exit", "unproductive query",
        {"max_candidates": 8, "max_new_pages": 5, "depth": "shallow"},
        tmp_path / "state",
    )
    state.set_candidates(candidates)

    reject_eval = json.dumps({
        "decision": "reject",
        "rejection_reason": "not relevant",
        "scorecard": {"weighted_total": 0.1},
        "page_drafts": [],
        "pages_to_update": [],
        "contradictions_found": [],
    })

    with patch.object(orchestrator, "_load_research_config", return_value={
             "qmd_command": ["uv", "run", "--no-sync", "qmd"],
             "research_state_dir": str(tmp_path / "state"),
             "early_exit_after_escalation_failures": 3,
         }), \
         patch.object(orchestrator, "QmdRunner", return_value=EmptyQmdRunner()), \
         patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_INDEX_MD", index), \
         patch.object(orchestrator, "_LOG_MD", log_path), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md), \
         patch.object(orchestrator, "AuditLog", return_value=FullDummyAudit()), \
         patch.object(orchestrator, "_check_synthesis_gaps", return_value=[]), \
         patch.object(orchestrator, "_get_concept_gaps", return_value=[]), \
         patch.object(orchestrator, "_fetch_smart", return_value="some content about the candidate"), \
         patch.object(orchestrator, "_call_subagent", return_value=reject_eval):
        result = orchestrator._run_research_state(state)

    assert result["status"] == "complete"
    # 4 (halfway, triggers escalation) + 3 (early-exit threshold) = 7 evaluated,
    # the 8th candidate should never have been reached.
    assert result["candidates_evaluated"] == 7
    evaluated_states = {c["state"] for c in state.candidates}
    assert "eval_rejected" in evaluated_states
    assert any(c["state"] == "discovered" for c in state.candidates)


def _minimal_research_state_fixture(tmp_path, session_id, candidates, max_candidates=5):
    pages_dir = tmp_path / "wiki" / "_pages"
    pages_dir.mkdir(parents=True)
    index = tmp_path / "wiki" / "index.md"
    index.write_text(
        "# Wiki Index\n\nLast updated: 2020-01-01 | Pages: 0 | Sources: 0\n\n"
        "## Entity Pages\n\n| Page | Summary | Tags | Sources | Inbound |\n"
        "|------|---------|------|---------|---------|\n\n"
        "## Synthesis Pages\n\n| Page | Connected Entities | Status | Inbound |\n"
        "|------|--------------------|--------|---------|\n",
        encoding="utf-8",
    )
    log_path = tmp_path / "wiki" / "log.md"
    log_path.write_text("", encoding="utf-8")
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text("```yaml\n[system_state]\ngraph_maturity: true\n```\n", encoding="utf-8")
    state = ResearchSessionState.create(
        session_id, "query",
        {"max_candidates": max_candidates, "max_new_pages": 5, "depth": "shallow"},
        tmp_path / "state",
    )
    state.set_candidates(candidates)
    return state, pages_dir, index, log_path, claude_md


def test_evaluating_candidate_retried_then_given_up_after_repeated_interruption(tmp_path):
    """A candidate found in "evaluating" state at resume start means a prior
    process was killed/crashed mid-candidate (see resume-path robustness gap
    hit live during the 2026-07-08 test run: candidates stuck "evaluating"
    aren't in resume's terminal skip-set, so a persistently unreachable URL
    re-runs its full fetch-retry sequence on every single resume, consuming
    most of the time budget and blocking every candidate behind it). It
    should be retried, but only up to max_evaluating_resume_retries times
    before being given up as fetch_failed."""
    state, pages_dir, index, log_path, claude_md = _minimal_research_state_fixture(
        tmp_path, "sess-stall", [
            {"url": "https://example.com/stuck", "title": "Stuck Candidate"},
        ],
    )
    # Simulate two prior resumes that were each interrupted mid-candidate.
    entry = state.candidates[0]
    entry["state"] = "evaluating"
    entry["resume_stall_count"] = 2

    fetch_calls = []

    def fake_fetch(url, retries=2):
        fetch_calls.append(url)
        return "some content"

    with patch.object(orchestrator, "_load_research_config", return_value={
             "qmd_command": ["uv", "run", "--no-sync", "qmd"],
             "research_state_dir": str(tmp_path / "state"),
             "max_evaluating_resume_retries": 2,
         }), \
         patch.object(orchestrator, "QmdRunner", return_value=EmptyQmdRunner()), \
         patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_INDEX_MD", index), \
         patch.object(orchestrator, "_LOG_MD", log_path), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md), \
         patch.object(orchestrator, "AuditLog", return_value=FullDummyAudit()), \
         patch.object(orchestrator, "_check_synthesis_gaps", return_value=[]), \
         patch.object(orchestrator, "_get_concept_gaps", return_value=[]), \
         patch.object(orchestrator, "_fetch_smart", side_effect=fake_fetch):
        result = orchestrator._run_research_state(state)

    assert result["status"] == "complete"
    assert entry["state"] == "fetch_failed"
    assert "3 interrupted resume attempts" in entry["error"]
    # Given up before ever re-attempting the fetch — the whole point is not
    # to burn the time budget on a candidate that keeps getting interrupted.
    assert fetch_calls == []


def test_evaluating_candidate_retried_normally_before_retry_limit(tmp_path):
    """Below max_evaluating_resume_retries, an "evaluating" candidate is
    retried like any other pending candidate, not silently dropped."""
    state, pages_dir, index, log_path, claude_md = _minimal_research_state_fixture(
        tmp_path, "sess-stall-retry", [
            {"url": "https://example.com/stuck", "title": "Stuck Candidate"},
        ],
    )
    entry = state.candidates[0]
    entry["state"] = "evaluating"
    entry["resume_stall_count"] = 1

    reject_eval = json.dumps({
        "decision": "reject",
        "rejection_reason": "not relevant",
        "scorecard": {"weighted_total": 0.1},
        "page_drafts": [],
        "pages_to_update": [],
        "contradictions_found": [],
    })

    with patch.object(orchestrator, "_load_research_config", return_value={
             "qmd_command": ["uv", "run", "--no-sync", "qmd"],
             "research_state_dir": str(tmp_path / "state"),
             "max_evaluating_resume_retries": 2,
         }), \
         patch.object(orchestrator, "QmdRunner", return_value=EmptyQmdRunner()), \
         patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_INDEX_MD", index), \
         patch.object(orchestrator, "_LOG_MD", log_path), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md), \
         patch.object(orchestrator, "AuditLog", return_value=FullDummyAudit()), \
         patch.object(orchestrator, "_check_synthesis_gaps", return_value=[]), \
         patch.object(orchestrator, "_get_concept_gaps", return_value=[]), \
         patch.object(orchestrator, "_fetch_smart", return_value="some content about the candidate"), \
         patch.object(orchestrator, "_call_subagent", return_value=reject_eval):
        result = orchestrator._run_research_state(state)

    assert result["status"] == "complete"
    assert entry["state"] == "eval_rejected"
    assert entry["resume_stall_count"] == 2


def test_keyword_manifest_includes_theme_and_previous_queries(monkeypatch):
    captured = {}

    def fake_call(manifest, research_config, usage_out=None):
        captured.update(manifest)
        return {"recommended_keywords": [], "avoid_patterns": [], "model": "test", "source": "test"}

    monkeypatch.setattr(orchestrator, "_call_keyword_recommender", fake_call)
    monkeypatch.setattr(orchestrator, "_get_repo_research_theme", lambda: "ProjectNimbus theme")
    monkeypatch.setattr(orchestrator, "_get_wiki_topic_summary", lambda: "Current coverage")
    monkeypatch.setattr(orchestrator, "_get_concept_gaps", lambda: ["Missing API"])
    monkeypatch.setattr(orchestrator, "_bridge_candidates_for_manifest", lambda: [])

    orchestrator._build_keyword_plan(
        "ProjectNimbus latency",
        {"keyword_recommendation_limit": 3},
        "shallow",
        {"previous_queries": ["ProjectNimbus docs"]},
    )

    assert captured["repo_research_theme"] == "ProjectNimbus theme"
    assert captured["previous_search_keywords"] == ["ProjectNimbus docs"]
    assert captured["wiki_topic_summary"] == "Current coverage"
    assert captured["concept_gaps"] == ["Missing API"]
    assert captured["bridge_candidates"] == []


def test_keyword_plan_records_full_manifest_to_audit_when_provided(monkeypatch):
    """Regression: previously only the recommender's *output* (keyword_plan)
    was ever saved (audit.set_keyword_plan()) -- there was no way to inspect
    what input it actually received (concept_gaps, bridge_candidates,
    gap_manifest, etc.) after the fact. Record the full manifest the same way
    "synthesis"/"evaluation" invocations already are."""
    from audit import AuditLog

    def fake_call(manifest, research_config, usage_out=None):
        return {"recommended_keywords": [{"query": "q", "reason": "r"}], "avoid_patterns": [],
                "model": "test", "source": "test"}

    monkeypatch.setattr(orchestrator, "_call_keyword_recommender", fake_call)
    monkeypatch.setattr(orchestrator, "_get_repo_research_theme", lambda: "theme")
    monkeypatch.setattr(orchestrator, "_get_wiki_topic_summary", lambda: "summary")
    monkeypatch.setattr(orchestrator, "_get_concept_gaps", lambda: [])
    monkeypatch.setattr(orchestrator, "_bridge_candidates_for_manifest",
                        lambda: [{"topic_a": "A", "topic_b": "B", "reason": "distant"}])

    audit = AuditLog("sess-audit-test", "q", {})
    audit.path.unlink(missing_ok=True)

    orchestrator._build_keyword_plan(
        "q", {}, "shallow", {}, audit=audit,
    )

    assert len(audit._invocations) == 1
    inv = audit._invocations[0]
    assert inv["subagent_type"] == "keyword_recommender"
    assert inv["input_manifest"]["bridge_candidates"] == [
        {"topic_a": "A", "topic_b": "B", "reason": "distant"}
    ]
    assert inv["schema_valid"] is True
    assert "recommended_keywords" in inv["raw_response"]
    audit.path.unlink(missing_ok=True)


def test_load_research_config_merges_selected_theme_profile(tmp_path, monkeypatch):
    claude = tmp_path / "CLAUDE.md"
    claude.write_text(
        "```yaml\n"
        "[research_config]\n"
        "topic_saturation_hit_threshold: 2\n"
        "preferred_source_types:\n"
        "  - generic source\n"
        "```\n\n"
        "```yaml\n"
        "[theme_profile]\n"
        "theme: RISC-V AI accelerator\n"
        "organization_choice: workflow_first\n"
        "page_types:\n"
        "  entity: General entity page\n"
        "  synthesis: Cross-page synthesis\n"
        "  hardware_target: Hardware or ISA target\n"
        "  benchmark_result: Measured result\n"
        "source_preferences:\n"
        "  - official documentation\n"
        "  - benchmark repository\n"
        "coverage_priorities:\n"
        "  - hardware/software/workload coverage\n"
        "lint_priorities:\n"
        "  - benchmark measurement context\n"
        "```\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(orchestrator, "_CLAUDE_MD", claude)

    config = orchestrator._load_research_config()

    assert config["theme_profile"]["theme"] == "RISC-V AI accelerator"
    assert "hardware_target" in config["page_type_taxonomy"]
    assert "benchmark_result" in config["page_type_taxonomy"]
    assert config["preferred_source_types"] == ["official documentation", "benchmark repository"]


def test_literature_theme_profile_extraction_patterns_flow_end_to_end(tmp_path, monkeypatch):
    """Phase 4c dry-run check: a non-hardware theme's extraction_patterns,
    hand-added to [theme_profile] the same way page_types already is, must
    actually reach extract_evidence() through _load_research_config() — not
    just work when called directly with a literal config dict (unit-tested
    separately in test_domain_analysis.py).
    """
    from domain_analysis import extract_evidence

    claude = tmp_path / "CLAUDE.md"
    claude.write_text(
        "```yaml\n[research_config]\n```\n\n"
        "```yaml\n"
        "[theme_profile]\n"
        "theme: Victorian novel\n"
        "organization_choice: character_first\n"
        "page_types:\n"
        "  entity: General entity page\n"
        "  synthesis: Cross-page synthesis\n"
        "  character: Person or character with traits, relationships, and arc\n"
        "extraction_patterns:\n"
        "  hardware: ['[A-Z][a-z]+ [A-Z][a-z]+']\n"
        "  workloads: ['marriage', 'inheritance']\n"
        "  metrics: ['reputation']\n"
        "```\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(orchestrator, "_CLAUDE_MD", claude)

    config = orchestrator._load_research_config()
    assert config["extraction_patterns"]["workloads"] == ["marriage", "inheritance"]

    evidence = extract_evidence(
        "Elizabeth Bennet weighs marriage and inheritance against reputation.",
        {"title": "Reading notes"},
        config,
    )
    assert "Elizabeth Bennet" in evidence["hardware_names"]
    assert "marriage" in [w.lower() for w in evidence["workload_names"]]
    assert "reputation" in evidence["metrics"]
    assert "GEMM" not in evidence["workload_names"]


def test_write_theme_profile_inserts_selected_profile(tmp_path, monkeypatch):
    claude = tmp_path / "CLAUDE.md"
    claude.write_text(
        "# LLM Wiki\n\n"
        "```yaml\n"
        "[research_config]\n"
        "page_type_taxonomy:\n"
        "  entity: general concept\n"
        "  synthesis: cross-page comparison\n"
        "```\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(orchestrator, "_CLAUDE_MD", claude)
    # Force deterministic fallback — isolate from any on-disk cached profiles
    monkeypatch.setattr(orchestrator, "_load_cached_profiles", lambda _theme: None)

    profile = orchestrator.select_theme_profile("RISC-V AI accelerator", "workflow_first")
    orchestrator.write_theme_profile(profile)

    text = claude.read_text(encoding="utf-8")
    assert "[theme_profile]" in text
    assert "theme: RISC-V AI accelerator" in text
    assert "organization_choice: workflow_first" in text
    assert "hardware_target:" in text


def test_audit_log_records_theme_profile(tmp_path, monkeypatch):
    import audit as audit_module

    fake_tools_dir = tmp_path / "tools"
    fake_tools_dir.mkdir()
    monkeypatch.setattr(audit_module, "__file__", str(fake_tools_dir / "audit.py"))
    audit_log = audit_module.AuditLog("sess-theme", "query", {"depth": "shallow"})
    audit_log.set_theme_profile({"theme": "RISC-V AI accelerator", "organization_choice": "workflow_first"})

    data = json.loads(audit_log.path.read_text(encoding="utf-8"))
    assert data["theme_profile"]["theme"] == "RISC-V AI accelerator"
    assert data["theme_profile"]["organization_choice"] == "workflow_first"


def test_repo_research_theme_is_clean_and_domain_specific(tmp_path, monkeypatch):
    readme = tmp_path / "README.md"
    readme.write_text(
        "The current example wiki is focused on ProjectNimbus latency systems, "
        "but the structure is reusable for other research domains.\n",
        encoding="utf-8",
    )
    index = tmp_path / "wiki" / "index.md"
    index.parent.mkdir()
    index.write_text(
        "# Wiki Index\n\n"
        "Last updated: 2026-01-01 | Pages: 3 | Sources: 7\n\n"
        "| Page | Summary | Tags | Sources | Inbound |\n"
        "|------|---------|------|---------|---------|\n"
        "| [nimbus_core.md](entity/nimbus_core.md) | Low-latency scheduler | scheduler, latency | 2 | 1 |\n"
        "| [nimbus_sdk.md](entity/nimbus_sdk.md) | SDK and deployment tools | sdk, latency | 1 | 0 |\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(orchestrator, "_PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(orchestrator, "_INDEX_MD", index)

    theme = orchestrator._get_repo_research_theme()

    assert "Current wiki focus: ProjectNimbus latency systems." in theme
    assert "reusable for other research domains" not in theme
    assert "Wiki scale: 3 pages, 7 sources." in theme
    assert "Recurring tags:" in theme
    assert "nimbus_core.md: Low-latency scheduler" in theme
    assert "| [nimbus_core.md]" not in theme


def test_ddg_discover_orders_recommendations_and_suppresses_repeats(monkeypatch):
    calls = []

    class FakeDDGS:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def text(self, query, max_results):
            calls.append(query)
            if query == "base query ProjectNimbus benchmark":
                return [
                    {"href": "https://avoid.example/page", "title": "Marketing", "body": "skip"},
                    {"href": "https://repeat.example/a", "title": "Repeat ProjectNimbus", "body": "old"},
                    {"href": "https://generic.example/a", "title": "AI software stack", "body": "No anchor term"},
                    {"href": "https://new.example/keyword", "title": "ProjectNimbus Keyword", "body": "new"}
                ]
            if query == "base query":
                return [
                    {"href": "https://new.example/base", "title": "Base", "body": "new"},
                ]
            return []

    monkeypatch.setitem(sys.modules, "ddgs", types.SimpleNamespace(DDGS=FakeDDGS))
    metadata = {}
    candidates = orchestrator._ddg_discover(
        "base query",
        2,
        already_processed=set(),
        research_config={"discovery_search_queries_limit": 3, "repeat_url_suppression": True},
        depth="shallow",
        keyword_plan={
            "recommended_keywords": [
                {"query": "base query ProjectNimbus benchmark", "reason": "diversify"}
            ],
            "avoid_patterns": ["avoid.example"],
        },
        discovery_metadata=metadata,
        repeat_urls={"https://repeat.example/a"},
    )

    assert calls[0] == "base query ProjectNimbus benchmark"
    assert [c["url"] for c in candidates] == [
        "https://new.example/keyword",
        "https://new.example/base",
    ]
    assert metadata["suppressed_repeat_urls"] == ["https://repeat.example/a"]


def test_session_checkpoint_pending_skips_terminal_candidates(tmp_path):
    state = ResearchSessionState.create("sess1", "query", {"depth": "shallow"}, tmp_path)
    state.set_candidates([
        {"url": "https://example.com/a", "title": "A"},
        {"url": "https://example.com/b", "title": "B"},
    ])
    state.transition(state.candidates[0], "skipped_similarity", qmd_matches=[{"file": "a.md"}])
    state.transition(state.candidates[1], "approved", drafts=[])

    loaded = ResearchSessionState.load("sess1", tmp_path)
    pending = loaded.pending_candidates()

    assert len(pending) == 1
    assert pending[0]["candidate"]["url"] == "https://example.com/b"
    assert loaded.candidates[0]["qmd_matches"][0]["file"] == "a.md"


def test_probable_duplicate_by_similarity_catches_mismatched_canonical_names(tmp_path):
    """Regression test for the MERGE candidate identity.resolve() missed in
    production: two benchmark_result pages from the same paper/hardware under
    different canonical_name strings. High BM25 score + shared source
    snapshot should flag it even though exact-key matching wouldn't.
    """
    pages_dir = tmp_path / "wiki" / "_pages" / "benchmark_result"
    pages_dir.mkdir(parents=True)
    existing = pages_dir / "compiler_benchmark_bananapi_f3_gcc15_clang21.md"
    existing.write_text(
        "---\ntype: benchmark_result\n"
        "canonical_name: Compiler Benchmark Comparison on BananaPi-F3 (RVV 1.0)\n"
        "sources: [raw/cache/deadbeef.md]\n---\n\n# Compiler Benchmark\n",
        encoding="utf-8",
    )
    draft = {
        "frontmatter": {"sources": ["raw/cache/deadbeef.md"]},
        "content": "# GCC 15 vs Clang 21 Autovectorization on BananaPi-F3 (RVV)\n",
    }
    qmd_matches = [{
        "rank": 1,
        "file": existing.name,
        "title": "Compiler Benchmark Comparison on BananaPi-F3 (RVV 1.0)",
        "score": 0.95,
    }]

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir.parent):
        result = orchestrator._probable_duplicate_by_similarity(
            "GCC 15 vs Clang 21 Autovectorization on BananaPi-F3 (RVV)",
            draft, qmd_matches, {"near_duplicate_score": 0.90},
        )

    assert result is not None
    assert result.filename == "compiler_benchmark_bananapi_f3_gcc15_clang21.md"


def test_probable_duplicate_by_similarity_ignores_low_score_or_no_shared_source(tmp_path):
    pages_dir = tmp_path / "wiki" / "_pages" / "entity"
    pages_dir.mkdir(parents=True)
    existing = pages_dir / "other_page.md"
    existing.write_text(
        "---\ntype: entity\ncanonical_name: Other Page\nsources: [raw/cache/other.md]\n---\n\n# Other\n",
        encoding="utf-8",
    )
    draft = {"frontmatter": {"sources": ["raw/cache/deadbeef.md"]}, "content": "# Draft\n"}

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir.parent):
        # High score but no shared source snapshot -> not flagged.
        assert orchestrator._probable_duplicate_by_similarity(
            "Some New Concept", draft,
            [{"rank": 1, "file": existing.name, "title": "Other Page", "score": 0.95}],
            {"near_duplicate_score": 0.90},
        ) is None
        # Shared source but score below near_duplicate_score -> not flagged.
        draft["frontmatter"]["sources"] = ["raw/cache/other.md"]
        assert orchestrator._probable_duplicate_by_similarity(
            "Some New Concept", draft,
            [{"rank": 1, "file": existing.name, "title": "Other Page", "score": 0.5}],
            {"near_duplicate_score": 0.90},
        ) is None


def test_rebuild_index_from_frontmatter_resyncs_stale_rows(tmp_path):
    """_update_index() only appends a row at page-creation time, embedding
    inbound_links as of then; it never revisits that row when a later page
    links to it. rebuild_index_from_frontmatter() must be the full-rebuild
    source of truth: every row's Sources/Inbound must match current
    frontmatter, and the header Sources/Pages counts must be recomputed too.
    """
    pages_dir = tmp_path / "wiki" / "_pages"
    entity_dir = pages_dir / "entity"
    entity_dir.mkdir(parents=True)
    (entity_dir / "alpha.md").write_text(
        "---\ntype: entity\ncanonical_name: Alpha\ntags: [x]\n"
        "sources: [raw/cache/a.md, raw/cache/b.md]\n"
        "inbound_links: 3\n---\n\n# Alpha\n\nAlpha body.\n",
        encoding="utf-8",
    )
    synthesis_dir = pages_dir / "synthesis"
    synthesis_dir.mkdir(parents=True)
    (synthesis_dir / "beta.md").write_text(
        "---\ntype: synthesis\nconnected_entities: [alpha]\nsynthesis_status: draft\n"
        "sources: []\ninbound_links: 0\n---\n\n# Beta\n",
        encoding="utf-8",
    )
    index = tmp_path / "wiki" / "index.md"
    index.write_text(
        "# Wiki Index\n\nLast updated: 2020-01-01 | Pages: 1 | Sources: 1\n\n"
        "## Entity Pages\n\n| Page | Summary | Tags | Sources | Inbound |\n"
        "|------|---------|------|---------|---------|\n"
        "| [alpha.md](entity/alpha.md) | Alpha | x | 2 | 0 |\n\n"
        "## Synthesis Pages\n\n| Page | Connected Entities | Status | Inbound |\n"
        "|------|--------------------|--------|---------|\n\n"
        "## Concept Index\n\n- **Stale Concept**: → [nowhere](entity/nowhere.md)\n\n"
        "## Optimization Pages\n\n| Page | Type | Summary | Tags | Sources | Inbound |\n"
        "|------|------|---------|------|---------|---------|\n",
        encoding="utf-8",
    )

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_INDEX_MD", index):
        orchestrator.rebuild_index_from_frontmatter()

    text = index.read_text(encoding="utf-8")
    assert "Pages: 2" in text
    assert "Sources: 2" in text
    assert "| [alpha.md](entity/alpha.md) | Alpha | x | 2 | 3 |" in text
    assert "| [beta.md](synthesis/beta.md) | alpha | draft | 0 |" in text
    # Concept Index is rebuilt from current frontmatter (canonical_name/aliases),
    # same full-rebuild-is-truth pattern as the tables above — stale hand-written
    # entries that no longer correspond to any page's canonical_name are dropped.
    assert "**Alpha**: → [alpha](entity/alpha.md)" in text
    assert "Stale Concept" not in text


def test_rebuild_index_populates_concept_gaps_from_dangling_outbound_links(tmp_path):
    """Regression: _get_concept_gaps() reads wiki/index.md's Concept Index
    section for "**Name**: ... no dedicated page" entries, but nothing ever
    wrote that pattern — rebuild_index_from_frontmatter() only rebuilt the
    Entity/Synthesis/Optimization tables, so _get_concept_gaps() had returned
    [] on every session since the autonomous research harness was first
    built (found live, via a real replication run's audit logs). A page's
    outbound_links target that doesn't resolve to any existing page stem is
    exactly a "mentioned but no dedicated page" concept — use it as the gap
    source instead of leaving the section permanently empty."""
    pages_dir = tmp_path / "wiki" / "_pages"
    entity_dir = pages_dir / "entity"
    entity_dir.mkdir(parents=True)
    (entity_dir / "gemmini.md").write_text(
        "---\ntype: entity\ncanonical_name: Gemmini\nsources: [raw/cache/a.md]\n"
        "inbound_links: 0\noutbound_links:\n"
        "- target: systolic_tensor_units\n  reason: related concept\n"
        "- target: some_unwritten_concept\n  reason: mentioned but no page yet\n"
        "---\n\n# Gemmini\n\nBody.\n",
        encoding="utf-8",
    )
    (entity_dir / "systolic_tensor_units.md").write_text(
        "---\ntype: entity\ncanonical_name: Systolic Tensor Units\nsources: [raw/cache/b.md]\n"
        "inbound_links: 1\n---\n\n# Systolic Tensor Units\n\nBody.\n",
        encoding="utf-8",
    )
    index = tmp_path / "wiki" / "index.md"
    index.write_text(
        "# Wiki Index\n\nLast updated: 2020-01-01 | Pages: 0 | Sources: 0\n\n"
        "## Entity Pages\n\n| Page | Summary | Tags | Sources | Inbound |\n"
        "|------|---------|------|---------|---------|\n\n"
        "## Synthesis Pages\n\n| Page | Connected Entities | Status | Inbound |\n"
        "|------|--------------------|--------|---------|\n\n"
        "## Concept Index\n\n\n"
        "## Optimization Pages\n\n| Page | Type | Summary | Tags | Sources | Inbound |\n"
        "|------|------|---------|------|---------|---------|\n",
        encoding="utf-8",
    )

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_INDEX_MD", index):
        orchestrator.rebuild_index_from_frontmatter()
        gaps = orchestrator._get_concept_gaps()

    text = index.read_text(encoding="utf-8")
    # systolic_tensor_units is resolved (has its own page) -> not a gap.
    assert "**Systolic Tensor Units**: → [systolic_tensor_units](entity/systolic_tensor_units.md)" in text
    assert "systolic_tensor_units" not in gaps
    # some_unwritten_concept has no page anywhere -> a real gap, and now
    # actually discoverable by _get_concept_gaps() for the first time.
    assert "**some_unwritten_concept**: mentioned in [gemmini](entity/gemmini.md) — *no dedicated page*" in text
    assert "some_unwritten_concept" in gaps


def test_rebuild_index_does_not_accumulate_blank_lines_across_repeated_calls(tmp_path):
    """Regression: _replace_section's trim-back loop decremented end_idx past
    trailing blanks but then used all_lines[end_idx:] as the tail, which still
    *started* at those same blank lines rather than past them -- every rebuild
    call added its own blank line on top of an untouched, never-actually-
    trimmed run, growing the gap between two sections by ~1-2 lines per call
    (confirmed live: 47+ accumulated blank lines in a long-running wiki's
    index.md between Concept Index and Optimization Pages). Calling rebuild
    repeatedly must be idempotent, not compounding."""
    pages_dir = tmp_path / "wiki" / "_pages"
    entity_dir = pages_dir / "entity"
    entity_dir.mkdir(parents=True)
    (entity_dir / "alpha.md").write_text(
        "---\ntype: entity\ncanonical_name: Alpha\nsources: []\ninbound_links: 0\n---\n\n# Alpha\n\nBody.\n",
        encoding="utf-8",
    )
    hw_dir = pages_dir / "hardware_target"
    hw_dir.mkdir(parents=True)
    (hw_dir / "beta.md").write_text(
        "---\ntype: hardware_target\ncanonical_name: Beta\nsources: []\ninbound_links: 0\n---\n\n# Beta\n\nBody.\n",
        encoding="utf-8",
    )
    index = tmp_path / "wiki" / "index.md"
    index.write_text(
        "# Wiki Index\n\nLast updated: 2020-01-01 | Pages: 0 | Sources: 0\n\n"
        "## Entity Pages\n\n| Page | Summary | Tags | Sources | Inbound |\n"
        "|------|---------|------|---------|---------|\n\n"
        "## Synthesis Pages\n\n| Page | Connected Entities | Status | Inbound |\n"
        "|------|--------------------|--------|---------|\n\n"
        "## Concept Index\n",
        encoding="utf-8",
    )

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_INDEX_MD", index):
        orchestrator.rebuild_index_from_frontmatter()
        first_pass = index.read_text(encoding="utf-8")
        for _ in range(3):
            orchestrator.rebuild_index_from_frontmatter()
        stable_pass = index.read_text(encoding="utf-8")

    assert first_pass == stable_pass
    assert "\n\n\n" not in stable_pass


def test_rebuild_index_renders_hub_hierarchy_from_theme_profile(tmp_path):
    """Phase 2: deliberate hub concepts, declared in [theme_profile].hub_hierarchy
    at theme setup, are a *derived* index view -- grouping existing pages by
    subtype under the hub's label -- not a forced synthesis page (which would
    violate its own "connected_entities non-empty" rejection criteria at cold
    start). A hub with zero matching pages yet still renders, honestly, as
    empty rather than being silently omitted."""
    pages_dir = tmp_path / "wiki" / "_pages"
    hw_dir = pages_dir / "hardware_target"
    hw_dir.mkdir(parents=True)
    (hw_dir / "chip-a.md").write_text(
        "---\ntype: hardware_target\ncanonical_name: Chip A\nsources: []\ninbound_links: 0\n---\n\n# Chip A\n\nBody.\n",
        encoding="utf-8",
    )
    (hw_dir / "chip-b.md").write_text(
        "---\ntype: hardware_target\ncanonical_name: Chip B\nsources: []\ninbound_links: 0\n---\n\n# Chip B\n\nBody.\n",
        encoding="utf-8",
    )
    index = tmp_path / "wiki" / "index.md"
    index.write_text(
        "# Wiki Index\n\nLast updated: 2020-01-01 | Pages: 0 | Sources: 0\n\n"
        "## Entity Pages\n\n| Page | Summary | Tags | Sources | Inbound |\n"
        "|------|---------|------|---------|---------|\n\n"
        "## Synthesis Pages\n\n| Page | Connected Entities | Status | Inbound |\n"
        "|------|--------------------|--------|---------|\n\n"
        "## Concept Index\n\n\n"
        "## Optimization Pages\n\n| Page | Type | Summary | Tags | Sources | Inbound |\n"
        "|------|------|---------|------|---------|---------|\n",
        encoding="utf-8",
    )
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text(
        "```yaml\n[theme_profile]\ntheme: RISC-V AI accelerator\nhub_hierarchy:\n"
        "- hub_id: vendor_core_families\n  label: Vendor RISC-V Core Families\n"
        "  subtype: hardware_target\n  description: Cores and SoCs by vendor.\n"
        "- hub_id: workload_landscape\n  label: Workload and Kernel Landscape\n"
        "  subtype: workload_kernel\n  description: Kernel shapes and baselines.\n```\n",
        encoding="utf-8",
    )

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_INDEX_MD", index), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md):
        orchestrator.rebuild_index_from_frontmatter()

    text = index.read_text(encoding="utf-8")
    assert "## Hub Hierarchy" in text
    assert "### Vendor RISC-V Core Families" in text
    assert "[chip-a](hardware_target/chip-a.md)" in text
    assert "[chip-b](hardware_target/chip-b.md)" in text


def test_rebuild_index_renders_two_parent_sub_hub_nested_under_both(tmp_path):
    """Part B: a sub-hub declaring two parent_hub_ids (a bridging subcategory)
    renders once under EACH parent's ### heading, as a #### sub-section --
    the visible expression of "introduce new subcategory under two parent
    categories when necessary". Membership is tag-based, not a new
    type/subtype value, so no page needs reclassifying."""
    pages_dir = tmp_path / "wiki" / "_pages"
    hw_dir = pages_dir / "hardware_target"
    hw_dir.mkdir(parents=True)
    (hw_dir / "chip-a.md").write_text(
        "---\ntype: hardware_target\ncanonical_name: Chip A\ntags: [quantized-gemm]\n"
        "sources: []\ninbound_links: 0\n---\n\n# Chip A\n\nBody.\n",
        encoding="utf-8",
    )
    index = tmp_path / "wiki" / "index.md"
    index.write_text(
        "# Wiki Index\n\nLast updated: 2020-01-01 | Pages: 0 | Sources: 0\n\n"
        "## Entity Pages\n\n| Page | Summary | Tags | Sources | Inbound |\n"
        "|------|---------|------|---------|---------|\n\n"
        "## Synthesis Pages\n\n| Page | Connected Entities | Status | Inbound |\n"
        "|------|--------------------|--------|---------|\n\n"
        "## Concept Index\n\n\n"
        "## Optimization Pages\n\n| Page | Type | Summary | Tags | Sources | Inbound |\n"
        "|------|------|---------|------|---------|---------|\n",
        encoding="utf-8",
    )
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text(
        "```yaml\n[theme_profile]\ntheme: RISC-V AI accelerator\nhub_hierarchy:\n"
        "- hub_id: vendor_core_families\n  label: Vendor RISC-V Core Families\n"
        "  subtype: hardware_target\n  description: Cores and SoCs by vendor.\n"
        "- hub_id: workload_landscape\n  label: Workload and Kernel Landscape\n"
        "  subtype: workload_kernel\n  description: Kernel shapes and baselines.\n"
        "- hub_id: quantized_gemm_cores\n  label: Quantized GEMM Cores\n"
        "  tag: quantized-gemm\n  parent_hub_ids: [vendor_core_families, workload_landscape]\n"
        "  description: Bridging sub-hub.\n```\n",
        encoding="utf-8",
    )

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_INDEX_MD", index), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md):
        orchestrator.rebuild_index_from_frontmatter()
        text_first_pass = index.read_text(encoding="utf-8")
        # Idempotency: guard against the earlier compounding blank-line bug --
        # a second rebuild on already-rebuilt content must not grow the file.
        orchestrator.rebuild_index_from_frontmatter()
        text_second_pass = index.read_text(encoding="utf-8")

    assert text_first_pass == text_second_pass
    assert text_first_pass.count("#### Quantized GEMM Cores") == 2
    assert "### Vendor RISC-V Core Families" in text_first_pass
    assert "### Workload and Kernel Landscape" in text_first_pass
    # appears nested under both parents, in each case listing the tagged page.
    # Sections start at a line beginning with exactly "### " (not "#### ").
    sections = re.split(r"\n(?=### [^#])", text_first_pass)
    for section in sections:
        if section.lstrip("#").lstrip().startswith(("Vendor RISC-V Core Families", "Workload and Kernel Landscape")):
            assert "#### Quantized GEMM Cores" in section
            assert "[chip-a](hardware_target/chip-a.md)" in section.split("#### Quantized GEMM Cores")[1]


def test_synthesis_gap_clusters_finds_uncovered_tag_and_excludes_covered(tmp_path):
    pages_dir = tmp_path / "wiki" / "_pages"
    entity_dir = pages_dir / "entity"
    entity_dir.mkdir(parents=True)
    for i in range(3):
        (entity_dir / f"page{i}.md").write_text(
            f"---\ntype: entity\ntags: [gemm]\n---\n\n# Page {i}\n", encoding="utf-8"
        )
    (entity_dir / "other.md").write_text(
        "---\ntype: entity\ntags: [unrelated]\n---\n\n# Other\n", encoding="utf-8"
    )
    synthesis_dir = pages_dir / "synthesis"
    synthesis_dir.mkdir(parents=True)
    (synthesis_dir / "existing.md").write_text(
        "---\ntype: synthesis\nconnected_entities: [page0]\n---\n\n# Existing\n", encoding="utf-8"
    )

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir):
        clusters = orchestrator._synthesis_gap_clusters(min_cluster_size=2)

    assert len(clusters) == 1
    tag, uncovered = clusters[0]
    assert tag == "gemm"
    # page0 is already covered by the existing synthesis page's connected_entities.
    assert sorted(uncovered) == ["page1", "page2"]


def test_synthesis_gap_clusters_includes_subtype_pages_not_just_literal_entity_type(tmp_path):
    """Regression test for a real bug found running the v2 replication test:
    subtype pages (hardware_target/benchmark_result/...) are written with the
    literal subtype name in `type` (e.g. type: hardware_target), not
    `type: entity, subtype: hardware_target` as the design doc describes —
    confirmed against real pages in both research/riscv-ai-accelerator and the
    replication run. The old `fm.get("type") == "entity"` filter silently
    excluded the majority of an optimization_first wiki's pages (subtype pages
    are also where tags are most consistently populated), so synthesis-gap
    detection almost never found a real cluster. Only `type: synthesis` pages
    should be excluded from clustering.
    """
    pages_dir = tmp_path / "wiki" / "_pages"
    hw_dir = pages_dir / "hardware_target"
    hw_dir.mkdir(parents=True)
    for name in ("chip_a", "chip_b", "chip_c"):
        (hw_dir / f"{name}.md").write_text(
            f"---\ntype: hardware_target\ntags: [RISC-V]\n---\n\n# {name}\n", encoding="utf-8"
        )
    entity_dir = pages_dir / "entity"
    entity_dir.mkdir(parents=True)
    (entity_dir / "unrelated.md").write_text(
        "---\ntype: entity\ntags: [software]\n---\n\n# Unrelated\n", encoding="utf-8"
    )

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir):
        clusters = orchestrator._synthesis_gap_clusters(min_cluster_size=3)

    assert len(clusters) == 1
    tag, uncovered = clusters[0]
    assert tag == "RISC-V"
    assert sorted(uncovered) == ["chip_a", "chip_b", "chip_c"]


def test_hub_member_pages_resolves_declared_subtype_membership(tmp_path):
    pages_dir = tmp_path / "wiki" / "_pages"
    hw_dir = pages_dir / "hardware_target"
    hw_dir.mkdir(parents=True)
    (hw_dir / "chip-a.md").write_text("---\ntype: hardware_target\n---\n\n# Chip A\n", encoding="utf-8")
    entity_dir = pages_dir / "entity"
    entity_dir.mkdir(parents=True)
    (entity_dir / "unrelated.md").write_text("---\ntype: entity\n---\n\n# Unrelated\n", encoding="utf-8")
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text(
        "```yaml\n[theme_profile]\nhub_hierarchy:\n"
        "- hub_id: vendor_core_families\n  subtype: hardware_target\n```\n",
        encoding="utf-8",
    )

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md):
        assert orchestrator._hub_member_pages() == {"chip-a"}


def test_hub_promotion_candidates_finds_cluster_within_declared_hub(tmp_path):
    """Phase 2c: a tag cluster within a declared hub's subtype, large enough
    to warrant its own sub-hub, is surfaced for human review -- never
    auto-applied (same principle as retrospective lint's MERGE/DELETE)."""
    pages_dir = tmp_path / "wiki" / "_pages"
    hw_dir = pages_dir / "hardware_target"
    hw_dir.mkdir(parents=True)
    for name in ("xuantie-c906", "xuantie-c908", "xuantie-c910"):
        (hw_dir / f"{name}.md").write_text(
            f"---\ntype: hardware_target\ntags: [xuantie, risc-v]\n---\n\n# {name}\n",
            encoding="utf-8",
        )
    (hw_dir / "sifive-x280.md").write_text(
        "---\ntype: hardware_target\ntags: [sifive, risc-v]\n---\n\n# SiFive X280\n",
        encoding="utf-8",
    )
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text(
        "```yaml\n[theme_profile]\nhub_hierarchy:\n"
        "- hub_id: vendor_core_families\n  label: Vendor RISC-V Core Families\n"
        "  subtype: hardware_target\n```\n"
        "```yaml\n[research_config]\nsynthesis_gap_min_cluster_size: 3\n```\n",
        encoding="utf-8",
    )

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md):
        candidates = orchestrator._hub_promotion_candidates()

    xuantie_candidates = [c for c in candidates if c["tag"] == "xuantie"]
    assert len(xuantie_candidates) == 1
    c = xuantie_candidates[0]
    assert c["parent_hub_id"] == "vendor_core_families"
    assert sorted(c["member_pages"]) == ["xuantie-c906", "xuantie-c908", "xuantie-c910"]
    # "risc-v" is shared by all 4 pages, including sifive-x280 -- also a
    # valid, separate cluster candidate under the same hub.
    assert any(c["tag"] == "risc-v" and len(c["member_pages"]) == 4 for c in candidates)
    # "sifive" alone only has 1 page -- below threshold, not proposed.
    assert not any(c["tag"] == "sifive" for c in candidates)


def test_hub_promotion_candidates_detects_cross_hub_cluster(tmp_path):
    """Part D detection: a tag whose tagged pages split across exactly two
    declared hubs' subtypes (not one) is surfaced as a bridging candidate
    with parent_hub_ids carrying both hub_ids -- the "two parent categories"
    case, not an accident."""
    pages_dir = tmp_path / "wiki" / "_pages"
    hw_dir = pages_dir / "hardware_target"
    wl_dir = pages_dir / "workload_kernel"
    hw_dir.mkdir(parents=True)
    wl_dir.mkdir(parents=True)
    for name, folder in [("chip-a", hw_dir), ("chip-b", hw_dir), ("kernel-a", wl_dir)]:
        page_type = "hardware_target" if folder is hw_dir else "workload_kernel"
        folder_path = folder / f"{name}.md"
        folder_path.write_text(
            f"---\ntype: {page_type}\ntags: [quantized-gemm]\n---\n\n# {name}\n",
            encoding="utf-8",
        )
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text(
        "```yaml\n[theme_profile]\nhub_hierarchy:\n"
        "- hub_id: vendor_core_families\n  label: Vendor RISC-V Core Families\n"
        "  subtype: hardware_target\n"
        "- hub_id: workload_landscape\n  label: Workload and Kernel Landscape\n"
        "  subtype: workload_kernel\n```\n"
        "```yaml\n[research_config]\nsynthesis_gap_min_cluster_size: 3\n```\n",
        encoding="utf-8",
    )

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md):
        candidates = orchestrator._hub_promotion_candidates()

    cross_hub = [c for c in candidates if c["tag"] == "quantized-gemm"]
    assert len(cross_hub) == 1
    c = cross_hub[0]
    assert sorted(c["parent_hub_ids"]) == ["vendor_core_families", "workload_landscape"]
    assert sorted(c["member_pages"]) == ["chip-a", "chip-b", "kernel-a"]


def test_run_taxonomy_evolution_persists_only_when_both_signals_agree(tmp_path):
    """Part D gate: persistence requires BOTH the objective (elevated
    centrality) and subjective (subagent approval) signals. Objective-only
    (patched False) must not persist even with a subagent that would approve."""
    pages_dir = tmp_path / "wiki" / "_pages"
    hw_dir = pages_dir / "hardware_target"
    hw_dir.mkdir(parents=True)
    for name in ("chip-a", "chip-b", "chip-c"):
        (hw_dir / f"{name}.md").write_text(
            f"---\ntype: hardware_target\ntags: [quantized-gemm]\ncanonical_name: {name}\n"
            f"sources: []\n---\n\n# {name}\n\nBody text.\n",
            encoding="utf-8",
        )
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text(
        "```yaml\n[theme_profile]\ntheme: t\norganization_choice: workflow_first\n"
        "organization_name: Workflow-first\nhub_hierarchy:\n"
        "- hub_id: vendor_core_families\n  label: Vendor RISC-V Core Families\n"
        "  subtype: hardware_target\n  description: d\n```\n"
        "```yaml\n[research_config]\nsynthesis_gap_min_cluster_size: 3\n"
        "max_new_subtypes_per_session: 2\n```\n",
        encoding="utf-8",
    )
    research_config = {
        # Built directly rather than via orchestrator._load_claude_md_block(),
        # which reads the *default* _CLAUDE_MD path -- not yet patched to
        # this fixture at this point in the test. Found live: in the original
        # dev repo that default path happened to have a real theme_profile
        # with a matching vendor_core_families hub, so this line silently
        # read production CLAUDE.md instead of the fixture and the test
        # passed for the wrong reason; in a clean checkout (no theme_profile
        # on disk) it returns {} and the test fails for real.
        "theme_profile": {
            "theme": "t",
            "organization_choice": "workflow_first",
            "organization_name": "Workflow-first",
            "hub_hierarchy": [{
                "hub_id": "vendor_core_families",
                "label": "Vendor RISC-V Core Families",
                "subtype": "hardware_target",
                "description": "d",
            }],
        },
        "page_type_taxonomy": {"hardware_target": {}},
        "synthesis_gap_min_cluster_size": 3,
        "max_new_subtypes_per_session": 2,
    }

    approving_subagent = MagicMock(return_value=json.dumps({
        "decision": "approve",
        "rejection_reason": None,
        "subtype_name": "quantized_gemm_cores",
        "label": "Quantized GEMM Cores",
        "description": "d",
        "structured_fields": [],
        "parent_hub_ids": ["vendor_core_families"],
    }))

    log_md = tmp_path / "wiki" / "log.md"
    log_md.write_text("", encoding="utf-8")

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md), \
         patch.object(orchestrator, "_LOG_MD", log_md), \
         patch.object(orchestrator.graph_topology, "cluster_is_structurally_distinct", return_value=False):
        persisted = orchestrator._run_taxonomy_evolution(research_config, call_subagent=approving_subagent)

    assert persisted == []
    assert "quantized_gemm_cores" not in claude_md.read_text(encoding="utf-8")

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md), \
         patch.object(orchestrator, "_LOG_MD", log_md), \
         patch.object(orchestrator.graph_topology, "cluster_is_structurally_distinct", return_value=True):
        persisted = orchestrator._run_taxonomy_evolution(research_config, call_subagent=approving_subagent)

    assert persisted == ["quantized_gemm_cores"]
    text = claude_md.read_text(encoding="utf-8")
    assert "quantized_gemm_cores" in text
    assert "taxonomy_evolution" not in text  # log goes to wiki/log.md, not CLAUDE.md
    # Regression guard: persistence must not blank sibling [theme_profile]
    # fields it isn't touching -- found live when _persist_new_subtype
    # incorrectly routed an already-on-disk profile back through
    # _serializable_theme_profile(), which expects the pre-serialization
    # (id/name) shape and blanks organization_choice/organization_name for
    # an on-disk (organization_choice/organization_name already-keyed) profile.
    assert "organization_choice: workflow_first" in text
    assert "organization_name: Workflow-first" in text


def test_run_taxonomy_evolution_respects_rate_limit(tmp_path):
    """Part D guardrail: persistence stops once max_new_subtypes_per_session
    is reached, even if more candidates would otherwise qualify."""
    pages_dir = tmp_path / "wiki" / "_pages"
    hw_dir = pages_dir / "hardware_target"
    hw_dir.mkdir(parents=True)
    for tag in ("tag-one", "tag-two"):
        for i in range(3):
            (hw_dir / f"{tag}-{i}.md").write_text(
                f"---\ntype: hardware_target\ntags: [{tag}]\ncanonical_name: {tag}-{i}\n"
                f"sources: []\n---\n\n# {tag}-{i}\n\nBody text.\n",
                encoding="utf-8",
            )
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text(
        "```yaml\n[theme_profile]\ntheme: t\nhub_hierarchy:\n"
        "- hub_id: vendor_core_families\n  label: Vendor RISC-V Core Families\n"
        "  subtype: hardware_target\n  description: d\n```\n",
        encoding="utf-8",
    )
    research_config = {
        # See the sibling dual-signal-gate test above for why this is built
        # directly rather than loaded via orchestrator._load_claude_md_block().
        "theme_profile": {
            "theme": "t",
            "hub_hierarchy": [{
                "hub_id": "vendor_core_families",
                "label": "Vendor RISC-V Core Families",
                "subtype": "hardware_target",
                "description": "d",
            }],
        },
        "page_type_taxonomy": {"hardware_target": {}},
        "synthesis_gap_min_cluster_size": 3,
        "max_new_subtypes_per_session": 1,
    }

    calls = {"n": 0}

    def approving_subagent(subagent_type, manifest, cfg):
        calls["n"] += 1
        return json.dumps({
            "decision": "approve",
            "rejection_reason": None,
            "subtype_name": f"subtype_{calls['n']}",
            "label": "L",
            "description": "d",
            "structured_fields": [],
            "parent_hub_ids": ["vendor_core_families"],
        })

    log_md = tmp_path / "wiki" / "log.md"
    log_md.write_text("", encoding="utf-8")

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md), \
         patch.object(orchestrator, "_LOG_MD", log_md), \
         patch.object(orchestrator.graph_topology, "cluster_is_structurally_distinct", return_value=True):
        persisted = orchestrator._run_taxonomy_evolution(research_config, call_subagent=approving_subagent)

    assert len(persisted) == 1


def test_hub_promotion_candidates_empty_when_no_hub_hierarchy_declared(tmp_path):
    pages_dir = tmp_path / "wiki" / "_pages"
    pages_dir.mkdir(parents=True)
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text("```yaml\n[theme_profile]\ntheme: x\n```\n", encoding="utf-8")

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md):
        assert orchestrator._hub_promotion_candidates() == []


def test_generate_synthesis_candidate_writes_page_and_respects_budget(tmp_path):
    """Regression coverage for Phase 3: the research loop previously only
    logged synthesis gaps (_check_synthesis_gaps) without ever acting on them.
    This exercises the full call -> validate -> pipeline -> write path.
    """
    pages_dir = tmp_path / "wiki" / "_pages"
    entity_dir = pages_dir / "entity"
    entity_dir.mkdir(parents=True)
    for name, tag in [("alpha", "gemm"), ("beta", "gemm"), ("gamma", "gemm")]:
        (entity_dir / f"{name}.md").write_text(
            f"---\ntype: entity\ntags: [{tag}]\ncanonical_name: {name.title()}\n---\n\n"
            f"# {name.title()}\n\nA GEMM optimization approach.\n\n"
            f"## Key Claims\n\n- {name.title()} claims something specific.\n",
            encoding="utf-8",
        )
    index = tmp_path / "wiki" / "index.md"
    index.write_text(
        "# Wiki Index\n\nLast updated: 2020-01-01 | Pages: 3 | Sources: 0\n\n"
        "## Entity Pages\n\n| Page | Summary | Tags | Sources | Inbound |\n"
        "|------|---------|------|---------|---------|\n\n"
        "## Synthesis Pages\n\n| Page | Connected Entities | Status | Inbound |\n"
        "|------|--------------------|--------|---------|\n",
        encoding="utf-8",
    )
    state = ResearchSessionState.create(
        "sess-synth", "gemm query", {"max_candidates": 5, "max_new_pages": 5, "depth": "shallow"},
        tmp_path / "state",
    )
    quota = QuotaManager(max_candidates=5, max_new_pages=5)
    audit = FullDummyAudit()

    synthesis_result = json.dumps({
        "decision": "approve",
        "rejection_reason": None,
        "page_draft": {
            "page_type": "synthesis",
            "filename": "gemm_approaches",
            "frontmatter": {
                "type": "synthesis",
                "connected_entities": ["alpha", "beta", "gamma"],
                "synthesis_status": "draft",
                "tags": ["gemm"],
            },
            "content": "# GEMM Approaches\n\n## RAG Summary\n\n" + ("word " * 180) + "\n\n"
            "## Full Synthesis\n\n[[alpha]] and [[beta]] and [[gamma]] compared.\n\n"
            "## Open Questions\n\n- What about a fourth approach?\n\n"
            "## Connected Pages\n\n- [[alpha]]\n- [[beta]]\n- [[gamma]]\n",
        },
    })

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_INDEX_MD", index), \
         patch.object(orchestrator, "_call_subagent", return_value=synthesis_result), \
         patch.object(orchestrator, "_run_eval_pipeline", return_value=(True, {
             "layer1_pass": True, "layer2_pass": True, "layer3_triggered": False,
             "final_decision": "approved",
         })):
        filename = orchestrator._generate_synthesis_candidate(
            state, quota, audit, {"synthesis_gap_min_cluster_size": 3}, set()
        )

    assert filename == "gemm_approaches.md"
    written = pages_dir / "synthesis" / "gemm_approaches.md"
    assert written.exists()
    assert quota._pages_written == 1
    # Budget respected: a second call with pages_exceeded should no-op.
    quota.max_new_pages = 1
    assert orchestrator._generate_synthesis_candidate(
        state, quota, audit, {"synthesis_gap_min_cluster_size": 3}, set()
    ) is None


def test_generate_synthesis_candidate_backfills_sources_for_real_eval_pipeline(tmp_path):
    """Regression test for a live bug found running the v2 replication test:
    the subagent's page_draft has no frontmatter.sources (a synthesis page
    draws from existing wiki content, not a freshly fetched external source),
    but eval_summary.py's Layer 1 EMPTY_SOURCES check applies unconditionally
    to every page type. Without backfilling sources from the cluster pages'
    own paths, every synthesis draft failed Layer 1 and
    _generate_synthesis_candidate() could never actually write a page — this
    test does NOT mock _run_eval_pipeline, so it exercises the real
    eval_summary.py subprocess the way the earlier
    test_generate_synthesis_candidate_writes_page_and_respects_budget test
    (which does mock it) could not have caught this.
    """
    pages_dir = tmp_path / "wiki" / "_pages"
    entity_dir = pages_dir / "entity"
    entity_dir.mkdir(parents=True)
    for name, tag in [("alpha", "gemm"), ("beta", "gemm"), ("gamma", "gemm")]:
        (entity_dir / f"{name}.md").write_text(
            f"---\ntype: entity\ntags: [{tag}]\ncanonical_name: {name.title()}\nsources: [https://example.com/{name}]\n---\n\n"
            f"# {name.title()}\n\nA GEMM optimization approach with real grounded content here.\n\n"
            f"## Key Claims\n\n- {name.title()} claims something specific.\n",
            encoding="utf-8",
        )
    index = tmp_path / "wiki" / "index.md"
    index.write_text(
        "# Wiki Index\n\nLast updated: 2020-01-01 | Pages: 3 | Sources: 0\n\n"
        "## Entity Pages\n\n| Page | Summary | Tags | Sources | Inbound |\n"
        "|------|---------|------|---------|---------|\n\n"
        "## Synthesis Pages\n\n| Page | Connected Entities | Status | Inbound |\n"
        "|------|--------------------|--------|---------|\n",
        encoding="utf-8",
    )
    state = ResearchSessionState.create(
        "sess-synth-sources", "gemm query", {"max_candidates": 5, "max_new_pages": 5, "depth": "shallow"},
        tmp_path / "state",
    )
    quota = QuotaManager(max_candidates=5, max_new_pages=5)
    audit = FullDummyAudit()

    rag_summary = (
        "GEMM optimization on RISC-V spans compiler-driven and hand-tuned approaches. " * 16
        + "The Alpha and Beta approaches illustrate this tradeoff directly."
    )
    synthesis_result = json.dumps({
        "decision": "approve",
        "rejection_reason": None,
        "page_draft": {
            "page_type": "synthesis",
            "filename": "gemm_approaches_no_sources",
            "frontmatter": {
                "type": "synthesis",
                "connected_entities": ["alpha", "beta", "gamma"],
                "synthesis_status": "draft",
                "tags": ["gemm"],
                # Deliberately no "sources" field, matching real subagent output.
            },
            "content": f"# GEMM Approaches\n\n## RAG Summary\n\n{rag_summary}\n\n"
            "## Full Synthesis\n\n[[alpha]] and [[beta]] and [[gamma]] compared.\n\n"
            "## Open Questions\n\n- What about a fourth approach?\n\n"
            "## Connected Pages\n\n- [[alpha]]\n- [[beta]]\n- [[gamma]]\n",
        },
    })

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_INDEX_MD", index), \
         patch.object(orchestrator, "_call_subagent", return_value=synthesis_result):
        filename = orchestrator._generate_synthesis_candidate(
            state, quota, audit, {"synthesis_gap_min_cluster_size": 3}, set()
        )

    assert filename == "gemm_approaches_no_sources.md"
    written = pages_dir / "synthesis" / "gemm_approaches_no_sources.md"
    assert written.exists()
    fm, _ = frontmatter.parse_page(written)
    assert fm.get("sources")  # backfilled, not empty


def test_refresh_connectivity_stats_only_touches_patched_claude_md(tmp_path):
    """Regression test: _refresh_connectivity_stats() is called from inside
    _run_research_state() and writes connectivity stats to _CLAUDE_MD. Two
    other tests in this file call _run_research_state() directly and only
    patched _WIKI_PAGES_DIR, not _CLAUDE_MD — so it silently recomputed stats
    from a throwaway tmp_path page set and wrote them into the real project
    CLAUDE.md on every test run. Assert the function only ever touches the
    paths it's given. (There is no graph_maturity flag/transition to log
    anymore — see graph_stats.py module docstring for why it was removed.)
    """
    pages_dir = tmp_path / "wiki" / "_pages" / "entity"
    pages_dir.mkdir(parents=True)
    (pages_dir / "a.md").write_text(
        "---\ntype: entity\ninbound_links: 1\n---\n\n# A\n", encoding="utf-8"
    )
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text(
        "```yaml\n[system_state]\norphan_fraction: 1.0\n```\n", encoding="utf-8"
    )

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md):
        orchestrator._refresh_connectivity_stats()

    text = claude_md.read_text(encoding="utf-8")
    assert "orphan_fraction: 0.0" in text or "orphan_fraction: 0" in text
    # Additive small-world topology fields (Phase 3b) are also refreshed — a
    # single-page, edgeless fixture has no outbound_links, so
    # clustering_coefficient is 0 and avg_path_length stays null (undefined
    # for a single isolated node).
    assert "clustering_coefficient: 0.0" in text
    assert "avg_path_length" in text


def test_refresh_connectivity_stats_survives_graph_topology_failure(tmp_path, monkeypatch):
    """graph_topology stats are informational-only: a failure there must not
    block writing the orphan_fraction/median_total_links connectivity stats."""
    pages_dir = tmp_path / "wiki" / "_pages" / "entity"
    pages_dir.mkdir(parents=True)
    (pages_dir / "a.md").write_text(
        "---\ntype: entity\ninbound_links: 1\n---\n\n# A\n", encoding="utf-8"
    )
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text("```yaml\n[system_state]\norphan_fraction: 1.0\n```\n", encoding="utf-8")

    def boom(*args, **kwargs):
        raise RuntimeError("networkx blew up")

    monkeypatch.setattr(orchestrator.graph_topology, "compute_topology_stats", boom)

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md):
        orchestrator._refresh_connectivity_stats()  # must not raise

    assert "orphan_fraction: 0.0" in claude_md.read_text(encoding="utf-8")


def test_approved_resume_writes_once_and_written_resume_skips(tmp_path):
    pages_dir = tmp_path / "wiki" / "_pages"
    log_path = tmp_path / "wiki" / "log.md"
    log_path.parent.mkdir(parents=True)
    log_path.write_text("", encoding="utf-8")
    state = ResearchSessionState.create(
        "sess2",
        "query",
        {"max_candidates": 2, "max_new_pages": 2, "depth": "shallow"},
        tmp_path / "state",
    )
    draft = {
        "page_type": "entity",
        "filename": "gemmini_resume",
        "frontmatter": {"tags": ["test"], "sources": []},
        "content": "# Gemmini Resume\n\n" + ("word " * 120),
    }
    state.candidates = [{
        "id": "cand1",
        "candidate": {"url": "https://example.com/gemmini", "title": "Gemmini"},
        "state": "approved",
        "drafts": [draft],
        "written_files": [],
        "audit_invocation_idx": 0,
    }]
    state.save("fixture")

    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text(
        "```yaml\n[system_state]\ngraph_maturity: false\n```\n", encoding="utf-8"
    )

    with patch.object(orchestrator, "_load_research_config", return_value={
             "qmd_command": ["uv", "run", "--no-sync", "qmd"],
             "research_state_dir": str(tmp_path / "state"),
         }), \
         patch.object(orchestrator, "QmdRunner", return_value=FakeQmdRunner()), \
         patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_INDEX_MD", tmp_path / "missing_index.md"), \
         patch.object(orchestrator, "_LOG_MD", log_path), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md), \
         patch.object(orchestrator, "AuditLog", return_value=DummyAudit()), \
         patch.object(orchestrator, "_run_graph_stats"), \
         patch.object(orchestrator, "_check_synthesis_gaps", return_value=[]):
        first = orchestrator._run_research_state(state)
        page = pages_dir / "entity" / "gemmini_resume.md"
        first_text = page.read_text(encoding="utf-8")
        second = orchestrator._run_research_state(ResearchSessionState.load("sess2", tmp_path / "state"))
        second_text = page.read_text(encoding="utf-8")

    assert first["status"] == "complete"
    assert second["status"] == "complete"
    assert first_text == second_text
    assert ResearchSessionState.load("sess2", tmp_path / "state").candidates[0]["state"] == "written"


def test_eval_result_with_null_pages_to_update_does_not_crash(tmp_path):
    """Regression test for a live crash hit during a real v2-replication run
    (session c7fdcf11, candidate github.com/XUANTIE-RV/riscv-matrix-extension-spec):
    the eval subagent returned valid JSON with "pages_to_update": null instead
    of []. validate_output._validate_eval_result() only ever iterates
    page_drafts, never pages_to_update, so a null pages_to_update sails through
    schema validation untouched — and orchestrator.py's
    `eval_result.get("pages_to_update", [])` doesn't protect against an
    explicit null (the default only applies when the key is *missing*), so
    `for update in None` raised TypeError and killed the whole research
    session, not just that one candidate.
    """
    pages_dir = tmp_path / "wiki" / "_pages"
    pages_dir.mkdir(parents=True)
    index = tmp_path / "wiki" / "index.md"
    index.write_text(
        "# Wiki Index\n\nLast updated: 2020-01-01 | Pages: 0 | Sources: 0\n\n"
        "## Entity Pages\n\n| Page | Summary | Tags | Sources | Inbound |\n"
        "|------|---------|------|---------|---------|\n\n"
        "## Synthesis Pages\n\n| Page | Connected Entities | Status | Inbound |\n"
        "|------|--------------------|--------|---------|\n",
        encoding="utf-8",
    )
    log_path = tmp_path / "wiki" / "log.md"
    log_path.write_text("", encoding="utf-8")
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text("```yaml\n[system_state]\ngraph_maturity: true\n```\n", encoding="utf-8")
    state = ResearchSessionState.create(
        "sess-null-updates", "RVME RISC-V matrix engine extension design",
        {"max_candidates": 1, "max_new_pages": 3, "depth": "shallow"},
        tmp_path / "state",
    )
    state.set_candidates([
        {"url": "https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/", "title": "RISC-V Matrix Extension Spec"},
    ])
    scorecard = {
        "novelty_delta": 0.8, "claim_density": 0.8, "self_containedness": 0.9,
        "bridge_score": 0.5, "hub_potential": 0.5, "gap_fill_score": 0.8,
        "contradiction_potential": 0.0, "weighted_total": 0.75,
    }
    malformed_but_schema_valid_eval = json.dumps({
        "decision": "approve",
        "rejection_reason": None,
        "scorecard": scorecard,
        "page_drafts": [{
            "page_type": "entity",
            "filename": "riscv_matrix_extension_spec",
            "frontmatter": {"type": "entity", "sources": ["https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/"]},
            "content": "# RISC-V Matrix Extension Spec\n\n" + ("word " * 120)
            + "\n\n## Key Claims\n\n- Claim one.\n- Claim two.\n- Claim three.\n",
        }],
        "pages_to_update": None,  # <- the actual malformed field from the live crash
        "contradictions_found": [],
    })

    with patch.object(orchestrator, "_load_research_config", return_value={
             "qmd_command": ["uv", "run", "--no-sync", "qmd"],
             "research_state_dir": str(tmp_path / "state"),
         }), \
         patch.object(orchestrator, "QmdRunner", return_value=EmptyQmdRunner()), \
         patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_INDEX_MD", index), \
         patch.object(orchestrator, "_LOG_MD", log_path), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md), \
         patch.object(orchestrator, "AuditLog", return_value=FullDummyAudit()), \
         patch.object(orchestrator, "_check_synthesis_gaps", return_value=[]), \
         patch.object(orchestrator, "_get_concept_gaps", return_value=[]), \
         patch.object(orchestrator, "_fetch_smart", return_value="RISC-V Matrix Extension spec content."), \
         patch.object(orchestrator, "_run_eval_pipeline", return_value=(True, {
             "layer1_pass": True, "layer2_pass": True, "layer3_triggered": False,
             "final_decision": "approved",
         })), \
         patch.object(orchestrator, "_call_subagent", return_value=malformed_but_schema_valid_eval):
        result = orchestrator._run_research_state(state)  # must not raise

    assert result["status"] == "complete"
    assert (pages_dir / "entity" / "riscv_matrix_extension_spec.md").exists()


def test_mocked_research_run_writes_benchmark_and_updates_hardware_page(tmp_path):
    pages_dir = tmp_path / "wiki" / "_pages"
    hardware_dir = pages_dir / "hardware_target"
    hardware_dir.mkdir(parents=True)
    (hardware_dir / "projectnimbus_x9.md").write_text(
        "---\n"
        "type: hardware_target\n"
        "sources: [https://example.com/spec]\n"
        "hardware_targets: [ProjectNimbus X9]\n"
        "toolchains: [LLVM]\n"
        "inbound_links: 0\n"
        "---\n\n# ProjectNimbus X9\n\nExisting hardware target page.\n",
        encoding="utf-8",
    )
    index = tmp_path / "wiki" / "index.md"
    index.write_text(
        "# Wiki Index\n\nLast updated: 2026-01-01 | Pages: 1 | Sources: 1\n\n"
        "## Entity Pages\n\n| Page | Summary | Tags | Sources | Inbound |\n"
        "|------|---------|------|---------|---------|\n\n"
        "## Synthesis Pages\n\n| Page | Connected Entities | Status | Inbound |\n"
        "|------|--------------------|--------|---------|\n",
        encoding="utf-8",
    )
    log_path = tmp_path / "wiki" / "log.md"
    log_path.write_text("", encoding="utf-8")
    state = ResearchSessionState.create(
        "sess3",
        "ProjectNimbus GEMM benchmark",
        {"max_candidates": 2, "max_new_pages": 3, "depth": "shallow"},
        tmp_path / "state",
    )
    state.set_candidates([
        {"url": "https://example.com/bench", "title": "ProjectNimbus X9 GEMM benchmark"},
        {"url": "https://example.com/update", "title": "ProjectNimbus SDK note"},
    ])

    scorecard = {
        "novelty_delta": 0.8,
        "claim_density": 0.8,
        "self_containedness": 0.9,
        "bridge_score": 0.5,
        "hub_potential": 0.5,
        "gap_fill_score": 0.8,
        "contradiction_potential": 0.0,
        "weighted_total": 0.75,
    }
    benchmark_eval = json.dumps({
        "decision": "approve",
        "rejection_reason": None,
        "scorecard": scorecard,
        "page_drafts": [{
            "page_type": "benchmark_result",
            "filename": "projectnimbus_x9_gemm_benchmark",
            "frontmatter": {
                "type": "benchmark_result",
                "sources": ["https://example.com/bench"],
                "hardware_targets": ["ProjectNimbus X9"],
                "workloads": ["GEMM 1024x1024"],
                "metrics": ["throughput"],
                "measurement_method": "reported SDK benchmark run",
                "evidence_strength": "reported",
            },
            "content": "# ProjectNimbus X9 GEMM Benchmark\n\n" + ("Measured benchmark context word " * 90)
            + "\n\n## Key Claims\n\n- Claim one reports 42 TOPS.\n- Claim two names GEMM 1024x1024.\n- Claim three names SDK 2.1.\n",
        }],
        "pages_to_update": [],
        "contradictions_found": [],
    })
    update_eval = json.dumps({
        "decision": "approve",
        "rejection_reason": None,
        "scorecard": scorecard,
        "page_drafts": [],
        "pages_to_update": [{
            "filename": "projectnimbus_x9",
            "section": "Benchmark Evidence",
            "update_description": "Add reported GEMM throughput context from the SDK benchmark note.",
        }],
        "contradictions_found": [],
    })
    audit = FullDummyAudit()

    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text(
        "```yaml\n[system_state]\ngraph_maturity: true\n```\n", encoding="utf-8"
    )

    with patch.object(orchestrator, "_load_research_config", return_value={
             "qmd_command": ["uv", "run", "--no-sync", "qmd"],
             "research_state_dir": str(tmp_path / "state"),
             "required_measurement_fields": [
                 "hardware_targets", "workloads", "metrics", "measurement_context"
             ],
             "page_type_taxonomy": {
                 "entity": {"description": "general concept"},
                 "synthesis": {"description": "cross-page comparison"},
                 "hardware_target": {"description": "hardware/ISA target"},
                 "benchmark_result": {"description": "measured or reported result"},
             },
         }), \
         patch.object(orchestrator, "QmdRunner", return_value=EmptyQmdRunner()), \
         patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_INDEX_MD", index), \
         patch.object(orchestrator, "_LOG_MD", log_path), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md), \
         patch.object(orchestrator, "AuditLog", return_value=audit), \
         patch.object(orchestrator, "_run_graph_stats"), \
         patch.object(orchestrator, "_check_synthesis_gaps", return_value=[]), \
         patch.object(orchestrator, "_get_concept_gaps", return_value=[]), \
         patch.object(orchestrator, "_fetch_smart", return_value="ProjectNimbus X9 reports 42 TOPS on GEMM with LLVM 18.1 throughput."), \
         patch.object(orchestrator, "_run_eval_pipeline", return_value=(True, {
             "layer1_pass": True,
             "layer2_pass": True,
             "layer3_triggered": False,
             "final_decision": "approved",
         })), \
         patch.object(orchestrator, "_call_subagent", side_effect=[benchmark_eval, update_eval]):
        result = orchestrator._run_research_state(state)

    benchmark_page = pages_dir / "benchmark_result" / "projectnimbus_x9_gemm_benchmark.md"
    hardware_text = (hardware_dir / "projectnimbus_x9.md").read_text(encoding="utf-8")
    patch_queue_text = (tmp_path / "wiki" / "patch_queue.md").read_text(encoding="utf-8")

    assert result["status"] == "complete"
    assert benchmark_page.exists()
    assert "## Benchmark Evidence" not in hardware_text
    assert "target_page: projectnimbus_x9.md" in patch_queue_text
    assert "reported GEMM throughput context" in patch_queue_text
    assert "evidence_extraction" in audit.invocations[0]["manifest"]
    assert audit.invocations[0]["manifest"]["wiki_context"]["gap_manifest"]["page_count"] >= 1


def test_write_page_populates_outbound_links_from_relationships_section(tmp_path):
    pages_dir = tmp_path / "_pages"
    pages_dir.mkdir()
    draft = {
        "page_type": "entity",
        "filename": "gemmini.md",
        "frontmatter": {"canonical_name": "Gemmini"},
        "content": (
            "\n# Gemmini\n\nA systolic-array accelerator.\n\n"
            "## Key Claims\n\n- claim one\n\n"
            "## Relationships\n\n"
            "- [[k230]]: alternative edge AI accelerator target.\n\n"
            "## Sources\n\ncite\n"
        ),
    }
    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir):
        page_path = orchestrator._write_page(draft)

    fm = frontmatter.parse_frontmatter(page_path)
    assert fm["outbound_links"] == [
        {"target": "k230", "reason": "alternative edge AI accelerator target"}
    ]


def test_write_page_omits_outbound_links_when_no_relationships_section(tmp_path):
    pages_dir = tmp_path / "_pages"
    pages_dir.mkdir()
    draft = {
        "page_type": "entity",
        "filename": "plain.md",
        "frontmatter": {"canonical_name": "Plain"},
        "content": "\n# Plain\n\nNo relationships section here.\n",
    }
    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir):
        page_path = orchestrator._write_page(draft)

    fm = frontmatter.parse_frontmatter(page_path)
    assert "outbound_links" not in fm


def test_bridge_candidates_for_manifest_reports_distant_topics(tmp_path):
    pages_dir = tmp_path / "_pages" / "entity"
    pages_dir.mkdir(parents=True)
    frontmatter.write_page(
        pages_dir / "a.md",
        {"type": "entity", "canonical_name": "Topic A", "outbound_links": [{"target": "b", "reason": "r"}]},
        "\n# a\n",
    )
    frontmatter.write_page(pages_dir / "b.md", {"type": "entity", "canonical_name": "Topic B"}, "\n# b\n")
    frontmatter.write_page(pages_dir / "x.md", {"type": "entity", "canonical_name": "Topic X"}, "\n# x\n")

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir.parent):
        candidates = orchestrator._bridge_candidates_for_manifest()

    assert len(candidates) == 1
    assert {candidates[0]["topic_a"], candidates[0]["topic_b"]} <= {"Topic A", "Topic B", "Topic X"}
    assert "separate connected components" in candidates[0]["reason"]


def test_bridge_candidates_for_manifest_swallows_errors(tmp_path):
    def boom(*args, **kwargs):
        raise RuntimeError("networkx blew up")

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", tmp_path), \
         patch.object(orchestrator.graph_topology, "find_bridge_candidates", side_effect=boom):
        assert orchestrator._bridge_candidates_for_manifest() == []


_LONG_FIRST_PARAGRAPH = (
    "This is a self-contained entity page describing a fictional RISC-V test "
    "component used only to exercise the patch-application pipeline in a unit "
    "test. It has a first paragraph that is deliberately long enough to satisfy "
    "the entity_first_paragraph word-count bounds enforced by eval_summary.py's "
    "deterministic pipeline gate, since that gate runs as a real subprocess "
    "against this fixture just like it would against any real drafted or "
    "merged page. The paragraph names the component, states what it is for, "
    "and includes some concrete numbers such as 4 cores and 2 GHz just in case "
    "density checks also apply here, without referencing any other page for "
    "its own meaning, and without any dangling reference pattern of the kind "
    "the self-containedness check would otherwise flag as a failure."
)


def _write_page_for_patch_test(pages_dir, subdir, stem, body_extra=""):
    d = pages_dir / subdir
    d.mkdir(parents=True, exist_ok=True)
    frontmatter.write_page(
        d / f"{stem}.md",
        {"type": "entity", "canonical_name": stem.title(), "sources": ["raw/cache/fixture.md"], "inbound_links": 0},
        f"\n# {stem.title()}\n\n{_LONG_FIRST_PARAGRAPH}{body_extra}\n\n"
        "## Key Claims\n\n- Existing claim one.\n- Existing claim two.\n- Existing claim three.\n\n"
        "## Relationships\n\nNo specific relationships to pages in the current wiki context.\n\n"
        "## Sources\n\n- existing source\n",
    )
    return d / f"{stem}.md"


def test_apply_one_pending_calls_content_merge_with_target_section_and_proposed_update(tmp_path):
    pages_dir = tmp_path / "wiki" / "_pages"
    _write_page_for_patch_test(pages_dir, "entity", "widget")

    seen_manifest = {}

    def fake_call_subagent(subagent_type, manifest, research_config):
        seen_manifest.update(manifest)
        assert subagent_type == "content_merge"
        merged = manifest["existing_content"] + "\n\n- New claim from proposed_update.\n"
        return json.dumps({"merged_content": merged, "merge_notes": "added claim"})

    block = (
        "## [2026-07-03] pending | widget.md\n"
        "target_page: widget.md\n"
        "target_section: Key Claims\n"
        "source: https://example.com/widget-spec\n"
        "status: approved\n"
        "proposed_update: Add a claim that Widget supports frobnication.\n"
    )

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir):
        ok, new_block = orchestrator._apply_one_pending(block, fake_call_subagent, {})

    assert ok
    assert "status: applied" in new_block
    assert seen_manifest["new_draft"] is None
    assert seen_manifest["target_section"] == "Key Claims"
    assert seen_manifest["proposed_update"] == "Add a claim that Widget supports frobnication."
    assert seen_manifest["source"] == "https://example.com/widget-spec"
    written = (pages_dir / "entity" / "widget.md").read_text(encoding="utf-8")
    assert "New claim from proposed_update" in written


def test_apply_one_pending_fails_when_page_not_found(tmp_path):
    pages_dir = tmp_path / "wiki" / "_pages"
    pages_dir.mkdir(parents=True)
    block = (
        "## [2026-07-03] pending | missing.md\n"
        "target_page: missing.md\n"
        "target_section: Key Claims\n"
        "source: https://example.com\n"
        "status: approved\n"
        "proposed_update: Add something.\n"
    )
    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir):
        ok, new_block = orchestrator._apply_one_pending(block, lambda *a: "{}", {})
    assert not ok
    assert "apply_failed (page not found)" in new_block


def test_apply_patch_queue_routes_both_merge_pending_and_pending_blocks(tmp_path):
    """Regression: apply_patch_queue() previously only ever recognized
    merge_pending headers -- every plain "pending" block was silently passed
    through untouched regardless of its approval status, so 18+ queued,
    human-approved section-update proposals had no automated apply path at
    all. Both kinds must now be processed when status: approved."""
    pages_dir = tmp_path / "wiki" / "_pages"
    log_md = tmp_path / "wiki" / "log.md"
    log_md.parent.mkdir(parents=True, exist_ok=True)
    log_md.write_text("# Wiki Log\n", encoding="utf-8")
    index_md = tmp_path / "wiki" / "index.md"
    index_md.write_text(
        "# Wiki Index\n\nLast updated: 2020-01-01 | Pages: 0 | Sources: 0\n\n"
        "## Entity Pages\n\n| Page | Summary | Tags | Sources | Inbound |\n"
        "|------|---------|------|---------|---------|\n\n"
        "## Synthesis Pages\n\n| Page | Connected Entities | Status | Inbound |\n"
        "|------|--------------------|--------|---------|\n\n## Concept Index\n",
        encoding="utf-8",
    )
    _write_page_for_patch_test(pages_dir, "entity", "alpha")
    _write_page_for_patch_test(pages_dir, "entity", "beta")

    queue_path = tmp_path / "wiki" / "patch_queue.md"
    queue_path.write_text(
        "# Wiki Patch Queue\n\n"
        "## [2026-07-03] merge_pending | alpha.md\n"
        "target_page: alpha.md\n"
        "canonical_name: Alpha\n"
        "source: https://example.com/alpha\n"
        "status: approved\n"
        "<!-- merge_draft_body\n# Alpha\n\nMerged alpha body.\nmerge_draft_body -->\n\n"
        "## [2026-07-03] pending | beta.md\n"
        "target_page: beta.md\n"
        "target_section: Key Claims\n"
        "source: https://example.com/beta\n"
        "status: approved\n"
        "proposed_update: Add a claim about beta.\n\n"
        "## [2026-07-03] pending | beta.md\n"
        "target_page: beta.md\n"
        "target_section: Key Claims\n"
        "source: https://example.com/beta2\n"
        "status: pending_review\n"
        "proposed_update: Not yet approved, must be skipped.\n",
        encoding="utf-8",
    )

    def fake_call_subagent(subagent_type, manifest, research_config):
        merged = manifest["existing_content"] + "\n\n- Applied.\n"
        return json.dumps({"merged_content": merged, "merge_notes": None})

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_LOG_MD", log_md), \
         patch.object(orchestrator, "_INDEX_MD", index_md):
        result = orchestrator.apply_patch_queue(call_subagent=fake_call_subagent)

    assert result == {"applied": 2, "skipped": 1, "failed": 0}
    queue_text = queue_path.read_text(encoding="utf-8")
    assert queue_text.count("status: applied") == 2
    assert "status: pending_review" in queue_text  # the unapproved one untouched
