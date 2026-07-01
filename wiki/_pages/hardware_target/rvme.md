---
type: hardware_target
canonical_name: RVME
aliases:
- RVME matrix engine
- RVME coprocessor
tags:
- risc-v
- matrix-extension
- accelerator
- gemm
- gem5
hardware_targets:
- RVME
toolchains:
- extended RISC-V GNU toolchain
- extended gem5 simulator
constraints:
- 8x8 Outer Product Array (OPA) size, four OPAs
- Matrix Register File 8KB, RLEN=256-bit
- 32 physical matrix registers
- host CPU 64-bit RISC-V out-of-order, 2 GHz; RVME core 1 GHz
sources:
- raw/sources/RVME_An_Efficient_Matrix_Engine_Design_Based_on_Matrix_Extension_of_RISC-V.pdf
created: 2026-07-01
updated: 2026-07-01
cold_start: true
inbound_links: 5
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.7
needs_summary_revision: true
---

# RVME

RVME (Wanqi Chen et al., Shanghai Jiao Tong University / Alibaba DAMO Academy, IEEE ICCD 2025) is a decoupled matrix-engine coprocessor design for RISC-V CPUs that accelerates General Matrix Multiplication (GEMM) for deep neural network workloads. Rather than integrating a monolithic systolic array (SA), RVME scales out four bubble-free Outer Product Arrays (OPAs), each sized 8x8, that read two Tile Registers as GEMM operands and accumulate results into an Accumulation Register, avoiding the pre-load-stage idle time and inter-PE communication overhead that limit conventional weight-stationary systolic arrays. RVME defines eight architectural matrix registers (m0-m7): four Tile Registers (TR, m0-m3) holding INT8 input matrices A and B, and four Accumulator Registers (AR, m4-m7) holding INT32 output matrix C, all configured via a single `mmacc` (C = C + A x B) instruction plus `mld`/`mst`, element-wise, and `mcfg`/`mzero` configuration instructions. It couples the matrix engine to an out-of-order RISC-V host CPU (Fetch/Decode/Rename/Issue-Execute-Writeback/Commit) via an instruction buffer, a 32-entry physical-register renaming unit, and a reorder buffer, and further introduces a cache-aware, loop-adaptive mapping framework that searches K-inner (Output Stationary), N-inner (Input Stationary), and M-inner (Weight Stationary) loop permutations for Energy-Delay-Product-optimal GEMM tiling across a four-level memory hierarchy (L0 register file, L1 matrix cache, L2 cache, L3 DRAM).

## Key Claims

- RVME's OPA design achieves bubble-free execution when the tile dimension mapped to the OPA (k) is greater than or equal to the tile dimension mapped to the systolic array (m), reducing matrix-MAC latency from 2k+m+n-2 (conventional SA) to k+m.
- The evaluated RVME configuration uses four 8x8 OPAs, a 32-physical-register renaming unit with a reorder buffer for out-of-order execution, an 8KB Matrix Register File (RLEN=256-bit), a 32KB matrix cache (64B cache lines), and a 256KB shared L2 cache, running at 1 GHz behind a 2 GHz 64-bit RISC-V out-of-order host CPU.
- RVME's `mmacc` instruction performs 64x more arithmetic operations than a corresponding RVV `vmacc` instruction, contributing to a >21.7x reduction in total instruction count versus a state-of-the-art RVV-based (RISC-V Vector Extension) vector engine at matched 256-bit VLEN/RLEN datapath width.
- RVME occupies 0.63 mm^2 at 28nm (61.8% matrix cache + shared L2 cache, 24.4% OPAs, 7% Matrix Register File) and draws 0.377W average power under real GEMM workloads (48.5% DRAM, 29.5% matrix/L2 cache, 15.8% OPAs).
- RVME's cache-aware loop-adaptive mapping framework classifies all six GEMM loop permutations into three dataflow families by innermost loop dimension: K-inner (Output Stationary), N-inner (Input Stationary), and M-inner (Weight Stationary), each requiring distinct tile-size search steps (e.g. K-inner: m_step=RLEN/16, n_step=RLEN/8, k_step=full K).
- Pipeline critical-path delay in the RVME OPA design increases by only 3.5% and area by 4.1% relative to the baseline SA implementation, due to added ping-pong partial-sum (psum) registers that let each PE accept a new instruction immediately after completing a MAC without waiting for output.

## Relationships

- [[riscv_matrix_extension_proposal]]: RVME's own matrix ISA extension is described as conforming to the design principles of the "Attached Matrix Extension (AME)" proposal, a separate decoupled tile/accumulator-register RISC-V matrix extension in the same design family as the RISC-V Matrix Specification Proposal (tile registers + accumulation registers, `mcfg`/`mmacc`-style instructions); the two are related but not confirmed identical from this source alone.
- Benchmark comparisons against RVME (RVV vector engine, Eyeriss, TPUv1, Gemmini, MECLA, MX, MACO) are captured in [[rvme_gemm_benchmark_comparison]].

## Sources

- W. Chen, W. Yang, Y. Guo, J. Qiu, R. Wang, J. Jiang, N. Jing, Q. Wang, "RVME: An Efficient Matrix Engine Design Based on Matrix Extension of RISC-V," 2025 IEEE 43rd International Conference on Computer Design (ICCD), pp. 602-609. raw/sources/RVME_An_Efficient_Matrix_Engine_Design_Based_on_Matrix_Extension_of_RISC-V.pdf, pages 1-8.
