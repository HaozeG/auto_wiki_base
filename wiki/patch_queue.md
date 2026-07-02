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

## [2026-07-02] merge_pending | pulp-platform.md
target_page: pulp-platform.md
canonical_name: PULP Platform
colliding_name: PULP Platform
source: https://www.pulp-platform.org/
status: pending_review
<!-- merge_draft_body
# PULP Platform

PULP (Parallel Ultra Low Power) is an open-source hardware platform developed by ETH Zurich and the University of Bologna for energy-efficient computing. It provides efficient implementations of RISC-V cores including the 32-bit 1-stage Snitch, 32-bit 4-stage CV32E40P, 64-bit 6-stage CVA6, and 32-bit 2-stage Ibex. The platform also offers complete system-on-chip designs such as single-core microcontrollers (PULPissimo, PULPino), multi-core IoT processors (OpenPULP), and multi-cluster heterogeneous accelerators (Hero). All components are released under a permissive SolderPad open-source license, and the platform includes a rich set of peripherals including I2C, SPI, HyperRAM, and GPIO. PULP has been used in multiple tape-outs and is supported by development boards from third-party vendors like open-isa.org (RV32M1-VEGA) and collaborative efforts such as AI Deck.

## Key Claims

- PULP provides efficient implementations of the Snitch, CV32E40P, CVA6, and Ibex RISC-V cores.
- Complete system offerings include PULPissimo, PULPino, OpenPULP, and Hero.
- The platform is released under a permissive SolderPad open-source license.
- Peripherals include I2C, SPI, HyperRAM, and GPIO.
- Development boards are available from open-isa.org (RV32M1-VEGA) and the collaborative AI Deck based on the PULP-shield.
- A recent tape-out (Flamingo) combines the Cheshire platform with Spatz vector units in 22nm.

## Relationships

- [[gemmini]]: Both are open-source hardware platforms for RISC-V-based computing; Gemmini focuses on systolic array acceleration while PULP provides general-purpose energy-efficient cores.
- [[nncase]]: nncase is a compiler stack for RISC-V AI accelerators and could be used to compile neural network models for PULP-based systems.
- Insufficient context for additional cross-links.

## Sources

- [PULP Platform Official Site](https://www.pulp-platform.org/)
merge_draft_body -->

## [2026-07-02] merge_pending | pulp-platform.md
target_page: pulp-platform.md
canonical_name: PULP Platform
colliding_name: PULP
source: https://github.com/pulp-platform/pulp
status: pending_review
<!-- merge_draft_body
# PULP

PULP (Parallel Ultra-Low-Power) is an open-source multi-core computing platform developed through an ongoing collaboration between ETH Zurich and the University of Bologna, initiated in 2013. The platform targets IoT end-node applications that require flexible processing of data streams from sensors such as accelerometers, low-resolution cameras, microphone arrays, and vital signs monitors. PULP consists of an advanced microcontroller architecture that improves upon the earlier PULPino design by including autonomous I/O via a micro-DMA (uDMA), advanced data pre-processing, external interrupt handling, and a tightly-coupled cluster of processors for offloading compute-intensive kernels. The architecture supports either the RI5CY core or the zero-riscy core as the main processor, alongside components such as a new memory subsystem, support for Hardware Processing Engines (HWPEs), a system DMA, and an event unit. The platform is designed to enhance energy efficiency in ultra-low-power signal processing applications and is accompanied by a dedicated RISC-V GNU toolchain for building and simulating the RTL platform.

## Key Claims

- PULP is an open-source multi-core computing platform targeting IoT edge processing applications.
- The architecture includes a choice of RI5CY (4-stage, RV32IMCF, with custom ISA extensions) or zero-riscy (2-stage, RV32IMC/E) as the main core.
- It features an autonomous I/O subsystem via uDMA, reducing core intervention for peripheral communication.
- PULP supports integration of hardware accelerators (HWPEs) that share memory with the main core and are programmed via the memory map.
- The platform supports interfaces including SPI, I2S, CPI, I2C, UART, and JTAG.
- It is developed and maintained by ETH Zurich and the University of Bologna.
- The PULP toolchain is based on a RISC-V GNU toolchain.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: Like PULP, this is an open-source RISC-V-related hardware optimization; PULP's HWPE mechanism could potentially host such accelerators.
- [[earth-shifting-based-vector-memory-access]]: PULP's parallel computing cluster could benefit from vector memory access optimizations, though the EARTH optimization targets a different vector unit.
- Insufficient context for additional cross-links; no existing entity pages in the wiki context.

## Sources

- [pulp-platform/pulp GitHub Repository](https://github.com/pulp-platform/pulp)
merge_draft_body -->

## [2026-07-02] merge_pending | pulp-platform.md
target_page: pulp-platform.md
canonical_name: PULP Platform
colliding_name: PULP Platform
source: https://arxiv.org/html/2412.20391v1
status: pending_review
<!-- merge_draft_body
# PULP Platform

The PULP (Parallel Ultra-Low Power) Platform is an open-source hardware research initiative that began in 2013 and is led by the University of Bologna and ETH Zürich. It provides a portfolio of digital intellectual property (IP) blocks including RISC-V processor cores, network-on-chips, peripherals, SoC templates, and hardware accelerators, all released under open-source licenses. PULP targets low-voltage, low-frequency, highly energy-efficient operation, compensating for performance loss through architectural parallelism and hardware acceleration rather than high-frequency scaling. The central computing block is the PULP cluster, which combines a multi-banked Tightly-Coupled Data Memory (TCDM), a set of RISC-V processors (4–16 cores) with optional ISA extensions for DSP and AI, and one or more Hardware Processing Engines (HWPEs) that share a wide memory port. The Heterogeneous Cluster Interconnect (HCI) arbitrates between core and accelerator accesses. PULP's open-source model aims to reduce non-recurring engineering costs and accelerate development of custom heterogeneous SoCs for AI and edge applications.

## Key Claims

- PULP is an open-source hardware platform started in 2013 by academic institutions (University of Bologna and ETH Zürich).
- The platform includes IP blocks such as RISC-V cores, network-on-chips, peripherals, SoC templates, and HW accelerators.
- PULP clusters are built around a multi-banked TCDM (64–256 KiB, 16–64 banks), 4–16 RISC-V cores, and one or more HWPEs.
- The architecture targets ultra-low-power operation through low-voltage, low-frequency design with parallelism and acceleration.
- The HCI provides arbitration between core and HWPE memory accesses, with a logarithmic crossbar for cores and a wide router for HWPEs.
- AI model parameters are scaling at 2× per year, training FLOPs at 4.2× per year; dedicated hardware performance scales at 1.3× per year (citations from resource).

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: The CPA-factored Gemmini optimization targets a systolic array generator, which could be integrated as an HWPE within a PULP cluster for AI acceleration.
- [[earth-shifting-based-vector-memory-access]]: The EARTH optimization addresses RISC-V vector memory access, relevant to PULP clusters that use RISC-V cores with vector extensions.
- Insufficient context for additional cross-links; existing wiki pages are limited to optimization recipes rather than entity pages.

## Sources

- [Open-Source Design of Heterogeneous SoCs for AI Acceleration: the PULP Platform Experience](https://arxiv.org/html/2412.20391v1)
merge_draft_body -->

## [2026-07-02] merge_pending | d1-h.md
target_page: d1-h.md
canonical_name: D1-H
colliding_name: Allwinner D1
source: https://linux-sunxi.org/D1
status: pending_review
<!-- merge_draft_body
# Allwinner D1

The Allwinner D1 (also known as D1-H, codename sun20iw1p1) is a system-on-chip (SoC) manufactured by Allwinner Technology. It is the first Allwinner SoC based on a RISC-V core, featuring a single XuanTie C906 core from T-Head Semiconductor (a subsidiary of Alibaba) supporting the RV64IMAFDCVU extensions (RV64GCV with vector extension). The SoC is fabricated on a 22nm process and supports up to 2 GB of DDR2 or DDR3 memory. It includes a video processing unit (VPU) capable of decoding 4K video at 30 FPS (H.265/H.264/MPEG/JPEG/VC1/MJPEG) and encoding 1080p at 60 FPS (JPEG/MJPEG). Additional features include a Tensilica HiFi4 DSP running at 600 MHz, a G2D graphics accelerator, a display engine (DE2.0), and various connectivity options such as HDMI, MIPI, LVDS, LCD, CVBS, 10/100/1000M Ethernet MAC, SDIO 3.0, eMMC 5.0, SPI NOR/NAND Flash, USB 2.0 OTG and Host, and multiple I2C, SPI, UART, PWM, IR, and ADC interfaces.

## Key Claims

- First Allwinner SoC based on a RISC-V core.
- Single XuanTie C906 core with RV64IMAFDCVU (RV64GCV including vector extension).
- Fabricated on 22nm process.
- VPU supports 4K decode at 30 FPS for H.265/H.264/MPEG/JPEG/VC1/MJPEG and 1080p encode at 60 FPS for JPEG/MJPEG.
- Includes Tensilica HiFi4 DSP operating at 600 MHz.
- Memory: DDR2/DDR3 up to 2 GB.
- Connectivity includes HDMI, MIPI, LVDS, LCD, CVBS, 10/100/1000M EMAC, SDIO 3.0, eMMC 5.0, SPI NOR/NAND Flash, USB 2.0 OTG and Host.
- Released in April 2021.
- Cooperation announced between Allwinner and T-Head (PingTou) in August 2020.

## Optimization-Relevant Details

- ISA/profile: RV64IMAFDCVU (RV64GCV including vector extension).
- Vector/matrix/accelerator support: The XuanTie C906 core includes the V vector extension (RVV 0.7.1-based XTheadVector). No dedicated matrix accelerator; DSP (HiFi4) for audio/signal processing.
- Memory/cache/TLB/DMA: Not detailed in source.
- Compiler/toolchain support: RISC-V GCC/LLVM toolchains; Allwinner SDK available.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: Both are hardware targets in the RISC-V ecosystem; the D1 provides a general-purpose RISC-V platform that could benefit from systolic array optimizations for AI workloads.
- [[earth-shifting-based-vector-memory-access]]: The D1's XuanTie C906 core includes vector extensions, making EARTH's vector memory access optimization relevant for improving performance on vectorized workloads on this hardware.
- Insufficient context for additional cross-links; no existing entity pages for T-Head C906 or similar SoCs are present in current wiki context.

## Sources

- [linux-sunxi.org D1 page](https://linux-sunxi.org/D1)
- CNX Software article referenced in source
- Allwinner press release
merge_draft_body -->

## [2026-07-02] merge_pending | rockchip-rk3588.md
target_page: rockchip-rk3588.md
canonical_name: Rockchip RK3588
colliding_name: Rockchip RK3588
source: https://ieeker.com/rk3588-npu-performance-industrial-edge-ai/
status: pending_review
<!-- merge_draft_body
# Rockchip RK3588

The Rockchip RK3588 is an ARM-based System-on-Chip (SoC) designed for edge AI applications, integrating a dedicated 6 TOPS Neural Processing Unit (NPU) alongside quad-core Cortex-A76 and quad-core Cortex-A55 CPU cores. The NPU supports real-time inference workloads, achieving over 54 frames per second on YOLOv5 object detection. The SoC is positioned as a cost-effective platform for industrial edge AI, leveraging the RKNN-Toolkit2 toolchain for model quantization and deployment. The 6 TOPS performance level is described as a "sweet spot" balancing throughput, power efficiency, and system cost for vision-heavy industrial applications.

## Key Claims

- The RK3588 NPU delivers 6 TOPS of integer performance.
- YOLOv5 inference achieves over 54 FPS on the NPU using RKNN-Toolkit2 quantization.
- The NPU is integrated with Cortex-A76/A55 CPU cores in a single SoC.
- The platform targets industrial edge AI applications, emphasizing power efficiency and I/O completeness.
- RKNN-Toolkit2 provides quantization tips to optimize model deployment.

## Optimization-Relevant Details

- ISA/profile: ARMv8.2-A (64-bit)
- Vector/matrix/accelerator support: Dedicated 6 TOPS NPU (neural processing unit), no explicit vector extensions on CPU.
- Memory/cache/TLB/DMA: Not specified in sources; typical for SoC with DDR4/LPDDR4 memory interface.
- Compiler/toolchain support: RKNN-Toolkit2 (Rockchip Neural Network Toolkit) for model conversion and quantization.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: While targeting different architectures (ARM vs RISC-V), both are optimization recipes for AI accelerators; the RK3588 NPU may benefit from similar systolic array optimizations in future designs.
- [[earth-shifting-based-vector-memory-access]]: This RISC-V vector memory optimization contrasts with the RK3588's fixed-function NPU approach; comparing the two highlights trade-offs between programmability and efficiency.
- Insufficient context for additional cross-links; no existing hardware target pages for ARM-based SoCs are currently in the wiki.

## Sources

- [Search snippets for: RK3588 NPU Performance: What 6 TOPS Means for Industrial AI ...](https://ieeker.com/rk3588-npu-performance-industrial-edge-ai/)
- [Rockchip RK3588 NPU Deep Dive: Real-World AI Performance ...](https://example.com) (snippet from search results)
- [RK3588 NPU: Edge AI Performance in 2026 - accio.com](https://accio.com) (snippet)
merge_draft_body -->

## [2026-07-02] merge_pending | rockchip-rk3588.md
target_page: rockchip-rk3588.md
canonical_name: Rockchip RK3588
colliding_name: RK3588
source: https://github.com/choushunn/awesome-RK3588
status: pending_review
<!-- merge_draft_body
# RK3588

RK3588 is Rockchip's flagship 8K SoC integrating a quad-core Cortex-A76 cluster and a quad-core Cortex-A55 cluster in a big.LITTLE configuration, along with a 6 TOPS neural processing unit. It supports 8K video encode and decode, multiple display outputs, and a range of peripherals. The SoC targets edge AI, multimedia, and embedded computing applications. It has an associated software stack including RKNN for NPU programming and RKLLM for edge LLM deployment. Development boards such as the iTOP-RK3588 provide a hardware platform for evaluation. A curated list of development resources is maintained in the awesome-RK3588 repository.

## Key Claims

- Integrates quad Cortex-A76 and quad Cortex-A55 cores.
- Features a 6 TOPS NPU for AI acceleration.
- Supports 8K video encode/decode.
- Targets edge AI, multimedia, and embedded applications.
- Software support includes RKNN and RKLLM.

## Optimization-Relevant Details

- ISA/profile: ARMv8.2-A (A76, A55).
- Vector/matrix/accelerator support: 6 TOPS NPU, NEON coprocessor.
- Memory/cache/TLB/DMA: Not specified in resource.
- Compiler/toolchain support: RKNN, RKLLM.

## Relationships

- [[gemmini]]: Both target AI acceleration, though Gemmini is a systolic array generator for RISC-V.
- [[nncase]]: Both are related to neural network compiler tools, though nncase targets RISC-V accelerators.
- Insufficient context for additional cross-links; no existing entity pages for Rockchip SoCs or ARM-based AI accelerators in the wiki.

## Sources

- [GitHub - choushunn/awesome-RK3588](https://github.com/choushunn/awesome-RK3588)
merge_draft_body -->

## [2026-07-02] merge_pending | opengeem-accelerator-generator.md
target_page: opengeem-accelerator-generator.md
canonical_name: OpenGeMM
colliding_name: OpenGeMM
source: https://hub.baai.ac.cn/paper/7fd2589c-86b3-40ee-a921-83653897137e
status: pending_review
<!-- merge_draft_body
# OpenGeMM

OpenGeMM is an open-source accelerator generator for general matrix multiplication (GeMM) designed for high hardware utilization and tight integration with a lightweight RISC-V control processor. It consists of a parameterizable GeMM accelerator written in Chisel, a lightweight RISC-V core, and a tightly coupled multi-bank scratchpad memory. To maximize utilization and system efficiency, OpenGeMM employs three key mechanisms: configuration preload, input prefetch with output buffering, and programmable stride memory access. The generator targets edge devices where computational and data-intensive deep neural networks (DNNs) must be deployed with both flexibility and efficiency. Experimental results reported by Yi et al. (2024) show that OpenGeMM achieves hardware utilization between 81.89% and 99.34% across various CNN and Transformer workloads, and delivers 3.58x to 16.40x normalized throughput improvement over the state-of-the-art open-source Gemmini accelerator, with a system efficiency of 4.68 TOPS/W.

## Key Claims

- OpenGeMM is an open-source, parameterizable GeMM accelerator generator integrating a Chisel-based accelerator, a lightweight RISC-V processor, and tightly coupled multi-bank scratchpad memory.
- Three optimization mechanisms—configuration preload, input prefetch & output buffering, and programmable stride memory access—improve hardware utilization and system efficiency.
- Across diverse CNN and Transformer workloads, OpenGeMM achieves hardware utilization ranging from 81.89% to 99.34%.
- Compared to the Gemmini accelerator, OpenGeMM achieves 3.58x to 16.40x improvement in normalized throughput.
- System efficiency reaches 4.68 TOPS/W.

## Relationships

- [[earth-shifting-based-vector-memory-access]]: Both OpenGeMM and EARTH target RISC-V-based hardware acceleration for efficient data movement, with EARTH focusing on vector memory access and OpenGeMM on GeMM accelerator generation.
- [[pulp-nn-optimization-recipe]]: PULP-NN provides software-level optimization for quantized neural networks on RISC-V clusters; OpenGeMM offers a complementary hardware generation approach for GeMM acceleration on edge devices.
- [[Gemmini]]: OpenGeMM is directly compared against the Gemmini accelerator and claims significant throughput improvements.

## Sources

- OpenGeMM paper on BAAI hub: https://hub.baai.ac.cn/paper/7fd2589c-86b3-40ee-a921-83653897137e
merge_draft_body -->

## [2026-07-02] merge_pending | opengeem-accelerator-generator.md
target_page: opengeem-accelerator-generator.md
canonical_name: OpenGeMM
colliding_name: OpenGeMM
source: https://www.researchgate.net/publication/385823001_OpenGeMM_A_High-Utilization_GeMM_Accelerator_Generator_with_Lightweight_RISC-V_Control_and_Tight_Memory_Coupling
status: pending_review
<!-- merge_draft_body
# OpenGeMM

OpenGeMM is an open-source acceleration platform for general matrix-matrix multiplication (GeMM) targeting resource-constrained extreme edge devices. It integrates a parameterized Chisel-coded GeMM accelerator, a lightweight RISC-V processor for control and programmability, and a tightly coupled multi-banked scratchpad memory system. The platform employs three mechanisms to boost hardware utilization and system efficiency: configuration pre-loading, which reduces setup overhead; input pre-fetching with output buffering, which minimizes data movement stalls; and programmable strided memory access, which enables flexible data layout handling. These mechanisms collectively allow OpenGeMM to achieve consistently high hardware utilization ranging from 81.89% to 99.34% across diverse CNN and Transformer workloads. In comparisons with the state-of-the-art open-source Gemmini accelerator, OpenGeMM demonstrates a 3.58x to 16.40x speedup on normalized throughput (GOPS/µm²) and delivers 4.68 TOPS/W system efficiency. The platform is designed to balance reusability, flexibility, and ease of configuration, providing a programmable alternative to fixed-function accelerators.

## Key Claims

- OpenGeMM is an open-source acceleration platform for GeMM with a parameterized Chisel-coded accelerator core.
- Integrates a lightweight RISC-V processor for flexible control without sacrificing efficiency.
- Employs tightly coupled multi-banked scratchpad memory for low-latency data access.
- Achieves hardware utilization of 81.89% to 99.34% across diverse CNN and Transformer workloads through three mechanisms: configuration pre-loading, input pre-fetching with output buffering, and programmable strided memory access.
- Demonstrates 3.58x to 16.40x speedup on normalized throughput compared to the Gemmini accelerator in both output-stationary and weight-stationary modes.
- Achieves 4.68 TOPS/W system efficiency.
- Designed for extreme edge devices with limited resources.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: Both involve optimization of GeMM-related hardware, with OpenGeMM as a full platform and CPA factoring targeting Gemmini's systolic array.
- [[earth-shifting-based-vector-memory-access]]: Both platforms explore memory access optimizations for RISC-V based accelerators, with OpenGeMM focusing on GeMM-specific prefetching and strided access.
- [[pulp-nn-optimization-recipe]]: Both target efficient neural network inference on RISC-V platforms; PULP-NN at the software kernel level and OpenGeMM at the hardware accelerator level.

## Sources

- [OpenGeMM: A High-Utilization GeMM Accelerator Generator with Lightweight RISC-V Control and Tight Memory Coupling](https://arxiv.org/abs/2411.09543) (arXiv preprint, November 2024)
- [ResearchGate entry for the same preprint](https://www.researchgate.net/publication/385823001_OpenGeMM_A_High-Utilization_GeMM_Accelerator_Generator_with_Lightweight_RISC-V_Control_and_Tight_Memory_Coupling)
merge_draft_body -->

## [2026-07-02] merge_pending | llvm-riscv-target.md
target_page: llvm-riscv-target.md
canonical_name: LLVM RISC-V Target
colliding_name: LLVM RISC-V Vector Extension
source: https://github.com/llvm/llvm-project/blob/main/llvm/docs/RISCV/RISCVVectorExtension.rst
status: pending_review
<!-- merge_draft_body
# LLVM RISC-V Vector Extension

The LLVM RISC-V Vector Extension (RVV) implementation models the version 1.0 of the ratified RISC-V Vector Extension specification in the LLVM compiler infrastructure. It maps RVV's 32 vector registers (of parameterized size VLEN) to LLVM's scalable vector types (`<vscale x n x ty>`), where the scaling factor `vscale` is defined as VLEN/64 (requiring VLEN ≥ 64). Each combination of SEW (Standard Element Width) and LMUL (Length Multiplier) maps to a specific scalable vector type: for example, SEW=64 and LMUL=1 corresponds to `<vscale x 1 x i64>`, while SEW=8 and LMUL=8 maps to `<vscale x 64 x i8>`. The implementation supports ELEN=32 or ELEN=64 and provides both regular LLVM IR instructions on vector types and RVV-specific intrinsics that mirror the C intrinsics specification, including unmasked and masked variants with passthru, AVL, and policy operands. This design enables LLVM to target any RVV 1.0 hardware with a single compiler, relying on scalable vector code generation to adapt to runtime VLEN.

## Key Claims

- LLVM models RVV 1.0 registers using scalable vector types `<vscale x n x ty>`, where `vscale = VLEN/64` and `n`/`ty` control LMUL and SEW respectively.
- Only ELEN=32 or ELEN=64 are supported; VLEN=32 is not supported.
- Two types with the same SEW/LMUL ratio produce the same mask vector type (e.g., SEW=64/LMUL=2 and SEW=32/LMUL=1 both yield `<vscale x 2 x i1>`).
- Mask vectors use densely packed bits and are mapped to types `<vscale x k x i1>` for k=1,2,4,8,16,32,64.
- RVV instructions can be represented as regular LLVM IR instructions (e.g., `add <vscale x 4 x i32>`) or as RVV intrinsics (e.g., `@llvm.riscv.vadd.nxv4i32.nxv4i32`).
- Intrinsics accept passthru operands for inactive/tail elements, AVL, and policy bits; masked variants add mask and vta/vma operands.
- The only valid types for RVV intrinsics are scalable vector types.

## Relationships

- [[llvm-riscv-fptrunc-narrowing-optimization]]: This optimization recipe targets RISC-V LLVM code generation and relies on the RVV extension modeling described in this page for its floating-point division improvements.
- [[tvm-metaschedule-rvv-integration]]: The TVM MetaSchedule integration uses LLVM as a backend toolchain; the LLVM RVV implementation provides the vector extension support that enables the reported performance improvements.
- Insufficient context for additional cross-links to entity pages; only two optimization recipe pages are available in the wiki context.

## Sources

- [RISC-V Vector Extension - LLVM Documentation](https://github.com/llvm/llvm-project/blob/main/llvm/docs/RISCV/RISCVVectorExtension.rst)
merge_draft_body -->

## [2026-07-02] pending | andes-ax45mpv.md
target_page: andes-ax45mpv.md
target_section: Key Claims
source: https://www.andestech.com/en/products-solutions/andescore-processors/riscv-ax45mpv/
status: pending_review
proposed_update: Add the following claims sourced from the Andes official page and press releases: Supports MMU for Linux-based applications; features dynamic branch prediction for efficient branch execution; dual-issue of common instruction pairs; level-1 instruction/data caches and local memories for low-latency accesses; demonstrated booting a lightweight LLM on an S2C Prodigy S8-100 FPGA with AMD Versal VP1902; collaboration with MachineWare for early RISC-V software simulation; general availability announced; licensed by Rain AI for in-memory computing solutions.

## [2026-07-02] merge_pending | ventana-veyron-v2.md
target_page: ventana-veyron-v2.md
canonical_name: Ventana Veyron V2
colliding_name: Veyron V2
source: https://linuxgizmos.com/ventana-to-launch-veyron-v2-risc-v-platform-for-hpc-in-2025/
status: pending_review
<!-- merge_draft_body
# Ventana Veyron V2

Ventana Veyron V2 is a high-performance RISC-V accelerated compute platform announced by Ventana Micro Systems in October 2024, targeting AI, data center, HPC, automotive, and edge computing workloads. The platform features a fifteen-wide out-of-order pipeline operating at 3.6GHz, built on a 4nm process technology. Each cluster supports 32 cores with scalability to 192 cores across multiple clusters, and includes 128MB of shared L3 cache per cluster. A 512-bit vector unit and AI matrix extensions enhance AI and machine learning workloads. The Veyron V2 also provides server-class IOMMU, Advanced Interrupt Architecture, comprehensive RAS features, and side channel attack mitigations for secure enterprise deployments.

## Key Claims

- Features a 15-wide out-of-order pipeline with 3.6GHz clock speed, built on 4nm process.
- Supports 32 cores per cluster, scalable to 192 cores across clusters.
- Includes 128MB shared L3 cache per cluster to reduce latency.
- Integrates a 512-bit vector unit for data-intensive operations.
- Incorporates AI matrix extensions for AI and machine learning acceleration.
- Provides server-class IOMMU, Advanced Interrupt Architecture, RAS features, and side channel attack mitigations.
- Designed for AI, data center, automotive, edge computing, and HPC workloads.

## Optimization-Relevant Details

- ISA/profile: RISC-V (implied by the context, no specific profile stated).
- Vector/matrix/accelerator support: 512-bit vector unit, AI matrix extensions.
- Memory/cache/TLB/DMA: 128MB shared L3 cache per cluster; no DMA details provided.
- Compiler/toolchain support: Not specified in the source.

## Relationships

- [[earth-shifting-based-vector-memory-access]]: Veyron V2's vector unit could benefit from optimized vector memory access techniques described in this recipe.
- [[llvm-riscv-fptrunc-narrowing-optimization]]: Compiler optimizations targeting RISC-V floating-point performance are relevant to the Veyron V2 platform.

## Sources

- [Ventana to Launch Veyron V2 RISC-V Platform for HPC in 2025](https://linuxgizmos.com/ventana-to-launch-veyron-v2-risc-v-platform-for-hpc-in-2025/)
merge_draft_body -->

## [2026-07-02] merge_pending | ventana-veyron-v2.md
target_page: ventana-veyron-v2.md
canonical_name: Ventana Veyron V2
colliding_name: Veyron V2
source: https://www.nextplatform.com/2023/11/07/ventana-launches-veyron-v2-risc-v-into-the-datacenter/
status: pending_review
<!-- merge_draft_body
# Veyron V2

The Veyron V2 is a RISC-V server processor designed by Ventana Micro Systems, announced in November 2023 as a successor to the Veyron V1. It targets datacenter workloads and incorporates the RISC-V Vector Extension 1.0 with 512-bit vector support, along with significant core architectural improvements. A key design change from the V1 is the adoption of the Universal Chiplet Interconnect Express (UCI-Express) standard for die-to-die chiplet linking, replacing the earlier Bunch of Wires (BoW) interconnect. This switch, driven by hyperscaler and cloud builder preferences, enables higher data rates, better power efficiency, and improved bandwidth per millimeter. The chip is intended to compete with X86 and Arm server processors in the datacenter space.

## Key Claims

- UCI-Express provides 2× the data rate of BoW, 2× better power efficiency, less than half the latency, and 35–65% higher bandwidth per millimeter compared to BoW, based on a paper by Lei Shan.
- Veyron V2 features the ratified RISC-V Vector Extension 1.0 with 512-bit vectors, akin to Intel's AVX-512.
- The chip uses UCI-Express chiplet interconnect instead of the earlier BoW standard, influenced by customer demand and industry momentum.
- Veyron V1 was competitive with X86 and Arm server chips of its time, and Veyron V2 introduces substantial core enhancements.
- The design shift to UCI-Express was accelerated to align with the new round of X86 and Arm server chips and to provide a standard chiplet interface.

## Optimization-Relevant Details

- ISA/profile: RISC-V with Vector Extension 1.0 (ratified), 512-bit vector length.
- Vector/matrix/accelerator support: RVV 1.0 512-bit vectors, no specific matrix accelerator details.
- Memory/cache/TLB/DMA: Not detailed in source; chiplet architecture suggests scalable memory via UCI-Express.
- Compiler/toolchain support: Standard RISC-V toolchain (GCC, LLVM) with vector support.
- Chiplet interconnect: UCI-Express (die-to-die), replacing BoW. Provides 2× data rate, 2× power efficiency, <0.5× latency, and 35–65% higher bandwidth density.

## Relationships

- [[earth-shifting-based-vector-memory-access]]: The EARTH optimization targets RISC-V vector memory access, potentially benefiting Veyron V2's vector unit performance.
- [[llvm-riscv-fptrunc-narrowing-optimization]]: This compiler optimization improves RISC-V floating-point division performance on SiFive P550 and may be applicable to Veyron V2 for datacenter workloads.
- [[cpa-factored-gemmini-systolic-array]]: As a RISC-V accelerator design technique, this optimization may complement Veyron V2's vector capabilities in AI inference.

## Sources

- [Ventana Launches Veyron V2 RISC-V Into The Datacenter](https://www.nextplatform.com/2023/11/07/ventana-launches-veyron-v2-risc-v-into-the-datacenter/)
merge_draft_body -->

## [2026-07-02] merge_pending | ventana-veyron-v2.md
target_page: ventana-veyron-v2.md
canonical_name: Ventana Veyron V2
colliding_name: Ventana Veyron V2
source: https://www.storagereview.com/news/ventana-veyron-v2-risc-v-processor-announced
status: pending_review
<!-- merge_draft_body
# Ventana Veyron V2

The Ventana Veyron V2 is a high-performance RISC-V processor designed by Ventana Micro Systems, fabricated on a 4nm process and operating at up to 3.6 GHz. It features a 15-wide out-of-order pipeline, supports scalable multi-core configurations of up to 192 cores, and includes a 512-bit vector unit with AI matrix extensions. The processor integrates 128 MB of shared L3 cache per cluster, an I/O memory management unit (IOMMU), Advanced Interrupt Architecture, hardware side-channel attack defenses, and comprehensive RAS capabilities. It employs a UCIe chiplet interconnect, allowing customization of compute, I/O, and memory. Ventana also provides a Software Development Kit (SDK) validated on its RISC-V platform. The Veyron V2 targets server-class performance for data center, automotive, 5G, AI, and client applications.

## Key Claims

- Up to 40% performance improvement over previous generation (microarchitecture improvements, processor fabric, cache hierarchy, vector processor).
- 15-wide out-of-order pipeline at 3.6 GHz.
- 4nm process technology.
- Scalable to 192 cores.
- 128 MB shared L3 cache per cluster.
- 512-bit vector unit with AI matrix extensions.
- Supports IOMMU, Advanced Interrupt Architecture, side-channel attack defenses, and RAS.
- UCIe chiplet interconnect reduces development time and costs.
- Available as chiplets and IP.

## Optimization-Relevant Details

- ISA/profile: RISC-V (unspecified profile, likely RVA22 or later given server features).
- Vector/matrix/accelerator support: 512-bit vector unit, AI matrix extensions (specific instruction set not detailed).
- Memory/cache/TLB/DMA: 128 MB shared L3 per cluster, IOMMU for I/O virtualization.
- Compiler/toolchain support: Ventana SDK, validated on Ventana platform.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: This optimization recipe targets systolic array designs for RISC-V accelerators, relevant to the Veyron V2's AI matrix extensions.
- [[earth-shifting-based-vector-memory-access]]: This optimization improves vector memory access for RISC-V vector units, relevant to the Veyron V2's 512-bit vector unit.
- Insufficient context for additional cross-links; no other entity pages for RISC-V processor families are present in the wiki.

## Sources

- [Ventana Veyron V2 RISC-V Processor Announced - StorageReview.com](https://www.storagereview.com/news/ventana-veyron-v2-risc-v-processor-announced)
merge_draft_body -->

## [2026-07-02] merge_pending | llvm-riscv-target.md
target_page: llvm-riscv-target.md
canonical_name: LLVM RISC-V Target
colliding_name: LLVM
source: https://llvm.org/
status: pending_review
<!-- merge_draft_body
# LLVM

LLVM is a collection of modular and reusable compiler and toolchain technologies that originated as a research project at the University of Illinois. Despite its name, LLVM is not a traditional virtual machine; the name "LLVM" is the full name of the project rather than an acronym. LLVM began with the goal of providing a modern, SSA-based compilation strategy capable of supporting both static and dynamic compilation of arbitrary programming languages, and has since grown into an umbrella project comprising numerous subprojects. The LLVM Core libraries provide a source- and target-independent optimizer built around the LLVM intermediate representation (LLVM IR), along with code generation support for many CPUs. LLVM is widely used in commercial and open-source projects, as well as in academic research, and its code is licensed under the Apache 2.0 License with LLVM exceptions. Within the RISC-V AI accelerator ecosystem, LLVM serves as a critical toolchain component for compiling high-level code into optimized machine code for RISC-V targets, including vector extensions (RVV) and specialized accelerators.

## Key Claims

- LLVM provides a modern SSA-based compilation strategy supporting static and dynamic compilation of arbitrary languages.
- The LLVM Core libraries include a source- and target-independent optimizer and code generation for many popular CPUs.
- Code in the LLVM project is licensed under the Apache 2.0 License with LLVM exceptions.
- Primary subprojects include: LLVM Core, Clang (C/C++/Obj-C), Flang (Fortran), LLDB (debugger), libc++/libc++ ABI, libc (C standard library), compiler-rt (low-level code generation support), MLIR (multi-level IR), OpenMP runtime, Polly (polyhedral optimizations), libclc (OpenCL), klee (symbolic execution), LLD (linker), and BOLT (post-link optimizer).
- LLVM supports code generation for RISC-V CPUs, including RVV (RISC-V Vector Extension).
- The project releases multiple versions per year; the latest release as of June 2026 is LLVM 22.1.8.

## Relationships

- [[llvm-riscv-fptrunc-narrowing-optimization]]: An optimization recipe that details an LLVM transformation improving code generation for RISC-V targets, leveraging LLVM's range analysis to reduce floating-point division latency.
- [[mlir-xdsl-rvv-lowering-pipeline]]: An optimization recipe that uses MLIR (a subproject of LLVM) combined with xDSL to enable RVV code generation for RISC-V platforms.
- [[vectrans]]: An optimization recipe that enhances compiler auto-vectorization using LLM assistance, targeting compilers including LLVM/Clang, relevant to improving LLVM's vectorization on RISC-V.
- Insufficient context for additional cross-links to entity pages; only optimization recipes are available in the current wiki context.

## Sources

- [The LLVM Compiler Infrastructure Project](https://llvm.org/)
merge_draft_body -->

## [2026-07-02] merge_pending | risc-v.md
target_page: risc-v.md
canonical_name: RISC-V
colliding_name: RISC-V
source: https://en.wikipedia.org/wiki/RISC-V
status: pending_review
<!-- merge_draft_body
# RISC-V

RISC-V (pronounced "risk-five") is a free and open standard instruction set architecture (ISA) based on reduced instruction set computer (RISC) principles. It was developed in 2010 at the University of California, Berkeley as the fifth generation of RISC processors from that institution, with foundational work by Krste Asanović and David Patterson. Unlike proprietary ISAs such as x86 and ARM, RISC-V is released under permissive open-source licenses, enabling royalty-free implementations. The specification defines base integer ISAs for 32-bit (RV32I), 64-bit (RV64I), and 128-bit (RV128I) address spaces, along with a suite of standard extensions: M (multiplication and division), A (atomic instructions), F/D/Q (single, double, and quad-precision floating-point), C (compressed 16-bit instructions), B (bit manipulation), V (vector operations), and various Z extensions for control and status registers, fences, and more. The ISA uses variable-length encoding, little-endian byte ordering, and a load-store architecture. Maintenance and governance of the standard were transferred to RISC-V International, a Swiss non-profit, in 2015. As of 2025, RISC-V International has over 4,500 members, and RISC-V has become widely adopted in microcontrollers and embedded systems, with commercial SoCs from companies such as SiFive, Andes Technology, StarFive, Espressif Systems, and SpacemiT.

## Key Claims

- RISC-V is a free and open standard ISA based on RISC principles, allowing royalty-free implementations.
- Developed at UC Berkeley in 2010 as the fifth generation of Berkeley RISC designs.
- Managed by RISC-V International since 2015, a non-profit with over 4,500 members.
- Supports 32-bit, 64-bit, and 128-bit address spaces (RV32I, RV64I, RV128I).
- Standard extensions include M (multiply/divide), A (atomics), F/D/Q (floating-point), C (compressed), B (bit manipulation), V (vector), and Z-series extensions.
- Used in microcontrollers, embedded systems, and growing into mobile, desktop, and server markets.
- Major implementors include SiFive, Andes Technology, StarFive, Espressif Systems, and SpacemiT.

## Relationships

- [[spacemit-x60-processor]]: A RISC-V processor designed for AI acceleration, based on the RISC-V ISA and used in platforms such as Bit-Brick K1.
- [[vectrans]]: An LLM-assisted compiler auto-vectorization framework that targets RISC-V and other architectures for improved code generation.
- [[llvm-riscv-fptrunc-narrowing-optimization]]: A compiler optimization specifically for RISC-V targets that reduces floating-point division latency via range analysis.
- Insufficient context for additional entity page cross-links; no entity pages are available in the provided wiki context.

## Sources

- [RISC-V - Wikipedia](https://en.wikipedia.org/wiki/RISC-V)
merge_draft_body -->

## [2026-07-02] pending | pulp-nn-optimization-recipe.md
target_page: pulp-nn-optimization-recipe.md
target_section: Measurements (under Transformation)
source: https://arxiv.org/abs/2011.14325
status: pending_review
proposed_update: Add the specific measured speedups from the XpulpNN paper: 6x for 4-bit operands, 8x for 2-bit operands, and peak efficiency 2.22 TOPs/s/W from a parallel cluster in GF22FDX. Reference the XpulpNN paper as a source for these hardware-level benchmarks. Also add XpulpNN as an explicit related ISA extension in the constraints list.

## [2026-07-02] pending | cutie-ternary-accelerator.md
target_page: cutie-ternary-accelerator.md
target_section: Key Claims
source: https://arxiv.org/abs/2011.01713
status: pending_review
proposed_update: From arXiv:2011.01713 (primary CUTIE paper), add the following claims: CUTIE achieves 3.1 POp/s/W (3100 TOp/s/W) energy efficiency, reduces core inference energy cost by a factor of 4.8x to 21x compared to state-of-the-art accelerators, and uses an architecture with completely unrolled data path in feature map and filter dimensions, ternary neural network targeting, and an optimized training method for higher weight sparsity.

## [2026-07-02] pending | cutie-ternary-accelerator.md
target_page: cutie-ternary-accelerator.md
target_section: frontmatter
source: https://www.researchgate.net/publication/345261170_CUTIE_Beyond_PetaOpsW_Ternary_DNN_Inference_Acceleration_with_Better-than-Binary_Energy_Efficiency
status: pending_review
proposed_update: Add new alias 'CUTIE (Completely Unrolled Ternary Inference Engine)' to frontmatter aliases list.

## [2026-07-02] pending | cutie-ternary-accelerator.md
target_page: cutie-ternary-accelerator.md
target_section: content
source: https://www.researchgate.net/publication/345261170_CUTIE_Beyond_PetaOpsW_Ternary_DNN_Inference_Acceleration_with_Better-than-Binary_Energy_Efficiency
status: pending_review
proposed_update: Replace the first paragraph with an expanded introduction: 'CUTIE (Completely Unrolled Ternary Inference Engine) is an all-digital ternary neural network accelerator fabricated in GF 22 nm FDX (FDSOI) technology. It achieves 3.1 POp/s/W energy efficiency by minimizing non-computational energy through a completely unrolled datapath architecture in feature map and filter dimensions, reducing switching activity via silencing and maximizing data reuse. CUTIE targets ternary neural networks (TNNs) where sparse weights further reduce switching activity, and introduces an optimized training method to increase weight sparsity. Compared with state-of-the-art accelerators, CUTIE achieves equal or greater accuracy while reducing core inference energy by 4.8x–21x. The design supports fully ternarized Temporal Convolutional Networks (TCNs) and is reported to achieve 3.1 POp/s/W, 2.72 µJ per inference at 12.2 mW, and post-synthesis simulation shows 1.7 µJ per frame for DVS gesture recognition.'

## [2026-07-02] pending | cutie-ternary-accelerator.md
target_page: cutie-ternary-accelerator.md
target_section: Key Claims
source: https://www.researchgate.net/publication/345261170_CUTIE_Beyond_PetaOpsW_Ternary_DNN_Inference_Acceleration_with_Better-than-Binary_Energy_Efficiency
status: pending_review
proposed_update: Add new claims: 'Achieves 3.1 POp/s/W energy efficiency (3100 TOp/s/W) [source]. Reduces core inference energy by 4.8x–21x compared to state-of-the-art accelerators [source]. Introduces an optimized training method to increase weight sparsity and further reduce switching activity [source].' Keep existing claims but note measurement context differences (the 1,036 TOp/s/W figure may be for a different configuration).

## [2026-07-02] pending | cutie-ternary-accelerator.md
target_page: cutie-ternary-accelerator.md
target_section: Optimization-Relevant Details
source: https://www.researchgate.net/publication/345261170_CUTIE_Beyond_PetaOpsW_Ternary_DNN_Inference_Acceleration_with_Better-than-Binary_Energy_Efficiency
status: pending_review
proposed_update: Expand with: 'Architecture: Completely unrolled in feature map and filter dimensions to eliminate iterative computation; hierarchical clock gating minimizes clock power. Standard cell memories (SCMs) used for weight and feature map storage. Fabrication: GF 22 nm FDX (FDSOI) technology. Training: Custom training method to encourage sparse ternary weights, reducing switching activity. Power: 12.2 mW (core) with 3.1 POp/s/W efficiency. Measurement context: Based on post-layout power simulation on CIFAR-10 test dataset.'

## [2026-07-02] pending | cutie-ternary-accelerator.md
target_page: cutie-ternary-accelerator.md
target_section: Relationships
source: https://www.researchgate.net/publication/345261170_CUTIE_Beyond_PetaOpsW_Ternary_DNN_Inference_Acceleration_with_Better-than-Binary_Energy_Efficiency
status: pending_review
proposed_update: Add link: [[cpa-factored-gemmini-systolic-array]] for comparison of accelerator design approaches (systolic array vs. fully unrolled datapath).

## [2026-07-02] pending | xuantie-c950.md
target_page: xuantie-c950.md
target_section: Optimization-Relevant Details
source: https://github.com/HelenMaryhm/shl
status: pending_review
proposed_update: Add under 'Compiler/toolchain support': SHL (Structure of Heterogeneous Library) is a high-performance heterogeneous computing library provided by T-HEAD that uses the CSI-NN2 API for the XuanTie CPU platform and provides optimized binary libraries (source: GitHub HelenMaryhm/shl).

## [2026-07-02] merge_pending | shl-heterogeneous-library.md
target_page: shl-heterogeneous-library.md
canonical_name: SHL
colliding_name: SHL
source: https://zhangwm-pt.github.io/shl/md_README.html
status: pending_review
<!-- merge_draft_body
# SHL

SHL (Structure of Heterogeneous Library, Chinese name: ShiHulan) is a high-performance heterogeneous computing library provided by T-HEAD for XuanTie CPU platforms. The library implements the CSI-NN2 neural network API and provides optimized binary libraries for XuanTie processors, supporting symmetric and asymmetric quantization, 8-bit, 16-bit, and float16 data types, and both NCHW and NHWC data formats. SHL is designed to be used with HHB (a deployment tool) for automatic API invocation across different architectures including CPU and NPU. The library includes reference C implementations and assembly-optimized implementations specifically for XuanTie CPUs. SHL is open source and references projects like Caffe, TensorFlow, ncnn, MNN, Tengine, CMSIS_5, ONNX, and XNNPACK. The library can be built from source for specific XuanTie cores, such as the C906, using the T-HEAD RISC-V GCC toolchain, and examples for running models like MobileNet-v1 are provided.

## Key Claims

- SHL provides a high-performance heterogeneous computing library for XuanTie CPU platforms using the CSI-NN2 API.
- Supports both symmetric and asymmetric quantization for neural network inference.
- Supports 8-bit, 16-bit, and float16 data types.
- Compatible with NCHW and NHWC data formats.
- Provides reference C implementation and assembly optimization for XuanTie CPUs.
- Integrates with HHB for automatic API invocation across CPU and NPU architectures.
- Can be built from source for specific XuanTie cores (e.g., C906) using the T-HEAD RISC-V GCC toolchain.
- Includes example deployment of MobileNet-v1 on XuanTie C906 hardware.

## Relationships

- [[spacemit-x60-processor]]: Another RISC-V hardware target that may benefit from SHL-like library support for heterogeneous computing.
- [[tvm-metaschedule-rvv-integration]]: TVM is used by HHB for model deployment; SHL integration with TVM-based compilers can optimize inference on RISC-V platforms.

## Sources

- [SHL README on GitHub Pages](https://zhangwm-pt.github.io/shl/md_README.html)
merge_draft_body -->

## [2026-07-02] merge_pending | shl-heterogeneous-library.md
target_page: shl-heterogeneous-library.md
canonical_name: SHL
colliding_name: SHL
source: https://github.com/openvinotoolkit/shl
status: pending_review
<!-- merge_draft_body
# SHL

SHL (Structure of Heterogeneous Library) is a high-performance heterogeneous computing library provided by T-HEAD, Alibaba's chip design division, for accelerating neural network inference on RISC-V based platforms. The library implements the CSI-NN2 interface, which is T-HEAD's neural network library API for XuanTie CPU platforms, and provides a set of optimized binary libraries that take advantage of the specific microarchitectural features of XuanTie processors. While SHL delivers reference implementations for the XuanTie CPU family, the optimization for each NPU target platform is delegated to the respective vendor, enabling a modular approach to heterogeneous computing. The library integrates with the HHB neural network compilation toolchain, which quantizes and compiles models for RISC-V deployment, and is hosted under the OpenVINO toolkit organization on GitHub, indicating interoperability with Intel's OpenVINO inference framework.

## Key Claims

- SHL provides the reference implementation for XuanTie CPU platform using the CSI-NN2 API.
- SHL offers a series of optimized binary libraries for neural network inference on XuanTie CPUs.
- NPU-specific optimization is completed by the vendor of the specific platform, not by SHL itself.
- SHL is developed by T-HEAD and hosted under the OpenVINO toolkit organization on GitHub.

## Relationships

- [[xuantie-c950]]: SHL is a software library that provides optimized neural network inference for XuanTie CPU platforms, including the C950.
- Insufficient context for additional cross-links; no existing wiki pages for CSI-NN2 or HHB toolchain are currently present.

## Sources

- [GitHub - openvinotoolkit/shl: An optimized neural network ...](https://github.com/openvinotoolkit/shl)
merge_draft_body -->

## [2026-07-02] pending | xuantie-c950.md
target_page: xuantie-c950.md
target_section: Optimization-Relevant Details
source: https://github.com/openvinotoolkit/shl
status: pending_review
proposed_update: Add SHL (Structure of Heterogeneous Library) as a supported software library for neural network optimization, with CSI-NN2 API support. Source: openvinotoolkit/shl repository.

## [2026-07-02] merge_pending | shl-heterogeneous-library.md
target_page: shl-heterogeneous-library.md
canonical_name: SHL
colliding_name: SHL
source: https://github.com/BHbean/shl
status: pending_review
<!-- merge_draft_body
# SHL

SHL (Structure of Heterogeneous Library), also known by its Chinese name ShiHulan, is a high-performance heterogeneous computing library provided by T-HEAD, the chip design division of Alibaba Group. It is specifically designed to provide an optimized reference implementation for neural network operators on XuanTie CPU platforms. The library exposes the CSI-NN2 API, which is T-HEAD's neural network library API for XuanTie CPUs, and ships as a set of optimized binary libraries targeting various neural network operations. The library is designed to work in conjunction with HHB, a tool that quantizes and compiles neural network models; during inference, SHL is called automatically by the HHB runtime. While SHL provides the reference implementation for XuanTie CPUs, optimizations for each NPU target platform are handled by the vendor of that specific platform, following a heterogeneous computing architecture that separates CPU and NPU optimization responsibilities.

## Key Claims

- SHL is a heterogeneous computing library provided by T-HEAD for XuanTie CPU platforms.
- SHL uses the CSI-NN2 API as its interface.
- SHL provides a series of optimized binary libraries for neural network operators.
- SHL can be called automatically by HHB after model quantization and compilation.
- NPU-specific optimizations are not part of SHL; vendors provide their own optimizations.

## Relationships

- [[xuantie-c950]]: SHL targets XuanTie CPU platforms, which include high-performance cores like the XuanTie C950.
- [[gemmini]]: SHL provides optimized neural network operators that could complement hardware accelerators such as the Gemmini systolic array generator, though direct integration is not documented.

## Sources

- [GitHub - BHbean/shl](https://github.com/BHbean/shl)
- [Alibaba - Hello from SHL | SHL](https://www.t-head.cn/)
merge_draft_body -->

## [2026-07-02] merge_pending | nncase.md
target_page: nncase.md
canonical_name: nncase
colliding_name: nncase
source: https://github.com/kendryte/nncase
status: pending_review
<!-- merge_draft_body
# nncase

nncase is an open-source deep learning compiler stack developed by Kendryte for AI accelerators, primarily targeting the Kendryte K230 RISC-V-based system-on-chip. It supports model conversion from TFLite, Caffe, and ONNX formats into optimized code for the K230's neural processing unit (NPU). The toolchain is available as a Python package installable via pip and includes a runtime library for inference deployment. nncase performs quantization (u8/int8) and optimization to achieve high inference throughput while preserving accuracy. Benchmark results for standard models such as MobileNetV2, ResNet50V2, YOLOv5s, and YOLOv8 variants show FPS ranging from approximately 5.5 to 600 on the K230 platform with minimal accuracy loss compared to floating-point baselines.

## Key Claims

- nncase is a neural network compiler for AI accelerators, notably the Kendryte K230.
- It supports model import from TFLite, Caffe, and ONNX formats.
- The compiler performs u8/u8 quantization and optimization.
- It achieves 600.24 FPS for MobileNetV2 at [1,224,224,3] shape on K230 with top-1 accuracy 71.1% vs baseline 71.3%.
- ResNet50V2 achieves 86.17 FPS with top-1 accuracy 75.11% vs baseline 75.44%.
- For object detection, YOLOv5s achieves 23.645 FPS with mAP50 0.566 vs baseline 0.567.
- YOLOv8s segmentation achieves 7.845 FPS with bbox mAP50 0.606 vs baseline 0.606.
- Pose estimation models (YOLOv8n_pose_320) achieve 36.066 FPS with keypoints mAP50-90 0.359 vs baseline 0.358.

## Relationships

- [[gap9-vs-stm32f7-odtl-benchmark]]: This unrelated benchmark page is the only existing page in the provided wiki context. Insufficient context for additional cross-links; no K230 or Kendryte hardware pages are available in the provided wiki context to link to.

## Sources

- [GitHub README: kendryte/nncase](https://github.com/kendryte/nncase)
merge_draft_body -->

## [2026-07-02] merge_pending | xiangshan-nanhu-vdot.md
target_page: xiangshan-nanhu-vdot.md
canonical_name: XiangShan Nanhu-vdot
colliding_name: XiangShan Nanhu-vdot
source: https://arxiv.org/abs/2409.00661
status: pending_review
<!-- merge_draft_body
# XiangShan Nanhu-vdot

XiangShan Nanhu-vdot is a specialized instruction set processor for edge AI based on the RISC-V instruction set architecture, extending the open-source XiangShan Nanhu processor core with custom vector dot product instructions and dedicated vector dot product calculation units. It is designed to accelerate large language model (LLM) inference computation on edge devices by enhancing execution efficiency and reducing energy consumption with limited hardware overhead. The Nanhu-vdot adds pipeline processing logic to support vector dot product operations and was validated on an FPGA platform, achieving over four times the speed of scalar methods in vector dot product computation and approximately 30% faster GPT-2 model inference compared to pure software implementation.

## Key Claims

- The Nanhu-vdot extends the XiangShan Nanhu RISC-V processor core with custom vector dot product instructions and dedicated calculation units.
- FPGA hardware testing demonstrated over 4x speedup in vector dot product computation compared to scalar execution.
- Hardware-software co-design for GPT-2 inference achieved approximately 30% speed improvement over pure software implementation with negligible additional hardware and power overhead.
- The design targets edge AI applications, addressing high-performance and low-power requirements.

## Optimization-Relevant Details

- ISA/profile: RISC-V base ISA with custom vector dot product extension.
- Vector/matrix/accelerator support: Custom vector dot product units and pipeline processing logic.
- Memory/cache/TLB/DMA: Not specified in available source.
- Compiler/toolchain support: Not specified in available source.

## Relationships

- [[earth-shifting-based-vector-memory-access]]: The EARTH optimization is a complementary microarchitectural technique for vector memory access in RISC-V vector units; Nanhu-vdot's vector dot product hardware could benefit from similar memory access optimizations.
- [[cpa-factored-gemmini-systolic-array]]: Both designs target AI acceleration on RISC-V platforms; while CPA-factored Gemmini focuses on systolic array optimization, Nanhu-vdot provides a vector dot product approach for LLM inference.

## Sources

- [2409.00661] Research on LLM Acceleration Using the High ... (arXiv)
merge_draft_body -->

## [2026-07-02] merge_pending | ucie.md
target_page: ucie.md
canonical_name: UCIe
colliding_name: Universal Chiplet Interconnect Express
source: https://semiengineering.com/what-is-ucie/
status: pending_review
<!-- merge_draft_body
# Universal Chiplet Interconnect Express

Universal Chiplet Interconnect Express (UCIe) is an open industry standard for die-to-die interconnect and serial bus communication between chiplets in a single package. Co-developed by AMD, Arm, ASE Group, Google Cloud, Intel, Meta, Microsoft, Qualcomm, Samsung, and TSMC, UCIe defines a complete protocol stack covering the Physical Layer, Die-to-Die Adapter Layer, and Protocol Layer. The specification supports data rates from 8 Gbps/pin to 16 Gbps/pin with planned extensibility to 32 Gbps/pin, uses clock forwarding with single-ended DDR signaling for power efficiency, and provides a sideband channel for parameter exchange and negotiation between two dies. UCIe maps common protocols such as PCI Express and CXL, enabling developers to leverage existing software stacks and simplifying the adoption of in-package integration using multi-die architectures. The standard is designed for compatibility with various package technologies from organic substrates to advanced silicon interposers.

## Key Claims

- UCIe is an open specification for die-to-die interconnect developed by a consortium of major semiconductor and cloud companies.
- It defines a three-layer protocol stack: Physical Layer (electrical AFE, clock forwarding, DDR signaling), Die-to-Die Adapter Layer (link initialization, capability discovery, CRC, retry), and Protocol Layer (mapping of PCIe, CXL, and user-defined protocols).
- Supports data rates from 8 Gbps/pin to 16 Gbps/pin, with planned support up to 32 Gbps/pin for future high-bandwidth applications.
- Uses data scrambling at the PHY level to reduce power supply disturbances without impacting bandwidth efficiency.
- Achieves high energy efficiency (pJ/b), high edge usage efficiency (Tbps/mm), and low latency (ns).
- Supports multiple current and trending use cases, including present and future high-bandwidth networking and data center applications.
- Interoperability of compliant devices is ensured by the complete stack definition.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: As a systolic array accelerator, Gemmini can be implemented as a chiplet and communicate with other dies (e.g., memory, I/O) via UCIe in a multi-die package, leveraging the standard's die-to-die interconnect capabilities.
- [[earth-shifting-based-vector-memory-access]]: This vector memory access optimization targets RISC-V vector units that could be integrated as a chiplet subsystem using UCIe for high-bandwidth communication with other system components.

## Sources

- [What Is UCIe? – Semiconductor Engineering](https://semiengineering.com/what-is-ucie/)
- [UCIe – Wikipedia](https://en.wikipedia.org/wiki/UCIe)
merge_draft_body -->

## [2026-07-02] merge_pending | sophon-sg2042.md
target_page: sophon-sg2042.md
canonical_name: Sophon SG2042
colliding_name: Sophon SG2042
source: https://www.research.ed.ac.uk/en/publications/is-risc-v-ready-for-hpc-prime-time-evaluating-the-64-core-sophon-/
status: pending_review
<!-- merge_draft_body
# Sophon SG2042

The Sophon SG2042 is a commodity 64-core RISC-V central processing unit designed for high-performance computing workloads. Released in 2023, it is built around the XuanTie C920 cores developed by T-Head Semiconductor (Alibaba's Damo Academy) and is the first commercially available 64-core RISC-V CPU targeting HPC and data center applications. The chip is designed to evaluate the readiness of RISC-V for HPC prime-time, providing a platform for benchmarking against existing x86 high-performance CPUs and other RISC-V hardware. The SG2042 is available on platforms such as the Milk-V Pioneer, and has been the subject of academic performance evaluations using the RAJAPerf benchmarking suite (Brown et al., SC'23 Workshops). The performance evaluation reported that the SG2042 delivers, per core, five to ten times the performance of the nearest widely available RISC-V hardware, and is outmatched by x86 CPUs by a factor of four to eight on multi-threaded workloads.

## Key Claims

- World's first commodity 64-core RISC-V CPU (as of 2023).
- Built on XuanTie C920 core technology.
- Per-core RAJAPerf benchmark performance is 5x to 10x faster than the nearest widely available RISC-V hardware.
- Multi-threaded performance is 4x to 8x slower than modern x86 high-performance CPUs, though some individual kernels run faster on the SG2042.
- The system used the RAJAPerf benchmarking suite for performance comparison.

## Optimization-Relevant Details

- ISA/profile: RISC-V (with XuanTie-specific extensions; XTheadVector based on RVV 0.7.1 per related documentation).
- Vector/matrix/accelerator support: Not specified in the available source.
- Memory/cache/TLB/DMA: Not specified.
- Compiler/toolchain support: Not specified (RAJAPerf used as benchmark suite).

## Relationships

- [[xuantie-c950]]: Both are high-performance RISC-V CPUs from the Alibaba/Damo Academy ecosystem; the XuanTie C950 is a newer server-class chip built on a 5nm process, while the SG2042 uses the older C920 cores.
- Insufficient context for additional cross-links to entity pages within the wiki.

## Sources

- [Is RISC-V ready for HPC prime-time: Evaluating the 64-core Sophon SG2042 RISC-V CPU](https://www.research.ed.ac.uk/en/publications/is-risc-v-ready-for-hpc-prime-time-evaluating-the-64-core-sophon-/)
merge_draft_body -->

## [2026-07-02] merge_pending | sophon-sg2042.md
target_page: sophon-sg2042.md
canonical_name: Sophon SG2042
colliding_name: Sophon SG2042
source: https://arxiv.org/html/2406.12394
status: pending_review
<!-- merge_draft_body
# Sophon SG2042

The Sophon SG2042 is a 64-core RISC-V CPU designed for high-performance workloads, first released in summer 2023. It is the first mass-produced, commodity-available high-core-count RISC-V processor, developed by Sophon and aimed at HPC applications. The CPU integrates 64 T-Head XuanTie C920 cores organized in clusters of four, each cluster sharing a 1MB L2 cache. The C920 cores implement the RV64GCV instruction set with the 0.7.1 draft version of the RISC-V Vector Extension (RVV) supporting 128-bit vectors. Each core features a 12-stage out-of-order, multiple-issue superscalar pipeline with three decode units, four rename/dispatch units, eight issue/execute units, and two load/store units. The cache hierarchy includes 64KB of L1 instruction and data cache per core, 1MB of L2 cache per quad-core cluster, and a 64MB L3 system cache shared across all cores. The SG2042 provides four DDR4-3200 memory controllers and 32 lanes of PCIe Gen4 for I/O. The CPU is available on the Milk-V Pioneer board, which includes 128GB of DDR4 RAM. Software support relies on T-Head's fork of the GNU Compiler Collection (XuanTie GCC) because mainline GCC and LLVM do not yet support the RVV v0.7.1 extension. The compiler generates Vector Length Specific (VLS) RVV assembly targeting the 128-bit vector width. The SG2042 represents a significant step toward RISC-V adoption in high-performance computing, offering a competitive alternative to x86-64 and AArch64 CPUs for certain workload classes.

## Key Claims

- First mass-produced 64-core RISC-V CPU for high-performance workloads (released summer 2023).
- C920 cores are 12-stage out-of-order superscalar with four-issue execution.
- RVV v0.7.1 with 128-bit vector width; requires custom XuanTie GCC for auto-vectorization.
- Cache hierarchy: 64KB L1 I/D per core, 1MB L2 per cluster, 64MB L3 shared.
- Memory subsystem: 4x DDR4-3200 controllers; memory bandwidth/latency identified as the primary performance bottleneck.
- In single-core performance, SG2042 delivers between 2.6x and 16.7x improvement over other RISC-V CPUs (based on NPB benchmarks).
- Compared to x86-64 and AArch64 desktop CPUs, SG2042 performs competitively on compute-bound algorithms but falls behind on memory-bound or latency-sensitive algorithms.

## Optimization-Relevant Details

- **ISA/profile**: RV64GCV with RVV v0.7.1 (draft version, not final RVV 1.0)
- **Vector/matrix/accelerator support**: 128-bit vector units; no matrix (tensor) accelerator on chip
- **Memory/cache/TLB/DMA**: 64KB L1 I/D per core; 1MB L2 per quad-core cluster; 64MB L3 system cache; 4x DDR4-3200 memory controllers; PCIe Gen4 x32; no on-chip DMA engine documented
- **Compiler/toolchain support**: XuanTie GCC 8.4 (20210618) recommended for best auto-vectorization; mainline GCC and LLVM lack RVV v0.7.1 support

## Relationships

- [[llvm-riscv-fptrunc-narrowing-optimization]]: The LLVM optimization for RISC-V FPTrunc narrowing may indirectly benefit SG2042 if LLVM gains RVV v0.7.1 support in the future.
- [[tvm-metaschedule-rvv-integration]]: The TVM MetaSchedule RVV integration targets RISC-V vector hardware; though supporting RVV 1.0, its methodology could inform future compiler work for the SG2042.
- [[saturn-vector-unit]]: The Saturn vector unit implements the full RVV 1.0 ISA, contrasting with the draft RVV v0.7.1 implementation in the SG2042's C920 cores.

## Sources

- [Performance characterisation of the 64-core SG2042 RISC-V CPU for HPC - arXiv](https://arxiv.org/html/2406.12394)
merge_draft_body -->

## [2026-07-02] merge_pending | sg2042-npb-benchmark.md
target_page: sg2042-npb-benchmark.md
canonical_name: SG2042 NAS Parallel Benchmark Performance
colliding_name: NAS Parallel Benchmark Performance on SG2042
source: https://arxiv.org/html/2406.12394
status: pending_review
<!-- merge_draft_body
# NAS Parallel Benchmark Performance on SG2042

A performance characterization study using NASA's NAS Parallel Benchmark (NPB) suite evaluated the Sophon SG2042 CPU (released summer 2023) against other RISC-V, x86-64, and AArch64 CPUs. The SG2042 was installed in a Milk-V Pioneer board with 128GB of DDR4 RAM, running at 2GHz. Software compiled with XuanTie GCC 8.4 (20210618 release) at optimization level -O3, which generates Vector Length Specific (VLS) RVV assembly targeting the 128-bit vector width. All results are averages of five runs with exclusive machine access. The study compared single-core performance across multiple NPB benchmarks, providing a detailed characterization of computational versus memory-bound performance characteristics. The source paper is from EPCC at the University of Edinburgh, authored by Nick Brown and Maurice Jamieson.

## Key Claims

- The SG2042 consistently outperforms all other tested RISC-V solutions (e.g., QEMU simulation, single-board RISC-V systems) by a factor of 2.6x to 16.7x in single-core NPB performance.
- Against x86-64 and AArch64 CPUs common in HPC (specific models not detailed in the available source), the SG2042 performs comparatively well on computationally bound algorithms (e.g., EP, CG) but shows decreasing relative performance on memory bandwidth or latency-bound algorithms (e.g., IS, MG, FT).
- The performance of the SG2042's memory subsystem is identified as the greatest bottleneck, limiting its suitability for memory-intensive HPC workloads.
- The SG2042 delivers a considerable performance uplift over earlier commodity RISC-V CPUs (confirmed via RAJAPerf suite in prior work), but it does not match the per-core performance of x86-64 and AArch64 CPUs on memory-bound kernels.

## Measurement Context

- **Hardware version**: Milk-V Pioneer board with Sophon SG2042 CPU (2GHz, 64-core, 128GB DDR4 RAM)
- **Software/toolchain version**: XuanTie GCC 8.4 (20210618 release), compiled with -O3
- **Workload shape**: NASA NAS Parallel Benchmark suite (NPB); individual benchmarks: CG, EP, FT, IS, MG; single-core execution mode
- **Metric**: Speedup ratio (SG2042 vs other RISC-V CPUs); relative performance classification (compute-bound vs memory-bound)
- **Method**: Each benchmark executed 5 times on exclusive-use machine; results averaged; no error bars reported in source
- **Evidence strength**: measured

## Relationships

- [[llvm-riscv-fptrunc-narrowing-optimization]]: The LLVM optimization targeting RISC-V FPTrunc narrowing is a compiler-level enhancement that, if ported to the SG2042's toolchain, could improve floating-point division performance for compute-bound NPB benchmarks.
- [[tvm-metaschedule-rvv-integration]]: The TVM MetaSchedule framework for RVV could potentially be applied to optimize NPB kernel implementations on the SG2042, although the SG2042 uses an older RVV version.
- [[saturn-vector-unit]]: The Saturn vector unit represents a more modern RVV 1.0 microarchitecture; the SG2042's RVV v0.7.1 implementation contrasts in vector length and instruction support, making performance comparisons informative.

## Sources

- [Performance characterisation of the 64-core SG2042 RISC-V CPU for HPC - arXiv](https://arxiv.org/html/2406.12394)
merge_draft_body -->

## [2026-07-02] pending | et-soc-1.md
target_page: et-soc-1.md
target_section: Optimization-Relevant Details
source: https://www.mfgrobots.com/Article/iiot/embedded/5249.html
status: pending_review
proposed_update: Add memory interface details: Four 64-bit DDR interfaces (each comprising four 16-bit channels) deliver 96×16-bit bandwidth using LPDDR4x. Add off-chip cache capability: a six-chip stack configuration reaches 100 GB off-chip cache. Source: search snippet from 'Esperanto Unveils 1,093‑Core RISC‑V AI Accelerator for Data ...' (https://www.mfgrobots.com/Article/iiot/embedded/5249.html).

## [2026-07-02] merge_pending | et-soc-1.md
target_page: et-soc-1.md
canonical_name: ET-SoC-1
colliding_name: ET-SoC-1
source: https://docs.hpc.gwdg.de/services/ftp/esperanto/index.html
status: pending_review
<!-- merge_draft_body
# ET-SoC-1 Platform

The ET-SoC-1 (ET) is a manycore processor originally developed by Esperanto Technologies for high-performance computing and artificial intelligence applications. The chip integrates over 1000 RISC-V ET-Minion processing cores, each featuring a vector processing unit (VPU) and a tensor unit (TU) optimized for machine learning operations. A network-on-chip (NoC) interconnects the cores with 32 GB of distributed LPDDR4X memory, enabling high throughput within a power envelope of approximately 40 W per card. Each card connects via a PCIe 4.0 x8 interface. In 2025, Ainekko acquired the intellectual property and plans to open-source the platform. The GWDG Future Technology Platform currently hosts 4 compute nodes with 8 ET-SoC-1 cards each for researcher access.

## Key Claims

- Integrates over 1000 RISC-V ET-Minion cores, each with a VPU and tensor unit.
- 32 GB of distributed LPDDR4X memory connected via a network-on-chip.
- Power envelope of approximately 40 W per card.
- PCIe 4.0 x8 interface per card.
- Ainekko acquired the IP in 2025 and plans to open-source the platform.
- Available on the GWDG FTP with 4 compute nodes hosting 8 cards each.

## Optimization-Relevant Details

- ISA/profile: RISC-V (ET-Minion cores with vector and tensor extensions)
- Vector/matrix/accelerator support: Each core contains a VPU and a tensor unit (TU).
- Memory/cache/TLB/DMA: 32 GB distributed LPDDR4X via NoC; no cache details provided.
- Compiler/toolchain support: Not specified in the source.

## Relationships

- [[pulp-nn-optimization-recipe]]: Both target accelerating neural network inference on RISC-V manycore platforms, with PULP-NN providing software-level optimizations for quantized NNs on clustered RISC-V processors.
- [[earth-shifting-based-vector-memory-access]]: EARTH optimization targets vector memory access efficiency on RISC-V vector units, which is relevant to the ET-SoC-1's VPU memory subsystem.
- Insufficient context for additional cross-links.

## Sources

- [ET-SoC-1 Platform :: Documentation for HPC](https://docs.hpc.gwdg.de/services/ftp/esperanto/index.html)
merge_draft_body -->

## [2026-07-02] pending | et-soc-1.md
target_page: et-soc-1.md
target_section: full
source: https://vlsifacts.com/esperantos-et-soc-1-chip-integrates-more-than-1000-risc-v-cores-for-energy-efficient-ml-recommendation/
status: pending_review
proposed_update: Add details from Hot Chips 33 presentation by Dave Ditzel: present operating frequency ranges (ET-Minion 500 MHz to 1.5 GHz, ET-Maxion 500 MHz to 2 GHz); add transistor count (24 billion); clarify on-die memory (over 160 MB); add interfaces (eMMC FLASH, PCIe x8 Gen4); add Glacier Point v2 accelerator card configuration (up to 6 ET-SoC-1 chips, 192 GB DRAM, 822 GB/s DRAM bandwidth, 120 W limit); add performance per watt estimates (123x for ML recommendation, 25.7x for image classification); note power typically <20 W. Update Key Claims to include these specific numbers.

## [2026-07-02] merge_pending | vindexmac-structured-sparse-matrix-optimization.md
target_page: vindexmac-structured-sparse-matrix-optimization.md
canonical_name: vindexmac instruction
colliding_name: Optimizing Structured-Sparse Matrix Multiplication in RISC-V Vector Processors
source: https://www.researchgate.net/publication/388180297_Optimizing_Structured-Sparse_Matrix_Multiplication_in_RISC-V_Vector_Processors
status: pending_review
<!-- merge_draft_body
# Structured-Sparse Matrix Multiplication Optimization in RISC-V Vector Processors

This optimization recipe describes how to accelerate structured-sparse matrix multiplication on RISC-V vector processors by exploiting the 2:4 block sparsity pattern and a newly proposed custom instruction called `vindexmac` (vector index-multiply-accumulate). The `vindexmac` instruction performs an indirect read from the vector register file using a scalar register as an index, multiplies that value with the least significant element of a second vector register, and accumulates the result into a destination vector register. The approach also leverages optimized loop unrolling strategies and careful data distribution across scalar and vector register files to reduce instruction count and data movement. According to the proposing research paper (accepted in IEEE Transactions on Computers), when integrated into a decoupled RISC-V vector processor, the `vindexmac` instruction combined with interleaved unrolling yields a runtime improvement of 25% to 33% compared to highly-optimized vectorized kernels using only the currently defined RISC-V instruction set. The optimization targets convolutional neural network workloads with structured sparsity, making it relevant for efficient ML inference and training on vector processors. Evidence strength is classified as reported, based on the paper's experimental results from an RTL implementation with negligible hardware overhead.

## Key Claims

- The addition of the single custom `vindexmac` instruction, combined with interleaved loop unrolling, improves runtime by 25% and 33% over optimized vectorized kernels that use only standard RISC-V vector instructions (source: accepted IEEE Transactions on Computers paper, 2025).
- The `vindexmac` instruction enables indirect reads from the vector register file without introducing additional dependencies that limit loop unrolling, reducing the number of instructions per matrix multiplication iteration.
- Critical performance parameters include data distribution across scalar and vector register files, data locality, and loop unrolling effectiveness; the work analyzes these quantitatively.
- The proposed method scales with the number of cores and with increasing sparsity rates (1:4 pattern shown in evaluations).
- Hardware cost is reported as negligible for integrating `vindexmac` into a decoupled RISC-V vector processor.

## Transformation

- **Prerequisites**: A RISC-V vector processor that supports the standard V extension (RVV) at any VLEN (vector length) and that allows custom instruction integration (e.g., via a decoupled vector unit). The input workload should involve matrix multiplication with structured sparsity patterns such as 2:4 block sparsity (up to 2 non-zero elements per 4 consecutive elements). A compiler toolchain (Clang) for baseline compilation is available.
- **Steps**:
  1. Identify structured-sparse matrix multiplication operations in the target workload (e.g., convolutional neural network layers).
  2. Represent the sparse matrix in a compact format that encodes the 2:4 pattern (position of non-zeros within each block).
  3. Implement the vector kernel using standard RISC-V vector loads and multiply-accumulate instructions, with inner and outer loop unrolling factors chosen for the target microarchitecture.
  4. Replace standard gather/scatter and multiply-accumulate sequences with the `vindexmac` instruction: use a scalar register to address a specific vector register containing the sparse index positions, multiply each indexed element with the corresponding element of a second vector register, and accumulate into the destination.
  5. Apply interleaved unrolling (inner and outer loop unrolling factors of 16 and 8 are recommended in the paper for Alg-3S) to expose more instruction-level parallelism and reduce loop overhead.
  6. Tune data placement to keep frequently used vectors in the register file and minimize scalar-to-vector moves.
- **Expected effect**: Reduction in instruction count per matrix multiplication iteration, elimination of register dependencies that hinder unrolling, and overall runtime improvement of 25% to 33% compared to the best standard-ISA vectorized baseline. Speedups can be higher for workloads with higher sparsity (e.g., 1:4 pattern) and on multi-core systems.
- **Failure modes**: The optimization relies on the availability of the custom `vindexmac` instruction, which is not part of the ratified RISC-V specification; adoption requires custom hardware extensions. For processors without such support, the standard vectorized baseline (e.g., Alg-3S with interleaved unrolling) still provides some benefit but lacks the indirect indexing capability. The effectiveness depends on the specific microarchitecture and VLEN; results may not generalize to all RISC-V vector processors. No failure modes related to correctness were reported.
- **Measurements**: On a decoupled RISC-V vector processor running CNN workloads with 2:4 structured sparsity, the proposed approach (inner/outer unrolling factors 8 and 4) achieved a speedup of 25% to 33% over the best standard-ISA baseline (SpMM with fine-grained unrolling factors 16/8) as reported in the paper. For 1:4 sparsity with increasing numbers of cores, the speedup remained consistent. Relative performance analysis shows the proposed algorithms (Alg-3S-FC-FI) outperforming sequential scalar implementations (SPA) by a large margin (figures in original paper). Evidence strength: reported (data from accepted IEEE Transactions on Computers paper, January 2025).

## Relationships

- [[vectrans]]: Both recipes target compiler-level or instruction-level optimization for RISC-V vector execution, but VecTrans uses LLM-assisted code refactoring whereas this recipe introduces a custom hardware instruction to reduce instruction count.
- [[llvm-auto-re-vectorization-to-riscv]]: That recipe focuses on re-vectorizing existing SIMD intrinsics to RVV; this one provides a specific optimization for structured-sparse matrix operations that could benefit from such re-vectorization as a compilation step before applying the `vindexmac` transformation at the kernel level.

## Sources

- Titopoulos, V., Alexandridis, K., Peltekis, C., Nicopoulos, C., & Dimitrakopoulos, G. (2025). Optimizing Structured-Sparse Matrix Multiplication in RISC-V Vector Processors. IEEE Transactions on Computers (accepted). arXiv:2501.10189. DOI: 10.48550/arXiv.2501.10189.
merge_draft_body -->
