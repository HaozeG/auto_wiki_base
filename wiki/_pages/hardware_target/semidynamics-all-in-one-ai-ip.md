---
canonical_name: Semidynamics All-In-One AI IP
aliases:
- All-In-One AI IP
- Semidynamics All-In-One
subtype: null
tags: []
hardware_targets:
- Semidynamics All-In-One AI IP
toolchains:
- ONNX Runtime
constraints:
- RISC-V custom core
- Tensor Unit for matrix multiplication
- Vector Unit for activation functions
- DMA-free architecture
- Gazzillion Misses technology for data streaming
- Shared vector registers between TU and VU
- Custom tensor extension instructions for 2D tile fetch and transpose
scorecard:
  novelty_delta: 0.8
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.3
sources:
- raw/cache/06c4048736e90634.md
- https://www.design-reuse-embedded.com/news/202406137/semidynamics-releases-tensor-unit-efficiency-data-for-its-new-all-in-one-ai-ip/
source_url: https://www.design-reuse-embedded.com/news/202406137/semidynamics-releases-tensor-unit-efficiency-data-for-its-new-all-in-one-ai-ip/
fetched_at: '2026-07-03T18:09:06.126642+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 1
---

# Semidynamics All-In-One AI IP

The Semidynamics All-In-One AI IP is a RISC-V-based AI accelerator designed to integrate CPU, Tensor Unit (for matrix multiplication), and Vector Unit (for activation computations such as SoftMax and Transpose) into a single, DMA-free processing element. This architecture eliminates the traditional three-chip design of CPU, GPU, and NPU, and uses a unified software stack based on ONNX and RISC-V. The IP leverages Semidynamics' Gazzillion Misses technology for high-throughput data movement between memory and compute units, and custom tensor extension instructions for efficient 2D tile fetching and transposition. It targets LLM inference workloads, with benchmark data for LLaMA-2 7B showing >80% Tensor Unit utilization for most matrix shapes and stable >70% utilization even for large matrices exceeding cache capacity. The All-In-One AI IP is available as licensable intellectual property from Semidynamics, a European RISC-V custom core AI specialist.

## Key Claims

- Integrates RISC-V core, Tensor Unit (MatMul), and Vector Unit (SoftMax/Transpose) in a single DMA-free element.
- Uses a single software stack based on ONNX and RISC-V, replacing three separate stacks (CPU, GPU, NPU).
- Zero-latency connectivity between Tensor and Vector Units via shared vector registers, avoiding data copies.
- Gazzillion Misses technology enables high number of in-flight cache misses for data prefetching, sustaining streaming rates.
- Custom tensor extension instructions optimize 2D tile fetching and transposing.
- ONNX Runtime Execution Provider optimized for the All-In-One IP.
- LLaMA-2 7B BF16: Tensor Unit utilization above 80% for most MatMul shapes (batch=1, first-token computation).
- Tensor Unit utilization stable above 70% for large matrices (8-bit and 16-bit) regardless of matrix size.

## Optimization-Relevant Details

- ISA/profile: RISC-V with custom tensor instructions and vector extension.
- Vector/matrix/accelerator support: Vector Unit (activation functions), Tensor Unit (matrix multiplication), Gazzillion Misses.
- Memory/cache/TLB/DMA: DMA-free, shared vector registers between TU and VU, streaming via Gazzillion Misses.
- Compiler/toolchain support: ONNX Runtime, custom tensor extension instructions.

## Relationships

- Shares the ONNX Runtime toolchain with [[spacemit-k1]], another RISC-V AI accelerator that supports ONNX Runtime for model deployment.
- The unified DMA-free architecture contrasts with traditional three-chip CPU+GPU+NPU designs documented for other hardware targets, offering a simpler programming model.

## Sources

- https://www.design-reuse-embedded.com/news/202406137/semidynamics-releases-tensor-unit-efficiency-data-for-its-new-all-in-one-ai-ip/
