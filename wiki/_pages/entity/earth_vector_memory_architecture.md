---
canonical_name: EARTH
aliases:
- Efficient ARchitecture for vecTor memory access
subtype: null
tags:
- RISC-V
- vector processor
- memory access
- shift networks
- FPGA
- Chisel
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/a6c84cac7bd60bfd.md
- https://arxiv.org/html/2504.08334
source_url: https://arxiv.org/html/2504.08334
fetched_at: '2026-07-02T06:46:40.826584+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
outbound_links:
- target: k230
  reason: The K230 SoC integrates a RISC-V vector core (C908) that can benefit from
    EARTH's memory access optimizations, as vector memory efficiency is critical for
    the KPU's data supply
- target: xuantie_c908
  reason: The XuanTie C908 is a RISC-V vector processor core that supports RVV 1.0;
    EARTH's shifting-based memory access techniques are directly applicable to improving
    its const-stride and segment load/store performance
- target: mlir_xdsl_rvv_gemm_codegen_recipe
  reason: This optimization recipe targets RVV code generation, and EARTH's memory
    access improvements complement software-level optimizations by ensuring efficient
    data movement
---

# EARTH

EARTH (Efficient ARchitecture for vecTor memory access) is a novel vector memory access architecture designed to address inefficiencies in handling constant-stride and segment memory access patterns in RISC-V vector processors. Unlike conventional designs that rely on high-overhead crossbar interconnects or large transposition buffers, EARTH introduces shifting-based optimizations: specialized shift networks for gathering and scattering strided elements, and a shifted register bank that enables direct column-wise access for segment operations. The architecture was implemented on FPGA using Chisel HDL, building upon the open-source Saturn RISC-V vector unit. EARTH achieves 4x-8x speedups on benchmarks dominated by constant-stride operations while reducing hardware area by 9% and power consumption by 41% compared to conventional designs.

## Key Claims

- EARTH employs layered shift networks in a Data Reorganization Module (DROM) to efficiently gather/scatter strided elements within cache lines, reducing the overhead of constant-stride access.
- For segment operations, a shifted register bank provides in-place bulk transposition without dedicated segment buffers.
- Evaluation on FPGA demonstrates 4x–8x speedups for workloads dominated by constant-stride memory accesses.
- Compared to conventional vector memory access designs, EARTH reduces hardware area by 9% and power consumption by 41%.
- The design is implemented on FPGA using Chisel HDL based on the open-source Saturn RISC-V vector unit.

## Relationships

- [[k230]]: The K230 SoC integrates a RISC-V vector core (C908) that can benefit from EARTH's memory access optimizations, as vector memory efficiency is critical for the KPU's data supply.
- [[xuantie_c908]]: The XuanTie C908 is a RISC-V vector processor core that supports RVV 1.0; EARTH's shifting-based memory access techniques are directly applicable to improving its const-stride and segment load/store performance.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: This optimization recipe targets RVV code generation, and EARTH's memory access improvements complement software-level optimizations by ensuring efficient data movement.

## Sources

- https://arxiv.org/html/2504.08334
