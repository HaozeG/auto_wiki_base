---
type: synthesis
connected_entities:
- amd_instinct
- amd_cdna_4
- amd_zen
synthesis_status: draft
tags:
- amd
- chiplet
- architecture
- gpu-architecture
- cpu-architecture
sources:
- wiki/_pages/entity/amd_instinct.md
- wiki/_pages/entity/amd_cdna_4.md
- wiki/_pages/entity/amd_zen.md
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
outbound_links:
- target: amd_instinct
  reason: unlabeled
- target: amd_cdna_4
  reason: unlabeled
- target: amd_zen
  reason: unlabeled
---

# AMD's Chiplet Strategy Across Zen CPUs and CDNA Accelerators

## RAG Summary
AMD's chiplet design philosophy unifies both its CPU (Zen) and GPU accelerator (CDNA) architectures, enabling scalable products across the Instinct and Ryzen/EPYC lines, with the MI300A APU demonstrating their convergence. The [[amd_zen]] architecture uses multiple compute chiplets (CCDs) on a separate I/O die, achieving generational IPC improvements of 3–19% per generation through microarchitectural enhancements. The [[amd_cdna_4]] architecture, powering the next-generation [[amd_instinct]] MI350X and MI355X, employs eight compute chiplets (XCDs) on two I/O dies, packing 185 billion transistors and delivering up to 10 PFLOPS of sparse FP8 compute. While both adopt heterogeneous chiplet integration for scalability, they target different workloads: Zen optimizes single-thread and general-purpose performance, while CDNA 4 optimizes matrix compute throughput for AI and HPC. This convergence culminates in the MI300A, which packages Zen 4 CPU cores with CDNA 3 GPU chiplets on a single substrate, marking a strategic move to unify AMD's compute portfolio for data center workloads.

## Full Synthesis
AMD's two major computing architectures—Zen for CPUs and CDNA for GPU accelerators—both rely on a chiplet-based design approach that decouples core compute from I/O, but they serve distinct purposes and have evolved along separate paths before converging in hybrid products.

### Shared Chiplet Philosophy
Both architectures divide the die into smaller chiplets fabricated on advanced process nodes. [[amd_zen]] employs compute chiplets (CCDs) that contain multiple CPU cores, connected via Infinity Fabric to a centralized I/O die (IOD). This allows AMD to scale core counts across desktop, workstation, and server processors while reusing Zen designs across markets. [[amd_cdna_4]] similarly uses eight compute chiplets (XCDs) on TSMC N3P, stacked vertically on two I/O dies on N6, packaging 185 billion transistors. The key difference is that Zen chiplets communicate coherently as a single CPU socket, while CDNA chiplets act as a unified GPU compute accelerator with shared HBM3E memory.

### Performance Focus Differences
Zen generations focus on IPC (instructions per cycle) improvements: Zen 3 achieved ~19% IPC gain over Zen 2, Zen 4 ~13%, and Zen 5 ~16% for desktop. These gains come from improved branch prediction, wider execution pipelines, and cache hierarchy redesigns—reflecting CPU-centric optimization. In contrast, CDNA and [[amd_instinct]] accelerators prioritize raw matrix compute throughput. [[amd_cdna_4]] peaks at 5.0 PFLOPS FP8 (10 PFLOPS with sparsity) by packing 256 compute units with enhanced local data share (LDS) bandwidth and support for AMD-unique MXFP6 format. The MI250X (CDNA 2) achieved 383 TFLOPS FP16; CDNA 4 increases this by over 10×. This divergence highlights the different workloads: Zen targets general-purpose and sequential tasks, while CDNA targets highly parallel matrix math.

### Convergence in the MI300 Family
The most explicit connection between the two architectures is the [[amd_instinct]] MI300A, an APU integrating 24 Zen 4 CPU cores and 228 CDNA 3 GPU compute units with 128 GB HBM3 memory. This hybrid package allows coherent CPU–GPU memory access, reducing data movement overhead for HPC and AI workloads. The MI300X accelerator (CDNA 3) omits CPU cores, focusing purely on GPU compute. This bifurcation shows AMD's strategy: offer both converged (APU) and discrete (GPU-only) options, depending on workload data-sharing requirements.

### Future Evolution
[[amd_cdna_4]] introduces MI350X (air-cooled, 1000 W TDP) and MI355X (liquid-cooled, 1400 W TDP), while [[amd_zen]] continues with Zen 5 improving HPC throughput by 37% per the EPYC line. The two architectures are likely to remain separate but increasingly share interconnects and packaging technology, as seen in the Infinity Fabric bandwidth claims matching NVIDIA NVLink speeds.

## Open Questions
- Will future hybrid APUs like MI300A become the dominant data center processor, or will discrete CPU (Zen) and GPU (CDNA) remain separate for independent scaling?
- How does AMD's heterogeneous chiplet approach compare to NVIDIA's monolithic GPU dies or Intel's tile-based architectures in terms of yield, cost, and performance per watt?
- What are the trade-offs of removing TF32 hardware support from CDNA 4, given that Zen CPUs still compute TF32 in software—will this force workload partitioning?
- Can AMD's chiplet strategy scale beyond 8 XCDs without hitting memory bandwidth or inter-chiplet latency bottlenecks?

## Connected Pages
- [[amd_instinct]]
- [[amd_cdna_4]]
- [[amd_zen]]
