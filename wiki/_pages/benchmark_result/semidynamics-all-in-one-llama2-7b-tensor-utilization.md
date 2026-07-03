---
canonical_name: Semidynamics All-In-One LLaMA-2 7B Tensor Utilization
aliases:
- Semidynamics All-In-One TU efficiency LLaMA-2
subtype: null
tags: []
hardware_targets:
- Semidynamics All-In-One AI IP
workloads:
- LLaMA-2 7B (self-attention MatMul layers)
datatypes:
- BF16
metrics:
- Tensor Unit utilization (%)
toolchains:
- ONNX Runtime
hardware_versions: []
software_versions: []
measurement_method: Batch=1, first-token computation, aggregated by A-tensor shape,
  measured using Semidynamics ONNX Runtime Execution Provider
evidence_strength: reported
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
type: benchmark_result
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# Semidynamics All-In-One LLaMA-2 7B Tensor Utilization

The Semidynamics All-In-One AI IP was benchmarked running the LLaMA-2 7B parameter LLM with BF16 weights. The Tensor Unit utilization was measured for all self-attention MatMul layers using Semidynamics' ONNX Runtime Execution Provider. Results were aggregated by A-tensor shape, showing above 80% utilization for most shapes under the challenging condition of batch=1 and first-token computation. For large matrices exceeding cache/scratchpad capacity, utilization remained stable above 70% for both 8-bit and 16-bit data types, attributed to the Gazzillion Misses technology enabling sustained streaming from main memory. These results were reported by Semidynamics in a press release in June 2024.

## Key Claims

- Tensor Unit utilization above 80% for most self-attention MatMul shapes in LLaMA-2 7B (batch=1, first-token).
- Stable Tensor Unit utilization above 70% for large matrices (8-bit and 16-bit), regardless of matrix size, due to Gazzillion Misses technology.
- Benchmark performed using Semidynamics' ONNX Runtime Execution Provider.

## Measurement Context

- Hardware version: Semidynamics All-In-One AI IP (no specific version given)
- Software/toolchain version: ONNX Runtime Execution Provider (no version given)
- Workload shape: LLaMA-2 7B self-attention MatMul layers, six different A-tensor shapes
- Metric: Tensor Unit utilization (%)
- Method: Batch=1, first-token computation, aggregated by A-tensor shape
- Evidence strength: reported (press release from Semidynamics)

## Relationships

- Results are directly tied to the [[semidynamics-all-in-one-ai-ip]] hardware architecture, which provides the Tensor Unit, Vector Unit, and Gazzillion Misses support.
- Shares the ONNX Runtime toolchain with [[spacemit-k1]], another RISC-V accelerator that uses ONNX Runtime for AI inference.

## Sources

- https://www.design-reuse-embedded.com/news/202406137/semidynamics-releases-tensor-unit-efficiency-data-for-its-new-all-in-one-ai-ip/
