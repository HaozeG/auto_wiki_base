---
type: entity
tags: [isa-extension, matrix-multiply, x86, intel, ai-acceleration]
sources:
  - https://en.wikipedia.org/wiki/Advanced_Matrix_Extensions
  - https://en.wikichip.org/wiki/x86/amx
  - https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/what-is-intel-amx.html
  - https://www.phoronix.com/review/intel-xeon-amx
  - https://www.intel.com/content/www/us/en/developer/articles/technical/accelerate-pytorch-training-inference-on-amx.html
  - https://docs.cortensor.network/technical-architecture/ai-inference/cpu-instruction-sets-for-llm-inference-avx-amx-sme-vs-gpus
created: 2026-06-26
updated: 2026-06-26
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# Intel AMX (Advanced Matrix Extensions)

Intel Advanced Matrix Extensions (AMX) is an x86 ISA extension introduced by Intel in the 4th Generation Xeon Scalable processors (Sapphire Rapids, released January 2023) that accelerates matrix multiplication workloads central to deep learning inference and training. AMX introduces a new tile register file — eight 2-D registers named tmm0 through tmm7, each 1 KB in size (16 rows × 64 bytes per row) — that hold sub-matrices resident in the CPU for computation without round-tripping to the cache hierarchy. A dedicated on-chip accelerator called the Tile Matrix Multiply Unit (TMUL) operates on these registers, performing fused multiply-accumulate operations on pairs of tiles and accumulating results into a third tile. Native data types are BF16 (Brain Float 16, with accumulation in FP32) and INT8 (with accumulation in INT32). Compared with AVX-512 VNNI — the dominant x86 path for matrix multiply before AMX — AMX can compute 1,024 BF16 multiply-accumulate operations per cycle versus 64 with AVX-512, representing a roughly 16× throughput improvement per core for sustained GEMM kernels. AMX is transparently used by Intel's oneDNN library (the backend for PyTorch and OpenVINO on Intel hardware) when the target ISA level is set to AVX512_CORE_AMX, requiring no changes to user-level neural-network code.

## Key Claims

- AMX introduces 8 tile registers (tmm0–tmm7), each 1 KB (16 rows × 64 bytes), constituting a new 8 KB 2-D register file added to the x86 architectural state.
- The TMUL unit performs Z += matmul(X, Y) in a single instruction pass; for BF16, two 16-bit inputs are internally promoted to FP32 before accumulation; for INT8, groups of four 8-bit values produce INT32 outputs.
- AMX throughput for BF16 is 1,024 operations per cycle per core, compared to 64 operations per cycle with AVX-512 VNNI, an approximately 16× improvement for large matrix kernels.
- Tile dimensions are configured at runtime via the LDTILECFG instruction, which reads a 64-byte memory descriptor specifying the palette, number of active tiles, row count, and column byte width; TILERELEASE frees all tiles before the next configuration.
- Key AMX instructions: LDTILECFG (configure tile state), TILELOADD / TILELOADDT1 (load tile from memory with optional L1 hint), TILESTORED (store tile to memory), TDPBF16PS (BF16 tile dot-product accumulate to FP32), TDPBUSD (INT8 unsigned×signed tile dot-product to INT32), TILERELEASE (reset tile state).
- AMX state is managed through the XSAVE/XRSTOR framework via two new state components: XTILECFG (512 bytes) and XTILEDATA (8 KB), enabling correct OS context-switching and virtualization support.
- Sapphire Rapids first shipped in production in January 2023; AMX support was subsequently extended to Intel Core Ultra (Meteor Lake, December 2023) client processors and Granite Rapids server processors (2024).
- Real-world inference benchmarks show approximately 2× tokens-per-second throughput for quantized LLM inference (e.g., LLaMA 3.2B INT8: ~57 t/s with AMX vs. ~28 t/s without) when using oneDNN-backed PyTorch.
- The published 4–8× AMX speedup over AVX-512 VNNI cited in Intel marketing applies specifically to sustained GEMM loops over large matrices inside tuned libraries (oneDNN, MKL), not to isolated single-tile operations.

## Relationships

- [[arm_sme]]: ARM Scalable Matrix Extension is the direct architectural counterpart to AMX in the Arm ISA; both add 2-D tile register files and dedicated matrix-multiply engines, but SME integrates with SVE2 predication while AMX is x86-specific.
- [[arm_sve2]]: SVE2 is the Arm vector extension that AMX's AVX-512 predecessor competes with; neither has native matrix-tile semantics unlike AMX/SME.
- [[risc_v_matrix_extensions]]: The RISC-V matrix extension proposals (IME/VME/AME) address the same GEMM acceleration problem as AMX in an open ISA context.
- [[gemmini]]: Gemmini is an open-source research accelerator for matrix multiply with a systolic array dataflow; AMX's TMUL is a commercial on-die equivalent targeting server CPUs rather than SoC integration.
- [[sifive_intelligence_x280]]: SiFive X280 implements RISC-V V (RVV) and is a competing CPU-side approach to AI inference throughput without dedicated tile registers.
- [[intel_itanium]]: An earlier Intel architecture with explicit parallelism and specialized functional units; AMX continues Intel's tradition of ISA-level hardware-software co-design for specific workloads.

## Sources

- Intel official AMX product page: https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/what-is-intel-amx.html
- WikiChip AMX architecture reference: https://en.wikichip.org/wiki/x86/amx
- Wikipedia Advanced Matrix Extensions: https://en.wikipedia.org/wiki/Advanced_Matrix_Extensions
- Phoronix AMX benchmarks on Sapphire Rapids: https://www.phoronix.com/review/intel-xeon-amx
- Intel developer article: Accelerate PyTorch Training and Inference using Intel AMX: https://www.intel.com/content/www/us/en/developer/articles/technical/accelerate-pytorch-training-inference-on-amx.html
- Cortensor CPU ISA comparison (AMX vs AVX vs SME): https://docs.cortensor.network/technical-architecture/ai-inference/cpu-instruction-sets-for-llm-inference-avx-amx-sme-vs-gpus
- Fixstars AMX explanation: https://blog.us.fixstars.com/intel-amx-advanced-matrix-extension-explained-introduction/
- Intel AMX acceleration brief (PDF): https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2022-12/accelerate-ai-with-amx-sb.pdf
