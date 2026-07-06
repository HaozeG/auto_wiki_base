---
canonical_name: MATCH
aliases:
- Model-Aware TVM-based Compilation for Heterogeneous Edge Devices
subtype: null
tags:
- compilation
- TVM
- edge
- DNN
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.5
sources:
- raw/cache/d0e07a019e49407f.md
- https://arxiv.org/html/2410.08855
source_url: https://arxiv.org/html/2410.08855
fetched_at: '2026-07-06T02:44:42.955840+00:00'
type: entity
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: gap9
  reason: MATCH targets the GAP9 SoC, achieving 2.15× latency improvement over the
    dedicated DORY compiler by synergistically exploiting the DNN accelerator and
    eight-core cluster
- target: mlir-xdsl-rvv-codegen-pipeline
  reason: Both MATCH and the MLIR-xDSL RVV code generation pipeline address compilation
    challenges for DNNs on edge platforms, but MATCH focuses on heterogeneous MCUs
    with custom accelerators using TVM, while the MLIR-xDSL pipeline targets RVV-based
    platforms using MLIR and xDSL
---

# MATCH

MATCH (Model-Aware TVM-based Compilation for Heterogeneous Edge Devices) is a novel DNN deployment framework that extends the TVM compiler infrastructure to support heterogeneous edge MCUs with custom hardware accelerators. Unlike prior retargetable toolchains that generate generic unoptimized code, MATCH uses a customizable model-based hardware abstraction and hardware cost models to enable agile retargeting across different processors and accelerators without requiring labor-intensive re-development. MATCH was evaluated on two state-of-the-art heterogeneous MCUs, GAP9 and DIANA, using the four DNN models of the MLPerf Tiny suite, demonstrating significant latency improvements over both generic TVM and custom toolchains such as HTVM and DORY.

## Key Claims

- MATCH is a TVM-based DNN deployment framework that uses a customizable model-based hardware abstraction and hardware cost models to enable agile retargeting across heterogeneous edge MCUs.
- On the DIANA platform, MATCH reduces inference latency by up to 60.88× compared to plain TVM, and 16.94% compared to HTVM (a fully customized toolchain for DIANA), as evaluated on the four DNN models of the MLPerf Tiny suite.
- On the GAP9 platform, MATCH improves inference latency by 2.15× compared to the dedicated DORY compiler, by exploiting both the DNN accelerator and the eight-core cluster.

## Relationships

- [[gap9]]: MATCH targets the GAP9 SoC, achieving 2.15× latency improvement over the dedicated DORY compiler by synergistically exploiting the DNN accelerator and eight-core cluster.
- [[mlir-xdsl-rvv-codegen-pipeline]]: Both MATCH and the MLIR-xDSL RVV code generation pipeline address compilation challenges for DNNs on edge platforms, but MATCH focuses on heterogeneous MCUs with custom accelerators using TVM, while the MLIR-xDSL pipeline targets RVV-based platforms using MLIR and xDSL.

## Sources

- https://arxiv.org/html/2410.08855
