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
