---
canonical_name: Vicuna 2.0
aliases:
- Vicuna 2.0 core
- vproc/vicuna2_core
subtype: null
tags:
- RISC-V
- vector co-processor
- embedded
- CV-X-IF
hardware_targets:
- Vicuna 2.0
toolchains:
- CMake
- Verilator
constraints:
- configurable vector register width (VREG_W)
- configurable datapath lane width (VLANE_W)
- configurable memory interface width (VMEM_W)
- dual pipeline default configuration
- CV-X-IF interface
- supports Zve32x, Zve32f, Zvfh (with pending half-precision FP comparison)
- targets low-cost embedded devices
scorecard:
  novelty_delta: 0.7
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.3
  hub_potential: 0.2
sources:
- raw/cache/bdb6d44d4e2e45a9.md
- https://github.com/vproc/vicuna2_core
source_url: https://github.com/vproc/vicuna2_core
fetched_at: '2026-07-06T02:03:51.860184+00:00'
type: hardware_target
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 1
---

# Vicuna 2.0

Vicuna 2.0 is an upgraded version of the original Vicuna vector co-processor, designed by vproc for inclusion in low-cost embedded RISC-V systems. It attaches to a main scalar core using the Core V eXtension Interface (CV-X-IF), providing vector processing capabilities without requiring a full vector-capable CPU core. The unit supports the ratified RISC-V embedded vector sub-extensions Zve32x (integer), Zve32f (single-precision floating-point), and Zvfh (half-precision floating-point). Its architecture is highly configurable: designers can set the vector register width (VREG_W), datapath lane width (VLANE_W), memory interface width (VMEM_W), and even define custom pipeline configurations with different functional unit placements to eliminate structural hazards. Floating-point operations depend on scalar FP support provided either by the main core or an additional coprocessor on the CV-X-IF interface. The complete RTL is available for integration into other projects, and Verilator simulation is supported via CMake with preprocessor flags to select the target ISA (rv32im_zve32x, rv32imf_zve32f, or rv32imf_zfh_zve32f_zvfh). A publication describing the design and half-precision floating-point support for TinyML applications was presented at Austrochip 2025.

## Key Claims

- Attaches to a main scalar core via the CV-X-IF interface (issue, commit, memory, result interfaces).
- Supports ratified RISC-V extensions Zve32x (vector integer), Zve32f (vector single-precision FP), and Zvfh (vector half-precision FP).
- Vector floating-point support for comparison operations is still in progress.
- Configuration parameters include VREG_W (register width), VLANE_W (datapath lane width), and VMEM_W (memory interface width).
- Default dual-pipeline configuration; custom pipelines can be defined to change functional unit placement and dispatch buffer size.
- CMake-based build integration provides three targets: VICUNA_SRCS, VICUNA_INCS, VICUNA_FLAGS.
- Requires scalar floating-point support (either in-core or on CV-X-IF) for vector FP operations.
- Floating-point rounding mode is taken from the scalar fcsr register via the float_round_mode_i signal.

## Optimization-Relevant Details

- ISA/profile: RISC-V embedded vector extensions Zve32x, Zve32f, Zvfh (subset of RVV 1.0).
- Vector/matrix/accelerator support: Configurable vector register width (VREG_W), datapath lane width (VLANE_W), and memory interface width (VMEM_W). Vector pipelines can be reorganized to move functional units between lanes.
- Memory/cache/TLB/DMA: Not specified; depends on the host scalar core and system architecture.
- Compiler/toolchain support: CMake with preprocessor flags (RISCV_ARCH) for Verilator simulation; RTL is SystemVerilog.

## Relationships

- No specific relationship to visible context pages. Vicuna 2.0 is an independent vector coprocessor design not directly connected to the SpacemiT K3 SoC or its cores.

## Sources

- https://github.com/vproc/vicuna2_core
