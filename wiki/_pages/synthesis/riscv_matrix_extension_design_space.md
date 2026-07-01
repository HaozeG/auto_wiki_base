---
type: synthesis
connected_entities:
- integrated_matrix_extension
- matrix_tile_extension
- riscv_matrix_extension_proposal
- riscv_vector_extension
- rvme
- llvm_riscv_target
synthesis_status: draft
sources:
- wiki/_pages/entity/integrated_matrix_extension.md
- wiki/_pages/entity/matrix_tile_extension.md
- wiki/_pages/entity/riscv_matrix_extension_proposal.md
- wiki/_pages/entity/riscv_vector_extension.md
- wiki/_pages/hardware_target/rvme.md
- wiki/_pages/entity/llvm_riscv_target.md
created: 2026-07-01
updated: 2026-07-01
cold_start: true
inbound_links: 0
scorecard:
  bridge_score: 0.85
  contradiction_potential: 0.7
  cross_domain_connection: 0.75
needs_summary_revision: true
---

# Competing Approaches to Matrix Acceleration on RISC-V

## RAG Summary

Three unratified RISC-V matrix-acceleration ISA proposals compete for the same GEMM-acceleration niche without interoperating: the Integrated Matrix Extension (IME) reuses the 32 existing Vector Extension registers with no new architected state, Matrix Tile Extension (MTE) adds only 6 instructions and a single 64-bit CSR while staying decoupled from any specific vector ISA (portable to RISC-V RVV or ARM SVE alike), and the RISC-V Matrix Specification Proposal (v0.6.0) instead defines 8 dedicated tile/accumulator registers and 8 new CSRs as fully separate architected state. This is a genuine unresolved contradiction, not a gap awaiting one obvious answer: IME and the v0.6.0 proposal take opposite positions on whether matrix acceleration needs new register state at all, while MTE explicitly optimizes for cross-vendor, cross-ISA portability that neither of the other two targets. None of the three is ratified or has shipping silicon; the RVV-based RVME research coprocessor and production RVV cores such as the XuanTie C908 instead build outer-product GEMM kernels directly on today's ratified RISC-V Vector Extension, without depending on any of the three proposals. LLVM's RISC-V backend tracks only ratified and experimental-but-accepted extensions, so it currently provides no code generation path for any of the three, meaning adoption of any one design would first require both RISC-V International ratification and a new LLVM/GCC backend before compilers could target it.

---

## Full Synthesis

RISC-V has no single, ratified answer to "how should a CPU accelerate matrix multiplication," and the wiki's coverage of the current design space surfaces three structurally different, mutually incompatible proposals rather than one emerging standard.

**No new state (IME).** The Integrated Matrix Extension treats the 32 vector registers defined by RVV as the only storage matrix operations need. A packed-panel micro-kernel template (parameterized by tile dimensions µ, ν, Λ and datatype) is expressed through a handful of intrinsics — `__riscv_vmzeroacc`, `__riscv_v{f}mmacc` — that accumulate outer products entirely within existing vector register space. The appeal is minimal hardware cost: any RVV-capable core is, in principle, one microcode/decoder change away from supporting IME.

**Fully decoupled, minimal-state (MTE).** Matrix Tile Extension goes further in the opposite direction on *portability* while converging with IME on *minimal new state*: it adds just 6 instructions and one 64-bit CSR, and is explicitly designed to sit on top of either RISC-V RVV or ARM SVE without modification, vectorizing GEMM across all three inner dimensions (M, N, K) using whatever vector register file the host ISA already provides. Where IME is RISC-V-specific and reuses V registers directly, MTE is vendor/ISA-agnostic by design.

**Dedicated architected state (RISC-V Matrix Specification Proposal v0.6.0).** The most structurally different proposal rejects the "reuse the vector file" premise entirely: it defines 4 Tile Registers and 4 Accumulation Registers as new architected state, sized by three implementation-defined constants (ELEN, TLEN, TRLEN), with 8 dedicated CSRs including a self-describing feature bitmap (`xmisa`). This buys implementations more freedom to size matrix hardware independently of the vector datapath, at the cost of being the most invasive change to the register file of the three.

**What's actually shipping.** None of these three proposals has ratified status or a documented compiler backend in [[llvm_riscv_target]] — the LLVM RISC-V target's documented extension support (RV32I/RV64I base plus ratified extensions like V, A, C, D, F, M and named profiles like rva23) does not list IME, MTE, or the v0.6.0 matrix proposal. Real matrix acceleration on RISC-V today instead happens directly on top of ratified RVV: [[rvme]]'s Outer Product Array coprocessor and the XuanTie C908's outer-product GEMM kernel both build custom hardware/software matrix paths on the existing [[riscv_vector_extension]] rather than waiting on any of the three extension proposals. This means the wiki's hardware_target pages (RVME, XuanTie C908) and its matrix-ISA entity pages (IME, MTE, RISC-V Matrix Specification Proposal) currently describe two disconnected tracks of the same problem: what ships now versus what's being proposed for later ratification.

## Open Questions

- Which, if any, of IME, MTE, or the v0.6.0 proposal will RISC-V International actually ratify — and would ratification obsolete RVME-style direct-RVV matrix engines, or would they coexist as a "fast path" versus "portable path" the way scalar and vector ISA extensions currently do?
- No source in this wiki documents a compiler (LLVM or GCC) backend targeting IME, MTE, or the v0.6.0 proposal; without one, none of the three can be evaluated on real workloads the way RVV-based approaches already have been (see [[mlir_xdsl_rvv_gemm_codegen_recipe]]).
- Does MTE's cross-ISA portability claim (RISC-V RVV and ARM SVE from one instruction set) hold up under an actual dual-ISA implementation, or does it degrade to two separate lowering paths in practice?
- [[rvismith_fuzzer_rvv_intrinsics]] found 13 previously-unknown compiler bugs in existing RVV intrinsic handling across GCC/LLVM/XuanTie; it is an open question whether a new matrix-extension backend would inherit or compound this class of compiler-correctness risk.

## Connected Pages

- [[integrated_matrix_extension]]
- [[matrix_tile_extension]]
- [[riscv_matrix_extension_proposal]]
- [[riscv_vector_extension]]
- [[rvme]]
- [[llvm_riscv_target]]
