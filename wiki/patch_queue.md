# Wiki Patch Queue

## [2026-07-09] merge_pending | ara2.md
target_page: ara2.md
canonical_name: Ara2
colliding_name: Ara2
source: https://bohrium.dp.tech/paper/arxiv/2311.07493
status: pending_review
<!-- merge_draft_body
# Ara2

Ara2 is a fully open-source vector processing unit developed by the PULP platform at ETH Zurich and the University of Bologna, supporting the RISC-V Vector Extension version 1.0 frozen ISA. It is designed as a coprocessor for the CVA6 RISC-V core and implements a modular, configurable architecture for single- and multi-core vector processing. Ara2 achieves an average functional-unit utilization of 95% on the most computationally intensive data-parallel kernels across various problem sizes and vector-unit configurations. As the successor to the first-generation Ara vector unit, Ara2 extends the design with improved performance and efficiency, making it the first fully open-source vector processor to implement the RISC-V V 1.0 frozen ISA.

## Key Claims

- Ara2 is the first fully open-source vector processor to support the RISC-V V 1.0 frozen ISA.
- Ara2 achieves an average functional-unit utilization of 95% on computationally intensive data-parallel kernels.
- Ara2 supports single- and multi-core vector processing configurations.
- Ara2 is designed as a coprocessor for the CVA6 RISC-V core within the PULP platform.
- Ara2 is the successor to the first-generation Ara vector unit, with enhancements for multi-core processing and higher utilization.

## Relationships

- [[ara]]: Ara2 is the successor to Ara. Both implement the RISC-V Vector Extension version 1.0 as coprocessors for the CVA6 core, but Ara2 adds support for multi-core configurations and achieves a higher average functional-unit utilization of 95% compared to Ara's baseline performance.

## Sources

- [Ara2: Exploring Single- and Multi-Core Vector Processing with ...](raw/cache/e96e952d676411c2.md)
merge_draft_body -->

## [2026-07-09] merge_pending | chipyard.md
target_page: chipyard.md
canonical_name: Chipyard
colliding_name: Chipyard
source: https://github.com/pku-liang/aps-chipyard
status: pending_review
<!-- merge_draft_body
# Chipyard

Chipyard is an open-source framework for agile development of Chisel-based systems-on-chip (SoCs). Developed by the Berkeley Architecture Research Group at the University of California, Berkeley, Chipyard integrates the Chisel hardware construction language, the Rocket Chip SoC generator, and a collection of Berkeley projects to produce RISC-V SoCs with MMIO-mapped peripherals and custom accelerators. It includes a range of processor cores such as Rocket, BOOM, and CVA6 (Ariane), vector units including Saturn and Ara, and accelerators such as Gemmini and NVDLA. Chipyard supports multiple concurrent hardware development flows: software RTL simulation, FPGA-accelerated simulation via FireSim, automated VLSI flows through Hammer, and bare-metal or Linux-based software workload generation with FireMarshal. The framework is actively maintained and documented at the official Chipyard documentation site.

## Key Claims

- Chipyard is an open-source framework for agile SoC design using the Chisel hardware construction language.
- It integrates the Rocket Chip SoC generator and a suite of Berkeley-developed components.
- It supports multiple processor cores: Rocket, BOOM (including SonicBOOM/BOOMv3), and CVA6 (Ariane).
- It includes vector units: Saturn and Ara.
- It includes accelerators: Gemmini and NVDLA.
- It supports four concurrent development flows: software RTL simulation, FPGA-accelerated simulation (FireSim), automated VLSI flows (Hammer), and software workload generation (FireMarshal).
- It is developed and maintained by the Berkeley Architecture Research Group (UCB-BAR) at UC Berkeley.

## Relationships

- [[ara]]: Chipyard integrates the Ara vector processing unit as one of its hardware generator options for data-parallel workloads. Ara is a 64-bit vector coprocessor for RISC-V that implements the RISC-V Vector Extension version 1.0.

## Sources

- [GitHub - pku-liang/aps-chipyard: An Agile RISC-V SoC Design Framework ...](raw/cache/cc91cee5ef218478.md)
merge_draft_body -->

## [2026-07-09] merge_pending | gemmini.md
target_page: gemmini.md
canonical_name: Gemmini
colliding_name: Gemmini
source: https://chipyard.readthedocs.io/en/1.5.0/Generators/Gemmini.html
status: pending_review
<!-- merge_draft_body
# Gemmini

Gemmini is an open-source systolic-array based matrix multiplication unit generator designed for integration into RISC-V SoCs through the Rocket Custom Coprocessor (RoCC) interface. Developed as part of the Chipyard framework, it enables exploration of software/hardware tradeoffs for machine learning accelerators targeting edge and mobile devices. The generator supports configurable systolic array dimensions (tile and mesh), multiple dataflows (output-stationary, weight-stationary, or runtime-selectable), and adjustable scratchpad and accumulator memory capacities. It also supports various fixed-point and floating-point data types for input, output, and accumulation, with configurable processing element latencies for floating-point operations. Gemmini implements access-execute decoupling through dedicated load, store, and execute queues, and includes a DMA engine for data movement between main memory and the local scratchpad. Its non-standard RISC-V ISA extension includes configuration, data movement, and matrix multiplication instructions, exposed via C macros and a matrix multiplication library.

## Key Claims

- Gemmini is a systolic-array based matrix multiplication unit generator intended for integrated SoC accelerators.
- It interfaces with Rocket or BOOM tiles via the RoCC port and connects to memory through the System Bus (L2 cache).
- The generator is highly parameterizable: systolic array dimensions (tileRows, tileColumns, meshRows, meshColumns), dataflow (output-stationary, weight-stationary, or runtime choice), scratchpad (sp_banks, sp_capacity) and accumulator (acc_capacity) memory, data types (inputType, outputType, accType), DMA parameters (dma_maxbytes, dma_buswidth, mem_pipeline), and queue sizes for access-execute decoupling.
- Optional scaling during move-in operations from main memory to scratchpad is supported via mvin_scale_args and mvin_scale_shared parameters.
- The Gemmini non-standard ISA extension includes configuration instructions, data movement instructions, and matrix multiplication execution instructions.
- A C matrix multiplication library and C macros for constructing instruction encodings are provided in the software directory.
- The generator produces a C header file reflecting the configuration parameters, which is compiled together with the application software.

## Relationships

- [[ara]]: Both Gemmini and Ara are open-source hardware accelerators for RISC-V SoCs that target data-parallel workloads. Gemmini focuses on matrix multiplication using a systolic array, while Ara implements the RISC-V Vector Extension for general vector processing. Both are parameterizable and can be integrated into Chipyard or PULP ecosystems.

## Sources

- [3.5. Gemmini — Chipyard documentation - Read the Docs](raw/cache/985ce15e462dd7e4.md)
merge_draft_body -->

## [2026-07-09] merge_pending | gemmini.md
target_page: gemmini.md
canonical_name: Gemmini
colliding_name: Gemmini
source: https://mikutyan4.github.io/chipyard-linux-nexys/ch06-gemmini-matrix-operations.html
status: pending_review
<!-- merge_draft_body
# Gemmini

Gemmini is a configurable systolic array generator included in the Chipyard open-source RISC-V SoC design framework. It provides a hardware-accelerated matrix multiplication unit that can be integrated with a Rocket core or other processors. Gemmini is designed to accelerate dense matrix operations common in neural network inference, such as fully connected layers and attention projections. It implements a weight-stationary dataflow where preloaded weights remain in processing elements while input activations flow through the array. The array is composed of processing elements (PEs) each capable of one multiply-accumulate (MAC) operation per cycle. In a typical 8x8 configuration, the array contains 64 PEs and can perform 64 Int8 MACs simultaneously at each clock cycle. Gemmini handles matrices larger than the physical array through automatic tiling, exposing an API called tiled_matmul_auto. The generator is parameterized and can be configured for different array sizes, data types, and memory system parameters. It is part of the Chipyard tutorial for FPGA-based RISC-V system development, where it is used to demonstrate hardware acceleration for LLM inference on FPGA.

## Key Claims

- Gemmini is a configurable systolic array generator within the Chipyard framework.
- Implements a weight-stationary (WS) dataflow mode where weights are preloaded and remain stationary in PEs.
- An 8x8 configuration contains 64 processing elements, each performing one Int8 multiply-accumulate per cycle.
- Provides the tiled_matmul_auto API that automatically tiles large matrices to fit the physical array.
- Designed to accelerate matrix multiplications common in neural network inference, such as QKV projections and FFN layers.
- Can be integrated with a Rocket core and deployed on FPGA.
- Each PE performs the operation c += a × b, receiving inputs from the left and above, and passing them to the right and below.
- Tiling example: a 288×768 matrix multiplication is split into 3456 tiles for an 8×8 array.

## Relationships

- [[ara]]: Ara is a vector processing unit supporting the RISC-V Vector Extension, while Gemmini is a systolic array matrix accelerator. Both are open-source RISC-V accelerators targeting data-parallel workloads, but they differ in approach: Gemmini uses a fixed systolic array for dense matrix multiplication, while Ara uses a general vector processor for arbitrary vector operations. They can be complementary in a system where Gemmini handles matrix-heavy layers and Ara handles other vector operations.

## Sources

- [Chapter 6: Gemmini — Hardware-Accelerated Matrix Operations on FPGA ...](raw/cache/2c1d8369e61c2065.md)
merge_draft_body -->

## [2026-07-09] merge_pending | spacemit_key_stone_k1.md
target_page: spacemit_key_stone_k1.md
canonical_name: SpacemiT Key Stone K1
colliding_name: SpacemiT Key Stone K1
source: https://github.com/spacemit-com/docs-chip/blob/main/en/key_stone/k1/k1_docs/k1_usermanual/1.Overview.md
status: pending_review
<!-- merge_draft_body
# SpacemiT Key Stone K1

The SpacemiT Key Stone K1 is a high-performance, ultra-low-power system-on-chip (SoC) that integrates eight RISC-V 64-bit CPU cores based on the SpacemiT X60 microarchitecture, adhering to the RISC-V 64GCVB architecture and the RVA22 standard. The cores are organized into two quad-core clusters: Cluster 0 delivers 2.0 TOPS AI computing power through customized RISC-V instructions enabling CPU-AI fusion, with each core having 32KB L1 cache, 512KB shared L2 cache, and 512KB TCM; Cluster 1 provides equivalent scalar processing but without the AI acceleration feature. The SoC supports 256-bit vector processing, dual-channel LPDDR4/LPDDR4x memory up to 16 GB, and a broad set of peripherals including USB 3.0, PCIe Gen2, Gigabit Ethernet, MIPI CSI/DSI, and HDMI 1.4. It also integrates an Imagination BXE-2-32 GPU supporting OpenCL 3.0, OpenGL ES 3.2, and Vulkan 1.3, a video processing unit capable of 4K decode/encode, dual ISPs for camera input, and a secure boot system with cryptographic acceleration. The chip targets AI inference workloads using TensorFlow Lite, TensorFlow, and ONNX Runtime frameworks, and is rated for industrial temperature ranges from -40°C to +85°C.

## Key Claims

- Integrates eight SpacemiT X60 RISC-V cores in a dual-cluster configuration (4+4), each core supporting the RISC-V 64GCVB architecture and RVA22 standard.
- Cluster 0 includes AI acceleration providing 2.0 TOPS via customized RISC-V instructions.
- Each core has 32KB L1 cache; clusters share 512KB L2 cache; Cluster 0 also includes 512KB TCM.
- Vector processing width is 256 bits per core.
- DVFS support with operating voltage from 0.6V to 1.05V.
- Memory: dual-chip LPDDR4/LPDDR4x up to 16 GB (2666 Mbps) or LPDDR3 up to 4 GB (1866 Mbps).
- Peripherals: USB 2.0 OTG/Host, USB 3.0 (combo PCIe), three PCIe Gen2 ports, dual Gigabit Ethernet with RGMII, 10x UART, 10x I2C, 4x SPI, 2x MIPI CSI-2 (4-lane), 1x MIPI DSI (4-lane), 128 GPIO, CAN-FD, and more.
- GPU: Imagination BXE-2-32 at 819 MHz, with 32KB SLC, supporting OpenCL 3.0, OpenGL ES 3.2, and Vulkan 1.3.
- VPU: H.265/H.264/VP8/VP9/MPEG4/MPEG2 decoder 4K@60fps, encoder 4K@30fps, simultaneous encode/decode at 1080P@60fps.
- Dual ISP supporting up to 16 MP @30fps, with hardware JPEG encoder, AF/AE/AWB, face detection, PDAF, and 3D denoise.
- Security: RISC-V PMP, secure boot, 4K-bit eFuse, cryptographic engine (TRNG, AES, RSA, ECC, SHA2, HMAC).
- Industrial temperature range (-40°C to +85°C).

## Relationships

- [[ara]]: Both the SpacemiT Key Stone K1 and the Ara vector unit implement 256-bit RISC-V vector processing (RVV), though K1 integrates vector execution directly within its X60 CPU cores while Ara is a dedicated open-source vector coprocessor from the PULP platform. The K1's vector support is part of its RISC-V 64GCVB compliance, whereas Ara is explicitly designed for the RISC-V Vector Extension version 1.0.

## Sources

- [docs-chip/en/key_stone/k1/k1_docs/k1_usermanual/1.Overview.md ... - GitHub](raw/cache/3fbc156ba94261a9.md)
merge_draft_body -->

## [2026-07-09] merge_pending | spacemit_key_stone_k1.md
target_page: spacemit_key_stone_k1.md
canonical_name: SpacemiT Key Stone K1
colliding_name: SpacemiT K1
source: https://www.spacemit.com/products/keystone/k1
status: pending_review
<!-- merge_draft_body
# SpacemiT K1

The SpacemiT K1 (also known as Key Stone K1) is an octa-core 64-bit RISC-V AI CPU developed by SpacemiT, a company focused on building next-generation computing ecosystems based on the RISC-V open instruction set architecture. The chip is designed to provide a high-efficiency and general-purpose AI processor platform for a wide range of applications including single-board computers (SBCs), intelligent robotics, edge inference of large models, home storage and computing terminals, industrial computing, AI PCs, and edge node computers. According to BananaPi documentation, the K1 delivers 50KDMIPS of CPU computing power and 2.0 TOPS of AI computing power, and its single-core performance is claimed to be 30% ahead of an ARM Cortex-A55 core. The chip aims to promote global open-source and open-compute ecosystems, and upstream support across system software, toolchains, and AI software is actively being contributed to open-source projects.

## Key Claims

- The K1 is an octa-core 64-bit RISC-V AI CPU.
- It provides 50KDMIPS CPU computing power and 2.0 TOPS AI computing power.
- Single-core performance is 30% ahead of the ARM Cortex-A55.
- Target applications include SBCs, robotics, edge AI, AI PCs, and edge computing.
- SpacemiT is actively contributing upstream support for the K1 across open-source projects including system software, toolchains, and AI software.

## Relationships

No specific relationship to visible context pages.

## Sources

- [K1 - spacemit.com](raw/cache/2fa3ccc6aed9005e.md)
merge_draft_body -->

## [2026-07-09] merge_pending | spacemit_key_stone_k1.md
target_page: spacemit_key_stone_k1.md
canonical_name: SpacemiT Key Stone K1
colliding_name: SpacemiT Key Stone K1
source: https://wiki.postmarketos.org/wiki/SpacemiT_Key_Stone_K1
status: pending_review
<!-- merge_draft_body
# SpacemiT Key Stone K1

The SpacemiT Key Stone K1 (also referred to as M1) is a RISC-V SoC designed by Chinese company SpacemiT and released in 2024. Manufactured on a 22 nm process, it integrates eight SpacemiT X60 CPU cores arranged in two clusters of four, with maximum clock speeds reaching 1.6 GHz in the first cluster and 2.0 GHz in the second. The SoC includes an IMG BXE-2-32 GPU and provides support for the RISC-V Vector Extension 1.0. Early mainline Linux support was added during Summer 2024, and the SoC is used in several single-board computers and laptops including the Banana Pi BPI-F3, Milk-V Jupiter, and Sipeed Lichee Pi 3A.

## Key Claims

- Manufactured by SpacemiT and released in 2024.
- Contains eight SpacemiT X60 cores in two clusters of four, with clock speeds of 1.6 GHz (cluster 0) and 2.0 GHz (cluster 1).
- Supports the RISC-V Vector Extension version 1.0.
- GPU is an IMG BXE-2-32.
- Fabricated on a 22 nm process.
- Used in multiple consumer devices: Banana Pi BPI-F3, Milk-V Jupiter, Sipeed Lichee Pi 3A, DeepComputing DC-ROMA Laptop II and PAD II, SpacemiT MUSE Book, Ky X1, and Xunlong Orange Pi RV2.
- Bootloader is based on a U-Boot fork with proprietary blobs; an effort to add oreboot support is underway.
- Early mainline Linux support was added in Summer 2024.

## Relationships

- [[ara]]: The Ara vector unit implements the same RISC-V Vector Extension version 1.0 that the SpacemiT X60 cores in the Key Stone K1 support, providing a shared vector ISA foundation for accelerating data-parallel workloads.

## Sources

- [SpacemiT Key Stone K1 - postmarketOS Wiki](raw/cache/9b39243f31bf206f.md)
merge_draft_body -->

## [2026-07-09] merge_pending | risc-v-matrix-extensions.md
target_page: risc-v-matrix-extensions.md
canonical_name: RISC-V Matrix Extensions
colliding_name: Attached Matrix Extension (AME)
source: https://github.com/riscv-admin/attached-matrix-extension/blob/main/charter.adoc
status: pending_review
<!-- merge_draft_body
# Attached Matrix Extension (AME)

The Attached Matrix Extension (AME) is a proposed RISC-V ISA extension for matrix operations, currently under development by the Attached Matrix Extension Task Group under the Unprivileged Spec IC. AME defines an attached matrix unit that executes instructions as part of the processor's instruction stream while maintaining program order and being self-contained with its own set of matrix registers. The extension is designed to be scalable, supporting different operand sizes and allowing matrix-geometry agnostic code. It targets a range of workloads from datacenter to IoT and mobile, including deep-learning training and inference. The specification will cover load, store, and move operations, matrix-matrix, vector-matrix, and scalar-matrix arithmetic, permutation operations, sparse-matrix compression/decompression, and a predication mechanism. AME is intended to be implementable without dependencies on the RISC-V Vector extension, though it defines interactions if both are present.

## Key Claims

- AME defines a RISC-V ISA extension for matrix operations using an attached matrix unit with its own architectural register state.
- The extension is scalable, supporting variable operand sizes and geometry-agnostic code.
- Planned operations include load/store/move, matrix-matrix/vector-matrix/scalar-matrix arithmetic, permutation, and sparse-matrix compression/decompression.
- A predication mechanism is included to control operations on matrix tiles.
- AME mandates a mapping of matrix operations onto instructions defined in a Matrix Operations Extension.
- The specification will review interaction of matrix load/store and prefetching with the RISC-V memory model.
- Deliverables include a specification, intrinsics, SAIL simulator, ACT coverage tools, and proof-of-concept implementations for Linux kernel, TensorFlow, PyTorch, oneDNN, GCC, QEMU, and LLVM MLIR.

## Relationships

- [[ara]]: AME is designed to be orthogonal to the RISC-V Vector Extension; when implemented together, AME supports move operations between vector registers and matrix tile rows/columns, enabling interoperability between vector and matrix computations. Ara implements the RISC-V Vector Extension v1.0 and serves as a reference vector unit design that could coexist with an AME unit.

## Sources

- [attached-matrix-extension/charter.adoc at main · riscv-admin ... - GitHub](raw/cache/a6588fba1f2c11f6.md)
merge_draft_body -->

## [2026-07-09] merge_pending | xuantie_c910.md
target_page: xuantie_c910.md
canonical_name: Xuantie C910
colliding_name: XuanTie C910
source: https://arxiv.org/html/2505.24363v1
status: pending_review
<!-- merge_draft_body
# XuanTie C910

The XuanTie C910 is an open-source superscalar out-of-order RISC-V core originally developed with proprietary interfaces and protocols, including non-standard AXI bus extensions and non-RISC-V compliant interrupt and debug support. In a 2025 study, a modified version of the C910 was presented that achieves full RISC-V standard compliance in its debug, interrupt, and memory interfaces while preserving its out-of-order execution capabilities. Implemented in GlobalFoundries 22FDX technology and integrated into the Cheshire open-source modular SoC platform, the modified C910 demonstrates a 75% area increase and a 119.5% IPC improvement over the scalar CVA6 core. Despite its larger area, the C910 is highly competitive in energy efficiency (GOPS/W), challenging the assumption that high-performance superscalar out-of-order designs inherently incur significant energy costs.

## Key Claims

- Superscalar out-of-order RISC-V core.
- Originally had non-standard AXI, interrupt, debug interfaces.
- A modified version achieves full RISC-V standard compliance.
- 75% area increase and 119.5% IPC improvement over scalar CVA6.
- Implemented in GF22FDX technology in Cheshire SoC.
- Competitive energy efficiency (GOPS/W).

## Relationships

This page currently has no specific relationship to visible context pages based on the source consulted.

## Sources

- [Ramping Up Open-Source RISC-V Cores: Assessing the Energy ...](raw/cache/dd944bc005e8fc47.md)
merge_draft_body -->
