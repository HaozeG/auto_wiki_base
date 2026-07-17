---
canonical_name: High Bandwidth Memory
aliases:
- HBM
- High Bandwidth Memory (HBM)
subtype: memory_architecture
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.8
sources:
- raw/cache/b2570c7de3abbced.md
- https://en.wikipedia.org/wiki/High_Bandwidth_Memory
source_url: https://en.wikipedia.org/wiki/High_Bandwidth_Memory
fetched_at: '2026-07-17T11:20:06.111374+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# High Bandwidth Memory

High Bandwidth Memory (HBM) is a computer memory interface for 3D-stacked synchronous dynamic random-access memory (SDRAM) initially developed by Samsung, AMD, and SK Hynix. It is used in performance-oriented graphics accelerators, network devices, FPGAs, and ASICs, and some CPUs utilize HBM as on-package cache or RAM, such as the NEC SX-Aurora TSUBASA and Fujitsu A64FX. The first HBM memory chip was produced by SK Hynix in 2013, and the first devices shipped with HBM were the AMD Fiji GPUs in 2015. HBM was adopted by JEDEC as an industry standard in October 2013, with subsequent generations including HBM2 (January 2016), HBM2E (August 2019), HBM3 (January 2022), HBM3E (May 2023), and HBM4 (April 2025). The technology achieves higher bandwidth than DDR4 or GDDR5 while using less power and in a substantially smaller form factor, accomplished by stacking up to 32 DRAM dies with through-silicon vias (TSVs) and microbumps, often connected to a memory controller through a silicon interposer. The major manufacturers in 2025 include SK Hynix, Samsung Electronics, and Micron Technology.

## Key Claims

- HBM is a JEDEC-standard 3D-stacked SDRAM interface, with HBM1 standardized in October 2013.
- HBM1 provides 128 GB/s bandwidth per stack (1024-bit bus, 1 GT/s per pin, 4 dies max).
- HBM2 doubles pin transfer rate to 2 GT/s, reaching 256 GB/s per stack, with up to 8 GB per package.
- HBM2E supports up to 307 GB/s per stack and 12-die stacks.
- HBM3 (January 2022) provides up to 819 GB/s per stack (6.4 Gb/s per pin, 16-bit channels).
- HBM3E (May 2023) increases to 9.8 Gb/s per pin, up to 1229 GB/s per stack, and 48 GB per stack.
- HBM4 (April 2025) achieves 8 Gb/s per pin with a 2048-bit bus, 2 TB/s per stack, and up to 64 GB per stack.
- The memory bus is very wide: an HBM1 stack has 8 channels of 128 bits each, total 1024 bits; four such stacks yield a 4096-bit interface.
- HBM uses through-silicon vias (TSVs) and microbumps for vertical die interconnection.
- A silicon interposer is commonly used to connect HBM stacks to the processor die.
- TSMC produces the base die for HBM and plans to be the foundry for several HBM companies in 2026.
- In early 2026, HBM demand has driven DRAM price increases exceeding 200%, with Micron noting a 3-to-1 wafer capacity conversion ratio between HBM and DDR5.

## Relationships

- HBM is used as the memory subsystem in [[amd_gpu_architecture]]; the AMD GPU architecture page references HBM2 as a constraint on memory capacity.
- HBM technology is similar in principle to but incompatible with the Hybrid Memory Cube (HMC) interface developed by Micron.

## Sources

- [High Bandwidth Memory - Wikipedia](raw/cache/b2570c7de3abbced.md)
