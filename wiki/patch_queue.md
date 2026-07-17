# Wiki Patch Queue

## [2026-07-17] pending | amd_cdna_4.md
target_page: amd_cdna_4.md
target_section: Key Claims
source: https://www.amd.com/en/newsroom/press-releases/2024-6-2-amd-accelerates-pace-of-data-center-ai-innovation-.html
status: pending_review
proposed_update: Add claim from AMD press release: 'Up to 35x increase in AI inference performance compared to AMD Instinct MI300 Series with CDNA 3 architecture' as a marketing claim (evidence strength: marketing). Add a note that this is a vendor-claimed generational improvement, not a measured benchmark.

## [2026-07-17] pending | amd_cdna_4.md
target_page: amd_cdna_4.md
target_section: Relationships
source: https://gpuopen.com/machine-readable-isa/
status: pending_review
proposed_update: Add a relationship entry linking to the AMD machine-readable GPU ISA specification page: 'The AMD CDNA 4 instruction encoding is documented in the machine-readable ISA XML specification (amdgpu_isa_cdna4.xml), which provides the canonical encoding for matrix core and data-path instructions.'

## [2026-07-17] pending | amd_cdna.md
target_page: amd_cdna.md
target_section: Key Claims
source: https://chipsandcheese.com/p/amds-cdna-3-compute-architecture
status: pending_review
proposed_update: Add the following detailed architectural claims about CDNA 3 from the Chips and Cheese article: MI300X uses 8 Accelerator Complex Dies (XCDs), each with 38 enabled Compute Units (304 total) and a 4 MB L2 cache per XCD; includes an Infinity Cache (Memory Attached Last Level, MALL) derived from RDNA to mitigate memory bandwidth starvation; presents a unified GPU memory pool unlike the MI250X which required manual work splitting; EMIB bridge in Intel Ponte Vecchio offers only 230 GB/s bandwidth; CDNA 3 uses two die types on TSMC 6nm and 5nm nodes. Also note the comparison with Nvidia H100 (132 SMs, monolithic die, split L2) and Ponte Vecchio (Compute Tiles with larger L1 caches, NUMA API for dual-stack configuration).

## [2026-07-17] pending | amd_cdna.md
target_page: amd_cdna.md
target_section: Key Claims
source: https://www.elprocus.com/amd-instinct-mi350/
status: pending_review
proposed_update: Add a subsection on CDNA 4, the fourth generation introduced with the AMD Instinct MI350 series in June 2025. CDNA 4 features 3nm XCDs, 6nm IODs, support for FP4/FP6 datatypes, up to 288GB HBM3E with 8TB/s bandwidth, and up to 35x inference performance improvement over CDNA 3 based products.

## [2026-07-17] merge_pending | amd_instinct_mi325x.md
target_page: amd_instinct_mi325x.md
canonical_name: AMD Instinct MI325X
colliding_name: AMD Instinct MI325X
source: https://wccftech.com/amd-instinct-ai-accelerator-lineup-mi325x-refresh-q4-3nm-mi350-cdna-4-2025-cdna-mi400-cdna-next-2026/
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI325X

The AMD Instinct MI325X is an AI accelerator announced by AMD at Computex 2024, based on the CDNA 3 microarchitecture and positioned as a refresh of the MI300X series. It features 288 GB of HBM3E memory with a peak bandwidth of 6 TB/s, delivers 1.3 PFLOPs of FP16 and 2.6 PFLOPs of FP8 compute performance, and can handle up to 1 trillion parameters per server. Compared to the NVIDIA H200, AMD claims 2x memory capacity, 1.3x memory bandwidth, and 1.3x peak AI compute performance. The accelerator uses the same chiplet housing structure as the MI300X and is planned for launch in Q4 2024. This accelerator is part of AMD's annual Instinct roadmap, with future models including the MI350 series (CDNA 4, 3nm, 2025) and MI400 series (CDNA Next, 2026).

## Key Claims

- 288 GB HBM3E memory with 6 TB/s peak memory bandwidth.
- 1.3 PFLOPs FP16 and 2.6 PFLOPs FP8 peak theoretical performance.
- Up to 1 trillion parameters per server.
- Versus NVIDIA H200: 2x memory, 1.3x memory bandwidth, 1.3x peak FP16/FP8.
- Uses chiplet housing design similar to MI300X.
- Available Q4 2024.

## Relationships

- The AMD Instinct MI325X is built on the [[amd_cdna|AMD CDNA]] 3 microarchitecture, inheriting its compute-focused design, multi-chip module packaging, and matrix compute hardware.

## Sources

- [AMD Instinct AI Accelerator Lineup Gets MI325X Refresh In Q4, 3nm...](raw/cache/da8f193fc9740574.md)
merge_draft_body -->

## [2026-07-17] pending | amd_cdna.md
target_page: amd_cdna.md
target_section: Key Claims
source: https://wccftech.com/amd-instinct-ai-accelerator-lineup-mi325x-refresh-q4-3nm-mi350-cdna-4-2025-cdna-mi400-cdna-next-2026/
status: pending_review
proposed_update: Add mention that CDNA 3 powers the Instinct MI325X accelerator announced in 2024, featuring 288 GB HBM3E memory, 6 TB/s bandwidth, and 1.3 PFLOPs FP16/2.6 PFLOPs FP8 compute, available Q4 2024.

## [2026-07-17] merge_pending | amd_instinct_mi325x.md
target_page: amd_instinct_mi325x.md
canonical_name: AMD Instinct MI325X
colliding_name: AMD Instinct MI325X
source: https://www.crn.com/news/ai/2024/amd-says-instinct-mi325x-bests-nvidia-h200-vows-huge-uplift-with-mi350
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI325X

The AMD Instinct MI325X is a data-center AI accelerator GPU announced in October 2024 as a memory-capacity upgrade to the Instinct MI300X. Based on the same CDNA 3 microarchitecture as the MI300X, the MI325X increases HBM memory from 192 GB to 256 GB of HBM3e and raises memory bandwidth from 5.3 TB/s to 6 TB/s. Compute throughput remains unchanged at 2.6 petaflops FP8 and 1.3 petaflops FP16 per chip. The MI325X is designed for large-language model inference and training, with AMD claiming up to 40% faster inference throughput on a Mixtral 8x7B model compared to Nvidia's H200 at the chip level, and 20% lower latency on a Llama 3.1 70B model. At the platform level, eight MI325X GPUs connected via Infinity Fabric provide 2 TB of HBM3e memory, 48 TB/s aggregate bandwidth, 20.8 petaflops FP8 and 10.4 petaflops FP16 performance. AMD positions the MI325X as a yearly cadence release, with systems from Dell, Lenovo, Supermicro, HPE, and others shipping from Q1 2025.

## Key Claims

- The MI325X features 256 GB of HBM3e memory with 6 TB/s bandwidth, up from 192 GB HBM3 and 5.3 TB/s in the MI300X.
- Compute throughput: 2.6 petaflops FP8 and 1.3 petaflops FP16 (identical to MI300X).
- At the chip level, AMD claims the MI325X delivers 40% faster inference throughput on a Mixtral 8x7B model and 30% lower latency on a Mixtral 7B model compared to Nvidia H200.
- On Llama 3.1 70B inference, AMD claims 20% lower latency versus H200.
- The eight-GPU MI325X platform offers 80% higher memory capacity and 30% greater memory bandwidth than Nvidia's H200 HGX platform.
- For single-GPU training of Llama 2 7B, AMD claims 10% faster performance than H200; eight-GPU training on Llama 2 70B is claimed to be on par.
- The MI325X uses the same CDNA 3 architecture as MI300X, with memory upgrade to HBM3e.

## Relationships

- Shares the CDNA 3 compute microarchitecture documented in [[amd_cdna]].

## Sources

- [AMD Says Instinct MI325X Bests Nvidia H200, Vows Huge Uplift With MI350](raw/cache/321526d73cf105b3.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_cdna_4.md
target_page: amd_cdna_4.md
canonical_name: AMD CDNA 4
colliding_name: AMD Instinct MI350
source: https://www.crn.com/news/ai/2024/amd-says-instinct-mi325x-bests-nvidia-h200-vows-huge-uplift-with-mi350
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI350

The AMD Instinct MI350 is a planned next-generation AI accelerator GPU series announced in October 2024, based on the new CDNA 4 microarchitecture and manufactured on a 3-nanometer process. The first chip in the series, the MI355X, will feature 288 GB of HBM3e memory with 8 TB/s bandwidth, a 50% increase in memory capacity over the MI300X platform. The MI350 series introduces support for 4-bit (FP4) and 6-bit (FP6) floating-point formats alongside FP8 and FP16, enabling peak performance of 9.2 petaflops for the MI355X at FP8 and 2.3 petaflops at FP16. In FP4/FP6, the MI355X achieves up to 74 petaflops. AMD projects that an eight-GPU MI350 platform will deliver up to 35× inference performance improvement over the MI300X platform on a 1.8-trillion-parameter mixture-of-experts model. The MI350 series is targeted for launch in the second half of 2025, with the MI400 series expected in 2026 using a further next-generation CDNA architecture.

## Key Claims

- The MI350 series uses CDNA 4 microarchitecture built on a 3nm manufacturing process.
- The MI355X GPU offers 288 GB of HBM3e memory and 8 TB/s memory bandwidth.
- Supports new FP4 and FP6 numeric formats for AI inference.
- MI355X peak performance: 9.2 petaflops FP8, 2.3 petaflops FP16, 74 petaflops FP4/FP6 (eight-GPU platform).
- AMD claims the eight-GPU MI350 platform provides up to 35× inference improvement over the MI300X platform (projected estimate).
- The MI350 platform can support models up to 4.2 trillion parameters, six times more than MI300X.
- The MI400 series is planned for 2026 with a new CDNA architecture.

## Relationships

- Implements the CDNA 4 microarchitecture documented in [[amd_cdna]].

## Sources

- [AMD Says Instinct MI325X Bests Nvidia H200, Vows Huge Uplift With MI350](raw/cache/321526d73cf105b3.md)
merge_draft_body -->

## [2026-07-17] pending | amd_cdna.md
target_page: amd_cdna.md
target_section: Key Claims
source: https://www.crn.com/news/ai/2024/amd-says-instinct-mi325x-bests-nvidia-h200-vows-huge-uplift-with-mi350
status: pending_review
proposed_update: Add that CDNA 3 is used in the Instinct MI325X (256GB HBM3e, 6TB/s memory) and CDNA 4 will power the Instinct MI350 series (288GB HBM3e, 8TB/s, 3nm). Cite the CRN source.

## [2026-07-17] merge_pending | amd_cdna_4.md
target_page: amd_cdna_4.md
canonical_name: AMD CDNA 4
colliding_name: AMD Instinct MI350 Series
source: https://www.amd.com/en/products/accelerators/instinct/mi350.html
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI350 Series

The AMD Instinct MI350 Series is a family of graphics processing units (GPUs) designed by AMD for data center artificial intelligence (AI) and high-performance computing (HPC) workloads. Announced in 2025, the MI350 series is built on the 4th generation AMD CDNA architecture, succeeding the MI300 series based on CDNA 3. The series includes multiple variants: the MI350P PCIe card with 128 compute units (CUs), 144 GB of HBM3E memory, and up to 4 TB/s bandwidth; and higher-end MI350X and MI355X platforms offering up to 288 GB of HBM3E memory and 8 TB/s bandwidth. The MI350 series introduces support for MXFP6 and MXFP4 low-precision datatypes to accelerate inference and training of generative AI models. The GPUs are supported by the open-source AMD ROCm software stack and are designed for drop-in compatibility with existing data center infrastructure.

## Key Claims

- Built on the 4th generation AMD CDNA architecture (CDNA 4).
- Introduces support for MXFP6 and MXFP4 low-precision datatypes for efficient AI inference and training.
- Top-end variants (MI350X/MI355X) offer up to 288 GB of HBM3E memory with 8 TB/s bandwidth.
- MI350P PCIe variant features 128 compute units, 144 GB HBM3E, and up to 4 TB/s peak theoretical memory bandwidth.
- Supported by AMD ROCm software stack, providing Day 0 support for frameworks like PyTorch, Hugging Face, and models like Llama 405B and GPT.
- Designed for drop-in compatibility with existing data center infrastructure and enables secure multi-tenant GPU sharing.
- Targets generative AI and agentic AI workloads as well as traditional HPC applications.

## Relationships

- The AMD Instinct MI350 series implements the 4th generation AMD CDNA microarchitecture (CDNA 4), which evolved from the compute-focused design principles of CDNA 1–3 described in [[amd_cdna]] and introduces new low-precision matrix formats and higher memory capacity.

## Sources

- [AMD Instinct™ MI350 Series GPUs](raw/cache/7c92212f6dba1da6.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_cdna_4.md
target_page: amd_cdna_4.md
canonical_name: AMD CDNA 4
colliding_name: AMD Instinct MI350 Series
source: https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/workload.html
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI350 Series

The AMD Instinct MI350 Series is a family of GPU accelerators based on the fourth-generation Compute DNA (CDNA 4) microarchitecture, targeting AI inference and high-performance computing workloads. It includes the MI350X and MI355X models, manufactured on TSMC N3P process for the compute chiplets and N6 for the I/O dies. The MI350 Series introduces significant architectural improvements over the preceding CDNA3-based MI300 Series: the compute unit count is reduced to 256 total active CUs (down from 304) but with 160 KB of local data share (LDS) per CU (up from 64 KB), doubled Matrix Core throughput for 16-bit and wider datatypes, native support for OCP MXFP8, MXFP6, and MXFP4 formats, and a shift from hardware TF32 to software emulation via BF16. Memory capacity reaches 288 GB of HBM3E with 8.0 TB/s peak bandwidth, and Infinity Fabric links operate at 38.4 Gbps. The architecture uses two I/O dies (compared to four on CDNA3) with a faster direct connection.

## Key Claims

- MI350X and MI355X GPUs are built on CDNA4 (gfx950) architecture, using TSMC N3P XCDs and N6 IODs.
- Total active compute units: 256, with 16,384 stream processors and 1,024 Matrix Cores.
- Maximum engine clock: 2,400 MHz.
- LDS per CU: 160 KB (up from 64 KB on CDNA3). L1 data cache is 32 KB; L2 cache is 4 MB per XCD; Infinity Cache is 256 MB.
- Memory: 288 GB HBM3E with 8.0 TB/s peak bandwidth.
- Peak theoretical performance: FP64 Vector 78.6 TF, FP32 Vector 157.3 TF, FP16/BF16 Matrix 2.5 PF (5.0 PF with sparsity), FP8 Matrix 5.0 PF (10 PF with sparsity), INT8 5.0 POPs (10 POPs with sparsity). MXFP8: 5.0 PF, MXFP6/MXFP4: 10 PF (via shared exponent per 32 elements).
- Native support for OCP FP8 variants (E5M2/E4M3), MXFP8, MXFP6, and MXFP4; TF32 is emulated in software via BF16.
- Power envelope: up to 1000W (MI350X) and 1400W (MI355X). Transistor count: 185 B.
- Partitioning modes: SPX (8 XCDs, 288 GB), DPX (4 XCDs, 144 GB, NPS2), QPX (2 XCDs, 72 GB, NPS2), CPX (1 XCD, 36 GB, NPS2). Most efficient mode: DPX + NPS2.
- Infinity Fabric link speed: 38.4 Gbps; P2P ring aggregate bandwidth: 1,075.2 GB/s; total peak aggregate I/O bandwidth: 1,203.2 GB/s.

## Relationships

- This page describes the MI350 Series which implements the CDNA4 microarchitecture, directly succeeding the CDNA3 architecture covered in [[amd_cdna]]. CDNA4 doubles the Matrix Core throughput for 16-bit and wider types and adds native MXFP8/MXFP6/MXFP4 support, whereas CDNA3 used the FNUZ FP8 variant and had 64 KB LDS per CU.

## Sources

- [AMD Instinct MI300 Series / MI350 Series workload optimization — ROCm Documentation](raw/cache/200c0a86713325b3.md)
merge_draft_body -->

## [2026-07-17] pending | amd_cdna.md
target_page: amd_cdna.md
target_section: Key Claims
source: https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/workload.html
status: pending_review
proposed_update: Add specific product details for MI300X and MI325X (CDNA3) from the ROCm documentation: 304 CUs, 19,456 stream processors, 1,216 Matrix Cores, 2,100 MHz max clock, 64 KB LDS, 192 GB HBM3 (MI300X) / 256 GB HBM3E (MI325X), 5.3 TB/s (MI300X) / 6.0 TB/s (MI325X) bandwidth, TF32 hardware support, FNUZ FP8 variant, 4 IODs, 153 B transistors, 750W power. Also add MI350 series as successor.

## [2026-07-17] merge_pending | amd_instinct_mi325x.md
target_page: amd_instinct_mi325x.md
canonical_name: AMD Instinct MI325X
colliding_name: AMD Instinct MI325X
source: https://awesomeagents.ai/hardware/amd-mi325x/
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI325X

The AMD Instinct MI325X is an AI accelerator based on the CDNA3 chiplet architecture, launched in October 2024 as a memory-upgraded evolution of the MI300X. It is equipped with 256 GB of HBM3e memory (33% more than the MI300X) and 6 TB/s of memory bandwidth (13% improvement over the predecessor), while retaining the same 304 compute units and 2.6 PFLOPS FP8 peak performance as the MI300X. Manufactured on TSMC 5nm (compute) and 6nm (I/O) nodes with a 1,000 W TDP, the MI325X uses the OAM (Open Accelerator Module) form factor and is designed for inference workloads on large language models such as Llama 2 70B and Mixtral, particularly in high-concurrency, large-batch scenarios where memory capacity becomes a binding constraint.

## Key Claims

- 256 GB HBM3e memory capacity (33% more than the MI300X) with 6 TB/s bandwidth (6,000 GB/s).
- Peak FP8 compute of 2,614.9 TFLOPS, identical to the MI300X; FP8 with sparsity reaches 5,229.8 TFLOPS.
- Same CDNA3 chiplet design and 304 compute units as the MI300X; the upgrade is entirely in memory.
- MLPerf Inference v5.0 results on Llama2 70B (8 GPU): within 3–7% of an NVIDIA H200 system; memory bandwidth advantage at high batch sizes flips the comparison.
- AMD internal benchmarks claim 40% higher throughput and 20–40% lower latency vs H200 on Mixtral and Llama 3.1.
- Form factor is OAM, allowing drop-in upgrades from MI300X with compatible firmware.
- Cloud rental ~$2.00–$2.25/hr per GPU (early 2026).
- 1,000 W TDP places it at the same power level as the NVIDIA B200, above the H200 (700 W) and above the MI300X (750 W).

## Relationships

- The AMD Instinct MI325X is a product instance of the CDNA3 architecture detailed in [[amd_cdna.md]]; it uses the same multi-chip module design and compute units as the MI300X but with upgraded HBM3e memory stacks, making it fully software-compatible with the earlier accelerator.

## Sources

- [AMD Instinct MI325X - 256GB CDNA3 for Inference | Awesome Agents](raw/cache/f301103b9c088449.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_rocm.md
target_page: amd_rocm.md
canonical_name: AMD ROCm
colliding_name: ROCm
source: https://wiki.gentoo.org/wiki/ROCm
status: pending_review
<!-- merge_draft_body
# ROCm

ROCm is an open software platform developed by AMD for heterogeneous computing, supporting a range of AMD GPUs including those based on the CDNA and RDNA microarchitectures. It provides an API and runtime environment for GPU-accelerated computing, with support for programming models such as HIP, OpenCL, and OpenMP. As an open-source ecosystem, ROCm is analogous to NVIDIA's CUDA platform, offering tools, libraries, and compilers for high-performance computing and machine learning workloads. ROCm targets discrete AMD GPUs from the GFX9 generation onward, covering GCN-3 through RDNA architectures. The platform is composed of drivers, runtimes, compilers (based on Clang/LLVM), and a suite of libraries prefixed with roc and hip.

## Key Claims

- ROCm is a brand name for an open software platform (ROCm open software platform) and an open platform ecosystem that includes hardware like FPGAs or other CPU architectures.
- In the Gentoo distribution, ROCm currently supports only AMDGPU hardware, though the platform itself is not limited to AMD.
- ROCm provides programming models HIP, OpenCL, and OpenMP, and is analogous to CUDA in providing a kernels-based GPU programming API.
- Officially supported hardware includes nearly all GFX9 and later GPU generations (GCN-3 Fiji chips through GCN-5 and all RDNA microarchitectures).
- Components of ROCm include: drivers/runtimes (amdgpu kernel module, roct-thunk-interface, rocr-runtime), programming models, compilers/tools (vanilla Clang >= 14.0.6), libraries (roc and hip packages), and deployment tools.
- Kernel configuration requires the AMD GPU driver (amdgpu), HSA kernel driver (for AMDKFD), and HMM-based shared virtual memory manager.
- User access to ROCm requires membership in the video group to access the /dev/kfd device.
- The rocm-smi tool provides system management interface for monitoring GPU temperature, power, clock speeds, and VRAM usage.

## Relationships

- ROCm is the software platform that supports AMD GPUs built on the [[amd_cdna]] microarchitecture, such as the Instinct accelerator series. ROCm provides the runtime and programming environment for CDNA-based compute units.

## Sources

- [ROCm - Gentoo wiki](raw/cache/a5b087e1be2d14bc.md)
merge_draft_body -->

## [2026-07-17] pending | amd_cdna.md
target_page: amd_cdna.md
target_section: Relationships
source: https://wiki.gentoo.org/wiki/ROCm
status: pending_review
proposed_update: Add relationship to ROCm: ROCm is the open software platform that provides the runtime and programming environment for CDNA-based AMD Instinct accelerators, supporting HIP, OpenCL, and OpenMP workloads on CDNA hardware.

## [2026-07-17] merge_pending | amd_cdna_4.md
target_page: amd_cdna_4.md
canonical_name: AMD CDNA 4
colliding_name: AMD Instinct MI350 Series
source: https://convergedigest.com/hot-chips-2025-amd-boosts-infinity-fabric/
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI350 Series

The AMD Instinct MI350 Series is a family of AI accelerator GPUs announced by AMD at Hot Chips 2025, based on the fourth-generation CDNA architecture (CDNA4). The series comprises two variants: the MI350X with a 1.0 kW TDP and the MI355X with a 1.4 kW TDP. Both variants feature 288 GB of HBM3E memory with 8 TBps bandwidth, built with 185 billion transistors using AMD's 3D stacking approach. The MI350 architecture employs two base dies on TSMC 6nm and eight Accelerator Complex Dies (XCDs) on TSMC 3nm, with a redesigned Infinity Fabric delivering 5.5 TBps die-to-die interconnect and seven Gen4 links for 1,075 GBps aggregate GPU-to-GPU bandwidth. Each GPU contains 256 CDNA4 compute units, supporting MXFP4 and MXFP6 formats, and sparse instructions for doubled throughput. The MI350 series targets both air-cooled and liquid-cooled Open Accelerator Modules (OAMs) for OCP racks, with hyperscale configurations supporting up to 128 liquid-cooled GPUs delivering 2.6 exaflops of FP4 compute and 36 TB of HBM3E memory.

## Key Claims

- 288 GB HBM3E memory with 8 TBps bandwidth per GPU.
- 185 billion transistors using AMD's 3D stacking, with two base dies (TSMC 6nm) and eight compute dies (TSMC 3nm).
- Redesigned Infinity Fabric: 5.5 TBps die-to-die interconnect and 1,075 GBps aggregate GPU-to-GPU bandwidth via seven Gen4 links.
- 256 CDNA4 compute units per GPU, doubling math throughput for key AI datatypes with support for MXFP4 and MXFP6; sparse instructions double throughput further.
- Inference performance up to 3x the MI300X and 1.3x more tokens/sec than NVIDIA B200.
- Training pre-training throughput up to 3.5x higher than MI300.
- Available as Open Accelerator Modules (OAM): air-cooled MI350X (1.0 kW TDP) and liquid-cooled MI355X (1.4 kW TDP).
- Hyperscale rack: up to 128 liquid-cooled GPUs delivering 2.6 exaflops FP4 and 36 TB of HBM3E memory.
- Enterprise rack: up to 64 air-cooled GPUs.
- Software support: ROCm 7 with Kubernetes and Slurm integration.

## Relationships

- The AMD Instinct MI350 Series is the first product to implement CDNA4, which extends the compute-focused architecture of the [[amd_cdna]] family with new matrix formats (MXFP4, MXFP6) and enhanced memory bandwidth. It succeeds the CDNA 3-based Instinct MI300 series.

## Sources

- [Hot Chips 2025: AMD Boosts Infinity Fabric - Converge Digest](raw/cache/26f1b36a2496b579.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_pollara_400.md
target_page: amd_pollara_400.md
canonical_name: AMD Pollara 400
colliding_name: Pensando Pollara 400
source: https://wccftech.com/amd-400gbe-speeds-industrys-first-uec-ready-pensando-pollara-400-ai-nic/
status: pending_review
<!-- merge_draft_body
# AMD Pensando Pollara 400

The AMD Pensando Pollara 400 is a 400 Gbps AI network interface card (NIC) designed by AMD through its Pensando networking division. It is the industry's first NIC to be described as Ultra Ethernet Consortium (UEC)-ready, supporting UEC-ready RDMA for high-performance scale-out AI networking. The Pollara 400 features a programmable P4 pipeline for flexible packet processing, and connects via a PCIe Gen5 x16 interface. It is intended to complement AMD's data center accelerator and processor families, such as the Instinct CDNA-based accelerators, to address networking bottlenecks in large-scale AI training and inference clusters.

## Key Claims

- Delivers 400 Gbps bandwidth, matching NVIDIA ConnectX-7 speeds.
- Offers up to 1.25x performance boost over baseline, with a 25% performance gain against RoCEv2 4 Qpairs and a 40% improvement versus RoCEv2 1 Qpair.
- Industry-first NIC to be UEC-ready, adopting the Ultra Ethernet Consortium open, interoperable, full-communications stack architecture.
- Built on a programmable P4 hardware pipeline, including a Table Engine (TE) and Match Processing Units (MPUs) for field manipulation.
- Integrates Virtual Address to Physical Address (va2pa) translation capability.
- Supports atomic memory operations adjacent to SRAM.
- Implements pipeline cache coherency via invalidate/update logic on an address range basis.
- Designed to address AI networking challenges such as poor link utilization from ECMP, network and node congestion, and packet loss.

## Relationships

- The Pensando Pollara 400 is part of AMD's data center networking portfolio, designed to work alongside Instinct accelerators based on the [[amd_cdna]] architecture for end-to-end AI infrastructure.

## Sources

- [AMD Delivers 400GbE Speeds With Industry's First "UEC-Ready ...](raw/cache/bdebbab11fd0fde4.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_pollara_400.md
target_page: amd_pollara_400.md
canonical_name: AMD Pollara 400
colliding_name: AMD Pensando Pollara 400 AI NIC
source: https://www.amd.com/en/products/network-interface-cards/pensando.html
status: pending_review
<!-- merge_draft_body
# AMD Pensando Pollara 400 AI NIC

The AMD Pensando Pollara 400 AI NIC is a network interface card designed by AMD for accelerating AI workloads in data centers. Based on the third-generation fully hardware programmable Pensando P4 engine, it achieves up to 400 Gigabit per second Ethernet speeds and is the industry's first Ultra Ethernet Consortium (UEC)-ready AI NIC. The card enables up to 8% faster AI job completion times through optimized GPU-GPU communication, 50% higher cluster uptime via enhanced reliability and congestion recovery, and up to 58% reduced network capital expenditure by supporting open multi-plane Ethernet architectures. It also provides intelligent packet spray, selective retransmission, path-aware congestion control, and supports both RoCEv2 and UEC RDMA for improved collective communication performance.

## Key Claims

- Up to 400 Gbps Ethernet speed using the Pensando P4 programmable engine.
- 8% faster AI job completion times compared to competing NICs.
- 50% higher effective cluster uptime through RAS enhancements and congestion recovery.
- 58% reduction in network capital expenditure via open multi-plane Ethernet architectures.
- Up to 10% better RoCEv2 collective communication performance compared to NVIDIA 400G RDMA NIC.
- Up to 25% higher collective communication operation performance with UEC RDMA versus RoCEv2.
- Fully programmable hardware and software enabling firmware updates for evolving UEC standards.
- Intelligent packet spray for load balancing, out-of-order packet handling with in-order message delivery, selective acknowledgment retransmission, and path-aware congestion control.
- Integrated UEC transport features into Ethernet for consistent AI workload performance.

## Relationships

- Shares the AMD ecosystem; pairs with AMD Instinct accelerators based on [[amd_cdna]] architecture for GPU-GPU communication in AI training clusters, where the Pollara 400 NIC offloads networking to improve job completion times and cluster utilization.

## Sources

- [AMD Pensando™ Pollara 400 AI NIC](raw/cache/8c063fa79585065f.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_instinct_mi325x.md
target_page: amd_instinct_mi325x.md
canonical_name: AMD Instinct MI325X
colliding_name: AMD Instinct MI325X
source: https://www.gadgetpilipinas.net/2024/10/amd-instinct-mi325x-accelerator/
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI325X

The AMD Instinct MI325X is a data center AI accelerator launched by AMD in Q4 2024 as part of the Instinct product line. Built on the CDNA 3 architecture, it features 304 compute units, 1216 matrix cores, and 19456 stream processors with a boost clock of 2100 MHz. The accelerator is equipped with 288 GB of HBM3E memory on an 8192-bit bus providing 6 TB/s of bandwidth, and includes full ECC support. It is designed to deliver high performance for AI training and inference, with AMD claiming 1.3x higher peak FP16 and FP8 compute than Nvidia's H200. The MI325X uses an OAM form factor and has a TDP of 750W, supported by 7 Infinity Fabric links for multi-GPU scaling.

## Key Claims

- Based on the AMD CDNA 3 architecture with 8 XCDs (compute dies) fabricated on TSMC N5, with an IOD on TSMC N6.
- 304 compute units, 1216 matrix cores, and 19456 stream processors at a boost clock of 2100 MHz.
- 288 GB of HBM3E memory on an 8192-bit bus delivering 6 TB/s bandwidth with full ECC support.
- FP16 matrix performance: 1307.4 TFLOPS; INT8 matrix performance: 2614.9 TOPS.
- 1.3x higher peak theoretical FP16 and FP8 compute performance than the Nvidia H200 accelerator.
- 1.8x more memory capacity and 1.3x more memory bandwidth than the Nvidia H200.
- Includes 7 Infinity Fabric links with a total bandwidth of 896 GB/s.
- TDP of 750W and OAM form factor.
- Launched in Q4 2024 with 153 billion transistors.

## Relationships

- Shares the CDNA 3 microarchitecture with other Instinct accelerators such as the MI300X; see [[amd_cdna]] for details on the architecture.

## Sources

- [AMD Launches Instinct MI325X Accelerator to Rival Nvidia's Blackwell](raw/cache/0f86256d7c2197b4.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_cdna.md
target_page: amd_cdna.md
canonical_name: AMD CDNA
colliding_name: AMD CDNA 3
source: https://zhaifeiyue.github.io/papers/amd-cdna3-whitepaper/detail.html
status: pending_review
<!-- merge_draft_body
# AMD CDNA 3

AMD CDNA 3 is the third-generation Compute DNA microarchitecture, introduced in 2023 for the AMD Instinct MI300 series accelerators. It marks a paradigm shift from monolithic or multi-chip module designs to a true heterogeneous 3D-stacked chiplet architecture. The flagship MI300X uses 12 chiplets: 8 Accelerator Complex Dies (XCD, TSMC 5nm) and 4 I/O Dies (IOD, TSMC 6nm), vertically stacked via 3D packaging. Each XCD contains 38 compute units (total 304 CU), 4 MB L2 cache, and a hardware scheduler. The four IODs integrate Infinity Fabric controllers, HBM PHYs, PCIe controllers, and a shared 256 MB Infinity Cache. This design enables unprecedented compute density, yielding 2,614.9 TFLOPS in FP8 matrix operations and 1,307.4 TFLOPS in FP16. The architecture first introduced support for OCP FP8 standard (E4M3/E5M2) and TF32 formats, along with 2:4 structured sparsity for matrix throughput doubling. The MI325X variant upgrades memory from 192 GB HBM3 (5.3 TB/s) to 256 GB HBM3E (6.0 TB/s) while maintaining identical compute performance. The MI300A APU variant replaces three XCDs with Zen4 CCDs, creating a unified CPU+GPU package sharing 128 GB HBM3 memory.

## Key Claims

- 8 XCD (TSMC 5nm) + 4 IOD (TSMC 6nm) 3D-stacked chiplet package, 12 total chiplets in MI300X.
- 304 compute units across 8 XCDs (38 per XCD, 2 disabled for yield).
- FP8 matrix performance: 2,614.9 TFLOPS; FP16 matrix: 1,307.4 TFLOPS; TF32 matrix: 490.3 TFLOPS.
- First AMD GPU to support OCP FP8 (E4M3/E5M2) and 2:4 structured sparsity.
- 256 MB Infinity Cache (memory-side cache) provides 17.2 TB/s aggregate bandwidth.
- HBM3 capacity: 192 GB (MI300X) / 256 GB HBM3E (MI325X).
- 7 Infinity Fabric links enable 8-GPU full interconnect within a node.
- MI300A APU: 6 XCD + 3 Zen4 CCDs + 4 IOD, 228 CU + 24 Zen4 cores sharing 128 GB HBM3.
- 2.4x FP64 matrix throughput vs H100 SXM5 (163.4 vs 66.9 TFLOPS).
- 32% higher FP16/FP8 throughput vs H100 SXM5.
- 2.4x memory capacity and 58% higher bandwidth vs H100 SXM5.
- Per-XCD memory bandwidth: 0.66 TB/s to HBM; 4.3 TB/s L2 read BW (6.5x amplification).

## Relationships

- [[amd_cdna]] covers the overall CDNA microarchitecture family (generations 1-3); this page provides the detailed technical specification for generation 3 specifically.
- [[nvidia_h100_hopper]] is the primary competitor; CDNA 3 claims 32% higher FP16/FP8 throughput and >2x memory capacity, though lacks a hardware Transformer Engine present in H100.
- [[amd_instinct_mi300x]] and [[amd_instinct_mi325x]] are the commercial products built on this architecture.

## Sources

- [AMD CDNA 3 Architecture White Paper — Feiyue KB](raw/cache/76e45c9ccb69f373.md)
merge_draft_body -->

## [2026-07-17] pending | amd_cdna.md
target_page: amd_cdna.md
target_section: Key Claims
source: https://zhaifeiyue.github.io/papers/amd-cdna3-whitepaper/detail.html
status: pending_review
proposed_update: Add specific CDNA 3 performance numbers (2,614.9 TFLOPS FP8, 256 MB Infinity Cache, chiplet breakdown) and correct the claim about 15 unique dies to 12 chiplets (8 XCD + 4 IOD) as per the white paper.

## [2026-07-17] merge_pending | amd_instinct_mi300_series.md
target_page: amd_instinct_mi300_series.md
canonical_name: AMD Instinct MI300 Series
colliding_name: AMD Instinct MI300X
source: https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI300X

The AMD Instinct MI300X is a high-performance GPU accelerator launched on December 6, 2023, based on the CDNA 3 architecture. It is designed for Generative AI and HPC workloads, featuring 19,456 stream processors, 1,216 matrix cores, 304 compute units, and 192 GB of HBM3 memory with 5.3 TB/s bandwidth. Manufactured using TSMC 5nm and 6nm FinFET processes, it supports FP8, FP16, BF16, TF32, FP32, FP64, and INT8 datatypes. The transistor count is 153 billion, and the typical board power consumption is 750W. The accelerator supports ROCm software and is available as an OAM module with PCIe 5.0 x16 connectivity, including eight Infinity Fabric links for coherent multi-GPU communication.

## Key Claims

- Architecture: CDNA 3, with 304 compute units and 1,216 matrix cores.
- Peak FP8 performance: 2.61 PFLOPs (5.22 PFLOPs with structured sparsity).
- Peak FP16 performance: 1.3 PFLOPs (2.6 PFLOPs with structured sparsity implied by FP8 ratio).
- Peak TF32 matrix: 653.7 TFLOPs (1,307.4 TFLOPs with sparsity).
- Peak FP32 matrix: 163.4 TFLOPs.
- Peak FP64: 81.7 TFLOPs (vector) / 163.4 TFLOPs (tensor).
- Peak INT8: 2.6 POPs (5.22 POPs with structured sparsity).
- Memory: 192 GB HBM3, 5.3 TB/s bandwidth, 8192-bit interface, ECC supported.
- Infinity Cache: 256 MB LLC.
- Power: 750W TBP.
- Up to 1.3X AI performance vs. NVIDIA H100 (peak TFLOPS comparisons shown).
- Up to 2.4X HPC performance vs. H100 (FP64 vector and tensor).
- 2.4X memory capacity and 1.6X memory bandwidth vs. H100.
- Fabric: 8 Infinity Fabric links, 128 GB/s peak bandwidth total.

## Relationships

- The MI300X implements the third-generation CDNA microarchitecture, sharing the compute-focused design and 3D chiplet integration of [[amd_cdna]]. This relationship grounds the MI300X as a concrete product instantiation of the architectural principles documented in the CDNA page.

## Sources

- [AMD Instinct™ MI300X Accelerators](raw/cache/1ec3cc01f6df4500.md)
merge_draft_body -->

## [2026-07-17] pending | amd_cdna.md
target_page: amd_cdna.md
target_section: Key Claims
source: https://www.techspot.com/news/104505-amd-admits-instinct-mi300x-ai-accelerator-cant-beat.html
status: pending_review
proposed_update: Add MLPerf Inference v4.1 benchmark results for the Instinct MI300X based on the LLama2-70B model. Include throughput numbers: with EPYC Genoa CPU, 8x MI300X achieved 21,028 tokens/s server mode, 23,514 tokens/s offline mode; with EPYC Turin, 22,021 tokens/s server mode, 24,110 tokens/s offline mode. Also note memory specs: 192 GB HBM3, 5.3 TB/s bandwidth. Compare to Nvidia H100 numbers provided in the source.

## [2026-07-17] merge_pending | amd_rocm.md
target_page: amd_rocm.md
canonical_name: AMD ROCm
colliding_name: AMD ROCm LLM Inference Optimization
source: https://github.com/MayurVijayPatil/amd-llm-rocm
status: pending_review
<!-- merge_draft_body
# AMD ROCm LLM Inference Optimization

AMD ROCm LLM Inference Optimization refers to the set of techniques and software stack components used to accelerate large language model (LLM) inference on AMD Instinct GPUs, primarily targeting the MI300X with 192 GB HBM3 memory. The core pipeline combines vLLM with PagedAttention, FlashAttention-2 implemented via ROCm HIP kernels, continuous batching, and AWQ INT4 quantisation. Benchmark projections calibrated to AMD's published MI300X specifications show a cumulative 2.80× throughput improvement over a naive HuggingFace BF16 baseline across models ranging from 3.8B to 70B parameters. The optimised pipeline achieves 96–102% of published NVIDIA H100 SXM throughput at AWQ INT4, with parity attributed to the MI300X's 5.3 TB/s HBM3 bandwidth advantage on memory-bandwidth-bound decode workloads. The methodology is documented in an open white paper and reproducibility suite hosted on GitHub, with a simulation mode that does not require an AMD GPU to reproduce the tables and figures.

## Key Claims

- The fully optimised pipeline (vLLM + FlashAttention-2 + continuous batching + AWQ INT4) delivers a projected 2.80× throughput improvement over the naive BF16 baseline on AMD MI300X.
- Projected MI300X throughput for Mistral-7B reaches 1,152 tokens/s, LLaMA-3-8B achieves 1,089 tokens/s, and LLaMA-3-70B reaches 139 tokens/s at AWQ INT4.
- The MI300X's 5.3 TB/s HBM3 bandwidth enables single-card 70B inference, eliminating the need for tensor parallelism across multiple GPUs.
- Projected MI300X throughput reaches 96–102% of published H100 SXM throughput at AWQ INT4 on memory-bandwidth-bound decode workloads.
- The benchmark suite includes a simulation mode validated against MLCommons MLPerf Inference v4.0 reference data with residual error below 5%.

## Relationships

- The MI300X GPU that serves as the primary target for this optimization study is based on the [[amd_cdna]] microarchitecture (CDNA 3), which provides the compute units, HBM3 memory controller, and Infinity Fabric interconnect leveraged by the ROCm software stack.

## Sources

- [GitHub - MayurVijayPatil/amd-llm-rocm: White paper ...](raw/cache/8aeaea8865feedd7.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_instinct_mi300_series.md
target_page: amd_instinct_mi300_series.md
canonical_name: AMD Instinct MI300 Series
colliding_name: AMD Instinct MI300
source: https://wccftech.com/amd-unveils-instinct-mi300-apus-mi300a-mi300x-flavors-cdna-3-gpu-up-to-24-zen-4-cores-192-gb-hbm3-153-billion-transistors/
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI300

The AMD Instinct MI300 series is a family of high-performance accelerators developed by AMD, integrating CDNA 3 GPU architecture with, in the case of the MI300A, up to 24 Zen 4 CPU cores on a unified chiplet package. Launched in 2023, the MI300 series represents AMD's first integrated x86 CPU and GPU package, designed for exascale supercomputing and generative AI workloads. The series includes two variants: the MI300A, a combined CPU-GPU APU (Accelerated Processing Unit) targeting HPC and AI, and the MI300X, a GPU-only accelerator optimized for large language model inference and training. Both variants utilize 3D chiplet packaging with up to 15 unique dies on 5nm and 6nm process nodes, housing a total of 153 billion transistors. The MI300X supports up to 192 GB of HBM3 memory with an 8192-bit bus, while the MI300A supports 128 GB. The accelerator uses a new unified memory architecture that connects the CPU and GPU to a shared HBM3 pool, eliminating redundant memory copies and reducing total cost of ownership. The MI300 series is socket-compatible with the SH5 socket and can be deployed in an eight-accelerator platform using the 4th-gen Infinity Fabric and CXL 3.0 interconnect. The MI300A began sampling in mid-2023, with the MI300X sampling in Q3 2023 and both ramping in Q4 2023.

## Key Claims

- 153 billion transistors across multiple 3D chiplets on 5nm and 6nm processes.
- MI300X: up to 304 CDNA 3 compute units (24,576 cores) and 192 GB HBM3 memory.
- MI300A: 6 XCDs (up to 228 CUs) and 3 CCDs (up to 24 Zen 4 cores) with 128 GB HBM3.
- 8x AI performance (TFLOPs) improvement over the previous-generation Instinct MI250X (CDNA 2).
- 5x performance per watt improvement over CDNA 2.
- Unified memory architecture (UMAA) enabling both CPU and GPU to access a single HBM3 pool without redundant copies.
- Compatibility with 4th-gen Infinity Fabric, CXL 3.0, and new SH5 socket.
- Capable of running a 40B parameter model (Falcon-40) on a single MI300X accelerator.
- MI300A sampling in 2023, MI300X sampling Q3 2023, production ramp in Q4 2023.

## Relationships

- Uses the [[amd_cdna|CDNA 3 microarchitecture]] as the GPU component, with advanced 3D chiplet integration and a compute-focused unified memory architecture that removes graphics hardware in favor of dedicated matrix compute units.

## Sources

- [AMD Unveils Instinct MI300 APUs In MI300A & MI300X Flavors: CDNA...](raw/cache/c88d1a5781afbd79.md)
merge_draft_body -->

## [2026-07-17] merge_pending | mlperf_inference.md
target_page: mlperf_inference.md
canonical_name: MLPerf Inference
colliding_name: MLPerf Inference
source: https://docs.mlcommons.org/inference/
status: pending_review
<!-- merge_draft_body
# MLPerf Inference

MLPerf Inference is a benchmark suite developed by MLCommons to measure the performance of machine learning inference on various hardware platforms. It defines a set of models, datasets, accuracy targets, and latency constraints across multiple task categories including image classification, text-to-image generation, object detection, medical image segmentation, language processing, text summarization, recommendation, graph neural networks, and automotive 3D object detection. The v5.0 round includes models such as ResNet50-v1.5, Stable Diffusion, Retinanet, 3D-UNet, BERT-Large, LLAMA2-70B, GPT-J, Mixtral-8x7B, DLRM_v2, R-GAT, and PointPainting. Benchmarks are categorized into Datacenter and Edge submission categories, with specific high accuracy variants for certain models requiring 99.9% of reference accuracy.

## Key Claims

- **ResNet50-v1.5**: Dataset Imagenet-2012 (224x224), 25.6 million parameters, 3.8 billion FLOPs, reference accuracy 76.46% ACC, server latency constraint 15ms. Datacenter and Edge category.
- **BERT-Large**: Dataset SQuAD v1.1 (384 sequence length), 340 million parameters, approximately 128 billion FLOPs, reference F1 score 90.874%, server latency constraint 130ms. Edge category.
- **LLAMA2-70B**: Dataset OpenORCA (GPT-4 split, max_seq_len=1024), 70 billion parameters, approximately 500 trillion FLOPs, Rouge1 44.4312, Rouge2 22.0352, RougeL 28.6162, tokens per sample 294.45. Server latency constraints: TTFT 2000ms, TPOT 200ms. Datacenter category.
- **GPT-J**: Dataset CNN Daily Mail v3.0.0, 6 billion parameters, approximately 148 billion FLOPs, Rouge1 42.9865, Rouge2 20.1235, RougeL 29.9881, gen_len 4,016,878. Server latency constraint 20s.
- **Mixtral-8x7B**: Datasets OpenORCA, GSM8K, MBXP (5k samples each, max_seq_len=2048), 47 billion parameters, reference accuracy: OpenORCA Rouge1 45.4911/Rouge2 23.2829/RougeL 30.3615, GSM8K accuracy 73.78%, MBXP accuracy 60.12%.
- **DLRM_v2**: Dataset Synthetic Multihot Criteo, approximately 23 billion parameters, reference accuracy AUC 80.31%, server latency constraint 60ms.
- **Stable Diffusion**: Dataset subset of Coco2014, 3.5 billion parameters, 1.28-2.4 trillion FLOPs, reference CLIP 31.74981837 and FID 23.48046692, required accuracy within 0.2% CLIP and 2% FID of reference.
- **Retinanet**: Dataset OpenImages, reference accuracy 0.3755 mAP, server latency constraint 100ms, high accuracy variant available.
- **3D-UNet**: Dataset KiTS2019, 32.5 million parameters, 100-300 billion FLOPs, reference mean DICE score 0.86330, equal issue mode true.
- **R-GAT**: Dataset Illinois Graph Benchmark heterogeneous validation, reference accuracy 72.86%, no server latency constraint.
- **PointPainting**: Dataset Waymo, 44 million parameters, 3 trillion FLOPs, reference mAP 54.25%.

## Relationships

No specific relationship to visible context pages is identified in this source.

## Sources

- [MLPerf Inference Benchmarks - MLPerf Inference Documentation](raw/cache/52b8915814d8c477.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_cdna_4.md
target_page: amd_cdna_4.md
canonical_name: AMD CDNA 4
colliding_name: AMD CDNA 4
source: https://github.com/jhinpan/ROCmKernelWiki/blob/main/sources/docs/doc-cdna4-whitepaper.md
status: pending_review
<!-- merge_draft_body
# AMD CDNA 4

AMD CDNA 4 is the fourth-generation compute-oriented GPU microarchitecture from AMD, designed for data center AI and HPC workloads. Introduced in the Instinct MI350 and MI355X accelerators, CDNA 4 is manufactured on TSMC N3P and consists of XCDs (accelerator complex dies) each containing 36 physical compute units (32 active) and 4 MB of L2 cache. Up to eight XCDs can be combined for a total of 256 active CUs. The MI355X variant ships with 288 GB of HBM3E memory delivering up to 8 TB/s bandwidth. CDNA 4 introduces new matrix numeric formats including OCP-FP8 (distinct from CDNA3's FNUZ FP8), MXFP6, and MXFP4, alongside standard FP16, BF16, and INT8. Peak matrix throughput reaches 10 PF for MXFP6/MXFP4 formats.

## Key Claims

- Each XCD contains 36 physical compute units (32 active) and 4 MB L2 cache, fabricated on TSMC N3P.
- Up to 8 XCDs per device, yielding 256 active CUs total.
- MI355X ships with 288 GB HBM3E at up to 8 TB/s bandwidth.
- Peak matrix throughput (Table 1): FP16/BF16 2.5 PF, OCP-FP8 5.0 PF, INT8 5.0 POPS, MXFP6/MXFP4 10 PF (dense).
- OCP-FP8 is the Open Compute Project FP8 encoding, distinct from the FNUZ FP8 format used in CDNA 3.

## Relationships

- CDNA 4 is the fourth generation of the [[amd_cdna]] microarchitecture family, building upon the chiplet and multi-XCD design of CDNA 3 while introducing new matrix numeric formats such as OCP-FP8 and MXFP6/MXFP4 and moving to a TSMC N3P process node.

## Sources

- [ROCmKernelWiki/sources/docs/doc-cdna4-whitepaper.md ... - GitHub](raw/cache/c264d64d9f2ebaff.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_instinct_mi325x.md
target_page: amd_instinct_mi325x.md
canonical_name: AMD Instinct MI325X
colliding_name: AMD Instinct MI325X
source: https://www.amd.com/en/newsroom/press-releases/2024-10-10-amd-delivers-leadership-ai-performance-with-amd-in.html
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI325X

The AMD Instinct MI325X is an AI accelerator from AMD based on the CDNA 3 architecture, announced in October 2024 as part of AMD's annual accelerator roadmap. It features 256 GB of HBM3E memory delivering 6.0 TB/s bandwidth, which represents a 1.8× capacity and 1.3× bandwidth increase over the NVIDIA H200. The accelerator also offers 1.3× peak theoretical FP16 and FP8 compute performance compared to the H200. It is designed for generative AI workloads including foundation model training, fine-tuning, and inference. Production shipments are scheduled for Q4 2024, with system availability from partners such as Dell, HPE, Lenovo, and Supermicro beginning in Q1 2025. The MI325X is supported by AMD's ROCm open software stack and integrates into the wider AMD Pensando networking ecosystem.

## Key Claims

- 256 GB HBM3E memory capacity with 6.0 TB/s bandwidth.
- 1.8× memory capacity and 1.3× bandwidth versus NVIDIA H200.
- 1.3× peak theoretical FP16 and FP8 compute performance versus H200.
- Up to 1.3× inference performance on Mistral 7B at FP16 compared to H200.
- Up to 1.2× inference performance on Llama 3.1 70B at FP8 compared to H200.
- Up to 1.4× inference performance on Mixtral 8x7B at FP16 compared to H200.
- Built on AMD CDNA 3 architecture.
- Production shipments in Q4 2024; system availability in Q1 2025 from multiple OEMs.
- Supports FP8 datatype, Flash Attention 3, Kernel Fusion, and other ROCm 6.2 features.

## Relationships

- The MI325X is built on the [[amd_cdna]] CDNA 3 architecture, inheriting its compute-focused design and chiplet packaging approach.

## Sources

- [AMD Delivers Leadership AI Performance with AMD Instinct MI325X ...](raw/cache/78ddb561e5d2b52a.md)
merge_draft_body -->

## [2026-07-17] pending | amd_cdna.md
target_page: amd_cdna.md
target_section: Key Claims
source: https://www.amd.com/en/newsroom/press-releases/2024-10-10-amd-delivers-leadership-ai-performance-with-amd-in.html
status: pending_review
proposed_update: Add claim: 'Used in the AMD Instinct MI325X accelerator (announced Oct 2024), which provides 256GB HBM3E and 6.0TB/s bandwidth, and delivers up to 1.3x inference performance uplift over H200 in LLM workloads.'

## [2026-07-17] merge_pending | amd_instinct.md
target_page: amd_instinct.md
canonical_name: AMD Instinct
colliding_name: AMD Instinct
source: https://grokipedia.com/page/AMD_Instinct
status: pending_review
<!-- merge_draft_body
# AMD Instinct

AMD Instinct is a family of high-performance GPU accelerators developed by Advanced Micro Devices (AMD) for data center applications, specifically optimized for artificial intelligence (AI), high-performance computing (HPC), and machine learning workloads. These accelerators leverage the CDNA (Compute DNA) architecture, distinct from the consumer-oriented RDNA series, to deliver exceptional compute density, memory bandwidth, and efficiency for scalable solutions in generative AI training, inference, scientific simulations, and large-scale data processing. The Instinct lineup includes successive generations such as the MI200, MI300, and MI350 series, each incorporating advanced Matrix Core Technologies and support for a wide range of data precisions including FP64, FP16, BF16, and emerging formats like MXFP4 and MXFP6. The platform is supported by the open-source ROCm software stack, providing programming models, libraries, and tools for developer accessibility.

## Key Claims

- The Instinct MI300X features 192 GB of HBM3 memory, while the MI325X provides 256 GB of HBM3E with up to 6 TB/s bandwidth.
- The MI300A is an APU that integrates Zen 4 CPU cores for unified memory access between CPU and GPU.
- The MI350 series, launched in 2025, introduces next-generation datatypes for improved AI efficiency.
- AMD Instinct accelerators power the El Capitan supercomputer.
- In late 2025, Alibaba ordered 40,000–50,000 units of the China-specific MI308 variant (a compliant version of the MI300X) with US export approval for AI large model training.
- AMD collaborated with Tata Consultancy Services to deploy the 'Helios' rack-scale AI architecture in India, using MI455X GPUs and supporting up to 200 MW capacity.
- The platform supports high-bandwidth memory variants (HBM3, HBM3E) and scales to thousands of GPUs for massive parallelism.

## Relationships

- This page describes the AMD Instinct product family, which implements the [[amd_cdna]] microarchitecture. The CDNA page covers the architectural details of the CDNA generations (CDNA 1–3) that power Instinct accelerators, including matrix compute units, chiplet packaging, and HBM integration.

## Sources

- [AMD Instinct - Grokipedia](raw/cache/98ad1ba7c7e63374.md)
merge_draft_body -->

## [2026-07-17] merge_pending | ampere_ampereone.md
target_page: ampere_ampereone.md
canonical_name: Ampere AmpereOne
colliding_name: AmpereOne
source: https://www.servethehome.com/ampereone-with-192-cores-128x-pcie-gen5-lanes-and-ddr5-in-2023-arm/
status: pending_review
<!-- merge_draft_body
# AmpereOne

AmpereOne is a custom-designed server processor architecture by Ampere Computing, introduced in 2023 as the successor to the Ampere Altra family. It features 136 to 192 custom cores (not based on Arm Neoverse) with private L1 and 2 MB L2 caches, an 8-channel DDR5 memory controller, 128 PCIe Gen5 lanes, and support for Bfloat16, confidential computing, and nested virtualization. Manufactured with a sea-of-cores design using chiplets for memory and I/O, AmpereOne targets cloud-native workloads requiring high core density and power efficiency without simultaneous multithreading (SMT).

## Key Claims

- AmpereOne offers 136 to 192 custom-designed Arm ISA cores, moving away from stock Arm Neoverse cores.
- Each core has private L1 cache and 2 MB of private L2 cache, improving single-core performance isolation.
- Memory subsystem: 8-channel DDR5 memory controller, providing significant bandwidth increase over previous generation.
- PCIe Gen5 support with 128 total lanes, doubling bandwidth compared to PCIe Gen4.
- Architecture supports Bfloat16 for AI inference workloads.
- Includes confidential computing and nested virtualization capabilities.
- Designed with a sea-of-cores center and memory/I/O chiplets on the edge, analogous to a reverse of AMD EPYC Rome architecture.
- Focus on single-socket deployments for high core density per rack, with performance efficiency gains via voltage/frequency scaling.
- Compared to AMD EPYC Genoa, AmpereOne claims better AI workload performance on certain benchmarks due to Bfloat16 support and high core count.

## Relationships

No specific relationship to visible context pages.

## Sources

- [AmpereOne with 192 Cores 128x PCIe Gen5 Lanes and DDR5 in 2023](raw/cache/ab28ab896b759639.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_cdna_4.md
target_page: amd_cdna_4.md
canonical_name: AMD CDNA 4
colliding_name: AMD Instinct MI355X
source: https://rocm.blogs.amd.com/artificial-intelligence/mlperf-training-v5.1/README.html
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI355X

The AMD Instinct MI355X is a GPU accelerator based on the AMD CDNA 4 architecture, announced as part of the MI350 series. It is designed for AI and HPC workloads, featuring native FP4 precision support delivering up to 20 petaflops, 288 GB of HBM3e memory with 8 TB/s bandwidth, and liquid cooling for sustained performance. The MI355X was first demonstrated in AMD's MLPerf Training v5.1 submission in November 2025, running Llama 3.1 8B pretraining and Llama 2 70B LoRA finetuning benchmarks.

## Key Claims

- First MLPerf Training results on AMD Instinct MI355X GPU (MLPerf Training v5.1, November 2025).
- AMD led the development of the new Llama 3.1 8B pretraining benchmark, designed as an accessible version of Llama 3.1 405B.
- Delivers up to 20 petaflops of FP4 performance.
- Provides 288 GB of HBM3e memory with 8 TB/s memory bandwidth.
- Supports liquid cooling for thermal efficiency and sustained peak performance.
- Utilizes the AMD CDNA 4 architecture.

## Relationships

- The MI355X is the top-tier model of the AMD Instinct MI350 series and is built on the [[amd_cdna]] CDNA 4 microarchitecture, succeeding the CDNA 3 generation used in the MI300X.
- The GPU was showcased alongside the AMD ROCm software ecosystem, which provides the open platform for AI development on AMD hardware.

## Sources

- [Technical Dive into AMD MLPerf Training v5.1 Submission — ROCm Blogs](raw/cache/83dc6a4f2e8d7c63.md)
merge_draft_body -->

## [2026-07-17] merge_pending | rdna_3.md
target_page: rdna_3.md
canonical_name: RDNA 3
colliding_name: RDNA
source: https://www.wikiwand.com/en/RDNA_(microarchitecture)
status: pending_review
<!-- merge_draft_body
# RDNA

RDNA (Radeon DNA) is a graphics processing unit (GPU) microarchitecture and instruction set architecture developed by AMD as the successor to the Graphics Core Next (GCN) architecture. First launched on July 7, 2019, with the Radeon RX 5000 series, RDNA introduced significant changes including a native wavefront width of 32 threads (down from 64 in GCN), single-cycle instruction issue (up from one instruction every four cycles), and a workgroup processor (WGP) that combines two compute units to improve compute power and memory bandwidth. The architecture is fabricated on TSMC N7, N6, N5, and N4 nodes and spans four generations: RDNA 1 (Navi 1x), RDNA 2 (Navi 2x), RDNA 3 (Navi 3x), and RDNA 4 (Navi 4x). It also serves as the basis for the GPUs in the PlayStation 5, Xbox Series X/S, and Samsung Exynos 2200.

## Key Claims

- RDNA supports both wavefront sizes of 32 and 64 threads, whereas GCN used only 64 threads per wavefront.
- Instruction issue rate improved from one instruction per wave every four cycles in GCN to one instruction per wave every cycle in RDNA.
- The workgroup processor (WGP) replaces the compute unit (CU) as the basic shader computation unit; each WGP encompasses 2 CUs, enabling more compute power and memory bandwidth per workgroup.
- Primitive shaders, which were present but disabled in GCN hardware, are compiler-controlled and operational in RDNA.
- The display controller supports Display Stream Compression 1.2a, enabling 4K@240 Hz, HDR 4K@120 Hz, and HDR 8K@60 Hz output.
- RDNA 1 chips include Navi 10, Navi 12, and Navi 14, used in a range of desktop and mobile Radeon RX graphics cards.

## Relationships

- [[amd_cdna]] — RDNA is the consumer graphics-oriented counterpart to AMD's compute-focused CDNA architecture. While both are modern AMD GPU microarchitectures that diverged from GCN, CDNA targets data-center compute with matrix-hardware focus, whereas RDNA targets gaming and consumer workloads with a full graphics pipeline.

## Sources

- [RDNA (microarchitecture) - Wikiwand](raw/cache/c5bfb31c4b6a4a43.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_infinity_fabric.md
target_page: amd_infinity_fabric.md
canonical_name: AMD Infinity Fabric
colliding_name: AMD Infinity Fabric
source: https://www.amd.com/en/blogs/2025/engineering-the-future-of-ai.html
status: pending_review
<!-- merge_draft_body
# AMD Infinity Fabric

AMD Infinity Fabric is a system-wide interconnect architecture developed by AMD that unifies communication among CPUs, GPUs, and accelerators across chiplet, node, and rack scales. Originally evolving from a CPU-focused interconnect, it has progressed through five generations: Gen3 powered the Frontier exascale supercomputer; Gen4 enabled the El Capitan system and introduced heterogeneous chiplet designs; and Gen5 now serves as the backbone for the upcoming AMD Instinct MI450 series and "Helios" rack deployments, extending connectivity from in-package chiplets to full rack-scale AI systems. Infinity Fabric is a critical component of AMD's architecture-first strategy, combining high-speed SerDes interconnects and advanced chiplet packaging to deliver scalable compute performance for AI and HPC workloads.

## Key Claims

- AMD has invested in silicon photonics R&D since 2017 to overcome the power-performance wall of electrical I/O and enable orders-of-magnitude improvements in bandwidth and energy efficiency.
- Infinity Fabric Gen3 was first deployed in the Frontier exascale supercomputer, marking its initial large-scale use.
- Infinity Fabric Gen4 enabled the world's fastest supercomputer, El Capitan, and introduced true heterogeneous chiplet-based design.
- Infinity Fabric Gen5 underpins a leadership product portfolio across scale-in, scale-up, and scale-out systems, and serves as the backbone for the AMD Instinct MI450 series with the Helios rack.
- Each Infinity Fabric generation has delivered significantly higher bandwidth and greater in-package and system capabilities.
- AMD pioneered multi-die architecture with early chiplet and 2.5D packaging innovations, and continues to invest in 2.5D, 3D, and hybrid bonding.
- The combination of Infinity Fabric, high-speed SerDes, and advanced packaging enables systems to scale efficiently from single nodes to full rack-scale AI systems.

## Relationships

- AMD Infinity Fabric is the system-wide interconnect used in AMD Instinct accelerators such as the CDNA-based MI300 series, connecting chiplets and enabling scale-out to rack-level systems. The [[amd_cdna]] compute architecture benefits directly from Infinity Fabric's bandwidth and scalability for multi-die communication.

## Sources

- [Engineering the Future of AI: How AMD Interconnects, Infinity ...](raw/cache/9624ea3ddebfd56a.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_infinity_fabric.md
target_page: amd_infinity_fabric.md
canonical_name: AMD Infinity Fabric
colliding_name: Infinity Fabric
source: https://cr0x.net/en/infinity-fabric-performance-bottlenecks/
status: pending_review
<!-- merge_draft_body
# Infinity Fabric

Infinity Fabric is AMD's scalable interconnect architecture that moves data and coherence traffic between CPU cores, caches, memory controllers, and I/O, enabling the chiplet approach to behave like a single logical CPU. It links the various components of AMD's CPU chiplets and acts as chiplet-chiplet, CPU-CPU, and CPU-GPU interconnect, providing high-bandwidth, low-latency connectivity for HPC and AI workloads. Originally a CPU interconnect, it has evolved into a cohesive system fabric that unifies compute across heterogeneous and distributed computing systems at scale. Infinity Fabric includes various interconnect links (Quad, Dual, Single, xGMI) achieving up to 81% of theoretical bandwidth while maintaining low latency in HPC deployments. Performance relies on tailored software interfaces such as hipMemcpy, RCCL, MPI, and NUMA-aware programming to optimize scheduling, data movement, and real-world application speedups.

## Key Claims

- Infinity Fabric is a modular, packet-based system fabric with link types Quad, Dual, Single, and xGMI, achieving up to 81% of theoretical bandwidth with low latency in HPC deployments.
- It supports coherent communications and resource sharing between AMD CPU and GPU solutions, enabling increased performance, lower latencies, and lower power consumption (Third-Gen Infinity Architecture).
- Infinity Fabric serves as chiplet-chiplet, CPU-CPU, and CPU-GPU interconnect, forming the core of AMD's scalable CPU architecture and heterogeneous system integration.
- Performance relies on tailored software interfaces: hipMemcpy, RCCL, MPI, and NUMA-aware programming for optimized scheduling and data movement.
- Third-Gen Infinity Architecture enables coherent CPU-GPU communication, allowing for a unified compute platform.

## Relationships

- [[amd_cdna]] – Infinity Fabric serves as the coherent interconnect that enables CPU-GPU communication in AMD Instinct accelerators employing CDNA, as noted in the third-generation Infinity Architecture. This allows the chiplet-based compute units in CDNA 3 to share resources with AMD EPYC CPUs, supporting heterogeneous computing workloads.

## Sources

- [Infinity Fabric: the invisible link that can make-or-break performance...](raw/cache/ca6e8e6a3ca4dd58.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_infinity_fabric.md
target_page: amd_infinity_fabric.md
canonical_name: AMD Infinity Fabric
colliding_name: Infinity Fabric
source: https://diversedaily.com/infinity-fabric-interconnect-scalability-and-performance-in-amd-chiplet-based-designs/
status: pending_review
<!-- merge_draft_body
# Infinity Fabric

Infinity Fabric is a scalable interconnect architecture developed by AMD for its chiplet-based processor designs. It facilitates high-bandwidth, low-latency communication between chiplets within a single processor package and extends that connectivity to multiple nodes in high-performance computing (HPC) systems. The architecture supports coherent communication among CPUs, GPUs, and other computing resources, enabling scalable performance in products such as the EPYC server processors and Instinct MI350 series GPUs. Infinity Fabric is a critical component of AMD's chiplet strategy, connecting clusters of cores more efficiently than legacy crossbar-based interconnects.

## Key Claims

- Infinity Fabric is AMD's scalable interconnect architecture for chiplet-based designs.
- It provides high-bandwidth, low-latency connectivity within a node and across multiple nodes in HPC systems.
- It enables coherent communication among CPUs, GPUs, and other computing resources.
- In EPYC packages, Infinity Fabric replaces legacy crossbar interconnects for better scalability.
- It is used to link multiple AMD Instinct MI350 GPUs efficiently.

## Relationships

- Infinity Fabric is the interconnect technology used to link multiple AMD Instinct MI350 GPUs, which are based on the [[amd_cdna]] microarchitecture.

## Sources

- [Infinity Fabric Interconnect: Scalability and Performance in AMD...](raw/cache/ac3caf1276aebd3b.md)
merge_draft_body -->

## [2026-07-17] merge_pending | nvidia_blackwell_platform.md
target_page: nvidia_blackwell_platform.md
canonical_name: NVIDIA Blackwell Platform
colliding_name: NVIDIA Blackwell
source: https://www.servethehome.com/nvidia-blackwell-platform-at-hot-chips-2024/
status: pending_review
<!-- merge_draft_body
# NVIDIA Blackwell

NVIDIA Blackwell is a GPU platform architecture for AI and high-performance computing, announced in 2024 and detailed at Hot Chips 2024. The Blackwell platform encompasses the GPU compute die, the Grace CPU (Arm-based) via NVLink-C2C interconnect, NVSwitch for scaling, and networking components such as Spectrum-X and BlueField-3. The GPU die itself uses NVIDIA’s High-Bandwidth Interface (NV-HBI) to deliver 10 TB/s of bandwidth between two dies. The GB200 Superchip pairs one Grace CPU with two Blackwell GPUs in a half‑width form factor; a compute tray housing two such superchips provides four GPUs and two Arm CPUs. Blackwell introduces FP4 and FP6 arithmetic precision, supported by NVIDIA Quasar Quantization to decide when lower precision can be used with minimal accuracy loss. The platform scales to the GB200 NVL72 configuration, a 72‑GPU system designed for trillion‑parameter AI models, and can also be configured as a 36‑GPU NVL36 variant for data centers with power constraints (120 kW racks). NVIDIA also showed a roadmap including 1.6 Tb/s ConnectX-9 networking in 2026.

## Key Claims

- The NV-HBI provides 10 TB/s of bandwidth between the two GPU dies (source: NVIDIA Blackwell Hot Chips 2024 presentation).
- Blackwell supports FP4 and FP6 precision alongside existing FP16 and BF16; Quasar Quantization determines when lower precision is viable.
- The GB200 Superchip combines one Grace CPU (Arm) and two Blackwell GPUs in a half-width platform; two superchips per compute tray yield four GPUs and two CPUs.
- The NVSwitch chip and tray enable scaling from 8 GPUs (NVLink 2016) to 72 GPUs in the current generation.
- The GB200 NVL72 targets trillion‑parameter AI models and consumes up to 120 kW per rack; an NVL36 variant exists for more power‑constrained environments.
- NVIDIA’s roadmap shows 1.6 Tb/s ConnectX-9 networking in 2026, requiring PCIe Gen7 support.
- Blackwell achieves close-to-BF16 inference performance when using FP4 precision on certain tasks (e.g., image generation).

## Relationships

- Competes with [[amd_cdna]] in the data center AI accelerator market; both target large‑scale matrix compute, but Blackwell introduces FP4/FP6 support and a proprietary NVLink‑based scaling fabric that spans 72 GPUs, whereas CDNA relies on Infinity Fabric and a chiplet approach.

## Sources

- [NVIDIA Blackwell Platform at Hot Chips 2024 - ServeTheHome](raw/cache/95d4992aefd6bbe3.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_instinct.md
target_page: amd_instinct.md
canonical_name: AMD Instinct
colliding_name: AMD Instinct
source: https://en.wikipedia.org/wiki/AMD_Instinct
status: pending_review
<!-- merge_draft_body
# AMD Instinct

AMD Instinct is a brand of data center GPUs developed by AMD for deep learning, artificial neural network acceleration, and high-performance computing (HPC) applications. Originally introduced as AMD Radeon Instinct in 2016 and later rebranded without the Radeon prefix in 2020, the product line replaced AMD's FirePro S series. The Instinct family directly competes with Nvidia's Tesla data center GPUs and Intel's Xeon Phi and Data Center GPU lines. The brand encompasses multiple generations based on Graphics Core Next (GCN), Compute DNA (CDNA), and CDNA 2/3 architectures, from the early MI6, MI8, and MI25 cards to the current MI300X and future MI350X accelerators. AMD Instinct GPUs are used in some of the world's fastest supercomputers, including Frontier, which held the top spot on the TOP500 list from June 2022 onward, and have also led the Green500 power-efficiency rankings. The product line is characterized by high memory bandwidth, support for mixed-precision arithmetic (FP64, FP32, FP16, BF16, INT8, INT4), and progressively smaller manufacturing nodes (14 nm through 3 nm).

## Key Claims

- AMD Instinct is a dedicated data center GPU brand, launched on June 20, 2017, with initial models MI6, MI8, and MI25.
- The MI6 (Polaris 10) delivers 5.7 TFLOPS FP32 and 358 GFLOPS FP64, targeting inference workloads with a TDP under 150 W.
- The MI25 (Vega 10) reaches 12.3 TFLOPS FP32 and 768 GFLOPS FP64, with 24.6 TFLOPS FP16 performance, at <300 W TDP.
- The MI100 series (CDNA 1) removed all graphics rendering hardware and added matrix processing units, achieving 11.5 TFLOPS FP64 and 184.6 TFLOPS FP16.
- The MI300X (CDNA 3) uses a chiplet design with 304 compute units, 192 GB HBM3 memory, and delivers 1307.4 TFLOPS FP16 (2614.9 with sparsity).
- The MI300A integrates 24 Zen 4 CPU cores with CDNA 3 GPU cores into a single APU, supporting 61.3 TFLOPS FP64 and 980.6 TFLOPS FP16.
- AMD Instinct GPUs use Infinity Fabric for chiplet interconnect and support PCIe 4.0/5.0 interfaces.
- Frontier supercomputer, powered by AMD Epyc CPUs and Instinct GPUs, was the world's fastest supercomputer as of 2023.

## Relationships

- AMD Instinct products from the MI100 series onward use the [[amd_cdna]] architecture (CDNA 1, 2, and 3). The MI300X and MI300A specifically implement the CDNA 3 architecture, while earlier models (MI6, MI8, MI25) relied on GCN-based architectures. Instinct accelerators share the CDNA microarchitecture's compute-focused design, matrix math units, and support for BF16/INT8/INT4 datatypes.

## Sources

- [AMD Instinct - Wikipedia](raw/cache/d24e455c1cd7f5a3.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_rocm.md
target_page: amd_rocm.md
canonical_name: AMD ROCm
colliding_name: ROCm
source: https://www.amd.com/en/products/software/rocm.html
status: pending_review
<!-- merge_draft_body
# ROCm

ROCm (Radeon Open Compute) is an open-source software stack developed by AMD that includes drivers, development tools, APIs, and runtime libraries for GPU programming on AMD hardware. It is designed to support AI and high‑performance computing (HPC) workloads, with optimizations for generative AI applications and large‑scale model training and inference. ROCm is compatible with the full AMD Instinct accelerator lineup, including the MI350 series, select AMD Radeon graphics cards, and the AMD Ryzen AI platform. It integrates with popular deep learning frameworks such as PyTorch and TensorFlow, and provides portability tools like HIP for converting CUDA code. The stack has evolved through multiple major versions (ROCm 1.0 through 7.0), adding support for Infinity Fabric interconnect, MIOpen deep learning libraries, RCCL communication libraries, new data types (FP6 and FP4 in ROCm 7.0), and orchestration for cluster‑scale deployments. ROCm also underpins the Oak Ridge National Laboratory Frontier exascale system.

## Key Claims

- ROCm is an open software stack that includes drivers, development tools, APIs, compilers, and runtime libraries for AI and HPC on AMD GPUs.
- ROCm 7 provides full support for AMD Instinct MI350 Series GPUs.
- ROCm 7 introduces support for FP6 and FP4 data types for enhanced flexibility and performance in large-scale models.
- HIP 7.0 enhances code portability between CUDA and ROCm.
- ROCm 6.0 enabled training of a 1 trillion parameter model on the Frontier system.
- ROCm supports cluster management tools including Docker, Kubernetes, and Slurm.
- ROCm maintains upstream support for PyTorch and TensorFlow.

## Relationships

- [[amd_matrix_cores]] are programmed via HIP, which is part of the ROCm software stack, and ROCm provides the runtime and libraries (e.g., MIOpen) that leverage Matrix Cores on CDNA architectures.

## Sources

- [AMD ROCm™ software empowers developers to optimize AI and HPC...](raw/cache/ecb24386768e9cbe.md)
merge_draft_body -->

## [2026-07-17] merge_pending | rdna_3.md
target_page: rdna_3.md
canonical_name: RDNA 3
colliding_name: AMD Radeon RX 9000 Series
source: https://www.amd.com/en/products/graphics/radeon-ai.html
status: pending_review
<!-- merge_draft_body
# AMD Radeon RX 9000 Series

The AMD Radeon RX 9000 Series is a family of consumer graphics cards built on the RDNA 4 architecture, designed for AI acceleration alongside traditional gaming and rendering workloads. Each compute unit integrates 2 dedicated AI accelerators that support sparsity and new data types, enabling up to 1557 TOPS of peak AI performance. The series includes models such as the Radeon RX 9070 with 16GB of GDDR6 memory and the professional-grade Radeon AI PRO R9700 with 32GB, targeting on-device AI inference, generative AI, content creation, and local machine learning development. The RX 9000 Series is compatible with major ML frameworks including Microsoft DirectML and, on select models, the AMD ROCm open software platform, allowing developers to run PyTorch-based models and deploy applications like Stable Diffusion via DirectML-optimized implementations.

## Key Claims

- RDNA 4 architecture delivers over 4× more AI compute than the previous-generation RDNA 3 architecture.
- Each compute unit features 2 AI accelerators with support for sparsity and new data types.
- Radeon 9000 Series graphics cards deliver up to 1557 TOPS of AI performance.
- Radeon RX 9070 includes 16GB GDDR6 video memory; Radeon AI PRO R9700 includes 32GB.
- Compatible with Microsoft DirectML and AMD ROCm software stacks.
- Supports popular generative AI applications: Stable Diffusion (via Automatic1111, DirectML WebUI), LM Studio, OLLAMA, and Adobe Creative Cloud AI features.
- Designed for both AI inference and training of advanced ML models on local, private hardware.

## Relationships

- AMD Radeon RX 9000 Series uses the RDNA 4 architecture, which is a separate design lineage from the CDNA architecture used in AMD Instinct accelerators. The ROCm software ecosystem, also used by [[amd_matrix_cores]] in the CDNA line, provides compatibility for RDNA-based GPUs on select models.

## Sources

- [AI Acceleration with AMD Radeon™ Graphics Cards](raw/cache/8502646ec6473c2f.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_instinct_mi325x.md
target_page: amd_instinct_mi325x.md
canonical_name: AMD Instinct MI325X
colliding_name: AMD Instinct MI325X
source: https://it-online.co.za/2024/10/16/amd-looking-to-power-the-next-generation-of-genai/
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI325X

The AMD Instinct MI325X is an AI accelerator built on the AMD CDNA 3 architecture, announced in October 2024 for powering large-scale generative AI infrastructure. It is designed for foundation model training, fine-tuning, and inference, and is positioned as a competitor to the NVIDIA H200. The MI325X features 256 GB of HBM3E memory with 6.0 TB/s bandwidth, offering 1.8× more memory capacity and 1.3× more bandwidth than the H200. It also provides 1.3× greater peak theoretical FP16 and FP8 compute performance compared to the H200. According to AMD, the MI325X delivers up to 1.3× inference performance on Mistral 7B at FP16, 1.2× on Llama 3.1 70B at FP8, and 1.4× on Mixtral 8×7B at FP16 relative to the H200. Production shipments began in Q1 2025, with system availability from OEMs such as Dell, HPE, Lenovo, and Supermicro. The MI325X is supported by the ROCm software stack, version 6.2, which introduced FP8 datatype support, Flash Attention 3, and kernel fusion. Compared to ROCm 6.0, ROCm 6.2 offers up to 2.4× inference performance improvement and 1.8× training improvement on various LLMs. AMD also leverages its Pensando Salina DPU and Pollara 400 NIC for AI networking, though these are separate products.

## Key Claims

- 256 GB HBM3E memory with 6.0 TB/s bandwidth, 1.8× capacity and 1.3× bandwidth vs. H200.
- 1.3× peak theoretical FP16 and FP8 compute vs. H200.
- Up to 1.3× inference performance on Mistral 7B (FP16), 1.2× on Llama 3.1 70B (FP8), and 1.4× on Mixtral 8×7B (FP16) vs. H200.
- Production shipments Q1 2025; system availability from Dell, Hewlett Packard Enterprise, Lenovo, Supermicro, and others.
- Supported by ROCm 6.2, which provides up to 2.4× inference and 1.8× training improvement over ROCm 6.0.
- Built on CDNA 3 architecture with Matrix Core units for mixed-precision computation.
- Ecosystem support for PyTorch, Triton, Hugging Face, and over one million models.

## Relationships

- The AMD Instinct MI325X uses the [[amd_matrix_cores]] hardware units within the CDNA 3 architecture to deliver its FP16 and FP8 matrix-accelerated performance. The MI325X is the concrete implementation of the CDNA3 Matrix Core capabilities described on that page, achieving up to 1307.4 TFLOPS (FP16) and 2614.9 TFLOPS (FP8) as documented by AMD.

## Sources

- [AMD looking to power the next generation of GenAI - IT-Online](raw/cache/26717dec5caff47d.md)
merge_draft_body -->

## [2026-07-17] pending | amd_gpu_architecture.md
target_page: amd_gpu_architecture.md
target_section: key claims
source: https://github.com/nod-ai/amd-shark-ai/blob/main/docs/amdgpu_kernel_optimization_guide.md
status: pending_review
proposed_update: Add specific compute topology and cache hierarchy details for MI300X (CDNA3) and MI355X (CDNA4) from the AMDGPU Kernel Optimization Guide: 304 CUs (MI300X), 256 CUs (MI355X), HBM3 5.2 TB/s peak bandwidth, HBM3E 8 TB/s, L1D 32KB, L2 4MB, LLC 256MB. The guide cites official AMD CDNA3/CDNA4 whitepapers.

## [2026-07-17] merge_pending | amd_pollara_400.md
target_page: amd_pollara_400.md
canonical_name: AMD Pollara 400
colliding_name: AMD Pensando Pollara 400
source: https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/
status: pending_review
<!-- merge_draft_body
# AMD Pensando Pollara 400

The AMD Pensando Pollara 400 is a 400GbE AI network interface card (NIC) designed for AI scale-out networks, announced by AMD at Hot Chips 2025. It is part of the Ultra Ethernet Consortium (UEC) ecosystem and leverages a P4 programmable packet pipeline for flexibility. The architecture includes a Table Engine for generating table keys and memory reads, a Match Processing Unit (MPU) for traffic flow classification, virtual address to physical address translation, atomic memory operations, and pipeline cache coherency. The NIC supports UEC features such as multipathing for packet spraying and reordering, congestion control mechanisms, and selective acknowledgement (SACK) for retransmission. AMD targets a 1:1 topology where each Pollara 400 is paired with one AMD Instinct GPU in systems supporting PCIe switches.

## Key Claims

- The Pollara 400 is a 400GbE AI NIC based on the P4 programmable dataplane.
- It includes a Table Engine (TE) for key generation and memory reads, a Match Processing Unit (MPU) for pattern matching in packet flows.
- It provides hardware support for virtual address to physical address translation, atomic memory operations, and pipeline cache coherency.
- It is designed to work in a 1:1 ratio with AMD Instinct GPUs in AI scale-out networks.
- The NIC is Ultra Ethernet Consortium (UEC) ready, supporting UEC multipathing, congestion control, and selective acknowledgement (SACK).
- AMD states that RCCL (AMD's collective communications library) with UEC-ready Pollara 400 NICs can increase performance (no specific numbers provided).

## Relationships

- [[amd_cdna]]: The Pollara 400 is designed to pair 1:1 with AMD Instinct GPUs based on the CDNA microarchitecture in AI scale-out network topologies, as shown in system diagrams from Hot Chips 2025.

## Sources

- [AMD Pollara 400 Details at Hot Chips 2025 - ServeTheHome](raw/cache/38bbda5aa9eac159.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_pollara_400.md
target_page: amd_pollara_400.md
canonical_name: AMD Pollara 400
colliding_name: Pensando Pollara 400
source: https://www.storagereview.com/news/amds-pensando-pollara-400-nic-brings-programmability-and-performance-to-ai-networking
status: pending_review
<!-- merge_draft_body
# Pensando Pollara 400

The Pensando Pollara 400 is a fully programmable AI Network Interface Card (NIC) developed by AMD, designed to accelerate AI workloads by optimizing GPU-to-GPU communication in data centers. It is the industry’s first fully programmable AI NIC, compatible with the developing Ultra Ethernet Consortium (UEC) standards. The card features a maximum bandwidth of 400 Gbps, a PCIe Gen5.0 x16 host interface, and a QSFP112 Ethernet interface supporting NRZ and PAM4 SerDes. It supports multiple port configurations including 1x400G, 2x200G, 4x100G, 4x50G, and 4x25G. Powered by AMD's P4 architecture, the Pollara 400 offers a fully programmable hardware pipeline, enabling support for RoCEv2, UEC RDMA, and custom transport protocols. Key capabilities include intelligent packet spraying, out-of-order packet handling, selective retransmission, and path-aware congestion control to maximize GPU utilization and minimize latency during AI training and inference. The half-height half-length (HHHL) form factor allows deployment in standard server chassis. The Pollara 400 has been validated in large-scale data centers and adopted by cloud service providers (CSPs) for its unique combination of programmability, high bandwidth, low latency, and extensibility within an open ecosystem.

## Key Claims

- **Bandwidth**: 400 Gbps maximum, with support for multiple port configurations (1x400G, 2x200G, 4x100G, 4x50G, 4x25G).
- **Host Interface**: PCIe Gen5.0 x16.
- **Form Factor**: Half-height, half-length (HHHL).
- **Ethernet Interface**: QSFP112, supporting NRZ and PAM4 SerDes, with speeds 25/50/100/200/400 Gbps.
- **Programmability**: Fully programmable hardware pipeline based on AMD's P4 architecture, allowing adaptation to emerging standards (e.g., UEC) and custom transport protocols without hardware replacement.
- **Protocol Support**: RoCEv2, UEC RDMA, and other Ethernet protocols.
- **Advanced Networking Features**: Intelligent packet spraying, out-of-order packet handling, selective retransmission, path-aware congestion control, and rapid fault detection to minimize GPU idle time.
- **Deployment**: Validated in large scale-out data centers and chosen by cloud service providers (CSPs).

## Relationships

- Designed to accelerate GPU-to-GPU communication for AI workloads, the Pensando Pollara 400 is commonly deployed in clusters containing [[amd_gpu_architecture]] to reduce network bottlenecks and improve GPU utilization.

## Sources

- [AMD’s Pensando Pollara 400 NIC Brings... - StorageReview.com](raw/cache/79ab67274d6a82e7.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_pollara_400.md
target_page: amd_pollara_400.md
canonical_name: AMD Pollara 400
colliding_name: AMD Pensando Pollara 400
source: https://www.tweaktown.com/news/101087/amd-reveals-worlds-first-ultra-ethernet-400-gbps-network-card/index.html
status: pending_review
<!-- merge_draft_body
# AMD Pensando Pollara 400

The AMD Pensando Pollara 400 is a fully programmable Ethernet network interface card (NIC) capable of 400 Gbps, designed specifically for AI cluster networking such as large-scale large language model (LLM) training. Unveiled by AMD in 2024, it targets GPU-to-GPU communication within AI networks and promises up to a sixfold performance improvement for AI workloads. The NIC enables users to customize, program, and optimize network processes, and AMD has stated it will become commercially available in the first half of 2025.

## Key Claims

- The AMD Pensando Pollara 400 is a fully programmable Ethernet NIC supporting 400 Gbps.
- It is designed for AI cluster networking, specifically GPU-to-GPU communication and large-scale LLM training.
- AMD claims up to a sixfold performance improvement for AI workloads.
- The NIC supports customization, programming, and optimization of network processes.
- Commercial availability targeted for the first half of 2025.

## Relationships

- The Pensando Pollara 400 is designed for GPU-to-GPU communication in AI clusters, complementing AMD GPU architectures such as those described in [[amd_gpu_architecture]] by providing high-bandwidth, low-latency networking tailored for distributed AI training.

## Sources

- [AMD reveals world's first Ultra Ethernet 400 Gbps network card](raw/cache/608e554c10f29d3a.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_cdna.md
target_page: amd_cdna.md
canonical_name: AMD CDNA
colliding_name: AMD CDNA
source: https://en.wikipedia.org/wiki/CDNA_(microarchitecture)
status: pending_review
<!-- merge_draft_body
# AMD CDNA

CDNA (Compute DNA) is a compute-centered GPU microarchitecture designed by AMD primarily for datacenter and high-performance computing (HPC) workloads. As the successor to the Graphics Core Next (GCN) architecture, CDNA removes graphics-specific hardware such as render output units (ROPs), tessellation units, and display engines, dedicating silicon area to compute resources and matrix acceleration. The first generation, CDNA 1, introduced in 2020 with the AMD Instinct MI100, uses a monolithic die named Arcturus manufactured on TSMC N7, featuring 120 compute units (CUs), 4 MB of L2 cache, a 4096-bit memory bus connected to four HBM2 stacks delivering 32 GB of memory and over 1200 GB/s of bandwidth. CDNA 2 shifted to a multi-chip module (MCM) design using an elevated fanout bridge (EFB) to connect dies, debuting in the Instinct MI250X and MI250. CDNA 3 adopts a chiplet-based approach with 15 unique dies on multiple nodes and advanced 3D packaging for the MI300A and MI300X. Across all generations, each compute unit contains four SIMD16 units executing 64-thread wavefronts (Wave64) and, starting with CDNA 1, dedicated matrix units for mixed-precision compute. The architecture supports datatypes including FP32, FP16, BF16, INT8, and INT4, and retains the VCN media engine for video decode (HEVC, H.264, VP9). The CDNA microarchitecture is the foundation of the AMD Instinct product line, aimed at competing with NVIDIA's data center GPU architectures.

## Key Claims

- CDNA is a compute-focused GPU microarchitecture for datacenters, succeeding GCN and removing graphics-specific hardware (ROPs, tessellation, display engine) while retaining the VCN media engine.
- CDNA 1 (Arcturus) is a monolithic die on TSMC N7 FinFET with 25.6 billion transistors on 750 mm², 120 CUs, 4 MB L2 cache, 4096-bit HBM2 memory bus, 32 GB memory, and over 1200 GB/s bandwidth.
- CDNA 2 uses a multi-chip module (MCM) approach with an elevated fanout bridge (EFB) to connect dies, featured in MI250X and MI250; the MI210 is a later monolithic addition.
- CDNA 3 uses 15 unique chiplets on multiple nodes with advanced 3D packaging for MI300X and MI300A.
- Each CU contains four SIMD16 units that execute Wave64 (64 threads) over four cycles.
- Matrix units are added per CU, supporting FP32, FP16, BF16, INT8, INT4 operations.
- Memory system includes per-CU L1 cache, 64 KB LDS, 4 KB GDS, and a shared 4 MB L2 cache with 2 KB/clock bandwidth to CUs.
- Samsung demonstrated a PIM (Processing-In-Memory) variant of the MI100 in December 2022, reporting significant throughput increases and power reduction.

## Relationships

- The AMD CDNA architecture is the compute-focused microarchitecture described as a hardware target in [[amd_gpu_architecture]], which details the hierarchical organization of AMD GPUs including shader engines, workgroup managers, and the role of compute units. CDNA uses 64-thread warps and contains asynchronous compute engines (ACEs) that break kernels into workgroups.
- AMD CDNA compute units integrate dedicated Matrix Cores ([[amd_matrix_cores]]) for mixed-precision matrix multiplication (MFMA). Matrix cores are programmed via HIP intrinsics and are a key differentiator from the consumer RDNA architecture, providing the acceleration for AI and HPC workloads on Instinct accelerators.

## Sources

- [CDNA (microarchitecture) - Wikipedia](raw/cache/9125f5a6c386787e.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_cdna_4.md
target_page: amd_cdna_4.md
canonical_name: AMD CDNA 4
colliding_name: AMD MI350 (CDNA 4)
source: https://gangliao.me/blog/2026/amd-gpu-architecture-deep-dive/
status: pending_review
<!-- merge_draft_body
# AMD MI350 (CDNA 4)

The AMD MI350 series is a family of datacenter GPU accelerators built on the CDNA 4 architecture, fabricated on TSMC N3 process, and designed for HPC and AI/ML workloads. It consists of two variants: MI350X with 256 Compute Units and 288 GB HBM3E memory at 8 TB/s bandwidth, and MI355X with 304 Compute Units. CDNA 4 introduces native support for FP6 and FP4 precision formats along with enhanced Matrix Cores, achieving up to 9.2 PFLOPS in FP4 dense compute on the MI355X. The architecture uses a multi-die chiplet design with Accelerator Complex Dies (XCDs) connected via Infinity Fabric, and it is programmed through the open-source ROCm stack including HIP.

## Key Claims

- MI350X: 256 CUs, 288 GB HBM3E, 8 TB/s bandwidth, 2.39 PFLOPS FP32, 4.61 PFLOPS FP32 w/ sparsity, 1000W TDP.
- MI355X: 304 CUs, 288 GB HBM3E, 8 TB/s bandwidth, 2.52 PFLOPS FP32, 5.03 PFLOPS FP32 w/ sparsity, 9.2 PFLOPS FP4, 1400W TDP.
- CDNA 4 is fabricated on TSMC N3 (3nm) process, a shrink from the 5nm/6nm used for CDNA 3.
- Native FP4 and FP6 compute is introduced for the first time in the AMD GPU architecture with CDNA 4.
- Matrix Cores are enhanced with wider matrix units and support for FP6 and FP4 formats, doubling FP16/BF16 throughput over CDNA 3.
- The chiplet architecture consists of XCDs (compute units, shared L2 cache, ACEs) and I/O dies connected via Infinity Fabric.
- Infinity Fabric provides low-latency coherent interconnect for multi-GPU scale-out with unified memory addressing.
- ROCm software stack includes HIP, MIOpen, rocBLAS, RCCL, rocFFT, rocRAND, hipSOLVER; all MIT-licensed except firmware.
- MI355X claims up to 35x inference performance over MI300X (which lacked FP4 support).
- Memory capacity increased 50% and bandwidth 51% compared to MI300X.

## Relationships

- The AMD MI350 series implements the hierarchical GPU compute model described in [[amd_gpu_architecture]], including shader engines, compute units, ACEs, and the CDNA-specific Wave64 wavefront organization.
- The CDNA 4 Matrix Cores in MI350 extend the [[amd_matrix_cores]] design with native FP6 and FP4 support, doubling FP16 throughput and achieving up to ~10 PFLOPS on FP4, as detailed in the AMD Matrix Cores page.

## Sources

- [Gang Liao | AMD MI350 GPU Architecture Deep Dive](raw/cache/0f34b7355979e93b.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_instinct_mi200.md
target_page: amd_instinct_mi200.md
canonical_name: AMD Instinct MI200
colliding_name: AMD Instinct MI200
source: https://wccftech.com/amd-provides-first-look-at-aldebaran-cdna-2-instinct-mi200-series-mcm-gpu-block-diagram/
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI200

The AMD Instinct MI200 series, codenamed Aldebaran, is a family of server GPUs based on the CDNA 2 architecture, announced at Hot Chips 34 as the industry's first multi-chip module (MCM) GPU design for HPC workloads. It is fabricated on TSMC's 6nm process and packages two GPU chiplets (GCDs) using 2.5D Elevated Fanout Bridge (EFB) technology, delivering a total of 58 billion transistors. Each chiplet contains 8 shader engines for a combined 16 shader engines, 224 compute units, and 14,336 stream processors. The design is optimized for FP64 matrix operations with second-generation Matrix Cores and features eight HBM2e memory stacks totaling 128 GB of capacity with an aggregate bandwidth of 3.2 TB/s. The MI200 series powers the Frontier supercomputer, the world's first exascale system, and includes multiple model variants such as the MI250X, MI250, and MI210.

## Key Claims

- The AMD Instinct MI200 series is the first HPC GPU to use an MCM design, packaging two dies (GCDs) with 2.5D Elevated Fanout Bridge (EFB) technology, offering 1.8x more cores and 2.7x higher memory bandwidth vs AMD previous-gen GPUs.
- Each GCD contains 112 compute units (7,168 stream processors), for a total of 224 CUs and 14,336 stream processors across the two dies.
- The GPU is fabricated on TSMC's 6nm process with 58 billion transistors.
- Each GCD has 8 MB of L2 cache partitioned into 32 slices (256 B/slice), with enhanced atomic operations.
- Per-GCD memory: 64 GB HBM2e (128 GB total), 32 channels, 1.6 TB/s bandwidth per GCD, aggregate 3.2 TB/s at 3.2 Gbps memory clock.
- Infinity Fabric: up to 8 links, with coherent CPU-GPU transfer at 144 GB/s and external GPU scaling up to 500 GB/s for four MI200 GPUs.
- Supports 2nd Gen Matrix Cores for FP64, FP32, FP16, BF16 matrix operations, delivering up to 4x peak theoretical FP64 performance vs previous-gen.
- Performance: up to 3x improvement over NVIDIA A100 in AMG HPC workloads (advertised).
- The MI200 series powers the Frontier supercomputer, achieving 1.1 ExaFLOPs of compute.

## Relationships

- The AMD Instinct MI200 implements the CDNA 2 architecture, which extends the general [[amd_gpu_architecture]] hierarchical design with an MCM layout and second-generation Matrix Cores. The Matrix Core block is further detailed in [[amd_matrix_cores]], though that page focuses on later CDNA3 and CDNA4 implementations.

## Sources

- [AMD Provides First Look At Aldebaran "CDNA 2" Instinct MI200 Series...](raw/cache/71ec38cf8e1f8c44.md)
merge_draft_body -->

## [2026-07-17] merge_pending | amd_instinct_mi100.md
target_page: amd_instinct_mi100.md
canonical_name: AMD Instinct MI100
colliding_name: AMD Instinct MI100
source: https://www.tweaktown.com/news/76275/amd-instinct-mi100-announced-fastest-hpc-gpu-in-the-world/index.html
status: pending_review
<!-- merge_draft_body
# AMD Instinct MI100

The AMD Instinct MI100 is a high-performance computing (HPC) GPU accelerator based on the AMD CDNA architecture, announced in November 2020. Fabricated on a 7nm process, it contains 120 Compute Units (7680 stream processors) clocked at approximately 1500 MHz, delivering 11.5 TFLOPS of FP64, 23.1 TFLOPS of FP32, and 185 TFLOPS of FP16 performance. The accelerator features 32 GB of HBM2 memory with 1.23 TB/s bandwidth, and uses second-generation Infinity Fabric links for peer-to-peer connectivity at up to 340 GB/s aggregate bandwidth per card. It supports PCIe Gen 4.0 and includes Matrix Core Technology for mixed-precision matrix operations (FP32, FP16, bfloat16, Int8, Int4), targeting convergence of HPC and AI workloads.

## Key Claims

- Fabricated on a 7nm process using the AMD CDNA architecture.
- Contains 120 Compute Units, equivalent to 7680 stream processors.
- Clock speed of approximately 1500 MHz.
- Peak performance: 11.5 TFLOPS FP64, 23.1 TFLOPS FP32, 185 TFLOPS FP16.
- Equipped with 32 GB of HBM2 memory providing 1.23 TB/s of memory bandwidth.
- Supports second-generation Infinity Fabric X16 interconnect with 276 GB/s peer-to-peer bandwidth (340 GB/s aggregate per card with three links).
- Includes Matrix Core Technology for FP32, FP16, bfloat16, Int8, and Int4 matrix operations.
- PCIe Gen 4.0 support with up to 64 GB/s transport bandwidth from CPU to GPU.
- Available in systems from Dell, GIGABYTE, HPE, and Lenovo by end of 2020.

## Relationships

- Implements the CDNA microarchitecture detailed in [[amd_gpu_architecture]], deploying 120 Compute Units and Matrix Core Technology for HPC and AI workloads.

## Sources

- [AMD Instinct MI100 announced: fastest HPC GPU in the world](raw/cache/f7472333b4a951ee.md)
merge_draft_body -->

## [2026-07-17] merge_pending | nvidia_blackwell_platform.md
target_page: nvidia_blackwell_platform.md
canonical_name: NVIDIA Blackwell Platform
colliding_name: NVIDIA Blackwell
source: https://glownet.io/nvidia-blackwell-capabilities/
status: pending_review
<!-- merge_draft_body
# NVIDIA Blackwell

NVIDIA Blackwell is a GPU architecture developed by NVIDIA for data center-scale generative AI and high-performance computing workloads. Introduced as the successor to the Hopper architecture, Blackwell focuses on delivering massive performance improvements for inference and training of large-scale neural network models, particularly those with trillions of parameters. Key architectural innovations include native support for FP4 precision, a new Transformer Engine optimized for transformer-based models, the NVLink 5.0 interconnect with high-bandwidth low-latency links, and a dual-die NV-HBI (High-Bandwidth Interconnect) bridge that enables two dies to be connected in a single package. This design allows scaling across multiple GPUs for distributed reasoning, effectively handling models that exceed single-GPU memory capacity.

## Key Claims

- Blackwell introduces FP4 (4-bit floating-point) precision, enabling higher throughput and memory efficiency for inference workloads compared to FP8 or FP16.
- The architecture incorporates a new generation of Transformer Engine specifically tuned for transformer model operations.
- NVLink 5.0 provides significantly increased bandwidth and reduced latency for GPU-to-GPU communication, supporting large-scale distributed inference.
- A dual-die NV-HBI bridge connects two GPU dies into a single cohesive package, doubling the effective die area and memory bandwidth.
- The architecture is designed to support trillion-parameter models by combining high memory capacity, fast interconnects, and efficient low-precision compute.
- Blackwell targets data center deployments for inference, scaling, and distributed reasoning tasks.

## Relationships

- [[amd_cdna]] shares the target domain of high-performance GPU computing for AI workloads, but uses a competitive chiplet-based packaging approach (AMD's CDNA 3 with 3D chiplets) compared to Blackwell's dual-die NV-HBI bridge. Blackwell's NVLink 5.0 provides a direct interconnect pathway, whereas CDNA relies on Infinity Fabric for multi-die communication.

## Sources

- [NVIDIA Blackwell GPU Technical Whitepaper Brief | Glownet](raw/cache/3b0fa3d8db31f41d.md)
merge_draft_body -->
