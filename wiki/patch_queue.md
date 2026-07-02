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
