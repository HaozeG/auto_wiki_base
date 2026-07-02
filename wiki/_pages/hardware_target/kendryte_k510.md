---
canonical_name: Kendryte K510
aliases:
- K510
- Canaan Kendryte K510
- Kendryte K510 SoC
- Kendryte K510 processor
subtype: hardware_target
tags:
- K510
- Kendryte
- Canaan
- RISC-V
hardware_targets:
- Kendryte K510
toolchains: []
constraints:
- tri-core RISC-V 64-bit
- 3 TOPS NPU
- FPU support
- DSP core
scorecard:
  novelty_delta: 0.6
  claim_density: 0.3
  self_containedness: 0.7
  bridge_score: 0.4
  hub_potential: 0.3
sources:
- raw/cache/8012072136744f51.md
- https://www.electronics-lab.com/kendryte-k510-is-tri-core-risc-v-processor-for-edge-ai-applications/
source_url: https://www.electronics-lab.com/kendryte-k510-is-tri-core-risc-v-processor-for-edge-ai-applications/
fetched_at: '2026-07-02T07:08:16.408885+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# Kendryte K510

The Kendryte K510 is a 64-bit tri-core RISC-V processor designed for edge AI applications, announced by Canaan Inc. as the successor to the Kendryte K210. It features two RISC-V cores clocked at up to 800 MHz and a third core configured as a digital signal processor (DSP), all with floating-point units (FPUs). The chip integrates a neural processing unit (NPU) capable of 3 TOPS (trillion operations per second), representing a threefold improvement in NPU performance over the K210, alongside a doubling of clock speed. The K510 targets edge AI tasks such as computer vision, intelligent sensing, and multimedia processing, leveraging the tri-core architecture to separate application processing and DSP workloads.

## Key Claims

- 64-bit tri-core RISC-V processor with FPUs, split into a dual-core block at 800 MHz and a single-core DSP block.
- NPU delivering 3 TOPS performance.
- Succeeds the Kendryte K210 dual-core RISC-V processor (400 MHz).
- Designed for edge AI applications with emphasis on compute upgrade per claim of "twice the clock speed, three times the NPU performance".

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit (specific extensions not disclosed in public snippets).
- Vector/matrix/accelerator support: NPU (3 TOPS), FPU per core.
- Memory/cache/TLB/DMA: Not specified in available sources.
- Compiler/toolchain support: Not specified; presumably standard RISC-V toolchains are applicable.

## Relationships

- The Kendryte K510 is from the same Canaan Inc. product family as the [[k230]], though the K230 integrates a different core configuration (two C908 cores) and a Knowledge Process Unit.
- The [[xuantie_c908]] is a comparable RISC-V AI accelerator core used in other Canaan designs; the K510's architecture offers a different balance of general-purpose cores and DSP capability.
- [[kendryte_k210]]: the predecessor SoC this chip succeeds, offering a dual-core RISC-V design with a 1 TOPS NPU versus the K510's tri-core, 3 TOPS design.

## Sources

- https://www.electronics-lab.com/kendryte-k510-is-tri-core-risc-v-processor-for-edge-ai-applications/
