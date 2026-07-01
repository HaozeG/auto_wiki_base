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
