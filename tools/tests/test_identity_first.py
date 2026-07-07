"""Tests for the write-time quality gates: frontmatter atomicity, connectivity
maturity, identity resolution + upsert, and the approval-gated content merge.

No API key required — the model-dependent paths use injected/monkeypatched
subagent callers."""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

import frontmatter
import graph_stats
import identity
import orchestrator


# ---------------------------------------------------------------------------
# Part 1 — frontmatter atomic round-trip (corruption regression)
# ---------------------------------------------------------------------------

def _write(path: Path, fm_lines: str, body: str = "# Title\n\nBody.\n") -> None:
    path.write_text(f"---\n{fm_lines}---\n\n{body}", encoding="utf-8")


def test_frontmatter_no_delimiter_corruption(tmp_path):
    p = tmp_path / "page.md"
    _write(p, "type: entity\ninbound_links: 0\n")
    for _ in range(5):
        frontmatter.increment_page_field(p, "inbound_links")
    frontmatter.set_page_field(p, "updated", "2026-06-30")
    text = p.read_text()
    assert text.count("---") == 2, f"delimiter corruption: {text!r}"
    fm, body = frontmatter.parse_page(p)
    assert fm["inbound_links"] == 5
    assert fm["updated"] == "2026-06-30"
    assert body.strip() == "# Title\n\nBody."


def test_frontmatter_noop_without_block(tmp_path):
    p = tmp_path / "plain.md"
    p.write_text("# Just a heading\n\ntext\n", encoding="utf-8")
    assert frontmatter.set_page_field(p, "x", 1) is False
    assert "x:" not in p.read_text()


def test_merge_embedded_frontmatter_preserves_content_fields():
    """Weaker eval-subagent models sometimes echo a second frontmatter block
    inside their own `content` field instead of using the structured
    `frontmatter` dict. That embedded block must be merged into
    draft['frontmatter'] (not silently discarded) so content-derived fields
    like tags/hardware_targets/constraints survive, matching an observed
    live-run draft (RISC-V IME Option D)."""
    draft = {
        "frontmatter": {"canonical_name": "IME Option D", "subtype": "hardware_target"},
        "content": (
            "---\n"
            "type: hardware_target\n"
            "created: 2025-04-10\n"
            "tags: [risc-v, ime, matrix-extension]\n"
            "sources: [\"https://hallucinated.example/ime\"]\n"
            "hardware_targets: [\"RISC-V IME\"]\n"
            "constraints: [\"VLEN=1024\"]\n"
            "---\n"
            "\n"
            "# RISC-V IME Option D\n"
            "\n"
            "Body text.\n"
        ),
    }
    orchestrator._merge_embedded_frontmatter(draft)
    fm = draft["frontmatter"]
    # structured dict fields win, embedded content-derived fields fill the rest
    assert fm["canonical_name"] == "IME Option D"
    assert fm["tags"] == ["risc-v", "ime", "matrix-extension"]
    assert fm["hardware_targets"] == ["RISC-V IME"]
    assert fm["constraints"] == ["VLEN=1024"]
    assert draft["content"].startswith("# RISC-V IME Option D")
    # orchestrator-managed keys must NOT be seeded from the embedded block,
    # even though the model echoed a (hallucinated) value for them
    assert "created" not in fm
    assert "sources" not in fm or "https://hallucinated.example/ime" not in fm["sources"]


def test_merge_embedded_frontmatter_strips_malformed_yaml_block():
    """Reproduces the allwinner_t536.md corruption at the orchestrator level:
    the embedded block's own YAML is malformed (duplicate `tags:` key), so it
    can't be parsed for field values, but it must still be structurally
    stripped from draft['content'] -- otherwise the garbage block reaches
    _write_page and survives to disk ahead of the real title/content."""
    draft = {
        "frontmatter": {"canonical_name": "Allwinner T536", "subtype": "hardware_target"},
        "content": (
            "---\n"
            "type: hardware_target\n"
            "tags:\n"
            "- allwinner\n"
            "- risc-v\n"
            "tags: []\n"
            "- risc-v\n"
            "- npu\n"
            "sources:\n"
            "- https://example.com/t536\n"
            "---\n"
            "\n"
            "# Allwinner T536\n"
            "\n"
            "Body text.\n"
        ),
    }
    orchestrator._merge_embedded_frontmatter(draft)
    # Malformed YAML means no fields could be parsed out of the embedded block,
    # but the block itself must still be gone from the content.
    assert draft["content"].startswith("# Allwinner T536")
    assert "tags: []" not in draft["content"]
    assert "allwinner" not in draft["content"]


def test_merge_embedded_frontmatter_noop_without_embedded_block():
    draft = {"frontmatter": {"canonical_name": "X"}, "content": "# X\n\nBody.\n"}
    before = dict(draft["frontmatter"])
    orchestrator._merge_embedded_frontmatter(draft)
    assert draft["frontmatter"] == before
    assert draft["content"] == "# X\n\nBody.\n"


# ---------------------------------------------------------------------------
# Part 3 — canonical_name normalizer spec (merge vs split)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("a,b", [
    ("Gemmini", "Gemmini Architecture"),
    ("MLIR", "MLIR (software)"),
])
def test_normalizer_must_merge(a, b):
    assert identity.normalize_canonical(a) == identity.normalize_canonical(b)


@pytest.mark.parametrize("a,b", [
    ("XuanTie C908", "XuanTie C910"),
    ("MLPerf Inference", "MLPerf Tiny"),
    ("Ara", "AraXL"),
    ("Tenstorrent Blackhole", "Tenstorrent Wormhole"),
])
def test_normalizer_must_split(a, b):
    assert identity.normalize_canonical(a) != identity.normalize_canonical(b)


@pytest.mark.parametrize("a,b", [
    # camelCase/spacing variant of the same compound name (found live: two
    # optimization_recipe pages generated from the identical source only
    # differed in "Banana Pi" vs "BananaPi" spacing and survived as separate
    # pages).
    ("RVV Optimization for LLM Inference on Banana Pi BPI-F3",
     "RVV-Optimized LLM Inference on BananaPi BPI-F3"),
    # -ize/-ization verb-noun morphology of the same recipe.
    ("GAP9 Quantization Recipe", "GAP9 Quantized Recipe"),
])
def test_normalizer_merges_spelling_and_morphology_variants(a, b):
    assert identity.normalize_canonical(a) == identity.normalize_canonical(b)


# ---------------------------------------------------------------------------
# Part 2 — connectivity-based maturity
# ---------------------------------------------------------------------------

def test_maturity_predicate_orphan_heavy_graph(tmp_path):
    # 8 orphans + 2 hubs: high mean, but median 0 and orphan_fraction 0.8 → NOT mature
    d = tmp_path / "_pages"
    d.mkdir()
    for i in range(8):
        _write(d / f"orphan{i}.md", "type: entity\ninbound_links: 0\n")
    _write(d / "hub1.md", "type: entity\ninbound_links: 20\n")
    _write(d / "hub2.md", "type: entity\ninbound_links: 20\n")
    stats = graph_stats.compute_stats(d)
    assert stats["mean_inbound_links"] > 2.0          # old predicate would say MATURE
    assert stats["orphan_fraction"] == 0.8
    assert stats["median_inbound_links"] == 0.0
    assert stats["mature"] is False                   # new predicate: NOT mature


def test_maturity_predicate_connected_graph(tmp_path):
    d = tmp_path / "_pages"
    d.mkdir()
    for i in range(10):
        _write(d / f"p{i}.md", f"type: entity\ninbound_links: {2 + (i % 3)}\n")
    stats = graph_stats.compute_stats(d)
    assert stats["orphan_fraction"] == 0.0
    assert stats["median_inbound_links"] >= 1
    assert stats["mature"] is True


# ---------------------------------------------------------------------------
# Part 3 — identity registry + resolve
# ---------------------------------------------------------------------------

def test_registry_resolve_collision_and_novel(tmp_path):
    d = tmp_path / "_pages"
    (d / "entity").mkdir(parents=True)
    _write(d / "entity" / "Gemmini.md", "type: entity\ncanonical_name: Gemmini\ninbound_links: 1\n")
    reg = identity.build_registry(d)
    action, ref = identity.resolve("Gemmini Architecture", reg)
    assert action == "upsert" and ref is not None and ref.filename == "Gemmini.md"
    action2, ref2 = identity.resolve("XuanTie C910", reg)
    assert action2 == "create" and ref2 is None


# ---------------------------------------------------------------------------
# Part 3 — write gate hard-blocks duplicate creation (mocked, no API)
# ---------------------------------------------------------------------------

def _orch_tmp_env(monkeypatch, tmp_path):
    pages = tmp_path / "wiki" / "_pages"
    (pages / "entity").mkdir(parents=True)
    monkeypatch.setattr(orchestrator, "_PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(orchestrator, "_WIKI_PAGES_DIR", pages)
    monkeypatch.setattr(orchestrator, "_LOG_MD", tmp_path / "wiki" / "log.md")
    monkeypatch.setattr(orchestrator, "_INDEX_MD", tmp_path / "wiki" / "index.md")
    monkeypatch.setattr(orchestrator, "_RAW_CACHE_DIR", tmp_path / "raw" / "cache")
    monkeypatch.setattr(orchestrator, "_run_qmd_update", lambda *_a, **_k: (True, None))
    orchestrator._REGISTRY_CACHE.clear()
    return pages


class _Audit:
    def record_page_written(self, *_a, **_k):
        pass


def _session(tmp_path, sid="testsess"):
    from research_state import ResearchSessionState
    return ResearchSessionState.create(sid, "q", {"depth": "shallow"}, tmp_path / "state")


def test_write_gate_blocks_duplicate_create(monkeypatch, tmp_path):
    from quota import QuotaManager
    pages = _orch_tmp_env(monkeypatch, tmp_path)
    _write(pages / "entity" / "Gemmini.md",
           "type: entity\ncanonical_name: Gemmini\naliases: []\nsources: []\ninbound_links: 2\n")
    session = _session(tmp_path)
    quota = QuotaManager(max_candidates=10, max_new_pages=10)
    entry = {
        "id": "c1",
        "candidate": {"url": "https://ex.com/gemmini2"},
        "drafts": [{
            "page_type": "entity",
            "filename": "Gemmini_Architecture",
            "frontmatter": {"canonical_name": "Gemmini Architecture", "aliases": [], "sources": []},
            "content": "# Gemmini Architecture\n\nA systolic array GEMM accelerator.\n",
        }],
        "updates": [],
        "source_snapshot": "raw/cache/abc.md",
        "source_url": "https://ex.com/gemmini2",
        "fetched_at": "2026-06-30T00:00:00Z",
    }
    status, err = orchestrator._write_approved_entry(
        entry, session, _Audit(), quota, None, set()
    )
    assert status == "ok"
    # No duplicate page created
    assert not (pages / "entity" / "Gemmini_Architecture.md").exists()
    # Existing page gained the colliding name as an alias
    fm, _ = frontmatter.parse_page(pages / "entity" / "Gemmini.md")
    assert "Gemmini Architecture" in (fm.get("aliases") or [])
    # A merge patch was queued
    queue = (tmp_path / "wiki" / "patch_queue.md").read_text()
    assert "merge_pending" in queue and "Gemmini.md" in queue


# ---------------------------------------------------------------------------
# Part 3b — approval-gated content merge via `patch apply`
# ---------------------------------------------------------------------------

def test_patch_apply_merges_only_when_approved(monkeypatch, tmp_path):
    pages = _orch_tmp_env(monkeypatch, tmp_path)
    target = pages / "entity" / "Gemmini.md"
    _write(target, "type: entity\ncanonical_name: Gemmini\nsources: []\ninbound_links: 2\n",
           body="# Gemmini\n\nOriginal claims.\n")
    queue = tmp_path / "wiki" / "patch_queue.md"
    queue.parent.mkdir(parents=True, exist_ok=True)
    block = (
        "# Wiki Patch Queue\n\n"
        "## [2026-06-30] merge_pending | Gemmini.md\n"
        "target_page: Gemmini.md\n"
        "canonical_name: Gemmini\n"
        "source: https://ex.com/x\n"
        "status: {status}\n"
        "<!-- merge_draft_body\n# Gemmini\n\nNew claim from second source.\nmerge_draft_body -->\n"
    )
    # deterministic pipeline always passes in this unit test
    monkeypatch.setattr(orchestrator, "_run_eval_pipeline", lambda draft: (True, {}))
    merged = "# Gemmini\n\nOriginal claims.\n\nNew claim from second source.\n"
    fake_merge = lambda *_a, **_k: json.dumps({"merged_content": merged, "merge_notes": "combined"})

    # (a) pending → untouched
    queue.write_text(block.format(status="pending_review"), encoding="utf-8")
    summary = orchestrator.apply_patch_queue(call_subagent=fake_merge)
    assert summary == {"applied": 0, "skipped": 1, "failed": 0}
    assert "Original claims." in target.read_text() and "New claim" not in target.read_text()

    # (b) approved → merged into the single page, marked applied, no 2nd page
    queue.write_text(block.format(status="approved"), encoding="utf-8")
    summary = orchestrator.apply_patch_queue(call_subagent=fake_merge)
    assert summary == {"applied": 1, "skipped": 0, "failed": 0}
    body = target.read_text()
    assert "New claim from second source." in body
    assert "status: applied" in queue.read_text()
    assert len(list(pages.rglob("*.md"))) == 1


# ---------------------------------------------------------------------------
# Part 5 — profile-architect falls back to deterministic on bad/absent agent
# ---------------------------------------------------------------------------

def test_profile_architect_fallback(monkeypatch):
    monkeypatch.setattr(orchestrator, "_call_subagent", lambda *_a, **_k: "not json at all")
    assert orchestrator._propose_profiles_via_agent("anything") is None
    profiles = orchestrator.propose_profiles("RISC-V AI accelerator", use_agent=True)
    assert profiles and all("id" in p for p in profiles)
