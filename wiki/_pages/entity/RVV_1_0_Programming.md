---
cold_start: true
created: '2026-06-11'
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.4
  hub_potential: 0.5
  novelty_delta: 0.6
  self_containedness: 0.9
sources:
- https://lucaberton.com/blog/risc-v-vector-extension-rvv-programming/
tags:
- RVV
- vector programming
- RISC-V
- VLA
type: entity
updated: '2026-06-28'
---

# RISC-V Vector Programming with RVV 1.0

RISC-V Vector Programming with RVV 1.0 is a programming model for RISC-V processors that implements the ratified vector extension version 1.0. Unlike traditional SIMD instruction sets such as x86 AVX or ARM NEON, which bake the vector register width into the ISA and require kernel rewrites for wider hardware, RVV adopts a vector-length-agnostic (VLA) approach where the software queries the hardware at runtime for the number of elements it can process per iteration. This is accomplished via the vsetvli instruction, which sets the vector length based on the requested element width (SEW) and LMUL grouping, and returns the granted length. The core loop pattern, known as stripmining, processes the data in chunks determined by the hardware's capability, making the same binary portable across implementations ranging from 128-bit to multi-kilobit vector registers. The model is particularly relevant for AI and HPC workloads where binary compatibility across hardware generations reduces the software maintenance burden. The RISC-V ecosystem includes auto-vectorizing compilers (GCC and Clang) and intrinsic headers (riscv_vector.h) that allow developers to write vector code without dropping to assembly.

## Key Claims

- RVV 1.0 uses a vector-length-agnostic (VLA) model instead of fixed-width SIMD.
- The vsetvli instruction sets the runtime vector length based on requested SEW and LMUL.
- Stripmining is the required loop pattern for VLA processing.
- The same binary runs on 128-bit and multi-kilobit implementations without recompilation.
- GCC and Clang auto-vectorize for RVV with the `-march=rv64gcv` flag.
- Intrinsic functions from `riscv_vector.h` provide assembly-like control in C.
- LMUL selection (m1 to m8) trades throughput for register usage.
- vfmacc fused multiply-add offers improved accuracy and throughput.
- Tail elements are handled naturally without a separate cleanup loop.
- QEMU can emulate RVV 1.0 for development without hardware (e.g., `-cpu rv64,v=true,vlen=128`).
- The SpacemiT K1 in the Banana Pi BPI-F3 is a shipping RVV 1.0 board.

## Relationships

- [[Gemmini_systolic_array_GEMM_accelerator]] – Both are RISC-V acceleration approaches: Gemmini uses a dedicated systolic array while this page covers the vector extension programming model.
- [[SiFive_P550_and_T-HEAD_C910_Benchmark_Comparison]] – That page discusses vector extension support in the C910 core and performance implications of the ecosystem gap, providing context for RVV adoption.

## Sources

- [RISC-V Vector Programming with RVV 1.0 | Luca Berton](https://lucaberton.com/blog/risc-v-vector-extension-rvv-programming/)
