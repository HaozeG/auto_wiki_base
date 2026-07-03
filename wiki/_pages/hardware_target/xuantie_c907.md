---
canonical_name: XuanTie C907
aliases:
- C907
- T-Head XuanTie C907
- XuanTie C907 processor
- XuanTie C907 with MME
subtype: null
tags:
- risc-v
- matrix-extension
- mme
- xuantie
- t-head
- ai
hardware_targets:
- XuanTie C907
toolchains: []
constraints:
- RLEN configurable (128, 256, or 512 bits)
- Eight two-dimensional matrix registers
- Peak computational power 0.5–32 TOPS
- Supported data types: fp32, fp16, bf16, int8, int4
- Data reuse rate of 2
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/44518bfe83043748.md
- https://riscv.org/blog/2024/11/enhancing-the-future-of-ai-ml-with-attached-matrix-extension/
source_url: https://riscv.org/blog/2024/11/enhancing-the-future-of-ai-ml-with-attached-matrix-extension/
fetched_at: '2026-07-02T03:42:26.515909+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 3
needs_summary_revision: false
outbound_links:
- target: xuantie_c908
  reason: a different XuanTie core that relies on the RISC-V Vector Extension; the
    C907 offers an alternative matrix-oriented path
- target: rvme
  reason: a research matrix engine design also aligned with the AME proposal; both
    explore decoupled matrix acceleration for RISC-V
- target: xuantie_c908_fp16_gemm_kernel
  reason: a vector-based GEMM kernel on the C908 provides a contrast to the matrix-based
    approach on the C907
---

# XuanTie C907

The XuanTie C907 is a RISC-V processor core developed by T-Head Semiconductor (Alibaba DAMO Academy) that implements the XuanTie Matrix-Multiply Extension (MME), a decoupled matrix extension designed for AI/ML matrix operations. It is the first XuanTie IP to integrate this matrix acceleration, offering scalable computational power from 0.5 TOPS to 32 TOPS by selecting different RLEN (register length) parameters (128, 256, or 512 bits). The core decouples matrix computations from the RISC-V Vector Extension (RVV), using independent matrix registers and its own instruction set for matrix multiply-accumulate, memory access, and configuration. It supports a range of data types including float32, float16, bfloat16, int8, and int4, with expanded precision for multiply-accumulate operations (e.g., accumulating bfloat16/float16 into float32, int8 into int32). The MME architecture also provides streaming load/store instructions for efficient data access and whole matrix register operations for context switching.

## Key Claims

- Peak computational power scalable from 0.5 TOPS to 32 TOPS by selecting different RLEN or execution throughput parameters.
- Decoupled matrix and vector extensions allow independent scaling and parallel execution of matrix and vector operations.
- Supports data types fp32, fp16, bf16, int8, int4 with expanded precision (2x for float, 4x for integer) during multiply-accumulate.
- Achieves data reuse rate of 2 for operands A and B, reducing memory bandwidth requirements.
- Eight two-dimensional matrix registers, with the recommended configuration using four as accumulation registers.
- RLEN configurable at implementation time (128, 256, 512 bits or higher) for area/performance trade-offs.
- Provides streaming load/store instructions (msld/msst) for optimized data access patterns.
- Whole matrix register load/store instructions (mld<1/2/4/8>m, mst<1/2/4/8>m) for fast context switching.
- Includes matrix addition and other element-wise operations beyond multiply-accumulate.
- First XuanTie IP to implement the MME.

## Optimization-Relevant Details

- ISA/profile: RISC-V with XuanTie MME custom extension; follows the Attached Matrix Extension (AME) design principles.
- Vector/matrix/accelerator support: MME with 8 matrix registers, RLEN configurable, peak 0.5–32 TOPS, decoupled from vector unit.
- Memory/cache/TLB/DMA: Not disclosed in the source.
- Compiler/toolchain support: Not specified; software development requires MME-aware toolchain support.

## Relationships

- [[xuantie_c908]]: a different XuanTie core that relies on the RISC-V Vector Extension; the C907 offers an alternative matrix-oriented path.
- [[rvme]]: a research matrix engine design also aligned with the AME proposal; both explore decoupled matrix acceleration for RISC-V.
- [[xuantie_c908_fp16_gemm_kernel]]: a vector-based GEMM kernel on the C908 provides a contrast to the matrix-based approach on the C907.

## Sources

- https://riscv.org/blog/2024/11/enhancing-the-future-of-ai-ml-with-attached-matrix-extension/
