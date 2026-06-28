"""
Unit tests for Layer 3 (self-retrieval precision) of eval_summary.py.

All tests mock subprocess.run so no qmd installation is required.
The known near-duplicate pairs from the 2026-06-27 lint pass are used
as discrimination fixtures: a saturated page (many competitors) must be
distinguishable from a distinct page (few competitors).
"""

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
from eval_summary import _normalize_qmd_file, layer3_check

FIXTURES = Path(__file__).parent / "fixtures"


# ---------------------------------------------------------------------------
# _normalize_qmd_file helpers
# ---------------------------------------------------------------------------

class TestNormalizeQmdFile:
    def test_strips_path_prefix(self):
        assert _normalize_qmd_file("entity/foo_bar.md") == "foo_bar"

    def test_strips_line_suffix(self):
        assert _normalize_qmd_file("entity/foo_bar.md:27") == "foo_bar"

    def test_converts_hyphens_to_underscores(self):
        assert _normalize_qmd_file("entity/gnu-toolchain-riscv.md") == "gnu_toolchain_riscv"

    def test_bare_filename(self):
        assert _normalize_qmd_file("xiangshan_riscv.md") == "xiangshan_riscv"

    def test_deep_path(self):
        assert _normalize_qmd_file("wiki/_pages/entity/gemmini.md:42") == "gemmini"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_qmd_result(file_str: str, score: float = 1.0) -> dict:
    return {"file": file_str, "score": score, "snippet": "..."}


def _mock_run(stdout_obj, returncode: int = 0):
    m = MagicMock()
    m.returncode = returncode
    m.stdout = json.dumps(stdout_obj)
    m.stderr = ""
    return m


# ---------------------------------------------------------------------------
# Self-retrieval: page IS in top-5 → pass
# ---------------------------------------------------------------------------

class TestSelfRetrieval:
    def test_self_retrieved_passes(self, tmp_path):
        page = FIXTURES / "pass_entity.md"
        qmd_results = [
            _make_qmd_result("entity/pass_entity.md", 0.95),
            _make_qmd_result("entity/other_page.md", 0.70),
            _make_qmd_result("entity/another.md", 0.60),
        ]
        with patch("subprocess.run", return_value=_mock_run(qmd_results)):
            result = layer3_check(page, "entity")
        assert result["pass"] is True
        assert result["self_retrieved"] is True

    def test_not_self_retrieved_fails(self, tmp_path):
        page = FIXTURES / "pass_entity.md"
        # slug is "pass_entity"; none of these match it
        qmd_results = [
            _make_qmd_result("entity/risc_v_vector_extension.md", 0.90),
            _make_qmd_result("entity/tvm_riscv_backend.md", 0.85),
            _make_qmd_result("entity/gemmini.md", 0.80),
            _make_qmd_result("entity/boom_riscv.md", 0.75),
            _make_qmd_result("entity/xiangshan_riscv.md", 0.70),
        ]
        with patch("subprocess.run", return_value=_mock_run(qmd_results)):
            result = layer3_check(page, "entity")
        assert result["pass"] is False
        assert result["self_retrieved"] is False

    def test_self_retrieved_with_line_suffix(self):
        """qmd sometimes appends :NN line number to file path — must still match."""
        page = FIXTURES / "pass_entity.md"
        qmd_results = [
            _make_qmd_result("entity/pass_entity.md:12", 0.95),
            _make_qmd_result("entity/other.md", 0.50),
        ]
        with patch("subprocess.run", return_value=_mock_run(qmd_results)):
            result = layer3_check(page, "entity")
        assert result["self_retrieved"] is True
        assert result["pass"] is True


# ---------------------------------------------------------------------------
# Saturation signal: near-duplicate pairs from 2026-06-27 lint
# ---------------------------------------------------------------------------

class TestSaturationSignal:
    """
    Discrimination test: the saturation metric must distinguish a distinct page
    from a saturated near-duplicate.  Uses known pairs from the lint report:
      near-dup:  gnu_toolchain_riscv_vector ↔ riscv_llvm_backend
      distinct:  gemmini  (very few close competitors)
    """

    def test_distinct_page_low_saturation(self):
        page = FIXTURES / "pass_entity.md"  # stand-in for a distinct page
        # Self at top, then unrelated pages — only 1 competitor
        qmd_results = [
            _make_qmd_result("entity/pass_entity.md", 0.95),
            _make_qmd_result("entity/boom_riscv.md", 0.40),
        ]
        with patch("subprocess.run", return_value=_mock_run(qmd_results)):
            result = layer3_check(page, "entity")
        assert result["saturation"] < 0.8
        assert result["saturated"] is False

    def test_near_dup_page_high_saturation(self):
        """A page whose top-5 are all near-duplicates should flag as saturated."""
        page = FIXTURES / "pass_entity.md"
        # slug = pass_entity; 4 competitors (>= topic_saturation_hit_threshold=4)
        qmd_results = [
            _make_qmd_result("entity/pass_entity.md", 0.92),
            _make_qmd_result("entity/gnu_toolchain_riscv_vector.md", 0.91),
            _make_qmd_result("entity/riscv_llvm_backend.md", 0.90),
            _make_qmd_result("entity/riscv_gnu_toolchain.md", 0.89),
            _make_qmd_result("entity/llvm_riscv_codegen.md", 0.88),
        ]
        with patch("subprocess.run", return_value=_mock_run(qmd_results)):
            result = layer3_check(page, "entity")
        assert result["saturated"] is True
        assert len(result["competitors"]) >= 4
        # Even though saturated, page still PASSES (saturation is informational)
        assert result["pass"] is True

    def test_saturation_does_not_block_pass(self):
        """Saturation is informational only — saturated page still passes if self_retrieved."""
        page = FIXTURES / "pass_entity.md"
        qmd_results = [
            _make_qmd_result("entity/pass_entity.md", 0.95),
            _make_qmd_result("entity/dup_a.md", 0.94),
            _make_qmd_result("entity/dup_b.md", 0.93),
            _make_qmd_result("entity/dup_c.md", 0.92),
            _make_qmd_result("entity/dup_d.md", 0.91),
        ]
        with patch("subprocess.run", return_value=_mock_run(qmd_results)):
            result = layer3_check(page, "entity")
        assert result["saturated"] is True
        assert result["pass"] is True  # self-retrieved → passes despite saturation


# ---------------------------------------------------------------------------
# Graceful degradation
# ---------------------------------------------------------------------------

class TestGracefulDegradation:
    def test_qmd_not_installed_skips(self):
        page = FIXTURES / "pass_entity.md"
        with patch("subprocess.run", side_effect=FileNotFoundError):
            result = layer3_check(page, "entity")
        assert result.get("skipped") is True
        assert result["pass"] is True

    def test_qmd_timeout_skips(self):
        import subprocess
        page = FIXTURES / "pass_entity.md"
        with patch("subprocess.run", side_effect=subprocess.TimeoutExpired(cmd="qmd", timeout=30)):
            result = layer3_check(page, "entity")
        assert result.get("skipped") is True
        assert result["pass"] is True

    def test_qmd_nonzero_exit_returns_not_found(self):
        # BM25 search fails → self_retrieved=False (not a skip)
        page = FIXTURES / "pass_entity.md"
        m = MagicMock()
        m.returncode = 1
        m.stdout = ""
        m.stderr = "error"
        with patch("subprocess.run", return_value=m):
            result = layer3_check(page, "entity")
        assert result.get("skipped") is not True
        assert result["self_retrieved"] is False
        assert result["pass"] is False

    def test_qmd_invalid_json_returns_not_found(self):
        # BM25 search returns unparseable output → self_retrieved=False
        page = FIXTURES / "pass_entity.md"
        m = MagicMock()
        m.returncode = 0
        m.stdout = "not valid json\nsome lines\n"
        m.stderr = ""
        with patch("subprocess.run", return_value=m):
            result = layer3_check(page, "entity")
        assert result.get("skipped") is not True
        assert result["self_retrieved"] is False

    def test_empty_results_list_fails_gracefully(self):
        page = FIXTURES / "pass_entity.md"
        with patch("subprocess.run", return_value=_mock_run([])):
            result = layer3_check(page, "entity")
        # Empty results: slug not in empty top_k → fail but no crash
        assert result["pass"] is False
        assert result["self_retrieved"] is False


# ---------------------------------------------------------------------------
# needs_summary_revision frontmatter flag lifecycle
# ---------------------------------------------------------------------------

class TestFrontmatterFlag:
    def test_flag_set_false_on_pass(self, tmp_path):
        """Passing page must have needs_summary_revision cleared to False."""
        import yaml
        src = FIXTURES / "pass_entity.md"
        page = tmp_path / "pass_entity.md"
        page.write_text(src.read_text())

        qmd_results = [_make_qmd_result("entity/pass_entity.md", 0.95)]
        with patch("subprocess.run", return_value=_mock_run(qmd_results)):
            result = layer3_check(page, "entity")

        assert result["pass"] is True
        text = page.read_text()
        end = text.find("---", 3)
        fm = yaml.safe_load(text[3:end])
        assert fm.get("needs_summary_revision") is False

    def test_flag_set_true_on_fail(self, tmp_path):
        """Failing page must have needs_summary_revision set to True."""
        import yaml
        src = FIXTURES / "pass_entity.md"
        page = tmp_path / "pass_entity.md"
        page.write_text(src.read_text())

        qmd_results = [_make_qmd_result("entity/completely_different.md", 0.5)]
        with patch("subprocess.run", return_value=_mock_run(qmd_results)):
            result = layer3_check(page, "entity")

        assert result["pass"] is False
        text = page.read_text()
        end = text.find("---", 3)
        fm = yaml.safe_load(text[3:end])
        assert fm.get("needs_summary_revision") is True

    def test_flag_cleared_after_improvement(self, tmp_path):
        """A page that previously failed (flag=True) gets flag cleared when it passes."""
        import yaml
        src = FIXTURES / "pass_entity.md"
        page = tmp_path / "pass_entity.md"
        # Pre-set the flag to True (simulating a prior failed run)
        content = src.read_text()
        content = content.replace(
            "needs_summary_revision: ~",
            "needs_summary_revision: true",
            1,
        )
        if "needs_summary_revision" not in content:
            # Insert it in frontmatter if not present
            content = content.replace("cold_start: true", "cold_start: true\nneeds_summary_revision: true", 1)
        page.write_text(content)

        qmd_results = [_make_qmd_result("entity/pass_entity.md", 0.95)]
        with patch("subprocess.run", return_value=_mock_run(qmd_results)):
            result = layer3_check(page, "entity")

        assert result["pass"] is True
        text = page.read_text()
        end = text.find("---", 3)
        fm = yaml.safe_load(text[3:end])
        assert fm.get("needs_summary_revision") is False
