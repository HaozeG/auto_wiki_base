# Wiki Patch Queue

## [2026-07-09] merge_pending | wormhole.md
target_page: wormhole.md
canonical_name: Wormhole
colliding_name: Wormhole
source: https://deepwiki.com/tenstorrent/tt-isa-documentation
status: applied
<!-- merge_draft_body
# Wormhole

Wormhole B0 is Tenstorrent's second-generation AI accelerator ASIC, designed with a many-tile architecture comprising over 120 Tensix compute tiles interconnected by dual independent Network-on-Chip (NoC) fabrics in a 2D torus topology. Each Tensix tile is a heterogeneous compute unit containing five Baby RISC-V cores (RV32IM ISA) for instruction dispatch and control, a specialized Tensor Coprocessor with a low-precision (19-bit) Matrix Unit (FPU) for high-throughput multiply-accumulate operations and a 32-lane Vector Unit (SFPU) for FP32 computations, and 1464 KiB of L1 SRAM organized into 16 banks for parallel data access. The chip provides comprehensive instruction set documentation covering the RISC-V cores, the Matrix and Vector units, data movement instructions (UNPACR, PACR), and configuration registers. Memory-mapped interfaces at defined base addresses (e.g., INSTRN_BUF_BASE, TENSIX_MOP_CFG_BASE) enable software to program the hardware directly. Wormhole B0 is the direct predecessor of the Blackhole A0 chip, which retains the same foundational architecture while introducing targeted enhancements to the vector unit, FMA, memory, and registers.

## Key Claims

- 120+ Tensix tiles organized in three functional categories, interconnected by dual independent NoCs (NoC #0 with X-major routing, NoC #1 with Y-major routing)
- Each Tensix tile contains five Baby RISC-V cores (RV32IM) for control: RISC-V B (data mover), RISC-V T0/T1/T2 for UNPACK/MATH/PACK phases
- Matrix Unit (FPU) performs low-precision (19-bit) operations at high throughput
- Vector Unit (SFPU) handles FP32 operations across 32 lanes
- 1464 KiB L1 RAM organized into 16 banks with parallel access
- MOP Expander at TENSIX_MOP_CFG_BASE can expand single instructions into thousands of micro-operations
- Wait Gate synchronizes instructions via semaphores at 0xFFE80020
- Supports floating-point models including FMA, and data formats like BFP (compressed block floating point)
- Blackhole A0 enhances SFPU, FMA, memory, and registers over Wormhole B0

## Relationships

- [[blackhole]] shares the same Tensix tile architecture and ISA foundation as Wormhole; Blackhole A0 introduces targeted enhancements to the SFPU, FMA, memory, and registers.
- [[tensix-core]] could be a future page for the specific compute core used in both Wormhole and Blackhole.

## Sources

- https://deepwiki.com/tenstorrent/tt-isa-documentation
merge_draft_body -->

## [2026-07-09] pending | blackhole.md
target_page: blackhole.md
target_section: Architecture
source: https://deepwiki.com/tenstorrent/tt-isa-documentation
status: applied
proposed_update: Add section on shared Tensix tile architecture: dual NoC with X/Y major routing, five Baby RISC-V cores per tile, Matrix Unit 19-bit, Vector Unit 32-lane FP32, and 1464 KiB L1 RAM. Also add note about MOP expander and instruction set documentation source.

## [2026-07-09] merge_pending | tt-metalium.md
target_page: tt-metalium.md
canonical_name: TT-Metalium
colliding_name: TT-Metalium
source: https://github.com/afuller-TT/tt-metalium
status: applied
<!-- merge_draft_body
# TT-Metalium

TT-Metalium is Tenstorrent's open-source, low-level AI hardware SDK and programming model that enables custom kernel development for Tenstorrent hardware. It serves as the foundation for the TT-NN operator library. Installation is available via four methods: pre-built binaries (via wheel), a Docker release image, building from source, or using Anaconda. The source installation involves cloning the repository and building the library. TT-Metalium aims to provide close-to-metal access for kernel developers and experimenters, supporting Tenstorrent's AI accelerator chips. The SDK is part of the tt-metal repository, which also includes the TT-NN operator library.

## Key Claims

- TT-Metalium is an open-source low-level AI hardware SDK by Tenstorrent.
- It provides a kernel development programming model that gives close-to-metal access.
- It is the foundation for the TT-NN operator library.
- Installation supports four methods: binaries, Docker, source build, and Anaconda.
- The SDK targets custom kernel development and experimentation on Tenstorrent hardware.

## Relationships

- [[blackhole]]: TT-Metalium is the low-level SDK used to program Tenstorrent hardware such as the Blackhole chip.

## Sources

- https://github.com/afuller-TT/tt-metalium
merge_draft_body -->

## [2026-07-09] merge_pending | tensix-core.md
target_page: tensix-core.md
canonical_name: Tensix Core
colliding_name: Tensix core
source: https://github.com/tenstorrent/tt-metal/blob/main/METALIUM_GUIDE.md
status: applied
<!-- merge_draft_body
# Tensix core

The Tensix core is the fundamental compute unit in Tenstorrent's Tensix processor architecture. Each Tensix core contains five small RISC-V CPUs for control and instruction dispatch, dedicated hardware units for matrix operations (FPU) and vector operations (SFPU), data packing/unpacking units, and 1.5 MB of local SRAM. Unlike GPU streaming processors, the RISC-V cores primarily handle instruction dispatch and control flow, while the matrix and vector units perform the actual computation. Data flows through a dual Network-on-Chip (NoC) interface into the core, where it is unpacked by the unpacker, processed by the compute units, packed by the packer, and sent out via the other NoC. The NoCs operate in a quasi-full-duplex configuration with a unidirectional wraparound 2D torus topology, enabling efficient communication across the chip. The architecture natively operates on 32×32 tiles, optimized for deep learning operations. Programming a Tensix core typically requires three kernel types: a reader kernel for data input, a compute kernel for calculations, and a writer kernel for data output, which coordinate through circular buffers in SRAM. This design prioritizes efficient data movement and local SRAM usage over frequent DRAM access, distinguishing it from traditional GPU architectures.

## Key Claims

- Each Tensix core contains five Baby RISC-V CPUs (Data Movement 0, Data Movement 1, Unpack, Math, Pack), a matrix unit (FPU), a vector unit (SFPU), unpack/pack units, and 1.5 MB of L1 SRAM.
- The NoC interfaces (NoC 0 and NoC 1) traverse the chip in opposite directions in a wraparound 2D torus topology, enabling bidirectional communication with unidirectional links.
- The architecture natively operates on 32×32 tiles, optimized for deep learning workloads.
- Typical data flow: NoC 0 reads data from DRAM or other cores; Unpacker prepares data; Matrix/Vector units compute; Packer packs results; NoC 1 sends results to DRAM or other cores.
- Programming requires three kernel types per core: reader, compute, and writer, coordinated via circular buffers in SRAM.

## Relationships

- [[blackhole]]: The Blackhole chip uses Tensix cores as its fundamental compute tiles, with 120 such cores in the p100a/p150 variants.

## Sources

- https://github.com/tenstorrent/tt-metal/blob/main/METALIUM_GUIDE.md
merge_draft_body -->

## [2026-07-09] merge_pending | tensix-core.md
target_page: tensix-core.md
canonical_name: Tensix Core
colliding_name: Tensix core
source: https://github.com/tenstorrent/tt-metal/blob/main/METALIUM_GUIDE.md
status: applied
<!-- merge_draft_body
# Tensix core

The Tensix core is the fundamental compute node in Tenstorrent's Tensix Processor AI accelerators. Each Tensix core contains five minimal RISC-V CPUs (called Baby RISC-V cores) for control and instruction dispatch, a dedicated matrix unit (FPU) for tile-based operations, a vector unit (SFPU) for element-wise and reduction ops, data packing and unpacking units, and 1.5 MB of local SRAM (also referred to as L1 memory). Two Network-on-Chip (NoC) interfaces connect the core to the chip-wide wraparound 2D torus interconnect, enabling data movement with DRAM and other Tensix cores. The intended data flow within a Tensix core follows a software-pipelined pattern: NoC 0 reads data from DRAM, the unpacker reformats it into 32×32 tiles, the matrix or vector unit performs computation, the packer compresses results, and NoC 1 sends output to DRAM or other cores. This architecture prioritizes efficient local SRAM usage over frequent DRAM access, and the five Baby RISC-V cores handle instruction dispatch rather than computation, keeping the design deliberately minimalist compared to modern superscalar CPUs.

## Key Claims

- Each Tensix core contains 5 Baby RISC-V CPUs (Data Movement 0, Data Movement 1, Unpack, Math, Pack) plus dedicated hardware for matrix (FPU) and vector (SFPU) operations.
- Each core has 1.5 MB of local SRAM (L1) for transient data and inter-component exchange.
- The NoC operates in a quasi-full-duplex configuration with two unidirectional wraparound rings (NoC 0 and NoC 1) traversing opposite directions, enabling simultaneous send and receive while optimizing power and area.
- Tensix cores natively operate on 32×32 tiles, a layout optimized for deep learning workloads.
- Data flow within a core follows a pipelined pattern: NoC read → unpack → compute → pack → NoC write, coordinated by the Baby RISC-V cores.

## Relationships

- [[blackhole]] uses Tensix cores as its compute tiles; the Blackhole chip contains 120 such cores (reduced from 140 via firmware).
- [[TT-Metalium]] is the programming model that orchestrates the reader, compute, and writer kernels mapped to Tensix cores.
- The same Tensix core architecture is also used in the earlier Wormhole processor.

## Sources

- https://github.com/tenstorrent/tt-metal/blob/main/METALIUM_GUIDE.md
merge_draft_body -->

## [2026-07-09] merge_pending | tt-metalium.md
target_page: tt-metalium.md
canonical_name: TT-Metalium
colliding_name: TT-Metalium
source: https://github.com/tenstorrent/tt-metal/blob/main/METALIUM_GUIDE.md
status: applied
<!-- merge_draft_body
# TT-Metalium

TT-Metalium is Tenstorrent's software programming model and SDK for developing applications that run on their Tensix Processor AI accelerators. The model exposes three kernel types per Tensix core: a reader kernel for data input, a compute kernel for the main arithmetic operations, and a writer kernel for data output. These kernels coordinate through circular buffers in the core's local SRAM, enabling a software-pipelined execution pattern with explicit data movement. The Metalium stack provides compute APIs and data movement abstractions that abstract the underlying hardware details while allowing developers to control resource allocation, kernel dispatch, and fast dispatch mechanisms. It also supports a Single Program Multiple Data (SPMD) paradigm for scaling workloads across multiple Tensix cores and chips. The architecture natively operates on 32×32 tiles, and the programming model is designed to minimize DRAM access by leveraging the local SRAM hierarchy and dual NoC interconnect. Metalium kernels are compiled to the Baby RISC-V cores for instruction dispatch, not for direct computation, making the programming model distinct from CUDA-style thread-level parallelism.

## Key Claims

- Each Tensix kernel set includes three distinct kernel types: reader, compute, and writer, coordinated via circular buffers in SRAM.
- Metalium provides compute APIs and data movement APIs for kernel development, ensuring compatibility across hardware generations.
- Fast dispatch is a mechanism for efficient kernel launch and resource management.
- SPMD (Single Program Multiple Data) is supported for multi-core and multi-chip scaling.
- The programming model is built for the tile-based (32×32) architecture and capitalizes on local L1 SRAM and the dual NoC wraparound topology.

## Relationships

- [[tensix-core]] is the hardware compute node that Metalium programs; each kernel set (reader, compute, writer) maps to a Tensix core.
- [[blackhole]] is one of the chip families that Metalium supports; the programming model abstracts the underlying core count and memory configuration.

## Sources

- https://github.com/tenstorrent/tt-metal/blob/main/METALIUM_GUIDE.md
merge_draft_body -->

## [2026-07-09] merge_pending | wormhole.md
target_page: wormhole.md
canonical_name: Wormhole
colliding_name: Wormhole
source: https://clehaxze.tw/gemlog/2025/04-21-programming-tensotrrent-processors.gmi
status: apply_failed (pipeline rejected)
<!-- merge_draft_body
# Wormhole

Tenstorrent Wormhole is an AI accelerator chip organized as a grid of Tensix cores interconnected by two unidirectional Network-on-Chip (NoC) interfaces running in opposite directions in a 2D torus topology. Each Tensix core contains five small RISC-V CPUs responsible for instruction dispatch, a vector unit, a matrix/tensor unit, a pack and unpack unit, and 1.5 MB of SRAM for local data storage. The programming model uses three independent kernels (reader, compute, writer) that run on the core and synchronize via circular buffers backed by hardware mutexes. Unlike GPU architectures that rely on SIMT, the Tenstorrent architecture emphasizes flexibility and supports SPMD patterns, allowing developers to customize data movement for specific operations such as the efficient Scaled Dot Product Attention algorithm on Wormhole.

## Key Claims

- Each Tensix core contains five "baby" RISC-V CPUs, each with a 5-stage pipeline, single issue, basic branch prediction, and asynchronous loading. These cores handle instruction dispatch, not computation.
- The core includes 1.5 MB of SRAM for local data storage and communication between components.
- Two unidirectional NoCs (NoC 0 and NoC 1) wrap around the chip in opposite directions, forming a 2D torus. Each supports simultaneous send and receive, providing a return path after each operation.
- The intended data flow is: NoC 0 reads data from DRAM or other cores, the unpacker prepares it for the matrix/tensor unit, the matrix unit performs computation, the packer formats results, and NoC 1 sends the output.
- The architecture is flexible: developers can use both interfaces for reading to double effective NoC bandwidth at the cost of overlapping reads and writes, or use SRAM as temporary storage.
- Synchronization between kernels is achieved through circular buffers (pipes/queues) backed by hardware mutexes.
- The default programming pattern is SPMD; topology-aware operations like FlashAttention can exploit the physical layout.

## Relationships

- [[blackhole]] is the successor chip to Wormhole. Both use the same Tensix core architecture, but Blackhole offers more cores, integrated Ethernet, and higher memory bandwidth.

## Sources

- https://clehaxze.tw/gemlog/2025/04-21-programming-tensotrrent-processors.gmi
merge_draft_body -->

## [2026-07-09] merge_pending | wormhole.md
target_page: wormhole.md
canonical_name: Wormhole
colliding_name: Tenstorrent Wormhole
source: https://arxiv.org/html/2603.23343v1
status: apply_failed (pipeline rejected)
<!-- merge_draft_body
# Tenstorrent Wormhole

The Tenstorrent Wormhole is a spatial computing platform designed for neural network acceleration, featuring an array of small, simple processing elements (PEs) with single-instruction multiple-data (SIMD) parallelism for high-throughput math. Each PE has a small scratchpad memory, and a user-controlled network-on-chip (NoC) enables explicit data movement between PEs. Unlike traditional CPUs and GPUs, Wormhole demands more explicit control over data placement and parallelism. The architecture supports vectorization and provides an open toolchain. Recent work has demonstrated that Wormhole can also be used for scientific computing workloads: researchers have implemented three numerical kernels—sparse iterative solvers, stencil computations, and a full conjugate gradient solver—on the platform and evaluated their performance against Nvidia GPUs, showing that AI accelerators merit consideration for workloads traditionally dominated by CPUs and GPUs.

## Key Claims

- Tenstorrent Wormhole features an array of simple PEs with SIMD parallelism and small scratchpad memories.
- The architecture uses a user-controlled network-on-chip (NoC) for explicit data movement between PEs.
- Supports vectorization and provides an open toolchain for software development.
- Enables implementation of scientific computing kernels including sparse iterative solvers, stencil computations, and conjugate gradient solvers.
- Performance evaluations against Nvidia GPUs show that Wormhole is competitive for traditional HPC workloads, challenging the assumption that AI accelerators are only suited for neural network training and inference.

## Relationships

- [[tt-xla-performance-optimization-techniques]]: The TT-XLA optimization techniques described in this recipe are applicable to Tenstorrent Wormhole as a single-chip Tenstorrent accelerator, providing guidance for performance tuning of PyTorch models on this hardware.

## Sources

- https://arxiv.org/html/2603.23343v1
merge_draft_body -->

## [2026-07-09] merge_pending | tt-forge.md
target_page: tt-forge.md
canonical_name: TT-Forge
colliding_name: TT-Forge
source: https://tenstorrent.com/en/software/tt-forge
status: applied
<!-- merge_draft_body
# TT-Forge

TT-Forge is Tenstorrent's MLIR-based compiler stack that enables compilation, optimization, debugging, and extension of AI models for execution on Tenstorrent hardware. It integrates with multiple machine learning frameworks including OpenXLA, MLIR, ONNX, TVM, PyTorch, and TensorFlow, lowering models into optimized intermediate representations (IRs) for Tenstorrent's low-level AI hardware SDKs, TT-NN and TT-Metalium. The compiler utilizes custom dialects such as TTIR, TTNN, and TTKernel to perform hardware-aware compilation, maximizing inference performance and hardware utilization. TT-Forge also provides tools including TT-Explorer for visual performance analysis, TT-Blacksmith for ready-to-run training examples, and TT-NPE for network-on-chip simulation and profiling.

## Key Claims

- TT-Forge is an MLIR-based compiler stack for Tenstorrent hardware.
- It connects with OpenXLA, MLIR, ONNX, TVM, PyTorch, and TensorFlow.
- Models are lowered into optimized IRs for execution on TT-NN and TT-Metalium.
- Custom dialects TTIR, TTNN, and TTKernel enable hardware-aware compilation.
- Hardware-aware compilation achieves high utilization, efficient memory access, and scalable performance across chips.
- Included tools: TT-Explorer (visual performance analyzer), TT-Blacksmith (ready-to-run training examples), and TT-NPE (network-on-chip simulator and profiler).
- TT-XLA is a PJRT-based bridge for JAX and PyTorch with multi-chip support.
- TT-Forge-ONNX is a framework-agnostic frontend for ONNX and TensorFlow single-chip projects.

## Relationships

- TT-Forge is the overarching compiler stack that includes the TT-XLA frontend; optimization techniques specific to TT-XLA are detailed in [[tt-xla-performance-optimization-techniques]].

## Sources

- https://tenstorrent.com/en/software/tt-forge
merge_draft_body -->

## [2026-07-09] merge_pending | tt-forge.md
target_page: tt-forge.md
canonical_name: TT-Forge
colliding_name: TT-Forge Software Stack
source: https://deepwiki.com/tenstorrent/tt-forge/2-tt-forge-software-stack
status: apply_failed (pipeline rejected)
<!-- merge_draft_body
# TT-Forge Software Stack

TT-Forge is Tenstorrent's open-source AI compiler system that provides a seamless path from standard machine learning framework code to optimized execution on Tenstorrent hardware. The architecture is modular, composed of three frontend systems (TT-XLA for PyTorch and JAX via the PJRT interface, TT-Forge-ONNX for ONNX/TensorFlow/PaddlePaddle via TVM, and the legacy TT-Torch frontend), a common TT-MLIR compiler backend, and the TT-Metalium runtime layer. The TT-MLIR compiler progressively lowers input graphs through a chain of intermediate representations: StableHLO, TTIR, TTNN-IR, TTMetal-IR, and TTKernel-IR, applying hardware-specific optimizations including automatic 32x32 tiling, memory management between SRAM (L1) and DRAM, and operation fusing and layout transformations. The runtime layer, TT-Metalium, dispatches the optimized kernels and manages device memory, built on the TTNN library of high-level operations (convolutions, matmuls) and the lower-level TT-Metal SDK. System software includes the User Mode Driver (UMD) and Kernel Mode Driver (KMD) for PCIe communication and device initialization. The stack supports the Wormhole_b0 and next-generation Blackhole architectures, both built on Tensix core arrays.

## Key Claims

- TT-Forge supports multiple frontends: TT-XLA (primary, for PyTorch/JAX via PJRT), TT-Forge-ONNX (TVM-based, for ONNX/TensorFlow/PaddlePaddle), and TT-Torch (legacy PyTorch frontend).
- The TT-MLIR compiler performs automatic tiling to 32x32 tiles, hardware-native for Tensix cores.
- Memory management in the compiler determines data placement between interleaved DRAM and fast local SRAM (L1).
- Optimization passes include operation fusing, layout transformations, and sharding for multi-device execution.
- The compiler progressively lowers through dialects: StableHLO → TTIR → TTNN-IR → TTMetal-IR → TTKernel-IR.
- The runtime consists of TTNN (high-level C++/Python optimized operations library), TT-Metal (SDK for kernel dispatch and memory management), and UMD/KMD drivers.
- Supported hardware includes Wormhole_b0 and Blackhole architectures.

## Relationships

- [[tt-xla-performance-optimization-techniques]]: TT-XLA is the primary frontend of the TT-Forge stack, responsible for ingesting PyTorch and JAX models and producing StableHLO IR for the TT-MLIR compiler. The optimization techniques documented for TT-XLA are applied within the broader TT-Forge software pipeline targeting single-chip Tenstorrent hardware.

## Sources

- https://deepwiki.com/tenstorrent/tt-forge/2-tt-forge-software-stack
merge_draft_body -->

## [2026-07-09] merge_pending | tensix-core.md
target_page: tensix-core.md
canonical_name: Tensix Core
colliding_name: Tensix Core
source: https://github.com/afuller-TT/tt-metalium/blob/main/METALIUM_GUIDE.md
status: apply_failed (pipeline rejected)
<!-- merge_draft_body
# Tensix Core

The Tensix Core is the fundamental compute node in Tenstorrent's Tensix processor architecture, designed as a specialized AI accelerator unit rather than a general-purpose CPU core. Each Tensix Core contains five small RISC-V CPUs (designated as Data Movement 0, Data Movement 1, Unpack, Math, and Pack) that handle instruction dispatch and control flow, while dedicated hardware units—a matrix unit (FPU) for tensor operations and a vector unit (SFPU) for element-wise vector operations—perform the actual computation. The core includes 1.5 MB of local SRAM (referred to as L1) that stores transient data and facilitates data exchange between internal components. Data movement is orchestrated via two Network-on-Chip (NoC) interfaces (NoC 0 and NoC 1) that operate in opposite directions on a wraparound 2D torus topology, enabling any core to communicate with any other location on the chip. The intended data flow is a pipeline: NoC 0 reads data from DRAM or other cores, the Unpacker converts data into 32×32 tiles, the compute units process the tiles, the Packer formats the result, and NoC 1 sends the result out. Programming a Tensix Core with the TT-Metalium framework requires three kernel types per core—reader, compute, and writer—that coordinate through circular buffers in SRAM. The RISC-V cores are deliberately minimal, resembling classic RISC architectures like the MIPS R3000, and serve primarily to issue commands to the NoC and compute units rather than perform computation directly.

## Key Claims

- Each Tensix Core contains five Baby RISC-V CPUs: Data Movement 0, Data Movement 1, Unpack, Math, and Pack.
- The core includes 1.5 MB of local SRAM (L1).
- Native tile-based computing on 32×32 tiles, optimized for deep learning operations.
- Two NoC interfaces (NoC 0 and NoC 1) operate in opposite directions on a wraparound 2D torus, providing full connectivity across the chip.
- Data flow pipeline: NoC → Unpacker → Compute (Matrix/Vector) → Packer → NoC.
- The Baby RISC-V cores are minimal and superscalar-free, sharing architectural similarity with the MIPS R3000.
- Programming with Metalium: reader, compute, and writer kernels per core, using circular buffers for coordination.

## Relationships

- [[blackhole]] is a Tenstorrent chip that integrates Tensix Cores; Blackhole's Tensix tile is described as having features identical to the Tensix Core, including five Baby RISC-V cores and ~1464 KiB L1 RAM (close to the 1.5 MB specified here).

## Sources

- https://github.com/afuller-TT/tt-metalium/blob/main/METALIUM_GUIDE.md
merge_draft_body -->

## [2026-07-09] merge_pending | tt-quietbox-2.md
target_page: tt-quietbox-2.md
canonical_name: TT-QuietBox 2
colliding_name: TT-QuietBox 2
source: https://docs.tenstorrent.com/tt-quietbox2-guide/
status: applied
<!-- merge_draft_body
# TT-QuietBox 2

The TT-QuietBox 2 (QB2) is a complete workstation-class AI accelerator system manufactured by Tenstorrent. It contains four Blackhole AI accelerators arranged on two p300c cards, providing a total of 480 Tensix cores running at 1.35 GHz and 720 MB of on-chip SRAM distributed across the chips. The system is liquid-cooled with a maximum acoustic noise of 38 dBA and ships with an AMD Ryzen 7 9700X CPU, 256 GB DDR5-5600 system RAM, a 4 TB NVMe PCIe Gen5 storage drive, and Ubuntu 24.04.3 LTS as the operating system. The QB2 is designed for running large language models and other AI workloads; it comes pre-loaded with the Qwen3-32B model, and its Four Blackhole chips are interconnected via Warp400 links using Samtec ARP6 connectors.

## Key Claims

- The QB2 contains 4× Blackhole AI accelerators (2× p300c cards), each with 120 Tensix cores at 1.35 GHz, totaling 480 cores.
- Total on-chip SRAM is 720 MB (180 MB per chip).
- Total DRAM is 128 GB GDDR6 (32 GB per chip), with a bandwidth of 1,024 GB/s per card.
- Chip interconnect uses Warp400 (2× per card, Samtec ARP6).
- Host system: AMD Ryzen 7 9700X (8 cores, 3.8 GHz), 256 GB DDR5-5600 RAM, 4 TB NVMe PCIe Gen5 storage.
- OS: Ubuntu 24.04.3 LTS.
- Peak power draw approximately 1,500 W from a 1,600 W PSU.
- Liquid cooling with 38 dBA max noise level.
- Pre-loaded with Qwen3-32B and supports a wide range of models via tt-inference-server, tt-metal, and tt-forge software stacks.
- Supported models include Llama-3.1-8B, Llama-3.3-70B, Qwen3-32B, FLUX.1, Mochi 1, and many others.

## Relationships

- [[tt-xla-performance-optimization-techniques]] shares the Blackhole AI accelerator architecture that the QB2 uses, but the optimization recipe targets single-chip configurations while the QB2 is a multi-chip system with four Blackhole chips.

## Sources

- https://docs.tenstorrent.com/tt-quietbox2-guide/
merge_draft_body -->

## [2026-07-09] merge_pending | tt-quietbox-2.md
target_page: tt-quietbox-2.md
canonical_name: TT-QuietBox 2
colliding_name: Quietbox 2
source: https://docs.tenstorrent.com/tt-quietbox2-guide/read/
status: apply_failed (pipeline rejected)
<!-- merge_draft_body
# Quietbox 2

The Tenstorrent Quietbox 2 (QB2) is a workstation designed for AI inference, integrating two Tenstorrent Blackhole p300c cards for a total of four Blackhole chips. Each p300c is a dual-chip PCIe Gen4 card, and each Blackhole chip contains 120 Tensix compute cores organized in a 12×10 compute grid within a 17×12 Network-on-Chip (NoC) mesh. The workstation ships with Ubuntu 24.04 LTS and a pre-installed software stack including the TTNN Python library, vLLM, the tt-smi hardware monitoring tool, tt-studio (a no-code web UI for model serving), and TT-Forge/XLA container wrapper. Model weights for Qwen3-32B are pre-cached on disk, allowing immediate deployment through tt-studio without downloading. The four Blackhole chips do not share memory and are addressed independently via the TTNN API (ttnn.CreateDevices({0,1,2,3})). The machine is intended for users who want to run large language models out of the box without compiling source code or installing drivers.

## Key Claims

- Contains 2× Blackhole p300c cards (4 Blackhole chips total) connected via PCIe Gen4 as four independent devices.
- Each Blackhole chip has 120 Tensix cores (out of 140 positions on the 12×10 compute grid).
- Pre-installed software: TTNN (Python venv at ~/tt-metal/python_env/), vLLM, tt-smi, tt-studio, TT-Forge/XLA container wrapper.
- Pre-cached model weights for Qwen3-32B.
- Runs Ubuntu 24.04 LTS.
- Default login username and password: ttuser/ttuser (should be changed on first boot).
- The ~/tt-metal directory contains only Python venvs, not source code; source code is intentionally omitted.

## Relationships

- [[blackhole]]: The Quietbox 2 uses two p300c cards, each containing two Blackhole chips, sharing the same Tensix core architecture and NoC structure described in the Blackhole page. The p300c card is a dual-chip variant not detailed in the Blackhole page.
- [[tt-metalium]]: The pre-installed TTNN Python library is the high-level operator API built on TT-Metalium.
- [[tt-forge]]: The pre-installed TT-Forge/XLA container wrapper is used for compiling models onto the Quietbox 2's Blackhole chips.

## Sources

- https://docs.tenstorrent.com/tt-quietbox2-guide/read/
merge_draft_body -->

## [2026-07-09] merge_pending | tt-forge.md
target_page: tt-forge.md
canonical_name: TT-Forge
colliding_name: TT-Forge
source: https://github.com/tenstorrent/tt-quietbox2-guide/blob/main/src/content/shared/tt-forge-intro.md
status: applied
<!-- merge_draft_body
# TT-Forge

TT-Forge is a compiler pipeline developed by Tenstorrent that compiles models from PyTorch, JAX, or ONNX into native executables for Tensix-core-based accelerators. It provides two frontends: TT-XLA, which uses `torch.compile(backend="tt")` for PyTorch and `jax.jit` for JAX/Flax, and TT-Forge-ONNX, which uses the `forge.compile` Python call for ONNX, TensorFlow, and PaddlePaddle models. Both frontends lower through the same TT-MLIR compiler. The compiled model runs directly on Tenstorrent hardware without needing a separate inference server or runtime. TT-Forge also integrates with the tt-forge-models zoo, which provides over 800 model variants (ResNet, BERT, CLIP, DINOv2, BLOOM, LLaMA, and others) through a standardized `ModelLoader` interface. Installation requires setting up a Python virtual environment and installing the `pjrt-plugin-tt` package from Tenstorrent's private package index.

## Key Claims

- TT-Forge compiles PyTorch, JAX, and ONNX models for Tenstorrent hardware.
- It provides two frontends: TT-XLA (primary, using `torch.compile(backend="tt")` and `jax.jit`) and TT-Forge-ONNX (using `forge.compile`).
- Both frontends lower to the TT-MLIR compiler.
- The compiled artifact runs natively on Tenstorrent Tensix cores with no additional inference runtime.
- TT-Forge is installed via pip with an extra index URL (`pjrt-plugin-tt`) followed by `tt-forge-install`.
- The tt-forge-models zoo provides over 800 model variants with a standardized `ModelLoader` interface.
- The compiled model retains the original PyTorch module interface, allowing drop-in replacement.

## Relationships

- [[tt-xla-performance-optimization-techniques]]: TT-XLA is the primary frontend of TT-Forge for PyTorch and JAX models; the optimization techniques documented for TT-XLA apply directly to models compiled through TT-Forge.

## Sources

- https://github.com/tenstorrent/tt-quietbox2-guide/blob/main/src/content/shared/tt-forge-intro.md
merge_draft_body -->

## [2026-07-09] merge_pending | tt-quietbox-2.md
target_page: tt-quietbox-2.md
canonical_name: TT-QuietBox 2
colliding_name: TT-QuietBox 2
source: https://wccftech.com/tenstorrent-tt-quietbox-2-risc-v-ai-workstation-128-gb-memory-liquid-cooling-9999-usd/
status: applied
<!-- merge_draft_body
# TT-QuietBox 2

The Tenstorrent TT-QuietBox 2 is an AI workstation powered by the RISC-V architecture, designed for on-premises deployment of large language models and other AI workloads without reliance on cloud infrastructure. Announced in March 2026, the system features up to four Blackhole ASICs, each integrating 16 RISC-V big cores and Tensix compute cores, with a combined total of 480 Tensix cores delivering 2,654 TFLOPS at BlockFP8 precision. It includes 128 GB of GDDR6 high-speed memory across the four cards, plus 256 GB of DDR5 system memory. The workstation employs liquid cooling to maintain quiet operation and plugs into a standard 120V wall outlet, requiring no specialized electrical work. The entire software stack, including the TT-Forge compiler, TT-Metalium low-level AI SDK, and TT-LLK kernel library, is open source, providing full visibility and control. The base configuration starts at $9,999, and the system ships globally in Q2 2026.

## Key Claims

- Runs Llama 3.1 70B at 476.5 tokens per second on the TT-QuietBox 2 (no batch size or sequence length specified).
- Runs GPT-OSS 120B, a 120-billion-parameter model, entirely on device.
- Predicts the structure of a 686-amino-acid protein using Boltz-2 in 49 seconds on a single Blackhole processor, matching flagship workstation GPU performance.
- Supports parallel inference of four protein structures, yielding 4x higher throughput compared to single-structure prediction.
- Delivers 2,654 TFLOPS at BlockFP8 precision across 480 Tensix cores.
- Includes 128 GB of GDDR6 memory and 256 GB of DDR5 system memory.
- Starts at $9,999 for the base configuration.
- Entire software stack is open source, including TT-Forge, TT-Metalium, and TT-LLK.
- Runs on Ubuntu 24.04 pre-installed and can run models from PyTorch, ONNX, TensorFlow, JAX, and PaddlePaddle via TT-Forge.

## Relationships

- [[tt-xla-performance-optimization-techniques]] — The TT-XLA optimization techniques documented for single-chip Tenstorrent hardware are applicable to the Blackhole ASICs inside the TT-QuietBox 2; compiler optimization levels, data format selection, device warmup, runtime trace, and batch size tuning can be used to improve inference performance on this multi-chip system.

## Sources

- https://wccftech.com/tenstorrent-tt-quietbox-2-risc-v-ai-workstation-128-gb-memory-liquid-cooling-9999-usd/
merge_draft_body -->

## [2026-07-09] merge_pending | blackhole.md
target_page: blackhole.md
canonical_name: Blackhole
colliding_name: Blackhole
source: https://aiwiki.ai/wiki/blackhole_tenstorrent
status: applied
<!-- merge_draft_body
# Blackhole

The Blackhole is Tenstorrent's third-generation AI accelerator chip used as the foundation of the company's high-performance computing systems. It integrates 140 Tensix++ compute cores (120 enabled on shipping cards), sixteen SiFive Intelligence X280 RISC-V cores, 32 GB of GDDR6 memory, a Gen5 PCI Express interface, and ten 400 Gbps Ethernet links on a single die, providing a standalone AI computer capable of running machine learning workloads. The chip is deployed in the Blackhole P150 PCIe board, which is designed for infinitely scalable AI processing. This architecture represents Tenstorrent's latest design, building on the Wormhole generation with increased core counts and higher bandwidth.

## Key Claims

- The Blackhole chip contains 140 Tensix++ compute cores, with 120 cores enabled on shipping cards.
- It includes sixteen SiFive Intelligence X280 RISC-V cores for control and general-purpose processing.
- The chip has 32 GB of GDDR6 memory on-package.
- Interfaces: Gen5 PCI Express and ten 400 Gbps Ethernet links.
- The chip is used in the Blackhole P150 PCIe board, which is marketed as infinitely scalable for AI workloads.
- The Blackhole is designed as a standalone AI computer, capable of executing models without host CPU intervention for many tasks.

## Relationships

- [[blackhole-quietbox]] uses four Blackhole P150 accelerator chips in a liquid-cooled workstation configuration, providing a development platform that scales to the Galaxy rack systems.

## Sources

- https://aiwiki.ai/wiki/blackhole_tenstorrent
- https://tenstorrent.com/cards (PCIe board details)
- https://nixos.wiki/wiki/Tenstorrent (Tenstorrent platform overview)
merge_draft_body -->

## [2026-07-09] merge_pending | tt-forge.md
target_page: tt-forge.md
canonical_name: TT-Forge
colliding_name: TT-Forge
source: https://github.com/tenstorrent/tt-forge/blob/main/README.md
status: applied
<!-- merge_draft_body
# TT-Forge

TT-Forge is Tenstorrent's open-source AI compiler stack, built on TT-Metalium. It brings together frontends, an MLIR compiler, a kernel DSL, and a model library to make running AI workloads on Tenstorrent hardware straightforward. It supports over 800 model variants tested in continuous integration, with thousands more tested internally, including large models such as GPT-OSS 120B, Llama 3 70B, Stable Diffusion XL, Whisper, and YOLOv12. TT-Forge supports inference and training workloads from PyTorch, JAX, and ONNX, and allows custom kernel development. The stack comprises several sub-projects: TT-XLA (PyTorch/JAX frontend), TT-Forge-ONNX (ONNX/TensorFlow/PaddlePaddle frontend), TT-MLIR (core MLIR compiler defining TTIR, TTNN, and TTKernel dialects), TT-Lang (Python kernel DSL, early preview), TT-Blacksmith (training recipes with 40+ experiments), and TT-Forge-Models (model library with standardized loaders).

## Key Claims

- TT-Forge is an open-source AI compiler stack built on TT-Metalium, available on GitHub.
- Supports inference and training on Tenstorrent hardware from PyTorch, JAX, and ONNX (single-chip for ONNX, single/multi-chip for PyTorch/JAX).
- Over 800 model variants are continuously tested in CI; thousands more have been tested internally, covering LLMs, vision, multimodal, detection, segmentation, speech, and more.
- Sub-projects: TT-XLA (PJRT-based PyTorch/JAX frontend), TT-Forge-ONNX (TVM-based ONNX/TensorFlow/PaddlePaddle frontend), TT-MLIR (core MLIR compiler with TTIR, TTNN, TTKernel dialects), TT-Lang (Python kernel DSL with simulation and profiling), TT-Blacksmith (optimized training recipes), and TT-Forge-Models (model library).
- Custom kernels can be written in TT-Lang, a Python DSL that supports fusion, simulation, profiling, and AI-assisted translation from Triton-class DSLs (early preview).
- Training recipes in TT-Blacksmith include 40+ experiments spanning vision, LLMs, and NLP using PyTorch, JAX, and Lightning.

## Relationships

- [[tt-xla-performance-optimization-techniques]] shares the TT-Forge ecosystem: TT-XLA is the primary PyTorch/JAX frontend within TT-Forge, and the optimization techniques documented on that page (optimization levels, warmup, data formats, runtime trace, batch tuning) are applied when compiling models with the TT-XLA component of TT-Forge.

## Sources

- https://github.com/tenstorrent/tt-forge/blob/main/README.md
merge_draft_body -->

## [2026-07-09] merge_pending | blackhole.md
target_page: blackhole.md
canonical_name: Blackhole
colliding_name: Tenstorrent Blackhole
source: https://anuraagw.me/blog/blackhole-architecture
status: applied
<!-- merge_draft_body
# Tenstorrent Blackhole

The Tenstorrent Blackhole is a deep learning accelerator architecture from Tenstorrent, instantiated in the P100A (28 GB GDDR6) and P150B (full chip) boards. It employs a grid of Tensix tiles interconnected by two Networks-on-Chip (NoCs) that operate in opposite directions: noc0 originates at the top-left corner and allows packets to move downward or to the right, while noc1 originates at the bottom-right corner and allows movement upward or to the left. This bidirectional separation of read (noc0) and write (noc1) traffic avoids head-of-line blocking. Communication with the host is routed through the PCIe tile (PCIe 0 on the P100A, PCIe 1 on the P150B). The P100A variant harvests two rightmost columns of Tensix tiles and one DRAM bank (4 GB) due to binning, with the fused-off coordinates varying per board. The toolchain is almost fully open source, ranging from the kernel-mode driver (tt-kmd) and user-mode driver (tt-umd) through low-level kernel libraries (tt-llk) to the high-level runtime (tt-metal and TTNN), with the Tensix SFPI toolchain (sfpi) for custom kernel compilation.

## Key Claims

- The Blackhole architecture uses a grid of Tensix tiles (17 columns x 12 rows on P150B, 14 columns on P100A) with two NoCs (noc0 and noc1) that carry traffic in opposite directions to avoid blocking.
- Multicast writes (broadcasting to multiple tiles simultaneously) are imperative for performance when uploading firmware or kernel binaries to many cores; unicast writes to every core sequentially would incur considerable slowdown.
- The P100A board has 28 GB of GDDR6 memory, with one DRAM bank (4 GB) fused off; the exact disabled tile and DRAM locations vary per unit.
- The open-source toolchain includes drivers, firmware, low-level kernels, and runtime components, providing control over nearly all layers above the Verilog design.
- The fan can be controlled dynamically by sending a message to the ARC tile, and the idle fan curve can be lowered via firmware modifications (e.g., in tt-zephyr-platforms).
- Matmul performance is reported to be approximately equal to an NVIDIA RTX 5090, though this is a reported claim without detailed measurement context.

## Relationships

- [[single-core-matmul-tt-metalium]] implements a basic bfloat16 matmul kernel on a single Tensix core of the Blackhole architecture, demonstrating the TT-Metalium programming model that runs on this hardware.

## Sources

- https://anuraagw.me/blog/blackhole-architecture
merge_draft_body -->
