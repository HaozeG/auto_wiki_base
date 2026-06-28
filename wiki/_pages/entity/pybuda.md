---
cold_start: false
created: '2026-06-27'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.5
  claim_density: 0.6
  hub_potential: 0.3
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://docs.tenstorrent.com/docs-test/pybuda/latest/user_guide.html
tags:
- tenstorrent
- compiler
- ML-framework
- tvm
type: entity
updated: '2026-06-28'
---

# PyBuda

PyBuda is Tenstorrent's ML compiler and runtime framework that enables the compilation and execution of AI workloads on Tenstorrent hardware, supporting multiple model frameworks including PyTorch, TensorFlow, JAX, ONNX, and TensorFlow Lite. It provides a Python API inspired by PyTorch for defining devices, placing modules, feeding inputs, and retrieving results. PyBuda allows distribution across heterogeneous devices (Tenstorrent, CPU, GPU) and includes features such as automatic CPU fallback for unsupported operators, a Tenstorrent Device Image (TTI) format for offline compilation and deployment, and support for both inference and training loops with gradient accumulation. The framework exposes low-level controls for manual training loops while also providing high-level all-in-one APIs like `run_inference` and `run_training` for common workflows.

## Key Claims

- PyBuda provides native support for PyBuda modules and supports PyTorch, TensorFlow, JAX, ONNX, and TensorFlow Lite through wrapper classes.
- It can distribute workloads across a heterogeneous set of devices including Tenstorrent devices, CPUs, and GPUs.
- CPU fallback is available for operators not supported by PyBuda, enabled via `compiler_cfg.enable_tvm_cpu_fallback`.
- Tenstorrent Device Image (TTI) archives capture the entire compiled state of a model, allowing offline compilation and cross-machine deployment.
- TTI archives include device configuration, compiler configuration, compiled model artifacts, backend build binaries, and parameter tensors.
- The framework supports both inference and training workflows, with manual control over forward, backward, and optimizer steps.
- Compilation can be performed on machines without a silicon device by setting target architecture and device type, saving a TTI for later deployment.

## Relationships

- [[tvm_riscv_backend]]: PyBuda provides a backend for TVM, allowing models from TVM-supported frameworks to target the PyBuda compiler for Tenstorrent hardware.
- [[risc_v_vector_extension]]: Through TVM, PyBuda can potentially target RISC-V vector units for inference, though PyBuda primarily targets Tenstorrent custom silicon.

## Sources

- https://docs.tenstorrent.com/docs-test/pybuda/latest/user_guide.html
