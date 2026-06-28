# Wiki Patch Queue

## [2026-06-28] pending | Gemmini_systolic_array_GEMM_accelerator.md
target_page: Gemmini_systolic_array_GEMM_accelerator.md
target_section: Key Claims
source: https://github.com/QuarantineGemmini/gemmini
status: pending_review
proposed_update: Add the following claims supported by the QuarantineGemmini/gemmini README: 'Includes peripheral circuitry to optionally apply activation functions (ReLU, ReLU6)', 'Supports power-of-2 scaling for quantized workloads', 'Supports matrix transpose before feeding into the systolic array for output-stationary dataflow', 'Dataflow can be hardened at elaboration time in addition to runtime selection', 'DMA parameters dma_maxbytes and dma_buswidth are tightly coupled with Rocket Chip SoC system parameters (cache block size and bus beat width)'.

## [2026-06-28] pending | Gemmini_systolic_array_GEMM_accelerator.md
target_page: Gemmini_systolic_array_GEMM_accelerator.md
target_section: Optimization-Relevant Details
source: https://github.com/QuarantineGemmini/gemmini
status: pending_review
proposed_update: Add bullet: 'Peripheral circuitry: activation functions (ReLU, ReLU6), power-of-2 scaling, transpose support'.

## [2026-06-28] pending | Gemmini_systolic_array_GEMM_accelerator.md
target_page: Gemmini_systolic_array_GEMM_accelerator.md
target_section: First paragraph (after existing first paragraph)
source: https://github.com/QuarantineGemmini/gemmini
status: pending_review
proposed_update: Insert sentence: 'The accelerator includes peripheral circuitry for activation functions (ReLU, ReLU6), power-of-2 scaling for quantized workloads, and matrix transpose to support different dataflows.'

## [2026-06-28] pending | Sipeed_MAIX_series.md
target_page: Sipeed_MAIX_series.md
target_section: Key Claims
source: https://deepwiki.com/kendryte/canmv/5.1-kpu-neural-network-processor
status: pending_review
proposed_update: Add detailed claims about the KPU (Knowledge Processing Unit) neural network processor based on the DeepWiki resource: The KPU enables real-time inference on Kendryte K210; supports CNN for computer vision tasks; includes model loading from SD card/flash; implements DMA channels for input image transfer, weight loading, output retrieval, and intermediate activation movement; exposes Python API through maix module with argument parsing for model path, input image, anchor boxes, and threshold; uses pix_ai field in image_t structure for optimized memory access; error handling includes validation for model format, input dimensions, memory allocation, and hardware status using MicroPython exception patterns.
