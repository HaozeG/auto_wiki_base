---
canonical_name: AX45MPV
aliases:
- AndesCore AX45MPV
- Andes AX45MPV
- AX45MPV RISC-V core
subtype: null
tags:
- RISC-V
- vector processor
- Andes Technology
hardware_targets:
- AX45MPV
toolchains: []
constraints:
- in-order dual-issue 8-stage pipeline
- up to 1024-bit Vector Processing Unit (VPU)
- symmetric multiprocessing up to 8 cores
- RISC-V Vector Extension (implied)
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.5
sources:
- raw/cache/e59a215ca9c55e2c.md
- https://www.andestech.com/en/products-solutions/andescore-processors/riscv-ax45mpv/
source_url: https://www.andestech.com/en/products-solutions/andescore-processors/riscv-ax45mpv/
fetched_at: '2026-07-02T04:51:47.308608+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# AndesCore AX45MPV

The AndesCore AX45MPV is a 64-bit in-order dual-issue 8-stage RISC-V CPU core developed by Andes Technology, incorporating a powerful Vector Processing Unit (VPU) with a maximum vector length (VLEN) and data path width (DLEN) of 1024 bits. It supports symmetric multiprocessing configurations of up to 8 cores, making it suitable for data-intensive compute workloads. The VPU provides rich single-instruction-multiple-data (SIMD) capabilities for operations on large arrays, targeting applications such as computer vision, digital signal processing, image processing, machine learning and deep learning inference, ADAS, AR/VR, cryptography, multimedia processing, and scientific computing. The core is designed for SoC integration in the AI and high-performance embedded markets. Andes Technology publicly demonstrated an AX45MPV-based FPGA prototype booting a lightweight large language model (LLM) inference workload at an industry conference, indicating early enablement of real-world software stacks. Detailed cache hierarchy, memory subsystem, and specific RISC-V profile version (e.g., RV64GCV) are not disclosed in public materials, but the VPU confirms support for the RISC-V Vector Extension.

## Key Claims

- 64-bit in-order dual-issue 8-stage pipeline.
- VPU with up to 1024-bit VLEN and DLEN.
- Symmetric multiprocessing support for up to 8 cores.
- Target applications include AI inference/training, ADAS, AR/VR, computer vision, cryptography, multimedia, and signal processing.
- A lightweight LLM inference demo on FPGA was shown at a 2025 Andes RISC-V Conference.
- Publicly announced in December 2022 with continued updates through 2026.

## Optimization-Relevant Details

- ISA/profile: RISC-V architecture (exact base profile not specified; VPU implies Vector Extension support).
- Vector/matrix/accelerator support: 1024-bit VPU with VLEN=DLEN up to 1024 bits, providing wide SIMD execution for vector operations.
- Memory/cache/TLB/DMA: Not specified in public materials.
- Compiler/toolchain support: Not specified; expected support from standard RISC-V toolchains (GCC/LLVM) with vector extension support.

## Relationships

- [[xuantie_c908]]: A comparable RISC-V core with configurable 128/256-bit vector width, representing a different design point in the RISC-V vector processor landscape (smaller vector width, different vendor).
- [[k230]]: A RISC-V SoC integrating the XuanTie C908 core, serving as an example of how RISC-V vector cores are used in real AIoT products; the AX45MPV targets similar application spaces.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: An optimization recipe for generating vector code using MLIR/xDSL; the AX45MPV's 1024-bit VPU is a potential target for such code generation techniques.

## Sources

- https://www.andestech.com/en/products-solutions/andescore-processors/riscv-ax45mpv/
- https://www.eetimes.com/andes-announces-risc-v-multicore-1024-bit-vector-processor/
- https://riscv.org/blog/enabling-risc-v-ai-innovations-with-andes-ax45mpv-running-llm-on-fpga/
