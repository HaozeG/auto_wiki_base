---
type: synthesis
connected_entities: [risc_v_profiles_rva, risc_v_vector_extension, risc_v_matrix_extension, gnu_toolchain_riscv_vector, muriscv_nn, onnx_runtime_riscv, iree_riscv, tvm_riscv_backend, mlir_riscv_backend, risc_v_zve_embedded_vector, openxiangshan_difftest_nemu]
synthesis_status: draft
created: 2026-06-27
updated: 2026-06-28
cold_start: false
sources:
- https://riscv.org/blog/risc-v-announces-ratification-of-the-rva23-profile-standard/
- https://github.com/riscv/riscv-profiles/blob/main/src/rva23-profile.adoc
- https://www.cnx-software.com/2025/07/08/ubuntu-25-10-release-to-mandate-rva23-profile-obsoleting-most-risc-v-hardware/
- https://www.phoronix.com/news/GCC-RISC-V-Auto-Vectorization
- https://llvm.org/docs/RISCVUsage.html
- https://medium.com/accelr-blog/apache-tvm-on-risc-v-experiment-results-aec86c3e7cf8
- https://dl.acm.org/doi/10.1145/3637543.3652878
- https://www.researchgate.net/publication/381895543_muRISCV-NN_Challenging_Zve32x_Autovectorization_with_TinyML_Inference_Library_for_RISC-V_Vector_Extension
inbound_links: 0
scorecard:
  bridge_score: ~
  contradiction_potential: ~
  cross_domain_connection: ~
---

# RISC-V AI: From ISA Standardization to Software Stack Convergence

## RAG Summary
<!-- THIS BLOCK IS SPECIAL: 150-250 words, self-contained, written last. -->

A defining tension in the RISC-V AI ecosystem is the gap between ISA standardization and software stack maturity. The ratification of RVV 1.0 (November 2021) and the RVA23 profile (October 2024) — which makes RVV mandatory — established the hardware contract that software can now rely on. Yet the compiler and runtime stack has had to race to match: GCC 14 (April 2024) shipped initial auto-vectorization for RVV, contributed by Rivos Inc., while LLVM had offered RVV codegen since 2021 but with varying optimization quality. Apache TVM's RISC-V backend leverages LLVM and achieves 46% lower latency than raw GCC. Higher up the stack, ONNX Runtime added RVV-accelerated CPU Execution Provider support, and the muRISCV-NN library demonstrated that hand-tuned RVV intrinsics outperform compiler auto-vectorization by up to 60% for convolutional inference kernels. IREE added RV64 microkernels in 2025. At the embedded end, muRISCV-NN targets Zve32x sub-extensions for MCU-class TinyML. Meanwhile, the absence of a ratified matrix extension means proprietary solutions (Alibaba AME, SiFive X390 VCIX) fill the gap for matrix-heavy AI. The XiangShan Difftest/NEMU co-simulation framework shows how open-source hardware verification tooling is maturing in parallel, enabling open-source RISC-V processor development to catch correctness bugs before silicon. The convergence signal: RVA23 + ratified software ABIs is enabling the first generation of standard binary Linux distributions (Ubuntu 25.10 mandates RVA23) that can ship vectorized AI libraries without per-chip customization.

---

## Full Synthesis

### The ISA Contract: From Fragmentation to RVA23

Early RISC-V AI deployments (K210, early XuanTie) required fully bespoke software stacks because every chip had different extension combinations. The introduction of profiles changes this: RVA20 established a minimum scalar baseline; RVA22 added optional vector; and RVA23 made RVV 1.0 mandatory, meaning any RVA23-compliant SoC (Ventana Veyron V2, TT-Ascalon, SiFive P870) guarantees SIMD inference acceleration to software without runtime probing.

### The Compiler Stack Race

The hardware standard has outpaced compiler support. LLVM led GCC in RVV maturity, and Apache TVM's choice to use LLVM as its codegen backend paid off — 46% latency over GCC. But even LLVM auto-vectorization leaves up to 60% performance on the table for structured convolution kernels versus hand-tuned muRISCV-NN intrinsics. This gap motivates a tiered approach: MLIR/IREE/TVM handle structured operator dispatch, hand-tuned microkernel libraries (muRISCV-NN, XNNPACK) fill the inner loops.

### The Missing Link: Matrix Extension

RVV handles SIMD-width computation, but generative AI and transformer inference are dominated by large matrix multiplies. Without a ratified matrix extension, proprietary solutions proliferate: Alibaba's AME (Attached Matrix Extension) in XuanTie C950, SiFive's X390 VCIX 1024-bit vector with dual ALUs, Stream Computing's v0.5 specification. A ratified RISC-V matrix extension would repeat the RVV unification story for matrix workloads — but that ratification appears at least 2–3 years away.

### Open Verification: Difftest and NEMU

Software stack convergence requires correct hardware. The OpenXiangShan Difftest/NEMU framework represents the open-source RISC-V ecosystem's answer to verification at scale: co-simulate RTL against a fast ISA emulator at every instruction commit. The risk — shared bugs between DUT and reference model — is partially mitigated by SimFuzz (2025) adding mutation-based fuzzing. This infrastructure is being reused beyond XiangShan, suggesting a shared verification commons may emerge.

### Convergence Timeline

- 2021: RVV 1.0 ratified; LLVM adds RVV codegen
- 2023: GCC 13 adds RVV intrinsics; TVM, IREE, muRISCV-NN port to RVV
- 2024 (March): RVA20/22 profiles v1.0 ratified; GCC 14 adds auto-vectorization
- 2024 (October): RVA23 ratified — RVV mandatory
- 2025: Ubuntu 25.10 mandates RVA23; IREE adds RV64 microkernels
- 2026+: Ratified matrix extension expected; first standard AI binary distributions

## Open Questions

- When will a RISC-V matrix extension be ratified, and will Stream Computing's v0.5 spec become the basis?
- Can hand-tuned microkernel libraries (muRISCV-NN) be auto-generated well enough by compilers to close the 60% gap?
- Will Difftest/NEMU become a cross-project RISC-V verification standard, or remain XiangShan-specific?
- Does Ubuntu 25.10's RVA23 mandate accelerate adoption or fragment the ecosystem between RVA22 and RVA23 hardware?

## Connected Pages

- [[risc_v_profiles_rva]]
- [[risc_v_vector_extension]]
- [[risc_v_matrix_extension]]
- [[gnu_toolchain_riscv_vector]]
- [[muriscv_nn]]
- [[onnx_runtime_riscv]]
- [[iree_riscv]]
- [[tvm_riscv_backend]]
- [[mlir_riscv_backend]]
- [[risc_v_zve_embedded_vector]]
- [[openxiangshan_difftest_nemu]]
