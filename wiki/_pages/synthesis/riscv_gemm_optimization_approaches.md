---
type: synthesis
connected_entities:
- mlir_xdsl_rvv_gemm_codegen_recipe
- opengemm
- generic_micro_kernel_templates_gemm
- xuantie_c908_fp16_gemm_kernel
synthesis_status: draft
sources:
- wiki/_pages/optimization_recipe/mlir_xdsl_rvv_gemm_codegen_recipe.md
- wiki/_pages/entity/opengemm.md
- wiki/_pages/optimization_recipe/generic_micro_kernel_templates_gemm.md
- wiki/_pages/workload_kernel/xuantie_c908_fp16_gemm_kernel.md
created: 2026-07-02
updated: 2026-07-02
cold_start: true
inbound_links: 4
scorecard:
  bridge_score: 0.85
  contradiction_potential: 0.3
  cross_domain_connection: 0.75
needs_summary_revision: false
---

# Compiler-Generated vs. Hand-Tuned vs. Hardware-Accelerated GEMM on RISC-V

## RAG Summary

Four approaches to producing high-performance GEMM kernels on RISC-V and adjacent SIMD architectures compete without a documented head-to-head comparison: the MLIR+xDSL Lowering Pipeline compiler-generates RVV-intrinsic C code from a GotoBLAS-style macro-kernel, reaching 12.2 GFLOPS (10-35% over OpenBLAS) on K230 and BananaPi F3 with no hand-tuning; the XuanTie C908 FP16 GEMM Outer Product Kernel is the opposite extreme, a fully hand-scheduled 16x12 register-blocked assembly kernel exploiting C908-specific instruction fusion; OpenGeMM abandons software optimization entirely and instead generates dedicated Chisel hardware, claiming 3.58x to 16.40x speedup over the Gemmini accelerator baseline; and the cross-architecture Template-Based Micro-kernel Generation approach shows the same compiler-driven idea as the MLIR+xDSL pipeline but for ARM Neon, ARM SVE, and Intel AVX512 rather than RISC-V, proving the technique generalizes beyond one ISA. This is a genuine unresolved comparison, not merely four complementary tools: none of the four has been benchmarked against the other three on identical hardware and matrix shapes, so no source in this wiki can currently say whether RISC-V compiler-generated GEMM (MLIR+xDSL), hand-tuned assembly (XuanTie C908 kernel), or dedicated hardware generation (OpenGeMM) delivers the best FLOPS-per-engineering-hour or FLOPS-per-watt on RISC-V specifically.

---

## Full Synthesis

GEMM is the single most-optimized kernel in this wiki, and the RISC-V ecosystem currently has at least three structurally different answers to "how do you make it fast," plus one non-RISC-V comparison point that shows the compiler-generation idea is portable.

**Compiler-generated, no hand-tuning ([[mlir_xdsl_rvv_gemm_codegen_recipe]]).** This pipeline bridges a gap in MLIR's own lowering paths by adding custom xDSL dialects and transformation passes that translate high-level tensor operations into RVV-intrinsic C code — automatically, following a GotoBLAS-style macro-kernel structure. The output, when dropped into a Goto-style GEMM, beats OpenBLAS by 10-35% (up to 12.2 GFLOPS) on both the K230 and BananaPi F3, and the same pipeline can generate a full family of micro-kernel variants tuned per-layer for models like BERT-Large. The entire appeal is that no RVV assembly is hand-written: the compiler infrastructure does the register blocking, intrinsic selection, and tile sizing.

**Fully hand-tuned assembly ([[xuantie_c908_fp16_gemm_kernel]]).** T-Head's own SHL library takes the opposite approach for the XuanTie C908: a hand-scheduled FP16 outer-product kernel using a 16x12 register tile, vector loads for weights (`vle`) and scalar loads for activations (`flh`), with manual instruction scheduling to eliminate read-after-write and write-after-write hazards, further pipelined by the C908's instruction-fusion hardware. This kernel is the computational core of SHL's im2col+GEMM and Winograd convolution paths — it is production code, not a research prototype, and its performance ceiling comes from exploiting C908-specific microarchitectural features (instruction fusion) that a general compiler pipeline like MLIR+xDSL would need explicit target-specific knowledge to replicate.

**Dedicated hardware generation instead of a software kernel ([[opengemm]]).** OpenGeMM rejects the premise that GEMM should run as software on a general-purpose vector unit at all. It is a parameterized, Chisel-coded GeMM accelerator paired with a lightweight RISC-V control processor and a tightly-coupled multi-banked scratchpad, targeting extreme-edge devices where neither a full vector pipeline nor a general accelerator like Gemmini is efficient enough. Its reported 3.58x-16.40x speedup over Gemmini and 4.68 TOPS/W efficiency come from configuration pre-loading, input pre-fetching with output buffering, and programmable strided memory access — techniques aimed at maximizing hardware utilization (81.89%-99.34% measured) rather than compiler cleverness.

**The same compiler-generation idea, proven portable, but not on RISC-V ([[generic_micro_kernel_templates_gemm]]).** This approach is architecturally the closest relative of the MLIR+xDSL pipeline — a generic, macro-parameterized micro-kernel template (tile dimensions m_r x n_r plus architecture-specific intrinsic mappings) integrated into the BLIS macro-kernel framework — but it targets ARM Neon, ARM SVE, and Intel AVX512, not RISC-V RVV, and was measured on NVIDIA Carmel, Fujitsu A64FX, and AMD EPYC 7282 rather than any RISC-V board. Its relevance to the RISC-V approaches above is as an existence proof: template-based, intrinsics-level micro-kernel generation is known to match hand-tuned BLIS/AOCL/ARMPL performance on three unrelated SIMD ISAs, which is indirect evidence (not direct proof) that the same class of technique used by MLIR+xDSL could, in principle, close the gap with hand-tuned RVV assembly like the XuanTie C908 kernel — if someone built the RVV-specific intrinsic mapping this template approach requires.

No page in this wiki reports these four approaches benchmarked against each other on the same hardware, same matrix shapes, and same datatype. The MLIR+xDSL pipeline's 10-35%-over-OpenBLAS figure, the XuanTie C908 kernel's un-quantified "outer-product acceleration for SHL convolution," and OpenGeMM's 3.58x-16.40x-over-Gemmini figure are three different baselines, making it impossible to currently rank the three RISC-V-specific approaches by raw throughput — only by design philosophy (compiler-automated vs. hand-tuned vs. dedicated-silicon).

## Open Questions

- Has anyone run the MLIR+xDSL-generated kernel and the XuanTie C908 hand-tuned kernel on the same C908 hardware, with the same matrix shapes and datatype (fp16 vs. fp32), to get a direct compiler-vs-hand-tuning comparison rather than two separate baselines?
- OpenGeMM's comparison baseline is Gemmini, not a software RVV kernel — would OpenGeMM's dedicated-hardware approach still show a large speedup if compared against the MLIR+xDSL-generated software kernel running on a similarly-provisioned RISC-V core, or is most of its advantage specific to beating Gemmini's dataflow?
- Could the ARM/x86 template-based intrinsic-mapping technique in [[generic_micro_kernel_templates_gemm]] be directly ported to add an RVV intrinsic mapping, effectively merging it with the MLIR+xDSL pipeline's goals — and if so, would it match or exceed the xDSL-based approach's 10-35% OpenBLAS speedup?
- Does the XuanTie C908's instruction-fusion advantage (exploited by the hand-tuned kernel) represent a class of microarchitectural optimization that compiler-generated approaches structurally cannot capture without vendor-specific compiler backend support, or is it a solvable code-generation problem?

## Connected Pages

- [[mlir_xdsl_rvv_gemm_codegen_recipe]]
- [[opengemm]]
- [[generic_micro_kernel_templates_gemm]]
- [[xuantie_c908_fp16_gemm_kernel]]
