---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.5
  claim_density: 0.7
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.3
sources:
- https://zhuanlan.zhihu.com/p/617155419
- https://github.com/RoySegal/tvmcon23_byoc
tags:
- tvm
- deep-learning-compiler
- code-generation
- byoc
type: entity
updated: '2026-06-27'
---

# TVM BYOC

Bring Your Own Codegen (BYOC) is a feature of Apache TVM that allows hardware vendors and developers to integrate proprietary or custom code generators into the TVM compilation pipeline without modifying the core framework. Hardware companies often have their own graph compilers tuned to their specific accelerator architectures; BYOC enables them to offload parts of a computation graph to these backends while retaining TVM's flexibility for the remaining portions of the model. This approach ensures that customers receive the same backend performance and numerical accuracy they expect from the native compiler, plus the added flexibility of TVM's end-to-end optimization stack. BYOC can be implemented in two primary ways: through C/C++ code generation for well-optimized hardware backends or through other integration mechanisms. The feature was a central topic at TVMCon 2023, where a tutorial demonstrated step-by-step how to create a new codegen integration using BYOC. In addition, TVM Unity, the next-generation compilation framework, further modularises the pass infrastructure to make BYOC offloading seamless and composable with other passes such as lowering and MetaSchedule tuning.

## Key Claims

- BYOC enables integration of hardware-specific graph compilers into TVM, allowing end users to benefit from both the native backend performance and TVM's flexibility.
- Two types of BYOC are available: C/C++ code generation for hardware backends that are already well-optimized.
- A practical tutorial on BYOC was presented at TVMCon 2023 by Roy Segal, with accompanying source code at the GitHub repository `RoySegal/tvmcon23_byoc`.
- TVM Unity further modularises the compilation flow, making BYOC offloading composable with passes like lowering and MetaSchedule tuning, as demonstrated in a TVM Discuss tutorial.
- The TVMCon 2023 presentation covered the rationale for using BYOC: keeping customers satisfied with consistent performance and accuracy while leveraging TVM's ecosystem.

## Relationships

- [[tvm]] — Apache TVM is the deep learning compiler framework that hosts the BYOC feature.
- [[tvm_unity]] — TVM Unity is the next-generation IR and pass infrastructure that enhances BYOC composability.
- [[tvm_metaschedule]] — MetaSchedule tuning passes can be combined with BYOC offloading in the Unity flow.
- [[tvm_codegen]] — Custom code generators are the core components integrated via BYOC.

## Sources

- https://zhuanlan.zhihu.com/p/617155419 (TVM BYOC in Practice – TVMCon2023)
- https://github.com/RoySegal/tvmcon23_byoc (GitHub repository with BYOC tutorial code)
