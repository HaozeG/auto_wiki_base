# Wiki Patch Queue

## [2026-07-03] pending | xuantie-c908.md
target_page: xuantie-c908.md
target_section: Benchmarking
source: https://github.com/XUANTIE-RV/xtai-benchmark
status: approved
proposed_update: Add a section describing the XuanTie AI Benchmark Suite (xtai-benchmark), which provides precompiled benchmark binaries for the C908 (BERT, EfficientNet, MobileNetV2 with various quantizations) via HHB. Source: https://github.com/XUANTIE-RV/xtai-benchmark

## [2026-07-03] pending | xuantie-ai-benchmark-suite.md
target_page: xuantie-ai-benchmark-suite.md
target_section: Relationships
source: https://github.com/XUANTIE-RV/xuantie-gnu-toolchain/
status: approved
proposed_update: Add a relationship entry linking to the XuanTie GNU Compiler Toolchain: 'The XuanTie GNU Compiler Toolchain provides the cross-compiler used to build the precompiled model binaries in this benchmark suite.'

## [2026-07-03] merge_pending | xuantie-c908.md
target_page: xuantie-c908.md
canonical_name: XuanTie C908
colliding_name: XuanTie C908
source: https://csi-nn2.opensource.alibaba.com/zh/blog/C908+accelerates+AI
status: applied
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
status: approved
proposed_update: Add a key claim: SHL provides optimized inference acceleration for XuanTie C908, supporting fp32/fp16/int8 datatypes and leveraging the processor's pipeline, instruction fusion, and high-speed cache technology. This is sourced from the same blog post.

## [2026-07-03] pending | shl.md
target_page: shl.md
target_section: content
source: https://zhangwm-pt.github.io/shl/md_README.html
status: approved
proposed_update: Merge the detailed information from the SHL README into the existing entity page. Specifically: (1) Expand the opening paragraph to mention version SHL 2.2.x and that the interface uses CSI-NN2 API. (2) Add a 'Features' subsection under Key Claims covering reference C implementation, assembly optimization for XuanTie CPU, symmetric and asymmetric quantization, support for 8-bit, 16-bit, and float16 data types, NCHW and NHWC layouts, automatic API calling via HHB, and coverage of CPU and NPU architectures. (3) Add a 'Usage' section containing build instructions from source for XuanTie C906 (including installing T-HEAD RISC-V GCC 2.6, cloning CSI-NN2, compiling and installing nn2_c906) and a quick-start example for running mobilenetv1 f16 on a C906-based board like the D1. (4) Add an 'Acknowledgements' subsection noting that SHL references Caffe, TensorFlow, ncnn, MNN, Tengine, CMSIS_5, ONNX, and XNNPACK. (5) Add a relationship to MLPerf tiny (from the candidate's mention of 'SHL to run MLPerf tiny') and to HHVB toolchain documentation. All updates should be grounded in the candidate's source_grounded_snippets.

## [2026-07-03] merge_pending | xuantie-c908.md
target_page: xuantie-c908.md
canonical_name: XuanTie C908
colliding_name: xuantie-c908
source: https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
status: applied
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
status: applied
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
status: applied
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
status: approved
proposed_update: Add a contradiction note: the GCC tuning patch submitted in June 2026 explicitly states that the C908 core does not support the vector extension (RVV), contradicting the assumption of RVV 1.0 support listed in the prerequisites and constraints (VLEN 128) of this optimization recipe. This may affect the validity of optimization techniques that rely on vector instructions (e.g., vle vector loads). The recipe should either restrict its applicability to a hypothetical SVE-like implementation or note that it targets a different C908 variant.

## [2026-07-03] merge_pending | k230-soc.md
target_page: k230-soc.md
canonical_name: K230
colliding_name: CanMV K230
source: https://deepwiki.com/kendryte/k230_canmv_docs
status: applied
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
status: applied
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
status: apply_failed (pipeline rejected)
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
status: applied
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
status: applied
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
status: applied
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
status: apply_failed (pipeline rejected)
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
status: applied
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
status: applied
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
status: applied
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
status: applied
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
status: applied
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
status: applied
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
status: apply_failed (pipeline rejected)
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
status: apply_failed (pipeline rejected)
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
status: applied
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

## [2026-07-03] merge_pending | xuantie-gnu-toolchain.md
target_page: xuantie-gnu-toolchain.md
canonical_name: XuanTie GNU Compiler Toolchain
colliding_name: XuanTie GNU Toolchain
source: https://github.com/XUANTIE-RV/xuantie-gnu-toolchain/
status: applied
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
status: applied
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
status: applied
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
status: applied
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
status: applied
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
status: approved
proposed_update: Add relationship link to [[bpi-f3-rvv-llm-benchmark]]: 'The BPI-F3 LLM inference benchmark with RVV-optimized llama.cpp validates the practical performance of the SpacemiT K1 RVV 1.0 extensions on representative LLM workloads.'

## [2026-07-03] merge_pending | llamacpp-quantization-methods.md
target_page: llamacpp-quantization-methods.md
canonical_name: llama.cpp Quantization Methods
colliding_name: GGML Quantization
source: https://deepwiki.com/ggml-org/llama.cpp/7.3-quantization-techniques
status: applied
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

## [2026-07-03] merge_pending | sophon-sg2042.md
target_page: sophon-sg2042.md
canonical_name: SOPHON SG2042
colliding_name: Sophon SG2042
source: https://arxiv.org/abs/2503.17422
status: applied
<!-- merge_draft_body
# Sophon SG2042

Sophon SG2042 is a 64-core RISC-V processor designed for server-class workloads, developed by Sophgo (later Sophon). It is the first commercially available many-core RISC-V CPU with vector processing capabilities, targeting flexible and cost-effective inference and reasoning workloads for large language models. The SG2042 features a complex memory hierarchy with Non-Uniform Memory Access (NUMA) and is equipped with 128GB of DRAM in the Milk-V Pioneer development board. Its vector processing units are supported by the Xuantie fork of GCC 10.4, which is required for compiling optimized kernels that fully exploit the hardware. The platform also supports mainstream toolchains such as GCC 13.2 and Clang 19 for the overall inference framework (llama.cpp). The SG2042's microarchitecture is built around Xuantie technology, as evidenced by the compiler toolchain, though the specific core model is not publicly documented in the source. This platform serves as a testbed for the V-Seek LLM inference optimization framework.

## Key Claims

- The Sophon SG2042 is the first commercially available many-core RISC-V CPU with vector processing capabilities.
- It features 64 cores and 128GB DRAM in the Milk-V Pioneer board.
- The vector units require Xuantie GCC 10.4 for compilation; the overall framework can use GCC 13.2 or Clang 19.
- The platform has a NUMA memory hierarchy that affects LLM inference performance.

## Optimization-Relevant Details

- ISA/profile: RISC-V with vector extensions (exact version not specified in source)
- Vector/matrix/accelerator support: vector processing units (no VLEN or DLEN specified)
- Memory/cache/TLB/DMA: 128GB DRAM, NUMA architecture; cache hierarchy not detailed
- Compiler/toolchain support: Xuantie GCC 10.4 (vector kernel support), GCC 13.2, Clang 19

## Relationships

No specific relationship to the visible context pages ([[xuantie-c906-hardware-target]], [[spacemit-x60-hardware-target]], [[gcc-tuning-c908-canmv-k230]]) can be established from the current source material; the SG2042 is a many-core server-class CPU while the visible pages cover embedded cores and scalar tuning.

## Sources

- https://arxiv.org/abs/2503.17422
merge_draft_body -->

## [2026-07-03] pending | et-soc-1-hardware-target.md
target_page: et-soc-1-hardware-target.md
target_section: all
source: https://github.com/10x-Engineers/et-soc1-docs/blob/main/01_esperanto_soc_overview.md
status: approved
proposed_update: Overwrite the page with detailed architectural information from official Esperanto ET-SoC-1 documentation (10x-Engineers/et-soc1-docs). Add precise core counts: 1,088 ET-Minion 64-bit RISC-V dual-threaded in-order scalar cores with custom vector/tensor units, 4 ET-Maxion 64-bit RISC-V single-threaded superscalar out-of-order cores, and 1 ET-Minion-based Service Processor. Include memory hierarchy: 140 MB on-die SRAM distributed across chip, each 1 MB block configurable as local L2 cache, part of chip-wide L3, or globally accessible scratchpad. Add PCI Express Gen4 x8 interface delivering peak throughput 128 Gbps. Add sixteen 16-bit LPDDR4X controllers at 4,266 MT/s (133 GB/s). Describe SoC hierarchy: Neighborhood (8 ET-Minion cores + 32 KB shared I-cache), Shire (4 Neighborhoods, 4 MB shared L2/L3 cache, mesh stop interface), 34 Minion Shires (1,088 cores total) plus PCI Shire and I/O Shire (ET-Maxion cores, Service Processor, Root of Trust, USB, I2C, SPI, UARTs). Add ET-Minion privileged architecture deviations: performance counters moved to shared PMU, minstret/mcycle always return 0, satp CSR shared between harts, mtvec/stvec alignment to 4 KB, WFI behavior. Update constraints field with: '1,093 RISC-V cores (1,088 Minion + 4 Maxion + 1 service)', '140 MB on-die SRAM', 'PCIe Gen4 x8 128 Gbps', 'LPDDR4X 16-channel 4,266 MT/s', 'TSMC 7nm'. Add source URL https://github.com/10x-Engineers/et-soc1-docs/blob/main/01_esperanto_soc_overview.md.

## [2026-07-03] merge_pending | xuantie-c908.md
target_page: xuantie-c908.md
canonical_name: XuanTie C908
colliding_name: XuanTie C908
source: https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719234.html
status: applied
<!-- merge_draft_body
# XuanTie C908

The XuanTie C908 is a 64-bit RISC-V core from T-Head Semiconductor, designed for embedded applications. A GCC tuning patch submitted to the GCC mailing list introduces a scalar scheduler model for the C908, based on the XuanTie C908 R1S0 User Manual. The scheduler models the scalar integer, load/store, multiply, divide, and floating-point pipeline resources. Long-latency reservations are clamped to 7 cycles, following the existing RISC-V scheduler modeling approach established in a prior GCC commit. Vector scheduling is not included in this patch and is left for future work under the identifier xt-c908v. The tuning was validated on a CanMV-K230-V1.1 board using CoreMark and a set of instruction throughput tests consisting of unrolled loops with independent register groups. These tests achieved approximately 0.8% improvement in CoreMark score and 5-17% cycle-count improvements on the throughput benchmarks, measured after 20 warm-up runs and 200 measured executions per test.

## Key Claims

- The GCC tuning model for the XuanTie C908 is based on the official XuanTie C908 R1S0 User Manual.
- The scheduler explicitly models scalar integer, load/store, multiply, divide, and floating-point pipeline resources.
- Long-latency reservation cycles are capped at 7, consistent with the existing RISC-V scheduler modeling convention.
- The tuning was tested on a CanMV-K230-V1.1 board; CoreMark score improves by approximately 0.8% compared to the generic tuning model.
- Instruction throughput tests (unrolled loops with independent registers for add, fadd, etc.) show cycle-count reductions of 5-17%.
- Vector scheduling is deliberately excluded from this patch and deferred to future xt-c908v work.

## Optimization-Relevant Details

- ISA/profile: RISC-V (specific extension set not detailed in the patch)
- Vector/matrix/accelerator support: None in this scalar tuning; vector scheduling is not modeled.
- Memory/cache/TLB/DMA: Not specified in the patch.
- Compiler/toolchain support: GCC, via a patch that introduces the xt-c908 tuning in riscv-cores.def, riscv-opts.h, riscv.cc, riscv.md, and a new file xt-c908.md. The tuning is merged into GCC trunk.

## Relationships

- [[xuantie-c906-hardware-target]]: Both the XuanTie C908 and C906 are in-order single-issue RISC-V cores from T-Head; the C906 includes a 128-bit SIMD vector unit, while the C908 tuning models only scalar pipelines and does not expose vector capabilities.
- [[spacemit-x60-hardware-target]]: Both the XuanTie C908 and SpacemiT X60 have GCC tuning patches that model in-order scalar pipelines; the X60 tuning additionally models dual-issue and RVV 1.0 vector capabilities, while the C908 tuning is single-issue scalar only.
- [[sophon-sg2044-hardware-target]]: The SG2044 uses XuanTie C920v2 cores, a more advanced member of the T-Head XuanTie family with RVV 1.0 vector support, whereas the C908 is a simpler embedded core with only scalar scheduling currently modeled.

## Sources

- https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719234.html
merge_draft_body -->

## [2026-07-03] pending | gap9.md
target_page: gap9.md
target_section: Key Claims
source: https://arxiv.org/abs/2603.08725
status: approved
proposed_update: Add a claim from arXiv:2603.08725: GAP9 offers the best energy efficiency within microcontroller-class power budgets when running a 336M MAC segmentation model (PicoSAM2), as benchmarked against STM32N6 and IMX500. This is a comparative finding from a 2026 IEEE I2MTC paper.

## [2026-07-03] merge_pending | gap9shield.md
target_page: gap9shield.md
canonical_name: GAP9Shield
colliding_name: GAP9Shield
source: https://github.com/pulp-platform/gap9-shield
status: applied
<!-- merge_draft_body
# GAP9Shield

The GAP9Shield is an ultra-low-power hardware module designed to enhance nano-drones with advanced AI, vision, and ranging capabilities. It is built around the GAP9 System-on-Chip (SoC), a 9-core RISC-V cluster with a dedicated NE16 AI accelerator, and integrates a 5 MP OV5647 camera, a 5-directional VL53L1 Time-of-Flight ranging array (covering front, back, left, right, and upward), and a NINA-W102 Wi-Fi/BLE module for wireless connectivity. The module achieves 15.6 GOPs for DSP workloads and 32.2 GMACs for ML tasks, with an energy efficiency of 330 µW/GOP and a sleep power as low as 45 µW. It operates at frequencies up to 370 MHz and consumes under 100 mW for most AI workloads. The GAP9Shield measures 50 mm × 27 mm, weighs approximately 6 grams, and is designed to mount on a Crazyflie 2.1 nano-drone, enabling real-time object detection (YOLO), SLAM, and obstacle avoidance in indoor and cluttered environments.

## Key Claims

- The GAP9Shield uses a 9-core RISC-V cluster with NE16 AI accelerator (15.6 GOPs DSP, 32.2 GMACs ML).
- Energy efficiency is 330 µW/GOP, with sleep power as low as 45 µW and frequency up to 370 MHz.
- Memory includes 1.6 MB L2 RAM, 2 MB embedded non-volatile memory, plus 256 Mbit PSRAM and 512 Mbit Flash.
- Camera: OV5647 5 MP sensor supporting QSXGA to QVGA, up to 120 fps at QVGA, via CSI2 interface.
- Ranging system: 5D VL53L1 ToF array covering right, left, front, back, and upward directions, range up to 400 cm at 60 Hz.
- Wireless: NINA-W102 module (ESP32, 2.4 GHz Wi-Fi/BLE, up to 12 Mbps UDP).
- Physical: 50 mm × 27 mm, approx. 6 g, 6-layer PCB.
- Achieves 20% higher frame rate for RGB images compared to conventional AI-decks (e.g., based on GAP8).
- Optimized for AI workloads including YOLO object detection, MCL localization, and SLAM.

## Relationships

- [[gap9]]: The GAP9Shield integrates the GAP9 SoC as its core processor; the module inherits the GAP9's RISC-V PULP architecture and AI acceleration capabilities.

## Sources

- https://github.com/pulp-platform/gap9-shield
merge_draft_body -->

## [2026-07-03] pending | gap9.md
target_page: gap9.md
target_section: Key Claims
source: https://github.com/pulp-platform/gap9-shield
status: approved
proposed_update: The GAP9 page states an 8-core architecture, but the GAP9Shield README describes a 9-core RISC-V cluster (likely 8 general-purpose cores + 1 NE16 accelerator core). Consider clarifying the core count and noting the NE16 accelerator. Also consider adding a reference to the GAP9Shield module and its integrated components.

## [2026-07-03] merge_pending | gcc-tuning-c908-canmv-k230.md
target_page: gcc-tuning-c908-canmv-k230.md
canonical_name: GCC Tuning Benchmark on XuanTie C908
colliding_name: XuanTie C908 GCC Tuning
source: https://www.mail-archive.com/gcc-patches@gcc.gnu.org/msg406313.html
status: applied
<!-- merge_draft_body
# XuanTie C908 GCC Tuning

The XuanTie C908 GCC tuning patch adds a scalar scheduler model for the T-Head XuanTie C908 RISC-V core to the GCC compiler backend, enabling instruction scheduling that reduces pipeline stalls on this in-order single-issue core. The tuning is based on the XuanTie C908 R1S0 User Manual and models the scalar integer, load/store, multiply, divide, and floating-point pipeline resources. It was validated on a CanMV-K230-V1.1 board using CoreMark and custom instruction throughput loops (groups of adds and fadds), yielding a 0.8% CoreMark improvement and 5–17% cycle-count improvements on the throughput tests. The patch does not model vector scheduling, leaving that for future work (xt-c908v). Long-latency reservations are clamped to 7 cycles following the existing RISC-V scheduler modelling approach.

## Key Claims

- The tuning models scalar pipeline resources for the XuanTie C908: integer, load/store, multiply, divide, and floating-point.
- Vector scheduling is not included; reserved for future xt-c908v model.
- Tested on CanMV-K230-V1.1 board with CoreMark and instruction throughput loops.
- Approximately 0.8% CoreMark improvement measured.
- Instruction throughput tests show 5–17% cycle-count improvements.
- Long-latency reservations clamped to 7 cycles.
- Patches applied to GCC trunk as of 2026-06-03.

## Transformation

- Prerequisites: GCC source tree, XuanTie C908 User Manual for pipeline details.
- Steps: Add cpu tuning entry in riscv-cores.def, microarchitecture type in riscv-opts.h, tune structure in riscv.cc, and include the xt-c908.md file in riscv.md. The xt-c908.md file defines the scheduler automaton and instruction reservations.
- Expected effect: Reduced pipeline stalls for scalar code, leading to better instruction throughput on XuanTie C908 cores. The patch reports 0.8% CoreMark improvement and 5-17% improvement on instruction throughput loops.
- Failure modes: If the scheduler model does not accurately reflect hardware, it may cause suboptimal scheduling. However, it is based on the user manual and validated with measurements. The model does not cover vector instructions; compiling vector code without future tuning may not benefit.
- Measurements: CoreMark: 0.8% improvement. Instruction throughput loops (add, fadd): 5-17% cycle-count improvement. Method: 20 warm-up runs, 200 measured runs, aligned memory.

## Relationships

- [[xuantie-c906-hardware-target]]: Both the XuanTie C906 and C908 are in-order single-issue RISC-V cores from T-Head; the C906 includes a 128-bit SIMD vector unit while the C908 relies on scalar performance, and this tuning patch addresses the C908's scalar pipeline.
- [[spacemit-x60-hardware-target]]: Both the XuanTie C908 and SpacemiT X60 have GCC tuning patches that model in-order scalar pipelines; however, the X60 tuning additionally models a vector unit (RVV 1.0) and dual-issue capability, while the C908 tuning is purely scalar and single-issue.

## Sources

- https://www.mail-archive.com/gcc-patches@gcc.gnu.org/msg406313.html
merge_draft_body -->

## [2026-07-03] pending | xuantie-c906-hardware-target.md
target_page: xuantie-c906-hardware-target.md
target_section: Relationships
source: https://www.mail-archive.com/gcc-patches@gcc.gnu.org/msg406313.html
status: approved
proposed_update: Update outbound_links target from 'gcc-tuning-c908-canmv-k230' to 'xuantie-c908-gcc-tuning' and refine relationship reason to note that the GCC tuning patch models the C908 scalar pipeline, while the C906 uses a custom 128-bit SIMD unit. The current reason is still valid but the target filename must match the new optimization recipe page.

## [2026-07-03] pending | spacemit-x60-hardware-target.md
target_page: spacemit-x60-hardware-target.md
target_section: Relationships
source: https://www.mail-archive.com/gcc-patches@gcc.gnu.org/msg406313.html
status: approved
proposed_update: Update outbound_links target from 'gcc-tuning-c908-canmv-k230' to 'xuantie-c908-gcc-tuning' and refine relationship reason to emphasize that both GCC tuning patches model in-order scalar pipelines but the X60 tuning also includes dual-issue and RVV 1.0 vector support, while the C908 tuning is purely scalar and single-issue.

## [2026-07-03] merge_pending | nncase.md
target_page: nncase.md
canonical_name: nncase
colliding_name: nncase
source: https://github.com/kendryte/k230_docs/blob/main/en/01_software/board/ai/K230_nncase_Development_Guide.md
status: applied
<!-- merge_draft_body
# nncase

nncase is a neural network compiler developed by Canaan Creative for AI accelerators, supporting targets including CPU, K210, K510, and K230. It compiles neural network models from TFLite and ONNX formats into kmodel files that can be executed on supported hardware. The compiler provides static memory allocation (no heap memory required), operator fusion and optimization, and support for both float and uint8/int8 quantized inference. Post-training quantization (PTQ) is supported using floating-point models and quantization calibration sets. The nncase software stack consists of a compiler component, which runs on a PC to produce kmodels, and a runtime library that integrates into user applications to load models, set input data, execute KPU inference, and retrieve outputs.

## Key Claims

- Supports multi-input multi-output networks and multi-branch structures.
- Static memory allocation, no heap memory required.
- Operator fusion and optimization.
- Supports float and uint8/int8 quantized inference.
- Post-training quantization using floating-point models and calibration sets.
- Flat model format supporting zero-copy loading.
- Supports neural network model formats: TFLite and ONNX.
- Compiler modules include: Importer, IR (Neutral IR and Target IR), Evaluator, Quantize, Transform optimization, Tiling, Partition, Schedule, and Codegen.
- Runtime provides kmodel loading, input setting, KPU execution, and output retrieval.
- Currently supported targets: CPU, K210, K510, K230.

## Relationships

No specific relationship to visible context pages ([[andes-ax45mpv-hardware-target]] does not share direct architectural or toolchain connection with nncase).

## Sources

- https://github.com/kendryte/k230_docs/blob/main/en/01_software/board/ai/K230_nncase_Development_Guide.md
merge_draft_body -->

## [2026-07-03] merge_pending | nncase.md
target_page: nncase.md
canonical_name: nncase
colliding_name: nncase
source: https://gitee.com/kendryte/nncase
status: applied
<!-- merge_draft_body
# nncase

nncase is an open-source deep learning compiler stack designed specifically for Kendryte AI accelerators, developed by kendryte (a Canaan Creative subsidiary). Licensed under Apache-2.0, nncase takes neural network models from frontends such as TFLite, ONNX, and Caffe and compiles them into optimized executables for Kendryte's hardware, with a primary target being the K230 SoC. The toolchain is available as a Python package (`pip install nncase nncase-kpu`) and includes a runtime library that integrates with the K230 SDK. nncase supports 8-bit quantization for both weights and activations, achieving inference performance that matches the accuracy of reference frameworks on standard benchmarks. For example, on the K230 platform with u8/u8 quantization, nncase achieves 600.24 FPS on MobileNetV2 (ImageNet top-1 accuracy 71.1% vs reference 71.3%) and 86.17 FPS on ResNet50V2 (top-1 accuracy 75.11% vs reference 75.44%). The project maintains versioned releases with active development across multiple branches (release/3.0, release/2.0, and various feature branches).

## Key Claims

- nncase is an open deep learning compiler stack for Kendryte AI accelerators, licensed under Apache-2.0.
- It supports model import from TFLite, ONNX, and Caffe, with detailed operator support documented for each frontend.
- The compiler targets the K230 SoC and is integrated with the K230 SDK, with a documented version mapping between nncase releases and SDK versions.
- nncase is installed via pip for both Linux and Windows; the Windows package requires a separate wheel file for the KPU runtime.
- Quantization uses u8 for both input features and weights; accuracy matches reference frameworks within 0.1–0.3% on ImageNet top-1.
- Benchmark results on K230 with u8/u8 quantization: MobileNetV2 at 600.24 FPS, ResNet50V2 at 86.17 FPS, YOLOv5s detection at 23.645 FPS, YOLOv8s detection at 9.373 FPS, YOLOv8s segmentation at 7.845 FPS, and YOLOv8n pose estimation at 36.066 FPS (320x320).
- The repository has 246 branches and 77 tags, indicating active development.

## Relationships

No specific relationship to pages in the current wiki context.

## Sources

- https://gitee.com/kendryte/nncase
- https://github.com/kendryte/nncase
merge_draft_body -->

## [2026-07-03] merge_pending | sophon-sg2042.md
target_page: sophon-sg2042.md
canonical_name: SOPHON SG2042
colliding_name: Sophon SG2042
source: https://arxiv.org/html/2406.12394v1
status: apply_failed (pipeline rejected)
<!-- merge_draft_body
# Sophon SG2042

The Sophon SG2042 is a 64-core RISC-V CPU designed by Sophon (SOPHGO) for high-performance workloads, first mass-produced and released in summer 2023. Built with T-Head XuanTie C920 cores organized in clusters of four, each core implements a 12-stage out-of-order multiple-issue superscalar pipeline with three decode, four rename/dispatch, eight issue/execute, and two load/store execution units. The chip runs at 2 GHz and supports the RV64GCV instruction set including version 0.7.1 of the RISC-V Vector Extension (RVV) with a 128-bit vector width. Each core has 64 KB L1 instruction and data caches, with 1 MB of L2 cache shared per four-core cluster and 64 MB of L3 system cache shared across all cores. The SG2042 provides four DDR4-3200 memory controllers and 32 lanes of PCI-E Gen4. The CPU is commonly available in the Milk-V Pioneer Box with 128 GB of DDR4 RAM. Because the C920 core supports only the pre-ratification RVV v0.7.1, mainline GCC and LLVM cannot target the vector unit; T-Head provides a custom XuanTie GCC compiler fork, with GCC 8.4 from the June 2021 release giving the best auto-vectorization results.

## Key Claims

- The SG2042 is a 64-core RISC-V CPU with 2 GHz clock, using T-Head XuanTie C920 cores with a 12-stage out-of-order superscalar pipeline.
- It supports RV64GCV ISA including RVV v0.7.1 with a fixed 128-bit vector width.
- Cache hierarchy: 64 KB L1 I/D per core, 1 MB L2 per four-core cluster, 64 MB L3 system cache.
- Memory: four DDR4-3200 controllers; I/O: 32 PCI-E Gen4 lanes.
- The vector unit requires a vendor-specific compiler fork (XuanTie GCC 20210618) for auto-vectorization; mainline compilers do not support RVV v0.7.1.
- In NAS Parallel Benchmark evaluation, the SG2042 outperformed other RISC-V CPUs by 2.6x to 16.7x at the single-core level, but its memory subsystem was identified as the primary bottleneck for memory-bound HPC workloads.

## Optimization-Relevant Details

- ISA/profile: RV64GCV with RVV v0.7.1 (128-bit VLEN)
- Vector/matrix/accelerator support: 128-bit vector unit per core, RVV v0.7.1
- Memory/cache/TLB/DMA: 64 KB L1 I/D, 1 MB L2 per 4-core cluster, 64 MB L3; DDR4-3200; PCI-E Gen4
- Compiler/toolchain support: XuanTie GCC fork (20210618, GCC 8.4) for auto-vectorization; no mainline GCC/LLVM support for RVV v0.7.1

## Relationships

- [[sophon-sg2044-hardware-target]]: SG2044 is the successor to SG2042, featuring C920v2 cores with ratified RVV v1.0 and an enhanced memory subsystem that addresses the SG2042's main bottleneck.
- [[xuantie-c906-hardware-target]]: Both are T-Head XuanTie cores; the C920 in the SG2042 is a 12-stage out-of-order multiple-issue core with RVV v0.7.1, while the C906 is a 5-stage in-order single-issue core with a custom 128-bit SIMD unit.
- [[andes-nx27v-hardware-target]]: Both implement RISC-V vector extensions; the C920 uses the pre-ratification RVV v0.7.1 with 128-bit VLEN, while the NX27V uses the ratified RVV v1.0 with up to 512-bit VLEN and out-of-order vector processing.

## Sources

- https://arxiv.org/html/2406.12394v1
merge_draft_body -->

## [2026-07-03] merge_pending | sophon-sg2042.md
target_page: sophon-sg2042.md
canonical_name: SOPHON SG2042
colliding_name: Sophon SG2042
source: https://arxiv.org/abs/2406.12394
status: applied
<!-- merge_draft_body
# Sophon SG2042

The Sophon SG2042 is a 64-core RISC-V CPU designed for high-performance workloads, first released in summer 2023 by Sophon. It is the first mass-produced, commodity-available high-core-count RISC-V processor targeting HPC applications. The chip integrates 64 XuanTie C920 cores designed by T-Head, each a 64-bit in-order core, running at 2 GHz. Cores are organized in clusters of four, sharing an unspecified L2 cache (the memory subsystem is identified as the primary performance bottleneck). The SG2042 implements the RISC-V ISA with vector extensions (RVV 1.0), though the specific extension set is not fully detailed in available sources. The chip is notable for its high core density and commodity availability, enabling RISC-V-based HPC exploration and benchmarking. Initial performance characterization using the NAS Parallel Benchmark (NPB) suite shows that the SG2042 outperforms other RISC-V CPUs by a factor of 2.6 to 16.7 at the single-core level, but its memory bandwidth and latency limit performance on memory-bound algorithms relative to x86-64 and AArch64 CPUs.

## Key Claims

- First mass-produced 64-core RISC-V CPU for HPC, released summer 2023.
- Contains 64 XuanTie C920 cores at 2 GHz, organized in clusters of four.
- Memory subsystem is the primary performance bottleneck, as identified by NPB benchmarking.
- Outperforms other RISC-V CPUs by 2.6–16.7× at single-core level.
- Competes well with x86-64 and AArch64 CPUs on compute-bound workloads but lags on memory-bound workloads.

## Optimization-Relevant Details

- ISA/profile: RISC-V with RVV 1.0 (vector), 64-bit cores.
- Vector/matrix/accelerator support: RVV (specific VLEN not disclosed).
- Memory/cache/TLB/DMA: Memory subsystem bottleneck; no detailed cache hierarchy published in this source.
- Compiler/toolchain support: Not specified; benchmarks likely used standard GCC/LLVM with RISC-V backend.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://arxiv.org/abs/2406.12394
merge_draft_body -->

## [2026-07-03] merge_pending | sophon-sg2042-npb-performance-benchmark-result.md
target_page: sophon-sg2042-npb-performance-benchmark-result.md
canonical_name: SG2042 NAS Parallel Benchmark Performance
colliding_name: NPB Performance of the Sophon SG2042
source: https://arxiv.org/abs/2406.12394
status: applied
<!-- merge_draft_body
# NPB Performance of the Sophon SG2042

The Sophon SG2042 64-core RISC-V CPU was characterized using the NASA NAS Parallel Benchmark (NPB) suite to evaluate its suitability for HPC workloads. The study compared the SG2042 against CPUs implementing RISC-V, x86-64, and AArch64 ISAs. Key findings include that the SG2042 delivers a 2.6 to 16.7 times performance improvement at the single-core level over other RISC-V CPUs. Against x86-64 and AArch64 CPUs, the SG2042 performs well on compute-bound algorithms but degrades on memory-bandwidth- or latency-bound algorithms, identifying the SG2042's memory subsystem as the primary bottleneck. The benchmark results were obtained using the NPB suite, which includes kernels such as Integer Sort (IS), Multi Grid (MG), Embarrassingly Parallel (EP), Conjugate Gradient (CG), and Fast Fourier Transform (FT), along with pseudo-applications. The measurement context is comparative across ISAs, with no specific version numbers for hardware or software reported in the excerpt. The evidence strength is measured, as actual execution on hardware was performed.

## Key Claims

- SG2042 outperforms all other tested RISC-V CPUs by 2.6–16.7× at single core in NPB.
- On compute-bound algorithms, SG2042 competes well with x86-64 and AArch64 CPUs.
- Memory-bound algorithms show reduced relative performance; the memory subsystem is the primary bottleneck.
- The study used the NPB suite with kernels: IS, MG, EP, CG, FT, and pseudo-applications.

## Measurement Context

- Hardware version: Sophon SG2042 (2 GHz, 64-core, XuanTie C920). Comparison CPUs: unspecified RISC-V, x86-64, AArch64.
- Software/toolchain version: NPB suite (version not specified).
- Workload shape: NPB kernels (IS, MG, EP, CG, FT) and pseudo-applications.
- Metric: single-core performance improvement (factor), qualitative compute/memory-bound classification.
- Method: Comparative benchmarks run on SG2042 and other CPUs; single-core results reported.
- Evidence strength: measured (actual hardware runs).

## Relationships

No specific relationship to visible context pages.

## Sources

- https://arxiv.org/abs/2406.12394
merge_draft_body -->

## [2026-07-03] pending | et-soc-1-hardware-target.md
target_page: et-soc-1-hardware-target.md
target_section: opening_paragraph
source: https://vlsifacts.com/esperantos-et-soc-1-chip-integrates-more-than-1000-risc-v-cores-for-energy-efficient-ml-recommendation/
status: approved
proposed_update: Replace the first paragraph with a more detailed self-contained description: 'The ET-SoC-1 (Esperanto Technologies Supercomputer-on-Chip 1) is a RISC-V AI inference accelerator chip fabricated on TSMC's 7nm process, integrating 1088 energy-efficient ET-Minion 64-bit in-order RISC-V cores each with a vector/tensor unit, 4 high-performance ET-Maxion 64-bit out-of-order RISC-V cores, and 1 RISC-V service processor. With 24 billion transistors on a 570 mm² die, it delivers peak compute rates of 100 to 200 TOPS while consuming typically less than 20 watts. It is designed for energy-efficient ML recommendation inference in large data centers and is packaged on a Glacier Point v2 accelerator card that houses up to six chips, providing up to 192 GB of DRAM with 822 GB/s bandwidth.'

## [2026-07-03] pending | spacemit-x60-hardware-target.md
target_page: spacemit-x60-hardware-target.md
target_section: Optimization-Relevant Details
source: https://arxiv.org/abs/2605.10860
status: approved
proposed_update: Add a bullet point under Optimization-Relevant Details about the RVV predication overhead and stride load performance bottlenecks identified in the GCC 15/Clang 21 auto-vectorization study (arXiv:2605.10860). These are issues not yet fully captured by current compiler cost models and affect in-order RVV 1.0 implementations such as the X60.

## [2026-07-03] merge_pending | riscv-v-extension.md
target_page: riscv-v-extension.md
canonical_name: RISC-V V Extension
colliding_name: CORE-V
source: https://github.com/openhwgroup/core-v-cores
status: applied
<!-- merge_draft_body
# CORE-V Family

The CORE-V family is a collection of permissively licensed open-source RISC-V cores curated by the OpenHW Foundation, which operates under the Eclipse Foundation. The family is designed to support a broad range of applications from embedded control to Linux-capable systems, with industrial-grade verification. The RTL for each core is highly configurable, enabling multiple unique core configurations from a single repository. The family includes several sub-families: CVA6 (6-stage, single/dual-issue in-order cores supporting RV32IMACF or RV64GC with three privilege levels M, S, U for Unix-like operating systems), CVW/Wally (5-stage cores for education, supporting RV32I/E and RV64I with optional caches and branch prediction), CVE4 (4-stage cores derived from the PULP RI5CY core, with variants targeting DSP, security, and compute-intensive applications through custom extensions and the CORE-V eXtension Interface), CVE2 (2-stage low-power cores for control-oriented tasks), and CVA5 (5-stage cores for FPGAs supporting RV32IMA). Each member is maintained in its own GitHub repository, and the project aims to provide industrial-grade, community-driven RISC-V processor IP.

## Key Claims

- CORE-V is a family of permissively licensed open-source RISC-V cores curated by the OpenHW Foundation, part of the Eclipse Foundation.
- CVA6 (formerly PULP Ariane) implements a 6-stage in-order pipeline, supports RV32IMACF or RV64GC, and includes configurable TLBs, hardware PTW, and branch prediction for Unix-like OS support.
- CVA6 variants include CV32A60AX (32-bit single-issue application class with CV-X-IF), CV32A60X (32-bit embedded class targeting TRL5 in early 2025), and CV64A60AX (64-bit application class targeting TRL4 in 2026).
- CVW (Wally) provides 5-stage cores for education with optional caches, branch prediction, virtual memory, and peripherals.
- CVE4 cores are 4-stage in-order cores derived from PULP RI5CY, with variants CV32E40P (DSP custom extensions including hardware loops, SIMD, bit manipulation), CV32E40S (security-focused with enhanced PMP and anti-tampering), CV32E40X (compute-intensive with CV-X-IF), and CV32E41P (prototype for Zce and Zfinx extensions).
- CVE2 is a low-complexity 2-stage core derived from lowRISC Ibex, targeting high energy efficiency for control-oriented tasks.
- CVA5 is a 32-bit FPGA-optimized core derived from the Taiga Project, supporting parallel variable-latency execution units.
- All cores are open-source with permissive licensing and are verified to industrial grade.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://github.com/openhwgroup/core-v-cores
merge_draft_body -->

## [2026-07-03] merge_pending | chips-alliance-entity.md
target_page: chips-alliance-entity.md
canonical_name: CHIPS Alliance
colliding_name: CHIPS Alliance
source: https://github.com/chipsalliance
status: applied
<!-- merge_draft_body
# CHIPS Alliance

CHIPS Alliance is an open-source consortium that develops high-quality hardware designs and tools relevant to ASICs and FPGAs. It hosts multiple open-source projects, including Chisel (a hardware design language written in Scala), Rocket Chip (a System-on-Chip generator), Verible (a suite of SystemVerilog developer tools covering parsing, linting, formatting, and language server support), riscv-dv (a random instruction generator for RISC-V processor verification), Cores-VeeR-EH1 (a VeeR EH1 core), FIRRTL (a Flexible Intermediate Representation for RTL), and the Caliptra subsystem (including Root of Trust IP, RTL, firmware, and software). By creating an open and collaborative environment, the alliance aims to lower the cost of hardware development through shared resources. The repositories are primarily licensed under Apache-2.0, with some under ISC.

## Key Claims

- CHIPS Alliance develops high-quality open source hardware designs and tools for ASICs and FPGAs.
- The alliance hosts projects such as Chisel, Rocket Chip, Verible, riscv-dv, Cores-VeeR-EH1, FIRRTL, and Caliptra.
- The mission is to lower development costs through open collaboration among companies and individuals.
- Repositories are predominantly Apache-2.0 licensed.
- The alliance has over 122 repositories, including VeeR EL2 core, Caliptra subsystem software, and Verilator (forked).

## Relationships

No specific relationship to visible context pages.

## Sources

- https://github.com/chipsalliance
merge_draft_body -->

## [2026-07-03] pending | c908-wino-gemm-optimization.md
target_page: c908-wino-gemm-optimization.md
target_section: Relationships
source: https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
status: approved
proposed_update: Add a relationship to the XuanTie C908 AI inference benchmark page: '[[xuantie-c908-ai-inference-benchmark]]: This page provides the quantitative performance results (MobileNet speedups, VLEN 256 scaling, comparison with C906) that result from the optimization recipes described here; the benchmark uses SHL and HHB on the XuanTie C908 target.'

## [2026-07-03] merge_pending | xuantie-c908.md
target_page: xuantie-c908.md
canonical_name: XuanTie C908
colliding_name: XuanTie C908
source: https://www.cnx-software.com/2022/11/04/t-head-xuantie-c908-risc-v-core-targets-aiot-applications/
status: applied
<!-- merge_draft_body
# XuanTie C908

The XuanTie C908 is a 64-bit RISC-V core designed by Alibaba's T-Head Semiconductor, targeting mid-range AIoT applications. It implements the RV64GCB[V] instruction set architecture with the RVA22 profile for Android and rich OS compatibility, and supports the optional RISC-V Vector Extension 1.0 (RVV 1.0) to accelerate AI inference workloads. The core features a 9-stage dual-issue in-order pipeline, supports clusters of 1 to 4 cores, and integrates a two-level cache system with hardware cache coherency and optional ECC. Enhanced physical memory protection (ePMP) provides up to 64 regions, and the platform-level interrupt controller (PLIC) handles up to 1023 sources. Performance-wise, the C908 sits between the earlier single-issue in-order C906 and the higher-end out-of-order C910, offering a 24–64% improvement over the C906 in synthetic benchmarks (Coremark, Dhrystone, Whetstone, Linkpacks) and 2–3.5× faster AI inference on MLPerf Tiny benchmarks using INT4 data types. The core can operate at up to 2 GHz on TSMC's 12 nm process, consuming a dynamic power of 52.8 mW/GHz per core, delivering over 20% better energy efficiency than the C906 under identical frequency and process conditions.

## Key Claims

- Supports RV64GCB[V] instruction set with Bit manipulation (B) and optional Vector extension (V).
- Complies with the RVA22 profile for interoperability with Android and other rich operating systems.
- 9-stage dual-issue in-order pipeline; can be configured in clusters of 1–4 cores.
- Two-level cache subsystem with hardware cache coherency and optional ECC.
- Bus interface: AXI4/ACE with optional device coherence port (DCP) and low-latency port (LLP).
- Enhanced physical memory protection (ePMP) with up to 64 regions.
- Programmable platform-level interrupt controller (PLIC) supporting up to 1023 interrupt sources.
- Maximum operating frequency: 2 GHz on TSMC 12 nm process.
- Dynamic power consumption: 52.8 mW/GHz per core on TSMC 12 nm.
- Energy efficiency improvement: >20% over XuanTie C906 under equivalent frequency and process.
- Performance: 24–64% gain over C906 in synthetic benchmarks (Coremark, Dhrystone, Whetstone, Linkpacks) under unspecified test conditions.
- AI inference speedup: 2–3.5× over C906 on MLPerf Tiny v0.7 benchmarks (wake word detection, image classification, keyword spotting, anomaly detection) using INT4 data.
- Includes RV32 COMPAT mode enabling 64-bit CPUs to run 32-bit binaries; merged into Linux 5.19.
- Xuantie custom extensions include Instruction and Memory Attributes Extension (XMAE).
- Virtual address systems: Sv39/Sv48.

## Optimization-Relevant Details

- ISA/profile: RV64GCB[V]; RVA22 profile; Xuantie custom extensions (XMAE).
- Vector/matrix/accelerator support: RISC-V Vector Extension 1.0 (optional, RVV 1.0).
- Memory/cache/TLB/DMA: Two-level cache (L1/L2) with hardware cache coherency and optional ECC; Sv39/Sv48 virtual addressing; AXI4/ACE bus with DCP and LLP interfaces.
- Compiler/toolchain support: Not specified in the source; Xuantie GCC toolchains historically used for earlier XuanTie cores.

## Relationships

No specific relationship to visible context pages. The only context page ([[q4x-quantization-llamacpp-rvv]]) is an optimization recipe for RISC-V vector CPUs, but it was validated on a Milk-V Jupiter (SpacemiT K1) platform, not on the XuanTie C908. Both involve RVV 1.0, but no direct verification or shared evidence links them. The C908 is positioned as a mid-range AIoT core between the C906 and C910, and supports the same RVV 1.0 extension version that the Q4X recipe targets, suggesting potential compatibility, but this remains unconfirmed.

## Sources

- https://www.cnx-software.com/2022/11/04/t-head-xuantie-c908-risc-v-core-targets-aiot-applications/
merge_draft_body -->

## [2026-07-03] merge_pending | xdsl-compiler-toolkit.md
target_page: xdsl-compiler-toolkit.md
canonical_name: xDSL
colliding_name: xDSL
source: https://xdsl.dev/
status: applied
<!-- merge_draft_body
# xDSL

xDSL is a Python-native compiler framework for building compiler infrastructure, centered on SSA-based intermediate representations (IRs). It is MLIR-compatible, using the same textual MLIR format for IR and enabling interoperability with the MLIR ecosystem. The framework provides a library of predefined domain-specific IRs and allows users to define custom IRs for their specific compilation tasks. xDSL is cross-platform, running on any system that supports Python, and is open source under the Apache License v2.0 with LLVM Exceptions. It is maintained by the xDSL project community on GitHub.

## Key Claims

- xDSL is a Python-native compiler framework that uses SSA-based intermediate representations.
- It is MLIR-compatible, sharing the same textual IR format as MLIR, which allows integration with MLIR-based tools.
- The framework includes a library of predefined domain-specific IRs and supports the definition of custom IRs.
- xDSL is cross-platform (runs on any platform with Python) and is open source under the Apache License v2.0 with LLVM Exceptions.
- The project is hosted on GitHub under the xdslproject/xdsl repository.

## Relationships

- [[sophon-sg2044-hardware-target]]: Both xDSL and the Sophon SG2044 are part of the LLVM/MLIR compiler ecosystem; xDSL can produce MLIR that is lowered through LLVM to target the SG2044's C920v2 cores with RVV 1.0 acceleration.

## Sources

- https://xdsl.dev/
- https://github.com/xdslproject/xdsl
merge_draft_body -->

## [2026-07-03] merge_pending | xdsl-compiler-toolkit.md
target_page: xdsl-compiler-toolkit.md
canonical_name: xDSL
colliding_name: xDSL
source: https://github.com/xdslproject/xdsl
status: apply_failed (pipeline rejected)
<!-- merge_draft_body
# xDSL

xDSL is a Python-native SSA compiler framework for building compiler infrastructure. It provides SSA-based intermediate representations (IRs) and Pythonic APIs to define, assemble, and optimize custom IRs, with seamless compatibility with MLIR from the LLVM project. Inspired by MLIR, xDSL enables smooth translation of programs and abstractions between frameworks, allowing users to prototype compilers entirely in Python while accessing MLIR's powerful optimization and code generation pipeline. All IRs in xDSL employ a unified SSA data structure with regions and basic blocks, making it easy to write generic analyses and transformation passes. xDSL supports assembling compilers from predefined or custom IRs, and organizing transformations across a multi-level IR stack, similar to the architecture of projects like Devito, PSyclone, and Firedrake.

## Key Claims

- xDSL is a Python-native SSA compiler framework that provides SSA-based intermediate representations (IRs) and Pythonic APIs to define, assemble, and optimize custom IRs.
- It offers seamless compatibility with MLIR from the LLVM project, enabling translation of programs between frameworks.
- Users can prototype compilers entirely in Python while accessing MLIR's optimization and code generation pipeline.
- All IRs in xDSL use a unified SSA data structure with regions and basic blocks, simplifying generic analyses and transformations.
- It supports assembling compilers from predefined or custom IRs and organizing transformations across a multi-level IR stack.
- The framework is used by projects like Devito, PSyclone, and Firedrake.
- xDSL supports subprojects with extra dependencies for GUI, JAX, and RISC-V (via `xdsl[riscv]`).
- The version is validated against MLIR version 22.1.2.

## Relationships

- [[sophon-sg2044-hardware-target]]: xDSL can compile code for the Sophon SG2044 through its MLIR compatibility, enabling targeting of the SG2044's XuanTie C920v2 cores and RVV v1.0 vector unit.
- [[andes-nx27v-hardware-target]]: xDSL's MLIR interoperation allows it to target the AndesCore NX27V's RVV 1.0 vector processing unit, supporting the development of optimizations for this out-of-order VPU.
- [[xuantie-c906-hardware-target]]: xDSL can be used to design and optimize compilers for the XuanTie C906 through the MLIR infrastructure, leveraging its support for custom RISC-V IRs and transformations.

## Sources

- https://github.com/xdslproject/xdsl
merge_draft_body -->

## [2026-07-03] merge_pending | xdsl-compiler-toolkit.md
target_page: xdsl-compiler-toolkit.md
canonical_name: xDSL
colliding_name: xDSL
source: https://xdsl.readthedocs.io/stable/marimo/
status: apply_failed (pipeline rejected)
<!-- merge_draft_body
# xDSL

xDSL is an open-source Python-native compiler framework that provides MLIR-based intermediate representation (IR) manipulation, dialect definitions, pattern rewriting, and code generation capabilities. Developed as a pure Python library, it enables compiler development directly within Python environments without requiring C++ infrastructure. xDSL uses Marimo notebooks for interactive exploration, allowing users to work with IR nodes, define custom dialects, and apply transformations in a reactive notebook environment. The framework supports multiple assembly-level dialects including RISC-V, LLVM, MPS (Metal Performance Shaders), WGSL (WebGPU Shading Language), and x86, and includes frontends for Python AST and the Pattern Description Language (PDL). It also provides tools for shape inference, equality saturation, and dialect conversion, making it suitable for research and prototyping of compiler optimizations.

## Key Claims

- xDSL is a Python-native compiler framework that operates on MLIR-based IR.
- It uses Marimo notebooks for interactive compiler development with automatic dependency tracking between cells.
- Supports multiple assembly-level dialects: RISC-V, LLVM, MPS, WGSL, and x86.
- Includes frontends for Python AST and PDL (Pattern Description Language).
- Provides rewriting infrastructure and shape inference patterns.
- Supports equality saturation as an optimization technique.
- Has a RISC-V dialect series that includes compiling linalg to Snitch.

## Relationships

- [[xuantie-c906-hardware-target]]: xDSL's RISC-V MLIR dialect provides a compiler-level representation that can target RISC-V cores such as the XuanTie C906, enabling dialect-level analysis and optimization before code generation.

## Sources

- https://xdsl.readthedocs.io/stable/marimo/
merge_draft_body -->

## [2026-07-03] pending | spacemit-x60-hardware-target.md
target_page: spacemit-x60-hardware-target.md
target_section: Relationships
source: https://www.rt-rk.com/gcc-tuning-for-spacemit-x60-building-an-in-order-dual-issue-scheduler-model-part-i/
status: approved
proposed_update: Add a relationship entry linking to the new optimization_recipe page: 'Describes the GCC tuning recipe that implements the instruction scheduling model documented in [[spacemit-x60-gcc-tuning]].'

## [2026-07-03] merge_pending | riscv-matrix-extension-specification.md
target_page: riscv-matrix-extension-specification.md
canonical_name: RISC-V Matrix Extension Specification
colliding_name: RISC-V Matrix Extension Specification
source: https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/
status: applied
<!-- merge_draft_body
# RISC-V Matrix Extension Specification

The RISC-V Matrix Extension Specification is a proposed matrix extension for AI applications under the RISC-V architecture, developed by T-HEAD (XUANTIE-RV). The specification is currently at version 0.6.0 and introduces a tile register file separated from accumulation registers, flexible register shapes not limited to rows = RLEN/32, and additional element-wise instructions for operator fusion. The project includes a specification document, an SHL neural networks library, an ABI manual, an intrinsic API reference manual, a QEMU emulator, a GNU toolchain with compiler and assembler, and demonstration applications for ResNet50 and GEMM. The extension is under construction and provided as a preview demo project, with build instructions and submodule dependencies for evaluation.

## Key Claims

- The specification proposes a matrix extension for RISC-V AI applications, currently at version 0.6.0, developed by T-HEAD (XUANTIE-RV).
- Source and accumulation registers are separated into tile and accumulation registers, supporting different source/destination sizes.
- Matrix register shapes are adjustable, no longer limited to rows = RLEN/32, enabling full coverage from pure outer products to pure inner products.
- New element-wise instructions have been added to facilitate operator fusion.
- The project includes an SHL neural networks library, an ABI manual, an intrinsic API reference manual, a QEMU emulator, and a GNU toolchain with GCC compiler and assembler.
- The specification is under construction and provided as a preview demo project.

## Relationships

No specific relationship to visible context pages in the wiki.

## Sources

- https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/
merge_draft_body -->

## [2026-07-03] merge_pending | sophon-sg2042.md
target_page: sophon-sg2042.md
canonical_name: SOPHON SG2042
colliding_name: Sophon SG2042
source: https://github.com/sophgo/sophgo-doc/blob/main/SG2042/TRM/source/system.rst
status: apply_failed (pipeline rejected)
<!-- merge_draft_body
# Sophon SG2042

Sophon SG2042 is a 64-core RISC-V SoC designed by Sophgo, featuring a network-on-chip (NoC) mesh architecture that partitions four CPU cores into one cluster, with a total of 16 clusters forming the full 64-core array. The system includes 16 System Level Cache (SLC) tiles, each 4 MiB in size (totaling 64 MiB), shared by all cores. Four DRAM controllers are located at the left and right edges of the mesh, accessible by all bus masters. The SoC supports a dual-socket configuration via two CCIX ports, each bound to a PCIe controller, enabling direct chip-to-chip connectivity. A separate System CoProcessor (SCP) outside the mesh handles platform initialization, including PCIe topology setup, DRAM configuration via I2C-based SPD reading, mesh configuration, and loading the RISC-V zero-stage bootloader. The memory subsystem implements RISC-V Sv39 virtual address translation with 40-bit physical addressing, supporting up to 1 TiB of address space in little-endian format.

## Key Claims

- 64 RISC-V CPU cores arranged as 16 clusters of 4 CPUs, connected via a NoC mesh.
- Each cluster has a 4 MiB SLC tile; 16 SLC tiles provide 64 MiB of shared last-level cache.
- Four DRAM controllers accessible by all bus masters on the mesh.
- Dual-socket operation through CCIX ports (CCIX0 bound to PCIe0, CCIX1 bound to PCIe1).
- SCP (System CoProcessor) is an out-of-mesh CPU subsystem responsible for boot-time initialization (PCIe, DRAM, mesh, CCIX, loading zsbl.bin).
- Memory addressing: Sv39 virtual, 40-bit physical, 1 TiB linear space, little-endian.
- Boot sequence: SCP boots from bootrom (SPI flash or SD card), then releases all 64 RISC-V cores.
- Bootrom loads SCP firmware from SPI flash at a given offset or from an SD card with MBR partition table and FAT32 file system (firmware named fip.bin).
- Zero-stage bootloader (zsbl.bin) is the first code executed by RISC-V cores.
- Boot strap pins BOOT_SEL[7:0] control boot device selection, SCP console, and test mode.

## Optimization-Relevant Details

- **ISA/profile**: RISC-V (64-bit), Sv39 virtual memory, 40-bit physical addressing.
- **Vector/matrix/accelerator support**: Not specified in this source; may be covered in other sections of the TRM.
- **Memory/cache/TLB/DMA**: 4 MiB SLC per cluster shared by all cores; DRAM controllers; PCI master nodes handle DMA transactions.
- **Compiler/toolchain support**: Not specified in this source.

## Relationships

- No specific relationship to visible context pages ([[andes-ax45mpv-hardware-target]] is a different vendor's RISC-V core IP without shared design details known from this source).

## Sources

- https://github.com/sophgo/sophgo-doc/blob/main/SG2042/TRM/source/system.rst
merge_draft_body -->

## [2026-07-03] merge_pending | spacemit-x60-gcc-tuning.md
target_page: spacemit-x60-gcc-tuning.md
canonical_name: SpacemiT X60 GCC Tuning
colliding_name: GCC Vector Scheduling for SpacemiT X60
source: https://www.rt-rk.com/gcc-tuning-for-spacemit-x60-building-an-in-order-dual-issue-scheduler-model-part-ii/
status: applied
<!-- merge_draft_body
# GCC Vector Scheduling for SpacemiT X60

This optimization recipe describes the implementation of a dynamic LMUL-based cost scaling model for vector instructions in the GCC scheduler targeting the SpacemiT X60 processor. The SpacemiT X60 has an in-order dual-issue scalar pipeline with two vector execution units (VXU0 and VXU1), but the tuning model initially models only a single vector unit (VXU0) as a stable baseline, splitting operations internally as one wider unit. Unlike scalar instructions with fixed latencies, vector instruction costs vary with the Length Multiplier (LMUL) and Selected Element Width (SEW). The primary transformation replaces a static latency assumption (e.g., LMUL=1) with dynamic cost scaling based on the effective LMUL at scheduling time, implemented through the `riscv_sched_adjust_cost` hook. Scaling is enabled by the `-madjust-lmul-cost` flag, implicitly activated with `-mtune=spacemit-x60`. The pipeline occupancy reservation in the DFA is capped at 7 cycles to prevent "DFA blowup," a compiler internal state explosion, without compromising optimization quality. Validation was performed using LLVM test-suite benchmarks and custom RVV instruction-level microbenchmarks from the camel-cdr/rvv-bench repository on a Banana Pi BPI-F3 board, with latency models derived from llvm-mca simulations and the existing SpacemiT X60 LLVM scheduling model.

## Key Claims

- The SpacemiT X60 vector scheduling model uses a single DFA unit `spacemit_x60_vxu0` to represent the vector pipeline, despite the hardware having two VXU units.
- Instruction latency is scaled purely by LMUL (not SEW) in this initial implementation, using the `riscv_sched_adjust_cost` hook reading the `vlmul_type` attribute.
- The DFA reservation for vector instructions is clamped to a maximum of 7 cycles to avoid state explosion in the scheduler automaton.
- The optimization is activated by the `-madjust-lmul-cost` flag, which is part of the `-mtune=spacemit-x60` tuning.
- The cost model is derived from llvm-mca simulations on the SpacemiT X60 LLVM model and validated with RVV microbenchmarks on a Banana Pi BPI-F3 board.
- A stress test benchmark (`stress_vcompress_heavy`) exercising mixed LMUL levels (m1, m2, m4) demonstrates the improvement of dynamic LMUL scaling over a fixed-latency baseline.

## Transformation

- **Prerequisites**: GCC with RISC-V backend support for the SpacemiT X60 tuning; LLVM model for the same core used as a cross-reference for latency values; a Banana Pi BPI-F3 or equivalent board for validation.
- **Steps**: 1) Define the vector execution unit as a DFA CPU unit (`spacemit_x60_vxu0`) in the machine description. 2) Set instruction reservations with a clamped 7-cycle occupancy for all vector types. 3) Implement the `riscv_sched_adjust_cost` hook to scale base latency by the effective LMUL factor (e.g., 2x for LMUL=2, 4x for LMUL=4, down to 0.125x for LMUL=MF8). 4) Enable the scaling hook with `-madjust-lmul-cost` tied to `-mtune=spacemit-x60`.
- **Expected effect**: The compiler scheduler makes more informed decisions for wide vector register groupings, reducing pipeline bubbles and improving instruction throughput compared to a fixed-latency model.
- **Failure modes**: Without the 7-cycle DFA clamp, the automaton could grow excessively large (DFA blowup), degrading compilation time with negligible scheduling benefit for long-latency operations. If LMUL scaling is not active, the scheduler may over- or underestimate vector instruction costs, leading to suboptimal instruction reordering.
- **Measurements**: Validation used the LLVM test-suite and custom stress tests (e.g., `stress_vcompress_heavy`). The key metric is throughput improvement for vector-heavy workloads; specific numeric results are not included in the source. The model is classified as "derived" because latency values originate from llvm-mca simulations, not direct hardware measurements.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://www.rt-rk.com/gcc-tuning-for-spacemit-x60-building-an-in-order-dual-issue-scheduler-model-part-ii/
merge_draft_body -->

## [2026-07-03] pending | spacemit-x60-hardware-target.md
target_page: spacemit-x60-hardware-target.md
target_section: Key Claims
source: https://camel-cdr.github.io/rvv-bench-results/articles/vector-utf.html
status: approved
proposed_update: Add a Key Claim: 'Achieved 8x speedup for UTF-8 to UTF-16 conversion using RVV vectorization on the X60 core (measured on Banana Pi BPI-F3).' Source: camel-cdr's RVV benchmark article (https://camel-cdr.github.io/rvv-bench-results/articles/vector-utf.html).

## [2026-07-06] merge_pending | sophon-sg2380-hardware-target.md
target_page: sophon-sg2380-hardware-target.md
canonical_name: Sophon SG2380
colliding_name: SOPHON SG2380
source: https://ee.ofweek.com/2024-04/ART-8320315-8220-30631334.html
status: applied
<!-- merge_draft_body
# SOPHON SG2380

SOPHON SG2380 (codename Oasis) is a high-performance RISC-V SoC designed for AI PC (AIPC) applications, jointly developed by SOPHON with SiFive and Imagination Technologies. It integrates 16 SiFive RISC-V P670 processor cores in a big.LITTLE configuration (12 big cores and 4 little cores), paired with an Imagination AXT-16-512 GPU supporting Vulkan 1.3, OpenGL ES 3.3/2.0/1.1, and OpenCL 3.0, and a dedicated SOPHON TPU (tensor processing unit) delivering 32 TOPS at INT8 and 16 TFLOPs at FP16 precision. The SoC features a 256-bit DDR memory interface supporting up to 128 GB of memory with 200 GB/s bandwidth, along with PCIe Gen4 and USB 3.2 Gen2 connectivity. It is designed to run generative AI workloads such as LLaMA-2 13B locally, enabling natural language processing, image generation, and text generation tasks on device.

## Key Claims

- 16-core SiFive RISC-V P670 processor (12 big + 4 little cores) for balanced performance and efficiency.
- Imagination AXT-16-512 GPU with support for Vulkan 1.3, OpenGL ES 3.3/2.0/1.1, and OpenCL 3.0.
- SOPHON TPU providing 32 TOPS (INT8) and 16 TFLOPs (FP16) for AI acceleration.
- 256-bit DDR interface supporting up to 128 GB of memory with 200 GB/s bandwidth.
- Connectivity includes PCIe Gen4 and USB 3.2 Gen2.
- Video decode resolution up to 8192x4320.
- Capable of running LLaMA-2 13B model locally for GenAI tasks.

## Optimization-Relevant Details

- ISA/profile: RISC-V (likely RV64GCV with custom TPU instructions; the P670 cores implement RISC-V standard extensions)
- Vector/matrix/accelerator support: SOPHON TPU for matrix multiplication (INT8/FP16); SiFive X280 (included in TPU cluster) provides RVV 1.0 vector processing
- Memory/cache/TLB/DMA: 256-bit DDR interface up to 128 GB, 200 GB/s; specific cache hierarchy and TLB details not disclosed in source
- Compiler/toolchain support: Not specified in the source

## Relationships

- No specific relationship to visible context pages: [[andes-ax45mpv-hardware-target]] is a different vendor's core IP (Andes Technology) targeting a different market (data-intensive computing) and does not share a common architecture, vendor, or ecosystem with the SOPHON SG2380.

## Sources

- https://ee.ofweek.com/2024-04/ART-8320315-8220-30631334.html (OFweek article, 2024-04-10)
merge_draft_body -->

## [2026-07-06] merge_pending | riscv-v-extension.md
target_page: riscv-v-extension.md
canonical_name: RISC-V V Extension
colliding_name: RVV Bench
source: https://github.com/camel-cdr/rvv-bench
status: applied
<!-- merge_draft_body
# RVV Bench

RVV Bench is a collection of RISC-V Vector (RVV) benchmarks hosted on GitHub under the camel-cdr organization. The project provides a standardized benchmarking suite designed to help developers write portably performant RVV code by offering a set of algorithm benchmarks (located in ./bench/) and instruction cycle count measurements (located in ./instructions/). The benchmarks cover various implementations of common algorithms, while the instruction cycle counter measures the cycle count of RVV instructions by unrolling and looping repeatedly. The repository includes a bench-all.sh script for easy execution and configurable parameters for runtime and precision. Benchmark results are published separately on a companion results page at https://camel-cdr.github.io/rvv-bench-results. The tool requires appropriate Linux kernel settings for performance counter access via /proc/sys/kernel/perf_user_access and /proc/sys/kernel/perf_event_paranoid, and supports both RVV and XTheadVector (deprecated) instruction sets. Licensed under MIT, the project welcomes contributions of new benchmarks and measurement results from different CPUs.

## Key Claims

- RVV Bench provides a collection of RVV benchmarks for writing performant portable RVV code.
- It includes both algorithm benchmarks and instruction cycle count measurements for RVV instructions.
- Benchmark results are published externally at https://camel-cdr.github.io/rvv-bench-results.
- The tool depends on Linux perf event access and configurable kernel parameters (perf_event_paranoid <= 2, perf_user_access must be enabled).
- It supports both standard RVV and XTheadVector (with a separate directory, though maintained as deprecated).
- The project is licensed under the MIT license and accepts contributions via GitHub issues or pull requests.

## Relationships

No specific relationships to visible wiki context pages are established from the source material. The RVV Bench framework is a general-purpose benchmarking tool and does not directly connect to the Q4X quantization recipe page or any other existing page in the current wiki context.

## Sources

- https://github.com/camel-cdr/rvv-bench
merge_draft_body -->

## [2026-07-06] merge_pending | spacemit-k3-hardware-target.md
target_page: spacemit-k3-hardware-target.md
canonical_name: SpacemiT K3
colliding_name: SpacemiT K3
source: https://bruno.verachten.fr/2026/03/12/benchmarking-llama.cpp-on-spacemit-k3-risc-v-ai-cores-vs-standard-rvv-part-4/
status: applied
<!-- merge_draft_body
# SpacemiT K3

SpacemiT K3 is an 8-core RISC-V SoC developed by SpacemiT, integrating eight X100 general-purpose cores operating at up to 2.4 GHz and eight A100 AI accelerator cores at 2.0 GHz, with a shared 8MB L2 cache. It supports the RVA23 profile and the RISC-V Vector Extension 1.0 (RVV 1.0). The X100 cores implement a 256-bit vector length while the A100 cores implement a 1024-bit vector length. The SoC also includes a 60 TOPS AI compute engine and supports extensions such as Zfh, Zvfh, Zfbfmin, Zvfbfmin, Zvfbfwma, and vector cryptography (Zvkng, Zvksg, Zvbc). The chip is used in the Milk-V Jupiter 2 single-board computer and has garnered attention for its dual-core-class architecture combining general-purpose and AI-accelerator cores.

## Key Claims

- Eight X100 cores at up to 2.4 GHz with RVV 1.0 and 256-bit VLEN.
- Eight A100 cores at up to 2.0 GHz with RVV 1.0 and 1024-bit VLEN.
- Shared 8MB L2 cache.
- RVA23 profile compliance.
- 60 TOPS peak AI compute (IME2 matrix instructions).
- Supports FP16/BF16 compute via Zvfh, Zfbfmin extensions.
- Vendor-specific IME2 matrix instructions not publicly documented.
- Powers the Milk-V Jupiter 2 SBC.

## Optimization-Relevant Details

- ISA/profile: RVA23 with RVV 1.0
- Vector/matrix/accelerator support: X100: 256-bit VLEN, A100: 1024-bit VLEN, IME2 matrix instructions (vendor-only)
- Memory/cache/TLB/DMA: 8MB shared L2 cache
- Compiler/toolchain support: llama.cpp (standard and vendor fork)

## Relationships

- [[llama.cpp-on-spacemit-k3-benchmark]]: Records benchmark results on this hardware for LLM inference workloads.
- [[spacemit-ime2-llama-cpp-optimization]]: Describes the vendor IME2 optimization recipe that unlocks A100 performance on this hardware.

## Sources

- https://bruno.verachten.fr/2026/03/12/benchmarking-llama.cpp-on-spacemit-k3-risc-v-ai-cores-vs-standard-rvv-part-4/
merge_draft_body -->

## [2026-07-06] pending | spacemit-x60-hardware-target.md
target_page: spacemit-x60-hardware-target.md
target_section: Key Claims
source: https://spacemit.com/
status: approved
proposed_update: Add claim: 'The SpacemiT X60 core demonstrated a 16% performance improvement in LLVM compiler-optimized code, as presented at the North America RISC-V Summit (October 2025) by Igalia engineer Mikhail (source: spacemit.com press release).' Include mention of the talk titled "Unlocking 15% More Performance: A Case Study in LLVM Optimization for RISC-V", noting the discrepancy between 15% and 16%.

## [2026-07-06] merge_pending | sophon-sg2380-hardware-target.md
target_page: sophon-sg2380-hardware-target.md
canonical_name: Sophon SG2380
colliding_name: Sophgo SG2380
source: https://www.cnx-software.com/2023/10/21/sophgo-sg2380-16-core-sifive-p670-risc-v-processor-20-tops-ai-accelerator/
status: apply_failed (pipeline rejected)
<!-- merge_draft_body
# Sophgo SG2380

The Sophgo SG2380 is a 16-core RISC-V SoC based on SiFive Performance P670 cores with a maximum clock frequency of 2.5 GHz, designed for desktop and edge computing applications. It integrates an Imagination AXT-16-512 GPU for 3D graphics, a video processing unit supporting 4Kp60 decoding of H.265, H.264, AV1, and VP9, and a dual AI accelerator system consisting of an 8-core SiFive Intelligence X280 and a Sophgo TPU coprocessor delivering up to 20 TOPS of INT8 inference performance. The SoC supports up to 64GB of 128-bit LPDDR4/DDR4 memory, UFS 3.2 and SATA 3.0 storage, and includes interfaces such as PCIe Gen3, USB 3.2, HDMI 2.0, and dual MIPI CSI. The SG2380 achieves full RISC-V RVA22 profile compliance and is the first platform to be featured on the Oasis mini-ITX motherboard, with availability expected in the second half of 2024.

## Key Claims

- 16-core SiFive P670 (RV64GCVH) @ up to 2.5 GHz with RISC-V Vector v1.0, Vector Crypto.
- Cluster configuration: 12x performance cores @ 2.5 GHz, 4x efficiency cores @ 1.6 GHz.
- Full RISC-V RVA22 profile compliance.
- Imagination AXT-16-512 GPU: 0.5 TFLOPS, Vulkan 1.3, OpenGL 3.0 support.
- VPU: 4Kp60 decode of H.265, H.264, AV1, VP9; no hardware encoder.
- AI: 8-core SiFive Intelligence X280 (BF16/FP16/FP32/FP64/INT8-64) + Sophgo TPU up to 20 TOPS INT8 via VCIX interface, compatible with OpenXLA/IREE.
- Memory: Up to 64GB via 128-bit DDR, LPDDR4/LPDDR4x 3733Mbps, DDR4 3200Mbps.
- Storage: UFS 3.2, SATA 3.0, QSPI NOR/NAND.
- Video output: eDP 1.2, DP 1.2, HDMI 2.0, MIPI DSI; dual output up to 4Kp60.
- Networking: Gigabit Ethernet via RGMII.
- USB: 1x USB 3.2 Gen1 (5 Gbps) with DP Alt Mode and Power Delivery, 1x USB 3.2 Gen1, 2x USB 2.0.
- PCIe: Gen3 with 8+4+2+1+1 lanes.
- Security: AES/DES/SHA256, TRNG, secure boot, SiFive WorldGuard, 32Kb OTP.
- TDP: 5 – 30 Watts.
- Oasis motherboard: mini-ITX, up to 64GB LPDDR5 5500MT/s, 2x 2.5GbE, M.2 slots, PCIe x16 (x8 signal).

## Optimization-Relevant Details

- **ISA/profile:** RVA22, rv64imafdcvh (implied from P670), RVV 1.0 with Vector Crypto.
- **Vector/matrix/accelerator:** RVV 1.0 (vector length not specified, but typical P670 VLEN=128 or 256); SiFive Intelligence X280 for vector compute; Sophgo TPU via VCIX for matrix operations.
- **Memory/cache/TLB:** Up to 64GB DDR/LPDDR4; cache details not provided.
- **Compiler/toolchain support:** IREE/OpenXLA compatible; GCC and LLVM expected based on RISC-V standard toolchain support.

## Relationships

- [[iree-riscv-microkernel-support]]: The Sophgo SG2380 SoC is an intended hardware target for the IREE RISC-V microkernel optimization recipe, as its Sophgo TPU coprocessor supports OpenXLA/IREE and the SiFive P670 cores comply with the RVA22 profile targeted by the IREE microkernels.

## Sources

- https://www.cnx-software.com/2023/10/21/sophgo-sg2380-16-core-sifive-p670-risc-v-processor-20-tops-ai-accelerator/
merge_draft_body -->

## [2026-07-06] merge_pending | xuantie.md
target_page: xuantie.md
canonical_name: XuanTie
colliding_name: XTheadVector
source: https://github.com/XUANTIE-RV/thead-extension-spec/blob/master/xtheadvector.adoc
status: applied
<!-- merge_draft_body
# XTheadVector

XTheadVector is a non-standard RISC-V vector extension developed by T-Head (XuanTie) for their CPU cores. Version 1.0 of the extension is frozen and stable. XTheadVector is not compatible with the standard RISC-V V extension due to intentional encoding overlaps with V version 0.7.1, and it defines its own instruction prefixes (th.) and CSR prefixes (th.) to avoid conflict with the standard extension. The extension provides 32 vector registers and six unprivileged CSRs (th.vstart, th.vxsat, th.vxrm, th.vl, th.vtype, th.vlenb) that overlap with the corresponding V extension registers. Tools are required to report an error if both XTheadVector and V extensions are enabled simultaneously. The extension is available on XuanTie CPUs with vendor ID 0x5b7, misa bit 21 set, and implementation ID 0, which currently identifies the C906V, C920, and R920 processors.

## Key Claims

- XTheadVector v1.0 is a stable, non-standard RISC-V vector extension that uses an encoding space overlapping with the V extension v0.7.1, making the two extensions mutually exclusive in toolchains.
- The extension adds 32 vector registers and six CSRs prefixed with `th.` instead of the standard `v` prefix.
- All instructions are prefixed with `th.` to distinguish them from standard V instructions.
- Compared to V v0.7.1, XTheadVector adds VLENB CSR, renames CSRs with `th.` prefix, and promotes Zvlsseg to a mandatory part rather than a subextension.
- Compared to V v1.0, XTheadVector lacks vsetivli, whole register moves, fractional LMUL, vlm/vsm, and configurable vta/vma (fixed to TAMU). It also has different load/store instruction encodings and strict register overlap rules for narrowing and comparison operations.
- Availability is gated by vendor ID 0x5b7, misa.V set, and mimpid == 0 (implementation ID zero), identifying C906V, C920, and R920 cores.

The extension defines pseudo instructions (`th.vmmv.m`, `th.vneg.v`, `th.vncvt.x.x.v`, `th.vfneg.v`, `th.vfabs.v`) to improve compatibility with RVV 1.0 source code.

## Optimization-Relevant Details

- ISA/profile: RISC-V vector extension derived from V v0.7.1 with modifications; uses `th.` prefix for instructions and CSRs
- Vector/matrix/accelerator support: 32 vector registers, CSRs for vector length (th.vl), vector type (th.vtype), and vector length in bytes (th.vlenb)
- Memory/cache/TLB/DMA: Not specified in source
- Compiler/toolchain support: Intrinsics header documented (include::xtheadvector/intrinsics.adoc[]), pseudo instructions defined for source-level compatibility with RVV 1.0; no specific toolchain versions mentioned

## Relationships

- [[andes-ax45mpv-hardware-target]]: XTheadVector is a non-standard RISC-V vector extension that conflicts with the standard V extension used by the Andes AX45MPV core, as its encoding overlaps with V v0.7.1 and uses different CSR/instruction naming conventions, making the two incompatible in a single toolchain.

## Sources

- https://github.com/XUANTIE-RV/thead-extension-spec/blob/master/xtheadvector.adoc
merge_draft_body -->

## [2026-07-06] merge_pending | spacemit-k3-hardware-target.md
target_page: spacemit-k3-hardware-target.md
canonical_name: SpacemiT K3
colliding_name: Llama.cpp SpaceMIT K3 Gemma 4 QAT MTP Benchmarks
source: https://github.com/rcarmo/llama-cpp-spacemit-k3/blob/master/README.md
status: applied
<!-- merge_draft_body
# Llama.cpp SpaceMIT K3 Gemma 4 QAT MTP Benchmarks

Benchmark results for running Gemma 4 QAT models (E2B, E4B, 12B, 26B A4B) with Multi-Token Prediction (MTP) on a Milk-V Jupiter 2 board (SpacemiT K3 SoC). All measurements were collected using a custom llama.cpp fork with the SpaceMIT CPU backend and TurboQuant optimizations enabled. The hardware platform uses 8 A100/IME2 preferred cores with TCM (block size 393216) and f16 KV cache. Two benchmark scenarios are reported: a cold-start server benchmark with a synthetic agent prompt (complex coding plan) and a llama-bench sweep across thread counts and ubatch sizes. The results demonstrate practical local LLM inference capability on a RISC-V native board with measured prefill rates up to 120.9 tok/s (Gemma 4 E2B) and generation rates up to 13.36 tok/s. MTP acceptance rates range from 0.306 to 0.429 depending on model size. The 26B A4B model achieves ~8.36 tok/s at 16K context, which is the sweet spot before memory exhaustion at 64K.

## Key Claims

- Gemma 4 E2B QAT (Q4_K_XL): cold prefill 93.14 tok/s, generation 12.93 tok/s, MTP acceptance 0.306, coherence pass.
- Gemma 4 E4B QAT: cold prefill 55.37 tok/s, generation 8.52 tok/s, MTP acceptance 0.336.
- Gemma 4 12B QAT: cold prefill 20.72 tok/s, generation 4.32 tok/s, MTP acceptance 0.429.
- Gemma 4 26B A4B QAT: best tg 8.36 tok/s at ctx=16K/f16 KV; OOM at 64K.
- llama-bench best: E2B prefill 120.90 tok/s (t=8 ub=256 f16), generation 13.36 tok/s (t=8 ub=512 f16).
- Thread count 8 performs best; t=12 causes TCM contention.
- f16 KV cache consistently outperforms q8_0 by ~1.8 tok/s on generation.

## Measurement Context

- Hardware version: SpacemiT K3 board (Milk-V Jupiter 2) with A100/IME2 cores, TCM block size 393216, memory backend HPAGE.
- Software/toolchain version: llama.cpp fork with spacemit backend (build flags: -DGGML_CPU_RISCV64_SPACEMIT=ON -DGGML_RV_ZBA=ON -DGGML_RV_ZFH=ON -DGGML_RV_ZVFH=ON).
- Workload shape: Server benchmark uses synthetic agent prompt (system + user) generating structured output of ~800-900 tokens with temperature=0.2, no max_tokens limit. Llama-bench sweep measures prefill and generation with varying ubatch sizes (256, 512, 1024).
- Metric: Prefill tokens per second, generation tokens per second, MTP acceptance rate (fraction of draft tokens accepted), coherence grade (pass/fail based on stop reason and content quality).
- Method: Cold startup measurements from llama-server after tcm-cleanup; warm request measurements with prompt-cache hit. Llama-bench runs 96 configurations.
- Evidence strength: measured (from live runs on the specific hardware).

## Relationships

No specific relationship to the visible context pages ([[q4x-quantization-llamacpp-rvv]], [[v-seek-llm-inference-optimization-sg2042]]) can be established from the source material; the benchmark targets a different hardware platform (Spacemit K3 vs Jupiter/SG2042) and a different quantization technique (QAT with MTP vs codebook-based Q4X or V-Seek). Future pages on SpaceMIT K3 hardware or the kernel optimizations could strengthen these links.

## Sources

- https://github.com/rcarmo/llama-cpp-spacemit-k3/blob/master/README.md
merge_draft_body -->

## [2026-07-06] merge_pending | sophon-sg2042.md
target_page: sophon-sg2042.md
canonical_name: SOPHON SG2042
colliding_name: Sophon SG2042
source: https://browser.geekbench.com/v5/cpu/21586331
status: apply_failed (pipeline rejected)
<!-- merge_draft_body
# Sophon SG2042

The Sophon SG2042 is a 64-core server-grade RISC-V CPU developed by Sophon Technology, based on the XuanTie C920 cores designed by T-Head (an Alibaba Group company). It operates at 2 GHz and implements the RV64GCV instruction set architecture, which includes the base scalar extensions along with the RISC-V Vector Extension (V). The chip is organised into clusters of four cores each, and features four DDR4-3200 memory controllers with 32 lanes of PCI-Express Gen4 for high-bandwidth I/O. The SG2042 targets high-performance computing workloads and represents a milestone as a high-core-count RISC-V processor for server applications. A Geekbench 5 benchmark run on Linux RISC-V reported a single-core score of 181 and a multi-core score of 3132.

## Key Claims

- 64 RISC-V processor cores running at 2 GHz.
- Cores are based on the XuanTie C920 microarchitecture from T-Head.
- Implements the RV64GCV ISA (includes RISC-V Vector Extension).
- Organized in clusters of four cores.
- Equipped with four DDR4-3200 memory controllers.
- Provides 32 lanes of PCI-Express Gen4.
- Geekbench 5.4.0 Preview results on Linux RISC-V: 181 single-core score, 3132 multi-core score.

## Optimization-Relevant Details

- ISA/profile: RV64GCV (with RISC-V Vector Extension, version unspecified)
- Vector/matrix/accelerator support: RISC-V Vector (V) extension; no further accelerator details from available sources
- Memory/cache/TLB/DMA: Four DDR4-3200 memory controllers; cache hierarchy and TLB details not provided in available snippets
- Compiler/toolchain support: Not specified in available sources (Geekbench 5.4.0 Preview was used for benchmark)

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- Geekbench browser page for SOPHON SG2042 (riscv) - reported single-core score 181, multi-core score 3132 with Geekbench 5.4.0 Preview on Linux RISC-V.
- Performance characterisation of the 64-core SG2042 RISC-V CPU for HPC (arXiv:2406.12394) - describes NPB benchmark characterisation, core cluster organisation, memory controllers, PCIe lanes.
- Sophon SG2042 specification snippet from SOPHON SG2042 | Milk-V page confirming 64-core server chip.
merge_draft_body -->

## [2026-07-06] merge_pending | sophon-sg2042.md
target_page: sophon-sg2042.md
canonical_name: SOPHON SG2042
colliding_name: Sophon SG2042
source: https://www.researchgate.net/publication/381517668_Performance_characterisation_of_the_64-core_SG2042_RISC-V_CPU_for_HPC
status: applied
<!-- merge_draft_body
# Sophon SG2042

The Sophon SG2042 is a 64-core RISC-V CPU designed for high-performance computing (HPC) workloads, first released in summer 2023. It is the first mass-produced, commodity-available high-core-count RISC-V processor aimed at HPC applications, integrating 64 T-Head XuanTie C920 high-performance out-of-order cores. The SG2042 targets computationally intensive workloads and has been benchmarked against x86-64 and AArch64 CPUs using the NAS Parallel Benchmark (NPB) suite. Performance evaluation shows that the SG2042 consistently outperforms all other RISC-V solutions by a factor of 2.6 to 16.7 at the single-core level. However, when compared against x86-64 and AArch64 CPUs, the SG2042 performs well on compute-bound algorithms but suffers decreased relative performance on memory-bandwidth- or latency-bound algorithms, with the memory subsystem identified as the primary bottleneck. The CPU is fabricated by Sophon and represents a significant step toward RISC-V adoption in high-performance environments.

## Key Claims

- The SG2042 is a 64-core RISC-V CPU designed for high-performance workloads, first mass-produced of its kind.
- Integrates T-Head XuanTie C920 cores, which are high-performance out-of-order cores.
- In single-core NPB benchmarks, the SG2042 outperforms all other RISC-V CPUs by 2.6x to 16.7x.
- The memory subsystem is the greatest performance bottleneck, especially for memory-bound algorithms.
- Relative to x86-64 and AArch64, the SG2042 is competitive on compute-bound algorithms but lags on memory-bound ones.

## Relationships

No specific relationships to existing wiki pages can be established from the available source context. The SG2042 is a distinct hardware target not yet represented in the wiki.

## Sources

- arXiv:2406.12394 ("Performance characterisation of the 64-core SG2042 RISC-V CPU for HPC", Brown and Jamieson, June 2024)
merge_draft_body -->

## [2026-07-06] merge_pending | npb-characterization-sg2042.md
target_page: npb-characterization-sg2042.md
canonical_name: NAS Parallel Benchmark characterization of Sophon SG2042
colliding_name: SG2042 NPB Benchmark Characterization
source: https://www.researchgate.net/publication/381517668_Performance_characterisation_of_the_64-core_SG2042_RISC-V_CPU_for_HPC
status: applied
<!-- merge_draft_body
# SG2042 NPB Benchmark Characterization

The Sophon SG2042 64-core RISC-V CPU was characterized using the NASA NAS Parallel Benchmark (NPB) suite in a June 2024 study by Brown and Jamieson (EPCC, University of Edinburgh). The benchmarks compare the SG2042 against other RISC-V CPUs, x86-64 (Xeon Platinum 8170), and AArch64 systems. Single-core results show that the SG2042 outperforms all other RISC-V solutions by a factor of 2.6 to 16.7. Multi-core NPB tests with OpenMP and MPI parallelization reveal that the SG2042 performs competitively on compute-bound algorithms but shows decreased relative performance on memory-bandwidth- or latency-bound workloads, with the memory subsystem identified as the primary bottleneck. The study uses NPB pseudo-applications including the MG (Multi-Grid) benchmark. The measurement method involves running the NPB suite with various configurations and comparing against established HPC CPUs. The evidence strength is measured, as the data comes from direct experimentation.

## Key Claims

- SG2042 delivers 2.6x to 16.7x single-core performance improvement over other RISC-V CPUs.
- On compute-bound NPB benchmarks, the SG2042 performs comparatively well against x86-64 and AArch64 CPUs.
- On memory-bandwidth- or latency-bound benchmarks, relative performance degrades significantly.
- The SG2042's memory subsystem is the greatest performance bottleneck for HPC workloads.

## Measurement Context

- Hardware version: Sophon SG2042 with T-Head XuanTie C920 cores, 64 cores.
- Software/toolchain version: NAS Parallel Benchmark suite, OpenMP, MPI; no specific compiler version reported.
- Workload shape: NPB pseudo-applications (MG, others unspecified).
- Metric: Single-core performance improvement factor; qualitative comparison of compute-bound vs memory-bound.
- Method: Direct benchmarking using NPB suite; single-core and multi-core runs; comparison against Xeon Platinum 8170 and an AArch64 CPU.
- Evidence strength: measured (preprint, experimental results).

## Relationships

No specific relationships to existing wiki pages can be established from the available source context. The SG2042 hardware target is documented in a separate hardware target page.

## Sources

- arXiv:2406.12394 ("Performance characterisation of the 64-core SG2042 RISC-V CPU for HPC", Brown and Jamieson, June 2024)
merge_draft_body -->

## [2026-07-06] merge_pending | spacemit-k3-hardware-target.md
target_page: spacemit-k3-hardware-target.md
canonical_name: SpacemiT K3
colliding_name: SpacemiT K3
source: https://www.cnx-software.com/2026/01/23/spacemit-k3-16-core-risc-v-soc-system-information-and-early-benchmarks/
status: applied
<!-- merge_draft_body
# SpacemiT K3

SpacemiT K3 is a 16-core RISC-V system-on-chip (SoC) developed by SpacemiT, based on the company's custom X100 processor cores and compliant with the RVA23 profile. The SoC operates at up to 2.5 GHz (observed at 2400 MHz in early benchmarks) and includes 32 GB of RAM, a 128 GB NVMe solid-state drive, a 64 GB UFS 2.2 flash device, and two Gigabit Ethernet ports. It runs Ubuntu 26.04 with Linux kernel 6.12. The graphics subsystem uses the saturn-edp driver for embedded DisplayPort output but lacks hardware 3D acceleration (software rendering only). The SoC is designed for server and possibly laptop applications, as evidenced by the eDP interface and the provision of remote-access for benchmarking.

## Key Claims

- 16-core configuration based on SpacemiT X100 cores.
- RVA23-compliant, meeting the hardware requirements for Ubuntu 25.10 and later.
- Operates at up to 2400 MHz in observed benchmarks (advertised 2.5 GHz).
- 32 GB system memory (available: 31.38 GiB).
- 128 GB NVMe SSD and 64 GB UFS 2.2 flash storage.
- Two Gigabit Ethernet ports (one active with dwmac_spacemit_ethqos driver).
- Embedded DisplayPort (eDP) interface via saturn-edp driver.
- No hardware GPU acceleration (softpipe renderer only).
- Temperature sensors are present but report erroneous high values (~413°C CPU); other thermal zones report plausible temperatures around 60–65°C.
- Available as a remote-access server for benchmarking.

## Optimization-Relevant Details

- ISA/profile: RVA23 (RISC-V 64-bit, rv64imafdcv likely from X100 core)
- Vector/matrix/accelerator support: Not specified in source; no dedicated AI accelerator mentioned.
- Memory/cache/TLB/DMA: 10 MiB L2 cache, 32 GB RAM, NVMe and UFS storage, eDP display, Gigabit Ethernet.
- Compiler/toolchain support: Linux kernel 6.12, Ubuntu 26.04, inxi 3.3.40.

## Relationships

- [[andes-ax45mpv-hardware-target]]: Both are high-performance RISC-V targets with vector processing capabilities; Andes AX45MPV is a licensable core IP available for SoC integration, while SpacemiT K3 is a complete SoC that integrates custom X100 cores and provides a system for benchmarking.

## Sources

- https://www.cnx-software.com/2026/01/23/spacemit-k3-16-core-risc-v-soc-system-information-and-early-benchmarks/
merge_draft_body -->

## [2026-07-06] pending | gap9.md
target_page: gap9.md
target_section: Key Claims
source: https://arxiv.org/html/2410.08855
status: approved
proposed_update: Add claim: MATCH compilation framework achieves 2.15x inference latency improvement over DORY on GAP9, measured on the MLPerf Tiny suite (source: arXiv 2410.08855).

## [2026-07-06] merge_pending | riscv-v-extension.md
target_page: riscv-v-extension.md
canonical_name: RISC-V V Extension
colliding_name: RISC-V
source: https://en.wikipedia.org/wiki/RISC-V
status: applied
<!-- merge_draft_body
# RISC-V

RISC-V (pronounced "risk-five") is a free and open standard instruction set architecture (ISA) based on reduced instruction set computer (RISC) principles, originally developed at the University of California, Berkeley starting in 2010. Unlike proprietary ISAs such as x86 and ARM, RISC-V specifications are released under permissive open-source licenses and can be implemented without paying royalties. The ISA supports 32-bit, 64-bit, and 128-bit address space variants, uses a load–store architecture with variable-length encoding (primarily 32-bit instructions with optional 16-bit compressed instructions via the C extension), and is little-endian by default. It defines a small base integer instruction set (RV32I, RV64I, RV128I) plus a growing set of standard extensions including M (integer multiplication and division), A (atomics with LR/SC and fetch-and-op), F (single-precision floating-point), D (double-precision floating-point), Q (quad-precision floating-point), C (compressed 16-bit instructions), B (bit manipulation), V (vector operations), and J (interpreted/JIT language support). Development and maintenance of the standard is managed by RISC-V International, a non-profit organization based in Switzerland with over 4,500 members as of 2025. RISC-V is widely adopted in microcontrollers and embedded systems and is increasingly targeted for higher-performance implementations in mobile, desktop, and server markets, supported by commercial SoCs from companies including SiFive, Andes Technology, SpacemiT, Alibaba, StarFive, and Espressif Systems.

## Key Claims

- RISC-V is an open-standard, royalty-free ISA based on RISC design principles, originally developed at UC Berkeley in 2010 and now maintained by RISC-V International.
- The ISA defines base integer variants for 32-bit (RV32I), 64-bit (RV64I), and 128-bit (RV128I) address spaces, each with a minimal set of instructions.
- Standard extensions cover multiplication (M), atomics (A), floating-point (F/D/Q), compressed instructions (C), bit manipulation (B), vector operations (V), and JIT support (J), among others.
- The architecture uses a load–store design with variable-length encoding (instructions are always little-endian) and a compare-and-branch branching style.
- RISC-V is supported by major Linux distributions and by compilers such as GCC and LLVM.
- Commercial implementations are available from multiple vendors, covering microcontrollers to server-class processors.

## Relationships

- [[sophon-sg2044-hardware-target]]: The SG2044's XuanTie C920v2 cores implement the RISC-V ISA with the ratified Vector Extension version 1.0, using a 128-bit vector unit.
- [[xuantie-c906-hardware-target]]: The XuanTie C906 core implements the RISC-V RV64IMA[FD]C[V] base architecture and adds 130 custom instruction extensions beyond the standard RISC-V set, while also using a 128-bit SIMD vector unit that is not standard RISC-V V.
- [[spacemit-x60-hardware-target]]: The SpacemiT X60 core implements the RISC-V RVA22 profile with the ratified Vector Extension version 1.0 (VLEN 256/128-bit) and is targeted by GCC tuning that models its in-order dual-issue pipeline and vector unit.

## Sources

- https://en.wikipedia.org/wiki/RISC-V
merge_draft_body -->
