---
cold_start: true
constraints:
- RVA23 profile
- RVV 1.0
- 1024-bit vector length
- LPDDR5
created: '2026-06-30'
hardware_targets:
- Milk-V Jupiter2
- SpacemiT K3 (RVA23)
inbound_links: 0
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://milkv.io/jupiter2
tags:
- RISC-V
- Spacemit K3
- Milk-V
- Jupiter2
- development platform
toolchains:
- GCC (RISC-V)
- LLVM (RISC-V)
type: hardware_target
updated: '2026-06-29'
---

# Milk-V Jupiter2

The Milk-V Jupiter2 is a RISC-V development platform and mini PC powered by the Spacemit K3 (RVA23) SoC, featuring an 8-core X100 CPU clocked up to 2.4GHz. It provides up to 60 TOPS of AI performance through 1024-bit RVV 1.0 vector acceleration and includes an Imagination BXM-4-64-MC1 GPU for graphics output. The board supports up to 32GB of LPDDR5 memory, onboard UFS storage up to 256GB, and an M.2 NVMe slot (PCIe Gen3 x4) for additional storage. Connectivity options include 10GbE SFP+, Gigabit Ethernet RJ45, Wi-Fi 6 and Bluetooth 5.2, as well as an M.2 B Key with Nano SIM slot for 4G/5G cellular expansion. The Jupiter2 is available as a pre-assembled mini PC with an aluminum enclosure and active cooling, targeting desktop and edge AI workloads. Pre-orders opened in May 2026 at a price of $300.

## Key Claims

- Powered by Spacemit K3 (RVA23) SoC with 8-core X100 CPU at up to 2.4GHz.
- AI performance up to 60 TOPS via 1024-bit RVV 1.0 vector acceleration.
- Imagination BXM-4-64-MC1 GPU for graphics.
- Up to 32GB LPDDR5 memory.
- Onboard UFS storage up to 256GB, plus M.2 NVMe slot (PCIe Gen3 x4).
- 10GbE SFP+, GbE RJ45, Wi-Fi 6, Bluetooth 5.2.
- M.2 B Key + Nano SIM for 4G/5G expansion.
- Pre-orders at $300 starting May 2026.
- Includes aluminum enclosure and active cooling.

## Optimization-Relevant Details

- **ISA/profile:** RVA23 profile, RVV 1.0 with up to 1024-bit vector length.
- **Vector/matrix/accelerator support:** 1024-bit RVV 1.0 vector acceleration for AI; Imagination BXM-4-64-MC1 GPU.
- **Memory/cache/TLB/DMA:** Up to 32GB LPDDR5; onboard UFS up to 256GB; PCIe Gen3 x4 for NVMe.
- **Compiler/toolchain support:** Standard RISC-V toolchains (GCC, LLVM) supporting RVV 1.0.

## Relationships

Insufficient context for additional cross-links (no entity pages available in the provided wiki context). Related pages in context include [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] and [[Tenstorrent_Grayskull_MatMul_Efficiency]], which provide comparative AI performance benchmarks on RISC-V hardware.

## Sources

- [Milk-V Jupiter2 official product page](https://milkv.io/jupiter2)
- Additional search snippets from Milk-V Jupiter2 promotional materials and pre-order announcements.
