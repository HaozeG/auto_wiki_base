---
canonical_name: Tenstorrent Memory Model
aliases:
- Tensix memory model
- TT-Metalium memory
- TT-Metalium Memory Model
- Tenstorrent NoC memory
subtype: null
tags: []
scorecard:
  novelty_delta: 0.6
  claim_density: 0.5
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/a535f5a2e8a09dba.md
- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/tt_metal/advanced_topics/memory_for_kernel_developers.html
source_url: https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/tt_metal/advanced_topics/memory_for_kernel_developers.html
fetched_at: '2026-07-09T11:10:14.430499+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 1
outbound_links:
- target: blackhole
  reason: Blackhole implements the same Tensix memory model; its Tensix tiles contain
    1464 KiB of L1 RAM per tile, consistent with the shared SRAM architecture described
    in this page
---

# Tenstorrent Memory Model

On Tenstorrent processors, memory is organized differently from CPUs and GPUs. Instead of a single address space, memory is addressed by an (x, y, local_address) tuple, reflecting the mesh-based Network-on-Chip (NoC) design where each node has its own local resources. Each Tensix compute core contains 1.5 MB of shared SRAM accessible to all cores on that tile, plus a small private memory region for stack and locals. RISC-V cores can directly access only their private memory and local shared SRAM; accessing memory on other tiles or DRAM requires DMA requests through the NoC. This architecture has performance implications: RISC-V loads/stores to SRAM have limited bandwidth and several cycles of latency, so bulk compute is offloaded to peripherals with higher bandwidth. The memory model is uniform across all NoC tiles—Tensix, Ethernet, DRAM, and PCIe—each accessed via the same tuple scheme.

## Key Claims

- Memory is addressed by an (x, y, local_address) tuple due to the mesh-based NoC design.
- Each Tensix tile has 1.5 MB of shared SRAM (historically called L1).
- RISC-V cores can directly access only their private memory and local shared SRAM; all other memory requires NoC DMA requests.
- RISC-V loads and stores to shared SRAM have limited bandwidth and a latency of several cycles.
- Bulk compute is performed by peripherals (e.g., matrix and vector units) that have much higher bandwidth to SRAM.
- DRAM is accessed through DRAM tiles: Wormhole has 6 DRAM controllers, each connected to 2 GB of GDDR6 memory (2 channels, 1 GB per channel).
- Shared SRAM is always accessible to all cores on the same tile; private memory is isolated per core and not accessible via NoC.
- NoC requests specify the target tile (x, y) and the address within that tile, and can access SRAM, DRAM, or PCIe memory.

## Relationships

- [[blackhole]]: Blackhole implements the same Tensix memory model; its Tensix tiles contain 1464 KiB of L1 RAM per tile, consistent with the shared SRAM architecture described in this page.

## Sources

- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/tt_metal/advanced_topics/memory_for_kernel_developers.html
