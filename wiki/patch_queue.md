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
