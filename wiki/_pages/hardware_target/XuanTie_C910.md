---
cold_start: true
constraints:
- 3-wide out-of-order superscalar
- 12-stage pipeline
- RVV 0.7.1 (pre-ratification)
- 64 KB 2-way set-associative L1 instruction cache
- FIFO replacement for L1i
- 16-entry fully-associative L0 BTB
- 1024-entry 4-way set-associative main BTB
- 22-bit global history bi-mode predictor (17.3 KB storage)
- 12-entry return stack
- 256-entry indirect target array
- 32-entry instruction queue + 16-entry loop buffer
- L1 data cache (not detailed in source)
- Shared 1 MB L2 cache in quad-core cluster
- 'Reorder buffer: up to 192 entries (64 defined in RTL, 192 per microbenchmark)'
- Physical register file (PRF) based OoO
- 'Core area: 0.8 mm² on TSMC 12nm'
- 'Dynamic power: ~100 microwatts/MHz (~0.2W at 2 GHz, core only)'
- 'Frequency: 2.0–2.5 GHz on TSMC 12nm (nominal), 2.8 GHz on TSMC 7nm'
- 'Core voltage: 0.8V at 2 GHz, 1.0V at 2.5 GHz'
created: '2025-03-15'
hardware_targets:
- XuanTie C910
- TH1520
- LicheePi
inbound_links: 3
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://chipsandcheese.com/p/alibabat-heads-xuantie-c910
tags:
- RISC-V
- T-HEAD
- out-of-order
- RVV
- Alibaba
- XuanTie
- C910
toolchains:
- Xuantie-900-gcc (vendor)
- gcc
type: hardware_target
updated: '2026-06-28'
---

# XuanTie C910

The XuanTie C910 is a 3-wide out-of-order RISC-V processor core designed by T-HEAD, a wholly owned subsidiary of Alibaba. It implements the RISC-V Vector Extension version 0.7.1 (pre-ratification), supporting masking and variable vector length, making it an early adopter of vector capabilities. The core targets high-performance applications including AI inference, edge servers, industrial control, and advanced driver-assistance systems (ADAS). Fabricated on TSMC's 12nm FinFET process, the C910 occupies 0.8 mm² per core and operates at 2.0 to 2.5 GHz with a dynamic power of approximately 100 microwatts/MHz, translating to roughly 0.2W at 2 GHz for the core only. On TSMC's 7nm process, frequency reaches 2.8 GHz. The core is organized in clusters of up to four cores sharing a 1 MB L2 cache and is integrated into the TH1520 system-on-chip used on the LicheePi single-board computer. T-HEAD has open-sourced the RTL code and subsequently released the C920 core with RVV 1.0 support while keeping the C910 microarchitecture unchanged.

## Key Claims

- The XuanTie C910 is a 3-wide out-of-order core with a 12-stage pipeline.
- Instruction cache: 64 KB, 2-way set-associative with FIFO replacement policy, storing 4 bits of predecode data per 16-bit slot (83.7 KB raw storage total).
- Branch predictor: bi-mode predictor with a 1024-entry selection table, two 16384-entry history tables, and a 22-bit global history register; approximately 17.3 KB storage.
- BTB: 1024 entries, 4-way set-associative.
- Frontend sustains 3 instructions per cycle from L1i; L2 code bandwidth under 1 IPC.
- Frontend: 16-entry fully-associative L0 BTB; 32-entry instruction queue; 16-entry loop buffer.
- Decode stage: 3-wide primary decoder, up to 4 micro-ops per cycle total; first slot handles complex instructions (4+ micro-ops).
- Rename stage: 4-wide; no decode-to-rename queue.
- Reorder buffer: 192 entries (per microbenchmark), 64 entries defined in RTL (ct_rtu_rob.v).
- Physical register file (PRF) based out-of-order execution.
- Core voltage scaling: 0.8V at 2 GHz, 1.0V at 2.5 GHz.
- L2 cache: 1 MB shared across quad-core cluster in TH1520.
- RVV 0.7.1 support with masking and variable vector length; C920 later moves to RVV 1.0.

## Optimization-Relevant Details

- ISA/profile: RV64GCV with RVV 0.7.1 (pre-1.0, incompatible with v1.0).
- Vector/matrix/accelerator support: RVV 0.7.1 vector extension; no custom accelerator interface discussed in source.
- Memory/cache/TLB/DMA: 64 KB L1 instruction cache (2-way, FIFO), L1 data cache details not provided; 1 MB shared L2; memory controller via LPDDR4X-3733 on TH1520.
- Compiler/toolchain support: Vendor Xuantie-900-gcc supports RVV 0.7.1 intrinsics; mainline GCC/LLVM support for RVV 0.7.1 is limited.

## Relationships

- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – SPEC benchmark results for the same core on a Lichee Module 4A board, providing measured performance data.
- [[XuanTie_C906]] – Another T-HEAD core (in-order, RVV 0.7.1) featuring a lower-power design; both implement the pre-ratification vector extension.
- [[fpga-sdv_RISC-V_Vector_Cluster]] – An FPGA-based RVV 0.7 platform with a vector unit; shares the same vector extension revision as C910.
- [[Sipeed_MAIX_series]] – A RISC-V AI/edge platform using the Kendryte K210, representing a different market segment with no vector extension.

## Sources

- [Alibaba/T-HEAD's Xuantie C910 – Chips and Cheese (Chester Lam)](https://chipsandcheese.com/p/alibabat-heads-xuantie-c910)
