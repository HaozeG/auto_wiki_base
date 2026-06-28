import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from domain_analysis import build_gap_manifest, extract_evidence, validate_benchmark_claim
from qmd_runner import QmdMatch, assess_candidate_similarity
from validate_output import validate_and_parse


def test_eval_schema_accepts_optimization_page_type_and_structured_frontmatter():
    raw = json.dumps({
        "decision": "approve",
        "rejection_reason": None,
        "scorecard": {
            "novelty_delta": 0.8,
            "claim_density": 0.8,
            "self_containedness": 0.9,
            "bridge_score": 0.6,
            "hub_potential": 0.5,
            "gap_fill_score": 0.7,
            "contradiction_potential": 0.0,
            "weighted_total": 0.72,
        },
        "page_drafts": [{
            "page_type": "hardware_target",
            "filename": "projectnimbus_x9",
            "frontmatter": {
                "type": "hardware_target",
                "hardware_targets": ["ProjectNimbus X9"],
                "toolchains": ["LLVM"],
                "constraints": ["int8 only"],
                "sources": ["https://example.com/spec"],
            },
            "content": "# ProjectNimbus X9\n\nBody.",
        }],
        "pages_to_update": [],
        "contradictions_found": [],
    })

    result = validate_and_parse(raw, "EvalResult")

    assert result is not None
    assert result["page_drafts"][0]["page_type"] == "hardware_target"


def test_similarity_gate_uses_configured_domain_stopwords_with_non_riscv_names():
    decision = assess_candidate_similarity(
        {"title": "ProjectNimbus Accelerator X9", "snippet": "matrix engine"},
        [QmdMatch(rank=1, file="entity/projectnimbus_accelerator_x8.md", score=0.84)],
        {
            "topic_similarity_min_score": 0.80,
            "near_duplicate_score": 0.90,
            "topic_saturation_hit_threshold": 2,
            "domain_stopwords": ["accelerator"],
        },
    )

    assert decision["skip"] is True
    assert decision["reason"] == "same_product_family"


def test_gap_manifest_summarizes_missing_structured_coverage(tmp_path):
    pages = tmp_path / "_pages"
    (pages / "hardware_target").mkdir(parents=True)
    (pages / "benchmark_result").mkdir()
    (pages / "hardware_target" / "nimbus_x9.md").write_text(
        "---\n"
        "type: hardware_target\n"
        "hardware_targets: [ProjectNimbus X9]\n"
        "toolchains: [LLVM]\n"
        "sources: [https://example.com/spec]\n"
        "---\n\n# ProjectNimbus X9\n",
        encoding="utf-8",
    )
    (pages / "benchmark_result" / "nimbus_gemm.md").write_text(
        "---\n"
        "type: benchmark_result\n"
        "hardware_targets: [ProjectNimbus X9]\n"
        "workloads: [GEMM]\n"
        "metrics: [throughput]\n"
        "sources: [https://example.com/bench]\n"
        "---\n\n# Nimbus GEMM\n",
        encoding="utf-8",
    )

    manifest = build_gap_manifest(pages, {})

    assert manifest["page_type_counts"]["hardware_target"] == 1
    assert manifest["structured_field_coverage"]["hardware_targets"]["ProjectNimbus X9"] == 2
    assert "missing_page_type:workload_kernel" in manifest["gap_types"]
    assert manifest["benchmark_results_missing_required_fields"] == [
        "nimbus_gemm.md: measurement_context"
    ]


def test_benchmark_claim_validation_requires_measurement_context():
    ok = validate_benchmark_claim({
        "hardware_targets": ["ProjectNimbus X9"],
        "workloads": ["GEMM 1024x1024"],
        "metrics": ["throughput"],
        "measurement_method": "vendor benchmark script on SDK 2.1",
        "evidence_strength": "reported",
    })
    missing = validate_benchmark_claim({
        "hardware_targets": ["ProjectNimbus X9"],
        "workloads": ["GEMM 1024x1024"],
        "metrics": ["throughput"],
        "evidence_strength": "reported",
    })

    assert ok["pass"] is True
    assert missing["pass"] is False
    assert missing["missing_fields"] == ["measurement_context"]


def test_evidence_extractor_finds_generic_measurements_and_toolchains():
    evidence = extract_evidence(
        "ProjectNimbus X9 reaches 42 TOPS on GEMM with LLVM 18.1 and SDK v2.0. "
        "The report lists throughput and latency.",
        {"title": "ProjectNimbus X9 benchmark"},
    )

    assert "42 TOPS" in evidence["candidate_measurements"]
    assert "GEMM" in evidence["workload_names"]
    assert any(tool.lower() == "llvm" for tool in evidence["toolchain_names"])
    assert "throughput" in evidence["metrics"]
