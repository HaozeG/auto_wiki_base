---
canonical_name: RISC-V Sparse DNN FPGA Extensions
aliases:
- Hardware/Software Co-Design of RISC-V Extensions for Accelerating Sparse DNNs on
  FPGAs
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/9c9c870839bdf684.md
- https://arxiv.org/html/2504.19659v1
source_url: https://arxiv.org/html/2504.19659v1
fetched_at: '2026-07-02T05:45:43.823974+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# RISC-V Sparse DNN FPGA Extensions

The RISC-V Sparse DNN FPGA Extensions refer to a hardware/software co-design approach for accelerating deep neural networks containing semi-structured and unstructured sparsity on FPGAs. Proposed in a 2025 research paper from Friedrich-Alexander-Universität Erlangen-Nürnberg, the method leverages the fine-grained configurability of FPGAs to implement custom RISC-V instruction set extensions and corresponding functional units. For semi-structured sparsity, reserved bits encode sparsity information to skip computations, while unstructured sparsity is handled by a variable-cycle sequential multiply-and-accumulate unit that processes only non-zero weights. The design is benchmarked on TinyML applications including keyword spotting, image classification, and person detection, achieving speedups of up to 3× for unstructured, 4× for semi-structured, and 5× for combined sparsity, all while consuming minimal additional FPGA resources.

## Key Claims

- Unstructured sparsity accelerator provides speedups of up to a factor of 3 on TinyML benchmarks.
- Semi-structured sparsity accelerator provides speedups of up to a factor of 4.
- Combined design handling both sparsity types provides speedups of up to a factor of 5.
- The designs consume a small amount of additional FPGA resources, enabling acceleration even on small FPGAs.
- The RISC-V custom functional units are tightly coupled with the CPU and enabled through instruction set extensions.

## Relationships

- [[xuantie_c908]]: a RISC-V processor core with vector extension support; the FPGA-based extensions could complement or be compared against such custom functional units.
- [[k230]]: a RISC-V SoC integrating the C908 core; its architecture provides a relevant platform for evaluating sparse DNN acceleration techniques.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: a complementary approach that generates optimized GEMM micro-kernels for RISC-V vector engines, applicable to dense matrix operations in contrast to the sparse-focused extensions described here.

## Sources

- https://arxiv.org/html/2504.19659v1
