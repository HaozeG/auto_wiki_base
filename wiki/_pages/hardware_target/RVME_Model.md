---
cold_start: true
constraints:
- Systolic array connection
- SRAM Occupy Mechanism
- Support for Xuantie MME v0.3 instructions
- Compute Unit Array computes one sub-matrix (partial sum) per cycle
- Automatically converts second matrix operator (mb) into transpose format
created: '2025-03-04'
hardware_targets:
- RVME (gem5 microarchitectural model)
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.7
  hub_potential: 0.4
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://github.com/superboy999/RVME/blob/main/README.md
tags:
- RISC-V
- matrix engine
- gem5
- simulation
toolchains:
- gem5
type: hardware_target
updated: '2026-06-29'
---

# RVME Model

RVME (RISC-V Matrix Engine) is a detailed microarchitectural model designed to accelerate matrix operations on RISC-V, based on the matrix extension defined in Xuantie MME v0.3. The model is implemented as an extension to the gem5 simulator, providing a simulation environment for evaluating matrix multiplication, store-load, and configuration instructions. The compute array originally used a direct sub-matrix computation where each compute unit produced one partial sum per cycle, and was later upgraded to a systolic array connection for improved dataflow. The design includes SRAM occupy mechanisms for read operations and a Memchecker for memory system verification. RVME supports both integer and signed/unsigned data types in its buffer memories, and is described in a paper accepted by ICCD 2025 titled "RVME: An Efficient Matrix Engine Design Based on Matrix Extension of RISC-V."

## Key Claims

- RVME is a microarchitectural model for the RISC-V matrix extension, built on the gem5 simulator.
- Supports instructions from the Xuantie MME v0.3 specification.
- Compute Unit Array initially ran as a non-systolic array computing one sub-matrix partial sum per cycle, then transitioned to a systolic array connection.
- Automatically converts the second matrix operand (mb) to its transpose format.
- Implements SRAM Occupy Mechanism for read operations and write protection via RAT.
- Matrix memory operations use unsigned integers; X/Y/Z Buffers support int or uint via static_cast.
- Bug fixes for accessing large data, especially full cache lines.
- Repository provides both debug and optimized build options for gem5.

## Optimization-Relevant Details

- ISA/profile: RISC-V with matrix extension (Xuantie MME v0.3).
- Vector/matrix/accelerator support: Matrix engine with compute unit array (systolic).
- Memory/cache/TLB/DMA: SRAM occupy mechanism, Memchecker, full cache-line access supported.
- Compiler/toolchain support: gem5 simulator with SCons build system; debugging via GDB.

## Relationships

- [[Gemmini_Architecture]] – Another RISC-V DNN accelerator generator, provides contrast in matrix acceleration approach (systolic vs. vector).
- [[GEMM_with_RISC-V_Vector_Extension]] – A workload kernel performing matrix multiplication using RISC-V vector extensions; related to the matrix operations RVME targets.

## Sources

- [GitHub Repository: superboy999/RVME](https://github.com/superboy999/RVME/blob/main/README.md)
