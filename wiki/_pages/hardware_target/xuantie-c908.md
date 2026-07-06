---
canonical_name: XuanTie C908
aliases:
- C908
- T-Head XuanTie C908
- Xuantie C908
- T-HEAD XuanTie C908
- xuantie-c908
- xt-c908
- C908V
- T-Head C908
- GCC Tuning for XuanTie C908 (CanMV-K230)
- XuanTie C908 tuning
- C908 scheduler model
- GCC XuanTie C908 scheduler model
subtype: null
type: hardware_target
tags: []
sources:
- raw/cache/f47a619a7b5e17eb.md
- https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/
- raw/cache/d97272025503b0a2.md
- https://csi-nn2.opensource.alibaba.com/zh/blog/C908+accelerates+AI
- raw/cache/73bedd2221cd9a03.md
- https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
- raw/cache/84a65460eb9d8421.md
- https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719208.html
- raw/cache/17dddb797b6e11ae.md
- https://github.com/FreeRTOS/FreeRTOS-Community-Supported-Demos/blob/main/RISC-V_XUANTIE_C908_GCC/README.md
- raw/cache/25ef1a75fb2012c6.md
- https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719234.html
- raw/cache/97c99da680dadacf.md
- https://www.cnx-software.com/2022/11/04/t-head-xuantie-c908-risc-v-core-targets-aiot-applications/
hardware_targets:
- XuanTie C908
toolchains:
- HHB
- SHL
constraints:
- TSMC 12nm
- 2 GHz
- 52.8 mW/GHz per core
created: '2022-11-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 1
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.5
source_url: https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/
fetched_at: '2026-07-03T13:14:57.990457+00:00'
---

# XuanTie C908

The XuanTie C908 is a 64-bit mid-range RISC-V processor core developed by T-Head Semiconductor (Alibaba Cloud). It implements the RV64GCB[V] instruction set and is compatible with the RVA22 profile for interoperability with Android and other rich operating systems. Note that the core can be configured with or without the Vector Extension (RVV); the GCC tuning model for the base C908 (without VPU) does not include RVV scheduling, with vector scheduling left for future work (xt-c908v). The core features a 9-stage dual-issue in-order pipeline with branch prediction technologies including a state-of-the-art Branch History Table, Branch Target Buffer, and Return Address Stack, and it utilizes instruction fusion technology to fuse multiple instructions into a single execution. Designed for AIoT applications such as intelligent interaction and AR/VR, the C908 includes an optional Vector Processing Unit (VPU) supporting the RISC-V Vector Extension 1.0 specification, with configurable vector register width of 128 bits or 256 bits (VLEN). The VPU handles various vector floating-point and integer data formats including FP16, BFP16, FP32, INT8, INT32, INT64, and dedicated INT8 and INT4 vector dot product instructions. The core uses a two-level cache system with hardware cache coherency and optional ECC, supporting multi-cluster configurations (1 to 4 cores per cluster). The bus interface supports AXI4/ACE protocol with a Device Coherence Port (DCP) and a Low Latency Port (LLP). The C908 can run at up to 2 GHz on TSMC 12nm process with dynamic power consumption of 52.8 mW/GHz per core, delivering over 20% better energy efficiency than the XuanTie C906 under identical frequency and process conditions. It also supports the RV32 COMPAT mode for running 32-bit applications, which was merged into Linux 5.19.

Adopting a hardware-software co-design methodology, the C908 integrates dedicated AI instructions (including an int8 vector dot product instruction) and is supported by the SHL (ShiHulan) heterogeneous computing library and the HHB toolchain for neural network quantization and compilation. SHL provides optimized neural network operators for the C908, including assembly-optimized convolution implementations (im2col+GEMM and Winograd). In synthetic benchmarks (Coremark, Dhrystone, Whetstone, Linkpacks) under unspecified test conditions, the C908 delivers a 24–64% gain over the C906. In MLPerf Tiny v0.7 inference benchmarks, the C908 achieved up to 3.5 times the performance of its predecessor, the XuanTie C906. The C908 delivers a 3.35x speedup on MobileNet with int8 dot product, and overall AI performance improvements of 3.75x to 4.57x versus XuanTie C906 (VLEN128 vs D1). When using INT4 data types, AI inference is 2–3.5× faster than the C906 on MLPerf Tiny v0.7 benchmarks (wake word detection, image classification, keyword spotting, anomaly detection). When comparing VLEN256 to VLEN128, the performance gain is 1.55x to 1.68x. A variant, the XuanTie C908X, further extends vector capabilities with dedicated AI instructions for terminal, edge, and infrastructure applications.

GCC has added a tuning and scheduler model for the C908, contributed by Milan Tripkovic and based on the XuanTie C908 R1S0 User Manual. The scheduler model covers scalar integer, load/store, multiply, divide, and floating-point pipeline resources. Long-latency reservations are clamped to 7 cycles following the existing RISC-V scheduler modelling approach (commit 8265192). The tuning was tested on a CanMV-K230-V1.1 board running CoreMark and instruction throughput tests consisting of unrolled loops with independent register groups (for integer add, float add, etc.), achieving a 0.8% CoreMark improvement and 5–17% cycle-count improvements on instruction throughput loops, measured after 20 warm-up runs and 200 measured executions per test. Vector scheduling is not covered in the initial patch; future work is planned under the label xt-c908v.

The XuanTie C908 is used in the Canaan Kendryte K230 SoC, which powers development boards such as the CanMV-K230-V1.1 and the XIAOHUI EVB. A FreeRTOS community port is available for this platform: it maps the PLIC at 0x08000000 and the CLINT at 0x0c000000, supports a configurable number of cores (1–4, default 1), an interrupt stack size of 8192 bytes, and an initial task stack of 4096 bytes. The default board target is CONFIG_BOARD_XIAOHUI_EVB. Compilation for the C908 requires the medium-any code model (`-mcmodel=medany`); the `-Os` size optimization is recommended. The GCC toolchain supports selecting a scalar-only configuration with `-mcpu=c908` or a configuration with vector extensions (RVV 1.0) with `-mcpu=c908v`.

## Key Claims

- Implements RV64GCB[V] instruction set and is compatible with the RVA22 profile.
- 9-stage dual-issue in-order pipeline with instruction fusion.
- Optional VPU compliant with RISC-V Vector 1.0, supporting INT4, BF16, half-precision, FP16, BFP16, FP32, INT8, INT32, INT64, and dedicated INT8/INT4 vector dot product instructions. Configurable VLEN 128 or 256.
- Supports RISC-V Bitmanip 1.0, CMO Base, Svinval, Svnapot, Svpbmt, and XMAE extensions.
- Two-level cache with hardware cache coherency and optional ECC.
- Maximum frequency of 2 GHz under TSMC 12nm; dynamic power 52.8 mW/GHz per core.
- Over 20% better energy efficiency than XuanTie C906 under equivalent frequency and process.
- 24–64% gain over C906 in synthetic benchmarks (Coremark, Dhrystone, Whetstone, Linkpacks).
- AI inference speedup: 2–3.5× over C906 on MLPerf Tiny v0.7 benchmarks using INT4 data; up to 3.5× overall; 3.35x on MobileNet with int8 dot product; overall AI performance gain of 3.75x–4.57x versus C906 (VLEN128 vs D1). VLEN256 provides 1.55x–1.68x improvement over VLEN128.
- Enhanced Physical Memory Protection (ePMP) with up to 64 regions.
- Platform-Level Interrupt Controller (PLIC) configurable up to 1023 interrupt sources.
- AI software tools: HHB neural network inference deployment tool and SHL high-performance heterogeneous computing library. SHL provides assembly-optimized convolution kernels (im2col+GEMM and Winograd) for the C908.
- Hardware-software co-design for AI acceleration.
- Dedicated int8 vector dot product instructions improve MobileNet inference by 3.35x.
- SHL provides optimized inference kernels for fp32, fp16, and int8 datatypes.
- C908X variant adds further dedicated AI instructions for edge and infrastructure deployments.
- The GitHub repository xtai-benchmark provides tools for evaluating AI performance on RISC-V including C908.
- GCC scheduler model for C908 (contributed to mainline GCC) covers scalar integer, load/store, multiply, divide, and floating-point pipeline resources; long-latency reservations clamped to 7 cycles.
- Tuning validated on CanMV-K230-V1.1 board: CoreMark improvement 0.8%, instruction throughput test cycle-count reductions 5–17%.
- Vector scheduling not included in initial GCC patch; labelled as future work (xt-c908v).
- Used in the Canaan Kendryte K230 SoC (CanMV-K230 and XIAOHUI EVB boards).
- FreeRTOS community port available: PLIC at 0x08000000, CLINT at 0x0c000000, configurable 1–4 cores, interrupt stack 8192 B, initial task stack 4096 B, default board XIAOHUI_EVB.
- GCC compilation requires `-mcmodel=medany`; `-Os` recommended; select scalar-only with `-mcpu=c908` or with vector extensions via `-mcpu=c908v`.
- RV32 COMPAT mode for running 32-bit applications, merged into Linux 5.19.
- Virtual address systems: Sv39/Sv48.

## Optimization-Relevant Details

- ISA/profile: RV64GCB[V] (compatible with RVA22); RV32GCB[V] for User mode; extends with Vector 1.0, Bitmanip 1.0, CMO, Svinval; dedicated AI instructions (int8 vector dot product).
- Vector/matrix/accelerator support: Optional VPU with RVV 1.0, configurable VLEN 128 or 256, vector dot product instruction extension (INT8, INT4), support for FP16, BFP16, FP32, INT8, INT32, INT64; C908X adds more AI-specific vector instructions. GCC tuning model for base C908 does not include vector scheduling.
- Memory/cache/TLB/DMA: Two-level cache with hardware coherency, Sv39/Sv48 virtual address, AXI4/ACE bus with DCP and LLP interfaces; high-speed cache technology.
- Compiler/toolchain support: HHB deployment tool for quantization and compilation; SHL library for optimized inference kernels on fp32, fp16, int8 (including im2col+GEMM and Winograd convolutions). GCC tuning model contributed for scheduler and pipeline; does not yet cover vector instructions. FreeRTOS port uses `-mcmodel=medany` and `-Os`.
- Energy efficiency: >20% improvement over XuanTie C906 under equivalent frequency and process.
- Synthetic benchmark performance: 24–64% gain over C906 in Coremark, Dhrystone, Whetstone, Linkpacks (test conditions unspecified).

## Relationships

- [[shl]]: SHL provides optimized neural network inference kernels for the XuanTie C908, leveraging its pipeline, instruction fusion, and cache to deliver performance across fp32, fp16, and int8 datatypes. SHL includes assembly-optimized convolution implementations (im2col+GEMM and Winograd).
- [[c908-wino-gemm-optimization]]: Shares the XuanTie C908 hardware target but focuses on SHL software library optimizations; note that the optimization recipe assumes RVV 1.0 support, while the GCC tuning model for the base C908 does not include vector scheduling – the core can be configured with or without a VPU, so these are complementary rather than contradictory.

## Benchmarking

The [XuanTie AI Benchmark Suite (xtai-benchmark)](https://github.com/XUANTIE-RV/xtai-benchmark) provides precompiled benchmark binaries for the C908, compiled via HHB, covering BERT, EfficientNet, and MobileNetV2 with various quantizations.

## Sources

- [XuanTie C908 Blog Post](https://riscv.org/blog/xuantie-c908-high-performance-risc-v-processor-catered-to-aiot-industry-chang-liu-alibaba-cloud/)
- Alibaba T-HEAD blog post (December 20, 2022): "XuanTie C908 Accelerates AI with Software and Hardware Fusion"
- Supplementary search snippets and DDG context.
- xtai-benchmark GitHub repository: https://github.com/XUANTIE-RV/xtai-benchmark
- [XuanTie C908 Accelerates AI with Software and Hardware Fusion](https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/)
- GCC patch series for C908 tuning: https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719208.html
- GCC tuning patch (individual submission): https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719234.html
- FreeRTOS community port for XuanTie C908: https://github.com/FreeRTOS/FreeRTOS-Community-Supported-Demos/blob/main/RISC-V_XUANTIE_C908_GCC/README.md
- https://www.cnx-software.com/2022/11/04/t-head-xuantie-c908-risc-v-core-targets-aiot-applications/
