---
cold_start: false
connected_entities:
- MLIR
- MLIR_software
- IREE
- APS_Framework
- SYCL_MLIR_Compiler
- TT-Forge
- Tenstorrent_Software_Stack
- tvmonriscv
- Seal5
- Gemmini_IREE_Integration_Strategy
created: 2026-06-29
inbound_links: 0
scorecard:
  bridge_score: 0.85
  contradiction_potential: 0.2
  cross_domain_connection: 0.9
sources:
- https://mlir.llvm.org/
- https://github.com/iree-org/iree
- https://github.com/llvm/torch-mlir
- https://github.com/ucb-bar/gemmini
- https://github.com/tenstorrent/tt-forge
synthesis_status: active
type: synthesis
updated: 2026-06-29
---

# MLIR for RISC-V AI Compilation

## RAG Summary

MLIR (Multi-Level Intermediate Representation), developed at Google in 2018 and merged into LLVM in 2019, has become the dominant infrastructure for building RISC-V AI compilers by enabling progressive lowering through user-defined dialects. Three distinct usage patterns appear across the RISC-V AI ecosystem: (1) IREE as an end-to-end ML compiler that lowers PyTorch/TensorFlow graphs to CPU, GPU, and RISC-V accelerator backends via MLIR's retargetable pipeline; (2) TT-Forge, Tenstorrent's compiler, which defines TTIR, TTNN, and TTKernel dialects and lowers AI workloads to Tensix RISC-V baby cores; and (3) APS Framework, a hardware-software co-design tool that uses MLIR to automate generation of RISC-V custom instruction extensions (ISAXs), synthesis RTL, and compiler support simultaneously. A fourth pattern is Seal5, which automates LLVM/MLIR backend patches from RISC-V ISA extension specifications, covering cases like the RVV vector dialect and future matrix extension lowering. The shared architectural insight is that MLIR dialects act as abstraction boundaries: high-level ML ops (linalg, tosa), tiled loop nests (affine, scf), and hardware-specific ops (TTKernel, Gemmini intrinsics) can coexist and be lowered incrementally. The main open question is whether the IREE → Gemmini integration path (via custom dialect + codegen plugin) can match hand-tuned DMA-scheduled performance on RISC-V vector and matrix accelerators.

---

## Full Synthesis

### MLIR as Universal AI Compiler Infrastructure

MLIR's key innovation is the dialect system: rather than a single fixed IR, each domain (ML frameworks, linear algebra, tensor tiling, hardware intrinsics) defines its own set of operations, types, and lowering passes. Dialects can be composed — a PyTorch model can be expressed in the `torch` dialect, progressively lowered through `linalg` → `affine` → `vector` → hardware-specific operations, with each stage applying domain-appropriate optimizations.

This makes MLIR the natural convergence point for RISC-V AI compilation because:
- **RVV vectorization** maps cleanly onto the MLIR `vector` dialect, which already has LLVM lowering infrastructure.
- **Custom accelerators** (Gemmini, Tensix, future RVM implementations) need only define a new dialect and a lowering pass from `linalg` or `tosa`.
- **ISA extension development** (Seal5, APS) can automate MLIR/LLVM backend patches from specification files.

### IREE → RISC-V Accelerator Path

IREE provides a retargetable compiler+runtime for ML workloads. Its standard CPU backend leverages the LLVM RISC-V backend and RVV autovectorization. For custom accelerators like Gemmini, the Gemmini-IREE integration strategy (see [[Gemmini_IREE_Integration_Strategy]]) proposes:
1. Add a `gemmini` dialect for tile-granularity matrix ops.
2. Insert a lowering pass from `linalg.matmul` tiling → `gemmini.tile_matmul`.
3. Use IREE's DMA scheduling infrastructure for scratchpad management.

The key challenge is that Gemmini's performance is highly sensitive to DMA pre-scheduling and scratchpad reuse — a general MLIR tiling approach may not match the hand-tuned `onnxruntime-riscv` baseline without custom codegen plugins.

### TT-Forge: MLIR in Production AI Hardware

TT-Forge is the most production-deployed MLIR-based compiler targeting RISC-V AI hardware. Its dialect hierarchy is:
```
TTIR (framework-independent tensor ops)
  → TTNN (operator library ops)
  → TTKernel (C++ kernel targeting RISC-V baby cores)
```
The TTKernel dialect generates C++ that runs directly on Tensix RISC-V baby cores, which is an unusual path — most accelerator backends target assembly or PTX. This demonstrates MLIR's flexibility for novel hardware that exposes a C/C++ programmable surface.

TT-Forge tests 800+ model variants in CI and is in public beta. See [[TT-Forge]] for compiler internals.

### APS: Closing the Hardware-Software Co-Design Loop

The APS Framework addresses a critical gap: when designing a new RISC-V custom instruction extension, the hardware (RTL), the ISA semantics, and the compiler backend must all be developed together. APS uses MLIR as the unified substrate to:
- Define the custom operation in an MLIR dialect.
- Synthesize RTL from the dialect via behavioral HLS.
- Generate LLVM/MLIR backend patches (instruction patterns, lowering rules) automatically.

This closes the loop that Seal5 partially addresses — Seal5 automates LLVM patches from ISA extension specs, while APS additionally covers hardware synthesis.

### Open Contradictions

- **SYCL-MLIR vs. OpenCL path:** The SYCL-MLIR approach (nested device code in host modules, SYCL dialect) is a research prototype, not production. Standard RISC-V accelerator backends use IREE or hand-written LLVM backends rather than SYCL. Whether the cross-module analysis benefits of SYCL-MLIR are worth the ecosystem cost is unresolved.
- **Compilation time vs. kernel performance:** MLIR-based compilers (IREE, TT-Forge) trade compilation time for portable performance. Against hand-tuned kernels (onnxruntime-riscv with Gemmini intrinsics, TT-Metalium C++ kernels), the gap on long-tail operators is unknown.

## Open Questions

1. Does IREE's CPU backend achieve comparable GEMM efficiency to onnxruntime-riscv on RVV hardware (same model, same chip)?
2. Can APS-generated RISC-V custom instruction backends match Seal5-generated ones in LLVM pattern matching quality?
3. What is TT-Forge compiler latency (time to first token) vs. TT-Metalium hand-tuned baseline on the same Wormhole hardware?
4. Is there a production IREE backend for any RISC-V matrix extension (RVM) hardware?

## Connected Pages

- [[MLIR]] — MLIR infrastructure overview
- [[MLIR_software]] — Wikipedia/encyclopedic entry with history and adoption
- [[IREE]] — end-to-end ML compiler and runtime
- [[APS_Framework]] — hardware-software co-design with MLIR for RISC-V
- [[SYCL_MLIR_Compiler]] — research SYCL dialect for cross-module optimization
- [[TT-Forge]] — production MLIR compiler for Tenstorrent Tensix RISC-V
- [[Tenstorrent_Software_Stack]] — TT-Forge in the broader stack context
- [[Seal5]] — automated LLVM backend generation from RISC-V ISA extension specs
- [[Gemmini_IREE_Integration_Strategy]] — proposed IREE codegen path for Gemmini
- [[tvmonriscv]] — TVM compilation workflow for RISC-V (pre-MLIR path)
