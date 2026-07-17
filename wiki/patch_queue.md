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

## [2026-07-17] merge_pending | google_ironwood_tpu.md
target_page: google_ironwood_tpu.md
canonical_name: Google Ironwood TPU
colliding_name: Google Ironwood TPU
source: https://techcrunch.com/2025/04/09/google-unveils-ironwood-a-new-ai-accelerator-chip/
status: pending_review
<!-- merge_draft_body
# Google Ironwood TPU

Google Ironwood is a seventh-generation Tensor Processing Unit (TPU) developed by Google, announced at the Cloud Next conference in April 2025. It is the first TPU generation optimized specifically for inference workloads, designed to run AI models at scale. Ironwood delivers 4,614 TFLOPs of peak computing power per chip, each with 192GB of dedicated RAM and memory bandwidth approaching 7.4 Tbps. The chip features an enhanced SparseCore for processing the types of data common in advanced ranking and recommendation workloads, such as algorithms that suggest products or content. Ironwood is scheduled to launch for Google Cloud customers in late 2025, available in two cluster configurations: a 256-chip cluster and a 9,216-chip cluster, and it will be integrated into Google's AI Hypercomputer platform for modular computing clusters.

## Key Claims

- Seventh-generation TPU and the first from Google optimized for inference workloads.
- Peak performance of 4,614 TFLOPs per chip.
- 192GB of dedicated RAM with memory bandwidth up to 7.4 Tbps.
- Enhanced SparseCore for ranking and recommendation workloads.
- Designed for energy efficiency through minimized data movement and reduced latency on-chip.
- Available in two cluster sizes: 256-chip and 9,216-chip configurations.
- Scheduled for launch in 2025 for Google Cloud customers.
- Part of the Google AI Hypercomputer integration for scalable deployment.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Ironwood is Google's newest AI accelerator chip | TechCrunch](raw/cache/f7f559569bd5b8bf.md)
merge_draft_body -->

## [2026-07-17] merge_pending | google_ironwood_tpu.md
target_page: google_ironwood_tpu.md
canonical_name: Google Ironwood TPU
colliding_name: TPU7x (Ironwood)
source: https://docs.cloud.google.com/tpu/docs/tpu7x
status: pending_review
<!-- merge_draft_body
# TPU7x (Ironwood)

TPU7x (Ironwood) is the seventh-generation Tensor Processing Unit (TPU) from Google Cloud, designed for large-scale AI training and inference workloads. It is the first release in the Ironwood family and offers a 9,216-chip footprint per Pod, sharing architectural similarities with the TPU v5p generation. Each TPU7x chip integrates two TensorCores and four SparseCores, and is composed of two distinct chiplets—each featuring one TensorCore, two SparseCores, and 96 GB of HBM—connected by a die-to-die interface six times faster than a 1D ICI link. The chip delivers up to 2307 TFLOPS of BF16 peak compute per chip and 4614 TFLOPS of FP8 peak compute, with 192 GB of HBM per chip providing 7.38 TB/s of memory bandwidth. The system architecture employs a 3D torus interconnect topology and supports slice shapes scaling from small single-host configurations up to 9216-chip pods. The memory hierarchy includes high-bandwidth memory (HBM), on-chip vector memory (VMEM) with ultra-high bandwidth to the Matrix Multiply Unit (MXU), and host memory accessible via PCIe for offloading activations or optimizer states. The dual-chiplet architecture is exposed to frameworks such as JAX as two separate devices per chip, enabling reuse of existing software models with minimal changes.

## Key Claims

- TPU7x is the first Ironwood-family TPU, with a 9,216-chip Pod footprint; it shares design similarities with TPU v5p.
- Each chip contains two TensorCores and four SparseCores, formed from two chiplets each with one TensorCore, two SparseCores, and 96 GB of HBM.
- Peak compute per chip: 2307 TFLOPS (BF16) and 4614 TFLOPS (FP8).
- HBM capacity per chip: 192 GiB; HBM bandwidth per chip: 7380 GBps.
- Inter-chip interconnect (ICI) bandwidth per chip: 200 GBps per axis (bidirectional); data center network (DCN) bandwidth per chip: 100 Gbps.
- The memory hierarchy comprises HBM, vector memory (VMEM) on-chip SRAM, and host memory via PCIe; VMEM provides higher bandwidth to the MXU than HBM and is a tunable parameter for custom Pallas kernels.
- The dual-chiplet architecture uses a die-to-die (D2D) interface and exposes each chip as two devices in JAX, requiring a fourth dimension in topology specifications.
- Supported slice topologies range from 2x2x1 (1/16th chip) to 8x16x16 (2048 chips); larger slices are composed of 4x4x4 cubes.
- The 3D torus interconnect topology allows scaling to 9216 chips with bidirectional bandwidth of 200 GBps per axis.
- Each TPU7x VM contains 4 chips with 224 vCPUs and 960 GB of RAM.
- Frameworks: JAX exposes two devices per chip; compute can be specified per chiplet. GKE is a supported orchestration platform.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [TPU7x (Ironwood) | Google Cloud Documentation](raw/cache/c5d9854149044f40.md)
merge_draft_body -->

## [2026-07-17] merge_pending | google_ironwood_tpu.md
target_page: google_ironwood_tpu.md
canonical_name: Google Ironwood TPU
colliding_name: TPU7x (Ironwood)
source: https://docs.cloud.google.com/tpu/docs/ironwood-performance
status: pending_review
<!-- merge_draft_body
# TPU7x (Ironwood)

TPU7x (Ironwood) is a tensor processing unit developed by Google for accelerating artificial intelligence and machine learning workloads. Part of the Google Cloud TPU ecosystem, Ironwood features a multi-tiered memory hierarchy including 192 GB of high-bandwidth memory (HBM) per chip, and supports hardware-accelerated FP8 (8-bit floating point) data types capable of delivering up to 4614 TFLOPS peak theoretical performance per chip. It is designed for both training and inference of large-scale neural networks, leveraging techniques such as low-precision training, sharding, communication optimization, activation rematerialization, and custom accelerator kernels. The architecture is optimized for efficient data movement across its memory tiers and interconnect topology, and its performance tuning framework emphasizes arithmetic intensity analysis to determine whether a workload is compute-bound, memory-bound, or interconnect-bound.

## Key Claims

- TPU7x (Ironwood) provides built-in hardware acceleration for FP8 data types, achieving a peak theoretical performance of 4614 TFLOPS per chip.
- FP8 training yields a performance improvement of approximately 1.3x over standard BF16 training while halving memory footprint for weights and activations.
- Each TPU7x chip includes 192 GB of HBM, enabling larger models to fit without offloading to host memory.
- FP8 reduces HBM pressure, increases effective batch size, and lowers memory bandwidth requirements.
- Recommended FP8 quantization practices: start with per-tensor scaling, default to dynamic scaling, mix E4M3 (forward pass) and E5M2 (backward pass) formats, and use round-to-nearest-even (RNE) rounding.
- MaxText supports FP8 training through the QWIX quantization library via the `use_qwix_quantization=true` flag.
- Performance tuning should begin with an arithmetic intensity analysis to classify workloads as compute-bound, memory-bound, or interconnect-bound.
- Sharding strategy should prioritize the simplest approach that meets memory constraints to minimize communication overhead.

## Relationships

- Shares the use of FP8 (8-bit floating point) datatypes for accelerating computation with [[amd_matrix_cores]], though TPU7x implements FP8 as a general-purpose data format for training and inference, while AMD Matrix Cores use FP8 specifically within matrix-core fused-multiply-add operations for non-TPU architectures.

## Sources

- [TPU7x (Ironwood) performance optimizations | Google Cloud ...](raw/cache/e2f0a899af98f5bc.md)
merge_draft_body -->

## [2026-07-17] merge_pending | google_ironwood_tpu.md
target_page: google_ironwood_tpu.md
canonical_name: Google Ironwood TPU
colliding_name: Google TPU Ironwood
source: https://www.nevsemi.com/blog/google-tpu-chip-ironwood-technology-explained
status: pending_review
<!-- merge_draft_body
# Google TPU Ironwood

The Google TPU Ironwood is Google's seventh-generation Tensor Processing Unit, a custom-designed ASIC for accelerating machine learning workloads. Announced in November 2025, Ironwood is the successor to the sixth-generation TPU Trillium and offers a fourfold improvement in both model training performance and inference throughput. Each chip features 192 GB of HBM3e memory with 7.4 TB/s bandwidth and achieves a peak computational performance of 4,614 TFLOPs in FP8 precision. A single Ironwood Superpod integrates 9,216 such chips, creating a large-scale AI supercomputer. Google's TPUs have evolved since the first generation in 2015, with each generation adding capabilities such as distributed training (v2), liquid cooling (v3), 3D torus interconnect (v4), and MLP core for Transformers (v6). Ironwood targets large-scale generative AI and enterprise AI deployments, addressing high cost and energy footprint of trillion-parameter models.

## Key Claims

- Ironwood is the seventh-generation Google TPU, commercialized in November 2025.
- Compared with the sixth-generation TPU Trillium, Ironwood delivers a fourfold improvement in both model training performance and inference throughput.
- Each Ironwood chip includes 192 GB of HBM3e memory with 7.4 TB/s bandwidth.
- Peak computational performance of 4,614 TFLOPs in FP8 precision.
- A single Ironwood Superpod integrates 9,216 TPU chips, collectively forming a high-capability AI supercomputer.
- AI developer Anthropic is reportedly preparing to deploy one million TPUs (presumably Ironwood) to support its Claude model family.
- Ironwood targets large-scale generative AI and enterprise-level AI deployments, aiming to reduce the high cost and energy footprint of operating trillion-parameter models.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Google TPU Chip Ironwood Technology Explained - Nevsemi ...](raw/cache/86810d726576fc07.md)
merge_draft_body -->

## [2026-07-17] merge_pending | intel_clearwater_forest.md
target_page: intel_clearwater_forest.md
canonical_name: Intel Clearwater Forest
colliding_name: Intel Clearwater Forest
source: https://www.servethehome.com/intel-clearwater-forest-is-set-to-be-a-tech-breakthrough-server-chip/
status: pending_review
<!-- merge_draft_body
# Intel Clearwater Forest

Intel Clearwater Forest is an upcoming server processor architecture from Intel, positioned as the successor to the Sierra Forest all-E-core Xeon line. It is planned to be manufactured on Intel's 18A process node, incorporating RibbonFET gate-all-around transistors and PowerVia backside power delivery, which Intel estimates will yield approximately 6% efficiency improvement. Clearwater Forest will utilize advanced packaging technologies including Foveros Direct 3D with direct copper bonding between compute tiles and base dies, and EMIB 3.5D combining chip-to-chip bridges with 3D stacking. The architecture is expected to deliver high core counts by stacking compute dies atop SRAM and fabric base dies, with I/O and memory controllers fabricated on separate, more mature process nodes. While specific performance figures and core counts have not been disclosed, Intel has indicated that Clearwater Forest will significantly increase core density and power efficiency compared to current Xeon offerings.

## Key Claims

- Clearwater Forest will be Intel's first server processor on the 18A process node.
- It uses RibbonFET (gate-all-around) transistors, replacing FinFET technology.
- It uses PowerVia backside power delivery, with Intel estimating a ~6% improvement in efficiency.
- The architecture uses Foveros Direct 3D packaging with direct copper bonding between compute tiles and base dies.
- It incorporates EMIB 3.5D packaging, combining EMIB (chip-to-chip bridges) and Foveros Direct 3D.
- Compute dies are placed on top of SRAM and fabric base dies to enable high core counts.
- I/O and SRAM are manufactured on separate, more mature process nodes (not 18A) to improve yield and reduce cost.
- Clearwater Forest is designed for high-density cloud-native server workloads.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Intel Clearwater Forest is Set to be a Tech Breakthrough Server Chip](raw/cache/c1eec18a570c53bb.md)
merge_draft_body -->

## [2026-07-17] merge_pending | granite_rapids.md
target_page: granite_rapids.md
canonical_name: Granite Rapids
colliding_name: Intel Xeon 6+ Clearwater Forest
source: https://www.servethehome.com/intel-xeon-6-clearwater-forest-is-out/
status: pending_review
<!-- merge_draft_body
# Intel Xeon 6+ Clearwater Forest

Intel Xeon 6+ Clearwater Forest is a processor architecture from Intel, announced in July 2026. It features up to 288 E-cores built on the Intel 18A process node, utilizing PowerVia and RibbonFET technologies. The chip supports DDR5-8000 memory and includes up to 576 MB of last-level cache. Clearwater Forest targets cloud-native and telco workloads, succeeding the Sierra Forest Xeon 6700E and 6900E lines. It is part of the Xeon 6900 series AP platform and aims to compete with Arm-based cores in cloud environments. Intel claims significant performance and efficiency improvements over both Sierra Forest and the older Cascade Lake, including 30% higher performance per thread and up to 9:1 consolidation ratio versus Cascade Lake. The architecture uses a tiled design with 12 compute tiles, three active base tiles, two I/O tiles, and EMIB and Foveros Direct 3D packaging, reflecting Intel's ongoing move toward disaggregated processors.

## Key Claims

- Up to 288 E-cores per socket, built on Intel 18A process with PowerVia and RibbonFET.
- DDR5-8000 memory support, up to 576 MB last-level cache.
- 30% higher performance at same core count compared to Sierra Forest.
- 60% better performance per watt compared to Sierra Forest.
- 38% reduction in rack power consumption compared to Sierra Forest.
- 30% greater average performance per thread compared to Cascade Lake.
- 55% greater average performance per watt compared to Cascade Lake.
- Up to 9:1 consolidation ratio versus Cascade Lake.
- Tiled architecture: 12 compute tiles, 3 active base tiles, 2 I/O tiles, 12 EMIB tiles.
- Supports Intel SGX and TDX for confidential computing.
- Intel Application Energy Telemetry (AET) for per-application core energy reporting.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Intel Xeon 6+ Clearwater Forest is Out - ServeTheHome](raw/cache/5d835c813913d071.md)
merge_draft_body -->

## [2026-07-17] merge_pending | nvidia_blackwell_platform.md
target_page: nvidia_blackwell_platform.md
canonical_name: NVIDIA Blackwell Platform
colliding_name: Blackwell
source: https://resources.nvidia.com/en-us-blackwell-architecture/blackwell-architecture-technical-brief
status: pending_review
<!-- merge_draft_body
# Blackwell

The NVIDIA Blackwell architecture is a graphics processing unit (GPU) microarchitecture developed by Nvidia as the successor to the Hopper and Ada Lovelace microarchitectures. Named after statistician and mathematician David Blackwell, the architecture was officially announced on March 18, 2024. Blackwell GPUs are built on the TSMC 4NP process and incorporate 208 billion transistors across two chiplet dies connected by a 10 TB/s NVLink interface. The architecture serves as the foundation for the Grace Blackwell GB200 superchip and the GB200 NVL72 rack-scale system, delivering up to 30 times more performance and 25 times greater energy efficiency for AI workloads compared to the prior generation.

## Key Claims

- Blackwell is the successor to the Hopper and Ada Lovelace GPU microarchitectures.
- Named after mathematician David Blackwell (Rao-Blackwell theorem).
- Comprises 208 billion transistors across two chiplet dies.
- Built on TSMC 4NP process node.
- Chiplet dies are connected via a 10 TB/s NVLink interface.
- The architecture powers the Grace Blackwell GB200 superchip and GB200 NVL72 system.
- Claims 30X performance improvement and 25X energy efficiency improvement over the preceding architecture (Hopper).
- B200 data center GPU listed at $30,000–40,000 per module as of July 2025.

## Relationships

No specific relationship to visible context pages.

## Sources

- [NVIDIA Blackwell Architecture Technical Overview](raw/cache/8a8198e5532f8680.md)
merge_draft_body -->

## [2026-07-17] merge_pending | nvidia_nvlink_nvswitch.md
target_page: nvidia_nvlink_nvswitch.md
canonical_name: Nvidia NVLink and NVSwitch
colliding_name: NVLink
source: https://intuitionlabs.ai/articles/nvidia-nvlink-gpu-interconnect
status: pending_review
<!-- merge_draft_body
# NVLink

NVIDIA NVLink is a high-speed GPU interconnect architecture that provides significantly higher bandwidth than PCIe, enabling efficient multi-GPU communication and unified memory. Introduced in 2016 with the Pascal P100 GPU, NVLink delivers up to 5× the bandwidth of PCIe 3.0 x16 per link. It supports cache coherence and unified virtual addressing, allowing GPUs and CPUs to share memory as peers. The architecture scales from point-to-point links to large fabrics using NVSwitch, achieving hundreds of GB/s to TB/s of GPU-to-GPU bandwidth. NVLink has been used in supercomputers such as Summit and Sierra, and in large-scale AI clusters such as Microsoft's 4,608-GPU Azure deployment.

## Key Claims

- NVLink was introduced in 2016 with the NVIDIA Pascal P100 GPU.
- NVLink provides up to 5× the bandwidth of PCIe 3.0 x16 per link.
- An NVIDIA Tesla P100 achieves 160 GB/s bidirectional bandwidth over NVLink, compared to ~32 GB/s over PCIe Gen3 x16.
- NVLink 1.0 (Pascal P100): 4 links per GPU, total bidirectional bandwidth 160 GB/s.
- NVLink 2.0 (Volta V100): 6 links per GPU, total bidirectional bandwidth 300 GB/s; added cache coherence and unified virtual addressing.
- NVLink 3.0 (Ampere A100): 6 links per GPU, total bidirectional bandwidth 600 GB/s.
- NVLink 4.0 (Hopper H100): 12 links per GPU, total bidirectional bandwidth 900 GB/s; per-link speed 100 GB/s in each direction.
- NVLink enables coherent shared memory across processors, deployed in Oak Ridge's Summit and Sierra supercomputers.
- Microsoft deployed a 4,608-GPU NVLink-connected cluster in 2025 using NVLink 5, achieving 92.1 exaFLOPS of FP4 inference.
- NVLink works with NVSwitch for intra-node all-to-all connectivity and can be extended for inter-node links.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [NVIDIA NVLink Explained: A Guide to the GPU Interconnect](raw/cache/1bb25d6ea84c0446.md)
merge_draft_body -->

## [2026-07-17] merge_pending | nvidia_blackwell_platform.md
target_page: nvidia_blackwell_platform.md
canonical_name: NVIDIA Blackwell Platform
colliding_name: NVIDIA Blackwell GPU Architecture
source: https://www.emergentmind.com/topics/nvidia-blackwell-gpus
status: pending_review
<!-- merge_draft_body
# NVIDIA Blackwell GPU Architecture

The NVIDIA Blackwell GPU Architecture is a modern GPU microarchitecture designed for scientific, engineering, and artificial intelligence inference and HPC workloads. It succeeds the Hopper architecture and introduces several key innovations including unified INT32/FP32 execution units that replace the prior separated integer and floating-point pipelines, fifth-generation tensor cores supporting ultra-low precision formats FP4, FP6, and FP8, and a refined memory hierarchy with a reduced L1/shared memory per streaming multiprocessor (128 KB vs. 256 KB on Hopper) and a monolithic 65 MB L2 cache. Blackwell is implemented in both consumer GPUs such as the RTX 5080 and in large datacenter variants like Blackwell Ultra. The architecture requires updated compiler heuristics and kernel tuning to fully exploit its new capabilities and mitigate tradeoffs such as reduced shared memory and unified L2 cache contention under heavy warp concurrency.

## Key Claims

- Unified INT32/FP32 execution units replace previously separated integer and floating-point pipelines; each unit can perform either operation per cycle but not both simultaneously.
- Each streaming multiprocessor (SM) is divided into four sub-core units: integer, FP32, FP64, and tensor (matrix multiply-accumulate).
- L1/shared memory per SM is reduced to 128 KB, compared to 256 KB on Hopper.
- L2 cache is a monolithic 65 MB, whereas Hopper uses two partitions totaling 50 MB.
- Fifth-generation tensor cores support FP4, FP6, and FP8 arithmetic via new PTX/SASS instructions (tcgen05, QMMA, OMMA).
- True latency for INT32/FP32 instructions is approximately 4 cycles on both Blackwell and Hopper.
- In dense GEMM benchmarks, Blackwell (RTX 5080) shows up to 4x lower sustained throughput than Hopper, likely due to compiler maturity and scheduling policies.
- FP4 tensor core operation draws as little as 16.75 W, while peak power in GEMM tests can exceed 110 W.
- Transformer inference workloads see power usage drop from ~58.8 W to 45 W when using FP8 kernels on Blackwell.
- Compiler optimizations are necessary to handle the unified execution units and to generate correct code for new tensor core instructions.

## Relationships

- [[nvidia_hopper_architecture]]: Blackwell is the direct successor to the Hopper architecture; it modifies the SM design (unified execution units), reduces L1 per SM, increases L2 cache size, and adds FP4/FP6 tensor core support, while inheriting the CUDA programming model and basic warp execution model.
- [[nvidia_blackwell_ultra]]: The Blackwell Ultra is a dual-reticle datacenter variant built on the same base Blackwell architecture as the consumer RTX 5080 covered here; while Blackwell Ultra targets large-scale AI training with 208B transistors and 15 PetaFLOPS NVFP4, the base Blackwell design (e.g., RTX 5080) uses a single die with lower memory capacity and different performance characteristics.

## Sources

- [NVIDIA Blackwell GPU Architecture - emergentmind.com](raw/cache/909eee89a00ce5f2.md)
merge_draft_body -->

## [2026-07-17] merge_pending | granite_rapids.md
target_page: granite_rapids.md
canonical_name: Granite Rapids
colliding_name: Intel Xeon Next-Generation Platform
source: https://newsroom.intel.com/artificial-intelligence/intel-unveils-future-generation-xeon
status: pending_review
<!-- merge_draft_body
# Intel Xeon Next-Generation Platform

Intel's next-generation Xeon platform, unveiled at Hot Chips 2023, introduces a dual-architecture strategy with two distinct processor families: Sierra Forest, featuring Efficient-cores (E-cores) for density-optimized cloud compute, and Granite Rapids, featuring Performance-cores (P-cores) for high-performance AI and general-purpose workloads. This platform marks a significant evolution in Intel's data center roadmap, leveraging a modular system-on-chip design, shared software stack, and advanced memory technologies including CXL 2.0 support and new multiplexed combined rank (MCR) DIMMs to address the growing demands of AI, cloud, and enterprise deployments.

## Key Claims

- Intel's next-generation Xeon platform introduces two distinct processor families for 2024: Sierra Forest (E-core) and Granite Rapids (P-core).
- The platform uses a modular system-on-chip design for scalability across AI, cloud, and enterprise workloads.
- Sierra Forest targets density-optimized compute with up to 144 cores per CPU and TDP as low as 200W.
- Sierra Forest claims 2.5x better rack density and 2.4x higher performance per watt compared to 4th Gen Intel Xeon processors (architectural projections as of August 21, 2023).
- Granite Rapids targets high-performance compute with enhanced AI capabilities, claiming 2-3x better performance for mixed AI workloads compared to 4th Gen Xeon (projected).
- Granite Rapids features enhanced Intel AMX with support for new FP16 instructions.
- The platform supports CXL 2.0 with backward compatibility to CXL 1.1 and up to 136 lanes of PCIe 5.0/CXL 2.0.
- The new platform includes Intel Flat Memory for hardware-managed data movement between DDR5 and CXL memory.
- Fastest DDR and new high-bandwidth multiplexed combined rank (MCR) DIMMs are supported.
- Socket scalability ranges from 1-socket to 8-socket configurations.
- 5th Gen Intel Xeon (Emerald Rapids) is on track for Q4 2023; Sierra Forest for H1 2024; Granite Rapids follows shortly after.

## Relationships

No specific relationship to visible context pages.

## Sources

- [Intel Unveils Future-Generation Xeon with Robust Performance and ...](raw/cache/06daa5137dc47860.md)
merge_draft_body -->

## [2026-07-17] merge_pending | oryon.md
target_page: oryon.md
canonical_name: Oryon
colliding_name: Qualcomm Oryon Core
source: https://chipsandcheese.com/p/hot-chips-2024-qualcomms-oryon-core
status: pending_review
<!-- merge_draft_body
# Qualcomm Oryon Core

The Qualcomm Oryon Core is a high-performance ARMv8-A CPU core designed by Qualcomm for use in the Snapdragon X Elite platform targeting laptops and edge devices. Presented at Hot Chips 2024, the Oryon core features an 8-wide decode pipeline fed by a TAGE (Tagged Geometric Length) branch predictor with an 80 KB conditional predictor storage budget, enabling high instruction throughput. The core implements a distributed scheduling model with large 64-entry reservation stations in the load/store unit, allowing for 64 outstanding loads before dispatch stalls. It includes a 96 KB multi-ported L1 data cache built from standard foundry bitcells, chosen to balance latency and clock speed. The memory subsystem employs unusually large TLBs, including a 224-entry DTLB and a very large L2 TLB that can handle up to 32768 4K page entries (or equivalent coverage via page fusion), with up to 20 concurrent page walks to minimize address translation latency. Both the scalar and vector execution engines have four data feeds from the load/store unit, enabling four loads per cycle. The core's 13-cycle branch misprediction penalty is not industry-leading but is balanced for the microarchitecture, and the wide fetch stage helps fill the pipeline quickly after mispredictions.

## Key Claims

- The branch predictor uses TAGE (Tagged Geometric Length) prediction with an 80 KB storage budget for the conditional predictor.
- The core implements an 8-wide decode pipeline with 64 bytes per cycle instruction fetch.
- The 13-cycle branch mispredict penalty is balanced for the microarchitecture; Zen 4's mispredict penalty ranges from 11 to 18 cycles.
- A distributed scheduling model is used, with the load/store unit having 64-entry reservation stations (schedulers).
- Microbenchmarks show 62 outstanding loads before dispatch stall at rename, indicating 64 total scheduler entries available to loads.
- The L1 data cache is 96 KB, multi-ported, and made from standard foundry bitcells.
- The DTLB has 224 entries, unusually large, designed to reduce address translation latency.
- The L2 TLB is very large; testing shows an inflection point at 128 MB, corresponding to 32768 4K pages, either from many entries or page fusion.
- The core can have 10 to 20 pending page walks concurrently, compared to 6 for Zen 4.
- Both vector and scalar execution engines can handle four loads per cycle from the load/store unit.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Hot Chips 2024: Qualcomm’s Oryon Core - by Chester Lam](raw/cache/b750a8e8016e8d62.md)
merge_draft_body -->

## [2026-07-17] merge_pending | oryon.md
target_page: oryon.md
canonical_name: Oryon
colliding_name: Qualcomm Oryon
source: https://www.servethehome.com/snapdragon-x-elite-qualcomm-oryon-cpu-design-and-architecture-hot-chips-2024-arm/
status: pending_review
<!-- merge_draft_body
# Qualcomm Oryon

The Qualcomm Oryon is a custom Arm architecture CPU core developed by Qualcomm from the Nuvia acquisition, first deployed in the Snapdragon X Elite SoC for Windows-on-Arm laptops. The core features a deep out-of-order pipeline with a 13-cycle branch mispredict latency, a 600+ entry reorder buffer, and a 6-wide integer, 4-wide vector (128-bit per pipe), and 4-wide load-store execution design. The memory subsystem includes a 12MB L2 cache per cluster operating at near-core frequency with 15-20 clock average latency, a 6MB system-level cache shared across SoC engines, and LPDDR5x memory with 135GB/s platform bandwidth. The Oryon core targets general-purpose computing with strong per-core performance, as demonstrated on Geekbench 6 and SPEC CPU2017 benchmarks.

## Key Claims

- Branch mispredict latency is 13 cycles, described as "balanced" by Qualcomm.
- Decode pipeline can handle every instruction class in the Arm architecture.
- Rename/dispatch: integer 6-wide, vector 4-wide (128-bit pipes), load-store 4-wide; supports almost every data type.
- Physical register files contain approximately 400 entries.
- Up to 200 in-flight load-store operations; mix of proprietary and industry prefetchers.
- L2 cache capacity is 12MB; average latency 15-20 clocks at near-core frequency.
- System-level cache is 6MB, shared by all SoC engines.
- Memory bandwidth: single core can utilize ~100GB/s out of 135GB/s platform LPDDR5x bandwidth.
- Per-core performance is notably better than that of Arm Neoverse N series or AmpereOne cores.
- Security features are designed for notebook use (theft/loss scenarios).

## Relationships

No specific relationship to visible context pages.

## Sources

- [Snapdragon X Elite Qualcomm Oryon CPU Design and Architecture Hot Chips 2024](raw/cache/3e337307a4c4f507.md)
merge_draft_body -->

## [2026-07-17] merge_pending | snapdragon_x_elite.md
target_page: snapdragon_x_elite.md
canonical_name: Snapdragon X Elite
colliding_name: Qualcomm Snapdragon X Elite
source: https://cputronic.com/cpu/qualcomm-snapdragon-x-elite
status: pending_review
<!-- merge_draft_body
# Qualcomm Snapdragon X Elite

The Qualcomm Snapdragon X Elite (codename Oryon) is a 12-core ARM-based processor designed for laptop computers, manufactured on TSMC's 4nm process. It features a unified performance-core design with 12 Oryon P-cores all supporting multithreading, a base frequency of 3.8 GHz and turbo up to 4.2 GHz, a 42 MB L3 cache, and an integrated Adreno GPU. The processor supports TDP configurations from 23 W to 65 W, making it suitable for ultrabooks and workstations. It achieved Geekbench 6 scores of 2694 single-core and 13969 multi-core, placing it competitively against top x86 processors from Intel and AMD. The chip includes integrated 5G and Wi-Fi 7 support and offers battery life up to 20 hours for video playback.

## Key Claims

- Built on TSMC 4nm process with 12 Oryon performance cores, each supporting two threads.
- Base clock 3.8 GHz, turbo up to 4.2 GHz.
- 42 MB L3 cache.
- TDP ranges from 23 W (ultrabook config) to 65 W (workstation config).
- Geekbench 6 single-core score 2694, multi-core 13969.
- Integrated Adreno GPU capable of 4K video and light gaming, not meant for AAA titles.
- Battery life up to 20 hours for 1080p video playback, 12–14 hours office work.
- 30–40% lower power consumption than comparable x86 chips.
- Supports 5G and Wi-Fi 7 out of the box.
- Compared to Apple M3 Max, offers higher multi-core Geekbench score (13969 vs 12800).
- Compared to AMD Ryzen 9 7940HS, similar performance with lower TDP range.
- Compared to Intel Core i9-13900H, longer battery life but lower single-thread performance.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Qualcomm Snapdragon X Elite: Detailed Specifications... - CpuTronic](raw/cache/7115879833a0822b.md)
merge_draft_body -->

## [2026-07-17] merge_pending | nvidia_hopper_architecture.md
target_page: nvidia_hopper_architecture.md
canonical_name: NVIDIA Hopper Architecture
colliding_name: NVIDIA Hopper GPU
source: https://arxiv.org/abs/2501.12084
status: pending_review
<!-- merge_draft_body
# NVIDIA Hopper GPU

The NVIDIA Hopper GPU architecture is a high-performance graphics processing unit architecture designed for accelerating AI training, inference, and scientific computing workloads. Introduced in 2022, Hopper introduces several novel hardware features including fourth-generation Tensor Cores with FP8 support, a Tensor Memory Accelerator (TMA) for asynchronous data movement, Distributed Shared Memory (DSM) for inter-SM communication, and DPX instructions for dynamic programming. Hopper's memory subsystem features an L2 partitioned cache with improved global memory access compared to its predecessors Ampere and Ada Lovelace. The architecture is manufactured on a TSMC 4N process and serves as the foundation for NVIDIA's H100 and H200 data center GPUs. This page summarizes the microbenchmarking analysis performed by Luo et al. (2025) that dissects Hopper's performance characteristics across memory, tensor core, and instruction-level dimensions.

## Key Claims

- The asynchronous programming model supported by the Tensor Memory Accelerator (TMA) achieves a 1.5x speedup in matrix multiplication compared to traditional approaches.
- FP8 precision delivers nearly double the performance of FP16 on Hopper's fourth-generation tensor cores for matrix operations.
- DPX instructions accelerate a computational biology algorithm (Smith-Waterman) by at least 4.75x compared to scalar implementations.
- The L2 partitioned cache and global memory subsystem show measurable latency and throughput improvements over Ampere and Ada Lovelace.
- Distributed Shared Memory (DSM) enables inter-SM communication with specific latency and throughput characteristics.
- The tensor cores support asynchronous wgmma (warp group matrix multiply-accumulate) instructions for efficient matrix operations.
- The architecture includes fourth-generation tensor cores that benefit from FP8 precision and asynchronous instructions.

## Relationships

- [[nvidia_blackwell_ultra]]: The NVIDIA Hopper GPU is the direct predecessor of the Blackwell Ultra GPU. Blackwell Ultra builds upon Hopper's tensor core and memory subsystem advancements, increasing transistor count from approximately 80 billion to 208 billion and introducing the NVFP4 data format, while Hopper introduced FP8 and asynchronous TMA.

## Sources

- [[2501.12084] Dissecting the NVIDIA Hopper Architecture ...](raw/cache/04d6b461ade29969.md)
merge_draft_body -->

## [2026-07-17] merge_pending | nvidia_hopper_architecture.md
target_page: nvidia_hopper_architecture.md
canonical_name: NVIDIA Hopper Architecture
colliding_name: Nvidia Hopper GPU
source: https://arxiv.org/abs/2402.13499
status: pending_review
<!-- merge_draft_body
# Nvidia Hopper GPU

The Nvidia Hopper GPU is a graphics processing unit architecture introduced by Nvidia as the successor to the Ampere architecture. It introduces several novel features including tensor cores with FP8 support for AI workloads, a DPX instruction set optimized for dynamic programming, and distributed shared memory capabilities. A comprehensive benchmarking study by Luo et al. (2024) from the Hong Kong University of Science and Technology examines the microarchitectural characteristics of the Hopper GPU through latency and throughput comparisons across the Hopper, Ada, and Ampere architectures. This study is the first to demystify the tensor core performance and programming instruction sets unique to Hopper GPUs, offering insights into the novel GPU AI function units and programming features.

## Key Claims

- The Hopper GPU introduces tensor cores with FP8 support, a DPX instruction set for dynamic programming, and distributed shared memory.
- A benchmarking study (Luo et al., 2024) conducts conventional latency and throughput benchmarks comparing Hopper, Ada, and Ampere architectures.
- The same study discusses and benchmarks Hopper-specific features including DPX instructions, distributed shared memory, and FP8 tensor cores.
- The microbenchmarking results provide a deeper understanding of the novel GPU AI function units and programming features unique to Hopper.
- This work is the first to demystify the tensor core performance and programming instruction sets specific to the Hopper architecture.

## Relationships

- [[nvidia_blackwell_ultra]]: The Nvidia Hopper GPU is the direct predecessor to the Blackwell Ultra architecture, sharing the use of tensor cores, the CUDA toolchain, and targeting similar AI training and inference workloads.

## Sources

- [[2402.13499] Benchmarking and Dissecting the Nvidia Hopper ...](raw/cache/a1f77160184ba76d.md)
merge_draft_body -->

## [2026-07-17] pending | nvidia_hopper_architecture.md
target_page: nvidia_hopper_architecture.md
target_section: Key Claims
source: https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
status: pending_review
proposed_update: Add the following Key Claims based on the NVIDIA Hopper Architecture In-Depth blog post: - Fourth-generation Tensor Cores provide up to 6x speedup chip-to-chip over A100, with per-SM 2x MMA rate on equivalent data types and 4x rate on FP8 compared to 16-bit. - New DPX Instructions accelerate dynamic programming algorithms (Smith-Waterman, Floyd-Warshall) by up to 7x over A100. - New thread block cluster feature extends CUDA programming hierarchy to enable synchronization across multiple SMs. - Transformer Engine delivers up to 9x faster AI training and up to 30x faster AI inference on large language models. - NVLink Switch System connects up to 256 GPUs with 57.6 TB/s all-to-all bandwidth. - The Grace Hopper Superchip pairs H100 with Grace CPU via 900 GB/s chip-to-chip interconnect, providing 10x higher performance for large-model AI/HPC and up to 30x higher aggregate bandwidth versus today's fastest servers.

## [2026-07-17] merge_pending | granite_rapids.md
target_page: granite_rapids.md
canonical_name: Granite Rapids
colliding_name: Intel Granite Rapids
source: https://wccftech.com/intel-next-gen-xeon-cpus-2024-granite-rapids-redwood-cove-p-cores-sierra-forest-sierra-glen-e-cores/
status: pending_review
<!-- merge_draft_body
# Intel Granite Rapids

Intel Granite Rapids is a family of server processors from Intel, designed as the P-core (performance-core) offering within the company's next-generation Xeon lineup for 2024. Optimized for compute-intensive and AI workloads, Granite Rapids utilizes the Intel 3 process node and features a modular architecture with separate compute and IO chiplets interconnected via the EmiB fabric. It supports up to eight-socket configurations, up to 12-channel DDR/MCR memory, 136 PCIe Gen 5 lanes, and CXL 2.0 with six UPI links. The compute die incorporates Redwood Cove cores, shared last-level cache, and a modular mesh fabric that enables low-latency chiplets access. Granite Rapids is positioned against AMD's Zen 4 cores and builds on Intel's commitment to offering both P-core and E-core Xeon families sharing a common platform and software stack.

## Key Claims

- Granite Rapids uses the Intel 3 process node and is optimized for compute-intensive and AI workloads.
- It features modular compute and IO chiplets interconnected via the EmiB fabric.
- Supports 1S to 8S socket scalability.
- Supports up to 12-channel DDR/MCR memory (1-2DPC), up to 136 PCIe Gen 5 lanes, 6 UPI links, and CXL 2.0.
- The compute die contains Redwood Cove cores with L2 cache, LLC+SF+CHA slice, and mesh fabric interface.
- The modular mesh fabric enables logically monolithic mesh with direct access between agents, shared LLC partitioned into per-die sub-numa clusters, and EmiB technology for high-speed die-to-die fabric.
- Aims for 2-3x better performance for mixed AI workloads, with enhanced Intel AMX and FP16 instructions.

## Relationships

- [[intel_sierra_forest]]: Both are families of next-gen Intel Xeon CPUs for 2024, sharing a common platform foundation and software stack. Granite Rapids targets P-core compute-intensive and AI workloads, while Sierra Forest targets E-core density-optimized and scale-out workloads.

## Sources

- [Intel Details Next-Gen Xeon CPUs For 2024: Granite Rapids With...](raw/cache/9adf13f4e7d491af.md)
merge_draft_body -->

## [2026-07-17] merge_pending | sierra_forest.md
target_page: sierra_forest.md
canonical_name: Sierra Forest
colliding_name: Intel Sierra Forest
source: https://wccftech.com/intel-next-gen-xeon-cpus-2024-granite-rapids-redwood-cove-p-cores-sierra-forest-sierra-glen-e-cores/
status: pending_review
<!-- merge_draft_body
# Intel Sierra Forest

Intel Sierra Forest is a family of server processors from Intel, representing the E-core (efficiency-core) offering in the company's next-generation Xeon lineup for 2024. Optimized for density-optimized computing and high efficiency in scale-out workloads, Sierra Forest utilizes the Intel 3 process node and features core tiles with 2-4 cores per module, each core single-threaded, reaching up to 144 cores per CPU. It supports 1S and 2S server configurations with TDP as low as 200W. The processor delivers 2.5x better rack density and 2.4x higher performance per watt compared to previous generations. Sierra Forest includes modern instruction set support with AVX and AI extensions, robust security and virtualization features, and foundational memory RAS. It shares a common platform and software stack with the P-core Granite Rapids family.

## Key Claims

- Sierra Forest uses the Intel 3 process node and is optimized for density-optimized, power-efficient scale-out workloads.
- Core tile consists of 2-4 cores per module, each single-threaded, with shared L2 cache and shared frequency/voltage domain.
- Top SKU offers up to 144 cores (36 core tiles × 4 cores) and 144 threads, with up to 144 MB L2 and 108 MB LLC.
- Supports 1S and 2S server configurations, with TDP as low as 200W.
- Claims 2.5x better rack density and 2.4x higher performance per watt.
- Supports modern instruction set with robust security, virtualization, and AVX with AI extensions.
- Includes foundational memory RAS features such as machine check and data cache ECC.
- Shares a common platform and software stack with Granite Rapids (P-core Xeon family).

## Relationships

- [[intel_granite_rapids]]: Both are families of next-gen Intel Xeon CPUs for 2024, sharing a common platform foundation and software stack. Sierra Forest targets E-core density-optimized and scale-out workloads, while Granite Rapids targets P-core compute-intensive and AI workloads.

## Sources

- [Intel Details Next-Gen Xeon CPUs For 2024: Granite Rapids With...](raw/cache/9adf13f4e7d491af.md)
merge_draft_body -->

## [2026-07-17] merge_pending | granite_rapids.md
target_page: granite_rapids.md
canonical_name: Granite Rapids
colliding_name: Granite Rapids
source: https://www.techbloat.com/hot-chips-2023-intel-granite-rapids-and-sierra-forest-xeons.html
status: pending_review
<!-- merge_draft_body
# Granite Rapids

Granite Rapids is a family of Intel Xeon server processors announced at Hot Chips 2023, built using P-core architecture with Redwood Cove cores for maximum per-core performance. It is positioned alongside Sierra Forest as part of Intel's split Xeon roadmap, where Granite Rapids targets workloads requiring high single-threaded performance and compute density. The platform succeeds the Sapphire Rapids and Emerald Rapids generations, leveraging enhanced performance cores and platform advancements such as high memory bandwidth and extensive I/O capabilities to cater to data center, HPC, and AI workloads.

## Key Claims

- Uses Redwood Cove P-cores for maximum per-core performance.
- Part of Intel's Xeon roadmap split, targeting workloads demanding high single-threaded performance.
- Succeeds Sapphire Rapids and Emerald Rapids generations.
- Manufactured on an advanced Intel process node (process node not specified in available sources).
- Supports high memory bandwidth and extensive I/O capabilities.

## Relationships

No specific relationship to visible context pages.

## Sources

- [Hot Chips 2023: Intel Granite Rapids and Sierra Forest Xeons](raw/cache/2d7c6f8579aeaa96.md)
merge_draft_body -->

## [2026-07-17] merge_pending | sierra_forest.md
target_page: sierra_forest.md
canonical_name: Sierra Forest
colliding_name: Sierra Forest
source: https://www.techbloat.com/hot-chips-2023-intel-granite-rapids-and-sierra-forest-xeons.html
status: pending_review
<!-- merge_draft_body
# Sierra Forest

Sierra Forest is a family of Intel Xeon server processors announced at Hot Chips 2023, representing Intel's first E-core Xeon Scalable chip designed for data center use. The architecture utilizes Sierra Glen E-cores, focusing on high core density and power efficiency. Sierra Forest is manufactured on the EUV-based Intel 3 process node, marking the first Xeon to employ this advanced fabrication technology. The processor features up to 144 cores, targeting high-density scale-out workloads and cloud-native applications. By splitting the Xeon roadmap into P-core and E-core families, Intel aims to address diverse computing needs within the data center.

## Key Claims

- First E-core Xeon Scalable chip for data center use.
- Uses Sierra Glen E-cores.
- Manufactured on the EUV-based Intel 3 process node.
- Features up to 144 cores.
- Targets high-density scale-out workloads and power-efficient cloud applications.
- Part of Intel's split Xeon roadmap alongside Granite Rapids.

## Relationships

No specific relationship to visible context pages.

## Sources

- [Hot Chips 2023: Intel Granite Rapids and Sierra Forest Xeons](raw/cache/2d7c6f8579aeaa96.md)
merge_draft_body -->

## [2026-07-17] merge_pending | sierra_forest.md
target_page: sierra_forest.md
canonical_name: Sierra Forest
colliding_name: Intel Xeon (Sierra Forest and Granite Rapids)
source: https://www.techpowerup.com/312952/intel-unveils-future-generation-xeon-with-robust-performance-and-efficiency-architectures
status: pending_review
<!-- merge_draft_body
# Intel Xeon (Sierra Forest and Granite Rapids)

At the 2023 Hot Chips conference, Intel unveiled its next-generation Xeon platform featuring two distinct processor architectures: Sierra Forest with Efficient-cores (E-cores) and Granite Rapids with Performance-cores (P-cores). The platform is built on a modular system-on-chip design that provides socket compatibility between the two variants, allowing customers to choose between density-optimized power-efficient compute (Sierra Forest) and high-performance compute for latency-sensitive workloads (Granite Rapids). Both architectures share the same IP, firmware, and software stack, simplifying deployment across cloud, enterprise, and AI workloads. The platform supports up to 144 E-cores per CPU (Sierra Forest) with TDP as low as 200W, and offers enhanced AI acceleration through Intel AMX with new FP16 instructions on Granite Rapids, along with significant memory bandwidth improvements via the inclusion of MCR DIMMs and Intel Flat Memory architecture for CXL memory tiering.

## Key Claims

- The Intel Xeon platform introduces two socket-compatible processor architectures: Sierra Forest (E-core) and Granite Rapids (P-core), sharing a common software stack.
- Sierra Forest provides up to 144 E-cores per processor for high-density compute with TDP as low as 200 W.
- Sierra Forest claims 2.5x better rack density and 2.4x higher performance per watt compared to previous generation.
- Granite Rapids integrates enhanced Intel AMX with support for FP16 instructions, targeting AI workload acceleration.
- Granite Rapids claims 2-3x better performance for mixed AI workloads over previous generations.
- The platform supports up to 136 lanes of PCIe 5.0/CXL 2.0 and up to six UPI links.
- New Intel Flat Memory enables hardware-managed data movement between DDR5 and CXL-attached memory, making total capacity visible to software.
- Support for high-bandwidth MCR DIMMs complements standard DDR5 memory.
- The platform supports socket scalability from one to eight sockets (Granite Rapids) and 1S/2S configurations for Sierra Forest.

## Relationships

- [[meta_vistara_cxl_bridge]]: Intel Xeon's support for CXL 2.0 and Flat Memory architecture enables hardware-managed memory tiering, a concept related to Meta's Vistara CXL bridge chip which attaches retired DDR4 modules as a low-cost capacity tier through the same underlying protocol, though Vistara targets specific reuse scenarios rather than general platform memory expansion.
- [[alphawave_semi_hbm_subsystem]]: Intel Xeon Granite Rapids uses DDR5 and MCR DIMMs, whereas the Alphawave Semi HBM Subsystem provides HBM3/2E/2 connectivity for 2.5D/3D packages, representing contrasting memory hierarchy choices: higher capacity and lower cost for Xeon versus extreme bandwidth at higher cost for HBM in compute-intensive applications.
- [[amd_gpu_architecture]]: Intel Xeon processors with AMX accelerators provide CPU-based AI inference, offering an alternative to GPU-accelerated AI on AMD GPU Architecture, particularly for workloads that benefit from lower latency and tighter integration with host memory.

## Sources

- [Intel Unveils Future-Generation Xeon with Robust Performance ...](raw/cache/1c0c0c2be8cd6488.md)
merge_draft_body -->

## [2026-07-17] merge_pending | sierra_forest.md
target_page: sierra_forest.md
canonical_name: Sierra Forest
colliding_name: Intel Xeon 6700E Sierra Forest
source: https://wccftech.com/intel-xeon-6700e-sierra-forest-cpus-144-e-cores-330w-tdp-more-efficient-vs-amd-epyc/
status: pending_review
<!-- merge_draft_body
# Intel Xeon 6700E (Sierra Forest)

The Intel Xeon 6700E, codenamed Sierra Forest, is a server processor family launched by Intel in June 2024 at Computex. It is part of the Xeon 6 family and utilizes only efficient (E) cores based on the Crestmont microarchitecture, fabricated on Intel's 3 process node. The Xeon 6700E series targets high-density compute and scale-out workloads such as web microservices, database analytics, cloud-native applications, networking, and edge computing. With up to 144 cores, the chips are designed to deliver improved performance per watt compared to previous Xeon generations and competing AMD EPYC Bergamo processors.

## Key Claims

- Launched at Computex 2024 with up to 144 cores (Xeon 6780E) and up to 330W TDP.
- Based on Crestmont E-core architecture, single-threaded, 4 MB L2 per 4-core cluster, 6-wide decode/allocate, 8-wide retire.
- Supports enhanced AVX2 (2x128), VNNI Int8, BF16/FP16, AES-256-bit encryption.
- Memory support: up to 8-channel DDR5-6400 (1DPC) or DDR5-5600, up to 88 PCIe Gen5/CXL 2.0 lanes.
- Platform: LGA 4710 socket, 1S and 2S configurations, built-in accelerators: 2 DSA, 2 IAA, 4 QAT, 4 DLB.
- Performance claims: up to 4.2x faster than 2nd Gen Xeon, 2.6x perf/watt improvement, 34% more efficient versus AMD EPYC Bergamo.
- SKU range: Xeon 6780E (144 cores, 330W), 6766E (144 cores, 250W), 6756E (128 cores, 225W), 6746E (112 cores, 250W), 6740E (96 cores, 250W), 6731E (96 cores, 250W), 6710E (64 cores, 205W).
- Long-life availability (7+ years) for several SKUs.

## Relationships

- [[meta_vistara_cxl_bridge]]: The Xeon 6700E platform supports CXL 2.0 interconnect, which is the protocol used by Meta's Vistara CXL bridge chip to attach DDR4 memory as a capacity tier, enabling cost-effective memory expansion in data centers using Xeon-based servers.

## Sources

- [Intel Xeon 6700E "Sierra Forest" CPUs Launched: Up To 144 E ...](raw/cache/0b439e7095159e2e.md)
merge_draft_body -->

## [2026-07-17] merge_pending | google_ironwood_tpu.md
target_page: google_ironwood_tpu.md
canonical_name: Google Ironwood TPU
colliding_name: Google TPU v7 Ironwood
source: https://www.humai.blog/apple-m5-vs-nvidia-blackwell-vs-google-tpu-the-complete-post-ces-2025-ai-chip-comparison/
status: pending_review
<!-- merge_draft_body
# Google TPU v7 Ironwood

The Google TPU v7 Ironwood is a tensor processing unit designed by Google for AI workloads, unveiled at Cloud Next in April 2025 and publicly available in late 2025. It delivers 4,614 TFLOPS of FP8 performance with 192GB of HBM3e memory offering 7.2-7.4 TB/s bandwidth, putting Google within striking distance of NVIDIA on raw specifications. Ironwood features a 9.6 Tb/s Inter-Chip Interconnect and scales to 9,216 chips per superpod, achieving 42.5 exaFLOPS theoretical compute. It is available alongside the earlier TPU v6 Trillium and is supported by JAX and TensorFlow frameworks. The chip is positioned for large-scale cloud AI training and inference, with pricing expected to offer a significant performance-per-dollar advantage over competing NVIDIA offerings.

## Key Claims

- Unveiled at Cloud Next April 2025, publicly available.
- 4,614 TFLOPS FP8 performance.
- 192GB HBM3e memory with 7.2-7.4 TB/s bandwidth.
- 9.6 Tb/s inter-chip interconnect.
- Scales to 9,216 chips per superpod (42.5 exaFLOPS).
- Supported by JAX and TensorFlow.
- Expected to deliver 4x+ performance-per-dollar compared to prior generation (implied from pricing table in source).

## Relationships

- Both the Google TPU v7 Ironwood and the [[nvidia_blackwell_b200]] use 192GB HBM3e memory, though with different bandwidth (7.2-7.4 TB/s vs 8 TB/s). This shared technology reflects their common target of high-bandwidth memory for large-scale AI workloads.

## Sources

- [Apple M5 vs NVIDIA Blackwell vs Google TPU: The Complete...](raw/cache/be48c2942b36c9b4.md)
merge_draft_body -->

## [2026-07-17] pending | alphawave_semi_hbm_subsystem.md
target_page: alphawave_semi_hbm_subsystem.md
target_section: Key Claims
source: https://awavesemi.com/press-release/alphawave-semi-spearheads-chiplet-based-custom-silicon-for-generative-ai-and-data-center-workloads-with-successful-3nm-tapeouts-of-hbm3-and-ucie-ip/
status: pending_review
proposed_update: Add claim about 3nm tapeout and updated HBM3 PHY data rate of 8.6 Gbps from Alphawave Semi's July 2023 press release. The existing page states 8.4 Gbps; this source reports 8.6 Gbps on TSMC 3nm with 16 channels and low power operation. Also note the PHY targets leading-edge high-performance memory interfaces for AI and HPC workloads.

## [2026-07-17] merge_pending | nvidia_blackwell_b200.md
target_page: nvidia_blackwell_b200.md
canonical_name: NVIDIA Blackwell B200
colliding_name: NVIDIA B200
source: https://thegioimaychu.vn/blog/ai-hpc/so-sanh-cac-gpu-tensor-core-cua-nvidia-b200-b100-h200-h100-a100-p20268/
status: pending_review
<!-- merge_draft_body
# NVIDIA B200

The NVIDIA B200 is a flagship Tensor Core GPU based on the Blackwell architecture, introduced in 2025. It delivers 40 teraFLOPS of FP64 performance, 2.2 petaFLOPS of FP32 Tensor Core throughput, 4.5 petaFLOPS in FP16/BF16 Tensor Core, and 9 petaFLOPS in INT8 and FP8 Tensor Core modes. A notable capability is FP4 precision at 18 petaFLOPS. The GPU is equipped with 192 GB of HBM3e memory offering up to 8 TB/s bandwidth and supports up to 7 Multi-Instance GPU (MIG) partitions at 23 GB each. It features 7 NVDEC and 7 JPEG decoders, and an NVLink interconnect speed of 1.8 TB/s. The B200 is sold as part of NVIDIA's AI Enterprise platform and is designed for the most demanding AI training and inference workloads.

## Key Claims

- FP64 performance: 40 teraFLOPS
- FP32 Tensor Core performance: 2.2 petaFLOPS
- FP16/BF16 Tensor Core performance: 4.5 petaFLOPS
- INT8 Tensor Core performance: 9 petaOPS
- FP8 Tensor Core performance: 9 petaFLOPS
- FP4 Tensor Core performance: 18 petaFLOPS
- Memory: 192 GB HBM3e
- Memory bandwidth: up to 8 TB/s
- MIG support: up to 7 instances at 23 GB each
- Decoders: 7 NVDEC, 7 JPEG
- NVLink speed: 1.8 TB/s
- Part of NVIDIA AI Enterprise

## Relationships

- [[nvidia_b100_tensor_core]]: Shares the Blackwell architecture with the B100, which offers slightly lower performance metrics and 141 GB HBM3e memory.
- [[nvidia_h200_tensor_core]]: The B200 is the next-generation successor to the H200 (Hopper architecture), with more than double the FP16 Tensor Core performance and increased memory bandwidth.
- [[nvidia_h100_tensor_core]]: The B200 outperforms the H100 in all Tensor Core precisions by a factor of 3–7×.
- [[nvidia_a100_tensor_core]]: The A100 (Ampere architecture) was the first Tensor Core GPU with MIG; the B200 provides 2.5× the FP32 Tensor Core performance and 4.5× the memory bandwidth.

## Sources

- [So sánh các thế hệ GPU Tensor Core đầu bảng của NVIDIA: B200...](raw/cache/0dd8e54681229db2.md)
merge_draft_body -->

## [2026-07-17] merge_pending | nvidia_hopper_architecture.md
target_page: nvidia_hopper_architecture.md
canonical_name: NVIDIA Hopper Architecture
colliding_name: NVIDIA H200
source: https://thegioimaychu.vn/blog/ai-hpc/so-sanh-cac-gpu-tensor-core-cua-nvidia-b200-b100-h200-h100-a100-p20268/
status: pending_review
<!-- merge_draft_body
# NVIDIA H200

The NVIDIA H200 is a Tensor Core GPU based on the Hopper architecture, launched in 2024 as an enhanced version of the H100 with upgraded high-bandwidth memory. It delivers 34 teraFLOPS FP64, 19.5 teraFLOPS FP64 Tensor Core, 80 teraFLOPS FP32, 989 teraFLOPS FP32 Tensor Core, and 1,979 teraFLOPS (1.98 petaFLOPS) FP16/BF16 Tensor Core. INT8 Tensor Core performance is 3,958 teraOPS and FP8 Tensor Core is 3,958 teraFLOPS. The H200 includes 141 GB of HBM3e memory (up from 80 GB HBM3 in the H100) with 4.8 TB/s bandwidth, supports up to 7 MIG partitions at 16.5 GB each, 5 NVDEC and 5 JPEG decoders, and an NVLink interconnect of 900 GB/s. The H200 is targeted at large-scale AI training and HPC workloads.

## Key Claims

- FP64 performance: 34 teraFLOPS
- FP64 Tensor Core performance: 19.5 teraFLOPS
- FP32 performance: 80 teraFLOPS
- FP32 Tensor Core performance: 989 teraFLOPS
- FP16/BF16 Tensor Core performance: 1,979 teraFLOPS
- INT8 Tensor Core performance: 3,958 teraOPS
- FP8 Tensor Core performance: 3,958 teraFLOPS
- Memory: 141 GB HBM3e
- Memory bandwidth: 4.8 TB/s
- MIG support: up to 7 instances at 16.5 GB each
- Decoders: 5 NVDEC, 5 JPEG
- NVLink speed: 900 GB/s

## Relationships

- [[nvidia_h100_tensor_core]]: The H200 is a mid-life update of the H100 with increased memory (141 GB HBM3e vs. 80 GB HBM3) and doubled memory bandwidth (4.8 vs. 2 TB/s).
- [[nvidia_b200_tensor_core]]: The B200 (Blackwell) succeeds the H200 with roughly 2× the FP16 Tensor Core performance and 1.7× the memory bandwidth.
- [[nvidia_b100_tensor_core]]: The B100 and H200 share identical memory capacity and bandwidth, but the B100 offers higher Tensor Core throughput at FP16/BF16 (3.5 vs. 1.98 petaFLOPS).

## Sources

- [So sánh các thế hệ GPU Tensor Core đầu bảng của NVIDIA: B200...](raw/cache/0dd8e54681229db2.md)
merge_draft_body -->

## [2026-07-17] merge_pending | nvidia_hopper_architecture.md
target_page: nvidia_hopper_architecture.md
canonical_name: NVIDIA Hopper Architecture
colliding_name: NVIDIA H200
source: https://convly.ai/ar/h100-vs-h200-for-ai/
status: pending_review
<!-- merge_draft_body
# NVIDIA H200

The NVIDIA H200 is a GPU accelerator introduced as an incremental update to the H100 within the Hopper architecture family, targeting generative AI and high-performance computing workloads. While retaining the identical compute core design—CUDA core count, Tensor Cores, and memory controller architecture—as the H100, the H200 replaces the HBM3 memory with the newer HBM3e, increasing total memory capacity from 80 GB to 141 GB and memory bandwidth from 3.35 TB/s to 4.8 TB/s. This memory-centric upgrade allows the H200 to load larger model parameters and larger batched datasets without modifying the compute pipeline, effectively extending the throughput of existing Hopper-based AI infrastructure. The H200 is delivered as part of the NVIDIA HGX H200 platform, which integrates multiple H200 GPUs for rack-scale deployment in data centers.

## Key Claims

- The H200 uses the same Hopper GPU compute architecture as the H100, including identical CUDA core and Tensor Core counts; only the memory subsystem differs.
- The H200 upgrades memory from HBM3 to HBM3e, increasing memory capacity from 80 GB to 141 GB and memory bandwidth from 3.35 TB/s to 4.8 TB/s.
- The increased memory capacity and bandwidth enable handling larger generative AI models (e.g., larger parameter sizes, larger batch sizes) without scaling cluster size.
- The H200 is positioned for generative AI and HPC workloads, supported by the NVIDIA HGX H200 platform.
- All other hardware specifications (compute performance per clock, interconnects, form factor) remain unchanged from the H100.

## Relationships

- [[alphawave_semi_hbm_subsystem]]: The H200's HBM3e memory is a later generation of the JEDEC High-Bandwidth Memory standard that the Alphawave Semi HBM Subsystem also supports (up to HBM3), though the H200 implements HBM3e directly on-package as part of the GPU, whereas the Alphawave subsystem is a standalone IP block for custom SoCs.

## Sources

- [NVIDIA H100 vs H200 for AI in 2026: Is the Memory... | Convly AI](raw/cache/220ce116aa2bb8a7.md)
merge_draft_body -->

## [2026-07-17] merge_pending | nvidia_blackwell_b200.md
target_page: nvidia_blackwell_b200.md
canonical_name: NVIDIA Blackwell B200
colliding_name: NVIDIA B200
source: https://www.gmicloud.ai/en/blog/nvidia-b200-inference-throughput
status: pending_review
<!-- merge_draft_body
# NVIDIA B200

The NVIDIA B200 is a Blackwell-generation data center GPU featuring 180 GB of HBM3e memory with 8.0 TB/s of memory bandwidth, representing a 1.67× increase over the H200's 4.80 TB/s. Designed for large language model inference, where throughput is often memory-bandwidth-bound, the B200 achieves a cost of two cents per thousand tokens on the independent InferenceX benchmark. Cloud pricing for the B200 SXM6 variant in June 2026 ranges from $3.70 per hour on neo-clouds to $14.24 per hour on AWS, a 3.8× price spread across providers. Memory bandwidth is the critical factor for LLM inference performance, making the B200's bandwidth advantage central to its value proposition.

## Key Claims

- The B200 is a Blackwell card with 180 GB of HBM3e and 8.0 TB/s memory bandwidth.
- Memory bandwidth is 1.67× higher than the H200 (4.80 TB/s).
- On the InferenceX benchmark, the B200 system achieves a cost of $0.02 per thousand tokens.
- On-demand cloud pricing for B200 SXM6 ranges from $3.70/hr (neo-clouds) to $14.24/hr (AWS) as of June 2026.
- Memory bandwidth is the critical factor for LLM inference on this architecture.

## Relationships

- [[meta_vistara_cxl_bridge]]: The B200 uses high-bandwidth HBM3e memory for maximum throughput, while Vistara repurposes low-cost DDR4 via CXL for capacity expansion; these are complementary memory strategies in AI server design.
- [[amd_gpu_architecture]]: Both are data center GPU architectures optimized for throughput-oriented parallel workloads, though B200 targets LLM inference with dedicated transformer engine support.

## Sources

- [NVIDIA B200 for Inference: When Throughput Justifies the Price](raw/cache/2ab98716c4d0d6e2.md)
merge_draft_body -->

## [2026-07-17] merge_pending | intel_xeon_sapphire_rapids.md
target_page: intel_xeon_sapphire_rapids.md
canonical_name: Intel Xeon Sapphire Rapids
colliding_name: Intel Sapphire Rapids-SP
source: https://www.techbyte.it/hardware/intel-sapphire-rapids-sp-3-volte-piu-potente-rispetto-a-ice-lake/
status: pending_review
<!-- merge_draft_body
# Intel Sapphire Rapids-SP

Intel Sapphire Rapids-SP is a family of Xeon-based server processors designed for high-performance computing (HPC) and artificial intelligence (AI) workloads, introduced by Intel during the ISC 2022 conference. The processors employ a chiplet architecture consisting of four XCC (Xeon Compute Core) dies, each approximately 400mm², interconnected via EMIB (Embedded Multi-die Interconnect Bridge) technology. Two variants are planned: a standard version and an HBM version that integrates 64 GB of HBM2E memory (four 16 GB stacks) directly on package. The HBM variant package measures 5700mm², 28% larger than the standard package at 4446mm². Intel claims Sapphire Rapids-SP delivers up to 3× the performance of its predecessor, Ice Lake, with EMIB providing twice the bandwidth density and four times the energy efficiency over standard interconnects.

## Key Claims

- Sapphire Rapids-SP aims to be 3× more powerful than Ice Lake for HPC and AI workloads (source: Intel at ISC 2022).
- Chiplet design: four XCC dies, each ~400mm², interconnected via EMIB.
- Standard variant uses 10 EMIB interconnects; HBM variant uses 14.
- EMIB features a pitch of 55 microns for interconnects and a core pitch of 100 microns.
- HBM variant integrates four 8-Hi HBM2E stacks for a total of 64 GB of on-package memory.
- Standard package size: 4446mm²; HBM package size: 5700mm² (28% larger).
- EMIB claimed to provide 2× bandwidth density improvement and 4× energy efficiency vs. standard interconnects.

## Relationships

- Shares the HBM2E memory standard with [[alphawave_semi_hbm_subsystem]], though Sapphire Rapids-SP integrates HBM2E directly via EMIB within a CPU package, whereas Alphawave Semi provides a standalone HBM subsystem IP for ASIC designs.

## Sources

- [Intel Sapphire Rapids-SP sarà 3 volte più potente rispetto a Ice Lake...](raw/cache/63b4ff550b0b197a.md)
merge_draft_body -->

## [2026-07-17] merge_pending | intel_xeon_sapphire_rapids.md
target_page: intel_xeon_sapphire_rapids.md
canonical_name: Intel Xeon Sapphire Rapids
colliding_name: Sapphire Rapids
source: https://en.wikipedia.org/wiki/Sapphire_Rapids
status: pending_review
<!-- merge_draft_body
# Sapphire Rapids

Sapphire Rapids is the codename for Intel's fourth-generation Xeon Scalable server and workstation processors, launched on January 10, 2023. Based on the Golden Cove microarchitecture and fabricated on the Intel 7 process, it features up to 60 Golden Cove cores per socket in a chiplet design, which is a first for Intel's server and workstation processors. The architecture supports up to octa-channel DDR5-4800 ECC memory and, in the Xeon Max variants, includes 64 GB of on-package HBM2e memory as an L4 cache. Sapphire Rapids also integrates multiple on-chip accelerators including DSA (Data Streaming Accelerator), QAT (QuickAssist Technology), DLB (Dynamic Load Balancer), and IAA (In-Memory Analytics Accelerator), targeting a range of server, workstation, and embedded applications. It is part of Intel's Eagle Stream server platform and powers the Aurora exascale supercomputer at Argonne National Laboratory.

## Key Claims

- Launched on January 10, 2023, branded as Xeon Bronze/Silver/Gold/Platinum (Sapphire Rapids-SP) and Xeon Max Series (Sapphire Rapids-HBM), plus Xeon w3/w5/w7/w9 (Sapphire Rapids-WS).
- Uses the Golden Cove microarchitecture on the Intel 7 process (formerly 10ESF).
- First Intel server/workstation processor with a chiplet design, using up to 60 cores per socket.
- Cache hierarchy: L1 80 KB per core (32 KB instruction + 48 KB data), L2 2 MB per core, L3 up to 112.5 MB (1.875 MB per core), L4 64 GB HBM2e (Xeon Max only).
- Memory: up to octa-channel DDR5-4800 with ECC support, and 64 GB HBM2e on select models.
- Integrated accelerators: Data Streaming Accelerator (DSA), QuickAssist Technology (QAT), Dynamic Load Balancer (DLB), In-Memory Analytics Accelerator (IAA).
- Supports instruction set extensions including AVX-512, AVX-VNNI, AMX, AES-NI, and others.
- Socket LGA 4677, part of the Eagle Stream platform.
- Product code name SPR, CPUID 806F6, product code 80713.

## Relationships

- [[alphawave_semi_hbm_subsystem]]: Sapphire Rapids Xeon Max variants integrate 64 GB of on-package HBM2e memory, which conforms to the JEDEC HBM2E standard supported by the Alphawave Semi HBM Subsystem's controller and PHY IP. Both address high-bandwidth memory integration, though the Sapphire Rapids implementation is a fixed on-package solution while the Alphawave subsystem is a licensable IP for custom SoC designs.

## Sources

- [Sapphire Rapids - Wikipedia](raw/cache/8cbb8896ccf30234.md)
merge_draft_body -->

## [2026-07-17] merge_pending | golden_cove.md
target_page: golden_cove.md
canonical_name: Golden Cove
colliding_name: Golden Cove
source: https://chipsandcheese.com/p/popping-the-hood-on-golden-cove
status: pending_review
<!-- merge_draft_body
# Golden Cove

Golden Cove is the high-performance P-core microarchitecture used in Intel's Alder Lake processors, introduced in late 2021. It is the direct successor to Sunny Cove and targets peak single-threaded performance through a wider and deeper pipeline. Key enhancements include a 45% larger reorder buffer, a 4K-entry micro-op cache (up from 2.25K in Sunny Cove), six instruction decoders, and a multi-level branch target buffer with reduced penalty for misses. Golden Cove also features improved branch prediction, capable of recognizing longer patterns than Skylake, though still slightly behind AMD's Zen 3 in pattern length. The architecture supports AVX-512 instructions on the silicon, but Intel disabled them on desktop Alder Lake SKUs. Its BTB can handle up to 128 branches with roughly one taken branch per cycle, and returns are handled by a return stack that shows unusual behavior beyond two nested calls. The L1 data cache can perform 2×512-bit loads per cycle when AVX-512 is enabled. These changes made Alder Lake competitive with AMD's Zen 3 for both integer and floating-point workloads after several years of Intel dominance in desktop performance.

## Key Claims

- Golden Cove's reorder buffer is 45% larger than Sunny Cove's, increasing instruction reordering capacity.
- The micro-op cache size increased from 2.25K entries (Sunny Cove) to 4K entries, matching Zen 3 in fetch bandwidth at 8 micro-ops per cycle.
- The branch target buffer (BTB) is multi-level; missing in the first level costs 1 cycle penalty, compared to AMD's 3 cycles for an L2 BTB hit.
- Branch prediction can recognize longer patterns than Skylake but shorter than Zen 3; with multiple branches, pattern length capacity is lower than both Zen 2 and Zen 3.
- Golden Cove can deliver roughly one taken branch per cycle for up to 128 branches, a regression from Sunny Cove in this specific metric.
- Return prediction lacks a clear capacity jump for up to 128 call/return pairs but is slower than Sunny Cove and Zen 2/3 when calls exceed two deep.
- The architecture includes six instruction decoders to feed the wider pipeline.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Popping the Hood on Golden Cove - Chips and Cheese](raw/cache/7fa9f612569e3589.md)
merge_draft_body -->

## [2026-07-17] merge_pending | gracemont.md
target_page: gracemont.md
canonical_name: Gracemont
colliding_name: Intel Gracemont
source: https://www.servethehome.com/intel-gracemont-architecture-day-2021/
status: pending_review
<!-- merge_draft_body
# Intel Gracemont

Intel Gracemont is a low-power x86 processor core architecture introduced by Intel as part of its Alder Lake hybrid processor lineup. Gracemont is the successor to the Tremont architecture and belongs to the Intel Atom lineage, though it delivers significantly higher performance than earlier Atom cores. Designed for efficiency rather than peak performance, Gracemont cores are optimized for low voltage and low power, making them suitable for background tasks and high-core-count configurations. Key architectural features include three-wide out-of-order decode, a 64KB L1 instruction cache, a 256-entry out-of-order window, 17 execution ports, and up to 4MB of L2 cache shared among four cores. The architecture also adds support for AVX2 and VNNI instructions, enabling basic AI inference acceleration. Intel claims that four Gracemont E-cores fit into approximately the same die area as one Skylake performance core, while delivering better performance at lower power.

## Key Claims

- Three-wide out-of-order decode with on-demand decoding capable of handling up to six uops into the queues.
- 64KB L1 instruction cache (up from 32KB in the previous generation Tremont).
- Increased branch target cache and prefetchers at all levels.
- Out-of-order window increased to 256 entries.
- 17 execution ports (up from 12 in the previous generation).
- Up to 4MB of L2 cache shared among four cores; Intel can vary cache size based on SKU needs.
- Supports AVX2 and VNNI instructions for AI inference.
- Optimized for low voltage and low power rather than maximum performance.
- Four E-cores fit into the same die area as one Skylake performance core (P-core).
- Can deliver performance at lower power than Skylake, but not necessarily at the same maximum frequency.

## Relationships

No specific relationship to visible context pages.

## Sources

- [Intel Gracemont Low Power x86 Cores - ServeTheHome](raw/cache/09b5bae249c0b0e9.md)
merge_draft_body -->

## [2026-07-17] pending | power10.md
target_page: power10.md
target_section: Key Claims
source: https://en.wikipedia.org/wiki/Power10
status: pending_review
proposed_update: Add details from Wikipedia: execution slices (eight per core, each with FPU, ALU, branch predictor, load-store unit, SIMD-engine), instruction queue sizes (512-entry shared instruction table, 128-entry load queue, 80-entry store queue), branch prediction accuracy doubled, two-hemisphere layout with 8 cores each sharing 64 MB L3 cache (total 128 MB before yield reduction), 8 crypto accelerators offloading AES and SHA-3. Also mention the IBM Power10 Enterprise E1080 server as the first system available.

## [2026-07-17] merge_pending | nvidia_a100_tensor_core.md
target_page: nvidia_a100_tensor_core.md
canonical_name: NVIDIA A100
colliding_name: NVIDIA A100 Tensor Core GPU
source: https://jingchaozhang.github.io/A100-white-paper/
status: pending_review
<!-- merge_draft_body
# NVIDIA A100 Tensor Core GPU

The NVIDIA A100 Tensor Core GPU is a data center accelerator based on the Ampere architecture, introduced in 2020 as the successor to the V100. It features third-generation Tensor Cores supporting a wide range of data types including TF32, FP64, FP16, BF16, INT8, INT4, and binary, enabling mixed-precision matrix operations for AI training and inference. The A100 introduces TF32 operations that deliver 10x faster performance than FP32 FMA operations on V100, and when used with fine-grained structured sparsity, INT8 Tensor Core operations achieve 20x more performance than V100. The GPU supports Multi-Instance GPU (MIG) for spatial partitioning into up to seven isolated instances, each with dedicated memory, cache, and compute resources. For multi-GPU scaling, the A100 uses third-generation NVLink (600 GB/s per GPU) and NVSwitch (4.8 TB/s aggregate bandwidth) for high-speed GPU-to-GPU communication. The DGX A100 system incorporates eight A100 GPUs with six NVSwitch chips, Mellanox ConnectX-6 HDR InfiniBand/200GbE networking, and PCIe Gen4 connectivity to CPUs and NVMe storage.

## Key Claims

- TF32 Tensor Core operations on A100 run 10x faster than FP32 FMA operations on the previous generation V100.
- Compared to V100, TF32 on A100 provides over 6x speedup for training BERT-Large.
- With fine-grained structured sparsity and the 2:4 pattern, INT8 Tensor Core operations on A100 offer 20x more performance than V100, and FP16 operations are 5x faster.
- MIG spatial partitioning provides fully isolated GPU memory, cache, and streaming multiprocessor resources per instance.
- Six third-generation NVSwitch chips enable GPU-to-GPU communication at 600 GB/s per switch and 4.8 TB/s total aggregate bandwidth in both directions.
- Third-generation NVLink provides 12 interconnects per GPU connecting to six NVSwitches (two links per switch).
- DGX A100 includes eight single-port Mellanox ConnectX-6 200 Gb/s HDR InfiniBand ports (configurable as 200GbE) providing 3.2 Tb/s peak bandwidth.
- PCIe Gen4 x16 buses provide 31.5 Gb/s per link for a total of 252 Gb/s per GPU access to network and storage.
- Supported software includes TensorFlow, PyTorch, and MXNet via NGC Deep Learning Containers starting with release 20.06.

## Relationships

- [[nvidia_blackwell_b200]]: Both the A100 and B200 are NVIDIA data center GPU accelerators, but the A100 is based on the Ampere architecture while the B200 uses the newer Blackwell architecture. The B200 significantly improves upon A100 with higher memory bandwidth (8 TB/s vs ~2 TB/s), more transistors (208B vs 54B), and newer NVLink 5 interconnect.
- [[amd_instinct_mi100]]: The A100 and AMD Instinct MI100 are contemporary data center GPU accelerators targeting HPC and AI workloads. Both support mixed-precision Tensor/Matrix Core operations, HBM2 memory, and PCIe Gen4, but the A100 features NVLink/NVSwitch for multi-GPU scaling while the MI100 uses Infinity Fabric.

## Sources

- [A100 White Paper - Jingchao's Website](raw/cache/69a6e0f6cd16cfa7.md)
merge_draft_body -->

## [2026-07-17] merge_pending | nvidia_a100_tensor_core.md
target_page: nvidia_a100_tensor_core.md
canonical_name: NVIDIA A100
colliding_name: Nvidia A100
source: https://www.nextbigfuture.com/2020/08/eight-nvidia-a100-next-generation-tensor-chips-for-5-petaflops-at-200000.html
status: pending_review
<!-- merge_draft_body
# Nvidia A100

The Nvidia A100 is a GPU architecture based on the Ampere microarchitecture, featuring third-generation Tensor Cores for artificial intelligence acceleration. Presented at Hot Chips 2020, the A100 is designed for data center AI workloads, offering significant performance improvements over its predecessor V100 and competing chips such as the Google TPU v3 and Huawei Ascend. The chip contains 54 billion transistors and can be partitioned into seven independent GPU instances to enable multi-tenant serving. In the DGX A100 system, eight A100 GPUs together deliver 5 petaflops of AI performance, with 320 GB of total GPU memory and 12.4 TB/s of aggregate memory bandwidth. According to NVIDIA, the A100 provides up to 20x higher performance over the prior generation and even outperforms the unreleased Google TPU v4 in most categories.

## Key Claims

- Third-generation Nvidia Tensor Core GPU, based on the Ampere architecture.
- Delivers up to 20x higher performance than the prior generation V100.
- Faster and more efficient than competing chips including the Google TPU v3, Huawei Ascend, and even the unreleased Google TPU v4 in most categories.
- Contains 54 billion transistors.
- Can be partitioned into seven GPU instances for multi-tenancy.
- A DGX A100 system includes eight A100 GPUs, achieving 5 petaflops of AI performance.
- The system provides 320 GB total GPU memory and 12.4 TB/s memory bandwidth.
- Memory bandwidth reaches 12.4 TB/s per system.

## Relationships

- [[alphawave_semi_hbm_subsystem]]: The Nvidia A100 uses HBM2E memory, which complies with the same JEDEC HBM2E specification supported by the Alphawave Semi HBM Subsystem.

## Sources

- [Eight Nvidia A100 Next Generation Tensor Chips for 5 Petaflops at ...](raw/cache/fe3b2aec312d3932.md)
merge_draft_body -->

## [2026-07-17] merge_pending | nvidia_blackwell_platform.md
target_page: nvidia_blackwell_platform.md
canonical_name: NVIDIA Blackwell Platform
colliding_name: NVIDIA Blackwell Architecture
source: https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/
status: pending_review
<!-- merge_draft_body
# NVIDIA Blackwell Architecture

The NVIDIA Blackwell Architecture is a GPU microarchitecture designed for AI factories and generative AI workloads, manufactured on a custom TSMC 4NP process with 208 billion transistors. It employs a dual-reticle design where two reticle-limited dies are connected via a high-speed chip-to-chip interconnect providing 10 terabytes per second (TB/s) of bandwidth, forming a unified single GPU. The architecture introduces a second-generation Transformer Engine with micro-tensor scaling techniques that enable 4-bit floating point (FP4) AI computation, optimizing performance and accuracy. Blackwell also debuts NVIDIA Confidential Computing with hardware-based security, becoming the first GPU capable of TEE-I/O (Trusted Execution Environment I/O) to protect sensitive data and AI models during training and inference.

## Key Claims

- Manufactured on TSMC 4NP process with 208 billion transistors.
- Uses a dual-reticle design with two dies connected via a 10 TB/s chip-to-chip interconnect.
- Integrates a second-generation Transformer Engine with micro-tensor scaling for 4-bit floating point (FP4) AI.
- Supports FP4 precision, doubling memory performance for next-generation models.
- Includes NVIDIA Confidential Computing with hardware-based security; first TEE-I/O capable GPU.
- Confidential Computing delivers nearly identical throughput compared to unencrypted modes.

## Relationships

- [[nvidia_blackwell_ultra]]: The NVIDIA Blackwell Ultra is a specific high-end implementation within the Blackwell Architecture, offering 2x attention-layer acceleration and 1.5x more AI compute FLOPS compared to base Blackwell GPUs.
- [[nvidia_hopper_architecture]]: The Blackwell Architecture succeeds the Hopper Architecture, introducing the second-generation Transformer Engine, FP4 precision, and confidential computing capabilities.

## Sources

- [The Engine Behind AI Factories | NVIDIA Blackwell Architecture](raw/cache/4e3cfb5f66900140.md)
merge_draft_body -->

## [2026-07-17] merge_pending | nvidia_blackwell_platform.md
target_page: nvidia_blackwell_platform.md
canonical_name: NVIDIA Blackwell Platform
colliding_name: NVIDIA Blackwell GPU
source: https://wccftech.com/nvidia-blackwell-ai-deep-dive-nv-hbi-fuse-two-ai-gpus-together-5th-gen-tensor-cores-5th-gen-nvlink-spectrum-x/
status: pending_review
<!-- merge_draft_body
# NVIDIA Blackwell GPU

The NVIDIA Blackwell GPU is a high-performance graphics processing unit built on the NVIDIA Blackwell architecture, designed for AI training and inference workloads in large-scale data centers. The GPU uses a dual-reticle design that fuses two reticle-limited dies via the NVIDIA High-Bandwidth Interface (NV-HBI), providing 10 TB/s of bidirectional die-to-die interconnect bandwidth. Manufactured on the TSMC 4NP process node, the chip contains 208 billion transistors on a die area greater than 1600 mm². Blackwell introduces a fifth-generation Tensor Core architecture with micro-tensor scaled floating-point formats including FP4, FP6, and FP8, enabling up to 20 PetaFLOPS of FP4 AI compute. The GPU is equipped with 8-site HBM3e memory offering 8 TB/s of memory bandwidth and features fifth-generation NVLink with 1.8 TB/s bidirectional bandwidth, scaling to 576 GPUs. The architecture also includes a Transformer Engine, a Secure AI engine with full-performance encryption and Trusted Execution Environment (TEE), a RAS engine capable of 100% in-system self-test, and a decompression engine with 800 GB/s bandwidth. The NVIDIA GB200 NVL72 system combines 72 Blackwell GPUs with 36 Grace CPUs in a liquid-cooled, rack-scale solution.

## Key Claims

- The Blackwell GPU is a dual-die design using NV-HBI, a high-bandwidth die-to-die interconnect achieving 10 TB/s bidirectional bandwidth with low energy per bit and full coherence.
- The GPU contains 208 billion transistors on TSMC 4NP with a die area exceeding 1600 mm².
- Peak AI compute reaches 20 PetaFLOPS for FP4, with 2x speedup per clock per SM over Hopper for FP16/BF16/FP8, 2x for FP6 over Hopper FP8, and 4x for FP4 over Hopper FP8.
- Memory subsystem uses 8-site HBM3e, providing 8 TB/s of memory bandwidth.
- Fifth-generation NVLink provides 1.8 TB/s bidirectional bandwidth per GPU, scaling up to 576 GPUs using 18 NVLink links each at 100 GB/s.
- The fourth-generation NVLink Switch chip (over 800 mm² on TSMC 4NP) extends NVLink to 72 GPUs with 7.2 TB/s all-to-all bidirectional bandwidth and SHARP in-network compute of 3.6 TFLOPs.
- Blackwell includes NVIDIA Quasar Quantization, which converts low-precision FP4 to high-accuracy output with MMLU scores equivalent to BF16 on LLMs.
- The GB200 NVL72 system integrates 72 Blackwell GPUs and 36 Grace CPUs in a liquid-cooled rack.
- Over 400 optimized CUDA-X libraries support Blackwell for maximum performance across diverse application domains.

## Relationships

- [[nvidia_blackwell_ultra]]: The NVIDIA Blackwell Ultra GPU is a higher-performance variant of the Blackwell architecture, also using NV-HBI and fifth-generation Tensor Cores but with 160 SMs and 640 Tensor Cores compared to the standard Blackwell's configuration, and delivering 15 PetaFLOPS NVFP4 compute. Both share the same foundational dual-reticle design, TSMC 4NP process, and NV-HBI interconnect.
- [[alphawave_semi_hbm_subsystem]]: Blackwell's HBM3e memory subsystem uses the same JEDEC-standard high-bandwidth memory interface as the Alphawave Semi HBM Subsystem, both targeting AI and HPC workloads with 2.5D/3D integration.

## Sources

- [NVIDIA Deep-Dives Into Blackwell Infrastructure: NV-HBI Used ... - Wccftech](raw/cache/92346b78e6442f9d.md)
merge_draft_body -->

## [2026-07-17] merge_pending | nvidia_blackwell_b200.md
target_page: nvidia_blackwell_b200.md
canonical_name: NVIDIA Blackwell B200
colliding_name: NVIDIA Blackwell B200
source: https://arxiv.org/abs/2512.02189v3
status: pending_review
<!-- merge_draft_body
# NVIDIA Blackwell B200

NVIDIA Blackwell B200 is a dual-chip GPU architecture introduced as the successor to the Hopper H100/H200 generation, incorporating fifth-generation tensor cores, a dedicated tensor memory (TMEM), and a hardware decompression engine (DE) to accelerate deep learning and high-performance computing workloads. The architecture supports a broad range of floating-point precisions including FP32, FP16, FP8, FP6, and FP4, and is designed to improve throughput and energy efficiency for mixed-precision training and inference. According to microbenchmarking studies, the B200 tensor core enhancements achieve 1.85x ResNet-50 and 1.55x GPT-1.3B mixed-precision training throughput over the H200, with 32% better energy efficiency.

## Key Claims

- Fifth-generation tensor cores with tensor memory (TMEM) and decompression engine (DE).
- Dual-chip design for increased compute density.
- Supports FP32, FP16, FP8, FP6, and FP4 floating-point precisions.
- 1.85x ResNet-50 mixed-precision training throughput compared to H200.
- 1.55x GPT-1.3B mixed-precision training throughput compared to H200.
- 32% better energy efficiency than H200.
- Open-source microbenchmark suite for Blackwell architecture analysis.

## Relationships

No specific relationship to visible context pages in the current wiki. The Blackwell B200 is a distinct GPU microarchitecture that does not share direct architectural features with the AMD GPU Architecture or Alphawave Semi HBM Subsystem pages currently present.

## Sources

- [Microbenchmarking NVIDIA's Blackwell Architecture: An in-depth ...](raw/cache/5b2f2622c26a524e.md)
merge_draft_body -->
