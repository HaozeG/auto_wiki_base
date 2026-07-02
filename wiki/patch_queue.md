# Wiki Patch Queue

## [2026-07-02] merge_pending | xuantie-c908.md
target_page: xuantie-c908.md
canonical_name: XuanTie C908
colliding_name: XuanTie C908 MLPerf tiny inference vs C906
source: https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/
status: pending_review
<!-- merge_draft_body
# XuanTie C908 MLPerf tiny inference vs C906

The XuanTie C908 achieves up to 3.5 times the inference performance of the XuanTie C906 on the MLPerf Tiny v0.7 benchmark, as reported by T-Head Semiconductor. The C908 runs at up to 2 GHz on TSMC 12nm and includes an optional Vector Processing Unit with INT4 data type support and vector dot product extensions. The C906 is a lower-cost single-issue in-order core. This benchmark result demonstrates the ML acceleration improvements of the C908 pipeline, instruction fusion, and data prefetching technologies, along with the HHB and SHL software libraries.

## Key Claims

- XuanTie C908 outperforms XuanTie C906 by up to 3.5× on MLPerf Tiny v0.7 inference tasks.
- The gain is attributed to architectural innovations (9-stage dual-issue pipeline, instruction fusion, data prefetching, vector unit with INT4).
- The comparison is at same frequency and process (TSMC 12nm).
- Source: T-Head Semiconductor official blog post, evidence strength: reported.

## Measurement Context

- Hardware version: XuanTie C908 (9-stage dual-issue in-order, 2 GHz, TSMC 12nm) vs XuanTie C906 (single-issue in-order).
- Software/toolchain version: MLPerf Tiny v0.7; HHB inference deployment tool; SHL computing library; Linux kernel 5.19+.
- Workload shape: MLPerf Tiny v0.7 inference (exact model/layer details not provided).
- Metric: Ratio of inference performance (e.g., throughput or latency improvement); up to 3.5×.
- Method: Reported from vendor blog post; no independent verification or detailed methodology disclosed.
- Evidence strength: reported

## Relationships

- [[xuantie-c908]]: The hardware target whose benchmark result is reported.
- [[cpa-factored-gemmini-systolic-array]]: Another optimization for RISC-V AI accelerators; no direct connection but contextually relevant to the AI acceleration theme.

## Sources

- [XuanTie C908 blog post on RISC-V International](https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/)
merge_draft_body -->

## [2026-07-02] merge_pending | sifive-intelligence-x280.md
target_page: sifive-intelligence-x280.md
canonical_name: SiFive Intelligence X280
colliding_name: SiFive Intelligence X280
source: https://www.cnx-software.com/2021/04/27/sifive-intelligence-x280-64-bit-risc-v-processor-integrates-ai-extensions/
status: pending_review
<!-- merge_draft_body
# SiFive Intelligence X280

The SiFive Intelligence X280 is a 64-bit RISC-V processor core based on the U7-series, featuring an 8-stage dual-issue in-order pipeline with vector extensions up to 512-bit register length and SiFive Intelligence Extensions for AI/ML acceleration. It supports a wide range of datatypes including BF16, FP16, FP32, FP64, and integer types from int8 to 64-bit fixed-point. The core includes a high-performance vector memory subsystem, virtual memory with precise exceptions, and up to 48-bit addressing. Designed for Linux-capable multi-core systems, the X280 targets edge AI/ML inference workloads such as AR/VR, sensor hubs, in-vehicle infotainment, IP cameras, and digital cameras. The processor incorporates software support via TensorFlow Lite and offers a compiler compatibility flag (-msifive-arm-compat) to facilitate migration from Arm NEON-optimized code.

## Key Claims

- 64-bit RISC-V ISA with 8-stage dual-issue in-order pipeline, coherent multi-core, Linux capable.
- SiFive Intelligence Extensions for ML workloads support BF16/FP16/FP32/FP64 and int8 to 64 fixed-point datatypes.
- 512-bit vector register length with variable-length operations, up to 512-bits of data per cycle.
- High-performance vector memory subsystem with memory parallelism for cache miss tolerance.
- Virtual memory support with precise exceptions and up to 48-bit addressing.
- AI instructions claimed to be twelve times faster than inference on RISC-V cores without intelligence extensions (source: SiFive announcement, no independent benchmarks provided).
- Code optimized for Arm NEON can be compiled using the -msifive-arm-compat flag.
- First customer integrating the core is Tenstorrent.

## Optimization-Relevant Details

- **ISA/profile:** RV64GC with vector extensions (RVV) and SiFive Intelligence Extensions.
- **Vector/matrix/accelerator support:** 512-bit vector registers, supports BF16/FP16/FP32/FP64 and integer types.
- **Memory/cache/TLB/DMA:** High-performance vector memory subsystem, virtual memory with precise exceptions, up to 48-bit addressing.
- **Compiler/toolchain support:** TensorFlow Lite, GCC with -msifive-arm-compat flag for Arm NEON compatibility.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: The X280 is a general-purpose RISC-V AI core, while the Gemmini systolic array is a domain-specific accelerator for matrix multiplication; both serve the RISC-V AI acceleration ecosystem.
- Insufficient context for additional cross-links; no existing entity pages for SiFive cores or related AI accelerators are present in the wiki.

## Sources

- [SiFive Intelligence X280 64-bit RISC-V processor integrates AI extensions - CNX Software](https://www.cnx-software.com/2021/04/27/sifive-intelligence-x280-64-bit-risc-v-processor-integrates-ai-extensions/)
merge_draft_body -->

## [2026-07-02] pending | sifive-intelligence-x160-gen-2.md
target_page: sifive-intelligence-x160-gen-2.md
target_section: Optimization-Relevant Details
source: https://github.com/riscv-non-isa/riscv-rvv-intrinsic-doc/
status: pending_review
proposed_update: In the 'Compiler/toolchain support' line, add: 'Clang 19 and GCC 14 support RVV v1.0 intrinsics as per the riscv-rvv-intrinsic-doc specification.'

## [2026-07-02] merge_pending | riscv-vector-intrinsics.md
target_page: riscv-vector-intrinsics.md
canonical_name: RISC-V Vector Intrinsics
colliding_name: RISC-V Vector C Intrinsics
source: https://github.com/riscv-non-isa/riscv-rvv-intrinsic-doc/blob/main/doc/rvv-intrinsic-spec.adoc
status: pending_review
<!-- merge_draft_body
# RISC-V Vector C Intrinsics

The RISC-V Vector C Intrinsics specification defines a C language interface that allows programmers to directly leverage the RISC-V "V" extension (RVV) at the source code level. It provides strongly-typed vector data types and intrinsic function calls that map to individual RVV instructions, freeing the programmer from managing instruction scheduling and register allocation. The specification includes a test macro `__riscv_v_intrinsic` for compiler support detection, a mandatory header file `<riscv_vector.h>`, and encodes effective element width (EEW) and effective LMUL (EMUL) into function names. It also controls application vector length (AVL) through a `size_t vl` argument, supports masking and policy bits (tail-agnostic, mask-agnostic), and defaults to tail-agnostic and mask-agnostic policies for high-performance cores. Version 1.0 of this specification corresponds to a macro value of 1,000,000 and is implemented in both GCC and LLVM toolchains, enabling portable vectorized code across RISC-V hardware.

## Key Claims

- The RISC-V Vector C Intrinsics provide a C-level API for directly utilizing the RISC-V V extension (RVV).
- The test macro `__riscv_v_intrinsic` is defined even when the vector extension is not enabled, and its value encodes the version using the formula MAJOR*1,000,000 + MINOR*1,000 + REVISION.
- The header `<riscv_vector.h>` must be included and should be guarded with the test macro for conditional compilation.
- Availability of intrinsic variants depends on the target architecture specified via the `-march` option;
for example, `vint64m1_t` is unavailable under `rv64gc_zve32x`.
- The intrinsics encode the effective element width (EEW) and effective LMUL (EMUL) of destination vector registers in function name suffixes.
- Application vector length (AVL) is specified via the `size_t vl` argument rather than directly exposing the `vl` control register;
the actual `vl` value is implementation-defined.
- Instructions available for masking provide masked intrinsic variants, fusing mask control with policy behavior (vta, vma).
- The default policy for tail and inactive masked-off elements is tail-agnostic and mask-agnostic (vta=1, vma=1), optimized for high-performance out-of-order cores.
- The specification version 1.0 defines the macro value 1000000.

## Relationships

- [[sifive-intelligence-x160-gen-2]]: This hardware target implements RVV1.0, making the intrinsics directly applicable for programming its vector unit.
- [[xuantie-c950]]: The C950 is a RISC-V server-class processor that supports the RVV extension and therefore benefits from the intrinsics defined in this specification.

## Sources

- [RISC-V Vector C Intrinsics Specification (GitHub)](https://github.com/riscv-non-isa/riscv-rvv-intrinsic-doc/blob/main/doc/rvv-intrinsic-spec.adoc)
merge_draft_body -->

## [2026-07-02] merge_pending | riscv-vector-intrinsics.md
target_page: riscv-vector-intrinsics.md
canonical_name: RISC-V Vector Intrinsics
colliding_name: RISC-V Vector Intrinsics
source: https://runebook.dev/en/docs/gcc/risc_002dv-vector-intrinsics
status: pending_review
<!-- merge_draft_body
# RISC-V Vector Intrinsics

RISC-V Vector Intrinsics are a set of compiler-provided functions and macros that enable C/C++ programmers to directly utilize the RISC-V Vector Extension (RVV) instructions for SIMD parallelism. These intrinsics, available through the riscv_vector.h header in GCC and other toolchains, allow operations on multiple data elements with a single instruction, accelerating workloads in signal processing, machine learning, and graphics. The intrinsics require target hardware support for the V extension, specified at compile time with appropriate -march flags. A key intrinsic is vsetvli, which sets the effective vector length (EVL) based on hardware capabilities and data type. Naming conventions are type-specific—for example, vle64 for 64-bit integer loads and vlfe64 for 64-bit floating-point loads. Incorrect usage can lead to runtime illegal instruction errors or incorrect results. As an alternative to manual intrinsics, GCC's auto-vectorization with -O3 can automatically convert simple loops into vector instructions, offering portability and maintainability.

## Key Claims

- RISC-V Vector Intrinsics provide direct access to RVV instructions from C/C++.
- The intrinsics require hardware support for the V extension; otherwise, illegal instruction errors occur at runtime.
- The vsetvli intrinsic must be called to set the effective vector length; its return value should be used for subsequent vector operations.
- Intrinsic function names are type-specific (e.g., vle64 for integers, vlfe64 for floats).
- Auto-vectorization with GCC -O3 and appropriate -march flags can be a simpler, portable alternative to manual intrinsics.
- An example of array summation demonstrates both manual intrinsic and auto-vectorization approaches.

## Relationships

- [[sifive-intelligence-x160-gen-2]]: A hardware target supporting RISC-V Vector Extension v1.0, on which these intrinsics can be used.
- [[xuantie-c950]]: A server-class RISC-V hardware target that likely supports the vector extension, enabling use of these intrinsics.

## Sources

- [A Friendly Guide to RISC-V Vector Intrinsics in GCC](https://runebook.dev/en/docs/gcc/risc_002dv-vector-intrinsics)
merge_draft_body -->
