---
cold_start: false
constraints:
- RoCC interface
- RISC-V custom instructions
- Systolic array
created: '2025-10-23'
datatypes: []
evidence_strength: reported
hardware_targets:
- Gemmini (systolic array GEMM accelerator)
inbound_links: 1
metrics: []
needs_summary_revision: false
scorecard:
  bridge_score: 0.8
  claim_density: 0.5
  hub_potential: 0.7
  novelty_delta: 0.8
  self_containedness: 0.6
sources:
- https://github.com/ucb-bar/merlin/issues/2
tags:
- Gemmini
- IREE
- RoCC
- integration
- systolic array
- compiler
toolchains:
- IREE
- buddy-mlir
- LLVM
- GNU gcc
- riscv64-unknown-linux-gnu-gcc
- CMake
type: optimization_recipe
updated: '2026-06-29'
workloads:
- linalg.matmul
- matrix multiplication
---

# Gemmini IREE Integration Strategy

This optimization recipe describes two strategies for integrating the Gemmini RoCC accelerator with the IREE compiler and runtime. The objective is to compile linalg operations (e.g., linalg.matmul) to utilize the Gemmini systolic array via RISC-V RoCC custom instructions. Path 1 (Linker-Level) treats the Gemmini kernel as an external C function, compiled separately and linked against the IREE module. Path 2 (Compiler-Level) integrates the buddy-mlir Gemmini dialect natively, teaching IREE to generate Gemmini instructions. Both paths avoid modifying IREE's internal LLVM for path 1 but require patching IREE's forked LLVM for path 2. The recipe is derived from the Merlin repository issue tracker and is currently at the planning stage; no performance measurements have been published.

## Key Claims

- Two primary integration strategies exist: a linker-level shim approach (Path 1) and a compiler-level dialect integration (Path 2).
- Path 1 uses IREE's hal.executable and hal.dispatch mechanisms to call a pre-compiled C library (libgemmini_shim.a) that contains Gemmini RoCC instructions.
- Path 2 integrates the buddy-mlir Gemmini dialect into IREE, requiring patches to IREE's llvm-project to recognize custom llvm.riscv.* intrinsics.
- Path 2 enables native fine-grained optimizations and code generation within IREE, while Path 1 requires only an external toolchain (riscv64-unknown-linux-gnu-gcc).

## Transformation

### Path 1: Custom Dispatch (Linker-Level Shim)
- **Prerequisites**: IREE compiler with embedded-elf backend; riscv64-unknown-linux-gnu-gcc toolchain that understands `.insn r` for RoCC instructions; Gemmini headers (include/gemmini.h, include/gemmini_nn.h).
- **Steps**:
  1. Create a static C library (libgemmini_shim.a) with wrapper functions (e.g., gemmini_matmul_os_shim) that call Gemmini tiled_matmul_os kernels, exposing a stable C ABI.
  2. Define an IREE HAL MLIR module that declares the external C function using `func.func private`, implements the hal.executable.export logic to extract raw buffer pointers from hal.buffer_view, and calls the imported function.
  3. Compile the MLIR module to a static library using iree-compile with the embedded-elf backend.
  4. Link the IREE-generated library, libgemmini_shim.a, and a C main() harness into a final ELF executable using riscv64-unknown-linux-gnu-gcc.
  5. Execute the final ELF on Spike with `spike --extension=gemmini pk ...`.
- **Expected Effect**: Enables Gemmini-accelerated matmul within IREE without modifying any IREE compiler internals.
- **Failure Modes**: Not documented; assumes correct ABI alignment and availability of Gemmini functional simulator.
- **Measurements**: None reported.

### Path 2: Full MLIR Dialect Integration (Compiler-Native)
- **Prerequisites**: IREE repository fork; buddy-mlir backend source; patching skills for LLVM CMake and RISCV.td; Apache 2.0 license compliance for buddy-mlir.
- **Steps**:
  1. Create a patch-set directory (e.g., //patches/llvm-gemmini) within the IREE repository.
  2. Cherry-pick .td files from buddy-mlir backend (IntrinsicsRISCVBuddyExt.td, RISCVBuddyExt.td, RISCVInstrInfoBuddyExt.td) and create diffs for CMakeLists.txt and RISCV.td to include +buddyext target feature.
  3. Apply the patch set to third_party/llvm-project before LLVM compilation.
  4. Integrate buddy-mlir Gemmini dialect source code (GemminiDialect.cpp, Gemmini.td) into the IREE build system.
  5. Integrate lowering passes (convert-linalg-to-gemmini, lower-gemmini) into IREE's pass registry.
  6. Integrate the MLIR-to-LLVMIR translation interface (GemminiToLLVMIRTranslation.cpp).
  7. Define a new IREE compilation pipeline that inserts the Gemmini lowering passes after linalg bufferization and passes target features +buddyext to the patched LLVM backend.
- **Expected Effect**: IREE can natively generate Gemmini RoCC instructions from linalg operations, enabling fine-grained optimizations.
- **Failure Modes**: Not documented; requires careful integration to avoid build breakage.
- **Measurements**: None reported.

## Relationships

- [[Gemmini_Architecture]] – Overview of the Gemmini hardware generator and its full-stack DNN acceleration capabilities.
- [[Gemmini_systolic_array_GEMM_accelerator]] – Detailed hardware target page covering the systolic array GEMM accelerator, RoCC interface, and software stack.

## Sources

- [GitHub Issue: [gemmini] [dispatch] [dialect] Integrate Gemmini RoCC Accelerator Support into IREE](https://github.com/ucb-bar/merlin/issues/2)
