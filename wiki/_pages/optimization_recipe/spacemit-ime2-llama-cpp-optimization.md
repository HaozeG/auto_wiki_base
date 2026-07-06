---
canonical_name: SpacemiT IME2 llama.cpp optimization
aliases:
- K3 IME2 optimization
- spine_barrier_t llama.cpp
- SpacemiT llama.cpp fork
subtype: null
tags: []
hardware_targets:
- SpacemiT K3
workloads:
- LLM inference (Qwen3-0.6B Q4_K_M)
datatypes:
- Q4_K_M
metrics:
- tokens per second (tok/s)
toolchains:
- llama.cpp vendor fork (PR
- Linux kernel (with registration for A100 core affinity)
constraints:
- A100 cores reserved via kernel registration
- pthreads pinned to cores 8–13
- spine_barrier_t atomic spinlock barrier
- persistent work loop (no OS dispatch)
evidence_strength: measured
scorecard:
  novelty_delta: 0.8
  claim_density: 0.7
  self_containedness: 0.7
  bridge_score: 0.5
  hub_potential: 0.6
sources:
- raw/cache/673f92af34a7ba79.md
- https://bruno.verachten.fr/2026/03/12/benchmarking-llama.cpp-on-spacemit-k3-risc-v-ai-cores-vs-standard-rvv-part-4/
source_url: https://bruno.verachten.fr/2026/03/12/benchmarking-llama.cpp-on-spacemit-k3-risc-v-ai-cores-vs-standard-rvv-part-4/
fetched_at: '2026-07-06T01:58:04.531727+00:00'
type: optimization_recipe
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: spacemit-k3-hardware-target
  reason: Describes the hardware platform and its IME2 matrix instructions
- target: llama.cpp-on-spacemit-k3-benchmark
  reason: Records the benchmark results achieved with this optimization
---

# SpacemiT IME2 llama.cpp optimization

The SpacemiT IME2 optimization recipe transforms the standard llama.cpp inference pipeline on the K3 SoC to unlock the A100 AI cores' matrix multiplication throughput. Prerequisites include the vendor llama.cpp fork (PR #22863), kernel drivers that allow pinning to reserved cores (8–13), and the use of spine_barrier_t atomic spinlock barriers for worker synchronization. The transformation replaces conventional thread dispatch with a persistent work loop where six pthreads are pinned to cores 8–13, never returning to the OS scheduler between operations, and process matrix tiles from a shared queue via barriers. The expected effect is a lift from approximately 2.5 tok/s (30x slower than X100) to 111 tok/s for prompt processing. Failure modes include missing kernel registration causing silent affinity refusal, and Go scheduling overhead if used instead of C pthreads.

## Key Claims

- Using the vendor llama.cpp fork (PR #22863) with IME2 matrix instructions improves A100 prompt processing throughput from 30x slower than X100 to 111 tok/s.
- The optimization uses six pthreads permanently pinned to cores 8–13.
- Worker synchronization uses spine_barrier_t atomic spinlock barriers, eliminating OS dispatch overhead.
- Without kernel registration for A100 core affinity, the optimization silently fails.
- Go scheduling is unsuitable due to higher overhead; C pthreads are required.

## Transformation

- Prerequisites:
  - SpacemiT K3 SoC with Linux kernel supporting registration for A100 core affinity.
  - Vendor llama.cpp fork (PR #22863) that implements the persistent worker pattern.
- Steps:
  1. Ensure kernel registration for A100 cores (cores 8–13) is complete; without it, affinity changes are silently refused.
  2. Use the vendor llama.cpp fork which spawns six pthreads targeting cores 8–13.
  3. Threads execute a persistent work loop: they never exit to the OS scheduler between operations.
  4. Synchronization via spine_barrier_t (atomic spinlock barrier) instead of conventional dispatch.
  5. Threads consume matrix tiles from a shared queue processed by IME2 matrix instructions.
- Expected effect:
  - A100 prompt processing throughput jumps from ~2.5 tok/s (~30x slower than X100) to 111 tok/s, exceeding X100 performance.
  - Text generation may not benefit as much; gains are primarily in prompt processing.
- Failure modes:
  - Missing kernel registration: affinity changes are silently refused, cores remain fenced off.
  - Using Go instead of C for threading: higher overhead negates benefits.
  - Using standard llama.cpp without IME2: A100 prompt processing is ~30x slower.
- Measurements:
  - X100 text generation: 76 tok/s, A100 prompt without IME2: ~2.5 tok/s, A100 prompt with IME2: 111 tok/s.

## Relationships

- [[spacemit-k3-hardware-target]]: Describes the hardware platform and its IME2 matrix instructions.
- [[llama.cpp-on-spacemit-k3-benchmark]]: Records the benchmark results achieved with this optimization.

## Sources

- https://bruno.verachten.fr/2026/03/12/benchmarking-llama.cpp-on-spacemit-k3-risc-v-ai-cores-vs-standard-rvv-part-4/
