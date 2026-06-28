---
cold_start: true
created: '2026-07-06'
inbound_links: 1
needs_summary_revision: false
scorecard:
  bridge_score: 0.8
  claim_density: 0.5
  hub_potential: 0.9
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://aiwiki.ai/wiki/tenstorrent
- https://tenstorrent.com
- https://github.com/tenstorrent
- https://aiwiki.ai/wiki/tenstorrent_ai_hardware_guide
- https://www.youtube.com/watch?v=... (Running Llama on Tenstorrent AI Accelerator
  vs NVIDIA RTX 4090)
tags:
- AI hardware
- RISC-V
- open-source
- accelerator
- Jim Keller
type: entity
updated: '2026-06-28'
---

# Tenstorrent

Tenstorrent is a North American artificial intelligence hardware and intellectual property company founded by legendary chip designer Jim Keller in 2016, designing open-standard RISC-V-based AI accelerators for training and inference. The company's product families include Grayskull, Wormhole, and Blackhole AI accelerators, as well as high-performance RISC-V CPUs branded as Ascalon, paired with a fully open-source software stack encompassing compilers (TT-Metalium, TT-MLIR, TT-XLA), frameworks (PyTorch, JAX), and deployment tools (tt-inference-server). Tenstorrent positions itself as a sovereign AI computing platform, offering scale-out servers for production AI workloads, and competes directly with NVIDIA GPU accelerators in the AI inference market by providing an open, vendor-neutral alternative.

## Key Claims

- Tenstorrent was founded in 2016 by chip designer Jim Keller.
- Product families: Grayskull, Wormhole, Blackhole AI accelerators, and Ascalon RISC-V CPUs.
- Software stack is fully open-source, including TT-Metalium, TT-MLIR, TT-XLA, tt-inference-server, and tt-installer.
- Offers sovereign, scale-out servers for production AI starting at $70,000.
- Wormhole N150 accelerator card can run LLama 3.1 8B, comparable to NVIDIA RTX 4090 in inference performance (as demonstrated in a video benchmark).

## Relationships

- [[risc_v_vector_extension]] — Tenstorrent's Ascalon CPUs implement dual 256-bit RVV 1.0 vector units, aligning with the RVV standard.
- [[tvm_riscv_backend]] — Tenstorrent's open-source compiler stack (TT-MLIR, TT-XLA) may be integrated with TVM for model compilation on RISC-V targets.

## Sources

- AI Wiki: Tenstorrent page (https://aiwiki.ai/wiki/tenstorrent)
- Tenstorrent.com — "Tenstorrent is a next-generation computing company that builds computers for AI."
- GitHub: tenstorrent/tt-metal, tenstorrent/tt-mlir, tenstorrent/tt-xla, tenstorrent/tt-inference-server, tenstorrent/tt-installer.
- AI Wiki: Tenstorrent AI Hardware Guide (https://aiwiki.ai/wiki/tenstorrent_ai_hardware_guide)
- YouTube video: "Running Llama on Tenstorrent AI Accelerator vs NVIDIA RTX 4090"
