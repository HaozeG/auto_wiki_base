---
canonical_name: IREE RISC-V Microkernel Support
aliases:
- 10x-IREE
- IREE RISC-V mmt4d microkernels
- IREE RISC-V microkernel support
subtype: null
tags: []
hardware_targets:
- MILK-V Jupiter
- RISC-V RVA22
workloads:
- LLM prefill
- LLM decode
- GEMM (matmul)
datatypes:
- f16 x f16 -> f32
metrics:
- tokens per second
- performance improvement
toolchains:
- IREE
- MLIR
- LM-Evaluation-Harness
constraints:
- VLEN=256
- RVA22 profile
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/bfa9d98ae6a1aa49.md
- https://arxiv.org/html/2508.14899v1
source_url: https://arxiv.org/html/2508.14899v1
fetched_at: '2026-07-03T15:26:45.626424+00:00'
type: optimization_recipe
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 2
outbound_links:
- target: mlir-xdsl-rvv-codegen-pipeline
  reason: Both approaches optimize GEMM on RISC-V for AI workloads, but the IREE recipe
    uses hand-written microkernels integrated into a production compiler framework,
    whereas the MLIR-xDSL pipeline uses compiler-driven code generation for portable
    kernel generation on K230 and BananaPi F3
- target: c908-wino-gemm-optimization
  reason: Both are optimization recipes for RISC-V matrix computations, but the IREE
    recipe is compiler-integrated and targets general RISC-V RVA22 platforms, while
    the C908 recipe is a hand-tuned library (SHL) optimization specific to the XuanTie
    C908 core with a 16x12 register blocking scheme
- target: iree-riscv-benchmark-milkv-jupiter
  reason: The benchmark page provides the measured performance results that validate
    this recipe
---

# IREE RISC-V Microkernel Support

The IREE RISC-V Microkernel Support is an optimization technique that adds RISC-V vector (RVV) microkernels to the IREE compiler framework, enabling efficient execution of Generative AI workloads on RISC-V-based hardware. The implementation focuses on the mmt4d (matrix multiply with transpose) operation for f16 x f16 -> f32 precision, with separate microkernels for LLM prefill and decode phases. VLEN-aware tiling is applied in the encoding pass to select optimal tile sizes based on the target VLEN (e.g., VLEN=256). Tile sizes for prefill are M,N,K=6,VLEN/8,1 and for decode are M,N,K=1,VLEN/4,1. Benchmarked on the MILK-V Jupiter board (1.66 GHz × 8 RISC-V cores, RVV 1.0, RVA22 profile), the optimized IREE achieves up to 50x decode speedup (single-threaded) and 17x decode speedup (multi-threaded) compared to upstream IREE for the Llama-3.2-1B-Instruct model. The optimization is validated by reproducing reference accuracy scores from HuggingFace on ARC_c and GPQA benchmarks.

## Key Claims

- Added RISC-V mmt4d microkernels for f16 x f16 -> f32 in IREE, covering LLM prefill (GEMM) and decode (GEMV) phases.
- Modified IREE's `iree-codegen-materialize-device-encoding` pass to enable transformation of linalg contraction ops to linalg.mmt4d with VLEN-aware tiling for RISC-V64.
- Tile sizes: prefill (M,N,K=6,VLEN/8,1), decode (M,N,K=1,VLEN/4,1).
- Achieves up to 50x single-threaded decode speedup, 17x multi-threaded decode speedup, and 2x multi-threaded prefill speedup over upstream IREE on MILK-V Jupiter.
- Accuracy of Llama-3.2-1B-Instruct compiled with optimized IREE matches HuggingFace reference on ARC_c and GPQA.

## Transformation

- Prerequisites: IREE compiler source, target RISC-V platform with RVV 1.0 and VLEN of at least 128 (tested with VLEN=256 on MILK-V Jupiter), understanding of IREE's encoding and microkernel pipeline.
- Steps:
  1. Extend the `iree-codegen-materialize-device-encoding` pass to detect RISC-V64 target and apply VLEN-aware tiling for linalg.mmt4d operations.
  2. Implement mmt4d microkernels for RISC-V vector target in IREE's microkernel library, covering f16 x f16 -> f32 with separate prefill (GEMM) and decode (GEMV) variants.
  3. Integrate the microkernels into IREE's lowering pipeline so that linalg.mmt4d operations are lowered to calls to these microkernels.
  4. Validate accuracy by running Llama-3.2-1B-Instruct through LM-Evaluation-Harness and comparing output against HuggingFace reference.
- Expected effect: Significant speedup for LLM inference on RISC-V hardware, especially for decode phase, with minimal impact on accuracy.
- Failure modes: Oversized tiles may cause register spills and performance degradation; undersized tiles underutilize registers. Tile size selection must be tuned to target VLEN.
- Measurements: See [[iree-riscv-benchmark-milkv-jupiter]] for detailed performance numbers on MILK-V Jupiter.

## Relationships

- [[mlir-xdsl-rvv-codegen-pipeline]]: Both approaches optimize GEMM on RISC-V for AI workloads, but the IREE recipe uses hand-written microkernels integrated into a production compiler framework, whereas the MLIR-xDSL pipeline uses compiler-driven code generation for portable kernel generation on K230 and BananaPi F3.
- [[c908-wino-gemm-optimization]]: Both are optimization recipes for RISC-V matrix computations, but the IREE recipe is compiler-integrated and targets general RISC-V RVA22 platforms, while the C908 recipe is a hand-tuned library (SHL) optimization specific to the XuanTie C908 core with a 16x12 register blocking scheme.
- [[iree-riscv-benchmark-milkv-jupiter]]: The benchmark page provides the measured performance results that validate this recipe.

## Sources

- https://arxiv.org/html/2508.14899v1
