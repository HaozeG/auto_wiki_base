---
canonical_name: LLVM RISC-V Target
aliases:
- LLVM RISC-V backend
- RISC-V LLVM target
- RISCV target
subtype: null
tags:
- LLVM
- RISC-V
- compiler
toolchains:
- LLVM
scorecard:
  novelty_delta: 0.85
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.4
sources:
- raw/cache/a90c8f07c871fe68.md
- https://llvm.org/docs/RISCVUsage.html
source_url: https://llvm.org/docs/RISCVUsage.html
fetched_at: '2026-07-01T06:07:20.355874+00:00'
type: entity
created: '2026-07-01'
updated: '2026-07-01'
cold_start: false
inbound_links: 15
needs_summary_revision: false
outbound_links:
- target: llvm_ir
  reason: the Static Single Assignment intermediate representation that the LLVM RISC-V
    target lowers into machine code; the RISC-V backend consumes LLVM IR as its input
- target: llvm_rvv_ir_representation
  reason: the detailed scalable-vector-type model the RISC-V target uses specifically
    to represent and lower RVV code
- target: compiler_benchmark_bananapi_f3_gcc15_clang21
  reason: a benchmark comparing this LLVM/Clang RISC-V backend's autovectorization
    output against GCC on RVV hardware
- target: sifive_performance_p570_gen3
  reason: a contemporary out-of-order RISC-V core that relies on this LLVM RISC-V
    target (and GCC) for its software ecosystem
---

# LLVM RISC-V Target

LLVM RISC-V Target is the code generation backend for RISC-V processors within the LLVM compiler infrastructure. It aims to implement the most recent ratified versions of the RISC-V base ISAs and ISA extensions, with pragmatic variances from the specifications where necessary to maintain compatibility. As documented in the LLVM 23.0.0git User Guide for RISC-V Target, the backend fully supports RV32I and RV64I base ISAs, while RV32E and RV64E are supported only in assembly-based tools and remain experimental for compiler code generation. LLVM also provides support for a wide range of ratified extensions such as A, C, D, F, M, V, and many more, with statuses ranging from assembly only to full compiler support including C language intrinsics and pattern matching. Additionally, LLVM implements several RISC-V profiles (e.g., rva20, rva22, rva23, rvb23) that can be passed via `-march` to enable a set of required extensions. The backend also carries support for experimental extensions (prefixed with `experimental-`) to assist in the ratification process, although no compatibility is promised between toolchain versions. Starting from LLVM 19, the default atomics ABI mapping is "A6S", which is compatible with both the original "A6" and the future "A7" ABI. Known variances from the specification include unconditionally allowing instructions from zifencei, zicsr, zicntr, and zihpm without gating on the extensions being enabled, due to backwards compatibility concerns.

## Key Claims

- RV32I and RV64I are fully supported as base ISAs; RV32E and RV64E are supported only in assembly and are experimental for compiler use.
- Supported RISC-V profiles for `-march` include rvi20u32, rvi20u64, rva20u64, rva20s64, rva22u64, rva22s64, rva23u64, rva23s64, rvb23u64, and rvb23s64; unratified profiles require `-menable-experimental-extensions`.
- Ratified extensions A, B, C, D, F, M, Q, V, and many others (e.g., Zba, Zbb, Zbc, Zbs, Zca, Zcb, Zcd, Zcf, Zfa, Zfh, Zfhmin, Zfinx, Zihintpause, Zmmul, Ztso, Zvbb, Zvbc, Zvfh, Zvkb, Zvkg, Zvkn, Zvks, etc.) are supported at various levels: "Supported" (full compiler support including intrinsics and pattern matching), "Assembly Support" (only in assembler, disassembler, and related tools), or with noted limitations (e.g., missing pattern matching for cryptographic extensions like Zknd, Zkne; Zve32x/Zve32f require VLEN>=64 for compiler support).
- Experimental extensions currently supported include `experimental-p` (draft 0.21), `experimental-zibi` (0.1), `experimental-zicfilp` and `experimental-zicfiss` (1.0), `experimental-zvbc32e` and `experimental-zvkgs` (0.7), `experimental-svukte` (0.3), `experimental-zvdot4a8i` (0.1), and `experimental-zvqwdota8i`, `experimental-zvqwdota16i`, `experimental-zvfwdota16bf`, `experimental-zvfqwdota8f` (0.2).
- The atomics ABI defaults to "A6S" from LLVM 19 onward, which is compatible with the original "A6" and future "A7" ABIs; the ELF attribute for this mapping is not emitted by default due to a compatibility bug with older binutils.
- LLVM does not currently support multiple specification revisions but acknowledges a likely future need, deferring decisions until a concrete example of incompatible hardware/software changes arises.

## Relationships

- [[mlir_xdsl_rvv_gemm_codegen_recipe]] This optimization recipe uses the LLVM toolchain for RISC-V vector code generation, relying on the LLVM RISC-V target for RVV intrinsic support.
- [[llvm_ir]]: the Static Single Assignment intermediate representation that the LLVM RISC-V target lowers into machine code; the RISC-V backend consumes LLVM IR as its input.
- [[llvm_rvv_ir_representation]]: the detailed scalable-vector-type model the RISC-V target uses specifically to represent and lower RVV code.
- [[compiler_benchmark_bananapi_f3_gcc15_clang21]]: a benchmark comparing this LLVM/Clang RISC-V backend's autovectorization output against GCC on RVV hardware.
- [[sifive_performance_p570_gen3]]: a contemporary out-of-order RISC-V core that relies on this LLVM RISC-V target (and GCC) for its software ecosystem.

## Sources

- https://llvm.org/docs/RISCVUsage.html (LLVM 23.0.0git User Guide for RISC-V Target)
