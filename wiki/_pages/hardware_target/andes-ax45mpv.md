---
canonical_name: AX45MPV
aliases:
- Andes AX45MPV
- Andes AX45MPV core
subtype: null
tags: []
hardware_targets:
- AX45MPV
toolchains:
- GCC (RISC-V toolchain)
constraints:
- In-order dual-issue scalar pipeline
- Vector unit up to 1024-bit, default VLEN=DLEN=512
- RISC-V Vector Extension (RVV) support
- AndeSim near-cycle-accurate microarchitecture simulator
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.4
sources:
- raw/cache/cf4003729a4c4c3b.md
- https://camel-cdr.github.io/rvv-bench-results/andesim_ax45mpv/index.html
source_url: https://camel-cdr.github.io/rvv-bench-results/andesim_ax45mpv/index.html
fetched_at: '2026-07-02T11:47:40.122491+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 2
---

# AX45MPV

The Andes AX45MPV is an in-order dual-issue RISC-V core from Andes Technology that supports a vector unit configurable up to 1024 bits. Its default configuration, as used in publicly available simulation-based benchmarks, sets both vector length (VLEN) and datapath width (DLEN) to 512 bits. The core was evaluated on the AndeSim near-cycle-accurate microarchitecture simulator, which models the CPU pipeline, caches, and memory hierarchy to provide cycle-level performance estimates. Instruction throughput measurements for a wide range of RISC-V Vector Extension (RVV) operations have been published, covering multiple LMUL and SEW settings, making this one of the first publicly documented microarchitectural performance references for the AX45MPV.

## Key Claims

- The AX45MPV is an in-order dual-issue core with a vector unit supporting up to 1024-bit vector operations.
- The default configuration uses VLEN=DLEN=512.
- Published benchmarks include throughput for many RVV instructions (vadd, vsub, vmul, vmin, vmax, etc.) under varying LMUL and SEW.
- Instruction throughput for vadd.vv is 1.0 cycles per iteration at LMUL=1 across all SEW, scaling linearly with LMUL.
- Scalar integer add (add) achieves 0.57-0.69 cycles per instruction depending on LMUL.

## Optimization-Relevant Details

- ISA/profile: RV64GC + RISC-V Vector Extension (RVV)
- Vector/matrix/accelerator support: Vector unit with VLEN configurable up to 1024 bits, default 512.
- Memory/cache/TLB/DMA: Simulator models caches; specific sizes not detailed.
- Compiler/toolchain support: Benchmarks compiled with GCC for RISC-V (assumed from context).

## Relationships

- [[earth-shifting-based-vector-memory-access]]: EARTH is a microarchitectural optimization for vector memory access that could potentially be applied to the AX45MPV's vector unit to improve memory performance.
- [[vectrans]]: VecTrans is an LLM-assisted auto-vectorization framework that could target the AX45MPV's RVV support to improve compiler-generated vector code.

## Sources

- [RVV benchmark AX45MPV](https://camel-cdr.github.io/rvv-bench-results/andesim_ax45mpv/index.html)
