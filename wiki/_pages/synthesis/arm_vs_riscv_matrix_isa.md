---
type: synthesis
connected_entities: [arm_sme, arm_sme2, arm_sve2, risc_v_matrix_extensions, risc_v_vector_extension, rva23_profile]
synthesis_status: draft
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  bridge_score: ~
  contradiction_potential: ~
  cross_domain_connection: ~
---

# ARM SME vs RISC-V Matrix Extensions: ISA Design Divergence

## RAG Summary

ARM SME (Scalable Matrix Extension) and the RISC-V matrix extension proposals (IME/VME/AME) represent two competing ISA philosophies for accelerating GEMM-class workloads directly inside general-purpose CPU cores, without a dedicated discrete accelerator. Both share the core idea of a 2D tile storage register that accumulates outer products of vectors, giving throughput that scales as the square of the vector length rather than linearly. ARM SME, introduced with Armv9-A, places the ZA tile storage in-core alongside the SVE2 Z register file, activated through a "Streaming SVE mode" context switch (SMSTART/SMSTOP). The RISC-V AME proposal takes a structurally similar approach: a tile register file (TR) accumulates outer products of RISC-V vector operands, with instructions analogous to SME's FMOPA. The key architectural divergence is standardisation pace and ecosystem lock-in: ARM SME is shipping silicon in the ARM Cortex-X925, AWS Graviton5, and Apple M4 (Armv9.2–9.4 family), while RISC-V's matrix extensions (IME, VME, AME) remain in the community proposal stage under the RISC-V International architecture review process as of mid-2026. ARM's VLA model — inherited from SVE2 — means the same binary runs on SME implementations from 128-bit to 2048-bit SVL, a property directly mirrored in RISC-V RVV's VLEN-agnostic model. A practical distinction is SME2's 512-bit ZT0 lookup table register, which has no current RISC-V counterpart, providing hardware acceleration for INT4/INT8 dequantization that matters significantly for large language model inference.

---

## Full Synthesis

### Shared Design Hypothesis

Both ARM SME and the RISC-V matrix extension proposals (primarily AME — Advanced Matrix Extension — and IME — Integer Matrix Extension) rest on the same architectural bet: that the GEMM outer-product loop is frequent enough and bandwidth-sensitive enough to justify dedicated in-core 2D storage and accumulation hardware, rather than offloading to a separate accelerator (as Gemmini does via RISC-V RoCC) or a discrete GPU.

The outer-product pattern `C[i][j] += A[i][k] * B[k][j]` appears in transformer attention, convolutions via im2col, and classical BLAS DGEMM. When the tile fits in the on-chip ZA register (SME) or tile register file (RISC-V AME), the data for a full tile-block multiply is fetched once and reused multiple times — reducing pressure on L1/L2 bandwidth and allowing higher sustained compute utilisation.

### Structural Parallels

| Feature | ARM SME/SME2 | RISC-V AME (proposal) |
|---|---|---|
| Tile storage | ZA (SVL×SVL bytes) | TR (VLEN×VLEN bits) |
| Vector operand source | SVE2 Z registers | RVV V registers |
| Outer-product instruction | FMOPA, SMOPA, UMOPA | MOPA variants (proposed) |
| Activation mode | Streaming SVE mode (SMSTART) | Normal execution (no mode switch in current proposals) |
| Lookup table | ZT0 (512-bit, SME2) | No equivalent yet |
| Shipping silicon | Cortex-X925, Graviton5, Apple M4 | None as of 2026 |

### Key Difference: Mode Switch vs. Unified Execution

ARM SME requires entering "Streaming SVE mode" before ZA and most SME instructions are accessible. This is a context-switch-like operation: the SVL may change, Z/P registers are zeroed, and normal SVE2 instructions execute at the streaming SVL. This design isolates the matrix-acceleration state from normal code, simplifying out-of-order speculative execution (no tile state to snapshot on mispredict), but introduces entry/exit overhead.

Current RISC-V AME proposals aim to keep matrix instructions available in the same execution context as RVV, without a mode switch. This avoids the entry/exit cost but creates more complex microarchitectural state for speculative execution pipelines to manage.

### Standardisation Asymmetry

ARM SME's standardisation timeline was controlled internally by Arm and moved from announcement (2021) to mandatory Armv9.2 silicon (Cortex-X925, Graviton5) in roughly 3 years. The RISC-V matrix extension proposals have been debated since approximately 2020, with multiple competing specifications (IME, VME, AME) still under review in 2026 — a consequence of RISC-V International's consensus-driven, open process. The RVA23 profile mandates RVV 1.0 but does not include any matrix extension, reflecting that no single matrix proposal has achieved ratification.

### Open Questions

- Will a RISC-V matrix extension be ratified before 2028, and if so, which of IME/VME/AME will prevail?
- Does SME2's mode-switch overhead (SMSTART/SMSTOP) constitute a significant cost for inference workloads with fine-grained kernel calls, or is it amortised over large tile operations?
- Apple's decision to implement SME/SME2 while skipping standard SVE2 in normal mode suggests a strong preference for the matrix-oriented model — does this imply SVE2 will see diminishing relative importance for ML workloads?
- Does the RISC-V AME tile register file (quadratic in VLEN) create unreasonable area overhead for small embedded cores where VLEN = 128 bits?

## Connected Pages

- [[arm_sme]] — Primary ARM entity page for the Scalable Matrix Extension
- [[arm_sme2]] — SME2 multi-vector and lookup table extensions
- [[arm_sve2]] — The SVE2 vector ISA that SME's Streaming SVE mode is built upon
- [[risc_v_matrix_extensions]] — RISC-V IME/VME/AME proposals
- [[risc_v_vector_extension]] — RISC-V RVV 1.0, analogue to SVE2 on the RISC-V side
- [[rva23_profile]] — RISC-V application profile mandating RVV 1.0 but not yet any matrix extension
- [[gemmini]] — Alternative approach: GEMM acceleration as a decoupled RoCC coprocessor
