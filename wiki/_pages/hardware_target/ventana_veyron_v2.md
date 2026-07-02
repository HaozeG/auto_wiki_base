---
canonical_name: Ventana Veyron V2
aliases:
- Veyron V2
- Ventana Veyron V2 CPU
- Ventana Veyron V2 RISC-V processor
- Ventana Veyron V2 RISC-V
subtype: null
tags: []
hardware_targets:
- Ventana Veyron V2
toolchains: []
constraints:
- RVA23 profile
- UCIe chiplet interface
- AMBA CHI
- IOMMU
- RAS ECC support
- Secure Boot and chiplet authentication
- 192 cores per socket via 6 compute chiplets
- Up to 128MB L3 cache per chiplet
- 512KB I-cache, 128KB D-cache, 1MB L2 cache per core
- DDR and PCIe controllers in I/O hub
- Domain-specific acceleration (DSA) chiplets
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/e8028d0bcc66b971.md
- https://www.servethehome.com/ventana-veyron-v2-risc-v-cpu-launched-for-the-dsa-future/
- raw/cache/efa0832900d66f7b.md
- https://www.nextplatform.com/compute/2023/11/07/ventana-launches-veyron-v2-risc-v-into-the-datacenter/1652320
source_url: https://www.servethehome.com/ventana-veyron-v2-risc-v-cpu-launched-for-the-dsa-future/
fetched_at: '2026-07-02T05:00:22.868284+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Ventana Veyron V2

The Ventana Veyron V2 is a data center RISC-V processor designed by Ventana Microsystems, announced in mid-2026 as a follow-up to the Veyron V1 architecture. It adopts a chiplet-based approach using the Universal Chiplet Interconnect Express (UCIe) standard to connect compute chiplets to an I/O hub that contains DDR and PCIe controllers. Each compute chiplet integrates 32 cores with up to 128 MB of shared L3 cache, and up to six chiplets can be combined to reach 192 cores per socket. The processor implements the RVA23 profile (including RISC-V vector extensions) and uses the AMBA CHI protocol for cache coherence. Key platform features include RAS with ECC and data poisoning, Secure Boot and chiplet authentication, and an IOMMU for memory management. The design targets hyperscaler data centers that demand domain-specific acceleration (DSA), allowing custom accelerator chiplets to be integrated alongside the compute chiplets. Ventana deliberately skipped full productization of the V1 to focus on standards compliance and platform maturity for the V2.

## Key Claims

- Chiplet architecture: six compute chiplets plus I/O hub, interconnected via UCIe.
- 192 cores per socket (32 cores per chiplet).
- RVA23 profile with RISC-V vector extensions.
- AMBA CHI cache coherence protocol.
- Cache hierarchy per core: 512 KB I-cache, 128 KB D-cache, 1 MB L2 cache; per chiplet: up to 128 MB L3 cache.
- RAS features: ECC, data poisoning.
- Security: Secure Boot, chiplet authentication.
- IOMMU for memory management.
- Supports domain-specific acceleration via chiplets (DSA).

## Optimization-Relevant Details

- ISA/profile: RVA23 (RISC-V Vector Extension implied).
- Vector/matrix/accelerator support: not specified in source (vector extension assumed via RVA23).
- Memory/cache/TLB/DMA: Per-core I-cache 512KB, D-cache 128KB, L2 cache 1MB; per-chiplet L3 cache up to 128MB; I/O hub with DDR and PCIe controllers.
- Compiler/toolchain support: not specified.

## Relationships

- [[xuantie_c908]]: another RISC-V core targeting AIoT, contrasting the Veyron V2's data-center focus.
- [[k230]]: a RISC-V SoC integrating the C908 core, showing a lower-end RISC-V platform.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: a compiler optimization recipe for RISC-V vector code generation, relevant to the Veyron V2's vector extension support.

## Sources

- https://www.servethehome.com/ventana-veyron-v2-risc-v-cpu-launched-for-the-dsa-future/
