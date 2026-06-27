---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.5
  claim_density: 0.2
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.3
sources:
- https://docs.jax.dev/en/latest/parallel.html
tags:
- jax
- parallel-computing
- google
- machine-learning
- xla
type: entity
updated: '2026-06-26'
---

# JAX (library)

JAX is a high-performance machine learning library developed by Google that provides automatic differentiation and just-in-time compilation via the Accelerated Linear Algebra (XLA) compiler. The library includes a powerful parallelization module, documented at docs.jax.dev/en/latest/parallel.html, which implements distributed arrays and automatic parallelization across multiple devices such as GPUs and TPUs. Through APIs like `pmap`, `shard_map`, and the experimental `pjit`, JAX enables transparent distribution of tensor operations over multi-device systems without requiring explicit communication calls. This abstraction reduces the complexity of scaling machine learning workloads, allowing researchers to implement operations on logically single arrays that are automatically partitioned across hardware accelerators. The automatic parallelization framework replaces traditional MPI-based patterns with a composable, functional programming model that leverages XLA's ability to fuse and optimize distributed operations. JAX's approach to parallelism is integral to its ecosystem, supporting both single-program multiple-data (SPMD) and data-parallel strategies for efficient large-scale training.

## Key Claims

- JAX's `pmap` function transforms a function into an SPMD program that runs across multiple devices, with automatic parallelization and collective communication.
- The `shard_map` API allows explicit sharding strategies for array operations, combining the flexibility of manual partitioning with JAX's compiler optimizations.
- The `pjit` (partitioned JIT) API enables fine-grained control over how operations are distributed across devices by using partition specifications.
- JAX's distributed array abstractions automatically handle device placement, communication, and synchronization, hiding low-level details from the user.
- The parallelization module supports both GPU and TPU hardware, using XLA for backend-agnostic compilation.
- JAX's functional paradigm ensures that parallel operations remain pure and composable, enabling automatic differentiation through distributed computations.

## Relationships

- [[ai_chip_export_controls]] — The export controls on high-performance AI chips (e.g., NVIDIA H100, AMD MI300X) directly impact the availability and performance of GPU hardware that JAX relies on for distributed computing; restricted chips limit the scale of JAX-based training workloads in affected regions.

## Sources

- https://docs.jax.dev/en/latest/parallel.html
