---
canonical_name: ET-SoC-1
aliases:
- Esperanto ET-SoC-1
- Esperanto Technologies ET-SoC-1
subtype: null
tags: []
hardware_targets:
- ET-SoC-1
toolchains: []
constraints: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/75a78991629076f1.md
- https://www.researchgate.net/publication/357611149_Accelerating_ML_Recommendation_with_over_a_Thousand_RISC-VTensor_Processors_on_Esperantos_ET-SoC-1_Chip
source_url: https://www.researchgate.net/publication/357611149_Accelerating_ML_Recommendation_with_over_a_Thousand_RISC-VTensor_Processors_on_Esperantos_ET-SoC-1_Chip
fetched_at: '2026-07-02T11:57:08.943875+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# ET-SoC-1

The ET-SoC-1 is a RISC-V based system-on-chip designed by Esperanto Technologies for accelerating machine learning recommendation workloads. Fabricated in TSMC 7nm technology with over 24 billion transistors, the chip integrates 1088 64-bit ET-Minion RISC-V processors for ML computation, four 64-bit ET-Maxion high-performance RISC-V processors for operating system and control tasks, and a single service processor. It features over 160 MB of on-die memory, LPDDR4x DRAM controllers for up to 32 GB of external memory, and eight lanes of PCIe Gen4 for host communication. The chip is designed to deliver peak performance between 100 and 200 TOPS while consuming under 20 watts, making it suitable for energy-constrained datacenter accelerator cards.

## Key Claims

- Integrates 1088 ET-Minion and 4 ET-Maxion RISC-V processors on a single chip.
- Fabricated in TSMC 7nm with over 24 billion transistors.
- Peak performance of 100-200 TOPS depending on operating frequency.
- Total power consumption under 20 watts.
- Over 160 MB of on-die memory and up to 32 GB external LPDDR4x memory.
- PCIe Gen4 x8 interface for host connectivity.
- Preliminary projections indicate over 100x better performance per watt compared to standard x86 servers on the MLPerf Deep Learning Recommendation Model benchmark.

## Optimization-Relevant Details

- ISA/profile: RISC-V RV64GC (with custom extensions for tensor processing)
- Vector/matrix/accelerator support: 1088 ET-Minion processors with tensor processing capabilities; hardware support for int8, fp16, and fp32 data types.
- Memory/cache/TLB/DMA: Over 160 MB on-die memory; LPDDR4x memory controllers; distributed on-die memory system.
- Compiler/toolchain support: Not specified in source.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: This optimization recipe targets Gemmini systolic arrays; ET-SoC-1 uses a different approach with many RISC-V cores but shares the goal of ML acceleration.
- [[earth-shifting-based-vector-memory-access]]: The EARTH optimization targets RISC-V vector memory access; ET-SoC-1's ET-Minion processors likely benefit from similar vector memory optimizations.

## Sources

- David Ditzel et al., "Accelerating ML Recommendation with over a Thousand RISC-V/Tensor Processors on Esperanto's ET-SoC-1 Chip," IEEE Micro, January 2022. DOI: 10.1109/MM.2022.3140674.
