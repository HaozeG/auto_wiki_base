---
canonical_name: Gemmini
aliases:
- Gemmini DNN accelerator generator
- Gemmini generator
subtype: null
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.95
  bridge_score: 0.2
  hub_potential: 0.85
sources:
- raw/cache/d7566393cf534c9f.md
- https://ar5iv.labs.arxiv.org/html/1911.09925
source_url: https://ar5iv.labs.arxiv.org/html/1911.09925
fetched_at: '2026-07-01T02:40:55.177668+00:00'
type: entity
created: '2026-07-01'
updated: '2026-07-01'
cold_start: true
inbound_links: 3
needs_summary_revision: false
---

# Gemmini

Gemmini is an open-source, full-stack DNN accelerator generator developed at UC Berkeley. It provides a highly parameterizable hardware template that can generate ASIC accelerators supporting multiple dataflows (vector and systolic), datatypes (integer and floating-point), and direct convolution execution, along with a multi-level programming interface and a complete RISC-V compatible SoC environment with OS support. Gemmini's architecture allows users to systematically evaluate the performance and energy efficiency of deep learning accelerators across the full stack, from hardware to software. Fabricated in TSMC 16 nm and Intel 22 nm FFL processes, Gemmini-generated accelerators have demonstrated up to 2,670× speedup over high-performance CPUs on various DNN benchmarks and competitive performance against state-of-the-art commercial DNN accelerators. The generator co-designs the accelerator, application, and system, enabling optimizations like virtual address translation tuning and memory resource partitioning.

## Key Claims

- Supports flexible architectural template with configurable spatial array type (systolic or vector).
- Supports both integer and floating-point datatypes, covering training and inference.
- Supports multiple dataflows configurable at design time and runtime.
- Provides direct execution of DNN operators, including convolution.
- Includes a multi-level programming interface: high-level framework integration (PyTorch, TVM) and low-level C/C++/assembly control.
- Integrates into a full RISC-V SoC with virtual memory support, Linux-capable OS, and shared system resources.
- Fabricated accelerators in TSMC 16 nm FinFET and Intel 22FFL processes.
- Achieves up to 2,670× speedup over a baseline CPU and comparable performance to a commercial DNN accelerator.
- Enables system-accelerator co-design case studies: optimizing virtual address translation and memory partitioning for DNN workloads.

## Relationships

- [[meta_mtia]]: a production, data-center-scale AI accelerator (Meta's Training and Inference Accelerator) that, unlike Gemmini's research/generator model, reaches RISC-V only as a Triton compiler codegen target rather than as a native accelerator ISA.
- [[systolic_tensor_units]]: the general systolic-array dataflow concept (as used in Google's TPU) that Gemmini's configurable spatial array can be instantiated as.

## Sources

- [1911.09925] Gemmini: Enabling Systematic Deep-Learning Architecture Evaluation via Full-Stack Integration. Hasan Genc et al. https://ar5iv.labs.arxiv.org/html/1911.09925
