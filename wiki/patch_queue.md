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

## [2026-07-03] merge_pending | riscv-matrix-extension-specification.md
target_page: riscv-matrix-extension-specification.md
canonical_name: RISC-V Matrix Extension Specification
colliding_name: RISC-V Matrix Extension Specification
source: https://github.com/XUANTIE-RV/riscv-matrix-extension-spec
status: pending_review
<!-- merge_draft_body
# RISC-V Matrix Extension Specification

The RISC-V Matrix Extension Specification is a proposal for a matrix computation extension to the RISC-V architecture, targeting AI applications. Developed by Alibaba's T-Head (Xuantie) and currently at version 0.6.0, it introduces new register types and instructions for matrix operations. Key features include separated source (tile) and accumulation registers of different sizes, adjustable matrix register shapes (rows and columns are no longer limited to RLEN/32), and additional element-wise instructions to support operator fusion. The specification is accompanied by a software ecosystem that includes the SHL 2.0 neural network library, the HHB deployment toolkit, a QEMU emulator with matrix extension support, and a GNU toolchain with compiler and assembler support. The project also provides evaluation demos for ResNet50 and GEMM kernels. The extension remains under active development, with this repository serving as a preview demo project; the specification documents are built using AsciiDoctor and can be generated as PDFs. The simulator GEM5-RVME provides a detailed microarchitectural model of the extension.

## Key Claims

- The RISC-V Matrix Extension is at version 0.6.0 and is a proposal for AI-focused matrix operations under the RISC-V architecture.
- It introduces a separation between source tile registers and accumulation registers, allowing source and destination registers of different sizes.
- The matrix register shape is flexible: the number of rows and columns can be adjusted independently, supporting configurations from pure outer products to pure inner products.
- New element-wise instructions have been added to facilitate operator fusion.
- The extension is supported by a software stack including SHL 2.0 (a neural network library), HHB (a model deployment toolkit), a QEMU emulator with matrix extension support, and a GNU toolchain (GCC, binutils).
- Evaluation demos for ResNet50 and GEMM are provided to demonstrate performance.
- The specification is still under construction; this repository is a preview demo project.
- The GEM5-RVME simulator provides a detailed microarchitectural model for the extension.

## Relationships

- [[xuantie-c906-hardware-target]]: The XuanTie C906 core uses custom SIMD instructions but does not implement the RISC-V Matrix Extension; the Matrix Extension is a separate proposal that may target future XuanTie cores for matrix-intensive AI workloads.
- [[mlir-xdsl-rvv-codegen-pipeline]]: Both target AI computation on RISC-V; the MLIR-xDSL pipeline generates RVV code for GEMM kernels, while the Matrix Extension proposes dedicated matrix instructions that could complement or replace vector-based approaches for similar workloads.
- [[spacemit-x60-hardware-target]]: The SpacemiT X60 implements RVV 1.0 for vector operations; the Matrix Extension proposes a complementary matrix-level instruction set not yet supported on the X60, representing a different approach to AI acceleration on RISC-V.

## Sources

- https://github.com/XUANTIE-RV/riscv-matrix-extension-spec
merge_draft_body -->

## [2026-07-03] merge_pending | riscv-matrix-extension-specification.md
target_page: riscv-matrix-extension-specification.md
canonical_name: RISC-V Matrix Extension Specification
colliding_name: RISC-V Matrix Extension Specification
source: https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/tree/v0.4.0
status: pending_review
<!-- merge_draft_body
# RISC-V Matrix Extension Specification

The RISC-V Matrix Extension Specification is a matrix extension proposal for AI applications under the RISC-V architecture, developed by T-Head (Xuantie RV). It defines scalable register sizes ranging from 64 bytes to 2048 bytes with peak performance varying from 0.125 Tops/GHz to 32 Tops/GHz. The extension supports multiple data types including int4, int8, int16, fp16, bf16, and fp32, and is designed for binary portability across implementations. It is strongly inspired by the RISC-V Vector extension but maintains a decoupled architecture, allowing independent evolution. The specification is extensible for future data types such as fp8 and fp4. As of v0.4.0, the specification is under active development and includes supporting tooling: a neural network library (SHL 2.0), a model deployment toolkit (HHB), an emulator (QEMU with matrix extension support), a GNU toolchain with matrix extension support, and an intrinsic API reference manual. The project is hosted on GitHub under the XUANTIE-RV organization and is licensed under Apache-2.0.

## Key Claims

- The RISC-V Matrix Extension is a matrix extension proposal for AI workloads under the RISC-V ISA, developed by T-Head.
- Register sizes are scalable from 64 bytes to 2048 bytes.
- Peak performance ranges from 0.125 Tops/GHz to 32 Tops/Ghz, depending on register size.
- Supported data types include int4, int8, int16, fp16, bf16, and fp32, with planned extensibility for fp8, fp4, and future types.
- The extension is binary portable across implementations.
- It is decoupled from the RISC-V Vector extension, though inspired by it, allowing independent feature evolution.
- The specification includes a tool ecosystem: SHL 2.0 (neural network library), HHB (deployment toolkit), QEMU emulator with matrix support, and a GNU toolchain with matrix intrinsics.
- As of v0.4.0, the extension is under construction and provided as a preview demo project.
- The specification also defines a Matrix Extension ABI Manual, an intrinsic API Reference Manual, and includes demos for GEMM and ResNet50 evaluation.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/tree/v0.4.0
merge_draft_body -->

## [2026-07-03] merge_pending | riscv-matrix-extension-specification.md
target_page: riscv-matrix-extension-specification.md
canonical_name: RISC-V Matrix Extension Specification
colliding_name: RISC-V Matrix Extension
source: https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/blob/master/demos/README.md
status: pending_review
<!-- merge_draft_body
# RISC-V Matrix Extension

The RISC-V Matrix Extension is an ISA extension for RISC-V processors that introduces matrix multiply-accumulate (MMA) instructions and associated intrinsic functions for efficient execution of dense linear algebra and neural network workloads. The extension is defined in the riscv-matrix-extension-spec repository maintained by XUANTIE-RV, the RISC-V processor team of Alibaba Group's T-Head business. It provides instructions for matrix multiplication with integer (int8) and floating-point (fp16) data types, and is designed to accelerate general matrix multiply (GEMM) and convolution operations common in deep learning inference. The extension is complementary to the RISC-V Vector Extension (RVV) and targets higher computational density for matrix operations by leveraging specialized matrix register files and execution units. Complete C code model implementations and intrinsic demos are provided in the specification repository to facilitate evaluation and adoption.

## Key Claims

- The RISC-V Matrix Extension defines matrix multiply-accumulate instructions for int8 and fp16 datatypes.
- The specification includes C code models and intrinsic-based demos for GEMM and matrix multiplication.
- Demo applications include gemm_int8, gemm_fp16, resnet50_int8, resnet50_fp16, and matmul.
- Benchmarks against the RISC-V Vector Extension (RVV) 1.0 show speedups of 5.28x–7.36x on ResNet50 and 9.76x–15.44x on GEMM (160x160x160).
- The extension is maintained by XUANTIE-RV (T-Head / Alibaba) and is available as open source under the riscv-matrix-extension-spec repository.

## Relationships

- [[risc-v-matrix-extension-demo-benchmarks]]: The entity defines the ISA extension whose performance is evaluated in the demo benchmark results.
- [[mlir-xdsl-rvv-codegen-pipeline]]: Both are RISC-V optimization approaches for matrix workloads; the Matrix Extension provides an ISA-level solution, while the MLIR-xDSL pipeline is a compiler-driven approach targeting RVV.
- [[c908-wino-gemm-optimization]]: Both address GEMM acceleration on RISC-V; the extension offers a hardware-level matrix instruction set, in contrast to the library-level algorithmic optimizations in SHL for the XuanTie C908.

## Sources

- https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/blob/master/demos/README.md
merge_draft_body -->

## [2026-07-03] merge_pending | xuantie-c908.md
target_page: xuantie-c908.md
canonical_name: XuanTie C908
colliding_name: XuanTie C908
source: https://github.com/FreeRTOS/FreeRTOS-Community-Supported-Demos/blob/main/RISC-V_XUANTIE_C908_GCC/README.md
status: pending_review
<!-- merge_draft_body
# XuanTie C908

The XuanTie C908 is a 64-bit RISC-V processor core developed by Alibaba's T-Head Semiconductor, designed as a higher-performance successor to the C906. It is used in SoCs such as the Canaan Kendryte K230, which powers development boards like the CanMV-K230-V1.1 and XIAOHUI EVB. The core supports optional floating-point and vector extensions selected via the GCC `-mcpu=c908v` flag, or a scalar-only configuration via `-mcpu=c908`. The FreeRTOS community-supported port for the C908 defines memory-mapped interrupt controllers: PLIC base at `0x08000000` and CLINT base at `0x0c000000`. The port supports a configurable number of cores (1 to 4) with a default of 1, an interrupt stack size of 8192 bytes, and an initial task stack of 4096 bytes. The board-specific configuration selects `CONFIG_BOARD_XIAOHUI_EVB` as the target hardware. The C908 requires the medium-any code model (`-mcmodel=medany`) for compilation and is supported by the GCC toolchain with the `-Os` size optimization recommended.

## Key Claims

- The XuanTie C908 is a 64-bit RISC-V core from T-Head with optional floating-point and vector extensions (RVV 1.0 implied by the `-mcpu=c908v` flag).
- The FreeRTOS port for C908 maps PLIC at `0x08000000` and CLINT at `0x0c000000`.
- The port uses a configurable core count (1–4) with `configNUMBER_OF_CORES`.
- The default board target is `XIAOHUI_EVB`.
- Compilation requires `-mcmodel=medany` and `-Os` is recommended.
- The port includes custom assembly files for context switching (`cpu_task_sw.S`) and a `portmacro.h` with port-specific macros.
- The C908 is the CPU in the CanMV-K230 board, which is also the hardware target for GCC tuning benchmarks.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit (implied RV64GC with optional V extension)
- Vector/matrix/accelerator support: Optional via `-mcpu=c908v` (RVV)
- Memory/cache/TLB/DMA: Not specified in this source, but known from K230: 32KB L1 I-cache, 32KB L1 D-cache, 128KB L2 cache (from other K230 documentation)
- Compiler/toolchain support: GCC with `-mcpu=c908` or `-mcpu=c908v`; FreeRTOS port available

## Relationships

- [[xuantie-c906-hardware-target]]: Both the XuanTie C908 and C906 are 64-bit RISC-V cores from Alibaba T-Head; the C908 adds optional RVV vector support and targets the CanMV-K230 board, while the C906 uses a custom 128-bit SIMD vector unit and is found in the Allwinner D1.
- [[gcc-tuning-c908-canmv-k230]]: The FreeRTOS port and the GCC tuning benchmark target the same XuanTie C908 hardware on the CanMV-K230 board; the benchmark validates the scheduler model for which this hardware provides the microarchitectural constraints.
- [[spacemit-x60-hardware-target]]: Both the XuanTie C908 and SpacemiT X60 are in-order RISC-V cores with optional RVV 1.0 support; the C908 is single-issue while the X60 is dual-issue, and they originate from different vendors (T-Head vs. SpacemiT).

## Sources

- https://github.com/FreeRTOS/FreeRTOS-Community-Supported-Demos/blob/main/RISC-V_XUANTIE_C908_GCC/README.md
merge_draft_body -->

## [2026-07-03] merge_pending | xuantie-c908.md
target_page: xuantie-c908.md
canonical_name: XuanTie C908
colliding_name: XuanTie C908
source: https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719208.html
status: pending_review
<!-- merge_draft_body
# XuanTie C908

XuanTie C908 is a 64-bit RISC-V processor core designed by Alibaba's T-Head Semiconductor Co., Ltd., targeting embedded and edge applications. It implements a scalar in-order pipeline (pipeline depth not publicly documented) and lacks a vector extension, distinguishing it from other XuanTie family members such as the C906 which includes a 128-bit SIMD vector unit. The C908 is the central core in the CanMV-K230 development board (K230 SoC) and is supported by the GCC compiler through a dedicated tuning and scheduler model patch that models scalar integer, load/store, multiply, divide, and floating-point pipeline resources. The scheduler model is based on the XuanTie C908 R1S0 User Manual and was validated on a CanMV-K230-V1.1 board, achieving a 0.8% improvement in CoreMark score and 5–17% cycle-count reductions on instruction throughput tests using independent register groups.

## Key Claims

- XuanTie C908 is a 64-bit RISC-V core without vector extension, using a scalar in-order pipeline.
- The core powers the CanMV-K230 development board (K230 SoC).
- A GCC patch (2026-06-03) adds a scheduler model covering scalar integer, load/store, multiply, divide, and floating-point pipeline resources based on the C908 R1S0 User Manual.
- Benchmark results on CanMV-K230-V1.1 show a 0.8% CoreMark improvement and 5–17% cycle-count improvement on instruction throughput loops.
- Long-latency reservations are clamped to 7 cycles following existing RISC-V scheduler modelling practice.
- Measurement methodology: 20 warm-up runs, 200 measured runs, aligned memory access.
- The patch initially omitted vector instruction types because the C908 does not support the vector extension; Jeffrey Law noted that all instruction types must still be covered with dummy reservations to avoid compiler errors.

## Optimization-Relevant Details

- ISA/profile: 64-bit RISC-V scalar (no vector extension supported).
- Vector/matrix/accelerator support: None.
- Memory/cache/TLB/DMA: Not specified in the source.
- Compiler/toolchain support: GCC (patch submitted June 2026, pre-trunk).

## Relationships

- [[xuantie-c906-hardware-target]]: Both the XuanTie C906 and C908 are 64-bit RISC-V in-order single-issue cores from T-Head; the C906 includes a 128-bit SIMD vector unit while the C908 lacks vector support and uses only scalar scheduling.
- [[gcc-tuning-c908-canmv-k230]]: The GCC tuning page documents the benchmark results of the scheduler model described here; the scheduler model defines the pipeline resources whose performance was measured.
- [[spacemit-x60-hardware-target]]: Both the C908 and SpacemiT X60 are RISC-V cores with in-order scalar pipelines and dedicated GCC tuning patches; however, the X60 is dual-issue and supports RVV 1.0, whereas the C908 is single-issue and lacks vector support.

## Sources

- https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719208.html
merge_draft_body -->

## [2026-07-03] merge_pending | xuantie-gnu-toolchain.md
target_page: xuantie-gnu-toolchain.md
canonical_name: XuanTie GNU Compiler Toolchain
colliding_name: XuanTie GNU Toolchain
source: https://github.com/XUANTIE-RV/xuantie-gnu-toolchain/
status: pending_review
<!-- merge_draft_body
# XuanTie GNU Toolchain

The XuanTie GNU Toolchain is a cross-compiler suite for RISC-V architectures, maintained by the XUANTIE-RV organization, specifically supporting Alibaba/T-Head XuanTie processor cores. It provides both a generic ELF/Newlib toolchain for bare-metal or RTOS environments and a Linux-ELF/glibc toolchain for Linux-based systems. The toolchain supports building for RV32 and RV64 base architectures with standard extensions including atomic (A), multiplication and division (M), single-precision float (F), double-precision float (D), and compressed instructions (C). It can be configured with various ABIs (ilp32, ilp32d, ilp32f, lp64, lp64f, lp64d) and architecture variants like rv32gc and rv64gc. Prebuilt binaries are available through the Open Chip Community portal, and the source is hosted on GitHub. Build dependencies are documented for Ubuntu, Fedora, CentOS, Arch Linux, and macOS; the process downloads about 200 MiB of upstream sources and requires approximately 8 GiB of disk space.

## Key Claims

- The toolchain offers two build modes: Newlib (bare-metal) and glibc (Linux), selected via `make` or `make linux` after configuration.
- It supports architecture strings rv32i/rv64i with standard extensions (A, M, F, D, C, or G for MAFD).
- Supported ABIs include ilp32, ilp32d, ilp32f, lp64, lp64f, and lp64d.
- Multilib builds (enabled with `--enable-multilib`) produce a single compiler capable of targeting both 32-bit and 64-bit with common `-march`/`-mabi` options.
- Build dependencies are listed for Ubuntu, Fedora/CentOS/RHEL, Arch Linux, and macOS (via Homebrew).
- Prebuilt toolchains can be downloaded from the OCC resource center at https://www.xrvm.cn/community/download.
- Troubleshooting guidance: use an empty install directory to prevent hard-float/soft-float conflicts; a case-sensitive filesystem is required for glibc builds on macOS; CentOS/RHEL users may need devtoolset-7 for current GNU tools.

## Relationships

- [[xuantie-c906-hardware-target]]: The XuanTie GNU Toolchain provides the GCC compiler used to compile code for the XuanTie C906, supporting its custom instruction extensions and 128-bit SIMD vector unit.
- [[gcc-tuning-c908-canmv-k230]]: The GCC tuning patches for the XuanTie C908 are built upon the XuanTie GNU Toolchain, and the benchmark results demonstrate the scheduler model validated using this compiler.

## Sources

- https://github.com/XUANTIE-RV/xuantie-gnu-toolchain/
merge_draft_body -->

## [2026-07-03] merge_pending | gcc-tuning-c908-canmv-k230.md
target_page: gcc-tuning-c908-canmv-k230.md
canonical_name: GCC Tuning Benchmark on XuanTie C908
colliding_name: XuanTie C908 GCC Tuning
source: https://www.mail-archive.com/gcc-patches@gcc.gnu.org/msg406284.html
status: pending_review
<!-- merge_draft_body
# XuanTie C908 GCC Tuning

The XuanTie C908 GCC tuning patch, submitted in June 2026 by Milan Tripkovic, defines a scheduler model for the XuanTie C908 RISC-V core within the GCC compiler backend. The model describes scalar integer, load/store, multiply, divide, and floating-point pipeline resources based on the XuanTie C908 R1S0 User Manual. It is the first GCC tuning specifically for the C908 core and targets in-order scalar scheduling only, leaving vector scheduling for future work (xt-c908v). The tuning was tested on a CanMV-K230-V1.1 board and resulted in a 0.8% CoreMark improvement and 5-17% cycle-count improvements on instruction throughput loops. The patch also introduced clamping of long-latency reservations to 7 cycles, following the existing RISC-V scheduler modelling approach. During review, Jeffrey Law noted that all instruction types must have reservations in the GCC RISC-V backend and recommended adding dummy reservations for unused types, similar to the SpacemiT X60 tuning, to avoid compilation failures (ICE).

## Key Claims

- The GCC scheduler model for XuanTie C908 models scalar integer, load/store, multiply, divide, and FP pipeline resources based on the XuanTie C908 R1S0 User Manual.
- Scalar-only scheduling implementation; vector scheduling is deferred to a future xt-c908v model.
- Tested on CanMV-K230-V1.1 board with 20 warm-up runs followed by 200 measured runs using aligned memory access.
- CoreMark improvement: 0.8%; instruction throughput loop cycle-count improvements: 5% to 17%.
- Long-latency reservations are clamped to 7 cycles, following the existing RISC-V scheduler modelling approach introduced by commit 8265192.
- Reviewer identified that missing instruction type reservations cause an ICE during scheduling; the fix requires covering all insn types, including dummy reservations for types not relevant to the C908 microarchitecture.

## Transformation

- **Prerequisites**: XuanTie C908 core (R1S0 revision); GCC source tree for RISC-V backend; access to a CanMV-K230-V1.1 board for testing.
- **Steps**:
  1. Add a new `riscv_microarchitecture_type` entry for `xt-c908` in `riscv-opts.h` and a corresponding `RISCV_TUNE` entry in `riscv-cores.def` with `PIPELINE_MODEL` and `TUNE_INFO`.
  2. Define the new tune structure in `riscv.cc`.
  3. Create `xt-c908.md` with define_insn_reservation rules for scalar pipeline resources.
  4. Include `xt-c908.md` in `riscv.md`.
  5. Ensure every `insn` type has a reservation (including dummy reservations for unused types like vector crypto instructions) using the pipeline-checker script.
- **Expected effect**: Reduced pipeline stalls for in-order scalar code, yielding 0.8% CoreMark improvement and 5-17% cycle-count improvements on throughput-intensive unrolled loops.
- **Failure modes**: Missing insn-type reservations cause an ICE during instruction scheduling; all types defined in the GCC backend must have corresponding reservation rules (even if they are dummy single-cycle reservations).
- **Measurements**: The benchmark methodology used 20 warm-up iterations and 200 measured iterations with aligned memory access. Results are reported as measured evidence.

## Relationships

- [[gcc-tuning-c908-canmv-k230]]: This optimization recipe describes the GCC tuning patch that produced the benchmark results reported in that page; the benchmark result provides the performance validation for the scheduler model defined here.
- [[xuantie-c906-hardware-target]]: Both the XuanTie C906 and C908 are T-Head in-order single-issue RISC-V cores with GCC tuning; however, the C906 includes a 128-bit SIMD vector unit while the C908 is entirely scalar and lacks any vector extension, making their scheduler models fundamentally different.
- [[spacemit-x60-hardware-target]]: Both the XuanTie C908 and SpacemiT X60 have GCC tuning patches that model in-order scalar pipelines using the same RISC-V backend infrastructure and both required dummy reservations for unsupported instruction types; however, the X60 tuning additionally models dual-issue capabilities and an RVV 1.0 vector unit.

## Sources

- https://www.mail-archive.com/gcc-patches@gcc.gnu.org/msg406284.html
merge_draft_body -->

## [2026-07-03] merge_pending | integrated-matrix-extension.md
target_page: integrated-matrix-extension.md
canonical_name: Integrated Matrix Extension
colliding_name: RISC-V IME Extension
source: https://deepwiki.com/spacemit-com/riscv-ime-extension-spec
status: pending_review
<!-- merge_draft_body
# RISC-V IME Extension

The RISC-V Intelligent Matrix Engine (IME) extension is a high-performance matrix multiplication and convolution acceleration proposal designed by SpacemiT. It extends the standard RISC-V Vector (RVV) by introducing a suite of matrix multiply-accumulate (MAC) operations that reuse existing vector registers and associated CSRs, enabling high-throughput dot-product capabilities with minimal hardware overhead. The extension supports vector lengths (VLEN) from 128 bits to 4096 bits, providing compatibility across a wide range of implementations while maintaining almost binary compatibility. By reusing vector resources, the IME extension aims to deliver more than a tenfold performance improvement for AI applications such as matrix multiplication and convolution at a very small hardware cost. The specification is authored in AsciiDoctor and follows standard RISC-V documentation conventions; the project is open-source on GitHub and organized for easy building and contribution.

## Key Claims

- Reuses vector registers and CSRs, minimizing hardware overhead compared to dedicated matrix units.
- Supports VLEN from 128 bits to 4096 bits for broad implementation compatibility.
- Achieves >10x performance improvement for AI matrix multiplication and convolution workloads.
- Designed for almost binary compatibility across different VLEN configurations.
- Authored in AsciiDoctor, open-source under SpacemiT on GitHub.

## Relationships

No specific relationship to visible context pages in this wiki. The IME extension is a new ISA extension specification not yet represented in the existing page set.

## Sources

- https://github.com/spacemit-com/riscv-ime-extension-spec
- https://deepwiki.com/spacemit-com/riscv-ime-extension-spec
merge_draft_body -->

## [2026-07-03] merge_pending | opengemm.md
target_page: opengemm.md
canonical_name: OpenGeMM
colliding_name: OpenGeMM
source: https://www.researchgate.net/publication/385823001_OpenGeMM_A_High-Utilization_GeMM_Accelerator_Generator_with_Lightweight_RISC-V_Control_and_Tight_Memory_Coupling
status: pending_review
<!-- merge_draft_body
# OpenGeMM

OpenGeMM is an open-source acceleration platform for General Matrix Multiplication (GeMM) designed for edge AI applications. It combines a parameterized Chisel-coded GeMM hardware accelerator with a lightweight RISC-V processor and a tightly coupled multi-banked scratchpad memory system. To achieve high hardware utilization, OpenGeMM introduces three system-level mechanisms: configuration pre-loading, input pre-fetching with output buffering, and programmable strided memory access. The accelerator is designed to be configurable and programmable, targeting diverse CNN and Transformer workloads. Experimental results reported in the paper demonstrate sustained hardware utilization ranging from 81.89% to 99.34% across these workloads, though specific hardware targets and measurement conditions are not detailed in available excerpts. The platform is open-source and aims to fill the gap between efficiency, utilization, configurability, and programmability in GeMM accelerators for RISC-V based edge systems.

## Key Claims

- OpenGeMM is an open-source acceleration platform for GeMM with a Chisel-based accelerator generator.
- It incorporates a lightweight RISC-V processor for control and a tightly coupled multi-banked scratchpad memory.
- Three system-level mechanisms enhance utilization: configuration pre-loading, input pre-fetching with output buffering, and programmable strided memory access.
- The accelerator can be parameterized and configured at design time and runtime.
- Reported hardware utilization ranges from 81.89% to 99.34% across diverse CNN and Transformer workloads, demonstrating high efficiency.
- The platform is suitable for edge AI applications requiring both high performance and programmability.

## Relationships

- [[mlir-xdsl-rvv-codegen-pipeline]]: OpenGeMM implements GEMM acceleration in hardware using a Chisel-based generator with a lightweight RISC-V control core, whereas the MLIR-xDSL pipeline uses compiler-driven code generation to produce RVV software kernels for GEMM on RISC-V platforms, representing a hardware-software design trade-off.

## Sources

- https://arxiv.org/abs/2411.09543
- https://www.researchgate.net/publication/385823001_OpenGeMM_A_High-Utilization_GeMM_Accelerator_Generator_with_Lightweight_RISC-V_Control_and_Tight_Memory_Coupling
merge_draft_body -->

## [2026-07-03] merge_pending | iree-rvv-mlir-ukernel.md
target_page: iree-rvv-mlir-ukernel.md
canonical_name: IREE MLIR-based uKernel for RVV
colliding_name: IREE MLIR Ukernels for RVV
source: https://github.com/iree-org/iree/issues/22720
status: pending_review
<!-- merge_draft_body
# IREE MLIR Ukernels for RVV

The IREE MLIR Ukernels for RVV is a proposed compiler transformation within the IREE project to implement micro-kernels (ukernels) for the RISC-V Vector (RVV) extension using the MLIR `vector` dialect. The approach follows the GPU backend's precedent of declarative, tensor-based ukernels. Prerequisites include a working MLIR toolchain with RVV support in LLVM, the IREE compiler with CPU target support, and a RISC-V platform implementing RVV with vector length 128 and the `zfh` half-precision floating-point extension. The expected effect is to enable automatic producer/consumer fusion (e.g., matrix multiply followed by bias addition and activation) via standard MLIR passes, while delegating instruction selection to the LLVM backend. Failure modes are not documented; the design is contingent on the correctness of the MLIR-to-LLVM-IR conversion for vector operations targeting RVV. No performance measurements are yet available as the implementation is currently proposed and not built or run.

## Key Claims

- The MVP is a single f16*f16->f32 mixed-precision matmul ukernel for vlen=128 RVV with zfh extension.
- The implementation uses generic MLIR `vector` dialect operations (`vector.fma`, `vector.load`, `vector.store`, `vector.broadcast`) rather than introducing a target-specific dialect.
- Data tiling is specified via a proposed `#iree_cpu.data_tiled_layout` attribute with tile sizes [8,8,1] and inner blocking order [0,1,2].
- Ukernel matching is constrained by a `cpu_feature` requirement (`+v`, `+zfh`).
- The design enables compiler fusion: bias addition and activation can be fused with the matmul via the `%init` accumulator argument.
- The LLVM backend is responsible for generating optimal RVV instructions (e.g., `vfmacc.vf`, `vle16.v`, `vse32.v`).

## Transformation

- Prerequisites:
  - MLIR toolchain with full support for RVV lowering (verification needed).
  - IREE compiler with CPU target backend and support for declarative ukernel attributes.
  - RISC-V hardware platform implementing RVV 1.0 with vlen=128 and the `zfh` extension.
- Steps:
  1. Verify that MLIR `vector` dialect operations (`vector.fma`, `vector.broadcast`, `vector.load`, `vector.store`) are correctly lowered to efficient RVV instructions by the LLVM backend. If gaps exist, contribute missing lowering patterns to upstream MLIR/LLVM.
  2. Implement IREE infrastructure for CPU ukernel declaration: create the `#iree_cpu.data_tiled_layout` MLIR attribute to describe optimal data tiling, and implement a `cpu_feature` constraint for ukernel matching.
  3. Define and implement the RVV matmul ukernel as a self-contained `.mlir` file (`iree_uk_riscv_dt_matmul_f16f16f32.mlir`) with declarative metadata and implementation using generic `vector` ops.
- Expected effect: Automatic fusion of matmul with bias and activation operations via standard MLIR compiler passes, enabling portable, target-specific RVV code generation without hand-tuned assembly.
- Failure modes: Not documented; the approach assumes that the MLIR-to-LLVM-IR conversion and LLVM instruction selector correctly lower the generic vector operations to performant RVV instructions.
- Measurements: None yet; the work is a proposal and has not been implemented or benchmarked.

## Relationships

- [[mlir-xdsl-rvv-codegen-pipeline]]: Both address the missing lowering path for RVV code generation from MLIR, but the IREE ukernel approach uses the MLIR `vector` dialect and relies on LLVM's backend for instruction selection, whereas the MLIR-xDSL pipeline implements custom lowering stages using xDSL to emit C code with RVV intrinsics.

## Sources

- https://github.com/iree-org/iree/issues/22720
merge_draft_body -->

## [2026-07-03] pending | spacemit-k1.md
target_page: spacemit-k1.md
target_section: Relationships
source: https://link.springer.com/chapter/10.1007/978-981-96-9869-1_43
status: pending_review
proposed_update: Add relationship link to [[bpi-f3-rvv-llm-benchmark]]: 'The BPI-F3 LLM inference benchmark with RVV-optimized llama.cpp validates the practical performance of the SpacemiT K1 RVV 1.0 extensions on representative LLM workloads.'

## [2026-07-03] merge_pending | llamacpp-quantization-methods.md
target_page: llamacpp-quantization-methods.md
canonical_name: llama.cpp Quantization Methods
colliding_name: GGML Quantization
source: https://deepwiki.com/ggml-org/llama.cpp/7.3-quantization-techniques
status: pending_review
<!-- merge_draft_body
# GGML Quantization

GGML Quantization refers to the block-based quantization system implemented in the GGML tensor library and used by llama.cpp for compressing neural network model weights. Instead of quantizing each weight independently, GGML divides tensors into small blocks, and each block is assigned its own scale factor and optionally a minimum value to minimize precision loss. This approach allows representing high-precision 16-bit or 32-bit floating-point weights in lower-bit formats such as 4-bit, 2-bit, or even ternary representations, significantly reducing memory footprint and accelerating inference on consumer hardware. The quantization system supports multiple formats ranging from Q40 to importance quantization, providing a spectrum of compression levels and accuracy trade-offs. This page describes the architectural design and supported quantization formats within the GGML/llama.cpp ecosystem.

## Key Claims

- Quantization in llama.cpp is built upon the GGML tensor library.
- The quantization approach is block-based: tensors are divided into small chunks, and each block has its own scale and optionally minimum value.
- Supported quantization formats range from Q40 to importance quantization.
- The primary goal is to reduce memory footprint and accelerate inference by compressing 16-bit or 32-bit floats into 4-bit, 2-bit, or ternary representations.

## Relationships

- [[auto-gemm-micro-kernel-c906-c910-benchmark]]: Both pages are part of the llama.cpp inference ecosystem; quantization reduces model weight precision to enable efficient LLM inference on the same RISC-V cores (C906, C910) that the auto-generated GEMM micro-kernels target.

## Sources

- https://deepwiki.com/ggml-org/llama.cpp/7.3-quantization-techniques
merge_draft_body -->
