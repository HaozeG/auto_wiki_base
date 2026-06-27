---
cold_start: true
created: 2026-06-27
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://arxiv.org/abs/2503.17422
- https://arxiv.org/html/2503.17422v1
- https://github.com/ggml-org/llama.cpp
- https://dl.acm.org/doi/10.1145/3719276.3727954
tags:
- risc-v
- LLM
- inference
- llama.cpp
- SG2042
- RVV
- benchmark
type: entity
updated: 2026-06-27
---

# LLM Inference on RISC-V

Large language model (LLM) inference on RISC-V hardware became practically feasible in 2024–2025 with the arrival of server-class many-core RISC-V CPUs and the porting of major inference frameworks. The primary inference engine is llama.cpp, which added native RISC-V Vector (RVV), ZVFH (half-precision vector floating-point), ZFH, ZICBOP (cache prefetch), and ZIHINTPAUSE support, enabling quantized (INT4/INT8) model execution on RVV-capable hardware without software emulation. The most detailed published benchmark is V-Seek (arXiv 2503.17422, March 2025), which optimizes LLM reasoning on the SOPHGO SG2042 — a 64-core XuanTie C920 RISC-V CPU inside the Milk-V Pioneer workstation. On DeepSeek R1 Distill Llama 8B, V-Seek achieves 4.32 tokens/s for token generation and 6.54 tokens/s for prompt processing; on DeepSeek R1 Distill Qwen 14B, 2.29 tokens/s generation and 3.68 tokens/s prompt processing. These throughputs represent 2.9× to 3.0× speedups compared to the unoptimized baseline on the same hardware. The RISC-V software ecosystem for LLM inference is not yet fully mature: software toolchains, kernel libraries, and memory bandwidth remain bottlenecks relative to x86 and ARM, but RISC-V's open-license ISA and the RVV extension provide a clear pathway toward custom AI inference silicon.

## Key Claims

- llama.cpp supports RISC-V natively via RVV, ZVFH, ZFH, ZICBOP, and ZIHINTPAUSE ISA extensions.
- V-Seek (arXiv 2503.17422) benchmarks LLM inference on SOPHGO SG2042 (64-core XuanTie C920 at 2 GHz).
- DeepSeek R1 Distill Llama 8B reaches 4.32 token/s generation and 6.54 token/s prompt processing on SG2042 with V-Seek.
- V-Seek achieves 2.9–3.0× speedup over the baseline llama.cpp on the same RISC-V hardware.
- DeepSeek R1 Distill Qwen 14B yields 2.29 token/s generation and 3.68 token/s prompt processing on SG2042.
- RISC-V's open ISA and RVV provide the foundation for future custom LLM inference SoCs with specialized matrix/vector units.

## Relationships

- [[milkv_pioneer_duo]]: SG2042 inside Milk-V Pioneer is the hardware platform used in V-Seek benchmarks.
- [[risc_v_vector_extension]]: RVV is the ISA building block that makes llama.cpp RISC-V support viable.
- [[riscv_matrix_extension]]: The upcoming RISC-V matrix extension (AME) targets exactly the matrix-multiply bottleneck in LLM inference.
- [[tvm_riscv_backend]]: TVM and IREE provide alternative compiler paths for deploying LLMs on RISC-V.

## Sources

- https://arxiv.org/abs/2503.17422 (V-Seek paper: LLM inference on SG2042)
- https://arxiv.org/html/2503.17422v1 (V-Seek full HTML with benchmark tables)
- https://github.com/ggml-org/llama.cpp (llama.cpp RISC-V RVV support)
- https://dl.acm.org/doi/10.1145/3719276.3727954 (V-Seek poster at ACM Computing Frontiers 2025)
