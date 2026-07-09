---
canonical_name: TT-QuietBox 2
aliases:
- QuietBox 2
- Tenstorrent QuietBox 2
- TT-QuietBox 2 Blackhole
- Quietbox 2
- QB2
- Tenstorrent Quietbox 2
- Tenstorrent TT-QuietBox 2
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 1.0
  bridge_score: 0.7
  hub_potential: 0.5
sources:
- raw/cache/853b5c87a9eec8a0.md
- https://www.storagereview.com/news/tenstorrent-quietbox-2-brings-risc-v-ai-inference-to-the-desktop
- raw/cache/3f95e2288cb95e56.md
- https://docs.tenstorrent.com/tt-quietbox2-guide/
- raw/cache/0ec2ac1c9d35521d.md
- https://wccftech.com/tenstorrent-tt-quietbox-2-risc-v-ai-workstation-128-gb-memory-liquid-cooling-9999-usd/
source_url: https://www.storagereview.com/news/tenstorrent-quietbox-2-brings-risc-v-ai-inference-to-the-desktop
fetched_at: '2026-07-09T11:12:45.444855+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 1
outbound_links:
- target: tt-xla-performance-optimization-techniques
  reason: The QuietBox 2 leverages the Forge compiler toolchain and TT-Metalium low-level
    SDK, which include the TT-XLA optimization techniques documented for single-chip
    Tenstorrent hardware. These techniques are applicable to optimizing model performance
    on the QuietBox 2's Blackhole ASICs
- target: tt-metalium
  reason: The QuietBox 2's pre-installed TTNN Python library is the high-level operator
    API built on TT-Metalium.
- target: tt-forge
  reason: The QuietBox 2 ships with a pre-installed TT-Forge/XLA container wrapper
    used to compile models onto its Blackhole chips.
---

# TT-QuietBox 2

TT-QuietBox 2 (also branded as QuietBox 2 or Blackhole) is a liquid-cooled AI workstation introduced by Tenstorrent in March 2026, designed for on-premises inference of models up to 120 billion parameters. It is powered by the RISC-V architecture and combines four Blackhole ASICs arranged on two p300c cards, each integrating 16 RISC-V big cores and Tensix compute cores, providing a total of 480 Tensix cores running at 1.35 GHz and 720 MB of on-chip SRAM (180 MB per chip). The system delivers 2,654 TFLOPS at BlockFP8 precision, with 128 GB of GDDR6 memory (32 GB per chip, 1,024 GB/s per card bandwidth) and 256 GB of DDR5-5600 system memory. The chips are interconnected via Warp400 links using Samtec ARP6 connectors. The host system includes an AMD Ryzen 7 9700X (8 cores, 3.8 GHz), a 4 TB NVMe PCIe Gen5 storage drive, and runs Ubuntu 24.04.3 LTS. The QB2 ships with a fully open-source software stack including TT-Forge for graph compilation, TT-Metalium for low-level kernel control, and TT-LLK for hardware-level software, and comes pre-loaded with the Qwen3-32B model. It is intended for lab, office, and small-business environments, requiring only a standard 120V wall outlet, with a peak power draw of approximately 1,500 W from a 1,600 W PSU. Liquid cooling keeps maximum acoustic noise at 38 dBA. Pre-integrated workloads include large language models, image generation, video synthesis, and biomolecular prediction; supported models include Llama-3.1-8B, Llama-3.3-70B, Qwen3-32B, FLUX.1, Mochi 1, and many others. The base configuration starts at $9,999, with shipping scheduled for Q2 2026.

## Key Claims

- Delivers 2,654 TFLOPS at BlockFP8 precision.
- Contains 4× Blackhole AI accelerators (2× p300c cards), each with 120 Tensix cores at 1.35 GHz, totaling 480 cores.
- Total on-chip SRAM is 720 MB (180 MB per chip).
- Total DRAM is 128 GB GDDR6 (32 GB per chip), with a bandwidth of 1,024 GB/s per card.
- Chip interconnect uses Warp400 (2× per card, Samtec ARP6).
- Host system: AMD Ryzen 7 9700X (8 cores, 3.8 GHz), 256 GB DDR5-5600 RAM, 4 TB NVMe PCIe Gen5 storage.
- OS: Ubuntu 24.04.3 LTS.
- Peak power draw approximately 1,500 W from a 1,600 W PSU.
- Liquid cooling with 38 dBA max noise level.
- Llama 3.1 70B achieves 476.5 tokens per second.
- GPT-OSS 120B runs entirely on the device, providing private, local inference.
- Boltz-2 predicts a 686-amino-acid protein structure in 49 seconds on a single Blackhole processor.
- Can predict four protein structures in parallel, achieving roughly 4x throughput of single-job runs.
- Entire software stack (TT-Forge, TT-Metalium, TT-LLK) is open source.
- Idle power consumption reduced by approximately 50% compared to the previous generation.
- Pre-loaded with Qwen3-32B and supports a wide range of models via tt-inference-server, tt-metal, and tt-forge software stacks.
- Supports models from PyTorch, ONNX, TensorFlow, JAX, and PaddlePaddle via TT-Forge.
- Pricing starts at $9,999, with shipping scheduled for Q2 2026.

## Relationships

- [[tt-xla-performance-optimization-techniques]]: The QuietBox 2 leverages the Forge compiler toolchain and TT-Metalium low-level SDK, which include the TT-XLA optimization techniques documented for single-chip Tenstorrent hardware. These techniques—compiler optimization levels, data format selection, device warmup, runtime trace, and batch size tuning—can be used to improve inference performance on this multi-chip system. However, since the QuietBox 2 is a multi-chip system with four Blackhole chips, techniques may need adaptation for the distributed mesh.

- [[tt-metalium]]: The pre-installed TTNN Python library is the high-level operator API built on TT-Metalium.
- [[tt-forge]]: The pre-installed TT-Forge/XLA container wrapper is used for compiling models onto the Quietbox 2's Blackhole chips.

## Sources

- https://www.storagereview.com/news/tenstorrent-quietbox-2-brings-risc-v-ai-inference-to-the-desktop
- https://docs.tenstorrent.com/tt-quietbox2-guide/
- https://wccftech.com/tenstorrent-tt-quietbox-2-risc-v-ai-workstation-128-gb-memory-liquid-cooling-9999-usd/
