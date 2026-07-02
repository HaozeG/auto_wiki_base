import json
import sys
import types
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).parent.parent))

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

    def record_response(self, idx, raw_response, schema_valid):
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


def test_keyword_recommender_model_prefers_strong_env_and_preserves_thinking_suffix():
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

    assert model == "deepseek-v4-pro[1m]"


def test_keyword_recommender_uses_anthropic_and_strong_model(monkeypatch):
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
    with patch.dict("os.environ", {"ANTHROPIC_MODEL": "deepseek-v4-pro[1m]"}, clear=True):
        plan = orchestrator._call_keyword_recommender(
            {"base_query": "ProjectNimbus", "concept_gaps": [], "max_keywords": 3},
            {},
        )

    assert calls["model"] == "deepseek-v4-pro[1m]"
    assert calls["model"] != "deepseek-v4-flash"
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
         patch.object(orchestrator, "_wiki_is_mature", return_value=True), \
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


def test_keyword_manifest_includes_theme_and_previous_queries(monkeypatch):
    captured = {}

    def fake_call(manifest, research_config):
        captured.update(manifest)
        return {"recommended_keywords": [], "avoid_patterns": [], "model": "test", "source": "test"}

    monkeypatch.setattr(orchestrator, "_call_keyword_recommender", fake_call)
    monkeypatch.setattr(orchestrator, "_get_repo_research_theme", lambda: "ProjectNimbus theme")
    monkeypatch.setattr(orchestrator, "_get_wiki_topic_summary", lambda: "Current coverage")
    monkeypatch.setattr(orchestrator, "_get_concept_gaps", lambda: ["Missing API"])

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
        "---\ntype: entity\ntags: [x]\nsources: [raw/cache/a.md, raw/cache/b.md]\n"
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
        "## Concept Index\n\n- **Alpha**: → [alpha](entity/alpha.md)\n\n"
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
    # Concept Index is untouched by the rebuild (not row-based like the tables).
    assert "**Alpha**: → [alpha](entity/alpha.md)" in text


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


def test_maybe_transition_maturity_only_touches_patched_claude_md(tmp_path):
    """Regression test: _maybe_transition_maturity() is called from inside
    _run_research_state() and writes connectivity stats to _CLAUDE_MD (and, on
    a cold_start -> mature transition, appends to _LOG_MD). Two other tests in
    this file call _run_research_state() directly and only patched
    _WIKI_PAGES_DIR, not _CLAUDE_MD/_LOG_MD — so it silently recomputed stats
    from a throwaway tmp_path page set and wrote them into the real project
    CLAUDE.md and wiki/log.md on every test run. Assert the function only
    ever touches the paths it's given.
    """
    pages_dir = tmp_path / "wiki" / "_pages" / "entity"
    pages_dir.mkdir(parents=True)
    (pages_dir / "a.md").write_text(
        "---\ntype: entity\ninbound_links: 1\n---\n\n# A\n", encoding="utf-8"
    )
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text(
        "```yaml\n[system_state]\ngraph_maturity: false\n```\n", encoding="utf-8"
    )
    log_md = tmp_path / "log.md"
    log_md.write_text("# Log\n", encoding="utf-8")

    with patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md), \
         patch.object(orchestrator, "_LOG_MD", log_md):
        orchestrator._maybe_transition_maturity("sess-test")

    text = claude_md.read_text(encoding="utf-8")
    assert "orphan_fraction: 0.0" in text or "orphan_fraction: 0" in text
    # This single-page fixture is mature (orphan_fraction 0, median 1), so the
    # cold_start -> mature transition fires and appends to the patched log.
    assert "transition | cold_start" in log_md.read_text(encoding="utf-8")


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
         }), \
         patch.object(orchestrator, "QmdRunner", return_value=EmptyQmdRunner()), \
         patch.object(orchestrator, "_WIKI_PAGES_DIR", pages_dir), \
         patch.object(orchestrator, "_INDEX_MD", index), \
         patch.object(orchestrator, "_LOG_MD", log_path), \
         patch.object(orchestrator, "_CLAUDE_MD", claude_md), \
         patch.object(orchestrator, "AuditLog", return_value=audit), \
         patch.object(orchestrator, "_run_graph_stats"), \
         patch.object(orchestrator, "_check_synthesis_gaps", return_value=[]), \
         patch.object(orchestrator, "_wiki_is_mature", return_value=True), \
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
