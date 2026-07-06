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

Sophon SG2380 (codename Oasis) is an upcoming high-performance RISC-V SoC designed for AI PC (AIPC) applications, jointly developed by Sophgo, SiFive, and Imagination Technologies. It features 16 SiFive RISC-V P670 processor cores in a big.LITTLE configuration (12 big cores and 4 little cores) running at 2.5 GHz, paired with an Imagination AXT-16-512 GPU supporting Vulkan 1.3, OpenGL ES 3.3/2.0/1.1, and OpenCL 3.0, and a dedicated Sophgo TPU delivering 20 TOPS or 32 TOPS at INT8 and 16 TFLOPs at FP16 precision via a SiFive Intelligence X280 AI accelerator with 512-bit vector registers and a VCIX interface. The SoC features a 256-bit DDR memory interface supporting up to 128 GB of memory with 200 GB/s bandwidth, along with PCIe Gen4 and USB 3.2 Gen2 connectivity. It is designed to run generative AI workloads such as LLaMA-2 13B locally for tasks like natural language processing, image generation, and text generation. The processor is intended to compete with Arm A78-class devices such as the Rockchip RK3588 and Raspberry Pi 5, offering higher core count and performance. Test chips were expected in September 2023, with a desktop-class mini-ITX motherboard planned for H2 2024 at a $120 price point. The SG2380 also supports the OpenXLA framework for AI development.

## Key Claims

- 2.5 GHz clock speed on all 16 SiFive P670 cores (12 big + 4 little).
- 20 TOPS AI accelerator (via SiFive Intelligence X280 and Sophgo TPU with VCIX interface).
- 32 TOPS (INT8) and 16 TFLOPs (FP16) from the Sophgo TPU.
- Imagination AXT-16-512 GPU with support for Vulkan 1.3, OpenGL ES 3.3/2.0/1.1, and OpenCL 3.0.
- 256-bit DDR interface supporting up to 128 GB of memory with 200 GB/s bandwidth.
- Connectivity includes PCIe Gen4 and USB 3.2 Gen2.
- Video decode resolution up to 8192x4320.
- Performance comparable to Arm A78 cores, a step ahead of RK3588 and Raspberry Pi 5.
- Capable of running LLaMA-2 13B model locally for GenAI tasks.
- Planned $120 mini-ITX motherboard in H2 2024.
- Test chips due September 2023.

## Optimization-Relevant Details

- ISA/profile: RISC-V (SiFive P670 supports RV64GC, likely with V extension and custom TPU instructions; the P670 cores implement RISC-V standard extensions).
- Vector/matrix/accelerator support: SiFive Intelligence X280 with 512-bit vector registers and VCIX interface; Sophgo TPU provides 20 TOPS (unspecified precision) and 32 TOPS (INT8) / 16 TFLOPs (FP16) for matrix multiplication; the X280 provides RVV 1.0 vector processing.
- Memory/cache/TLB/DMA: 256-bit DDR interface up to 128 GB, 200 GB/s; specific cache hierarchy and TLB details not disclosed in sources.
- Compiler/toolchain support: OpenXLA framework.

## Relationships

No specific relationship to the visible context page (Andes AX45MPV) beyond both being RISC-V processor designs for AI acceleration; they originate from different vendors and use distinct microarchitectures. [[andes-ax45mpv-hardware-target]] is a different vendor's core IP (Andes Technology) targeting a different market (data-intensive computing) and does not share a common architecture, vendor, or ecosystem with the Sophon SG2380.

## Sources

- https://news.ycombinator.com/item?id=40141776
- https://www.cnx-software.com/2024/05/20/sophgo-sg2380-a-2-5-ghz-16-core-sifive-p670-risc-v-processor-with-a-20-tops-ai-accelerator/
- https://ee.ofweek.com/2024-04/ART-8320315-8220-30631334.html
