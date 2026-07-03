---
canonical_name: QiMeng-TensorOp
aliases: []
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.7
  bridge_score: 0.7
  hub_potential: 0.5
sources:
- raw/cache/1b9c599677f606e2.md
- https://arxiv.org/html/2505.06302v1
source_url: https://arxiv.org/html/2505.06302v1
fetched_at: '2026-07-03T18:36:20.296788+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: mlir-xdsl-rvv-codegen-pipeline
  reason: Both QiMeng-TensorOp and the MLIR-xDSL RVV Code Generation Pipeline aim
    to automate generation of high-performance tensor operators on RISC-V platforms,
    but QiMeng-TensorOp uses LLMs to produce hardware-primitive code, while the MLIR-xDSL
    pipeline relies on custom compiler IR transformations and xDSL passes for code
    generation
- target: c908-wino-gemm-optimization
  reason: QiMeng-TensorOp's claim of reaching 251% of OpenBLAS on RISC-V CPUs is directly
    relevant to hand-tuned library approaches like the SHL optimizations for the XuanTie
    C908; however, QiMeng-TensorOp aims for automatic cross-platform generation rather
    than per-platform manual tuning
---

# QiMeng-TensorOp

QiMeng-TensorOp is a framework for automatically generating high-performance tensor operators using large language models (LLMs) and hardware primitives. The framework accepts a one-line user prompt and guides LLMs to exploit hardware characteristics, generating code that uses assembly instructions or hardware intrinsics for diverse architectures including RISC-V, ARM, and NVIDIA GPUs. It tunes parameters automatically to optimize performance across platforms, aiming to replace the months-long manual optimization process required by libraries such as OpenBLAS and cuBLAS. Experimental results demonstrate that QiMeng-TensorOp achieves up to 1291× performance improvement over vanilla LLMs and reaches 251% of OpenBLAS performance on RISC-V CPUs and 124% of cuBLAS performance on NVIDIA GPUs, while reducing development costs by 200× compared to human experts.

## Key Claims

- Uses LLMs to generate tensor operators with hardware primitives (assembly, intrinsics) from a one-line user prompt.
- Achieves up to 1291× performance improvement over vanilla LLMs on tensor operator generation.
- Reaches 251% of OpenBLAS performance on RISC-V CPUs (exact RISC-V platform not specified).
- Reaches 124% of cuBLAS performance on NVIDIA GPUs (exact GPU model not specified).
- Reduces development costs by 200× compared to manual implementation by human experts.
- Supports diverse hardware architectures including RISC-V, ARM, and GPUs without platform-specific manual optimization.
- Framework automatically tunes parameters for optimal performance across different hardware.

## Relationships

- [[mlir-xdsl-rvv-codegen-pipeline]]: Both QiMeng-TensorOp and the MLIR-xDSL RVV Code Generation Pipeline aim to automate generation of high-performance tensor operators on RISC-V platforms, but QiMeng-TensorOp uses LLMs to produce hardware-primitive code, while the MLIR-xDSL pipeline relies on custom compiler IR transformations and xDSL passes for code generation.
- [[c908-wino-gemm-optimization]]: QiMeng-TensorOp's claim of reaching 251% of OpenBLAS on RISC-V CPUs is directly relevant to hand-tuned library approaches like the SHL optimizations for the XuanTie C908; however, QiMeng-TensorOp aims for automatic cross-platform generation rather than per-platform manual tuning.

## Sources

- https://arxiv.org/html/2505.06302v1
