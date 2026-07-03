# Wiki Patch Queue

## [2026-07-03] pending | xuantie-c908.md
target_page: xuantie-c908.md
target_section: Benchmarking
source: https://github.com/XUANTIE-RV/xtai-benchmark
status: pending_review
proposed_update: Add a section describing the XuanTie AI Benchmark Suite (xtai-benchmark), which provides precompiled benchmark binaries for the C908 (BERT, EfficientNet, MobileNetV2 with various quantizations) via HHB. Source: https://github.com/XUANTIE-RV/xtai-benchmark

## [2026-07-03] pending | xuantie-ai-benchmark-suite.md
target_page: xuantie-ai-benchmark-suite.md
target_section: Relationships
source: https://github.com/XUANTIE-RV/xuantie-gnu-toolchain/
status: pending_review
proposed_update: Add a relationship entry linking to the XuanTie GNU Compiler Toolchain: 'The XuanTie GNU Compiler Toolchain provides the cross-compiler used to build the precompiled model binaries in this benchmark suite.'

## [2026-07-03] merge_pending | xuantie-c908.md
target_page: xuantie-c908.md
canonical_name: XuanTie C908
colliding_name: XuanTie C908
source: https://csi-nn2.opensource.alibaba.com/zh/blog/C908+accelerates+AI
status: pending_review
<!-- merge_draft_body
# XuanTie C908

XuanTie C908 is a high-performance RISC-V processor core designed by T-HEAD, Alibaba's semiconductor division, using a hardware-software co-design methodology to accelerate deep learning inference. The core integrates dedicated AI instructions, including an int8 vector dot product instruction, and leverages a design that combines processor pipeline optimization, instruction fusion, and high-speed cache technology. It is supported by the SHL (ShiHulan) heterogeneous computing library and the HHB toolchain for neural network quantization and compilation. In MLPerf Tiny v0.7 inference benchmarks, the C908 achieved up to 3.5 times the performance of its predecessor, the XuanTie C906. A variant, the XuanTie C908X, further extends vector capabilities with dedicated AI instructions for terminal, edge, and infrastructure applications. The C908 focuses on delivering efficient AI inference for RISC-V platforms through both architectural enhancements and optimized software support.

## Key Claims

- XuanTie C908 adopts a co-design methodology for both hardware and software AI acceleration.
- It includes dedicated int8 vector dot product instructions that improve MobileNet inference by 3.35x.
- The SHL library provides optimized inference kernels for the C908 supporting fp32, fp16, and int8 datatypes.
- C908 outperforms C906 by up to 3.5x in MLPerf Tiny v0.7 inference benchmarks.
- The C908X variant adds further dedicated AI instructions for edge and infrastructure deployments.
- The GitHub repository xtai-benchmark provides tools for evaluating AI performance on RISC-V including C908.

## Optimization-Relevant Details

- ISA/profile: RISC-V with dedicated AI instructions (int8 vector dot product).
- Vector/matrix/accelerator support: Vector extensions enhanced with AI instructions; C908X adds more.
- Memory/cache/TLB/DMA: High-speed cache technology (detailed hierarchy not specified in available sources).
- Compiler/toolchain support: HHB for quantization and compilation, SHL for optimized inference kernels.

## Relationships

- [[shl]]: SHL provides optimized neural network inference kernels for the XuanTie C908, leveraging its pipeline, instruction fusion, and cache to deliver performance across fp32, fp16, and int8 datatypes.

## Sources

- Alibaba T-HEAD blog post (December 20, 2022): "XuanTie C908 Accelerates AI with Software and Hardware Fusion"
- Supplementary search snippets and DDG context.
- xtai-benchmark GitHub repository: https://github.com/XUANTIE-RV/xtai-benchmark
merge_draft_body -->

## [2026-07-03] pending | shl.md
target_page: shl.md
target_section: Key Claims
source: https://csi-nn2.opensource.alibaba.com/zh/blog/C908+accelerates+AI
status: pending_review
proposed_update: Add a key claim: SHL provides optimized inference acceleration for XuanTie C908, supporting fp32/fp16/int8 datatypes and leveraging the processor's pipeline, instruction fusion, and high-speed cache technology. This is sourced from the same blog post.

## [2026-07-03] pending | shl.md
target_page: shl.md
target_section: content
source: https://zhangwm-pt.github.io/shl/md_README.html
status: pending_review
proposed_update: Merge the detailed information from the SHL README into the existing entity page. Specifically: (1) Expand the opening paragraph to mention version SHL 2.2.x and that the interface uses CSI-NN2 API. (2) Add a 'Features' subsection under Key Claims covering reference C implementation, assembly optimization for XuanTie CPU, symmetric and asymmetric quantization, support for 8-bit, 16-bit, and float16 data types, NCHW and NHWC layouts, automatic API calling via HHB, and coverage of CPU and NPU architectures. (3) Add a 'Usage' section containing build instructions from source for XuanTie C906 (including installing T-HEAD RISC-V GCC 2.6, cloning CSI-NN2, compiling and installing nn2_c906) and a quick-start example for running mobilenetv1 f16 on a C906-based board like the D1. (4) Add an 'Acknowledgements' subsection noting that SHL references Caffe, TensorFlow, ncnn, MNN, Tengine, CMSIS_5, ONNX, and XNNPACK. (5) Add a relationship to MLPerf tiny (from the candidate's mention of 'SHL to run MLPerf tiny') and to HHVB toolchain documentation. All updates should be grounded in the candidate's source_grounded_snippets.

## [2026-07-03] merge_pending | xuantie-c908.md
target_page: xuantie-c908.md
canonical_name: XuanTie C908
colliding_name: xuantie-c908
source: https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
status: pending_review
<!-- merge_draft_body
# XuanTie C908

XuanTie C908 is a RISC-V processor core developed by T-Head Semiconductor, a subsidiary of Alibaba Group, designed for AI and IoT applications with a focus on software-hardware fusion. It operates at a frequency of up to 2 GHz and is compliant with the RISC-V Vector Extension version 1.0, supporting configurable vector register widths of 128 bits or 256 bits (VLEN). The vector execution unit handles FP16, BFP16, FP32 floating-point operations and INT8, INT32, INT64 integer operations, along with dedicated INT8 and INT4 vector dot product instructions. The microarchitecture features instruction fusion technology to reduce pipeline overhead and improve computational efficiency. For AI inference, the C908 is supported by the Structure of Heterogeneous Library (SHL), a neural network library providing optimized operators, and the Heterogeneous Honey Badger (HHB) toolchain for model quantization and code generation. Compared to its predecessor XuanTie C906, the C908 delivers significant performance improvements in common CNN models due to its vector extensions and optimized software stack.

## Key Claims

- XuanTie C908 is the latest RISC-V processor from T-Head, with a frequency of up to 2 GHz.
- It is compliant with RISC-V Vector Extension 1.0.
- Supports configurable vector register bit width VLEN 128 or 256.
- Vector execution unit supports FP16/BFP16/FP32, INT8/INT32/INT64, and INT8/INT4 vector dot product operations.
- Features instruction fusion technology.
- SHL (Structure of Heterogeneous Library) provides optimized neural network operators for the C908, including assembly-optimized convolution implementations (im2col+GEMM and Winograd).
- HHB toolchain adapts to the C908 for quantization and model deployment.
- Performance speedup: 3.35x on MobileNet with int8 dot product, 1.55-1.68x from VLEN256 vs VLEN128, and 3.75-4.57x overall AI performance vs XuanTie C906 (VLEN128 vs D1).

## Optimization-Relevant Details

- ISA/profile: RV64GCV (with V extension 1.0)
- Vector/matrix/accelerator support: RVV 1.0, VLEN 128/256, vector dot product (INT8/INT4)
- Memory/cache/TLB/DMA: Not specified in source
- Compiler/toolchain support: SHL (neural network library), HHB (quantization and compilation toolchain)

## Relationships

- [[shl]]: SHL provides the optimized neural network operators that leverage the XuanTie C908's vector unit, instruction fusion, and dot product instructions for inference acceleration.

## Sources

- https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
merge_draft_body -->

## [2026-07-03] merge_pending | shl.md
target_page: shl.md
canonical_name: SHL
colliding_name: SHL
source: https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/blob/master/doc/shl/introduce.adoc
status: pending_review
<!-- merge_draft_body
# SHL

SHL (Structure of Heterogeneous Library) is a high-performance heterogeneous computing library developed by T-HEAD for the XuanTie CPU platform. It provides optimized binary libraries using the CSI-NN2 neural network library API, supporting both reference C implementations and assembly optimizations for XuanTie CPUs. SHL supports symmetric and asymmetric quantization, 8-bit, 16-bit, and FP16 data types, and is compatible with both NCHW and NHWC tensor formats. The library covers different architectures including CPU and NPU, and provides a reference heterogeneous schedule implementation. SHL uses a per-layer API for CPU and DSP execution, and a graph execution mode for NPU and GPU, with a modular architecture that includes Vector Instruction OPT and Driver Wrapper modules.

## Key Claims

- SHL provides a reference C implementation and assembly-optimized binaries for XuanTie CPUs.
- Supports symmetric and asymmetric quantization, and data types 8-bit, 16-bit, and FP16.
- Compatible with NCHW and NHWC tensor formats.
- Covers CPU, DSP, NPU, and GPU architectures with heterogeneous execution.
- Uses CSI-NN2 API for neural network operations.
- Buildable from source via git clone and make targets (x86 reference, C906 optimization).
- Two API modes: per-layer execution for CPU/DSP and graph execution for NPU/GPU.
- Modular architecture includes Vector Instruction OPT, Driver Wrapper, and Reference Runtime.

## Relationships

- [[c908-wino-gemm-optimization]]: SHL is the library that implements the Winograd and GEMM optimization techniques described on that page for the XuanTie C908.

## Sources

- https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/blob/master/doc/shl/introduce.adoc
merge_draft_body -->

## [2026-07-03] merge_pending | xuantie-c908.md
target_page: xuantie-c908.md
canonical_name: XuanTie C908
colliding_name: XuanTie C908
source: https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719208.html
status: pending_review
<!-- merge_draft_body
# XuanTie C908 (GCC Tuning)

The XuanTie C908 is a RISC-V core designed by T-Head (Alibaba) that implements a scalar pipeline but does not include a vector extension (RVV). GCC added a tuning and scheduler model for the C908, contributed by Milan Tripkovic, based on the XuanTie C908 R1S0 User Manual. The scheduler model covers scalar integer, load/store, multiply, divide, and floating-point pipeline resources. Long-latency reservations are clamped to 7 cycles following the existing RISC-V scheduler modelling approach. The tuning was tested on a CanMV-K230-V1.1 board running CoreMark and instruction throughput tests, achieving a 0.8% CoreMark improvement and 5-17% cycle-count improvements on instruction throughput loops. Vector scheduling is left for future work (xt-c908v). This page documents the GCC compiler support and tuning details for the C908 core.

## Key Claims

- The XuanTie C908 core does not support the vector (RVV) extension.
- GCC's scheduler model for C908 includes scalar integer, load/store, multiply, divide, and floating-point pipeline resources.
- Long-latency reservations are clamped to 7 cycles, consistent with the existing RISC-V modelling approach introduced by commit 8265192.
- The tuning was validated on a CanMV-K230-V1.1 board.
- CoreMark improvement: 0.8%.
- Instruction throughput test improvements: 5% to 17% cycle-count reduction.
- Benchmark methodology: 20 warm-up runs, 200 measured runs, aligned memory access.
- Vector scheduling is not covered in the initial patch; future work is planned under the label xt-c908v.

## Relationships

- [[c908-wino-gemm-optimization]]: Shares the XuanTie C908 hardware target but focuses on SHL software library optimizations; note that the optimization recipe assumes RVV 1.0 support, while the GCC model confirms the C908 lacks a vector extension, creating a contradiction that requires reconciliation.

## Sources

- https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719208.html
merge_draft_body -->

## [2026-07-03] pending | c908-wino-gemm-optimization.md
target_page: c908-wino-gemm-optimization.md
target_section: Key Claims or Prerequisites
source: https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719208.html
status: pending_review
proposed_update: Add a contradiction note: the GCC tuning patch submitted in June 2026 explicitly states that the C908 core does not support the vector extension (RVV), contradicting the assumption of RVV 1.0 support listed in the prerequisites and constraints (VLEN 128) of this optimization recipe. This may affect the validity of optimization techniques that rely on vector instructions (e.g., vle vector loads). The recipe should either restrict its applicability to a hypothetical SVE-like implementation or note that it targets a different C908 variant.

## [2026-07-03] merge_pending | k230-soc.md
target_page: k230-soc.md
canonical_name: K230
colliding_name: CanMV K230
source: https://deepwiki.com/kendryte/k230_canmv_docs
status: pending_review
<!-- merge_draft_body
# CanMV K230

CanMV K230 is a MicroPython-based development environment and platform designed for the Kendryte K230 AIoT System-on-Chip (SoC). Developed by Canaan Technology’s Kendryte series, the platform provides hardware abstraction layers, media processing pipelines, computer vision capabilities, and AI inference functionality optimized for edge computing applications. Its core software component is the PipeLine class, which orchestrates a dual-stream architecture: one camera stream displays directly for low-latency output, while a second stream passes through ai2d preprocessing and runs KPU (Kendryte Processing Unit) inference, with results overlaid on the display. This architecture enables real-time AI vision processing on resource-constrained embedded devices.

## Key Claims

- CanMV K230 is a MicroPython-based development environment for the Kendryte K230 AIoT SoC.
- Provides hardware abstraction, media processing pipelines, computer vision, and AI inference capabilities.
- The PipeLine class implements a dual-stream architecture: a direct display stream for low latency and a second stream with ai2d preprocessing and KPU inference with overlay.
- Optimized for edge computing applications.

## Relationships

None at this time.

## Sources

- kendryte/k230_canmv_docs on DeepWiki (https://deepwiki.com/kendryte/k230_canmv_docs)
merge_draft_body -->

## [2026-07-03] merge_pending | k230-soc.md
target_page: k230-soc.md
canonical_name: K230
colliding_name: Kendryte K230
source: https://owhinata.github.io/canmv-k230/en/
status: pending_review
<!-- merge_draft_body
# Kendryte K230

The Kendryte K230 is a system-on-chip (SoC) designed by Canaan Inc. that integrates two Xuantie C908 RISC-V 64-bit cores in a heterogeneous configuration, each running a distinct operating system. The big core (CPU1) operates at 1.6 GHz and runs the RT-Smart real-time OS, handling AI inference via the KPU (Neural Process Unit) and media processing tasks. The little core (CPU0) runs at 800 MHz with Linux 5.10.4 for system control, networking, and user interaction. The big core includes RISC-V Vector 1.0 support with a 128-bit vector length. The SoC also includes 512 MB LPDDR3 memory and a KPU accelerator that supports INT8 and INT16 quantized inference, converting ONNX and TFLite models to kmodel format using the nncase compiler. The two cores communicate through a shared filesystem at /sharefs. This SoC powers the CanMV K230 development board, which adds WiFi (2.4 GHz via Broadcom bcmdhd) and USB serial connectivity.

## Key Claims

- Dual-core heterogeneous architecture: big core at 1.6 GHz (RT-Smart) and little core at 800 MHz (Linux 5.10.4).
- Big core implements RISC-V Vector 1.0 with 128-bit vector registers.
- KPU supports INT8/INT16 quantized model inference.
- Models are compiled from ONNX/TFLite to kmodel using nncase.
- Two cores communicate via a shared filesystem (/sharefs).
- Board includes 512 MB LPDDR3 RAM and 2.4 GHz WiFi (Broadcom bcmdhd).

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit, RVV 1.0 (128-bit) on big core.
- Vector/matrix/accelerator support: KPU for AI, RVV for operators not supported by KPU (e.g., softmax).
- Memory/cache/TLB/DMA: 512 MB LPDDR3; further details not provided in this guide.
- Compiler/toolchain support: Linux 5.10.4, RT-Smart, nncase, CanMV MicroPython.

## Relationships

- [[c908-wino-gemm-optimization]]: The K230's big core is a XuanTie C908 processor; the optimization recipe for SHL-based im2col/GEMM and Winograd convolution targets the same core and applies directly to K230 deployments.

## Sources

- https://owhinata.github.io/canmv-k230/en/
merge_draft_body -->

## [2026-07-03] merge_pending | k230-soc.md
target_page: k230-soc.md
canonical_name: K230
colliding_name: K230
source: https://www.kendryte.com/en/proDetail/230
status: pending_review
<!-- merge_draft_body
# Kendryte K230

The K230 is an end-side AIoT (Artificial Intelligence of Things) system-on-chip (SoC) produced by Kendryte, featuring a dual-core RISC-V processor configuration with one core operating at 1.6 GHz and a second at 0.8 GHz. The higher-performance core (CPU1) includes a 128-bit RISC-V Vector Extension version 1.0 (RVV 1.0) and is supported by 32 KB instruction and data caches plus a 256 KB L2 cache, while the lower-power core (CPU0) runs at 0.8 GHz with 32 KB I/D caches and a 128 KB L2 cache. The chip integrates a Knowledge Processing Unit (KPU) for INT8 and INT16 neural network inference, a Depth Processing Unit (DPU) for 3D structured light depth perception, and a Video Processing Unit (VPU) supporting H.264/H.265 encoding and decoding as well as JPEG codec up to 8K resolution. The K230 targets edge-side applications including multimodal large model access terminals, interactive robots, smart cameras, smart manufacturing, and smart home devices. It is supported by multiple software development kits: a Micropython-based CanMV K230 SDK, RT-Smart SDK, Linux SDK, and a combined Linux + RT-Smart dual-core heterogeneous SDK.

## Key Claims

- Dual-core RISC-V processors: CPU1 at 1.6 GHz with RVV 1.0, CPU0 at 0.8 GHz.
- KPU supports INT8 and INT16 inference; typical performance: ResNet50 ≥85 fps, MobileNetV2 ≥670 fps, YOLOv5S ≥38 fps (INT8).
- DPU capable of 3D structured light depth computation up to 1920×1080 resolution.
- VPU: H.264/H.265 encode at 3840×2160@20 fps, decode at 3840×2160@40 fps; JPEG codec up to 8192×8192 (8K).
- Display output: MIPI DSI 1×4 lane or 1×2 lane, max 1920×1080@60 fps.
- Camera input: up to 3 MIPI CSI lanes (1×4 + 1×2 or 3×2).
- On-chip interfaces: 5 UART, 5 I2C, 6 PWM, 72 GPIO, 2 USB 2.0 OTG, 2 SD/eMMC controllers, 3 SPI (1 OSPI + 2 QSPI), WDT, RTC, Timer.
- SDKs: CanMV K230 (Micropython), RT-Smart, Linux, and Linux + RT-Smart dual-OS.

## Optimization-Relevant Details

- **ISA/profile:** RISC-V; CPU1 supports RVV 1.0 with 128-bit vector registers.
- **Vector/matrix/accelerator support:** KPU (neural network accelerator), DPU (depth engine), VPU (video codec).
- **Memory/cache/TLB/DMA:** CPU1: 256 KB L2; CPU0: 128 KB L2; 32 KB I-cache and D-cache per core. DMA details not specified.
- **Compiler/toolchain support:** Micropython, RT-Smart (C/C++), Linux (C/C++), dual-core heterogeneous SDK.

## Relationships

- [[c908-wino-gemm-optimization]]: Both the K230 (CPU1) and the XuanTie C908 implement the RVV 1.0 vector extension with a VLEN of 128 bits, though the K230's CPU1 uses a different microarchitecture and is integrated into a Kendryte SoC rather than a T-Head design. The optimization recipe for the C908 targets SHL on convolutional workloads, whereas the K230's KPU provides dedicated neural network hardware for such tasks.

## Sources

- https://www.kendryte.com/en/proDetail/230
merge_draft_body -->

## [2026-07-03] merge_pending | spacemit-k1.md
target_page: spacemit-k1.md
canonical_name: SpacemiT K1
colliding_name: SpacemiT K1
source: https://docs.banana-pi.org/en/BPI-F3/SpacemiT_K1
status: pending_review
<!-- merge_draft_body
# SpacemiT K1

SpacemiT Key Stone K1 is a high-performance, ultra-low-power SoC integrating eight RISC-V CPU cores with SpacemiT's Daoyi AI computing power. The chip is built around SpacemiT's proprietary X60 RISC-V core, which conforms to the RISC-V 64GCVB architecture and the RVA22 standard. It extends the ISA with 16 dedicated AI instructions for matrix multiplication and sliding window operations, forming an open system of instruction sets and operator libraries that can execute AI models from classical AlexNet to modern large language models such as Llama-2-7b. The K1 implements RISC-V PMP security specifications and ePMP security extensions, and supports secure boot, secure storage, signature verification, and product lifecycle security management. Memory support extends to 16 GB, and the SoC includes SDIO3.0 for SD cards and hardware video encoding/decoding for 4K resolutions in H.265, H.264, VP9, and VP8 formats.

## Key Claims

- Integrates eight RISC-V CPU cores with the proprietary X60 core design.
- The X60 core adheres to RISC-V 64GCVB and RVA22, providing 16 extended AI instructions for matrix multiplication and sliding window.
- The open instruction set and operator library support AI algorithms ranging from AlexNet to Llama-2-7b.
- Supports RISC-V PMP and ePMP security extensions, secure boot, secure storage, signature verification, and product lifecycle security management.
- Memory capacity up to 16 GB; supports SDIO3.0 SD card interface.
- Hardware video decode/encode for 4K formats: H.265, H.264, VP9, VP8.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64GCVB + RVA22, plus X60 proprietary AI extensions.
- Vector/matrix/accelerator support: 16 dedicated AI instructions for matrix multiplication and sliding window.
- Memory/cache/TLB/DMA: Not specified in source.
- Compiler/toolchain support: Not specified in source.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://docs.banana-pi.org/en/BPI-F3/SpacemiT_K1
- https://github.com/SpacemiT-OpenSource/docs-chip/blob/main/en/key_stone/k1/k1_docs/k1_ds.md (referenced in search snippets)
merge_draft_body -->

## [2026-07-03] merge_pending | sophon-sg2042.md
target_page: sophon-sg2042.md
canonical_name: SOPHON SG2042
colliding_name: Sophon SG2042
source: https://ar5iv.labs.arxiv.org/html/2309.00381
status: pending_review
<!-- merge_draft_body
# Sophon SG2042

The Sophon SG2042 is the world's first publicly available, mass-produced 64-core RISC-V CPU targeting high-performance workloads. Released in summer 2023, it is built around T-Head XuanTie C920 cores, which are marketed for high-performance computing. The SG2042 represents a significant step change in RISC-V core count and performance potential, offering a commodity platform for evaluating RISC-V in high-performance computing (HPC) contexts. Independent benchmarking using the RAJAPerf suite has shown that the SG2042 delivers, per core, between five and ten times the performance compared to the nearest widely available RISC-V hardware, while high-performance x86 CPUs commonly used in supercomputers outperform it by four to eight times for multi-threaded workloads, though some individual kernels run faster on the SG2042.

## Key Claims

- The SG2042 is the first commodity 64-core RISC-V CPU for high-performance workloads (source: paper abstract).
- Per-core performance is 5-10× that of the nearest widely available RISC-V hardware (RAJAPerf benchmarks).
- Modern x86 HPC CPUs outperform the SG2042 by 4-8× in multi-threaded workloads on average.
- Some individual kernels in the RAJAPerf suite execute faster on the SG2042 than on the x86 CPUs tested.
- The paper is described as the first independent benchmarking study of a high-performance 64-core RISC-V CPU.

## Optimization-Relevant Details

- **ISA/profile:** RISC-V (no specific extensions detailed in the paper).
- **Vector/matrix/accelerator support:** Not detailed; the C920 cores likely support some vector extensions but specifics are not in the provided content.
- **Memory/cache/TLB/DMA:** Not detailed in the provided excerpt.
- **Compiler/toolchain support:** RAJAPerf suite used; toolchain specifics not given.
- **Constraints:** 64 cores, XuanTie C920 core microarchitecture.

## Relationships

- [[c908-wino-gemm-optimization]]: Both the SG2042 and the C908 are T-Head XuanTie core products; the SG2042 uses the higher-end C920 core, while the C908 is a more efficiency-focused design with RVV 1.0 and different optimization techniques. They share the XuanTie core family but target different segments (HPC vs. AI acceleration).

## Sources

- https://ar5iv.labs.arxiv.org/html/2309.00381
- Brown, N., Jamieson, M., Lee, J., & Wang, P. (2023). Is RISC-V ready for HPC prime-time: Evaluating the 64-core Sophon SG2042 RISC-V CPU. arXiv:2309.00381.
merge_draft_body -->

## [2026-07-03] merge_pending | xiangshan-overview.md
target_page: xiangshan-overview.md
canonical_name: XiangShan
colliding_name: XiangShan
source: https://github.com/Ergou-ren/XiangShan_docs
status: pending_review
<!-- merge_draft_body
# XiangShan

XiangShan (香山) is an open-source high-performance RISC-V processor project developed by the Institute of Computing Technology, Chinese Academy of Sciences. The project employs agile development methodology to accelerate chip design, as documented in a MICRO 2022 publication. XiangShan has produced three named micro-architectures: Yanqihu (first stable version, developed since June 2020), Nanhu (second stable version), and Kunminghu (current version under development on the master branch). The design is written in Chisel and can generate Verilog code for simulation and synthesis. The repository includes submodules for a floating-point unit (fudian), an L2/L3 cache subsystem (huancun), and a difftest co-simulation framework (difftest). XiangShan provides official documentation at docs.xiangshan.cc, including a design document for Kunminghu V2R2 and a user guide, all licensed under CC-BY-4.0. Simulation is supported via Verilator with pre-built images for running programs such as CoreMark. The project also offers IDE support (bsp, IDEA) and a troubleshooting guide.

## Key Claims

- XiangShan is an open-source high-performance RISC-V processor project.
- The first stable micro-architecture is Yanqihu (released June 2020).
- The second stable micro-architecture is Nanhu.
- The current development version is Kunminghu.
- The project uses agile development methodology (MICRO 2022 paper).
- Design is implemented in Chisel and generates Verilog.
- Submodules: fudian (floating-point unit), huancun (L2/L3 cache), difftest (co-simulation framework).
- Documentation is available at docs.xiangshan.cc, licensed under CC-BY-4.0.
- Simulation can be performed with Verilator using pre-built images.
- IDE support for bsp and IDEA is available.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://github.com/Ergou-ren/XiangShan_docs
merge_draft_body -->

## [2026-07-03] merge_pending | xiangshan-overview.md
target_page: xiangshan-overview.md
canonical_name: XiangShan
colliding_name: XiangShan
source: https://deepwiki.com/OpenXiangShan/XiangShan
status: pending_review
<!-- merge_draft_body
# XiangShan

XiangShan is an open-source, high-performance out-of-order RISC-V processor implementation developed by the Institute of Computing Technology, Chinese Academy of Sciences (ICT CAS) and partners. It supports the RV64GCVH base extensions, which include the vector extension (V), and has been developed through multiple microarchitecture generations: Yanqihu (first stable release, on the yanqihu branch), Nanhu (second stable release, on the nanhu branch), and Kunminghu (current version under development on the master branch). The project was launched in June 2020 and employs an agile hardware design methodology using the Chisel hardware construction language. The verification and simulation infrastructure includes NEMU (a RISC-V emulator) and Verilator (an open-source Verilog simulator). XiangShan is reported to achieve the highest performance among open-source RISC-V processors to date, as stated in project documentation from 2023. The project has been presented at MICRO 2022 in a paper titled "Towards Developing High Performance RISC-V Processors Using Agile Methodology," which received all three available artifact evaluation badges.

## Key Claims

- XiangShan is an open-source RISC-V processor project initiated in June 2020 by ICT CAS and partners.
- It implements an out-of-order execution pipeline supporting the RV64GCVH extension set.
- Three microarchitecture generations exist: Yanqihu (stable), Nanhu (stable), and Kunminghu (in development).
- The design uses Chisel for hardware construction and agile development methodology.
- Simulation is supported through NEMU (functional emulator) and Verilator (Verilog simulator).
- The project claims to achieve the highest performance among open-source RISC-V processors.
- A paper describing the agile methodology was published at MICRO 2022 and earned artifact evaluation badges.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://deepwiki.com/OpenXiangShan/XiangShan
- https://github.com/OpenXiangShan/XiangShan
merge_draft_body -->

## [2026-07-03] merge_pending | baby-llama2-milkv-duo-benchmark.md
target_page: baby-llama2-milkv-duo-benchmark.md
canonical_name: Baby LLama2 Benchmark on Milk-V Duo
colliding_name: Baby LLama2 Optimization for Milk-V Duo
source: https://github.com/chamchamgo/rvspoc-s2311-llama2
status: pending_review
<!-- merge_draft_body
# Baby LLama2 Optimization for Milk-V Duo

This optimization recipe documents the transformations applied to the Baby LLama2 inference engine to run LLM inference on the Milk-V Duo board, a RISC-V platform with a T-Head C906 core at 1GHz, RVV 0.7 vector extension, and 64MB SDRAM. The recipe consists of five optimizations: int8 quantization to reduce memory footprint, partial on-fly dequantization to further reduce memory and improve file I/O cache, RVV intrinsic for the time-consuming matrix multiplication, a fast approximation for the exponential function, and OpenMP directives for auto-vectorization of small loops (effective only with Clang). The expected effect is a story generation speed of 24 tokens/s on the official Milk-V Duo system with 55MB memory configuration. A known failure mode is that the official Milk-V Duo GCC toolchain (version V2.6.1) cannot compile the RVV intrinsic code; the Xuantie-900-gcc-linux-5.10.4-musl32 V2.8.1 toolchain is required instead. The GCC-compiled binary is about 10% slower than Clang but smaller.

## Key Claims

- Int8 quantization reduces memory footprint and improves performance.
- Partial on-fly dequantization dramatically reduces memory footprint and improves file I/O cache performance.
- RVV intrisic instructions optimize the matrix multiplication (matmul) function.
- Fast exponential approximation replaces the standard exp() call.
- OpenMP directives enable auto-vectorization of small loops when compiled with Clang.
- The optimized binary achieves 24 tokens/s story generation speed with 55MB memory configuration.

## Transformation

- Prerequisites:
  - Milk-V Duo board with T-Head C906 core and RVV 0.7 support.
  - Linux system with free memory above 25MB (official image needs recompilation per Milk-V FAQ).
  - Xuantie-900-gcc-linux-5.10.4-musl32 V2.8.1 or Xuantie-900-llvm-linux-5.10.4-glibc V1.0.0-beta toolchain (official V2.6.1 toolchain fails on RVV intrinsics).
- Steps:
  1. Use int8 quantized model (download or convert from stories15M.pt via export.py).
  2. Modify runq.c to implement partial on-fly dequantization.
  3. Replace matmul implementation with RVV intrinsics.
  4. Replace exp() with fast approximation.
  5. Add OpenMP directives for auto-vectorization.
  6. Compile with `make runfast` (default GCC) or `COMPILER=clang make runfast`.
  7. Upload binary runq-fast and int8 model (stories15M_q80.bin) to board.
- Expected effect: 24 tokens/s story generation speed on official Milk-V Duo system with 55MB memory.
- Failure modes:
  - Official Milk-V GCC V2.6.1 cannot compile RVV intrinsic code; use V2.8.1 or Clang.
  - Clang binary is about 10% faster but larger than GCC binary.
- Measurements: 24 tokens/s reported; no further run count or statistical variation provided.

## Relationships

No specific relationship to visible context pages in this wiki. This optimization recipe targets the Milk-V Duo board with the XuanTie C906 core (RVV 0.7), which is not yet represented in existing pages for SpacemiT X60 (RVV 1.0) or C908 GCC tuning (scalar core).

## Sources

- https://github.com/chamchamgo/rvspoc-s2311-llama2
merge_draft_body -->

## [2026-07-03] merge_pending | xdsl-compiler-toolkit.md
target_page: xdsl-compiler-toolkit.md
canonical_name: xDSL
colliding_name: xDSL
source: https://github.com/xdslproject
status: pending_review
<!-- merge_draft_body
# xDSL

xDSL is a Python-native framework for building compiler infrastructure. It provides SSA-based intermediate representations (IRs) and Pythonic APIs to define, analyze, and transform programs. Originally developed as a research and teaching tool, xDSL has grown into a full-featured compiler design toolkit with support for multiple backends and integration with the MLIR ecosystem. The project is organized under the xdslproject GitHub organization, which hosts over 30 repositories covering a range of compiler-related domains: xdsl (the core toolkit), xdsl-jax (extending JAX with xDSL), xdsl-quantum (quantum compiler utilities), xdsl-torch (a reimplementation of torch-mlir), xdsl-webgpu (WebGPU support), xdsl-clang (interoperability with Clang via CIR), xdsl-asl (integrating Arm ASL in the xDSL/MLIR ecosystem), and xdsl-bench (benchmarking infrastructure for the xDSL compiler framework). The project is licensed under Apache-2.0 and is actively maintained with several hundred stars on GitHub.

## Key Claims

- xDSL is a Python-native framework for building compiler infrastructure, providing SSA-based IRs and Pythonic APIs.
- The xdslproject organization hosts over 30 repositories, including sub-projects for JAX integration, quantum computing, PyTorch, WebGPU, Clang/CIR, and benchmarking.
- xDSL is used in research to implement missing lowering stages for RISC-V Vector (RVV) code generation in the MLIR ecosystem.
- The project has active community contributions and is licensed under Apache-2.0.

## Relationships

- [[mlir-xdsl-rvv-codegen-pipeline]]: This pipeline uses custom dialects and transformation passes implemented in xDSL to bridge missing lowering stages for RVV code generation, demonstrating xDSL's role as a compiler design toolkit.
- [[mlir-xdsl-gemm-benchmark-k230-banana-pi]]: This benchmark evaluates GEMM kernels generated by the MLIR-xDSL pipeline, which relies on xDSL's infrastructure for defining and transforming intermediate representations.

## Sources

- https://github.com/xdslproject
merge_draft_body -->

## [2026-07-03] merge_pending | v851s-yuzukilizard.md
target_page: v851s-yuzukilizard.md
canonical_name: Allwinner V851S
colliding_name: Allwinner V851S
source: https://github.com/Jebumon/v851s
status: pending_review
<!-- merge_draft_body
# Allwinner V851S

The Allwinner V851S is a heterogeneous System-on-Chip (SoC) designed for IP camera and intelligent vision applications. It integrates a single ARM Cortex-A7 core clocked at 900MHz, a RISC-V E907GC core running at 600MHz, and a 0.5 TOPS INT8 neural processing unit (NPU). The SoC includes 64MB of on-package DDR2 memory and connects to a 128MB SPI NAND flash. Peripheral interfaces include MIPI DSI (2-lane, up to 1280x720@60fps), MIPI CSI (2-lane), USB, SDIO, Ethernet, and an on-board XR829 WiFi/BT module. The SoC also features a hardware H.264/H.265 decoder capable of 4096x4096 resolution and an encoder supporting 3840x2160@20fps at 400MHz. The Yuzukilizard development board implements this SoC and runs the Tina Linux operating system, which is based on OpenWrt. A Docker image with a prebuilt SDK is available for development.

## Key Claims

- Cortex-A7 core at 900MHz
- RISC-V E907GC core at 600MHz
- NPU: 0.5 TOPS at INT8 precision
- On-package 64MB DDR2 memory
- 128MB SPI NAND storage
- MIPI DSI 2-lane up to 1280x720@60fps
- MIPI CSI 2-lane
- H.264/H.265 decode 4096x4096
- H.264/H.265 encode 3840x2160@20fps@400MHz
- On-board XR829 WiFi/BT up to 150Mbps
- Runs Tina Linux (OpenWrt-based)
- Docker development image available

## Optimization-Relevant Details

- ISA/profile: Cortex-A7 (ARMv7) + RISC-V (E907GC, likely RV32IMAFC)
- Vector/matrix/accelerator support: NPU with 0.5 TOPS INT8; no vector extension on RISC-V core
- Memory/cache/TLB/DMA: 64MB on-chip DDR2; 128MB SPI NAND; no cache details
- Compiler/toolchain support: Tina Linux; Docker with prebuilt SDK

## Relationships

No specific relationship to visible context pages in this wiki.

## Sources

- https://github.com/Jebumon/v851s
merge_draft_body -->

## [2026-07-03] merge_pending | v851s-yuzukilizard.md
target_page: v851s-yuzukilizard.md
canonical_name: Allwinner V851S
colliding_name: Allwinner V851s
source: https://github.com/Jebumon/v851s/blob/master/README.md
status: pending_review
<!-- merge_draft_body
# Allwinner V851s

The Allwinner V851s is a high-performance H.264/H.265 encoding SoC targeting IP camera applications, integrating a single Cortex-A7 core at 900 MHz, a RISC-V E907GC core at 600 MHz, and a 0.5 TOPS int8 NPU for AI inference. The SoC includes 64 MB of built-in DDR2 memory, supports 128 MB SPI NAND flash, and provides interfaces for TF card, XR829 WiFi/BT, MIPI DSI (up to 1280×720@60fps), MIPI CSI, and an ISP with maximum resolution of 2560×1440. Video encoding and decoding capabilities include H.264/H.265 at up to 4096×4096 for decoding and 3840×2160@20fps for encoding. The V851s is used in the Yuzukilizard development board, which runs Tina Linux (based on OpenWrt). A Docker image is provided for SDK development, and the hardware design files are licensed under CERN Open Hardware Licence Version 2 - Strongly Reciprocal.

## Key Claims

- SoC includes a Cortex-A7 application core at 900 MHz and a RISC-V E907GC coprocessor at 600 MHz.
- Integrated NPU delivers 0.5 TOPS for int8 inference workloads.
- Built-in 64 MB DDR2 memory and 128 MB SPI NAND storage.
- XR829 WiFi and Bluetooth module supports up to 150 Mbps.
- MIPI DSI supports display up to 1280×720 at 60 fps.
- MIPI CSI with ISP supports camera input up to 2560×1440.
- H.264/H.265 decoder handles 4096×4096 resolution.
- H.264/H.265 encoder handles 3840×2160 at 20 fps (400 MHz).
- Software support via Tina Linux (OpenWrt-based) and a Docker image for development.

## Optimization-Relevant Details

- ISA/profile: Cortex-A7 (ARMv7-A) and RISC-V E907GC (RV32IMAFC, no vector extension confirmed).
- Vector/matrix/accelerator support: Dedicated 0.5 TOPS int8 NPU, no RISC-V vector extension.
- Memory/cache/TLB/DMA: 64 MB DDR2 (integrated), 128 MB SPI NAND; no detailed cache hierarchy provided.
- Compiler/toolchain support: Tina Linux SDK; a Docker image with prebuilt environment is available.

## Relationships

- [[baby-llama2-milkv-duo-benchmark]] – Both the Yuzukilizard (Allwinner V851s) and Milk-V Duo integrate a RISC-V core for coprocessing, but they use different core implementations: the V851s uses the Allwinner E907GC at 600 MHz paired with a dedicated 0.5 TOPS int8 NPU, whereas the Milk-V Duo uses the XuanTie C906 at 1 GHz with RVV 0.7 and no on-chip NPU, relying on software-optimized inference for comparable AI tasks.

## Sources

- https://github.com/Jebumon/v851s/blob/master/README.md
merge_draft_body -->

## [2026-07-03] merge_pending | v851s-yuzukilizard.md
target_page: v851s-yuzukilizard.md
canonical_name: Allwinner V851S
colliding_name: Allwinner V851s
source: https://linux-sunxi.org/V851s
status: pending_review
<!-- merge_draft_body
# Allwinner V851s

The Allwinner V851s is a system-on-chip (SoC) designed for the IP-camera market, integrating an ARM Cortex-A7 CPU core clocked at 900MHz with NEON and VFPv4 extensions, a RISC-V CPU core running at 600MHz (ISA extensions unknown), a 0.5 TOPS NPU (reportedly Vivante IP), and 64MB of SiP DDR2 memory. It also includes a Cedar Engine VPU for video processing, connectivity interfaces such as RGB, MIPI-DSI, MIPI-CSI, audio interfaces including I2S and DMIC, and storage support for SD Card 3.0 and eMMC 4.5. The V851s is recommended by Allwinner as a replacement for the NRND V3s. A variant, the V851SE, integrates an Ethernet PHY but differs in pin-muxing. Currently, there is no mainline Linux kernel or U-Boot support for this chip, though bootloaders awboot and xboot provide support. The pinctrl is reportedly similar to the D1 pinctrl, and the chip contains two clock control units (CCUs). The V851s is manufactured by Allwinner and targets the embedded Linux camera segment.

## Key Claims

- Contains ARM Cortex-A7 processor at 900MHz with NEON and VFPv4 co-processors.
- Contains a RISC-V core at 600MHz with unknown ISA extensions.
- NPU rated at 0.5 TOPS, believed to be Vivante IP.
- 64MB of SiP DDR2 memory.
- Cedar Engine VPU for video encode/decode.
- No mainline Linux kernel or U-Boot support as of the source date.
- V851SE variant adds an integrated Ethernet PHY with different pin-muxing.
- Pinctrl is very similar to D1 pinctrl but with different muxing.
- Two CCUs: a regular one and a PRCM for the RISC-V core.
- Peripheral driver compatibility documented for various blocks (e.g., RTC, USB, SPI, MMC).

## Optimization-Relevant Details

- ISA/profile: ARM Cortex-A7 (ARMv7-A) with NEON, VFPv4; RISC-V (unspecified, likely RV64 with unknown vector support)
- Vector/matrix/accelerator support: NEON on ARM side; NPU (Vivante IP) for AI workloads
- Memory/cache/TLB/DMA: 64MB SiP DDR2; no further cache hierarchy details provided
- Compiler/toolchain support: No mainline Linux; awboot and xboot support boot; driver compatibility documented for mainline U-Boot and kernel drivers (e.g., sun20i-d1-dma, sun20i-d1-mmc)

## Relationships

No specific relationship to visible context pages in this wiki. The V851s is a distinct Allwinner SoC with an ARM/RISC-V/NPU architecture, not directly comparable to the existing XuanTie C906-based Milk-V Duo benchmark page.

## Sources

- https://linux-sunxi.org/V851s
merge_draft_body -->
