# Wiki Patch Queue

## [2026-06-28] pending | Gemmini_systolic_array_GEMM_accelerator.md
target_page: Gemmini_systolic_array_GEMM_accelerator.md
target_section: Key Claims
source: https://github.com/QuarantineGemmini/gemmini
status: pending_review
proposed_update: Add the following claims supported by the QuarantineGemmini/gemmini README: 'Includes peripheral circuitry to optionally apply activation functions (ReLU, ReLU6)', 'Supports power-of-2 scaling for quantized workloads', 'Supports matrix transpose before feeding into the systolic array for output-stationary dataflow', 'Dataflow can be hardened at elaboration time in addition to runtime selection', 'DMA parameters dma_maxbytes and dma_buswidth are tightly coupled with Rocket Chip SoC system parameters (cache block size and bus beat width)'.

## [2026-06-28] pending | Gemmini_systolic_array_GEMM_accelerator.md
target_page: Gemmini_systolic_array_GEMM_accelerator.md
target_section: Optimization-Relevant Details
source: https://github.com/QuarantineGemmini/gemmini
status: pending_review
proposed_update: Add bullet: 'Peripheral circuitry: activation functions (ReLU, ReLU6), power-of-2 scaling, transpose support'.

## [2026-06-28] pending | Gemmini_systolic_array_GEMM_accelerator.md
target_page: Gemmini_systolic_array_GEMM_accelerator.md
target_section: First paragraph (after existing first paragraph)
source: https://github.com/QuarantineGemmini/gemmini
status: pending_review
proposed_update: Insert sentence: 'The accelerator includes peripheral circuitry for activation functions (ReLU, ReLU6), power-of-2 scaling for quantized workloads, and matrix transpose to support different dataflows.'

## [2026-06-28] pending | Sipeed_MAIX_series.md
target_page: Sipeed_MAIX_series.md
target_section: Key Claims
source: https://deepwiki.com/kendryte/canmv/5.1-kpu-neural-network-processor
status: pending_review
proposed_update: Add detailed claims about the KPU (Knowledge Processing Unit) neural network processor based on the DeepWiki resource: The KPU enables real-time inference on Kendryte K210; supports CNN for computer vision tasks; includes model loading from SD card/flash; implements DMA channels for input image transfer, weight loading, output retrieval, and intermediate activation movement; exposes Python API through maix module with argument parsing for model path, input image, anchor boxes, and threshold; uses pix_ai field in image_t structure for optimized memory access; error handling includes validation for model format, input dimensions, memory allocation, and hardware status using MicroPython exception patterns.

## [2026-06-28] pending | MilkV_Pioneer.md
target_page: MilkV_Pioneer.md
target_section: Key Claims
source: https://milkv.io/docs/pioneer/resources/inferllm
status: pending_review
proposed_update: Add note that InferLLM documentation specifies RISC-V vector 0.7 for the SG2042 CPU in the Milk-V Pioneer, while the current page states RVV 1.0. Clarify that the SG2042 implements RVV 0.7.1 according to some sources, and update the ISA claim to reflect this discrepancy.

## [2026-06-28] pending | Sipeed_MAIX_series.md
target_page: Sipeed_MAIX_series.md
target_section: Key Claims
source: https://wiki.sipeed.com/en/
status: pending_review
proposed_update: Add claims about the newer MaixCAM and MaixCAM2 models based on the Sipeed Wiki comparison table: MaixCAM2 uses AX630C dual-core ARM A53, 3.2 Tops NPU, 113 FPS YOLO11n 640x640; MaixCAM uses SG2002, 1 Tops NPU, 23 FPS YOLO11n 640x640. Include software support (MaixCDK, MaixPy) and mention the range from MaixCAM2 down to Maix-IV with decreasing capability. Source: https://wiki.sipeed.com/en/

## [2026-06-28] pending | Chiplet_RISC_V_AI_SoC_Benchmark_Results.md
target_page: Chiplet_RISC_V_AI_SoC_Benchmark_Results.md
target_section: Sources
source: https://arxiv.org/html/2306.15552v3
status: pending_review
proposed_update: Add reference to survey 'A Survey on Deep Learning Hardware Accelerators for Heterogeneous HPC Platforms' (arXiv:2306.15552) which provides a comprehensive taxonomy including chiplet-based accelerators and RISC-V-based accelerators. This source contextualizes the chiplet architecture within the broader landscape of DL accelerators.

## [2026-06-28] pending | GEMM_with_RISC-V_Vector_Extension.md
target_page: GEMM_with_RISC-V_Vector_Extension.md
target_section: Sources
source: https://arxiv.org/html/2306.15552v3
status: pending_review
proposed_update: Add reference to survey 'A Survey on Deep Learning Hardware Accelerators for Heterogeneous HPC Platforms' (arXiv:2306.15552) which covers RISC-V-based accelerators as part of a broader taxonomy of DL hardware accelerators. This provides context for the RISC-V vector GEMM implementation.

## [2026-06-29] pending | Tenstorrent_Grayskull_e150.md
target_page: Tenstorrent_Grayskull_e150.md
target_section: toolchains
source: https://github.com/tenstorrent/tt-forge
status: pending_review
proposed_update: Add TT-Forge to the list of toolchains, as it is the new MLIR-based compiler stack built on TT-Metalium that supports compiling and running AI workloads on Grayskull hardware. TT-Forge is now the primary open-source compiler for Tenstorrent hardware.

## [2026-06-29] pending | Kendryte_K210.md
target_page: Kendryte_K210.md
target_section: Debugging
source: https://visualgdb.com/tutorials/risc-v/kendryte/k210/
status: pending_review
proposed_update: Add a new 'Debugging' section covering JTAG debug setup for the Kendryte K210 using Visual Studio and VisualGDB. Include: JTAG signal mapping (TDI, TMS, TCK, TDO, RESET) to Sipeed M1 Dock board; recommended JTAG debuggers (Segger J-Link, Olimex ARM-USB-OCD-H, FTDI-based); steps to create, build, and debug a Blinking LED project using the VisualGDB Embedded Project Wizard; note on using the Kendryte-specific toolchain (not generic RISC-V); description of the debug workflow (breakpoints, 'load' command fallback); instructions for programming the external FLASH using K-FLASH tool; reliability issues with Kendryte OpenOCD fork and workarounds (setting breakpoints before program start, reloading firmware, using K-FLASH). This information is sourced from the VisualGDB tutorial 'Debugging Kendryte K210 Projects with Visual Studio'.

## [2026-06-29] pending | Ara_simulator.md
target_page: Ara_simulator.md
target_section: full
source: https://github.com/pulp-platform/ara
status: pending_review
proposed_update: Replace the Ara_simulator.md content with detailed hardware/software dependency information, toolchain build instructions (LLVM, Spike, Verilator), configuration parameters (config folder), simulation modes (including Ideal Dispatcher mode without CVA6), and an overview of supported instructions from the official Ara GitHub README. Update frontmatter: hardware_targets to include Ara and CVA6; toolchains to include LLVM, gcc 7.2.0, Verilator, Bender; constraints to include RISC-V Vector Extension 1.0, CVA6 coprocessor interface, Verilator simulation, and long vector length (default 4096-bit). Add relationships section linking to CVA6 (if page exists) and PULP platform. Retain existing created date and inbound_links count. Update scorecard to reflect new evidence.

## [2026-06-29] pending | Gemmini_systolic_array_GEMM_accelerator.md
target_page: Gemmini_systolic_array_GEMM_accelerator.md
target_section: Key Claims
source: https://github.com/VedantPahariya/BitNet-RISCV-Multicore
status: pending_review
proposed_update: Add a note about a custom Gemmini PE variant for ternary weights: the BitNet-RISCV-Multicore project implements a mux-based PE that replaces multiplier MAC paths for ternary weights {-1,0,+1}, reducing area/power while preserving accuracy. This modification was integrated in a Chipyard-based Ara/CVA6+Gemmini flow using Chisel and targets 1-bit LLM inference.
