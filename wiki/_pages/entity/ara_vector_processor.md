---
cold_start: true
created: 2026-06-27
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://arxiv.org/abs/1906.00478
- https://arxiv.org/abs/2210.08882
- https://arxiv.org/html/2311.07493v2
- https://arxiv.org/pdf/2501.10301
tags:
- risc-v
- vector-processor
- open-source
- eth-zurich
- rvv
- high-performance
type: entity
updated: 2026-06-27
---

# Ara Vector Processor

Ara is a family of open-source, lane-scalable RISC-V vector processors developed at ETH Zurich, designed to execute high-throughput linear algebra and machine learning kernels on in-order vector pipelines. The Ara microarchitecture organizes compute into identical lanes, each containing a slice of the vector register file (VRF) and functional units, so performance scales linearly with lane count. The project has evolved from Ara (RVV v0.5 draft, up to 16 lanes) through Ara2 (RVV 1.0, first open-source compliant implementation) to AraXL (up to 64 lanes), making it the most extensively published open-source vector architecture for RISC-V.

## Key Claims

- Original Ara (2019) implemented in GlobalFoundries 22 nm FD-SOI, runs at over 1 GHz, achieves up to 33 DP-GFLOPS and 41 DP-GFLOPS/W, with 97% FPU utilization on 256×256 double-precision matrix multiplication.
- Original Ara evaluated in 2-, 4-, 8-, and 16-lane configurations; silicon area for 16-lane instance is approximately 4.47 mm² in 22 nm.
- Ara2 (2022) is the first open-source vector processor fully compliant with the frozen RVV 1.0 ISA; 4-lane configuration achieves 37.8 DP-GFLOPS/W at 0.8 V in 22 nm FD-SOI.
- Ara2 multi-core scaling: eight 2-lane Ara2 instances (16 total FPUs) achieves more than 3× higher performance than a single 16-lane Ara2 on 32×32×32 matrix multiplication.
- AraXL extends the design to 64 lanes (maximum VRF size allowed by RVV 1.0 spec), reaching 1.15 GHz and 40.1 GFLOPS/W in 22 nm.
- VRF per lane is 1024 bits; total VRF scales proportionally with lane count.
- Clock frequency is 1.35 GHz for 8-lane or fewer configurations and 1.08 GHz for 16-lane in typical corner.

## Relationships

- [[risc_v_vector_extension]]: Ara2 is one of the first silicon-level implementations fully compliant with RVV 1.0 frozen specification.
- [[gemmini]]: Both are ETH Zurich / UC Berkeley open-source compute engines; Ara targets programmable vector workloads, Gemmini targets fixed-function systolic matrix multiply.
- [[tvm_riscv_backend]]: TVM's RVV backend can generate code for Ara-class hardware using vector intrinsics.
- [[mlir_riscv_backend]]: MLIR vector dialect lowering to RVV intrinsics targets processors like Ara.

## Sources

- Ara original: arXiv:1906.00478 — "Ara: A 1 GHz+ Scalable and Energy-Efficient RISC-V Vector Processor"
- Ara2: arXiv:2311.07493 — "Ara2: Exploring Single- and Multi-Core Vector Processing with an Efficient RVV 1.0 Compliant Open-Source Processor"
- New Ara / RVV 1.0: arXiv:2210.08882
- AraXL: arXiv:2501.10301
