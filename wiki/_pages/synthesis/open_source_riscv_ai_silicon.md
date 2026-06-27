---
type: synthesis
connected_entities:
  - lowrisc_opentitan
  - western_digital_swerv_core
  - starfive_visionfive2_jh7110
  - marvell_octeon_10_dpu
  - gemmini
  - risc_v_architecture
  - iree_mlir_compiler
synthesis_status: active
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  bridge_score: 0.65
  contradiction_potential: 0.35
  cross_domain_connection: 0.7
---

# Open-Source RISC-V AI Silicon: From Berkeley to Production

## RAG Summary

Open-source RISC-V silicon has progressed from academic research cores to production hardware deployed in data centers and consumer devices. The LowRISC OpenTitan project achieved the first open-source silicon root of trust to reach production tape-out at TSMC 40 nm in 2023, using the RISC-V Ibex core and partnering with Google, Western Digital, ETH Zurich, and Microsoft. Western Digital's SweRV EH1, open-sourced in 2019 under Apache 2.0 via CHIPS Alliance, demonstrated that commercial-grade RISC-V cores (4.9 CoreMark/MHz at 1.8 GHz on 28 nm) could be released as open hardware without sacrificing competitiveness. The Gemmini spatial array (UC Berkeley, integrated in Chipyard) remains the reference open-source ML accelerator tightly coupled to a RISC-V pipeline, used in academic neural architecture search and dataflow optimization research. StarFive's JH7110 SoC (quad-core SiFive U74, mainline Linux 6.6, Imagination GPU) represents the first affordable open-platform RISC-V SoC with GPU and NPU integration at volume scale. Marvell's OCTEON 10 shows the hybrid path: RISC-V cores for programmable packet processing alongside proprietary ML inference engines in a production DPU. The convergence of open ISA (RISC-V), open toolchains (LLVM, IREE, GCC), and open RTL (Chipyard, OpenTitan, SweRV) creates a full-stack open alternative to proprietary ML silicon—though software ecosystem maturity and volume production remain gaps versus ARM. Key open questions are whether CHIPS Alliance can standardize a common ML extension profile across SweRV successors and Andes cores, and whether OpenTitan-style open RoT will be adopted beyond Google's infrastructure.

---

## Full Synthesis

### From Berkeley to Production

The RISC-V open-source silicon journey follows a clear arc. UC Berkeley's Rocket Chip (2016) established the first production-quality open RISC-V RTL generator, from which Gemmini (spatial array ML accelerator) derived. These remain academic reference platforms. The first industry transition was Western Digital's SweRV EH1 (2019), open-sourced under Apache 2.0 after deployment in NAND flash controllers—the first time a major storage OEM released production RISC-V CPU RTL. CHIPS Alliance absorbed SweRV and has since expanded to host multiple RISC-V IP cores and infrastructure tools.

### OpenTitan: Open Security Silicon

OpenTitan represents a qualitative advance: not merely an open CPU core but a complete open-source security SoC. The 2023 TSMC 40 nm tape-out validated that open-source silicon processes—from RTL (Apache 2.0) through verification, synthesis, and physical design—can produce shipping hardware. Google's deployment of OpenTitan-derived chips in data center servers gives open-source RISC-V silicon its first hyperscale production use case. ETH Zurich's Ibex core at the center of OpenTitan shows European academic institutions contributing production-grade RISC-V IP.

### The Hybrid Path: Marvell OCTEON 10

Marvell's OCTEON 10 DPU illustrates the commercial hybrid approach: RISC-V cores for flexible programmable packet processing are combined with proprietary ARM Cortex-A78 application cores and a proprietary ML inference accelerator. This architectural pattern—open ISA core for flexibility, proprietary compute engines for peak performance—is likely to be replicated as RISC-V cores commoditize the programmable offload layer while differentiated ML accelerators remain proprietary.

### Software Ecosystem as the Binding Constraint

StarFive JH7110 and SpacemiT K1 demonstrate that RISC-V SoC hardware has reached cost-performance parity with low-end ARM SoCs for edge AI. The constraint is now software: PyTorch, ONNX Runtime, and major ML frameworks treat RISC-V as a secondary target. IREE's AOT compilation pipeline provides a path for native RISC-V RVV kernel deployment, but the lack of first-class framework support (compared to ARM's Compute Library) is the primary gap. CHIPS Alliance's AI workgroup is coordinating toolchain standardization across SweRV successors, Andes cores, and open SoC platforms, but convergence timelines are unclear.

## Open Questions

- Can CHIPS Alliance produce a ratified "RISC-V ML Extension Profile" that standardizes software ABI and hardware capability bits across SweRV, AndesCore, and SpacemiT K1 targets?
- Will OpenTitan's open-source RoT model be adopted by cloud providers other than Google, given the supply-chain trust argument for open hardware in AI infrastructure?
- At what production volume threshold does the open-source RISC-V SoC ecosystem (StarFive, SpacemiT) achieve ARM Cortex-A comparable software support from major ML frameworks?
- Does Marvell's hybrid RISC-V + ARM OCTEON 10 architecture predict the long-term role of RISC-V in data center silicon—programmable offload rather than primary compute?

## Connected Pages

- [[lowrisc_opentitan]] — OpenTitan open-source silicon RoT, first production-taped-out open RISC-V chip
- [[western_digital_swerv_core]] — SweRV EH1/EH2/EL2 open-source RISC-V cores via CHIPS Alliance
- [[starfive_visionfive2_jh7110]] — StarFive JH7110 SoC in VisionFive 2 SBC, mainline Linux RISC-V
- [[marvell_octeon_10_dpu]] — OCTEON 10 hybrid RISC-V + ARM DPU with ML inference
- [[gemmini]] — Berkeley open-source spatial array ML accelerator coupled to RISC-V
- [[risc_v_architecture]] — Base ISA and ecosystem context for all open-source RISC-V silicon
- [[iree_mlir_compiler]] — IREE AOT compiler as open-source software path for RISC-V ML deployment
