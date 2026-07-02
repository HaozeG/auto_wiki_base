# Wiki Patch Queue

## [2026-07-01] merge_pending | k230.md
target_page: k230.md
canonical_name: K230
colliding_name: Kendryte K230
source: https://www.electronics-lab.com/canmv-k230-ai-development-board-with-kendryte-k230-risc-v-processor-and-6-tops-npu/
status: pending_review
<!-- merge_draft_body
# Kendryte K230

The Kendryte K230 is a 64-bit dual-core RISC-V SoC developed by Canaan Technology, designed for edge AI applications such as computer vision and intelligent interaction. It integrates two RISC-V cores: a high-performance core operating at up to 1.6 GHz and an efficient core at 800 MHz, both supporting the RISC-V Vector Extension 1.0 with hardware floating-point support. The chip includes a dedicated neural processing unit (NPU) capable of 6 TOPS (INT8) for accelerating AI inference workloads. It features a built-in convolution accelerator and is packaged with 1 GB of LPDDR4 memory on development boards. The K230 is the successor to the K210, claiming a 13.7x performance improvement. It targets AI vision applications and is supported by the CanMV open-source framework, enabling Python-based development for rapid prototyping.

## Key Claims

- 64-bit dual-core RISC-V processor with RISC-V Vector Extension 1.0 support, cores at 1.6 GHz and 800 MHz.
- Integrated 6 TOPS NPU for AI inference acceleration.
- Hardware floating-point support and convolution accelerator.
- 1 GB LPDDR4 memory on development platforms.
- Successor to K210 with 13.7x performance improvement.
- Supports 1080p/60fps HDMI output and camera connectivity.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit dual-core with Vector Extension 1.0.
- Vector/matrix/accelerator support: 6 TOPS NPU, convolution accelerator.
- Memory/cache/TLB/DMA: 1 GB LPDDR4 (on-board), MicroSD storage expansion up to 512 GB.
- Compiler/toolchain support: CanMV Python framework, MLIR and xDSL pipelines demonstrated for GEMM optimization (see [[mlir_xdsl_rvv_gemm_codegen_recipe]]).

## Relationships

- The K230 is the target hardware for the MLIR+xDSL lowering pipeline for RVV GEMM micro-kernels: [[mlir_xdsl_rvv_gemm_codegen_recipe]].
- As a RISC-V AI accelerator SoC, it is comparable to the [[xuantie_c908]] from T-Head, though from a different vendor and with a different architectural focus (NPU-based vs. vector-extension-based acceleration).
- The K230 serves as the successor to the earlier Kendryte K210 chip, though no dedicated page exists yet for that predecessor.

## Sources

- https://www.electronics-lab.com/canmv-k230-ai-development-board-with-kendryte-k230-risc-v-processor-and-6-tops-npu/
merge_draft_body -->

## [2026-07-01] pending | k230.md
target_page: k230.md
target_section: Board Features
source: https://www.hackster.io/canaan-kendryte-team/kendryte-k230-risc-v64-board-canmv-k230-d3e86a
status: pending_review
proposed_update: Add board-level specifications for CANMV-K230: board dimensions 56x85mm, USB2.0 OTG, 100Mbps Ethernet, HDMI and MIPI DSI display (max 1920x1080@60fps), 500M camera, audio interface, I2C, PWM, GPIO, and references to GitHub documentation (k230_docs) and SDK (k230_sdk) repositories, as well as support for RT-Thread IoT OS and Buildroot.

## [2026-07-01] pending | k230.md
target_page: k230.md
target_section: entire
source: https://www.kendryte.com/k230/en/main/K230_brief_datasheet.html
status: pending_review
proposed_update: Expand K230 hardware_target page with detailed specifications from the product brief datasheet: ISP (8MP@30fps, 3A, 2DNR/3DNR, WDR/HDR, local tone mapping, RGB-IR 4x4 pattern), video input (3x MIPI CSI), video output (1x MIPI DSI 2MP@60fps), video codec (H.264/H.265 encoding 8MP@20fps, decoding 8MP@40fps, JPEG/MJPEG, CBR/VBR/CQP/ROI), audio (2 DAC, 2 ADC, ALC, up to 8 PDM DMIC inputs, I2S 2x2 expansion), DPU (3D structured light depth calculation up to 1920x1080, operators: Img_check/LCN/SAD/Post_proc/Align/Disptodepth, typical 1280x800@30fps), memory (DDR3L@1600Mbps, LPDDR3@2133Mbps, LPDDR4@2667Mbps, max 2GB, SIP 128MB 16bit LPDDR4@3200Mbps, SRAM 2MB+2MB), security (PUF/OTP/TRNG, AES, SHA, RSA, SM2/3/4, ECC), PMU (deep sleep ≤20uW, RTC 32KHz, long/short press detection, IO edge/level detection, 512 bits system log on shutdown), peripherals (5 UART, 5 I2C, 6 PWM, 64 GPIO+8 PMU GPIO, 2 USB 2.0 OTG, 2 SDxC SD3.01/eMMC5.0, 1 OSPI + 2 QSPI, WDT/RTC/Timer), decompression module (≥400MB/s GZIP), 4096-point FFT/IFFT unit, fastboot (3A first picture ≤400ms), package (BGA 0.65mm pitch, 13x13mm, 11x11mm SIP). Update Optimization-Relevant Details to include DPU, video codec, ISP, and security accelerators. Add typical applications: 3D face lock and smart dictionary pen.

## [2026-07-01] merge_pending | xuantie-c910.md
target_page: xuantie-c910.md
canonical_name: XuanTie C910
colliding_name: Xuantie C910
source: https://github.com/XUANTIE-RV/buildroot
status: pending_review
<!-- merge_draft_body
# Xuantie C910

The Xuantie C910 is a 64-bit RISC-V core developed by T-Head Semiconductor, designed for high-performance applications such as 3D graphics, visual AI, and multimedia processing. It implements the rv64imafdcsu ISA profile with support for vector operations (version 0.7.1 as confirmed by boot-time logs on the ICE SoC). Each core features a 64 kB instruction cache and a 64 kB data cache, a 2 MB shared L2 cache, and a 1024-entry four-way set-associative TLB. The core operates at a clock frequency of up to 1.2 GHz. The ICE SoC integrates three C910 cores together with a GPU core, providing capabilities including 4K@60 HEVC/AVC/JPEG decoding and a variety of high-speed interfaces and peripherals. T-Head provides a customized Buildroot distribution and U-Boot bootloader to support Linux system building for the RVB-ICE board based on this SoC.

## Key Claims

- Implements rv64imafdcsu ISA with vector extension version 0.7.1.
- Three-core configuration in the ICE SoC, each core running at 1.2 GHz.
- Per-core caches: 64 kB instruction cache and 64 kB data cache; shared 2 MB L2 cache.
- TLB: 1024 entries, 4-way associative.
- Supports 4K@60 HEVC/AVC/JPEG hardware decoding via integrated GPU.
- Buildroot and U-Boot are available as open-source with T-Head customizations for building Linux systems.
- The RVB-ICE development board (SoC ICE) provides UART and fastboot flashing support.

## Optimization-Relevant Details

- ISA/profile: rv64imafdcsu with vector extension 0.7.1.
- Vector/matrix/accelerator support: Vector unit (version 0.7.1), GPU for graphics/media.
- Memory/cache/TLB/DMA: 64 kB I-cache, 64 kB D-cache per core; 2 MB L2; 1024-entry, 4-way TLB; DRAM up to 4 GiB on ICE board.
- Compiler/toolchain support: Custom Buildroot (Xuantie fork) for cross-compilation; U-Boot bootloader; thead-tools for flashing via UART.

## Relationships

- Similar core from same vendor: [[xuantie_c908]]
- Related optimized kernel targeting the same architecture family: [[xuantie_c908_fp16_gemm_kernel]]
- The RVB-ICE board is the reference platform for this hardware target.

## Sources

- https://github.com/XUANTIE-RV/buildroot
- https://occ.t-head.cn/community/risc_v_en/detail?id=RVB-ICE
merge_draft_body -->

## [2026-07-01] merge_pending | xuantie-c910.md
target_page: xuantie-c910.md
canonical_name: XuanTie C910
colliding_name: Xuantie C910
source: https://chipsandcheese.com/p/alibabat-heads-xuantie-c910
status: pending_review
<!-- merge_draft_body
# Xuantie C910

The Xuantie C910 is a 3-wide out-of-order RISC-V processor core developed by T-HEAD Semiconductor, a wholly owned subsidiary of Alibaba. It implements a 12-stage pipeline and supports the RISC-V vector extension (version V0.7.1), making it one of the few out-of-order RISC-V cores with vector support to have been fabricated in hardware. Fabricated on TSMC's 12nm FinFET process with a target frequency of 2 to 2.5 GHz, a single C910 core occupies approximately 0.8 mm². The core features a 32KB/64KB configurable Harvard L1 instruction and data cache with cache coherency support, and is implemented in clusters of up to four cores sharing a slow and small L2 cache without a mid-level cache. The CIU (Cluster Interconnect Unit) provides inter-core data transfers within the cluster with reasonable latency. The C910 is T-HEAD's first out-of-order core, and some revisions supporting V0.7.1 have also been labeled as C920.

## Key Claims

- 3-wide out-of-order core with a 12-stage pipeline.
- First out-of-order core from T-HEAD Semiconductor.
- Supports RISC-V vector extension version V0.7.1.
- Fabricated on TSMC 12nm FinFET process, targets 2 to 2.5 GHz.
- Single core area: approximately 0.8 mm².
- Configurable 32KB/64KB Harvard L1 instruction and data cache with cache coherency.
- Cluster of up to four cores with a shared L2 cache described as slow and small, with no mid-level cache.
- CIU provides inter-core data transfer with latency significantly better than SiFive P550, which exhibited over 300 ns within a quad-core cluster.
- Some C910 silicon implementing V0.7.1 vector extension has been marketed as C920, making model numbering ambiguous.

## Optimization-Relevant Details

- ISA/profile: RISC-V with vector extension V0.7.1.
- Vector/matrix/accelerator support: Vector extension V0.7.1 (not yet ratified version).
- Memory/cache/TLB/DMA: 32KB/64KB Harvard L1 I/D cache; shared L2 cache (weak, slow); no mid-level cache.
- Compiler/toolchain support: Not specified in source.

## Relationships

- [[xuantie_c908]] — later-generation RISC-V core from T-HEAD with RISC-V Vector Extension 1.0 and instruction fusion.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]] — optimization recipe targeting RISC-V vector extension, applicable to C910's vector unit.

## Sources

- https://chipsandcheese.com/p/alibabat-heads-xuantie-c910
merge_draft_body -->

## [2026-07-01] merge_pending | sifive_intelligence_x280.md
target_page: sifive_intelligence_x280.md
canonical_name: SiFive Intelligence X280
colliding_name: SiFive Intelligence X280
source: https://www.sifive.com/blog/introduction-to-the-sifive-intelligence-x280
status: pending_review
<!-- merge_draft_body
# SiFive Intelligence X280

The SiFive Intelligence X280 is a multi-core, multi-cluster capable RISC-V processor designed for AI/ML compute at the edge. It implements the RISC-V Vector Extension (RVV) v1.0 with 512-bit vector registers, enabling up to 4096-bit vector operations through LMUL=8. The processor features decoupled scalar and vector pipelines for parallel execution of scalar and vector computations, and integrates SiFive Intelligence Extensions, custom instructions that accelerate AI/ML performance-critical operations. It supports virtual memory with up to 48-bit addressing, flexible connectivity to SoC peripherals, and multi-core configuration options with up to 8 cores. The X280 is marketed as a second-generation Intelligence processor (Gen 2) and builds on the X280 core complex with scalable, configurable IP. The scalar unit is a RISC-V 64-bit 8-stage dual-issue in-order pipeline, paired with a vector unit supporting variable vector length computation.

## Key Claims

- Implements RISC-V Vector Extension v1.0 with 512-bit vector register length and up to 4096-bit operations via LMUL=8.
- Features decoupled scalar and vector pipelines for optimum parallel execution.
- Includes SiFive Intelligence Extensions, custom instructions that accelerate AI/ML performance-critical operations.
- Supports multi-core, multi-cluster configurations with up to 8 cores.
- Provides virtual memory support with up to 48-bit addressing.
- Offers high-performance, flexible connectivity to SoC peripherals.
- Scalar pipeline: RISC-V 64-bit, 8-stage, dual-issue, in-order.
- Optimized for AI/ML compute at the edge.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit (RV64) with RVV v1.0.
- Vector/matrix/accelerator support: 512-bit vector registers, SiFive Intelligence Extensions (custom AI instructions), RVV v1.0.
- Memory/cache/TLB/DMA: Virtual memory up to 48-bit addressing; details on cache hierarchy not provided in available snippets.
- Compiler/toolchain support: Not documented in available sources; SiFive typically provides toolchain support (GCC/LLVM with RVV).

## Relationships

- Related RISC-V AI accelerator core: [[xuantie_c908]]
- Related matrix engine design: [[rvme]]
- Related code generation approach: [[mlir_xdsl_rvv_gemm_codegen_recipe]]

## Sources

- https://www.sifive.com/blog/introduction-to-the-sifive-intelligence-x280
- https://thincb2b.com/intelligence-processor-gets-smarter/
- https://www.cnx-software.com/
- https://www.techpowerup.com/
merge_draft_body -->

## [2026-07-01] merge_pending | sifive_intelligence_x280.md
target_page: sifive_intelligence_x280.md
canonical_name: SiFive Intelligence X280
colliding_name: SiFive X280
source: https://reviews.llvm.org/D149710
status: pending_review
<!-- merge_draft_body
# SiFive X280

The SiFive X280 is a 64-bit RISC-V processor core from SiFive that implements the SiFive7 scheduler model and provides support for the RISC-V Vector Extension (RVV) 1.0, including multiple vector length configurations (32, 64, 128, 256, and 512 bits). It includes the standard extensions M, A, F, D, C, Zfh, Zvfh (experimental), Zba, Zbb, along with the Zicsr and Zifencei features. Designed for AI/ML workloads in the datacenter, the X280 is part of SiFive's Intelligence product line. LLVM added target support for this processor in 2023, enabling compilation with `-mcpu=sifive-x280` which automatically enables the appropriate feature flags and uses the SiFive7 scheduling model.

## Key Claims

- The SiFive X280 is supported in LLVM as a target CPU via `-mcpu=sifive-x280`, enabling vector and sub-vector length extensions (Zvl32b, Zvl64b, Zvl128b, Zvl256b, Zvl512b). (source: D149710)
- It uses the SiFive7 scheduler model for instruction scheduling in LLVM. (source: D149710)
- The processor is targeted at AI/ML applications in the datacenter, with multi-core capabilities and vector processing. (source: SiFive Intelligence X280 product descriptions as referenced in evidence snippets)

## Optimization-Relevant Details

- ISA/profile: RV64, with extensions M, A, F, D, C, V, Zfh, Zvfh, Zba, Zbb, Zicsr, Zifencei, Zvl32b, Zvl64b, Zvl128b, Zvl256b, Zvl512b.
- Vector/matrix/accelerator support: Full RVV 1.0 support with variable vector lengths up to 512 bits.
- Memory/cache/TLB/DMA: Not explicitly detailed in the LLVM patch; refer to SiFive documentation.
- Compiler/toolchain support: LLVM (from version 17) with `-mcpu=sifive-x280`.

## Relationships

- [[mlir_xdsl_rvv_gemm_codegen_recipe]] This optimization recipe targets RISC-V Vector code generation and can be compiled for the SiFive X280 using the LLVM RISC-V backend.
- [[llvm_riscv_target]] The LLVM RISC-V target backend provides the compiler support for the SiFive X280, including the scheduler model and feature definitions.

## Sources

- D149710: [RISCV] Add sifive-x280 processor with all of its extensions. LLVM Phabricator. https://reviews.llvm.org/D149710
merge_draft_body -->

## [2026-07-01] pending | llvm_riscv_target.md
target_page: llvm_riscv_target.md
target_section: Key Claims
source: https://reviews.llvm.org/D149710
status: pending_review
proposed_update: Add a new Key Claim: 'The SiFive X280 processor is supported as -mcpu=sifive-x280 starting from LLVM 17 (commit rG839469436afc), with features including RVV, Zvl, Zfh, Zvfh, Zba, Zbb, and the SiFive7 scheduler model.' Also add a relationship link to the new page [[sifive_x280]] in Relationships section.

## [2026-07-01] merge_pending | sifive_intelligence_x280.md
target_page: sifive_intelligence_x280.md
canonical_name: SiFive Intelligence X280
colliding_name: SiFive Intelligence X280
source: https://www.sifive.com/press/tenstorrent-selects-sifive-intelligence-x280-for-next-generation1
status: pending_review
<!-- merge_draft_body
# SiFive Intelligence X280

The SiFive Intelligence X280 is a 64-bit RISC-V processor core from SiFive, Inc., designed to accelerate machine learning workloads through a comprehensive suite of vector instructions called SiFive Intelligence Extensions. It features a dual-issue, in-order 8-stage pipeline and supports coherent multi-core configurations, making it suitable for Linux-capable systems-on-chip (SoCs). The X280 supports a wide range of data types critical for AI workloads, including BF16, FP16, FP32, FP64, and integer types from 8-bit to 64-bit. In April 2021, Tenstorrent, a next-generation AI computing company, announced that it had selected the X280 for its upcoming AI training and inference SoC, which will integrate Tenstorrent's Tensix AI cores. The Tensix architecture is initially targeting datacenter deployments, with versions planned for near-edge and micro-edge devices. This selection signals the X280's role as a vector-capable RISC-V core suitable for high-performance AI accelerator designs, providing a programmable vector processing unit that complements dedicated tensor cores.

## Key Claims

- The SiFive Intelligence X280 is a 64-bit RISC-V core with an 8-stage dual-issue in-order pipeline.
- It implements SiFive Intelligence Extensions, a set of vector instructions designed to accelerate machine learning workloads.
- Supports data types BF16, FP16, FP32, FP64, and integer types from int8 to int64.
- The core is multi-core coherent and Linux-capable, based on the U7 series core.
- Tenstorrent selected the X280 for its next-generation AI processor, integrating it with Tensix AI cores for training and inference.
- The Tensix-based SoC targets datacenter, near-edge, and micro-edge applications.

## Relationships

- The X280 is a RISC-V core developed by [[sifive]] (entity page not yet present in wiki).
- The processor is designed for AI acceleration, a domain also addressed by the [[mlir_xdsl_rvv_gemm_codegen_recipe]] which targets RISC-V Vector code generation for GEMM workloads.
- The [[k230]] SoC from Canaan integrates a different RISC-V core (C908), but like the X280 is used in AI-capable systems and benefits from vector extension support.
- Insufficient context for additional cross-links to entity pages; this note acknowledges that fewer than two related entity pages exist in current wiki context.

## Sources

- https://www.sifive.com/press/tenstorrent-selects-sifive-intelligence-x280-for-next-generation1
merge_draft_body -->

## [2026-07-01] merge_pending | mlperf_inference_tiny_benchmark_suite.md
target_page: mlperf_inference_tiny_benchmark_suite.md
canonical_name: MLPerf Inference: Tiny
colliding_name: MLPerf Tiny Benchmark
source: https://www.researchgate.net/publication/352397004_MLPerf_Tiny_Benchmark
status: pending_review
<!-- merge_draft_body
# MLPerf Tiny Benchmark

MLPerf Tiny is the first industry-standard benchmark suite for ultra-low-power tiny machine learning (TinyML) systems. Developed by more than 50 organizations in academia and industry, it provides a set of four standard benchmarks—keyword spotting, visual wake words, image classification, and anomaly detection—to evaluate deep neural network inference on resource-constrained devices such as microcontrollers, digital signal processors (DSPs), and tiny neural network accelerators. The benchmark suite captures the inherent tradeoffs in TinyML by measuring latency, energy consumption, and accuracy across these workloads. It defines two submission divisions: a stricter closed division that requires identical models and preprocessing, and a more flexible open division that allows customization, enabling reproducible comparison across a wide range of hardware platforms. The benchmark framework is based on EEMBC's software development platform and is open-source, hosted under MLCommons.

## Key Claims

- First industry-standard benchmark suite specifically designed for ultra-low-power TinyML systems.
- Provides four representative benchmarks (keyword spotting, visual wake words, image classification, anomaly detection) selected through community consensus of more than 50 organizations.
- Measures latency, energy, and accuracy to capture the tradeoffs inherent to TinyML inference.
- Two submission divisions: closed (strict, reproducible) and open (flexible, encouraging innovation).
- Built on the EEMBC software development platform for consistent measurement methodology.
- Open-source implementation available on GitHub under MLCommons/tiny.
- Aims to enable fair comparison across microcontrollers, DSPs, and tiny NN accelerators.

## Relationships

- [[xuantie_c908]]: A RISC-V processor core capable of running TinyML inference workloads that could be evaluated via the MLPerf Tiny benchmark suite.
- [[rvme]]: A RISC-V matrix engine coprocessor design that may be applicable to TinyML inference tasks relevant to MLPerf Tiny benchmarks.

## Sources

- https://arxiv.org/abs/2106.07597
- https://www.researchgate.net/publication/352397004_MLPerf_Tiny_Benchmark
- https://github.com/mlcommons/tiny
merge_draft_body -->

## [2026-07-02] merge_pending | xuantie_c930.md
target_page: xuantie_c930.md
canonical_name: XuanTie C930
colliding_name: XuanTie C930
source: https://inf.news/en/tech/ba346db5ad34377a23c68be253a11939.html
status: pending_review
<!-- merge_draft_body
# XuanTie C930

The XuanTie C930 is a server-grade RISC-V processor core developed by the XuanTie team within Alibaba's DAMO Academy, targeting AI-HPC workloads. As Alibaba's first server-grade processor design, it operates at a main frequency exceeding 3.4 GHz and achieves a performance score of 15.2/GHz, indicating strong per-cycle performance. The core integrates the XuanTie TITAN vector engine, a large-bit-width vector unit that supports scalable vector length configurations from 512 to 4096 bits, enabling instruction-level parallel acceleration for demanding workloads. The C930 is available for licensing to system-on-chip makers, with initial shipments scheduled to begin in March.

## Key Claims

- Main frequency exceeds 3.4 GHz under typical working scenarios.
- Performance score of 15.2/GHz (benchmark unspecified).
- First server-grade processor from the XuanTie / DAMO Academy lineage, targeting AI-HPC workloads.
- Incorporates the XuanTie TITAN vector engine supporting scalable vector lengths from 512 to 4096 bits.
- Available for licensing to SoC makers; shipments begin in March.

## Optimization-Relevant Details

- ISA/profile: RISC-V (server-class profile with vector extension support).
- Vector/matrix/accelerator support: XuanTie TITAN vector engine, 512-4096-bit scalable vector length configuration, instruction-level parallel acceleration.
- Memory/cache/TLB/DMA: Not publicly disclosed.
- Compiler/toolchain support: Not publicly disclosed; common RISC-V GNU/Linux toolchains expected.

## Relationships

- [[xuantie_c908]]: Earlier-generation XuanTie core targeting AIoT and embedded AI inference, representing a different market segment from the server-class C930.
- [[xuantie_c950]]: Another server-class XuanTie core from the same family, described as newer-generation; the C930 is positioned as the first server-grade design, potentially overlapping or preceding the C950.
- [[rvme]]: A matrix engine coprocessor design co-authored by researchers from DAMO Academy and Shanghai Jiao Tong University; while not explicitly confirmed as part of C930, it shares institutional origin and is relevant to the vector/matrix acceleration landscape.

## Sources

- https://inf.news/en/tech/ba346db5ad34377a23c68be253a11939.html (news article snippet compilation)
- https://www.tomshardware.com (cited within snippets)
- https://www.benzinga.com (cited within snippets)
merge_draft_body -->

## [2026-07-02] merge_pending | allwinner_t536.md
target_page: allwinner_t536.md
canonical_name: Allwinner T536
colliding_name: Allwinner T536
source: https://www.electronics-lab.com/allwinner-t536-octa-core-risc-v-processor-supports-4k-video-ai-acceleration-and-android-linux-os/
status: pending_review
<!-- merge_draft_body
# Allwinner T536

The Allwinner T536 is a system-on-chip (SoC) designed by Allwinner Technology, a Chinese fabless semiconductor company founded in 2007 and headquartered in Zhuhai, Guangdong. Targeting industrial and AIoT applications, the T536 features an octa-core RISC-V processor (though alternative reports from CNX Software describe it as a quad-core Arm Cortex-A55 plus a 600 MHz RISC-V core configuration), an optional neural processing unit (NPU) delivering up to 3 TOPS of AI performance, support for ECC memory up to 6GB, dual Gigabit Ethernet ports, a PCIe 2.1/USB 3.1 DRD combo interface, and display interfaces including MIPI DSI, RGB, and LVDS. Camera interfaces include parallel CSI and MIPI CSI, while industrial I/O encompasses CAN FD, SPI, I2C, UART, ADCs, and PWM. The SoC integrates a G2D hardware graphics accelerator, a hardware image signal processor (ISP), and a video processing unit (VPU) supporting 4K video decoding and encoding. Storage options include SDIO 3.0, eMMC 5.1, SPI NOR/NAND, and raw NAND flash with ECC protection. Security features comprise hardware encryption, hashing algorithms, RSA/ECC signatures, a true random number generator (TRNG), and eFuse. The T536 runs both Android and Linux operating systems.

## Key Claims

- Optionally integrates an NPU with up to 3 TOPS AI performance.
- Supports ECC memory up to 6GB.
- Dual Gigabit Ethernet and PCIe 2.1/USB 3.1 DRD combo connectivity.
- MIPI DSI, RGB, and LVDS display interfaces and parallel/MIPI CSI camera interfaces.
- Industrial I/Os including CAN FD, SPI, I2C, UART, ADCs, and PWM.
- Storage: SDIO 3.0, eMMC 5.1, SPI NOR/NAND, raw NAND with ECC.
- G2D hardware graphics accelerator, hardware ISP, and VPU capable of 4K video decode/encode.
- Hardware security: encryption, hashing, RSA/ECC, TRNG, eFuse.
- Supports Android and Linux OS.

## Optimization-Relevant Details

- ISA/profile: RISC-V (exact core microarchitecture not specified in source; CNX Software notes a 600 MHz RISC-V core alongside quad Cortex-A55).
- Vector/matrix/accelerator support: Optional NPU (3 TOPS); no explicit vector extension details.
- Memory/cache/TLB/DMA: ECC memory controller supporting up to 6GB; no public cache hierarchy details.
- Compiler/toolchain support: Linux kernel and Android OS support; specific compiler toolchains not detailed.

## Relationships

- [[xuantie_c908]]: The XuanTie C908 page lists the T536 as a sibling SoC integrating a XuanTie-family RISC-V core, relevant for understanding the processor’s architectural lineage.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: This optimization recipe targets RISC-V Vector hardware code generation; the T536’s RISC-V core, while not specified for vector extensions, positions it as a potential target for similar compilation approaches in the RISC-V ecosystem.

## Sources

- https://www.electronics-lab.com/allwinner-t536-octa-core-risc-v-processor-supports-4k-video-ai-acceleration-and-android-linux-os/
- CNX Software, April 14, 2025: "Allwinner T536 quad-core Arm Cortex-A55 & RISC-V industrial SoC supports ECC RAM, up to 3 TOP AI accelerator"
merge_draft_body -->

## [2026-07-02] merge_pending | opengemm.md
target_page: opengemm.md
canonical_name: OpenGeMM
colliding_name: RVV GEMM Progressive Optimization Benchmark on Banana Pi F3 (SpaceMit K1)
source: https://github.com/AlexanderGSC/rvv-gemm
status: pending_review
<!-- merge_draft_body
# RVV GEMM Progressive Optimization Benchmark on Banana Pi F3 (SpaceMit K1)

This benchmark result presents a comprehensive performance analysis of seven progressive GEMM optimization stages running natively on a 64-bit RISC-V architecture with the RVV 1.0 vector extension, executed on a Banana Pi F3 single-board computer powered by the SpaceMit K1 octacore SoC (X60 SoC system). The study measures pure computation time for a single-precision floating-point matrix multiplication of dimensions 2000×3000×100, using the perf stat tool to collect cycles, instructions, branch statistics, and L1 data cache access/miss counts. The optimization stages are: scalar baseline compiled with -O2 (GEMM_O2), compiler auto-vectorization with -O3 (GEMM_O3), manual vector multiply-add with vle32.v/vfmul.vf/vfadd.vv using LMUL=8 (GEMM_vaddmul), fused multiply-accumulate with vfmacc.vv (GEMM_vmacc), loop nest blocking for L1 cache residency (GEMM_tiled), loop unrolling with depth 4 and ILP interleaving using LMUL=4 (GEMM_unroll), and OpenMP multithreading across eight cores (GEMM_omp). The best single-core variant (GEMM_unroll) achieves a 15.02× speedup over the scalar baseline, and the multithreaded version reaches 66.58× speedup, reducing execution time from 2.881 seconds to 0.043 seconds. The results highlight that manual optimization of data movement and instruction scheduling yields substantially better performance than compiler auto-vectorization.

## Key Claims

- GEMM_unroll (single core, loop unrolling with ILP and LMUL=4) achieves a 15.02× speedup over scalar GEMM_O2 baseline (0.192 s vs 2.881 s) and a 4× speedup over compiler auto-vectorized GEMM_O3 (0.768 s).
- GEMM_tiled (loop nest blocking) achieves ~9× speedup (0.320 s) by keeping submatrices in L1 cache, eliminating costly stores to RAM.
- GEMM_vmacc (fused multiply-accumulate) reduces instruction count from 793M to 782M compared to separate multiply/add (GEMM_vaddmul), demonstrating operation fusion.
- GEMM_unroll reduces IPC from 0.37–0.39 of early vector versions to 0.55 while actually increasing overall throughput via ILP exploitation.
- Numerical drift of order 10⁻⁵ is observed with separate multiplication and addition operations (GEMM_vaddmul), which may affect scientific computing applications.
- The compiler auto-vectorization uses LMUL=1 (conservative register pressure management), while manual versions achieve better performance with LMUL=4 or 8.
- The multithreaded version (GEMM_omp) achieves 66.58× speedup (0.043 s) by utilizing all eight cores.

## Measurement Context

- **Hardware version**: Banana BPI-F3 SBC; SpaceMit K1 octacore SoC (X60 SoC system); 8 physical cores; RVV 1.0 vector unit.
- **Software/toolchain version**: GCC with -O2, -O3 optimization flags; manual RVV 1.0 intrinsics; perf stat for measurement.
- **Workload shape**: GEMM with M=2000, K=3000, N=100 (result matrix C of size 2000×100); single-precision floating-point (fp32).
- **Metric**: Computing time (seconds), speedup (relative to GEMM_O2 baseline), CPU cycles, number of instructions, instructions per cycle (IPC), L1-dcache loads, load misses, stores, store misses.
- **Method**: perf stat command: `perf stat -e cycles,instructions,branches,branch-misses,L1-dcache-loads,L1-dcache-load-misses,L1-dcache-stores,L1-dcache-store-misses ./P3GEMM_version 2000 3000 100`; each stage is a separate executable.
- **Evidence strength**: measured (perf hardware counters).

## Relationships

- This hand-tuned optimization study can be compared to the code generation approach in [[mlir_xdsl_rvv_gemm_codegen_recipe]], which targets the same Banana Pi F3 platform but uses MLIR/xDSL to automatically generate RVV intrinsics; the hand-tuned approach achieves 66.58× speedup versus the reported 10–35% improvement over OpenBLAS for the generated kernels.
- The kernel structure (scalar→auto-vectorized→manual intrinsics→tiling→ILP→parallel) is a complementary resource to [[xuantie_c908_fp16_gemm_kernel]], which describes a fp16 GEMM outer-product kernel on a different hardware target (XuanTie C908).

## Sources

- https://github.com/AlexanderGSC/rvv-gemm (README, source code, benchmark tables)
merge_draft_body -->

## [2026-07-02] pending | mlir_xdsl_rvv_gemm_codegen_recipe.md
target_page: mlir_xdsl_rvv_gemm_codegen_recipe.md
target_section: Relationships
source: https://github.com/AlexanderGSC/rvv-gemm
status: pending_review
proposed_update: Add a note comparing the MLIR/xDSL generated kernel performance to the hand-tuned progressive GEMM benchmark on Banana Pi F3 (66.58× speedup vs scalar) to provide a reference point for manual versus automatic vectorization.

## [2026-07-02] merge_pending | xuantie_c930.md
target_page: xuantie_c930.md
canonical_name: XuanTie C930
colliding_name: XuanTie C930
source: https://zhuanlan.zhihu.com/p/1929835889116288188
status: pending_review
<!-- merge_draft_body
# XuanTie C930

XuanTie C930 is a RISC-V processor core designed by Alibaba T-Head for server-class AI and HPC workloads. It achieves a clock frequency of up to 3.4 GHz and a SPECint2006 performance of 15.2 per GHz. The core includes a 64 KB L1 cache with I-cache coherence, a private L2 cache of up to 1 MB with 64 bytes per cycle access bandwidth, and Parity/ECC support. For AI acceleration, the C930 supports the RVA23 Profile standard with enhanced vector and floating-point compute, and introduces the XuanTie Matrix extension and XuanTie coprocessor extension, providing int8 compute up to 8 TOPS with flexible compute ratio allocation.

## Key Claims

- Clock frequency up to 3.4 GHz.
- SPECint2006 score of 15.2 per GHz.
- 64 KB L1 cache with I-cache coherence.
- Up to 1 MB private L2 cache with 64 B/cycle access bandwidth and Parity/ECC.
- Supports RVA23 Profile with vector and floating-point compute enhancements.
- Introduces XuanTie Matrix extension and XuanTie coprocessor extension.
- Delivers int8 compute up to 8 TOPS with flexible compute ratio.

## Optimization-Relevant Details

- ISA/profile: RVA23 Profile (RISC-V).
- Vector/matrix/accelerator support: XuanTie Matrix extension, XuanTie coprocessor extension, vector compute, floating-point.
- Memory/cache/TLB/DMA: 64 KB L1 cache, up to 1 MB private L2 (64 B/cycle), Parity/ECC.
- Compiler/toolchain support: Not publicly specified in the source.

## Relationships

- [[xuantie_c908]]: earlier-generation XuanTie core targeting embedded AIoT; the C930 is a higher-performance server-class sibling with different market focus.
- [[xuantie_c950]]: another server-class XuanTie core from the same family; the C930 fills a distinct performance segment.
- [[xuantie_c906]]: earlier-generation core that served as a baseline for C908 speedup claims; the C930 targets a different workload domain.

## Sources

- https://zhuanlan.zhihu.com/p/1929835889116288188
merge_draft_body -->

## [2026-07-02] merge_pending | xuantie_c930.md
target_page: xuantie_c930.md
canonical_name: XuanTie C930
colliding_name: XuanTie C930
source: https://inf.news/en/tech/0099e3834452466e8dc47942e35d6956.html
status: pending_review
<!-- merge_draft_body
# XuanTie C930

The XuanTie C930 is a server-grade RISC-V processor IP developed by Alibaba's DAMO Academy, targeting high-performance server and AI computing workloads. It supports the RVA23 Profile standard, which provides vector computing, floating-point operations, and other high-performance computing capabilities. The C930 also incorporates proprietary Xuantie Matrix extensions and Xuantie coprocessor extensions, enabling an INT8 compute capacity of up to 8 TOPS with flexible compute ratio options. The core operates at a main frequency of up to 3.4 GHz. Launched in 2024 and starting delivery in March 2025, the C930 is positioned as the most powerful server RISC-V processor IP from DAMO Academy, complementing the existing XuanTie family of cores.

## Key Claims

- The XuanTie C930 is a server-grade RISC-V processor IP from Alibaba DAMO Academy, targeting high-performance server and AI workloads.
- It supports the RVA23 Profile standard, including vector and floating-point computing.
- It incorporates Xuantie Matrix extension and Xuantie coprocessor extension for enhanced AI compute.
- INT8 compute capacity up to 8 TOPS with flexible compute ratio.
- Main frequency up to 3.4 GHz.
- General computing performance reported at 15/GHz in the SPECint2006 benchmark test (15.2/GHz at 3.4 GHz).
- Launched in 2024 and delivered from March 2025.

## Optimization-Relevant Details

- ISA/profile: RISC-V with RVA23 Profile.
- Vector/matrix/accelerator support: RVA23 vector and floating-point, Xuantie Matrix extension, Xuantie coprocessor extension.
- Memory/cache/TLB/DMA: Not specified in available sources.
- Compiler/toolchain support: Not specified.

## Relationships

- [[xuantie_c908]]: Previous-generation XuanTie core targeting AIoT and embedded applications, contrasting with the server-class C930.
- [[xuantie_c950]]: Another server-class XuanTie core from the same T-Head family, representing a different model in the XuanTie server line.
- [[xuantie_c906]]: Earlier-generation XuanTie core; the C930 builds on the XuanTie core family lineage.

## Sources

- [https://inf.news/en/tech/0099e3834452466e8dc47942e35d6956.html](https://inf.news/en/tech/0099e3834452466e8dc47942e35d6956.html)
merge_draft_body -->

## [2026-07-02] merge_pending | xuantie_c930.md
target_page: xuantie_c930.md
canonical_name: XuanTie C930
colliding_name: XuanTie C930
source: https://www.eefocus.com/article/1865193.html
status: pending_review
<!-- merge_draft_body
# XuanTie C930

The XuanTie C930 is a high-performance RISC-V processor core developed by Alibaba's T-Head Semiconductor, achieving a clock frequency of 3.4 GHz and a SPECint2006 score of 15.2 per GHz. It supports the RVA23 Profile standard, bringing enhanced vector computation and floating-point performance. The core integrates the XuanTie Matrix extension and XuanTie coprocessor extension, delivering up to 8 TOPS of INT8 AI compute power. Its cache hierarchy includes 64 KB of L1 cache, I-Cache coherence support, and up to 1 MB of private L2 cache with a 64 B/cycle access bandwidth, with Parity/ECC protection.

## Key Claims

- Clock frequency of 3.4 GHz.
- SPECint2006 score of 15.2 per GHz.
- Compliant with RVA23 Profile.
- Integrates XuanTie Matrix extension and XuanTie coprocessor extension.
- INT8 AI compute up to 8 TOPS.
- L1 cache: 64 KB with I-Cache coherence.
- L2 cache: up to 1 MB private, 64 B/cycle bandwidth.
- Cache supports Parity/ECC.

## Optimization-Relevant Details

- ISA/profile: RISC-V, RVA23 Profile.
- Vector/matrix/accelerator support: XuanTie Matrix extension, XuanTie coprocessor extension, enhanced vector and floating-point.
- Memory/cache/TLB/DMA: 64 KB L1, up to 1 MB private L2, Parity/ECC.
- Compiler/toolchain support: Not specified.

## Relationships

- [[xuantie_c908]]: earlier-generation XuanTie core; the C930 targets higher performance and server-class workloads.
- [[rvme]]: a decoupled matrix-engine coprocessor for RISC-V; the C930's integrated Matrix extension provides a different approach to matrix acceleration.

## Sources

- https://www.eefocus.com/article/1865193.html
merge_draft_body -->

## [2026-07-02] pending | xuantie_c908.md
target_page: xuantie_c908.md
target_section: Relationships
source: https://www.eefocus.com/article/1865193.html
status: pending_review
proposed_update: Update the reference to XuanTie C930 to include a wiki link to the new [[xuantie_c930]] page.

## [2026-07-02] merge_pending | riscv_vector_extension.md
target_page: riscv_vector_extension.md
canonical_name: RISC-V Vector Extension (RVV)
colliding_name: RISC-V Vector Extension
source: https://github.com/riscvarchive/riscv-v-spec
status: pending_review
<!-- merge_draft_body
# RISC-V Vector Extension

The RISC-V Vector Extension (RVV) is a standard specification that defines vector processing capabilities for the RISC-V instruction set architecture. The working draft of the proposed extension is maintained in the riscvarchive/riscv-v-spec GitHub repository, which is a publicly archived repository. Version 1.0 of the specification has been frozen and undergone public review, while a version 1.1-draft is currently under development. The repository also holds the draft Zawrs (fast-track) extension and is used to make releases for reviews. The specification has evolved through several major versions. Toolchain support includes the RISC-V Proxy Kernel that supports v1.0 binaries and a Binutils port for v0.8.

## Key Claims

- The RVV specification is at version 1.1-draft, with version 1.0 frozen and publicly reviewed.
- The riscvarchive/riscv-v-spec repository serves as the authoritative working draft for the proposed RISC-V V vector extension.
- The repository also contains the draft Zawrs (fast-track) extension.
- Toolchain support: the RISC-V Proxy Kernel supports v1.0 binaries; Binutils supports v0.8.

## Relationships

- [[xuantie_c908]]: Implements RISC-V Vector Extension 1.0 as part of its ISA profile.
- [[rvme]]: The RVME matrix engine is compared against an RVV-based vector engine at matched datapath width.

## Sources

- https://github.com/riscvarchive/riscv-v-spec
merge_draft_body -->

## [2026-07-02] merge_pending | sifive_intelligence_x280.md
target_page: sifive_intelligence_x280.md
canonical_name: SiFive Intelligence X280
colliding_name: SiFive Intelligence X280
source: https://www.datacenterdynamics.com/en/news/google-deploys-sifives-intelligence-x280-processor-for-ai-workloads/
status: pending_review
<!-- merge_draft_body
# SiFive Intelligence X280

The SiFive Intelligence X280 is a multi-core capable RISC-V processor designed for AI/ML workloads in data centers. It implements the RISC-V Vector Extension and includes SiFive's custom Intelligence Extensions and the Vector Coprocessor Interface Extension (VCIX) for flexible AI hardware programming. The X280 runs a full RISC-V software stack with hypervisor support, enabling it to serve as an AI compute host. Google has deployed the X280 alongside its Tensor Processing Units (TPUs) to accelerate data feeding to matrix multiplication units, and the processor is also used by organizations including NASA, Tenstorrent, Renesas, Microchip, and Kinara.

## Key Claims

- Multi-core RISC-V processor with vector extension.
- SiFive Intelligence Extensions provide custom AI/ML instructions.
- VCIX enables flexible programming of vector coprocessors.
- Deployed as AI compute host for Google TPU.
- Runs full RISC-V software stack with hypervisor.
- Used by NASA, Tenstorrent, Renesas, Microchip, Kinara.

## Optimization-Relevant Details

- ISA/profile: RISC-V with Vector Extension, SiFive Intelligence Extensions, VCIX.
- Vector/matrix/accelerator support: VCIX for custom vector coprocessor attachments.
- Memory/cache/TLB/DMA: Not publicly documented in available sources.
- Compiler/toolchain support: GCC/LLVM with VCIX support via SiFive software flow.

## Relationships

- [[xuantie_c908]]: a competing RISC-V core from T-Head targeting AI workloads, using a different microarchitecture with a configurable vector path and no VCIX interface.
- [[k230]]: an AIoT SoC integrating RISC-V C908 cores, representing a highly integrated edge approach compared to the X280's data-center host role.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: a compiler-based optimization recipe for RISC-V vector hardware that could be adapted to the X280's VCIX and vector capabilities.

## Sources

- https://www.datacenterdynamics.com/en/news/google-deploys-sifives-intelligence-x280-processor-for-ai-workloads/
merge_draft_body -->

## [2026-07-02] merge_pending | sifive_intelligence_x280.md
target_page: sifive_intelligence_x280.md
canonical_name: SiFive Intelligence X280
colliding_name: SiFive Intelligence X280
source: https://diversedaily.com/sifive-intelligence-x280-risc-v-core-optimized-for-ai-workloads/
status: pending_review
<!-- merge_draft_body
# SiFive Intelligence X280

The SiFive Intelligence X280 is a multi-core capable RISC-V processor designed for AI/ML workloads at the edge and in the data center. It features a 64-bit RISC-V ISA with an 8-stage dual-issue in-order pipeline, a memory management unit (MMU), and caching support. The processor includes RISC-V Vector Extensions and SiFive Intelligence Extensions, which accelerate machine learning computations. The X280 supports scalable multi-core and multi-cluster designs with up to eight cores, making it suitable for diverse AI applications such as healthcare, autonomous vehicles, and smart cities. It is deployed by Google as an AI Compute Host for data-center AI workloads and is integrated into Microchip's PIC64HX1000 series of MPUs for post-quantum security and edge AI processing.

## Key Claims

- Multi-core capable RISC-V processor with vector extensions and SiFive Intelligence Extensions.
- Optimized for AI/ML compute at the edge and in the data center.
- 64-bit RISC-V ISA with 8-stage dual-issue in-order pipeline, MMU, and caching.
- Scalable multi-core and multi-cluster architecture supporting up to 8 cores.
- Google deploys the X280 as an AI Compute Host for AI workloads in the data center.
- Microchip integrates the X280 into the PIC64HX1000 series for post-quantum security and edge AI.
- Supports a wide range of AI applications across industries including healthcare, autonomous vehicles, and smart cities.

## Optimization-Relevant Details

- ISA/profile: 64-bit RISC-V ISA, 8-stage dual-issue in-order pipeline, MMU, caching, Linux-capable applications processor.
- Vector/matrix/accelerator support: RISC-V Vector Extensions (standard RVV), SiFive Intelligence Extensions (VCIX interface for custom accelerators).
- Memory/cache/TLB/DMA: Caching present; exact cache sizes and memory hierarchy not publicly detailed.
- Compiler/toolchain support: Not specified in available sources; expected to be compatible with standard RISC-V toolchains and SiFive's software flow.

## Relationships

- [[xuantie_c908]]: a comparable RISC-V AI-optimized vector processor from T-Head, sharing RVV support but differing in pipeline depth and vendor-specific extensions.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: a compilation approach for generating RVV GEMM micro-kernels, relevant to the X280's vector capabilities.
- [[k230]]: a RISC-V AIoT SoC integrating a C908 core, illustrating an alternative hardware platform for similar edge AI workloads.

## Sources

- https://diversedaily.com/sifive-intelligence-x280-risc-v-core-optimized-for-ai-workloads/
merge_draft_body -->

## [2026-07-02] merge_pending | xuantie-c910.md
target_page: xuantie-c910.md
canonical_name: XuanTie C910
colliding_name: XuanTie C910
source: https://www.riscvschool.com/2023/03/09/t-head-xuantie-c910-risc-v/
status: pending_review
<!-- merge_draft_body
# XuanTie C910

The XuanTie C910 is a 64-bit high-performance RISC-V processor core developed by T-Head Semiconductor Co., Ltd., a subsidiary of Alibaba Group. Designed for control-flow intensive and computationally demanding workloads, it employs an out-of-order 12-stage pipeline architecture to deliver industry-leading performance in control flow, computing, and frequency. The core is based on the RV64GCV instruction set and implements the XuanTie Instruction Extension (XIE) technology for custom arithmetic, bit manipulation, load/store, and TLB/cache operations. The C910 is an early adopter of the RISC-V Vector Extension, enabling variable-length vector processing for data-parallel workloads. T-Head has released the core design as open-source under the name OpenC910 on GitHub, providing a publicly accessible RTL implementation for academic and commercial use. The processor targets applications requiring high single-thread performance and has been integrated into various SoCs and systems.

## Key Claims

- Based on the RV64GCV instruction set with XuanTie Instruction Extension (XIE).
- Out-of-order 12-stage pipeline for high single-thread performance.
- Early adopter of RISC-V Vector Extension for vector processing.
- Open-source release as OpenC910 on GitHub.
- Designed for control flow, computing, and frequency efficiency.

## Optimization-Relevant Details

- ISA/profile: RV64GCV with XIE.
- Vector/matrix/accelerator support: RISC-V Vector Extension (VLEN not specified).
- Memory/cache/TLB/DMA: (not specified in source).
- Compiler/toolchain support: (not specified).

## Relationships

- [[xuantie_c908]]: sibling core in the XuanTie family, targeting AIoT with vector extension and instruction fusion.
- Insufficient context for additional cross-links.

## Sources

- https://www.riscvschool.com/2023/03/09/t-head-xuantie-c910-risc-v/
merge_draft_body -->

## [2026-07-02] merge_pending | xuantie-c910.md
target_page: xuantie-c910.md
canonical_name: XuanTie C910
colliding_name: XuanTie C910
source: https://chipsandcheese.com/p/alibabat-heads-xuantie-c910
status: pending_review
<!-- merge_draft_body
# XuanTie C910

The XuanTie C910 is a 64-bit RISC-V out-of-order superscalar processor core developed by T-HEAD Semiconductor (Alibaba Group). It is implemented in clusters of up to four cores, each cluster sharing a unified L2 cache. The core is fabricated on TSMC's 12nm FinFET process and targets clock frequencies between 2 and 2.5 GHz, with a core area of approximately 0.8 mm². The C910 features a configurable Harvard L1 cache (32KB or 64KB each for instructions and data) with cache coherency support. A notable architectural characteristic is the absence of a mid-level cache, leaving L1 misses to directly access the shared L2 cache, which is described as both slow and small. The core's DRAM bandwidth is also noted as lackluster. The C910 is T-HEAD's first out-of-order RISC-V core, distinguishing it from earlier in-order designs like the C906 and C908.

## Key Claims

- First out-of-order RISC-V core from T-HEAD.
- Fabricated on TSMC 12nm FinFET, target 2-2.5 GHz.
- Core area 0.8 mm².
- Cluster of up to 4 cores with shared L2.
- Configurable 32KB/64KB Harvard L1 I-cache and D-cache with coherency.
- No mid-level cache; shared L2 is slow and small.
- DRAM bandwidth is lackluster.
- CIU (core interconnect unit) provides reasonable inter-core latency, better than P550's >300 ns within quad-core cluster.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit out-of-order superscalar (specific extensions not detailed in source).
- Vector/matrix/accelerator support: Not mentioned; likely no dedicated vector unit or matrix accelerator.
- Memory/cache/TLB/DMA: 32KB/64KB L1 I-cache, 32KB/64KB L1 D-cache, shared L2 cache per cluster (size not specified), no mid-level cache. DRAM bandwidth unspecified but described as lackluster.
- Compiler/toolchain support: Not specified in source.

## Relationships

- [[xuantie_c908]]: The C908 is a later in-order core from T-HEAD focusing on AIoT with RISC-V Vector Extension 1.0, offering a contrasting design philosophy versus the C910's out-of-order design.
- [[k230]]: The K230 SoC integrates dual C908 cores, demonstrating T-HEAD's deployment of its core IP in commercial AIoT platforms, while the C910 targets higher-performance applications.

## Sources

- https://chipsandcheese.com/p/alibabat-heads-xuantie-c910
merge_draft_body -->

## [2026-07-02] merge_pending | andes_nx27v.md
target_page: andes_nx27v.md
canonical_name: Andes NX27V
colliding_name: NX27V
source: https://www.andestech.com/en/products-solutions/andescore-processors/riscv-nx27v/
status: pending_review
<!-- merge_draft_body
# NX27V

The NX27V is a 64-bit RISC-V vector processor core developed by Andes Technology Corporation, implementing the IMAFD standard instruction profiles and a dedicated Vector Processing Unit (VPU) to accelerate computation-intensive workloads such as AI inference, AR/VR, and computer vision. The core supports the Andes Custom Extension (ACE) framework, enabling customers to create custom domain-specific instructions for application-specific acceleration. The NX27V is integrated into Andes' 7nm QiLai SoC, which pairs it with a quad-core AX45MP cluster to form the compute backbone of the world's first RISC-V AI PC. Andes has also introduced DSP instruction set extensions for the NX27V and other multi-core RISC-V processors targeting HPC markets. The processor is designed for broad market segments requiring high vector throughput and supports the latest RISC-V vector specification.

## Key Claims

- 64-bit RISC-V vector processor supporting IMAFD standard instructions.
- Integrated Vector Processing Unit (VPU) for AI, AR/VR, and general computation acceleration.
- Andes Custom Extension (ACE) framework for custom instruction creation.
- Deployed in the 7nm QiLai SoC alongside a quad-core AX45MP cluster.
- Used in the first RISC-V AI PC.
- DSP instruction set extensions available for HPC workloads.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit with IMAFD and Vector Extension.
- Vector/matrix/accelerator support: VPU (Vector Processing Unit), ACE custom instructions.
- Memory/cache/TLB/DMA: Not specified.
- Compiler/toolchain support: Not specified.

## Relationships

- [[xuantie_c908]]: Another RISC-V vector processor core with configurable VLEN, offering a comparison point for the NX27V's fixed or unspecified vector length.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: An optimization recipe for RISC-V Vector GEMM code generation; the NX27V's VPU could serve as a target for such code generation pipelines.
- [[k230]]: An AIoT SoC integrating a different vector processor (C908), illustrating the broader landscape of RISC-V vector-capable platforms.

## Sources

- https://www.andestech.com/en/products-solutions/andescore-processors/riscv-nx27v/
merge_draft_body -->

## [2026-07-02] merge_pending | pulp_nn.md
target_page: pulp_nn.md
canonical_name: PULP-NN
colliding_name: PULP-NN
source: https://github.com/pulp-platform/pulp-nn
status: pending_review
<!-- merge_draft_body
# PULP-NN

PULP-NN is a multicore computing library for quantized neural network (QNN) inference on Parallel-Ultra-Low-Power (PULP) clusters of RISC-V based processors. It adopts the Height-Width-Channel (HWC) data layout for storing neural network weights and activations and implements convolution-based kernels as a matrix multiplication operation, a pattern inspired by ARM's CMSIS-NN open source library. The library fully exploits the Xpulp ISA extension and the cluster's parallelism to achieve high performance and energy efficiency on PULP-based devices. It includes kernels for standard convolution, pointwise convolution, depthwise convolution, and linear layers, supporting both 8-bit quantized and mixed-precision (sub-byte) computation. The library is described in Garofalo et al. (2020) and Bruschi et al. (2020), with the source code maintained on GitHub under the pulp-platform organization.

## Key Claims

- Implements convolution as im2col plus matrix multiplication using HWC data layout.
- Optimized matrix multiplication kernel (4x2 MatMul) for data reuse at register file level.
- Supports standard, pointwise, depthwise convolution and linear kernels.
- Includes both 8-bit quantized and mixed-precision (sub-byte) kernels.
- Exploits Xpulp ISA SIMD dot-product instructions for high throughput.
- Depthwise convolution uses CHW data layout for input activations and HWC for outputs.
- Structured into 8-bit and mixed sub-directories, with mixed precision being a work-in-progress extension.

## Relationships

- [[xuantie_c908]]: A RISC-V processor core that could serve as a target for PULP-NN kernels.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: Describes optimization techniques for GEMM on RISC-V vector hardware, related to the MatMul optimization in PULP-NN.
- Note: Insufficient context for additional cross-links to entity-type pages; only hardware_target and optimization_recipe pages were available.

## Sources

- https://github.com/pulp-platform/pulp-nn
- https://arxiv.org/abs/1908.11263 (Garofalo et al. 2020)
- https://arxiv.org/abs/2007.07759 (Bruschi et al. 2020)
merge_draft_body -->

## [2026-07-02] merge_pending | ventana_veyron_v2.md
target_page: ventana_veyron_v2.md
canonical_name: Ventana Veyron V2
colliding_name: Ventana Veyron V2
source: https://www.nextplatform.com/compute/2023/11/07/ventana-launches-veyron-v2-risc-v-into-the-datacenter/1652320
status: pending_review
<!-- merge_draft_body
# Ventana Veyron V2

The Ventana Veyron V2 is a RISC-V server processor chip launched by Ventana Micro Systems in November 2023. It is the second generation of the Veyron chiplet-based server design, following the Veyron V1 which had been in development since 2022. The Veyron V2 is targeted at hyperscalers and cloud builders seeking greater control over their infrastructure by adopting an open-standard RISC-V architecture. A key feature of the V2 is the adoption of the Universal Chiplet Interconnect Express (UCI-Express) standard, replacing the earlier Bunch of Wires (BoW) interconnect used in the V1. Ventana made this shift in response to customer demand, as UCI-Express offers double the data rate, twice the power efficiency, less than half the latency, and 35–65% higher bandwidth per millimeter compared to BoW. The Veyron V2 also integrates the RISC-V Vector Extension 1.0 with 512-bit vector length, bringing advanced SIMD capabilities for datacenter workloads. The processor includes AMBA CHI coherent interface support, addressing a gap in the UCI-Express 1.0 standard. Ventana's co-founder and CEO Balaji Baktha stated that the company accelerated the V2 launch due to strong industry momentum behind UCI-Express, which also solves packaging costs and 3D memory stacking challenges.

## Key Claims

- Launched November 2023 as the second-generation Veyron server chip.
- Replaced BoW chiplet interconnect with UCI-Express 1.1, achieving 2× data rate, 2× power efficiency, and less than half the latency of BoW.
- Added support for RISC-V Vector Extension 1.0 with 512-bit vector length.
- Integrated AMBA CHI coherent interface on top of UCI-Express 2.0.
- Targeting hyperscalers and cloud builders who want to control their own hardware stacks.
- Backward compatible with Veyron V1 design and chiplet ecosystem.

## Relationships

- [[k230]]: Another RISC-V SoC with vector extension support, though aimed at AIoT rather than datacenter, providing a contrast in target market.
- [[xuantie_c908]]: A RISC-V core with RVV 1.0 support, but with configurable 128/256-bit vector length versus the Veyron V2's 512-bit vector length.

## Sources

- https://www.nextplatform.com/compute/2023/11/07/ventana-launches-veyron-v2-risc-v-into-the-datacenter/1652320
merge_draft_body -->

## [2026-07-02] merge_pending | xuantie_c906.md
target_page: xuantie_c906.md
canonical_name: XuanTie C906
colliding_name: XuanTie C906
source: https://www.riscvschool.com/2023/03/09/t-head-xuantie-c906-risc-v/
status: pending_review
<!-- merge_draft_body
# XuanTie C906

The XuanTie C906 is a RISC-V processor core developed by T-Head Semiconductor, designed for high energy efficiency and low cost in AIoT and embedded applications. It is based on the RV64GCV instruction set and includes customized arithmetic enhancement, bit manipulation, load store enhancement, and TLB/Cache operations enhancements. The core supports a configurable RISC-V V vector instruction extension with a vector register width of 128 bits, supporting element sizes of 8, 16, 32, and 64 bits, as well as half-precision floating-point (FP16) operations. It integrates a floating-point unit, a vector unit, and an AXI master interface with a Turbo Engine for efficient data movement. The C906 is positioned in T-Head's XuanTie processor family between the earlier C910 and the later C908, and it implements the RVV 0.7.1 vector extension (pre-ratified version). The core has been used as a reference target for early RISC-V vector software optimizations, such as the OpenBLAS library which includes hand-tuned kernels for the C906's vector units.

## Key Claims

- Based on the RV64GCV instruction set with customized arithmetic, bit manipulation, load store, and TLB/cache enhancement extensions.
- Supports configurable RISC-V V vector instruction extension (pre-ratification version RVV 0.7.1).
- Vector register width of 128 bits with element sizes 8/16/32/64 bits and half-precision support.
- Includes a floating-point unit, vector unit, and Turbo Engine with AXI master interface.
- Targets high energy efficiency and low cost, suitable for AIoT and embedded scenarios.
- Performance lies between the XuanTie C910 and C908 cores.
- OpenBLAS has been optimized for the C906's RVV 0.7.1 vector extensions, indicating software ecosystem support.

## Optimization-Relevant Details

- ISA/profile: RV64GCV (includes G, C, V extensions) with custom T-Head extensions.
- Vector/matrix/accelerator support: 128-bit vector unit supporting RVV 0.7.1, FP16, INT8/16/32/64 operations.
- Memory/cache/TLB/DMA: TLB/Cache operations enhancements, AXI master interface with Turbo Engine; specific cache sizes not publicly documented.
- Compiler/toolchain support: OpenBLAS optimized for RVV 0.7.1; GCC/LLVM toolchains with RVV 0.7.1 support.

## Relationships

- [[xuantie_c908]]: the next-generation XuanTie core after the C906, implementing RISC-V Vector Extension 1.0 and offering higher performance with instruction fusion and configurable VLEN.
- [[k230]]: a Canaan Kendryte SoC that integrates the XuanTie C908 core; the C906 is an earlier core in the same T-Head family, providing architectural lineage.
- [[llama_cpp]]: the LLM inference library supports RISC-V vector instructions (RVV), which can target the C906's RVV 0.7.1 unit for efficient inference on capable hardware.

## Sources

- https://www.riscvschool.com/2023/03/09/t-head-xuantie-c906-risc-v/
merge_draft_body -->

## [2026-07-02] merge_pending | xuantie_c906.md
target_page: xuantie_c906.md
canonical_name: XuanTie C906
colliding_name: XuanTie C906
source: https://riscv.org/blog/2022/06/xuantie-c906-tops-mlperf-tiny-v0-7-benchmark-mengchang-alibaba-cloud/
status: pending_review
<!-- merge_draft_body
# XuanTie C906

The XuanTie C906 is a 64-bit high-energy processor core developed by Alibaba Cloud (T-Head Semiconductor) based on the RISC-V instruction set architecture. It features a five to eight stage integer pipeline and implements the RISC-V Vector Extension version 0.7.1 with 128-bit vector operation units, supporting data formats including int8, int16, int32, int64, bf16, fp16, fp32, and fp64. The C906 incorporates multi-channel and mode data prefetching technologies to optimize data access bandwidth and prefetching efficiency. This core is used in the Allwinner D1 system-on-chip (SoC), which has entered full-scale production and is available in various development boards on the open market. A comprehensive software stack supports neural network deployment on the C906, including the CSI-NN2 acceleration library (assembly-optimized for the RISC-V Vector extension), the HHB deployment toolset based on Apache TVM, and the Sinian model compression platform.

## Key Claims

- Achieved top marks in the MLPerf Tiny v0.7 benchmark across all four core categories: Visual Wake Words (VWW), Image Classification (IC), Keyword Spotting (KWS), and Anomaly Detection (AD).
- Implements RISC-V Vector Extension V0.7.1 with 128-bit vector units, supporting a wide range of data formats (int8/16/32/64, bf16, fp16/32/64).
- Uses fp16 as the default data format for MLPerf Tiny benchmarks, achieving best performance.
- Integrated into the Allwinner D1 SoC, which is commercially available.
- CSI-NN2 provides assembly-level optimization for the RISC-V Vector extension and is open source on GitHub.
- HHB, based on Apache TVM, supports model formats from Caffe, TensorFlow, ONNX, and TensorFlow Lite, and generates C code with CSI-NN2 API calls.
- Sinian model compression platform reduced calculation workload by three to eight times for the benchmark models.

## Optimization-Relevant Details

- ISA/profile: 64-bit RISC-V with RVV 0.7.1 vector extension (supports V extension subset).
- Vector/matrix/accelerator support: 128-bit vector operation units; no dedicated matrix accelerator (relies on vector units for neural network ops).
- Memory/cache/TLB/DMA: Multi-channel data prefetching; specific cache sizes not disclosed in available sources.
- Compiler/toolchain support: CSI-NN2 library (assembly-optimized for RVV), HHB toolchain (TVM-based), Sinian compression tool; supports TensorFlow, Caffe, ONNX, TensorFlow Lite.

## Relationships

- The [[k230]] hardware target uses the newer XuanTie C908 core, a different design from the C906, and represents a later generation in the XuanTie family.
- The [[allwinner_v853]] is an SoC combining an Arm Cortex-A7 with a Xuantie E907 RISC-V core, representing a different approach to AI acceleration compared to the C906's vector-based compute.
- Insufficient context for additional cross-links.

## Sources

- https://riscv.org/blog/2022/06/xuantie-c906-tops-mlperf-tiny-v0-7-benchmark-mengchang-alibaba-cloud/
merge_draft_body -->

## [2026-07-02] pending | xuantie_c908.md
target_page: xuantie_c908.md
target_section: multiple
source: https://www.cnx-software.com/2022/11/04/t-head-xuantie-c908-risc-v-core-targets-aiot-applications/
status: pending_review
proposed_update: Add power consumption (52.8 mW/GHz per core on TSMC 12nm), performance numbers (24-64% improvement on synthetic benchmarks, 2-3.5x on AI workloads MLPerf Tiny v0.7 INT4), and architectural details: 9-stage dual-issue in-order pipeline, ePMP with up to 64 regions, PLIC configurable up to 1023 interrupt sources, RV32 COMPAT mode, AXI4/ACE bus with DCP and LLP. Incorporate these into the first paragraph (adding power and process context), Key Claims (add specific power and comparison numbers), and Optimization-Relevant Details (pipeline stage, ePMP, PLIC, bus interfaces).

## [2026-07-02] merge_pending | semidynamics_tensor_unit.md
target_page: semidynamics_tensor_unit.md
canonical_name: Semidynamics Tensor Unit
colliding_name: Semidynamics Tensor Unit
source: https://www.eetimes.com/semidynamics-releases-risc-v-tensor-unit-for-ai/
status: pending_review
<!-- merge_draft_body
# Semidynamics Tensor Unit

Semidynamics has announced a RISC-V Tensor Unit designed for ultra-fast AI solutions, based on its fully customizable 64-bit cores. The Tensor Unit provides hardware specifically tailored to matrix multiplication workloads, integrating with the company's Vector Unit and Gazzillion Misses technology to avoid data misses. It is used for layers requiring matrix multiplication such as fully connected and convolutional layers, while activation functions are delegated to the Vector Unit. The unit recently demonstrated over 70% utilization on the Llama2-7B model, as reported by Semidynamics.

## Key Claims

- Provides hardware specifically tailored to matrix multiplication workloads, accelerating fully connected and convolutional layers.
- Integrates with the company's 64-bit fully customizable RISC-V core and Vector Unit.
- Uses Gazzillion Misses technology to ensure continuous data supply with no misses.
- Reports tensor-unit utilization exceeding 70% while executing the Llama2-7B large language model.
- Delegates activation functions (ReLU, Sigmoid, Softmax) to the Vector Unit.

## Relationships

- [[xuantie_c908]]: another RISC-V AI accelerator core with a different microarchitectural approach; the Semidynamics Tensor Unit reuses vector registers for matrix storage, contrasting with the C908's instruction fusion.
- [[llama.cpp]]: LLM inference library that could target this tensor unit for efficient execution of models like Llama2-7B.

## Sources

- https://www.eetimes.com/semidynamics-releases-risc-v-tensor-unit-for-ai/
merge_draft_body -->

## [2026-07-02] merge_pending | semidynamics_tensor_unit.md
target_page: semidynamics_tensor_unit.md
canonical_name: Semidynamics Tensor Unit
colliding_name: Semidynamics Tensor Unit
source: https://www.eejournal.com/industry_news/semidynamics-launches-first-fully-coherent-risc-v-tensor-unit-to-supercharge-ai-applications/
status: pending_review
<!-- merge_draft_body
# Semidynamics Tensor Unit

The Semidynamics Tensor Unit is a hardware accelerator for matrix multiplication workloads, announced by Semidynamics in October 2023, designed to supercharge AI applications on RISC-V platforms. It is built on top of the Semidynamics RVV1.0 Vector Processing Unit and leverages the existing vector registers to store matrix data, avoiding the introduction of new architectural state. The Tensor Unit is integrated into the cache-coherent subsystem of the Atrevido-423 core, using the Gazzillion technology to fetch data from memory at the high rates required by tensor operations. This design allows the Tensor Unit to handle matrix multiplication for fully connected and convolutional layers while the Vector Unit handles activation functions, providing a combined solution that outperforms standalone NPUs on activation-layer processing. Semidynamics claims a performance increase of 128x compared to running the same AI software on the scalar core alone, and the unit operates seamlessly under any RISC-V vector-enabled Linux distribution without additional driver changes. The company is based in Barcelona, Spain, and focuses on high-bandwidth, high-performance RISC-V processor IP for machine learning and AI applications.

## Key Claims

- First fully-coherent RISC-V tensor unit announced (October 2023).
- Built on Semidynamics RVV1.0 Vector Processing Unit; reuses vector registers for matrix storage.
- Leverages Gazzillion technology for high-bandwidth data fetching to keep the tensor unit fed.
- Cache-coherent integration eliminates the need for difficult-to-program DMAs.
- 128x performance improvement over scalar-core-only execution for AI software.
- No new architecturally-visible state; works under any RISC-V vector-enabled Linux without changes.
- Optimized for matrix multiplication in LLMs (e.g., LLaMa-2, ChatGPT) and convolution layers.

## Optimization-Relevant Details

- ISA/profile: RISC-V Vector Extension 1.0 (RVV1.0).
- Vector/matrix/accelerator support: Tensor unit built on vector unit; uses vector registers for matrix data; matrix multiplication for fully-connected and convolution layers; activation functions handled by vector unit.
- Memory/cache/TLB/DMA: Cache-coherent subsystem integrated with Atrevido-423 core; Gazzillion technology for data fetching; no external DMA required.
- Compiler/toolchain support: Works with standard RISC-V vector-enabled Linux; no special compiler modifications required.

## Relationships

- [[xuantie_c908]]: Another RISC-V processor with RVV 1.0 support and AI acceleration focus; the XuanTie C908 page already links to this Semidynamics Tensor Unit as a comparison point for different microarchitectural choices (vector-register reuse vs. instruction fusion).
- [[k230]]: A SoC that integrates the XuanTie C908 core, demonstrating a different approach to AI acceleration via a dedicated KPU; the K230 can serve as a validation platform for comparing vector-based and fixed-function AI accelerators.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: A compiler pipeline for generating RVV micro-kernels; techniques from this recipe could potentially be adapted to target the Semidynamics Tensor Unit’s matrix multiplication capabilities.
- [[llama_cpp]]: An LLM inference library with explicit RVV support; the Tensor Unit’s claim of 128x speedup over scalar execution is directly relevant to running llama.cpp on Semidynamics hardware.

## Sources

- https://www.eejournal.com/industry_news/semidynamics-launches-first-fully-coherent-risc-v-tensor-unit-to-supercharge-ai-applications/
merge_draft_body -->

## [2026-07-02] merge_pending | semidynamics_tensor_unit.md
target_page: semidynamics_tensor_unit.md
canonical_name: Semidynamics Tensor Unit
colliding_name: Semidynamics All-In-One AI IP
source: https://www.electronicspecifier.com/products/artificial-intelligence/semidynamics-reveals-tensor-unit-efficiency-for-new-ai-ip/
status: pending_review
<!-- merge_draft_body
# Semidynamics All-In-One AI IP

Semidynamics All-In-One AI IP is a proprietary accelerator architecture developed by Semidynamics, a European RISC-V custom core AI specialist. The architecture integrates a RISC-V CPU core, a Tensor Unit for matrix multiplication (analogous to an NPU), and a Vector Unit for activation computations (analogous to a GPU) into a single scalable processing element. This unified design eliminates the need for DMA-intensive programming and separate software stacks typical of traditional CPU-GPU-NPU systems. The architecture uses a single ONNX-based software stack running on RISC-V and achieves zero-latency connectivity between the compute units by sharing vector registers. Semidynamics’ Gazzillion Misses technology enables efficient data movement by allowing a large number of in-flight cache misses for ahead-of-time data fetching. The company reported Tensor Unit utilization above 80% for most matrix multiplication shapes in LLaMA-2 7B (BF16) inference, with stable performance above 70% regardless of matrix size.

## Key Claims

- The architecture merges CPU, Tensor Unit, and Vector Unit into a single processing element with zero-latency data transfer via shared vector registers.
- The Tensor Unit handles all matrix multiplications (MatMul) in attention layers, while the Vector Unit handles Transpose and SoftMax activations.
- The system is DMA-free and uses a single software stack based on ONNX and RISC-V, reducing programming complexity and integration overhead.
- Gazzillion Misses technology enables high streaming data rates by supporting many in-flight cache misses for ahead-of-time data fetching.
- Tensor Unit utilization exceeds 80% for most MatMul shapes in LLaMA-2 7B (BF16), with the most challenging shapes (batch=1, first-token) still achieving over 80%.
- Performance remains stable above 70% regardless of total matrix size, even when matrices exceed cache/scratchpad capacity.

## Relationships

- [[tenstorrent_grayskull_e75]]: Another RISC-V AI accelerator with comparable benchmark data on MatMul efficiency.
- [[k230]]: A RISC-V AI accelerator targeting edge inference, relevant for architectural comparison.

## Sources

- https://www.electronicspecifier.com/products/artificial-intelligence/semidynamics-reveals-tensor-unit-efficiency-for-new-ai-ip/
merge_draft_body -->

## [2026-07-02] merge_pending | meta_mtia.md
target_page: meta_mtia.md
canonical_name: Meta MTIA
colliding_name: Meta MTIA
source: https://www.servethehome.com/meta-ai-acceleration-in-the-next-gen-meta-mtia-for-recommendation-inference-risc-v/
status: pending_review
<!-- merge_draft_body
# Meta MTIA

The Meta MTIA (Meta Training and Inference Accelerator) is a custom application-specific integrated circuit (ASIC) designed by Meta Platforms for recommendation inference workloads. The second-generation MTIA, announced at Hot Chips 2024, is built on TSMC's 5nm process with a 90W thermal design power (TDP). It features 128GB of LPDDR5 memory and 256MB of on-chip SRAM organized in an 8x8 compute grid. The accelerator uses a PCIe Gen5 x8 host interface and employs RISC-V cores for control and processing elements with scalar and vector units. The design includes a dot product engine (DPE), an integer dynamic quantization engine, hardware decompression engines for both data and weights, and a Table Branch Embedding (TBE) unit that improves runtime by 2-3x. The accelerator module integrates two MTIA chips per card with a total TDP of 220W, and the rack-scale system uses twelve modules per chassis, three chassis per rack, totaling 72 accelerators at approximately 16kW accelerator power.

## Key Claims

- Built on TSMC 5nm process with 90W TDP.
- Includes 128GB LPDDR5 memory and 256MB on-chip SRAM.
- Uses PCIe Gen5 x8 host interface.
- RISC-V cores for control and processing elements (scalar and vector).
- Features dot product engine (DPE) and integer dynamic quantization engine.
- Hardware decompression engine for data and weight decompression.
- Table Branch Embedding (TBE) improves runtime by 2-3x.
- Dual-chip module with 220W TDP.
- Rack configuration: 12 modules per chassis, 3 chassis per rack, 72 accelerators, ~16kW accelerator power.
- Model performance claims on internal workloads (baseline unspecified).

## Optimization-Relevant Details

- ISA/profile: RISC-V (control and PE cores), no specific profile disclosed.
- Vector/matrix/accelerator support: Dot product engine, integer dynamic quantization engine, hardware decompression engine, Table Branch Embedding.
- Memory/cache/TLB/DMA: 128GB LPDDR5, 256MB on-chip SRAM, PCIe Gen5 x8 host interface.
- Compiler/toolchain support: Not specified; likely Meta's internal software stack.

## Relationships

- [[xuantie_c908]]: Another RISC-V-based AI accelerator core, though targeting embedded AIoT rather than datacenter recommendation inference.
- [[k230]]: A RISC-V system-on-chip with dedicated AI acceleration (KPU), representing a different design point in the RISC-V AI accelerator space.

## Sources

- https://www.servethehome.com/meta-ai-acceleration-in-the-next-gen-meta-mtia-for-recommendation-inference-risc-v/
merge_draft_body -->

## [2026-07-02] merge_pending | meta_mtia.md
target_page: meta_mtia.md
canonical_name: Meta MTIA
colliding_name: Meta MTIA
source: https://www.abhs.in/blog/meta-mtia-chip-roadmap-four-generations-inference-2026
status: pending_review
<!-- merge_draft_body
# Meta MTIA

Meta MTIA (Meta Training and Inference Accelerator) is a family of custom application-specific integrated circuits (ASICs) designed by Meta Platforms for accelerating AI inference workloads in its data centers. The MTIA roadmap, announced in March 2026, comprises four generations—MTIA 300, MTIA 400, MTIA 450, and MTIA 500—developed within a two-year cycle. These chips are built on the open-source RISC-V instruction set architecture, fabricated by TSMC, and co-designed with Broadcom. They are optimized for generative AI inference at scale, with each generation delivering significant compute and memory bandwidth improvements. The roadmap reflects a strategy of rapid silicon iteration to keep pace with evolving AI models, countering the traditional multi-year ASIC development timeline.

## Key Claims

- Meta unveiled four MTIA chip generations (300, 400, 450, 500) in March 2026, all within a two-year development window.
- MTIA 400 delivers over 5x the compute performance and 50% more HBM bandwidth than MTIA 300, with 400% higher FP8 FLOPS.
- Compute scaling from MTIA 300 to MTIA 500 is 25x.
- Chips are based on RISC-V architecture and fabricated by TSMC.
- The roadmap delivers a new chip generation every six months through 2027.

## Optimization-Relevant Details

- ISA/profile: RISC-V (specific profile not disclosed in source).
- Vector/matrix/accelerator support: Inference acceleration units (exact microarchitecture not detailed).
- Memory/cache/TLB/DMA: HBM memory (explicitly mentioned for MTIA 400).
- Compiler/toolchain support: Not specified in source.

## Relationships

- [[xuantie_c908]]: A RISC-V processor core for AIoT applications, representing a different market segment from Meta's data center inference accelerators.
- [[k230]]: A RISC-V SoC with dedicated AI acceleration (KPU), illustrating a contrasting approach to on-chip AI acceleration versus MTIA's data-center-scale design.
- [[llama_cpp]]: An LLM inference runtime that could potentially target MTIA hardware if appropriate toolchain support is developed.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: A RISC-V vector code generation recipe that represents the open-source approach to optimizing inference kernels, contrasting with Meta's proprietary compilation stack.

## Sources

- https://www.abhs.in/blog/meta-mtia-chip-roadmap-four-generations-inference-2026
merge_draft_body -->

## [2026-07-02] merge_pending | xuantie_c906.md
target_page: xuantie_c906.md
canonical_name: XuanTie C906
colliding_name: XuanTie C906
source: https://riscv.org/blog/xuantie-c906-tops-mlperf-tiny-v0-7-benchmark-mengchang-alibaba-cloud/
status: pending_review
<!-- merge_draft_body
# XuanTie C906

XuanTie C906 is a 64-bit high-performance RISC-V processor developed by Alibaba's T-Head division (Cloud). It implements the RISC-V Vector Extension version 0.7.1 with 128-bit vector operation units. The processor features a five- to eight-stage integer pipeline and employs multi-channel and mode data prefetching technologies to optimize data access bandwidth. The C906 silicon chip is deployed in the Allwinner D1 SoC, which powers various development boards available in the open market. The processor achieved top marks across all four categories of the MLPerf Tiny v0.7 benchmark for IoT AI workloads: Visual Wake Words (VWW), Image Classification (IC), Keyword Spotting (KWS), and Anomaly Detection (AD). A software stack consisting of CSI-NN2, HHB, and Sinian was used to deploy and optimize neural network models on the C906.

## Key Claims

- Implements RISC-V Vector Extension V0.7.1 with 128-bit vector units, supporting data formats int8, int16, int32, int64, bf16, fp16, fp32, and fp64. The best benchmark performance was achieved using fp16.
- Achieved top marks in MLPerf Tiny v0.7 across all four tasks (VWW, IC, KWS, AD), demonstrating competitive AI inference performance for IoT-class devices.
- The C906 silicon is mass-produced in the Allwinner D1 SoC and is available on development boards in the open market.
- The neural network software stack includes CSI-NN2 (assembly-level RVV-optimized acceleration library, open source on GitHub), HHB (deployment toolchain based on Apache TVM, open source on GitHub, supporting Caffe, TensorFlow, ONNX, and TensorFlow Lite model formats), and Sinian (model compression platform using network structure search and knowledge distillation, achieving 3–8× computation reduction).

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit with Vector Extension V0.7.1.
- Vector/matrix/accelerator support: 128-bit vector operation units.
- Memory/cache/TLB/DMA: Multi-channel and mode data prefetching technologies; no specific cache sizes documented in the source.
- Compiler/toolchain support: CSI-NN2 acceleration library with RVV assembly optimization; HHB deployment tools based on Apache TVM; Sinian for model compression; model formats: Caffe, TensorFlow, ONNX, TensorFlow Lite.

## Relationships

- [[k230]] is a later XuanTie-family processor (C908 cores) integrating the RISC-V Vector Extension 1.0 and a dedicated KPU, representing a higher-performance AIoT design.
- [[allwinner_v853]] is another Allwinner SoC that includes a Xuantie E907 RISC-V core alongside an Arm Cortex-A7 and a 1 TOPS NPU, targeting similar AI vision applications.

## Sources

- https://riscv.org/blog/xuantie-c906-tops-mlperf-tiny-v0-7-benchmark-mengchang-alibaba-cloud/
merge_draft_body -->

## [2026-07-02] merge_pending | xuantie-c910.md
target_page: xuantie-c910.md
canonical_name: XuanTie C910
colliding_name: XuanTie C910
source: https://chipsandcheese.com/p/alibabat-heads-xuantie-c910
status: pending_review
<!-- merge_draft_body
# XuanTie C910

The XuanTie C910 is an out-of-order RISC-V processor core developed by T-HEAD Semiconductor (Alibaba Group). It is T-HEAD’s first out-of-order implementation and is designed to be clustered in groups of up to four cores sharing a unified L2 cache. The core is fabricated on TSMC’s 12nm FinFET process with a target frequency range of 2.0 to 2.5 GHz, and each core occupies approximately 0.8 mm² silicon area. The memory subsystem includes a configurable 32KB/64KB Harvard L1 cache but lacks a mid-level cache, making the cluster’s shared L2 cache a performance bottleneck. The Core Interconnect Unit (CIU) provides inter-core communication with latency significantly lower than the SiFive P550’s quad-cluster latency of over 300 ns. This core represents T-HEAD’s entry into high-performance RISC-V computing, preceding later designs like the C908 and C950.

## Key Claims

- First out-of-order RISC-V core from T-HEAD.
- Targets 2.0–2.5 GHz on TSMC’s 12nm FinFET process.
- Core area 0.8 mm².
- Clusters up to four cores with a shared L2 cache.
- CIU inter-core latency better than SiFive P550 (which had >300 ns within a quad-core cluster).
- Cache subsystem described as exceptionally weak: shared L2 is small and slow, with no mid-level cache to insulate L1 misses.

## Optimization-Relevant Details

- ISA/profile: RISC-V out-of-order (implied RV64GC).
- Vector/matrix/accelerator support: Not specified; standard RISC-V base ISA.
- Memory/cache/TLB/DMA: L1 I-cache and D-cache (32KB/64KB configurable), shared L2 per cluster (small and slow), no mid-level cache.
- Compiler/toolchain support: Not specified.

## Relationships

- [[xuantie_c908]]: A later-generation XuanTie core with configurable vector extension support and instruction fusion, representing a different microarchitecture (in-order vector processor) compared to the C910’s out-of-order scalar design.
- [[k230]]: A Kendryte SoC integrating a pair of C908 cores, illustrating the evolution of T-HEAD’s core IP from the C910 to the C908 in AIoT applications.

## Sources

- https://chipsandcheese.com/p/alibabat-heads-xuantie-c910
merge_draft_body -->

## [2026-07-02] merge_pending | xuantie_c950.md
target_page: xuantie_c950.md
canonical_name: XuanTie C950
colliding_name: XuanTie C950
source: https://www.eetimes.com/alibaba-launches-xuantie-c950-cpu-for-agentic-ai/
status: pending_review
<!-- merge_draft_body
# XuanTie C950

The XuanTie C950 is a 64-bit multi-core RISC-V CPU developed by Alibaba's DAMO Academy, designed specifically for agentic AI workloads. Unveiled in March 2026, it is fabricated on a 5-nanometer process and leverages the open-standard RISC-V instruction set architecture to offer an alternative to proprietary Western architectures such as x86 and ARM. As the latest generation in the XuanTie family of processor cores, it targets server-class AI inference and autonomous agent applications, building on the foundation established by previous XuanTie cores like the C930 and C908. The processor aims to challenge proprietary architectures with open-source competition, and reflects Alibaba's investment in RISC-V as a strategic platform for AI acceleration.

## Key Claims

- 64-bit multi-core RISC-V CPU for agentic AI workloads.
- Fabricated on 5nm process.
- Designed to challenge proprietary Western architectures with open-source competition.
- Developed by Alibaba's DAMO Academy (Academy for Discovery, Adventure, Momentum and Outlook).
- Targets server-class AI workloads including autonomous agent systems.

## Optimization-Relevant Details

- ISA/profile: RISC-V (specific profile not disclosed).
- Vector/matrix/accelerator support: Not detailed in public sources.
- Memory/cache/TLB/DMA: Not disclosed.
- Compiler/toolchain support: Not specified.

## Relationships

- [[xuantie_c908]]: earlier generation XuanTie core targeting AIoT, with detailed vector extension information and software ecosystem documentation.
- [[llama_cpp]]: a high-performance LLM inference library that can potentially run on the C950 given its RISC-V support and RVV extensions.
- [[xuantie_c930]]: server-class XuanTie core also targeting AI/HPC workloads, a predecessor in the same market segment.

## Sources

- https://www.eetimes.com/alibaba-launches-xuantie-c950-cpu-for-agentic-ai/
- https://www.cnbc.com/2026/03/24/alibaba-reveals-new-ai-cpu-chip-designed-for-agents.html (CNBC)
- https://www.reuters.com/technology/alibaba-unveils-next-gen-chip-agentic-ai-company-says-2026-03-24/ (Reuters)
merge_draft_body -->

## [2026-07-02] merge_pending | xuantie_c908.md
target_page: xuantie_c908.md
canonical_name: XuanTie C908
colliding_name: XuanTie C908
source: https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
status: pending_review
<!-- merge_draft_body
# XuanTie C908

The XuanTie C908 is a RISC-V processor core developed by T-Head Semiconductor (Alibaba Group) designed for AI-focused edge and Internet-of-Things applications. It operates at up to 2 GHz and complies with the RISC-V Vector Extension 1.0, supporting configurable vector register bit widths of 128 or 256 bits. The vector execution unit handles FP16, BFP16, FP32, INT8, INT32, and INT64 operations, with additional INT8 and INT4 vector dot product instructions for neural network acceleration. The processor implements instruction fusion technology to improve pipeline efficiency. Software support includes the Structure of Heterogeneous Library (SHL), a set of neural network library APIs providing optimized implementations for convolution, pooling, activation, and other operators, and the Heterogeneous Honey Badger (HHB) deployment tool for quantization and code generation. The C908 succeeds the XuanTie C906, offering significant AI inference performance improvements through both architectural enhancements and software-hardware co-optimization.

## Key Claims

- Operates at up to 2 GHz and is compliant with RISC-V Vector Extension 1.0.
- Supports configurable vector register widths of 128 and 256 bits.
- Vector execution unit handles FP16, BFP16, FP32, INT8, INT32, INT64, and supports INT8 and INT4 vector dot product instructions.
- Implements instruction fusion technology to reduce instruction overhead.
- SHL provides optimized implementations for key neural network operators including conv2d, depthwise conv2d, pooling, activation, and fully connected layers.
- HHB tool supports int8 asymmetric and fp16 quantization and generates C code for inference deployment.
- Compared to the previous generation XuanTie C906, the C908 achieves 3.75–4.57× AI inference performance improvement.

## Optimization-Relevant Details

- ISA/profile: RV64GCV (RISC-V Vector Extension 1.0)
- Vector/matrix/accelerator support: 128/256-bit configurable vector registers, vector dot product INT8/INT4, instruction fusion
- Memory/cache/TLB/DMA: Not detailed in available source.
- Compiler/toolchain support: SHL (Structure of Heterogeneous Library), HHB (Heterogeneous Honey Badger)

## Relationships

- The C908 is the target processor for dedicated optimization recipes such as [[xuantie_c908_shl_convolution_acceleration]] and micro-kernel implementations like [[xuantie_c908_fp16_gemm_kernel]].
- The MLIR+xDSL code generation pipeline [[mlir_xdsl_rvv_gemm_codegen_recipe]] targets similar RISC-V vector hardware and provides a complementary software optimization approach.
- The predecessor core [[xuantie_c906]] is compared in performance benchmarks.

## Sources

- https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
merge_draft_body -->

## [2026-07-02] merge_pending | xuantie-c910.md
target_page: xuantie-c910.md
canonical_name: XuanTie C910
colliding_name: XuanTie C910
source: https://arxiv.org/abs/2505.24363
status: pending_review
<!-- merge_draft_body
# XuanTie C910

The XuanTie C910 is an out-of-order superscalar RISC-V processor core developed by T-Head Semiconductor, originally designed with proprietary interfaces and protocols including non-standard AXI extensions, interrupts, and debug support. In the work by Fu et al. (2025), the C910 was modified to achieve full RISC-V standard compliance in its debug, interrupt, and memory interfaces, and integrated into the Cheshire open-source SoC platform implemented in GF22FDX 22nm technology. The core's superscalar out-of-order microarchitecture delivers a 119.5% IPC improvement over the single-issue in-order CVA6 core at the cost of a 75% area increase, and demonstrates competitive energy efficiency (GOPS/W) compared to in-order cores. This challenges the assumption that high performance in superscalar and out-of-order designs inherently incurs significant area and energy efficiency penalties.

## Key Claims

- Originally used proprietary interfaces; modified to full RISC-V standard compliance for debug, interrupt, and memory interfaces.
- Integrated into the Cheshire open-source SoC platform in GF22FDX 22nm technology.
- Achieves 119.5% IPC improvement over the single-issue in-order CVA6 core with a 75% area increase.
- Shows competitive energy efficiency (GOPS/W) relative to in-order cores, contradicting the common belief that OoO superscalar designs are inherently less energy efficient.
- Area efficiency (GOPS/mm²) is lower than that of CVA6S+ (dual-issue in-order) but the core is competitive on energy efficiency.

## Optimization-Relevant Details

- ISA/profile: RISC-V, superscalar out-of-order, with modifications to achieve standard compliance.
- Vector/matrix/accelerator support: Not specified in available resource.
- Memory/cache/TLB/DMA: Not specified; relies on Cheshire SoC platform.
- Compiler/toolchain support: Not specified; uses industrial EDA tool flow for 22nm synthesis.

## Relationships

- [[xuantie_c908]]: sibling core from the same XuanTie family, targeting AIoT with vector extensions, while the C910 targets higher-performance OoO execution.
- [[xuantie_c906]]: earlier-generation in-order XuanTie core; the C910 represents a significant microarchitectural step forward.
- [[k230]]: SoC integrating a different XuanTie core (C908), whereas the C910 was integrated into Cheshire SoC.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: an optimization recipe for RVV code generation on other RISC-V hardware; the C910's OoO design would interact differently with such compiler passes.
- insufficient context for additional cross-links

## Sources

- https://arxiv.org/abs/2505.24363
merge_draft_body -->

## [2026-07-02] merge_pending | xiangshan.md
target_page: xiangshan.md
canonical_name: XiangShan
colliding_name: XiangShan
source: https://openxiangshan.github.io/
status: pending_review
<!-- merge_draft_body
# XiangShan

XiangShan is an open-source, industry-competitive, high performance RISC-V processor launched by a research group to raise the performance ceiling of publicly accessible processors and set a competitive groundwork for architecture research. The project, started in June 2020, has developed two major generations codenamed YQH and NH. The latest version achieves the highest performance of open-source RISC-V processors. XiangShan is a superscalar out-of-order processor implementing the RV64GCBK ISA. Its micro-architecture includes a high-throughput frontend with an advanced branch predictor, a six-width aggressive out-of-order execution engine, a high-bandwidth load/store unit, and a highly configurable cache system. The design is written in Chisel, a high-level hardware description language, to maintain readability and maintainability. The project also provides a development infrastructure platform called Minjie, which integrates tools for functional verification and performance evaluation.

## Key Claims

- Open-source RISC-V processor designed for industry-competitive performance.
- Two major generations: YQH and NH.
- Superscalar out-of-order micro-architecture with RV64GCBK ISA support.
- High-throughput frontend with advanced branch predictor.
- Six-width aggressive out-of-order execution engine.
- High-bandwidth load/store unit and highly configurable cache system.
- Written in Chisel for high readability and maintainability.
- Tape-out status and published performance evaluation (specific figures not disclosed in source).
- Includes the Minjie development infrastructure platform with tools for verification and evaluation.

## Relationships

- [[xuantie_c908]]: a commercial open-source RISC-V core from T-Head Semiconductor, offering a different design point in the open-source RISC-V ecosystem.
- [[k230]]: a RISC-V SoC that integrates a C908 core, representing a complete platform contrasting with the XiangShan processor's focus on high-performance core design.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: a compilation pipeline for RISC-V Vector extensions, relevant for optimizing code on RISC-V processors like XiangShan if vector support is added.

## Sources

- XiangShan project tutorial overview (ASPLOS 2023): https://openxiangshan.github.io/
- Tutorial slides and updates: https://xiangshan-doc.readthedocs.io/zh_CN/latest/tutorials/asplos23/
merge_draft_body -->

## [2026-07-02] merge_pending | riscv_vector_extension.md
target_page: riscv_vector_extension.md
canonical_name: RISC-V Vector Extension (RVV)
colliding_name: RISC-V
source: https://en.wikipedia.org/wiki/RISC-V
status: pending_review
<!-- merge_draft_body
# RISC-V

RISC-V (pronounced "risk-five") is a free and open standard instruction set architecture (ISA) based on reduced instruction set computer (RISC) principles. It was originally developed in 2010 at the University of California, Berkeley as the fifth generation of RISC processors from the university, under the direction of Krste Asanović and David Patterson. Unlike proprietary ISAs such as x86 and ARM, the RISC-V specification is released under permissive open-source licenses, allowing implementations without royalty payments. The standard supports 32, 64, and 128-bit address spaces, includes mandatory base integer instructions (RV32I, RV64I, RV128I) and a modular set of optional extensions for multiplication, atomics, floating-point, vector processing, bit manipulation, and compressed instructions. In 2015, stewardship was transferred to the non-profit RISC-V International, which now counts over 4,500 members. RISC-V has become a popular architecture for microcontrollers, embedded systems, and increasingly for mobile, desktop, and server markets, with commercial chips from SiFive, Andes Technology, Alibaba, StarFive, Espressif, and Raspberry Pi. Its vector extension (RVV) is particularly relevant for AI accelerator workloads, as it provides a standardised, scalable SIMD vector processing model that can be implemented across a wide range of hardware targets.

## Key Claims

- RISC-V is a free and open ISA, not a specific processor implementation.
- Developed at UC Berkeley in 2010 as the fifth generation of Berkeley RISC research.
- The ISA specification is published under permissive open-source licenses (BSD for CPU designs, Creative Commons Attribution 4.0 for technical reports).
- RISC-V International, founded in 2015, maintains the standard and has over 4,500 members as of 2025.
- The base ISA comes in 32-bit, 64-bit, and 128-bit variants, with a fixed set of base integer instructions (RV32I, RV64I, RV128I).
- Optional extensions include: M (multiply/divide), A (atomics), F/D/Q (floating-point), C (compressed instructions), B (bit manipulation), V (vector operations), Zicsr (control/status registers), Zifencei (load/store fence), and J (interpreted/JIT language support).
- The ISA is variable-length encoding with a load-store design, little-endian, and 4 KiB page size by default.
- Major Linux distributions support RISC-V; commercial SoCs are available from SiFive, Andes Technology, Alibaba (DAMO Academy), StarFive, Espressif, Raspberry Pi, SpacemiT, and others.
- The vector extension (RVV 1.0) defines 32 vector registers, software-configurable vector length, and length-agnostic programming, enabling efficient AI and data-parallel workloads.

## Relationships

- The [[sifive_performance_p570_gen3]] is a commercial RISC-V processor core compliant with the RVA23 profile, implementing the RVV 1.0 vector extension with a 128-bit vector pipeline.
- The [[coral_npu_vector_execution_engine]] implements the Zve32x subset of RVV 1.0, using a separate SIMD instruction queue and decode unit for edge AI inference.
- RISC-V's vector extension (RVV) is a key enabler for optimization recipes like [[mlir_xdsl_rvv_gemm_codegen_recipe]], which targets RVV intrinsics for GEMM kernels.
- The [[llvm_riscv_target]] provides LLVM backend support for RISC-V, including the vector extension, essential for compiling code for RVV hardware targets.
- Insufficient context for additional cross-links.

## Sources

- https://en.wikipedia.org/wiki/RISC-V
merge_draft_body -->

## [2026-07-02] merge_pending | xiangshan.md
target_page: xiangshan.md
canonical_name: XiangShan
colliding_name: XiangShan
source: https://www.servethehome.com/xiangshan-high-performance-risc-v-processors-at-hot-chips-2024/
status: pending_review
<!-- merge_draft_body
# XiangShan

XiangShan is an open-source high-performance RISC-V CPU project developed by Chinese universities and hosted on GitHub. The project targets server-class and high-performance computing applications, with two microarchitectures: Kunminghu, aimed at competing with the Arm Neoverse N2, and Nanhu, targeting the Arm Cortex A76. The design features a 13-stage pipeline with 6-wide decode, rename, and dispatch, a 4-ALU integer execution block, and dedicated floating-point and vector units. The memory hierarchy includes private L2 caches of up to 1 MB per core and a shared L3 cache of 16 MB. The project also provides an agile development toolchain called Minjie, along with verification tools like difftest and LightSSS for RTL error detection and debug reproduction. XiangShan includes support for RISC-V vector and hypervisor extensions, and the roadmap aims for a tapeout every year with two teams working in parallel.

## Key Claims

- Kunminghu microarchitecture targets Arm Neoverse N2 performance; Nanhu targets Arm Cortex A76.
- 13-stage out-of-order pipeline with 6-wide frontend (decode, rename, dispatch) and backend.
- 4 ALU integer execution block; floating-point and vector blocks present.
- Private L2 cache up to 1 MB per core; shared L3 cache 16 MB.
- Supports RISC-V vector and hypervisor extensions (exact version unspecified).
- Agile development toolchain: Minjie; verification tools: difftest (RTL error detection), LightSSS (debug reproduction).
- Collaborations include a server CPU, a 5 nm AI acceleration chip, and a 7 nm DPU.
- Aims for yearly tapeouts through two parallel teams.

## Optimization-Relevant Details

- ISA/profile: RISC-V with vector and hypervisor extensions (exact profile not disclosed).
- Vector/matrix/accelerator support: Vector units present; no specific matrix or AI accelerator mentioned for the core, though chip-level collaborations include AI and DPU accelerators.
- Memory/cache/TLB/DMA: Private L2 up to 1 MB per core; shared L3 16 MB; no specific L1, TLB, or DMA details provided.
- Compiler/toolchain support: Minjie agile development toolchain; difftest for RTL verification; LightSSS for simulation debug.

## Relationships

- [[xuantie_c908]]: Another high-performance RISC-V core design, but targeting embedded AI rather than server-class; both demonstrate the diversity of RISC-V high-performance implementations.
- [[k230]]: An SoC integrating a RISC-V core (C908) with AI accelerators, contrasting with XiangShan's general-purpose high-performance approach aimed at server and compute markets.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: A code generation recipe for RISC-V Vector, relevant to software tooling that could be applied to XiangShan's vector units.

## Sources

- https://www.servethehome.com/xiangshan-high-performance-risc-v-processors-at-hot-chips-2024/
merge_draft_body -->

## [2026-07-02] merge_pending | xiangshan.md
target_page: xiangshan.md
canonical_name: XiangShan
colliding_name: XiangShan
source: https://github.com/SigmaOfTy/XiangShan_ty
status: pending_review
<!-- merge_draft_body
# XiangShan

XiangShan (Chinese: 香山) is an open-source, high-performance RISC-V processor project developed by the Institute of Computing Technology (ICT) at the Chinese Academy of Sciences (CAS). It employs agile hardware development methodology and has produced three microarchitecture generations: Yanqihu (first stable, June 2020), Nanhu (second stable), and Kunminghu (currently under development on the master branch). The project provides comprehensive documentation at docs.xiangshan.cc, a design document for Kunminghu V2R2, and a user guide. XiangShan's research contributions include a MICRO 2022 paper on agile RISC-V processor development, which received all three artifact evaluation badges (Available, Functional, Reproduced). The repository includes design files in Scala/Chisel, simulation infrastructure via Verilator and XSPdb, a difftest co-simulation framework, and scripts for agile development workflows. Submodules such as NEMU (a RISC-V ISA simulator), nexus-am (abstract machine), huancun (cache subsystem), and yunsuan (custom functional units) support the verification and extension of the processor design.

## Key Claims

- XiangShan is an open-source high-performance RISC-V processor project from ICT, CAS.
- Three microarchitecture generations: Yanqihu (stable since June 2020), Nanhu, and Kunminghu (active development on master branch).
- Agile hardware development methodology is used, including custom tools for design, verification, debugging, and performance validation.
- MICRO 2022 paper "Towards Developing High Performance RISC-V Processors Using Agile Methodology" received all three artifact evaluation badges.
- Documentation is publicly available under CC-BY-4.0 license.
- Design files are written in Scala/Chisel and compile to Verilog via Chisel.
- Supports simulation with Verilator (C++ emulator) and prebuilt simulation binaries.
- Integration with NEMU ISA simulator, difftest framework, and nexus-am for functional verification.

## Relationships

- [[xuantie_c908]]: Another open-source RISC-V processor core, though targeting AIoT rather than the high-performance general-purpose compute focus of XiangShan.
- [[k230]]: An SoC integrating RISC-V C908 cores, demonstrating the broader RISC-V hardware ecosystem to which XiangShan belongs.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: A compiler pipeline for generating RVV intrinsics-based code, applicable to RISC-V vector processors like XiangShan for runtime performance optimization.

## Sources

- https://github.com/SigmaOfTy/XiangShan_ty
- https://docs.xiangshan.cc
- https://talks-pubs.xiangshan.cc/publications/micro2022-xiangshan.pdf
merge_draft_body -->

## [2026-07-02] merge_pending | tenstorrent_grayskull_e75.md
target_page: tenstorrent_grayskull_e75.md
canonical_name: Tenstorrent Grayskull e75
colliding_name: Tenstorrent Grayskull e75
source: https://arxiv.org/html/2505.06085
status: pending_review
<!-- merge_draft_body
# Tenstorrent Grayskull e75

The Tenstorrent Grayskull e75 is a RISC-V-based AI accelerator card featuring a grid of 96 Tensix cores fabricated on a 12nm process. It operates at 1 GHz, provides 8 GB of LPDDR4 memory with 102.4 GB/s bandwidth, and delivers a peak performance of 55 TFLOPs for FP16. Each Tensix core contains five programmable baby RISC-V cores, a 1 MB local SRAM, a SIMD Matrix & Vector engine, and Network on Chip routers. The accelerator supports multiple data formats including BF16 and Block Floating Point (BFP) with configurable math fidelity levels. It is designed for AI workloads such as LLM inference and matrix multiplication.

## Key Claims

- 96 Tensix cores at 1 GHz on a 12nm process.
- 8 GB LPDDR4 memory with 102.4 GB/s bandwidth.
- 55 TFLOPs FP16 peak raw throughput.
- Each Tensix core: 5 programmable RISC-V cores, 1 MB SRAM, SIMD Matrix & Vector engine, NoC routers.
- Data format support: BF16, BFP4/8/16, standard FP; four Math Fidelity levels.
- Peak energy efficiency of 1.55 TFLOPs/Watt when executing MatMul with BF16.

## Optimization-Relevant Details

- ISA/profile: Proprietary RISC-V baby cores within Tensix architecture; not a standard ISA extension.
- Vector/matrix/accelerator support: SIMD Matrix & Vector engine per Tensix core; block floating point formats for reduced precision.
- Memory/cache/TLB/DMA: 1 MB local SRAM (L1) per core; 8 GB LPDDR4 external; NoC for inter-core communication.
- Compiler/toolchain support: TTNN (Python library built on TT-Metal), C++ kernel level programming.

## Relationships

- [[grayskull_e75_matmul_benchmark]]: benchmark results on the same hardware, reporting MatMul efficiency and comparison with NVIDIA GPUs.
- [[k230]]: another RISC-V-based AI accelerator (Canaan Kendryte), representing an alternative approach with a KPU and dual RISC-V C908 cores.
- [[allwinner_v853]]: a comparable SoC with a RISC-V MCU and NPU, targeted at similar AI vision workloads.

## Sources

- https://arxiv.org/html/2505.06085
merge_draft_body -->

## [2026-07-02] merge_pending | tenstorrent_grayskull_e75.md
target_page: tenstorrent_grayskull_e75.md
canonical_name: Tenstorrent Grayskull e75
colliding_name: Tenstorrent Grayskull
source: https://www.techradar.com/pro/firm-headed-by-legendary-chip-architect-behind-amd-zen-finally-releases-first-hardware-days-after-being-selected-to-build-the-future-of-ai-in-japan-tenstorrent-unveils-grayskull-its-risc-v-answer-to-gpus
status: pending_review
<!-- merge_draft_body
# Tenstorrent Grayskull

Tenstorrent Grayskull is a RISC-V-based AI accelerator architecture developed by Tenstorrent, a company founded by legendary chip architect Jim Keller. The Grayskull processor is designed as an alternative to traditional GPUs for AI inference, with a focus on ease of programming, scalability, and efficient handling of run-time sparsity and conditional computation. The first hardware products based on Grayskull are the Grayskull e75 and Grayskull e150 DevKits, which are inference-only PCIe Gen4 boards targeted at AI development. The architecture is built around Tensix cores, which include integrated network communication hardware that enables direct core-to-core data transfer without routing through DRAM, reducing latency and improving throughput. Tenstorrent provides two software stacks: TT-Buda for running pre-trained models out-of-the-box, and TT-Metalium for users who need to customize models or develop new ones. The DevKits support a range of popular AI models including BERT, ResNet, Whisper, YOLOv5, and U-Net. The e75 operates at 75W and has a low-profile half-length form factor, while the e150 operates at up to 200W in a standard-height 3/4-length form factor. The e75 is priced at $599 and the e150 at $799.

## Key Claims

- Tenstorrent Grayskull is a RISC-V-based AI accelerator architecture for inference, designed to be easier to program than GPUs and efficient at handling sparsity and conditional computation.
- The Grayskull e75 DevKit is a half-length, low-profile PCIe Gen4 board with a single Grayskull processor, operating at 75W and priced at $599.
- The Grayskull e150 DevKit is a standard-height, 3/4-length PCIe Gen4 board with a single Grayskull processor, operating at up to 200W and priced at $799.
- The architecture uses Tensix cores that communicate directly via an integrated network, bypassing DRAM for lower latency.
- Software support includes TT-Buda (out-of-box model execution) and TT-Metalium (custom model development).
- Supported models include BERT, ResNet, Whisper, YOLOv5, and U-Net.
- Tenstorrent also assists in planning to build a 2nm AI Accelerator for Japan's LSTC using RISC-V and Chiplet IP.
- The DevKits are available for purchase as of the announcement date.

## Optimization-Relevant Details

- ISA/profile: RISC-V based (proprietary Tensix cores; exact ISA extensions not publicly detailed).
- Vector/matrix/accelerator support: Tensix cores with network-on-chip; no standard vector extension confirmed, but custom support for sparsity and conditional computation.
- Memory/cache/TLB/DMA: Not disclosed in available sources.
- Compiler/toolchain support: TT-Buda (high-level model execution), TT-Metalium (low-level customization).

## Relationships

- [[xuantie_c908]]: Another RISC-V AI accelerator core, though focused on embedded AIoT with standard RISC-V Vector extensions, representing a different design philosophy from Grayskull's Tensix network architecture.
- [[k230]]: A RISC-V AIoT SoC integrating C908 cores with a dedicated KPU, contrasting with Grayskull's homogeneous Tensix-core approach.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: A research recipe for generating RVV-optimized GEMM kernels; if Grayskull supports standard RISC-V vector extensions, this recipe could be adapted for optimization, but this is not confirmed.

## Sources

- https://www.techradar.com/pro/firm-headed-by-legendary-chip-architect-behind-amd-zen-finally-releases-first-hardware-days-after-being-selected-to-build-the-future-of-ai-in-japan-tenstorrent-unveils-grayskull-its-risc-v-answer-to-gpus
merge_draft_body -->

## [2026-07-02] merge_pending | tenstorrent_grayskull_e75.md
target_page: tenstorrent_grayskull_e75.md
canonical_name: Tenstorrent Grayskull e75
colliding_name: Tenstorrent Grayskull
source: https://gigazine.net/gsc_news/en/20240311-jim-keller-tenstorrent-grayskull-e75-e150/
status: pending_review
<!-- merge_draft_body
# Tenstorrent Grayskull

Tenstorrent Grayskull is a family of PCIe expansion cards for AI inference released by Tenstorrent in March 2024, comprising the Grayskull e75 and Grayskull e150 models. The cards are based on Tenstorrent's Tensix architecture, with the e75 featuring 96 Tensix cores at 75W and the e150 featuring 120 Tensix cores at 200W. They are supported by the TT-Buda and TT-Metalium open-source software stacks, enabling inference of models such as GPT-2 and Stable Diffusion. The product was announced alongside a developer bounty program and partnerships with Japan's LSTC and Rapidus.

## Key Claims

- Grayskull e75: 96 Tensix cores, 75W TDP, priced at $599.
- Grayskull e150: 120 Tensix cores, 200W TDP, priced at $799.
- Supported software stacks: TT-Buda and TT-Metalium, both open-source.
- AI models available through TT-Buda: GPT-2, Stable Diffusion, and others listed in the tt-buda-demos repository.
- Developer bounty program for adding models: Gemma 2B, Qwen 1.5 (0.5B), and others.
- Roadmap: Gen 1 networked AI product soon, Gen 2 (Blackhole) planned for April 2024, and Gen 3 low-cost AI later.
- Partnership with Japan's LSTC (Leading-edge Semiconductor Technology Center) and Rapidus for semiconductor development.

## Relationships

- [[k230]]: Canaan Kendryte K230 SoC with dedicated KPU for AI inference, representing a competing approach to AI acceleration at the edge.
- [[allwinner_v853]]: Allwinner V853 SoC with NPU up to 1 TOPS, another AI accelerator target in a different performance class.
- Insufficient context in the wiki for additional cross-links to directly related Tenstorrent or inference-card pages.

## Sources

- https://gigazine.net/gsc_news/en/20240311-jim-keller-tenstorrent-grayskull-e75-e150/
merge_draft_body -->

## [2026-07-02] merge_pending | sifive_automotive_family.md
target_page: sifive_automotive_family.md
canonical_name: SiFive Automotive Family
colliding_name: SiFive Automotive E6-A and S7-A
source: https://www.eeworldonline.com/development-tools-for-risc-v-support-sifive-automotive-solutions/
status: pending_review
<!-- merge_draft_body
# SiFive Automotive E6-A and S7-A

The SiFive Automotive E6-A and S7-A are RISC-V processor core families from SiFive designed for automotive applications such as infotainment, connectivity, and ADAS. The E6-A is a 32-bit real-time core targeting system control, hardware security modules (HSMs), safety islands, and standalone microcontrollers, while the S7-A is a 64-bit high-performance real-time core suited for modern SoCs requiring performant safety islands with low latency interrupt support and unified 64-bit memory space visibility. Both processor families offer flexibility for integrity levels including ASIL B and ASIL D, with split-lock capability for mixed criticalities in line with ISO 26262. IAR Systems provides the IAR Embedded Workbench for RISC-V, a comprehensive development toolchain certified by TÜV SÜD for functional safety standards including ISO 26262 and IEC 61508, which supports these SiFive Automotive cores. The toolchain includes a C/C++ compiler, debugger, and C-STAT static analysis tool for MISRA compliance.

## Key Claims

- The E6-A series is a 32-bit real-time RISC-V core for automotive system control, HSMs, and safety islands.
- The S7-A is a 64-bit high-performance real-time RISC-V core with low latency interrupt support and 64-bit memory space visibility for performant safety islands.
- Both processor families support ASIL B, ASIL D, and mixed criticalities through split-lock.
- IAR Embedded Workbench for RISC-V is certified by TÜV SÜD for ISO 26262 and IEC 61508 functional safety standards.
- The toolchain includes C-STAT for MISRA C/C++ static analysis to ensure code quality for automotive applications.
- The development solution aims to maximize energy efficiency, simplicity, security, and flexibility for embedded developers at OEMs and suppliers.

## Relationships

- [[xuantie_c908]]: Another RISC-V processor core family from T-Head, offering a comparison point for SiFive's automotive-focused cores.
- [[k230]]: A RISC-V SoC integrating the XuanTie C908, representing a different approach to RISC-V hardware for embedded systems with AI acceleration.

## Sources

- https://www.eeworldonline.com/development-tools-for-risc-v-support-sifive-automotive-solutions/
merge_draft_body -->
