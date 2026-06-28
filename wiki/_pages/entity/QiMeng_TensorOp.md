---
cold_start: true
created: '2026-07-02'
inbound_links: 1
needs_summary_revision: false
scorecard:
  bridge_score: 0.8
  claim_density: 0.9
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.7
sources:
- https://arxiv.org/html/2505.06302v1
tags:
- tensor operator
- LLM
- auto-generation
- hardware primitive
- GEMM
- convolution
type: entity
updated: '2026-06-28'
---

# QiMeng-TensorOp

QiMeng-TensorOp is an LLM-based framework for automatically generating high-performance tensor operators with hardware primitives across diverse hardware platforms including RISC-V, ARM, and NVIDIA GPUs. The framework requires only a one-sentence user prompt describing the target operator and hardware, then uses general hardware optimization hints to guide LLMs in comprehending hardware characteristics and extracting relevant factors from hardware manuals. It generates sketch and kernel code with hardware primitives and employs an LLM-assisted Monte Carlo Tree Search (MCTS) algorithm for performance tuning. QiMeng-TensorOp achieves significant performance improvements over vanilla LLM prompts (up to 1291x) and can match or exceed human-optimized libraries like OpenBLAS (251% on RISC-V CPUs) and cuBLAS (124% on NVIDIA GPUs), while reducing development costs by an estimated 200x compared to human experts.

## Key Claims

- First end-to-end framework to automatically generate hardware-primitive-level tensor operators using LLMs.
- Requires only a one-line user prompt; no manual specification of hardware details.
- Uses general hardware intrinsic optimization hints to help LLMs understand hardware and extract information from manuals.
- Implements LLM-assisted MCTS for efficient tuning of generated code.
- Achieves up to 1291x performance improvement over vanilla LLM prompts.
- Achieves up to 251% of OpenBLAS performance on RISC-V CPUs and 124% of cuBLAS on NVIDIA GPUs.
- Reduces development costs by 200x compared to senior human developers.

## Relationships

- [[TVM_and_Gemmini_Accelerator_Benchmark_Results]] – Both are auto-generation frameworks for tensor operators; QiMeng leverages LLMs while TVM uses tuning and auto-scheduling.
- [[GEMM_with_RISC-V_Vector_Extension]] – A GEMM kernel implementation using RISC-V vector extension; QiMeng can automatically generate such kernels and potentially outperform them.

## Sources

- [arXiv:2505.06302v1](https://arxiv.org/html/2505.06302v1)

