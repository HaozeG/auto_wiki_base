---
cold_start: false
connected_entities:
- IREE
- ncnn
- onnxruntime-riscv
- ONNX_Runtime_Build_for_Inferencing
- llama-cpp-mini
- tvmonriscv
- GEMM_with_RISC-V_Vector_Extension
- QiMeng_TensorOp
- XuanTie_GNU_Toolchain
- Seal5
created: 2026-06-29
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: 0.85
  contradiction_potential: 0.6
  cross_domain_connection: 0.9
sources:
- wiki/_pages/entity/IREE.md
- wiki/_pages/entity/ncnn.md
- wiki/_pages/entity/onnxruntime-riscv.md
- wiki/_pages/entity/ONNX_Runtime_Build_for_Inferencing.md
- wiki/_pages/entity/llama-cpp-mini.md
- wiki/_pages/entity/tvmonriscv.md
- wiki/_pages/workload_kernel/GEMM_with_RISC-V_Vector_Extension.md
- wiki/_pages/entity/QiMeng_TensorOp.md
- wiki/_pages/entity/XuanTie_GNU_Toolchain.md
- wiki/_pages/entity/Seal5.md
synthesis_status: active
type: synthesis
updated: 2026-06-29
---

# RISC-V ML Inference Toolchain Landscape

## RAG Summary

The RISC-V ML inference toolchain spans four abstraction layers, each with distinct trade-offs for portability, performance, and maintenance cost. At the kernel layer, implementations such as the GEMM RISC-V Vector Extension workload kernel expose RVV 1.0 intrinsics directly, yielding highest performance but requiring per-ISA effort. Above that, lightweight on-device runtimes — ncnn (Tencent, zero external dependencies, ARM/RISC-V support across AllWinner D1 and Loongson 2K1000) and llama-cpp-mini (C++20, GGUF loader, Q4/Q6/Q8 quantization) — embed their own compute kernels and target specific model families without a general compiler. The third layer consists of cross-platform model runtimes: ONNX Runtime and its RISC-V fork onnxruntime-riscv, which adapts ONNX Runtime for RISC-V platforms and integrates with the Gemmini DNN accelerator via UCB ASPIRE. At the compiler layer, IREE (MLIR-based, iree-compiler + iree-runtime, retargetable to CPUs/GPUs/accelerators) and the TVM-on-RISC-V workflow tvmonriscv represent ahead-of-time compilation paths that optimize the full model graph before deployment. Toolchain support — XuanTie GNU Toolchain, LLVM extensions via Seal5 — underlies all layers. A key unresolved tension exists between the auto-vectorization path (TVM → Clang → LLVM RVV) and the manual intrinsic path (RVV kernel hand-tuning); neither dominates across workload types as of mid-2026.

---

## Full Synthesis

### Abstraction Layer Model

The RISC-V ML inference stack can be mapped to four layers:

1. **Kernel layer** — Hand-written or auto-generated compute kernels using RVV 1.0 intrinsics. [[GEMM_with_RISC-V_Vector_Extension]] is a canonical example: implementing double/single/half-precision GEMM using RVV vector load/store/FMA intrinsics. This layer achieves near-peak throughput but is ISA-version specific (RVV 0.7.1 vs 1.0 incompatibilities).

2. **Lightweight runtime layer** — Self-contained C/C++ runtimes with embedded kernels:
   - [[ncnn]]: no BLAS/NNPACK dependency, Vulkan fallback, RISC-V backend (AllWinner D1 tested), models converted via pnnx from PyTorch/ONNX. Strongest on mobile/embedded workloads.
   - [[llama-cpp-mini]]: C++20 reference implementation of Llama-family decoder inference. Supports Q4_K, Q6_K, Q8_0 quantization; Apple Silicon primary target, but illustrates the GGUF ecosystem that llama.cpp extends to RISC-V (Milk-V Pioneer, LicheePi 4A).

3. **Cross-platform model runtime layer**:
   - [[ONNX_Runtime_Build_for_Inferencing]]: Standard ONNX Runtime cross-compiled for RISC-V. Supports graph-level optimization passes (constant folding, op fusion) and hardware accelerator backends.
   - [[onnxruntime-riscv]]: UCB ASPIRE fork targeting Gemmini systolic array. CPU-only path exists but the sgemm kernel is naive; performance on RVV targets is not validated in this fork.

4. **Compiler layer**:
   - [[IREE]]: MLIR-based end-to-end compiler + runtime. Separates iree-compiler (produces flatbuffer artifacts) and iree-runtime (executes them). Retargetable; RISC-V CPU backend requires LLVM RVV support.
   - [[tvmonriscv]]: Demonstrates TVM-to-RISC-V workflow using QEMU user-mode emulation. TVM does not natively generate RVV code; workaround generates C code and uses Clang auto-vectorization.

### Toolchain Dependencies

All layers depend on a RISC-V compiler toolchain with RVV support. [[XuanTie_GNU_Toolchain]] provides binaries for the T-HEAD ecosystem (C906, C908, C910 targets). [[Seal5]] automates LLVM backend extension for custom ISA instructions, enabling DSE-driven toolchain specialization without manual LLVM hacking.

[[QiMeng_TensorOp]] addresses the tensor operator layer specifically for LLMs, using auto-generated hardware primitives (GEMM, convolution) that bridge the kernel and runtime layers.

### Contradictions and Open Questions

- **Auto-vectorization vs hand-tuning**: tvmonriscv uses Clang auto-vectorization for RVV code generation. The RVV GEMM kernel in GEMM_with_RISC-V_Vector_Extension is hand-written. No systematic benchmark directly compares both approaches on the same hardware at the same precision.
- **ONNX Runtime vs IREE for RISC-V**: Both target RISC-V but via different abstractions. ONNX Runtime is graph-level; IREE is IR-level. No head-to-head latency data on identical RISC-V boards exists in current wiki pages.
- **ncnn RISC-V backend maturity**: ncnn lists AllWinner D1 and Loongson 2K1000 as tested RISC-V targets, but no kernel-level RVV 1.0 intrinsic usage is documented in existing pages.

## Open Questions

- Which inference runtime achieves the best throughput per watt on RVV 1.0 hardware (e.g., SpacemiT K1, XuanTie C908) for INT8 CNN workloads?
- Does IREE's RISC-V backend produce comparable throughput to hand-tuned ncnn kernels on tested RISC-V boards?
- Is there an onnxruntime-riscv path with proper BLAS (OpenBLAS or SHL) that matches ncnn performance on non-Gemmini targets?
- When will TVM's upstream add native RVV 1.0 codegen, eliminating the Clang workaround in tvmonriscv?

## Connected Pages

- [[IREE]]
- [[ncnn]]
- [[onnxruntime-riscv]]
- [[ONNX_Runtime_Build_for_Inferencing]]
- [[llama-cpp-mini]]
- [[tvmonriscv]]
- [[GEMM_with_RISC-V_Vector_Extension]]
- [[QiMeng_TensorOp]]
- [[XuanTie_GNU_Toolchain]]
- [[Seal5]]
