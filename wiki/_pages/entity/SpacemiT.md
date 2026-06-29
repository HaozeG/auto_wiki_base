---
cold_start: false
created: '2026-06-28'
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: 0.8
  claim_density: 0.6
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://github.com/spacemit-com
tags:
- SpacemiT
- RISC-V
- AI accelerator
- K1
- K3
type: entity
updated: '2026-06-28'
---

# SpacemiT

SpacemiT is a RISC-V AI accelerator ecosystem developer known for the K1 and K3 SoCs. The SpacemiT GitHub organization (github.com/spacemit-com) serves as the central hub for open-source enablement of K1/K3 support across system software, toolchains, AI software, and independent open-source projects. This page summarizes the upstream progress and available resources, including Linux kernel mainline support for K1, OpenSBI completion, U-Boot work-in-progress, LLVM and GCC upstream efforts, and AI inference engine ports such as llama.cpp and onnxruntime. Additionally, the organization hosts repositories for AI SDK, AI gateway, model zoos for ASR, TTS, vision, and media processing platforms. Communication channels include a forum, Reddit, X/Twitter, and WeChat groups.

## Key Claims

- Linux kernel: mainline support for K1 (2026-05-30).
- OpenSBI: completed major planned support for K1; planning for K3.
- U-Boot: WIP for K1 upstream support.
- LLVM: upstream status tracked via dedicated status page.
- GCC: upstream status tracked via dedicated status page.
- llama.cpp: WIP support for K1/K3 (2026-06-05).
- FlagGems: independent OSS project with spine-FlagGems repository for operator library.
- onnxruntime: module status tracked.
- spine-triton: independent OSS project.
- K3-Ubuntu-Images: repository providing UEFI-bootable Ubuntu RISC-V image for K3 Pico-ITX board, flashed via fastboot.
- AI SDK and AI Gateway repositories for ASR, TTS, VAD, Vision, LLM, Embedding, and Rerank APIs.
- Communication channels: forum (forum.spacemit.com), Reddit (r/spacemit_riscv), X/Twitter (@spacemit_riscv), WeChat groups (via forum link).

## Relationships

- [[HAL_riscv_rvv_OpenCV_Optimization_Recipe]] – Optimization recipe for OpenCV on SpacemiT KeyStone K1, which is the hardware target from this organization.
- [[HAL_riscv_rvv_Performance_Benchmarks]] – Benchmark results for the same HAL on K1 hardware.

Insufficient context for additional cross-links to entity pages; available related pages are from other types.

## Sources

- [SpacemiT GitHub organization](https://github.com/spacemit-com)
