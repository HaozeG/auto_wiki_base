---
cold_start: false
created: '2026-07-02'
datatypes:
- int8
- int16
evidence_strength: reported
hardware_targets:
- P-CORE (RV32IM with P-extension v0.9.11)
hardware_versions:
- RV32IM P-extension v0.9.11
inbound_links: 0
measurement_method: Design Space Exploration (DSE) evaluating SIMD8 (8-bit 4-way)
  and SIMD16 (16-bit 2-way) configurations; experimental results reported in the paper.
metrics:
- speedup
- power efficiency
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.9
software_versions: []
sources:
- https://ui.adsabs.harvard.edu/abs/2025IEEEA..1346603A/abstract
tags:
- RISC-V
- P-extension
- Packed-SIMD
- CNN
- RV32IM
toolchains: []
type: benchmark_result
updated: '2026-06-29'
workloads:
- CNN max-pooling
- CNN matrix multiplication
- CNN fully connected networks
- LeNet-5
---

# P-CORE Packed-SIMD Extension Benchmark Results

The P-CORE is a RISC-V processor based on the RV32IM base ISA with optional support for the Packed-SIMD (P) extension, specifically version 0.9.11-draft-20211209. This work presents the first processor implementing the P-extension for the RV32 specification, targeting efficient integer-based computation for CNN inference. Benchmark evaluations using a LeNet-5 handwritten digit recognition CNN demonstrate speedups of up to 17x for max-pooling, 7x for matrix multiplication, and 4.8x for fully connected networks when the P-extension is activated. Similar improvements in power efficiency are also reported. A Design Space Exploration (DSE) compares SIMD8 (8-bit, 4-way) and SIMD16 (16-bit, 2-way) configurations to assess the impact of data-level parallelism. These results are sourced from the research paper 'P-CORE: Exploring RISC-V Packed-SIMD Extension for CNNs'.

## Key Claims

- With the P-extension activated, CNN max-pooling achieves speedups of up to 17x.
- Matrix multiplication (likely GEMM) achieves speedups of up to 7x.
- Fully connected network layers achieve speedups of up to 4.8x.
- Power efficiency improvements accompany the speedup gains similarly.
- A Design Space Exploration (DSE) evaluates the P-extension with SIMD8 (8-bit, 4-way) and SIMD16 (16-bit, 2-way) data-level parallelism configurations.

## Measurement Context

- **Hardware version:** P-CORE (RV32IM base ISA with P-extension v0.9.11).
- **Software/toolchain version:** Not specified in the available resource.
- **Workload shape:** CNN operations (max-pooling, matrix multiplication, fully connected networks) and the LeNet-5 handwritten digit recognition model.
- **Metric:** Speedup factor (ratio of execution time without P-extension to execution time with P-extension); power efficiency (qualitative improvement relative to baseline).
- **Method:** Design Space Exploration with two SIMD configurations; results reported from the paper (likely simulation-based on an RTL or architectural simulator).
- **Evidence strength:** reported (claims from a paper; exact measurement infrastructure not detailed in the available text).

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Another set of RISC-V AI accelerator benchmark results, providing context for comparison of different RISC-V AI acceleration strategies.
- [[Gemmini_Architecture]] – An open-source DNN accelerator generator for RISC-V, representing an alternative approach to accelerating CNNs.
- Insufficient context for additional cross-links to entity pages; the P-extension and P-CORE are new concepts not yet represented in the wiki.

## Sources

- [arXiv abstract: P-CORE: Exploring RISC-V Packed-SIMD Extension for CNNs](https://ui.adsabs.harvard.edu/abs/2025IEEEA..1346603A/abstract)
