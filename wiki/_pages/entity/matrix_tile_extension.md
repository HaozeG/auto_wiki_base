---
canonical_name: Matrix Tile Extension (MTE)
aliases:
- MTE
- Matrix Tile Extension
subtype: null
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.8
  bridge_score: 0.7
  hub_potential: 0.8
sources:
- raw/cache/afaafe3db2d88bf6.md
- https://arxiv.org/html/2507.03522v1
source_url: https://arxiv.org/html/2507.03522v1
fetched_at: '2026-07-01T03:48:09.910417+00:00'
type: entity
created: '2026-07-01'
updated: '2026-07-01'
cold_start: true
inbound_links: 0
needs_summary_revision: false
---

# Matrix Tile Extension (MTE)

Matrix Tile Extension (MTE) is a proposed Instruction Set Architecture (ISA) extension for CPUs that accelerates General Matrix Multiplications (GEMMs) by completely decoupling the instruction set from the underlying microarchitecture. It seamlessly interacts with existing vector ISAs, such as RISC‑V Vector Extension and ARM SVE, and requires only six additional instructions and a 64‑bit Control Status Register (CSR) to manage state. MTE can vectorise GEMMs across all three inner dimensions (M, N, K), fully exploits the capacity of the existing vector register file for storing matrices in both uniform and mixed‑precision scenarios, and decouples the tile shape from the hardware implementation, allowing portable code that adapts to different microarchitectures without programmer intervention.

## Key Claims

- MTE is the first geometry‑agnostic matrix ISA that completely separates the ISA from the microarchitecture, enabling code portability across implementations.
- It requires only six new operations and a 64‑bit CSR, incurring minimal hardware overhead.
- It can vectorise GEMMs across the M, N, and K loops, leveraging the full capacity of the vector register file for matrix storage.
- MTE decouples the tile shape from the underlying hardware, avoiding static tile restrictions of prior matrix ISAs such as Intel AMX or ARM SME.
- It achieves an average speed‑up of 1.35× over the best state‑of‑the‑art matrix ISA (AMX) across a heterogeneous set of convolution and transformer workloads.
- Two microarchitectures supporting MTE are described: a lean extension of a long vector processor and a systolic‑array‑based design.

## Relationships

- MTE can accelerate GEMM kernels similar to the outer product kernel described in [[xuantie_c908_fp16_gemm_kernel]], providing a new ISA that could be targeted by such kernels.
- MTE could be a target for the MLIR/xDSL code generation pipeline documented in [[mlir_xdsl_rvv_gemm_codegen_recipe]], replacing or complementing direct RISC‑V Vector intrinsic generation.

## Sources

- https://arxiv.org/html/2507.03522v1
