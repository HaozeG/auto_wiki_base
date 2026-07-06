---
canonical_name: Sophon SG2380
aliases:
- Sophgo SG2380
- SG2380
- SOPHON SG2380
- Oasis
- Sophgo SG2380 SoC
subtype: null
tags: []
hardware_targets:
- Sophon SG2380
- SiFive P670
- SiFive Intelligence X280
toolchains:
- OpenXLA
constraints:
- 2.5 GHz
- 16 cores (SiFive P670)
- 20 TOPS AI accelerator (X280 + Sophgo TPU)
- VCIX interface for custom vector coprocessors
- 512-bit vector registers (X280)
- Planned mini-ITX motherboard at ~$120
scorecard:
  novelty_delta: 0.8
  claim_density: 0.4
  self_containedness: 0.7
  bridge_score: 0.2
  hub_potential: 0.5
sources:
- raw/cache/b5a4d7e39b6b09ea.md
- https://news.ycombinator.com/item?id=40141776
- raw/cache/c842ce1854e7aa64.md
- https://ee.ofweek.com/2024-04/ART-8320315-8220-30631334.html
- raw/cache/dfecae48d49f0bba.md
- https://www.cnx-software.com/2023/10/21/sophgo-sg2380-16-core-sifive-p670-risc-v-processor-20-tops-ai-accelerator/
source_url: https://news.ycombinator.com/item?id=40141776
fetched_at: '2026-07-06T01:54:17.589096+00:00'
type: hardware_target
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
---

# Sophon SG2380

Sophon SG2380 is an upcoming 2.5 GHz 16-core RISC-V processor developed by Sophgo, based on SiFive Performance P670 cores. It integrates a SiFive Intelligence X280 AI accelerator with 512-bit vector registers and a VCIX interface that connects a Sophgo TPU, delivering 20 TOPS of AI performance. The processor is designed to compete with Arm A78-class devices such as the Rockchip RK3588 and Raspberry Pi 5, offering higher core count and performance. Test chips were expected in September 2023, with a desktop-class mini-ITX motherboard planned for H2 2024 at a $120 price point. The SG2380 also supports the OpenXLA framework for AI development.

## Key Claims

- 2.5 GHz clock speed on all 16 SiFive P670 cores.
- 20 TOPS AI accelerator via SiFive Intelligence X280 and Sophgo TPU with VCIX interface.
- Performance comparable to Arm A78 cores, a step ahead of RK3588 and Raspberry Pi 5.
- Multi-cluster, multi-core configuration with 12 large and 4 small cores.
- Planned $120 mini-ITX motherboard in H2 2024.
- Test chips due September 2023.

## Optimization-Relevant Details

- ISA/profile: RISC-V (SiFive P670 supports RV64GC, likely with V extension)
- Vector/matrix/accelerator support: SiFive Intelligence X280 with 512-bit vector registers and VCIX interface; Sophgo TPU provides 20 TOPS
- Memory/cache/TLB/DMA: Not specified in available sources
- Compiler/toolchain support: OpenXLA framework

## Relationships

No specific relationship to the visible context page (Andes AX45MPV) beyond both being RISC-V processor designs for AI acceleration; they originate from different vendors and use distinct microarchitectures.

## Sources

- https://news.ycombinator.com/item?id=40141776
- https://www.cnx-software.com/2024/05/20/sophgo-sg2380-a-2-5-ghz-16-core-sifive-p670-risc-v-processor-with-a-20-tops-ai-accelerator/
