---
type: entity
tags: [ai-accelerator, ipu, bsp, graphcore, inference, training]
sources:
  - https://docs.graphcore.ai/projects/ipu-programmers-guide/en/latest/about_ipu.html
  - https://hc33.hotchips.org/assets/program/conference/day2/HC2021.Graphcore.SimonKnowles.v04.pdf
  - https://www.graphcore.ai/hubfs/assets/pdf/Citadel%20Securities%20Technical%20Report%20-%20Dissecting%20the%20Graphcore%20IPU%20Architecture%20via%20Microbenchmarking%20Dec%202019.pdf
  - https://research.spec.org/icpe_proceedings/2024/companion/p14.pdf
created: 2026-06-26
updated: 2026-06-26
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# Graphcore IPU (Intelligence Processing Unit)

The Graphcore IPU (Intelligence Processing Unit) is a massively parallel processor designed for machine intelligence workloads, distinguished from conventional GPU architectures by its use of the Bulk Synchronous Parallel (BSP) execution model and an entirely on-chip SRAM memory hierarchy. The second-generation Colossus Mk2 GC200, announced in 2020 and fabricated on TSMC's 7 nm process, integrates 1,472 independent processing tiles on a single 823 mm² die containing 59.4 billion transistors. Each tile contains its own processor and 624 KiB of local SRAM, yielding a total of approximately 900 MB of in-processor memory (IPM) accessible at 47.5 TB/s on-chip bandwidth — far exceeding the off-chip HBM bandwidth of contemporary GPUs. The chip delivers 250 TFLOPS of FP16 AI compute (with sparsity) and 62.5 TFLOPS at FP32, while supporting up to 8,832 simultaneous parallel execution threads. The central design argument is that irregular, fine-grained parallelism in graph-structured AI computations benefits more from proximity of memory to compute than from the high peak bandwidth of shared HBM pools.

## Key Claims

- The GC200 integrates 1,472 IPU-Core tiles on a single TSMC 7 nm die of 823 mm², with 59.4 billion transistors, delivering 250 TFLOPS FP16 (with sparsity) and 62.5 TFLOPS FP32.
- Each of the 1,472 tiles holds 624 KiB of local SRAM; total on-chip memory is ~900 MB with an aggregate on-chip bandwidth of 47.5 TB/s, compared to H100's ~3.35 TB/s off-chip HBM3 bandwidth.
- The IPU executes in a strict Bulk Synchronous Parallel (BSP) cycle: all tiles run a local compute phase in parallel, then synchronize at a global barrier, then perform an exchange phase via the IPU-Exchange fabric — no inter-tile communication occurs during the compute phase.
- The Poplar Graph Compiler (part of the Poplar SDK) maps computation graphs onto tiles as BSP supersteps; the PopART (Poplar Advanced Run Time) serves as the interface between ML frameworks (PyTorch, ONNX) and Poplar.
- The chip supports 8,832 independent hardware threads (6 per tile), allowing fine-grained context switching to hide latency during the exchange phase without stalling compute units.
- Unlike GPU streaming multiprocessors, which rely on a shared global memory hierarchy (L2 + HBM), IPU tiles access only their private SRAM during compute phases; inter-tile data movement is explicitly scheduled by the compiler rather than handled by a cache coherence protocol.

## Relationships

- [[nvidia_hopper_h100]] — contrasting architecture: H100 uses shared HBM3 and cache coherence; IPU tiles use private SRAM with compiler-scheduled exchange, making the two architectures suited to different parallelism patterns.
- [[cerebras_wse]] — both chips use large-die, on-chip SRAM-centric designs to avoid HBM bandwidth limits; WSE-3 carries 44 GB on-chip SRAM vs. GC200's 900 MB, targeting even larger models.
- [[google_tpu]] — both are domain-specific AI accelerators with custom compiler stacks (Poplar vs. XLA), but TPU uses systolic arrays with HBM whereas IPU tiles each have local SRAM and run BSP.
- [[groq_lpu]] — Groq also uses a deterministic, compiler-scheduled execution model (no caches, no out-of-order execution) but targets streaming dataflow rather than BSP tile synchronization.
- [[gemmini]] — Gemmini is a research-grade systolic array for RISC-V; IPU represents a commercial many-tile alternative that avoids systolic fixed-function units in favor of general tile processors.

## Sources

- Graphcore IPU Programmer's Guide: https://docs.graphcore.ai/projects/ipu-programmers-guide/en/latest/about_ipu.html
- Hot Chips 33 (2021) — Graphcore Colossus Mk2 IPU presentation by Simon Knowles: https://hc33.hotchips.org/assets/program/conference/day2/HC2021.Graphcore.SimonKnowles.v04.pdf
- Citadel Securities / Graphcore technical report — Dissecting the Graphcore IPU Architecture via Microbenchmarking (2019): https://www.graphcore.ai/hubfs/assets/pdf/Citadel%20Securities%20Technical%20Report%20-%20Dissecting%20the%20Graphcore%20IPU%20Architecture%20via%20Microbenchmarking%20Dec%202019.pdf
- SPEC ICPE 2024 — Evaluating Emerging AI/ML Accelerators: IPU, RDU, and NVIDIA/AMD GPUs: https://research.spec.org/icpe_proceedings/2024/companion/p14.pdf
- Graphcore Mk2 product brief: https://www.graphcore.ai/hubfs/MK2-%20The%20Graphcore%202nd%20Generation%20IPU%20Final%20v7.14.2020.pdf
