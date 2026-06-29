---
cold_start: false
constraints:
- Requires LLM with coding capability
- Requires test suite for compile-and-test feedback
created: '2026-07-10'
datatypes: []
evidence_strength: measured
hardware_targets:
- RISC-V Vector Extension v1.0
inbound_links: 0
metrics:
- performance speedup
needs_summary_revision: true
scorecard:
  bridge_score: 0.6
  claim_density: 0.7
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.7
sources:
- https://arxiv.org/html/2510.10119v1
tags:
- RISC-V
- LLM
- intrinsic
- translation
- vector
toolchains:
- LLM (GPT-5, Claude-4, etc.)
type: optimization_recipe
updated: '2026-06-28'
workloads:
- Vectorized algorithms (34 cases from open-source libraries)
---

# IntrinTrans: LLM-based Intrinsic Code Translator for RISC-V Vector

IntrinTrans is an LLM-based multi-agent framework designed to translate intrinsic code from Arm Neon to RISC-V Vector (RVV) intrinsics automatically. The framework integrates compile-and-test feedback loops and liveness analysis optimization to produce semantically correct and high-performance RVV intrinsic code. It comprises specialized agents—an RVV-code Translator, Compilation Executor, Test Executor, and Optimizer—orchestrated by a finite state machine. Evaluated on 34 vectorized algorithm cases from open-source libraries, IntrinTrans with advanced LLMs demonstrates up to 5.93× performance improvement over native community implementations. This tool addresses the scarcity of RVV programming expertise and fills a gap in cross-architecture intrinsic translation, which previously relied heavily on manual rewriting or incomplete rule-based methods.

## Key Claims

- IntrinTrans uses an LLM-based multi-agent approach with compile-and-test feedback to translate Arm Neon intrinsics to RVV intrinsics.
- The framework includes an Optimizer agent that uses liveness analysis to improve vector register utilization.
- Evaluated on 34 vectorized algorithm cases from open-source libraries (e.g., OpenCV, OpenBLAS, NCNN).
- With advanced LLMs, the translated code achieves up to 5.93× the performance of the native RVV implementations from the open-source community.
- Rule-based approaches (e.g., SSE2RVV) have low success rates due to RVV's sizeless type system and dynamic vector-length execution model.
- Naive prompting without iterative feedback yields low success rates; the iterative compile-and-test cycle is crucial.

## Transformation

- Prerequisites: Arm Neon intrinsic C/C++ code for vectorized algorithms, a test suite with correctness checks and performance measurement infrastructure, and access to an LLM with strong code generation capabilities (e.g., GPT-5, Claude-4).
- Steps:
  1. Input Arm Neon intrinsic code to the IntrinTrans framework.
  2. The Translator agent generates an initial RVV intrinsic candidate.
  3. The Compilation Executor attempts to compile the candidate and reports errors back to the Translator for refinement.
  4. The Test Executor runs correctness tests on the compiled code; failures are fed back for correction.
  5. The Optimizer performs liveness analysis to identify vector register pressure and suggests optimization improvements.
  6. Steps 2–5 repeat until the code passes all tests and performance targets are met.
- Expected effect: Semantically correct and performance-competitive RVV intrinsics, with speedups up to 5.93× over community RVV implementations in some cases.
- Failure modes: Without iterative feedback, naive LLM prompting often produces semantically or syntactically incorrect code. Incomplete test suites may allow subtle bugs. LLM limitations on novel ISA features can stall convergence.
- Measurements: Evaluated on 23 mainstream LLMs; up to 5.93× speedup measured; success rate after limited iterations is high for advanced LLMs.

## Relationships

- [[GEMM_with_RISC-V_Vector_Extension]] – A vectorized workload kernel that could be translated from Arm Neon to RVV using IntrinTrans.
- [[XuanTie_C906]] – A commercial RISC-V core with RVV v0.7.1, representing a hardware target for translated intrinsic code.

## Sources

- [IntrinTrans: LLM-based Intrinsic Code Translator for RISC-V Vector - arXiv](https://arxiv.org/html/2510.10119v1)

