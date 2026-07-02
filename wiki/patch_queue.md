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

## [2026-07-02] merge_pending | k230.md
target_page: k230.md
canonical_name: K230
colliding_name: K230
source: https://github.com/kendryte/k230_docs/blob/main/zh/00_hardware/K230_datasheet.md
status: pending_review
<!-- merge_draft_body
# K230

The K230 is a system-on-chip (SoC) developed by Canaan Creative under the Kendryte series, targeting AIoT applications with a multi-heterogeneous unit acceleration computing architecture. It integrates two RISC-V C908 computing cores, one running at up to 800 MHz (CPU0) and the other at up to 1.6 GHz (CPU1), along with a new-generation KPU (Knowledge Process Unit) for AI inference supporting INT8 and INT16 precision. The chip also includes a 2.5D GPU, image processing engines (2D engine, AI 2D engine, 3D depth engine), and a comprehensive set of peripheral interfaces. K230 is designed to provide low latency, high performance, low power consumption, fast startup, and high security, making it suitable for smart door locks, security cameras, dictionary pens, payment recognition, 3D structured light modules, drones, interactive robots, smart home appliances, smart toys, smart manufacturing, and intelligent vehicle cockpits.

## Key Claims

- CPU0: 64-bit RISC-V core, 800 MHz, RISC-V 64GCB instruction set, floating-point unit (FPU), 32 KB instruction cache, 32 KB data cache, 128 KB L2 cache, MMU, PLIC (208 interrupt sources), JTAG debugging, WFI support.
- CPU1: 64-bit RISC-V core, 1.6 GHz, RISC-V Vector Extension 1.0, 128-bit vector processing unit, FPU, 32 KB instruction cache, 32 KB data cache, 256 KB L2 cache, MMU, PLIC, JTAG, WFI.
- KPU: Supports INT8 and INT16 precision with weight sparse compression. Typical network performance at INT8: ResNet-50 ≥85 fps, MobileNet_v2 ≥670 fps, YOLOv5S ≥38 fps.
- Framework support: TensorFlow, PyTorch, TFLite, PaddlePaddle, ONNX. Includes quantization toolchain and profiling tools with less than 1% accuracy loss.
- Extensive operator support: Abs, Acos, Acosh, Add, AveragePool, BatchNormalization, Conv, ConvTranspose, MatMul, Gemm, MaxPool, and many more (see datasheet for full list).

## Optimization-Relevant Details

- ISA/profile: CPU0 uses RISC-V 64GCB; CPU1 adds RVV 1.0.
- Vector/matrix/accelerator support: CPU1 includes 128-bit vector unit; dedicated KPU for AI inference.
- Memory/cache/TLB/DMA: 32 KB L1 I/D cache per core; L2 cache 128 KB (CPU0) and 256 KB (CPU1); MMU present; PLIC with 208 external interrupt sources.
- Compiler/toolchain support: Quantization toolchain provided by Canaan; supports standard ML frameworks (TensorFlow, PyTorch, ONNX, etc.).

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: While the K230 KPU is not derived from Gemmini, this optimization recipe demonstrates a systolic-array accelerator optimization approach applicable to similar hardware targets.
- Insufficient context for additional cross-links; no existing entity pages for RISC-V cores or chip-level AI accelerators are present in the current wiki.

## Sources

- [K230 Datasheet (GitHub)](https://github.com/kendryte/k230_docs/blob/main/zh/00_hardware/K230_datasheet.md)
merge_draft_body -->

## [2026-07-02] merge_pending | k230.md
target_page: k230.md
canonical_name: K230
colliding_name: Kendryte K230
source: https://www.qemu.org/docs/master/system/riscv/k230.html
status: pending_review
<!-- merge_draft_body
# Kendryte K230

The Kendryte K230 is an AIoT SoC from Canaan Inc. that uses a multi-heterogeneous unit accelerated computing structure. It integrates two RISC-V computing cores, one of which is a c908 little core, and a new-generation KPU (Knowledge Process Unit) for AI acceleration. The k230 machine in QEMU emulates this chip for development and testing, providing support for peripherals such as Core Local Interruptor (CLINT), Platform-Level Interrupt Controller (PLIC), watchdog timers, and five UART controllers. The virtual platform is compatible with the Kendryte K230 SDK and can boot via M-mode U-Boot or directly load OpenSBI, Linux kernel, initrd, and device tree binary (DTB). Because QEMU does not emulate the T-HEAD C9xx private MAEE page table attributes, kernels must be rebuilt with standard RISC-V PTE bits to boot under emulation. Specific memory maps and boot procedures are documented in the QEMU user manual for this machine.

## Key Claims

- The Kendryte K230 is a chip from the AIoT SoC series by Kendryte (a part of Canaan Inc.) with a multi-heterogeneous unit accelerated computing structure.
- It has two RISC-V computing cores, including a c908 little core.
- It includes a new-generation KPU (Knowledge Process Unit) smart computing unit.
- The QEMU k230 machine supports CLINT, PLIC, K230 Watchdog Timer, and 5 UART devices.
- Two boot modes are supported: K230 SDK boot via M-mode U-Boot (which then starts OpenSBI/Linux) and direct Linux boot.
- For QEMU boot, kernels must be built with standard RISC-V PTE bits because QEMU does not implement the T-HEAD C9xx private MAEE page table attributes.
- Direct Linux boot uses memory-mapped addresses: OpenSBI at 0x08000000, Linux at 0x08200000, DTB at 0x0a000000, initrd placed by QEMU's generic boot helper.
- U-Boot boot requires Linux Image rebuilt with standard RISC-V PTE bits; loader devices place firmware components at specified RAM addresses.

## Optimization-Relevant Details

- ISA/profile: RISC-V (64-bit), with T-HEAD MAEE page table extensions used by SDK kernels.
- Vector/matrix/accelerator support: KPU (Knowledge Process Unit) for AIOT workloads.
- Memory/cache/TLB/DMA: Not specifically detailed in source; memory map for boot is provided.
- Compiler/toolchain support: K230 SDK includes U-Boot, OpenSBI, and Linux build infrastructure; kernels require standard PTE bits for QEMU.

## Relationships

- [[xuantie-c950]]: Another RISC-V chip from the T-HEAD/XuanTie family, related to the c908 core lineage.
- [[gemmini]]: An open-source systolic array generator for AI acceleration; the K230's KPU targets similar AIoT workloads.
- Insufficient context for additional cross-links to entity pages within the wiki.

## Sources

- [QEMU documentation: Kendryte K230 virt reference platform](https://www.qemu.org/docs/master/system/riscv/k230.html)
merge_draft_body -->

## [2026-07-02] merge_pending | k230.md
target_page: k230.md
canonical_name: K230
colliding_name: Kendryte K230
source: https://linuxgizmos.com/canmv-k230-features-dual-risc-v-processors-and-kpu/
status: pending_review
<!-- merge_draft_body
# Kendryte K230

The Kendryte K230 is a system-on-chip (SoC) from Canaan (formerly Kendryte) that integrates two 64-bit RISC-V C908 cores—a high-performance core clocked at up to 1.6 GHz supporting the RISC-V Vector Extension 1.0 with FPU and VPU, and a low-power core running at up to 800 MHz supporting the RISC-V 64GCB instruction set—alongside a knowledge process unit (KPU) for AI inference with INT8 and INT16 precision, a depth processing unit (DPU), and a video processing unit (VPU). The chip targets applications in robotics, computer vision, and smart devices. The CanMV-K230 development board features this SoC with 512 MB DDR3, a MicroSD slot, QSPI flash, HDMI, MIPI DSI display (1080p@60fps), 3x MIPI CSI camera interfaces, USB 2.0 OTG, 100 Mbps Ethernet, and a 40-pin expansion header offering up to 29 GPIO pins, 5 PWM channels, and multiple I2C interfaces.

## Key Claims

- Integrates dual RISC-V C908 cores: Core1 at 1.6 GHz with RVV 1.0, Core0 at 800 MHz with RV64GCB.
- KPU supports multi-precision AI computing with INT8 and INT16.
- DPU supports 3D structured light depth calculation at 1280×800@30fps.
- VPU supports H.264/H.265/JPEG/MJPEG encoding/decoding up to 4K@40fps.
- Board includes 512 MB DDR3, MicroSD slot, HDMI, MIPI DSI, 3x MIPI CSI, USB 2.0 OTG, 100 Mbps Ethernet.
- 40-pin expansion header with 29x GPIO, 5x PWM, 4x I2C (documentation states 4x I2C; board provides up to 2x I2C on header).
- Compatible with TensorFlow and PyTorch for AI workload deployment.

## Optimization-Relevant Details

- ISA/profile:
  - Core0: RISC-V 64GCB (RV64GCB)
  - Core1: RISC-V 64-bit with Vector Extension 1.0, FPU, VPU
- Vector/matrix/accelerator support:
  - RISC-V Vector Extension 1.0 on Core1 (vector length unspecified)
  - KPU: dedicated AI accelerator with INT8/INT16
  - DPU: 3D depth computation
- Memory/cache/TLB/DMA:
  - 512 MB DDR3 (onboard) via CanMV-K230 board
- Compiler/toolchain support:
  - TensorFlow, PyTorch (for KPU deployment)
- Additional accelerators:
  - 2D image engine, AI 2D engine, 2.5D GPU, 3D depth engine

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: While not directly related, this optimization recipe targets a different systolic array accelerator; the K230's KPU may benefit from similar factoring techniques in future work. Insufficient context for additional cross-links.

## Sources

- [CanMV K230 features dual RISC-V processors and KPU (LinuxGizmos)](https://linuxgizmos.com/canmv-k230-features-dual-risc-v-processors-and-kpu/)
merge_draft_body -->

## [2026-07-02] merge_pending | k230.md
target_page: k230.md
canonical_name: K230
colliding_name: Kendryte K230
source: https://www.youyeetoo.com/products/canmv-k230-kendryte-k230-risc-v64-board
status: pending_review
<!-- merge_draft_body
# Kendryte K230

The Kendryte K230 is a RISC-V based system-on-chip (SoC) designed by Canaan (formerly Kendryte) for AI vision and edge computing applications. It features a dual-core CPU architecture: a high-performance core operating at 1.6GHz that supports the RISC-V Vector Extension 1.0 (RVV 1.0) along with a floating-point unit (FPU) and video processing unit (VPU), and a power-efficient core running at 800MHz that supports the RV64GCB instruction set. The SoC integrates a neural network processing unit (KPU) with hardware support for INT8 and INT16 quantization, enabling efficient inference for deep learning models. It includes interfaces for camera input, HDMI and MIPI DSI display output, Ethernet, and USB/OTG, and is commonly deployed on the CanMV-K230 development board which provides 512MB LPDDR3 memory, QSPI flash, and a microSD card slot. The SoC is compatible with multiple AI frameworks including TVM, TensorFlow, PyTorch, and ONNX, allowing flexible model deployment.

## Key Claims

- Dual-core RISC-V architecture: 1.6GHz (RVV 1.0, FPU, VPU) and 800MHz (RV64GCB) cores.
- Integrated KPU supports INT8 and INT16 quantization.
- Typical neural network inference performance on KPU: Resnet50 ≥85fps INT8, Mobilenet_v2 ≥670fps INT8, YoloV5S ≥38fps INT8.
- Compatible with TVM, TensorFlow, PyTorch, and ONNX for model deployment.
- Memory: 512MB LPDDR3.
- Display output: HDMI, MIPI DSI up to 1080p60.
- Storage: QSPI flash, microSD card slot.
- Connectivity: Ethernet, USB/OTG, serial console.

## Optimization-Relevant Details

- ISA/profile: RV64GCBV (high-performance core), RV64GCB (efficiency core).
- Vector/matrix/accelerator support: RVV 1.0 (vector length not specified), KPU for neural network acceleration.
- Memory/cache/TLB/DMA: 512MB LPDDR3; details not specified for cache hierarchy.
- Compiler/toolchain support: TVM, TensorFlow, PyTorch, ONNX; typical RISC-V GCC/LLVM toolchain expected.

## Relationships

- [[xuantie-c950]]: Another high-performance RISC-V SoC targeting AI applications, though with a different architectural focus (server-class).
- [[sifive-intelligence-x160-gen-2]]: A 32-bit RISC-V AI core from SiFive; comparison highlights the different bit-width and vector capabilities.
- Insufficient context for additional cross-links; the wiki lacks entity pages for related RISC-V AI SoCs or board vendors.

## Sources

- [Youyeetoo CanMV-K230 product page](https://www.youyeetoo.com/products/canmv-k230-kendryte-k230-risc-v64-board)
- [NuttX documentation for CanMV K230](https://nuttx.apache.org/docs/latest/platforms/risc-v/k230/index.html)
merge_draft_body -->

## [2026-07-02] pending | nncase.md
target_page: nncase.md
target_section: Key Claims
source: https://gitee.com/kendryte/nncase
status: pending_review
proposed_update: Expand the Key Claims section and add a new subsection 'Detailed Benchmarks' with the full benchmark table from the source. The table includes models (mobilenetv2, resnet50V2, yolov5s, yolov8s variants, etc.), input shapes, quantization type (u8/u8), nncase FPS, original model accuracy (tflite/onnx), and nncase accuracy on ImageNet 2012 and COCO val2017. For example: mobilenetv2 [1,224,224,3] achieves 600.24 FPS with top-1 accuracy 71.3% (original) vs 71.1% (nncase); resnet50V2 [1,3,224,224] achieves 86.17 FPS with top-1 75.44% vs 75.11%; yolov5s_det [1,3,640,640] achieves 23.645 FPS with mAP50 0.567 vs 0.566. Add these as bullet-point claims under Key Claims and optionally include the HTML table from the source.

## [2026-07-02] merge_pending | tenstorrent-grayskull-e75.md
target_page: tenstorrent-grayskull-e75.md
canonical_name: Tenstorrent Grayskull e75
colliding_name: Tenstorrent Grayskull e150
source: https://www.research.ed.ac.uk/en/publications/accelerating-stencils-on-the-tenstorrent-grayskull-risc-v-acceler
status: pending_review
<!-- merge_draft_body
# Tenstorrent Grayskull e150

The Tenstorrent Grayskull e150 is a RISC-V based PCIe accelerator designed for high-performance computing workloads, built on the Tensix core architecture that decouples data movement from compute. This accelerator targets HPC applications such as stencil computations and can be clustered for higher performance. In a 2024 study by Brown and Barton, the Grayskull e150 demonstrated performance comparable to a Xeon Platinum CPU when executing the Jacobi iterative method, using approximately five times less energy. Scaling to four e150 cards yielded roughly four times the CPU performance at similar energy efficiency. The accelerator operates on BF16 datatype, contrasting with the FP32 baseline of the CPU, and is programmed via RISC-V vector instructions. The architecture supports PCIe integration into existing systems, making it a middle-ground solution for adopting RISC-V in HPC without replacing entire CPU solutions.

## Key Claims

- RISC-V based PCIe accelerator with Tensix core architecture.
- Decouples data movement from compute within each core.
- BF16 datatype support.
- Single e150 delivers similar performance to a Xeon Platinum CPU (BF16 vs FP32) with approximately five times less energy.
- Four e150 cards provide approximately four times the CPU performance at around five times less energy.
- Targeted at HPC workloads such as stencil computations (e.g., Jacobi iterative method).

## Optimization-Relevant Details

- ISA/profile: RISC-V with custom Tensix extensions for data movement.
- Vector/matrix/accelerator support: Proprietary Tensix cores (not standard RVV).
- Memory/cache/TLB/DMA: Not specified in available source.
- Compiler/toolchain support: Not specified; likely uses RISC-V toolchain with custom intrinsics.

## Relationships

- [[gemmini]]: Both Tenstorrent Grayskull and Gemmini are RISC-V-based accelerator platforms, though Gemmini generates systolic arrays while Grayskull uses Tensix cores.
- [[nncase]]: nncase is a compiler stack for RISC-V AI accelerators; similar compilation toolchains may be applicable to Grayskull.

## Sources

- [Accelerating stencils on the Tenstorrent Grayskull RISC-V accelerator (arXiv)](https://arxiv.org/pdf/2409.18835)
merge_draft_body -->

## [2026-07-02] merge_pending | sifive-intelligence-x280.md
target_page: sifive-intelligence-x280.md
canonical_name: SiFive Intelligence X280
colliding_name: SiFive Intelligence X280 Gen 2
source: https://semiiphub.com/ip/multi-core-capable-risc-v-processor-ip-with-vector-extensions-ip-23509
status: pending_review
<!-- merge_draft_body
# SiFive Intelligence X280 Gen 2

The SiFive Intelligence X280 Gen 2 is a 64-bit RISC-V CPU core from SiFive's 2nd Generation Intelligence family, designed for edge artificial intelligence and machine learning compute workloads. It features an 8-stage dual-issue in-order superscalar scalar pipeline with wide vector processing capabilities, supporting a vector length (VLEN) of 512 bits and a datapath width (DLEN) of 256 bits. The core implements the RISC-V Vector Extension v1.0 (RVV 1.0) and includes SiFive Intelligence Extensions to accelerate critical AI/ML operations. It supports multi-core and multi-cluster configurations, with up to 4 cores per cluster, making it suitable for standalone AI processing or accelerator control and assist at the edge. The design also hybridizes RISC-V cores with TPU-like architecture characteristics for enhanced data center AI performance.

## Key Claims

- 8-stage dual-issue in-order superscalar scalar pipeline.
- Vector processing with 512-bit VLEN and 256-bit DLEN.
- Full support for RISC-V Vector Extension v1.0 (RVV 1.0).
- SiFive Intelligence Extensions for AI/ML operation acceleration.
- Multi-core and multi-cluster configuration, up to 4 cores per cluster.
- Optimized for AI/ML compute at the edge, with capability for accelerator control.
- Hybridizes RISC-V cores with TPU architecture for data center AI applications.
- 64-bit RISC-V ISA, Linux capable.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit, RVV 1.0.
- Vector/matrix/accelerator support: 512-bit VLEN, 256-bit DLEN; SiFive Intelligence Extensions.
- Memory/cache/TLB/DMA: Not specified in available sources.
- Compiler/toolchain support: Not specified in available sources (expected RISC-V GC/LLVM with vector extension support).

## Relationships

- [[sifive-intelligence-x160-gen-2]]: Lower-end 32-bit variant in the same 2nd Generation Intelligence family, with 128-bit VLEN and 64-bit DLEN.
- [[gemmini]]: Related open-source systolic array generator; the X280 Gen 2 can serve as a scalar controller for accelerator designs such as those generated by Gemmini.

## Sources

- [SemiWiki IP listing for Multi-core capable RISC-V processor with vector extensions](https://semiiphub.com/ip/multi-core-capable-risc-v-processor-ip-with-vector-extensions-ip-23509)
- [SiFive Enhances Popular X280 Processor IP to Meet... | SemiWiki](https://semiwiki.com/ai/sifive/349230-sifive-enhances-popular-x280-processor-ip-to-meet/)
- [RISC-V is Outstanding in Vector Processing, Part II: SiFive RISC-V with Vector Extensions](https://semiwiki.com/ai/sifive/349210-risc-v-is-outstanding-in-vector-processing-part-ii-sifive-risc-v-with-vector-extensions/)
merge_draft_body -->

## [2026-07-02] merge_pending | sifive-intelligence-x280.md
target_page: sifive-intelligence-x280.md
canonical_name: SiFive Intelligence X280
colliding_name: SiFive Intelligence X280
source: https://riscv.org/blog/sifive-enhances-popular-x280-processor-ip-to-meet-accelerated-demand-for-vector-processing-sifive/
status: pending_review
<!-- merge_draft_body
# SiFive Intelligence X280

The SiFive Intelligence X280 is a RISC-V vector processor core from SiFive, announced in June 2022 with a set of enhanced features designed to meet accelerated demand for vector processing. The enhanced version introduces scalability up to a 16-core cache-coherent complex, WorldGuard trusted protection for security, and a new Vector Coprocessor Interface eXtension (VCIX) that enables seamless integration between the X280's vector unit and customer-designed external AI accelerators or other coprocessors. The X280 is described as the most widely adopted implementation of the RISC-V Vector extension, targeting workloads that require high-performance vector processing as an alternative to legacy SIMD-style architectures. It is part of the broader SiFive Intelligence family of processors optimized for AI and compute-intensive applications.

## Key Claims

- The X280 is scalable up to a 16-core cache-coherent complex.
- It includes WorldGuard trusted protection for hardware-enforced security domains.
- It introduces VCIX (Vector Coprocessor Interface eXtension) for integration with external AI accelerators and coprocessors.
- The X280 is the most widely adopted implementation of the RISC-V Vector extension.
- It serves as an alternative to legacy SIMD-style architectures.

## Optimization-Relevant Details

- ISA/profile: RISC-V with Vector Extension (RVV).
- Vector/matrix/accelerator support: VCIX interface for connecting external AI accelerators or coprocessors to the vector unit.
- Memory/cache/TLB/DMA: Not specified in available sources.
- Compiler/toolchain support: Not specified in available sources.

## Relationships

- [[sifive-intelligence-x160-gen-2]]: A sibling core in the SiFive Intelligence family, sharing design philosophy and interfaces but targeting different performance/power trade-offs.
- Insufficient context for additional cross-links; no existing entity pages for VCIX, WorldGuard, or the broader SiFive Intelligence family are present in the wiki.

## Sources

- [SiFive Enhances Popular X280 Processor IP to Meet Accelerated Demand for Vector Processing | SiFive - RISC-V International](https://riscv.org/blog/sifive-enhances-popular-x280-processor-ip-to-meet-accelerated-demand-for-vector-processing-sifive/)
merge_draft_body -->

## [2026-07-02] merge_pending | llvm-rv.md
target_page: llvm-rv.md
canonical_name: llvm-rv
colliding_name: LLVM RISC-V Vector Extension Support
source: https://llvm.org/docs/RISCV/RISCVVectorExtension.html
status: pending_review
<!-- merge_draft_body
# LLVM RISC-V Vector Extension Support

LLVM RISC-V Vector Extension Support is the implementation of the RISC-V Vector Extension (RVV) version 1.0 within the LLVM compiler infrastructure. The support models RVV using scalable vector types of the form <vscale x n x ty>, where the factor n controls LMUL (vector length multiplier) and the element type ty controls SEW (standard element width). The vscale factor is defined as VLEN/64, requiring VLEN to be at least 64 bits. Mask vectors are represented as <vscale x k x i1> where k depends on the SEW/LMUL ratio. The LLVM IR represents vector instructions both as regular scalable and fixed-length vector operations and through RISC-V vector intrinsics that mirror the C intrinsics specification with masked and unmasked variants. The SelectionDAG lowering handles fixed-length vectors by lowering them to scalable container types with insertion and extraction of subvectors, using VL nodes to control the vector length.

## Key Claims

- The RISC-V target supports RVV version 1.0 in LLVM 23.0.
- Scalable vector types <vscale x n x ty> are used where n controls LMUL and ty controls SEW.
- vscale is defined as VLEN/64, so VLEN must be at least 64 bits (VLEN=32 not supported).
- LMUL can be 1/8, 1/4, 1/2, 1, 2, 4, or 8; SEW can be i8, i16, i32, i64, half, float, double, bfloat.
- Mask vectors are mapped to <vscale x k x i1> where k ranges from 1 to 64 based on the SEW/LMUL ratio.
- Vector instructions are represented either as regular LLVM IR instructions (scalable or fixed-length) or as RISC-V vector intrinsics with unmasked and masked variants.
- RISC-V vector intrinsics include passthru and AVL operands for controlling inactive/tail elements and active vector length.
- Fixed-length vectors are custom lowered to scalable container types using insert_subvector and extract_subvector nodes with VL nodes containing an AVL operand.
- The RISCVVLOptimizer pass automatically reduces the AVL to avoid vsetvli toggles for most instructions.
- LLVM only supports ELEN=32 or ELEN=64.

## Relationships

- [[llvm-riscv-fptrunc-narrowing-optimization]]: This optimization recipe targets RISC-V and relies on LLVM's RVV support for vector code generation.
- Insufficient context for additional cross-links; no entity pages are available in the current wiki context.

## Sources

- [RISC-V Vector Extension — LLVM 23.0.0git documentation](https://llvm.org/docs/RISCV/RISCVVectorExtension.html)
merge_draft_body -->

## [2026-07-02] merge_pending | spacemit-k1.md
target_page: spacemit-k1.md
canonical_name: SpacemiT K1
colliding_name: SpacemiT K1
source: https://www.cnx-software.com/2024/04/30/muse-book-laptop-spacemit-k1-octa-core-risc-v-ai-processor-16gb-ram/?trk=article-ssr-frontend-pulse_little-text-block
status: pending_review
<!-- merge_draft_body
# SpacemiT K1

The SpacemiT K1 is an octa-core 64-bit RISC-V SoC compliant with the RVA22 profile and featuring the RVV 1.0 (256-bit vector extension). It integrates an unnamed GPU supporting OpenCL 3.0, OpenGL ES 3.2, and Vulkan 1.2, a VPU capable of 4K H.265/H.264/VP9/VP8 encoding and decoding, and a 2.0 TOPS AI NPU. The SoC supports up to 16GB of LPDDR4/LPDDR4X memory with up to 10.6 GB/s bandwidth, and includes storage interfaces for eMMC 5.1, SDIO 3.0, and NVMe over PCIe 2.1. Connectivity includes dual GMAC, multiple PCIe lanes, USB 3.0, and low-speed interfaces such as SPI, I2C, UART, CAN-FD, and PWM. The chip operates with a typical TDP of 3-5W and supports an industrial temperature range of -40°C to 85°C. Software support includes Bianbu OS (Debian-based), mainline Linux, and RTOS.

## Key Claims

- First RISC-V SoC compliant with the RVA22 standard.
- First RISC-V SoC compliant with the 256-bit RVV 1.0 standard.
- AI NPU delivering 2.0 TOPS.
- Octa-core X60 cores claim to be faster than Cortex-A55 in multi-core configurations.
- Supports up to 16GB of LPDDR4X memory.
- Standard power consumption of 3-5W TDP.
- Industrial temperature range from -40°C to 85°C.
- Software ecosystem includes Bianbu OS, mainline Linux, and RTOS.
- Integrated VPU supports 4K H.265/H.264/VP9/VP8 encoding and decoding.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit, RVA22 profile.
- Vector/matrix/accelerator support: RVV 1.0 (256-bit vector length), AI NPU 2.0 TOPS.
- Memory/cache/TLB/DMA: Up to 16GB LPDDR4X, eMMC 5.1, SDIO 3.0, NVMe via PCIe 2.1.
- Compiler/toolchain support: Bianbu OS (Debian-based), mainline Linux, RTOS; optimized libraries such as OpenCV, OpenBLAS, XNNPACK.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: Existing page on systolic array optimization (unrelated to SpacemiT K1).
- Insufficient context for additional cross-links; no related workloads, recipes, or toolchain pages are present in the wiki.

## Sources

- [CNX Software - Muse Book laptop featuring SpacemiT K1](https://www.cnx-software.com/2024/04/30/muse-book-laptop-spacemit-k1-octa-core-risc-v-ai-processor-16gb-ram/)
merge_draft_body -->

## [2026-07-02] merge_pending | spacemit-k1.md
target_page: spacemit-k1.md
canonical_name: SpacemiT K1
colliding_name: SpacemiT Key Stone K1
source: https://wccftech.com/chinese-startup-unveils-first-risc-v-based-ai-cpu-powers-k1-domestic-laptop/
status: pending_review
<!-- merge_draft_body
# SpacemiT Key Stone K1

The SpacemiT Key Stone K1 is an octa-core RISC-V system-on-chip (SoC) designed for AI computing and introduced by the Chinese startup SpacemiT (IntoTimeSpace) in April 2024. It integrates eight X60 RISC-V cores compliant with the RVA22 profile, delivering a reported 2.0 TOPS of AI acceleration from its on-chip NPU. The K1 supports up to 16 GB of LPDDR4X-2666 memory and includes storage interfaces such as eMMC (up to 128 GB) and an M.2 PCIe 2.1 x2 slot for NVMe SSDs up to 1 TB. It powers the SpacemiT Muse Book 1st Gen laptop, which runs the Bianbu OS (Debian-based) and features a 14.1-inch 1920x1080 IPS display with 72% NTSC color gamut. The chip is aimed at demonstrating RISC-V viability in the AI segment, with claimed performance advantages over ARM Cortex-A55 cores including up to 130% higher single-core performance and 60–80% lower power consumption. Networking is provided via a Realtek RTL8852BE WiFi 6 module, and power delivery uses USB PD 3.1 (65 W adapter). The SoC is packaged in a laptop weighing 1.36 kg and measuring 322.6×209.2×17.8 mm.

## Key Claims

- Octa-core X60 RISC-V cores compliant with RVA22 profile.
- Integrated 2.0 TOPS AI NPU for on-device acceleration.
- Supports LPDDR4X-2666 memory up to 16 GB.
- Storage options: 32 GB eMMC (default, option up to 128 GB) and M.2 NVMe SSD up to 1 TB.
- WiFi 6 (RTL8852BE) and USB PD 3.1 (65 W) connectivity.
- Claimed 130% higher single-core performance versus ARM Cortex-A55 (source: wccftech article citing jasonwill tweet).
- Claimed 60–80% lower power consumption versus ARM Cortex-A55 (same source).
- Claimed 1.5× deployment efficiency for AI models compared to ARM (same source).
- Powers the SpacemiT Muse Book 1st Gen laptop with Bianbu OS (Debian-based).

## Optimization-Relevant Details

- ISA/profile: RISC-V RVA22 profile (ratified vector extension included via X60 cores).
- Vector/matrix/accelerator support: 2.0 TOPS AI NPU; core vector unit details not specified in source.
- Memory/cache/TLB/DMA: LPDDR4X-2666 interface; cache hierarchy not publicly detailed.
- Compiler/toolchain support: Bianbu OS (Debian-based), Ubuntu, Linux; expects standard RISC-V GCC/LLVM toolchain.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: This optimization recipe targets Gemmini, another RISC-V AI accelerator design, and represents related work in the RISC-V AI acceleration space.
- Insufficient context for additional cross-links in the wiki.

## Sources

- [Chinese Startup Unveils The First RISC-V Based AI CPU, Powers The K1 Domestic Laptop – Wccftech](https://wccftech.com/chinese-startup-unveils-first-risc-v-based-ai-cpu-powers-k1-domestic-laptop/)

Specifications compiled by CNX Software as referenced in the article.
merge_draft_body -->

## [2026-07-02] merge_pending | banana-pi-bpi-f3.md
target_page: banana-pi-bpi-f3.md
canonical_name: Banana Pi BPI-F3
colliding_name: Banana Pi BPI-F3
source: https://4pda.to/forum/index.php?showtopic=1091545
status: pending_review
<!-- merge_draft_body
# Banana Pi BPI-F3

The Banana Pi BPI-F3 is an industrial-grade RISC-V single-board computer built around the SpacemiT K1 system-on-chip. The SoC integrates eight X60 CPU cores implementing the RV64GCVB ISA with the RVA22 profile and full RVV 1.0 vector extension support, providing 2.0 TOPS of AI compute through an on-chip neural processing unit. The board includes 4GB of onboard DDR memory and 16GB of eMMC storage, with additional expansion via a PCIe-connected M.2 slot. Networking is provided by dual Gigabit Ethernet ports (with PoE support via an add-on HAT), dual-band 2.4G/5G WiFi, and Bluetooth 4.2. Display output is via a full-size HDMI 1.4 port supporting up to 1080p at 60Hz, and four USB 3.0 ports are available for peripherals.

## Key Claims

- The SpacemiT K1 is an 8-core RISC-V processor with X60 cores, RVA22 profile, and RVV 1.0 vector extension.
- The SoC delivers 2.0 TOPS of AI computing power from its integrated NPU.
- Onboard memory includes 4GB DDR and 16GB eMMC.
- The board provides 2x GbE Ethernet, HDMI 1.4 (1080p@60fps), WiFi 2.4G/5G, Bluetooth 4.2, 4x USB 3.0, and PCIe M.2.
- PoE support is available via an add-on HAT.

## Optimization-Relevant Details

- **ISA/profile**: RV64GCVB, RVA22
- **Vector/matrix/accelerator support**: RVV 1.0 (128-bit vector length expected per X60 core), integrated 2.0 TOPS NPU
- **Memory/cache/TLB/DMA**: 4GB DDR (evidently onboard, capacity and type not further specified), 16GB eMMC storage
- **Compiler/toolchain support**: Not documented in this source; standard RISC-V toolchains (GCC/LLVM) should be compatible given RVA22 compliance.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: This existing optimization recipe targets a different hardware platform, but the BPI-F3 could serve as a candidate target for similar systolic-array optimizations given its AI accelerator and vector support.
- Insufficient context for additional cross-links; no other directly related pages were found in the wiki context.

## Sources

- [4PDA Forum - Banana Pi F3 SpacemiT K1 (X60™)](https://4pda.to/forum/index.php?showtopic=1091545)
merge_draft_body -->

## [2026-07-02] merge_pending | spacemit-k1.md
target_page: spacemit-k1.md
canonical_name: SpacemiT K1
colliding_name: SpacemiT Key Stone K1
source: http://wikidevi.wive-ng.ru/SpacemiT
status: pending_review
<!-- merge_draft_body
# SpacemiT Key Stone K1

The SpacemiT Key Stone K1 is a high-performance, ultra-low-power system-on-chip developed by SpacemiT (associated with SinoVoIP), integrating eight RISC-V CPU cores based on the RV64GC 64-bit instruction set and operating at a frequency of 1.6 GHz. It incorporates a dedicated Daoyi AI accelerator for machine learning inference tasks. The SoC targets embedded edge AI and networking applications, with reported usage in the Start9 RISC-V Router running a fork of OpenWrt. Software support includes the Armbian Linux distribution, indicating active community and ecosystem development. The K1 is manufactured in the PRC and is available as a sample.

## Key Claims

- 8-core RISC-V RV64GC CPU at 1.6 GHz (source: WikiDevi snippet "CPU: SpacemiT Key Stone K1 (X60) @1.6GHz. SoC: Octa-Core RISC-V (RV64GC) 64-bit.")
- Integrated SpacemiT Daoyi AI accelerator for machine learning (source: docs-chip snippet "integrates 8 RISC-V CPU cores with SpacemiT Daoyi AI computing power.")
- Used in the Start9 RISC-V Router with a custom OpenWrt-based firmware (StartWRT) (source: Russian-language snippet)
- Supported by Armbian Linux, as listed among partner platforms (source: Armbian partner list snippet)

## Optimization-Relevant Details

- ISA/profile: RV64GC
- Vector/matrix/accelerator support: Daoyi AI accelerator (details not specified in available sources)
- Memory/cache/TLB/DMA: Not specified in available sources
- Compiler/toolchain support: Not specified; RISC-V GCC/LLVM likely compatible

## Relationships

No existing entity pages directly related to SpacemiT Key Stone K1 are present in the wiki. Insufficient context for additional cross-links.

## Sources

- [WikiDevi - SpacemiT](http://wikidevi.wive-ng.ru/SpacemiT)
- [docs-chip/en/key_stone/k1/k1_docs/k1_ds.md at main](https://github.com/spacemit-tech/docs-chip/blob/main/en/key_stone/k1/k1_docs/k1_ds.md)
- Armbian partner list (snippet mentioning SpacemiT)
merge_draft_body -->

## [2026-07-02] merge_pending | banana-pi-bpi-f3.md
target_page: banana-pi-bpi-f3.md
canonical_name: Banana Pi BPI-F3
colliding_name: Banana Pi F3
source: https://dev.to/gounthar/running-a-local-llm-on-risc-v-building-llamacpp-on-a-banana-pi-f3-part-1-4d5g
status: pending_review
<!-- merge_draft_body
# Banana Pi F3

The Banana Pi F3 is a single-board computer built around the SpacemiT K1 SoC, which houses an 8-core SpacemiT X60 RISC-V processor operating at 1.6 GHz. The board provides 16 GB of LPDDR4 RAM (approximately 14 GB available to the operating system), 116 GB of eMMC storage, and runs Armbian 25.11.2 (Debian 13 trixie) with kernel 6.6.99-current-spacemit. It is designed for AI and edge computing workloads, with support for RISC-V Vector (RVV 1.0) extensions including the zvfh float16 vector extension. The platform has been used for local LLM inference via llama.cpp, achieving approximately 8.5 tokens/second on TinyLlama 1.1B. Compiler toolchain support includes GCC 14.2.0 and cmake 3.31.6, and it runs Docker natively. The board was received through the RISC-V DevBoard program and also serves as a self-hosted GitHub Actions runner.

## Key Claims

- Power: Pine64 desktop PSU.
- Supports RISC-V Vector extensions including zvfh (float16 vector operations).
- Achieves ~8.5 tokens/second running TinyLlama 1.1B with llama.cpp (OpenAI-compatible API server).
- Native Docker support with v29.2.1.
- Used for self-hosted CI (GitHub Actions runner).

## Optimization-Relevant Details

- ISA/profile: RISC-V 64GCVB, RVA22.
- Vector/matrix/accelerator support: RVV 1.0 with zvfh, zvfhmin, zve32f, zve32x, zve64d, zve64f, zve64x.
- Memory/cache/TLB/DMA: 16 GB LPDDR4 RAM (14 GB usable), 116 GB eMMC.
- Compiler/toolchain support: GCC 14.2.0, cmake 3.31.6, Docker v29.2.1, Node v22.22.0, Armbian 25.11.2 OS.

## Relationships

- [[spacemit-x60-processor]]: The Banana Pi F3 uses the SpacemiT X60 processor within the K1 SoC.
- [[llvm-risc-v-fptrunc-narrowing-optimization]]: As a RISC-V target, the Banana Pi F3 may benefit from LLVM optimizations for floating-point operations.
- Insufficient context for additional cross-links.

## Sources

- [Running a Local LLM on RISC-V: Building llama.cpp on a Banana Pi F3 (Part 1) - DEV Community](https://dev.to/gounthar/running-a-local-llm-on-risc-v-building-llamacpp-on-a-banana-pi-f3-part-1-4d5g)
merge_draft_body -->

## [2026-07-02] merge_pending | milk-v-pioneer.md
target_page: milk-v-pioneer.md
canonical_name: Milk-V Pioneer
colliding_name: Milk-V Pioneer
source: https://www.cnx-software.com/2023/06/30/64-core-risc-v-motherboard-and-workstation-enables-native-risc-v-development/
status: pending_review
<!-- merge_draft_body
# Milk-V Pioneer

The Milk-V Pioneer is a microATX motherboard and accompanying workstation (Pioneer Box) designed for native RISC-V development, based on the SOPHON SG2042 system-on-chip (SoC) which integrates 64 T-Head C920 RISC-V cores operating at up to 2.0 GHz with support for the RVV 0.71 vector extension. The board provides up to 128 GB of DDR4 ECC memory via four DIMM slots, multiple storage options including M.2 NVMe and SATA III ports, three PCIe x16 expansion slots (wired as PCIe 3.0 x8), dual 2.5GbE networking, and eight USB 3.2 Gen 2 Type-A ports. It supports UEFI boot through OpenSBI mainline, with initial U-Boot porting for OS boot, and engineers are developing EDK2 for UEFI/ACPI support. The Pioneer Box bundles the motherboard with 128 GB RAM, a 1 TB NVMe SSD, an AMD R5 230 graphics card, a dual 10GbE network card, and a 350 W power supply in a slim enclosure. The platform is capable of running various Linux distributions including Fedora, Debian, Ubuntu, and ArchLinux, making it a comprehensive environment for RISC-V software development and testing.

## Key Claims

- The Milk-V Pioneer is a 64-core RISC-V microATX motherboard based on the SOPHON SG2042 SoC with T-Head C920 cores at up to 2.0 GHz.
- Supports up to 128 GB DDR4 ECC memory and multiple storage interfaces.
- Includes three PCIe x16 slots (wired as PCIe 3.0 x8) for expansion.
- Provides dual 2.5GbE and an optional dual 10GbE network card in the Pioneer Box configuration.
- Boot support includes OpenSBI, U-Boot, and ongoing EDK2 UEFI/ACPI development.
- Runs multiple Linux distributions: Fedora, OpenEuler, Debian, Gentoo, Deepin, Ubuntu, ArchLinux.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit with vector extension RVV 0.71 (pre-ratification version).
- Vector/matrix/accelerator support: T-Head C920 cores with 128-bit vector length (as per RVV 0.71 specification). No dedicated matrix accelerator.
- Memory/cache/TLB/DMA: 64 KB I-cache, 64 KB D-cache per core, 1 MB L2 cache per cluster, 64 MB L3 system cache. Memory up to 128 GB DDR4 ECC. No explicit TLB or DMA details provided.
- Compiler/toolchain support: No specific toolchain versions mentioned; however, the platform supports U-Boot and OpenSBI, and runs standard Linux distributions which include GCC and LLVM toolchains.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: unrelated optimization recipe for Gemmini; currently no directly related hardware targets or workloads exist in the wiki to form a strong bridge. (Insufficient context for additional cross-links.)

## Sources

- [64-core RISC-V motherboard and workstation enable native RISC-V development (Crowdfunding) - CNX Software](https://www.cnx-software.com/2023/06/30/64-core-risc-v-motherboard-and-workstation-enables-native-risc-v-development/)
merge_draft_body -->

## [2026-07-02] merge_pending | sophon-sg2042.md
target_page: sophon-sg2042.md
canonical_name: Sophon SG2042
colliding_name: Sophon SG2042
source: https://www.themoonlight.io/en/review/performance-characterisation-of-the-64-core-sg2042-risc-v-cpu-for-hpc
status: pending_review
<!-- merge_draft_body
# Sophon SG2042

The Sophon SG2042 is a 64-core RISC-V central processing unit designed by Sophon Technology, targeting high-performance computing and server-class workloads. It integrates XuanTie C920 cores, which are 64-bit out-of-order superscalar processors implementing the RV64GCV instruction set with the RISC-V Vector Extension v0.7.1, operating on 128-bit vector widths. The chip is one of the highest-core-count RISC-V CPUs available, designed to compete with x86-64 and AArch64 architectures in HPC environments. Performance characterization using the NASA NAS Parallel Benchmarks (NPB) has demonstrated that the SG2042 delivers between 2.6x and 16.7x better single-core performance compared to other RISC-V solutions, while still trailing x86-64 and AArch64 CPUs on certain workloads. The SG2042 is available on the Milk-V Pioneer platform, a developer board with PCIe 2.0 and other peripherals.

## Key Claims

- 64-core RISC-V CPU with XuanTie C920 cores.
- RV64GCV instruction set with RVV v0.7.1 (128-bit vector width).
- Designed for HPC and server workloads.
- Single-core performance improvement of 2.6x to 16.7x over other RISC-V CPUs in NPB.
- Outperforms all other RISC-V solutions in single-core NPB performance.

## Optimization-Relevant Details

- ISA/profile: RV64GCV with RVV v0.7.1.
- Vector/matrix/accelerator support: RVV v0.7.1 (128-bit).
- Memory/cache/TLB/DMA: Not specified in available sources.
- Compiler/toolchain support: Not specified.

## Relationships

- [[xuantie-c950]]: Another high-performance RISC-V CPU from Alibaba's XuanTie family, targeting server-class AI computing.
- [[sifive-intelligence-x160-gen-2]]: A 32-bit RISC-V core from SiFive's 2nd Gen Intelligence family, optimized for edge AI, contrasting with the server-class SG2042.

## Sources

- [Literature Review: Performance characterisation of the 64-core SG2042...](https://www.themoonlight.io/en/review/performance-characterisation-of-the-64-core-sg2042-risc-v-cpu-for-hpc)
- [arXiv:2406.12394](https://arxiv.org/abs/2406.12394)
merge_draft_body -->

## [2026-07-02] merge_pending | sophon-sg2042.md
target_page: sophon-sg2042.md
canonical_name: Sophon SG2042
colliding_name: Sophon SG2042
source: https://arxiv.org/abs/2406.12394
status: pending_review
<!-- merge_draft_body
# Sophon SG2042

The Sophon SG2042 is a 64-core RISC-V CPU designed for high-performance workloads, first released in summer 2023 and becoming widely available by mid-2024. It is the first mass-produced, commodity-available high-core-count RISC-V CPU, employing the T-Head XuanTie C920 cores—each a 64-bit core optimised for high per-core performance—organised in clusters of four and running at a nominal 2 GHz. The CPU aims to bring RISC-V into the high-performance computing (HPC) domain, offering significant parallelism for computationally demanding applications. Preliminary performance characterisation using the NAS Parallel Benchmark (NPB) suite shows that the SG2042 outperforms other RISC-V solutions by a factor of 2.6 to 16.7 at the single-core level, but struggles with memory-bandwidth- and latency-bound algorithms, with the memory subsystem identified as the primary bottleneck. The processor competes with x86-64 and AArch64 CPUs common in production supercomputers, performing comparatively well on compute-intensive workloads while falling short on memory-intensive ones.

## Key Claims

- 64-core RISC-V processor with XuanTie C920 cores running at 2 GHz.
- First mass-produced high-core-count RISC-V CPU for high-performance workloads.
- Delivers a 2.6× to 16.7× single-core performance improvement over other RISC-V CPUs when measured with the NAS Parallel Benchmark suite.
- Performance on computationally bound algorithms is competitive with x86-64 and AArch64 CPUs; memory-bound algorithms show significant relative degradation.
- The memory subsystem (bandwidth and latency) is the greatest performance bottleneck.

## Optimization-Relevant Details

- ISA/profile: RISC-V (64-bit, specific extensions not disclosed in source).
- Vector/matrix/accelerator support: The XuanTie C920 cores include the XTheadVector extension (based on RVV 0.7.1) as noted in other sources, but the paper does not provide details; no dedicated AI accelerator is mentioned.
- Memory/cache/TLB/DMA: Precise cache hierarchy not provided in source; the memory subsystem is noted as a bottleneck.
- Compiler/toolchain support: Not specified in the paper; typical RISC-V toolchains (GCC, LLVM) are expected to be supported.

## Relationships

- [[llvm-riscv-fptrunc-narrowing-optimization]]: As a RISC-V CPU, the SG2042 could benefit from optimisations in the LLVM compiler toolchain, though no direct connection is established in the paper.
- Insufficient context for additional cross-links: only one relevant page exists in the wiki.

## Sources

- [https://arxiv.org/abs/2406.12394](https://arxiv.org/abs/2406.12394)
merge_draft_body -->

## [2026-07-02] merge_pending | sophon-sg2042.md
target_page: sophon-sg2042.md
canonical_name: Sophon SG2042
colliding_name: SG2042
source: https://api.emergentmind.com/papers/2406.12394
status: pending_review
<!-- merge_draft_body
# SG2042

The SOPHON SG2042 is a server-grade RISC-V processor integrating 64 RV64GCV cores, designed for high performance, low power consumption, and high throughput. It is one of the first 64-core RISC-V CPUs publicly characterized. Research using NASA's NAS Parallel Benchmark (NPB) suite compared the SG2042 against other CPUs implementing RISC-V, x86-64, and AArch64 ISAs. In single‑core performance, the SG2042 outperformed all other RISC‑V solutions by a factor of 2.6 to 16.7×. Initial profiling also indicated memory subsystem challenges; the SG2042 was expected to perform best on the BT benchmark and worst on SP. The processor implements the RV64GCV instruction set and employs advanced platform technologies for low‑power server applications.

## Key Claims

- SG2042 integrates 64 RV64GCV RISC-V cores and is positioned as a server‑grade, high‑throughput processor.
- In single‑core NPB benchmarks, the SG2042 surpasses existing RISC‑V hardware by 2.6× to 16.7×.
- Among the NPB suite, the SG2042 is anticipated to achieve best performance on BT (Block Tri-diagonal) and worst on SP (Scalar Penta-diagonal) due to memory bandwidth constraints.

## Relationships

- [[CPA-Factored Gemmini Systolic Array]]: The SG2042 is a RISC-V CPU target for which optimization recipes and benchmarks like the Gemmini systolic array could be evaluated, though no direct experimental results exist in the current wiki.
- Insufficient context for additional cross-links; no other existing entity pages relate to the SG2042 or the Sophon product line.

## Sources

- [Performance characterisation of the 64-core SG2042 RISC-V CPU](https://api.emergentmind.com/papers/2406.12394)
merge_draft_body -->

## [2026-07-02] merge_pending | sophon-sg2042.md
target_page: sophon-sg2042.md
canonical_name: Sophon SG2042
colliding_name: Sophon SG2042
source: https://link.springer.com/content/pdf/10.1007/978-3-031-73716-9_25
status: pending_review
<!-- merge_draft_body
# Sophon SG2042

The Sophon SG2042 is a 64-core RISC-V CPU designed for high performance computing workloads, first mass-produced and commodity-available in summer 2023. It implements the RISC-V ISA and targets HPC applications. The SG2042 has been characterized using the NASA NAS Parallel Benchmark (NPB) suite, where it consistently outperforms other RISC-V solutions by a factor of 2.6 to 16.7 at the single-core level. When compared against x86-64 and AArch64 CPUs common in high performance computing, the SG2042 shows competitive performance on compute-bound algorithms but exhibits relative performance degradation on memory bandwidth or latency-bound algorithms. This performance profile identifies the memory subsystem as the primary bottleneck for this CPU in HPC contexts. The SG2042 represents a milestone as the first high-core-count RISC-V CPU available to the general market for high-performance workloads.

## Key Claims

- The SG2042 delivers between 2.6 and 16.7 times better single-core performance compared to other RISC-V CPUs when running the NAS Parallel Benchmark suite.
- The SG2042 performs competitively with x86-64 and AArch64 CPUs on compute-bound algorithms but suffers on memory bandwidth/latency-bound workloads.
- The memory subsystem is the greatest performance bottleneck of the SG2042.

## Optimization-Relevant Details

- ISA/profile: RISC-V (specific profile not disclosed in source)
- Vector/matrix/accelerator support: Not specified in source
- Memory/cache/TLB/DMA: Memory subsystem identified as bottleneck; no further details
- Compiler/toolchain support: Not specified in source; benchmarks likely compiled with GCC or LLVM

## Relationships

- [[llvm-riscv-fptrunc-narrowing-optimization]]: As a RISC-V CPU, the SG2042 may benefit from LLVM optimizations targeting RISC-V, including the FPTrunc narrowing optimization which improves floating-point division performance on RISC-V cores.
- Insufficient context for additional cross-links to entity pages; only one page available in wiki context.

## Sources

- [Performance Characterisation of the 64-Core SG2042 RISC-V CPU for HPC - Springer](https://link.springer.com/content/pdf/10.1007/978-3-031-73716-9_25)
merge_draft_body -->

## [2026-07-02] merge_pending | sophon-sg2042.md
target_page: sophon-sg2042.md
canonical_name: Sophon SG2042
colliding_name: Sophgo SG2042
source: https://milkv.io/docs/pioneer/resources/gcc
status: pending_review
<!-- merge_draft_body
# Sophgo SG2042

The Sophgo SG2042 is a 64-core RISC-V processor designed for high-performance computing and server applications, featuring T-head C920 cores clocked at up to 2 GHz. Each core includes 64 KB of L1 instruction and data caches, and cores are grouped into clusters of four sharing a 1 MB L2 cache. A 64 MB L3 cache is shared across all cores, and the chip integrates four DDR4-3200 memory controllers supporting up to 128 GB of ECC memory, along with 32 lanes of PCIe Gen4 for high-speed I/O. The SG2042 powers the Milk-V Pioneer developer board, which provides a desktop RISC-V environment with abundant storage and expansion interfaces, including multiple M.2 slots, SATA ports, and USB. It supports the RISC-V 64GC instruction set with T-HEAD vendor extensions (XThead), and the primary toolchain is the T-HEAD GNU Compiler Toolchain, which includes optimizations for these extensions. A prebuilt toolchain is available, and the chip also supports LLVM via the `thead llvm` documentation.

## Key Claims

- 64-core T-head C920 RISC-V CPU operating at up to 2 GHz.
- Memory subsystem: 64 KB L1 I/D per core, 1 MB L2 per quad-core cluster, 64 MB L3 system cache.
- Four DDR4-3200 memory controllers supporting up to 128 GB with ECC.
- 32 lanes of PCIe Gen4 for high-speed peripheral connectivity.
- Supports T-HEAD XThead vendor extensions, including XTheadVector (RVV 0.7 compatible).
- Serves as the SoC for the Milk-V Pioneer developer board.
- Official toolchain: T-HEAD GNU Compiler Toolchain (GCC), with prebuilt binaries and source available.
- Also supports thead LLVM toolchain.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64GC with XThead vendor extensions.
- Vector/matrix/accelerator support: XTheadVector extension (based on RISC-V Vector extension v0.7).
- Memory/cache/TLB/DMA: L1 I/D 64KB each per core, L2 1MB per quad-core cluster, L3 64MB shared.
- Compiler/toolchain support: T-HEAD GCC (primary), thead LLVM.

## Relationships

- [[llvm-risc-v-fptrunc-narrowing-optimization]]: As a RISC-V target, the SG2042 may benefit from LLVM optimizations like the FPTrunc narrowing pass, improving floating-point performance on T-head cores.
- [[spacemit-x60-processor]]: The SpacemiT X60 is another multicore RISC-V processor with AI acceleration; comparing the SG2042's compute and memory architecture to the X60 provides insight into the RISC-V high-performance landscape.

## Sources

- [SG2042 GCC toolchain documentation - Milk-V](https://milkv.io/docs/pioneer/resources/gcc)
- [Milk-V Pioneer Board Documentation - GitHub](https://github.com/sophgocommunity/Pioneer_Doc)
- [SG2042 Newsletter issue 058](https://github.com/sophgocommunity/SG2042-Newsletter/blob/main/newsletters/058.md)
- [Performance characterisation of SG2042 - Research (snippet in resource)]
merge_draft_body -->
