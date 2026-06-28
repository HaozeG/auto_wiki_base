---
cold_start: true
created: YYYY-MM-DD
inbound_links: 1
scorecard:
  bridge_score: 0.5
  claim_density: 0.5
  hub_potential: 0.3
  novelty_delta: 0.7
  self_containedness: 0.9
sources:
- https://github.com/rpelke/tvmonriscv/
tags:
- RISC-V
- TVM
- Machine Learning
- Workflow
type: entity
updated: '2026-06-28'
---

# tvmonriscv: TVM Compilation Workflow for RISC-V

The tvmonriscv repository provides a minimal, end-to-end example of building a convolutional neural network (CNN) using TensorFlow, compiling it with Apache TVM, and executing the compiled model on a RISC-V target using user-mode QEMU. The workflow includes scripts for building LLVM and TVM with RISC-V support, training an MNIST digit recognition model offline, compiling the model into a shared object for host execution, and cross-compiling the same model for execution inside a RISC-V QEMU environment. Additionally, the repository demonstrates a method for generating C code from TVM and using a Clang cross-compiler to apply auto-vectorization for the RISC-V vector extension, which is not natively supported by the current TVM version. This makes tvmonriscv a practical reference for researchers and practitioners interested in deploying machine learning workloads on RISC-V platforms using the TVM compiler stack.

## Key Claims

- TVM can compile a CNN model (MNIST) for both native host execution and RISC-V QEMU (64-bit) execution using the TVM C++ runtime.
- TVM does not currently support the RISC-V vector extension; a workaround generates C code from TVM and compiles it with Clang to leverage LLVM's auto-vectorization features.
- The repository includes build scripts for LLVM and TVM with RISC-V target support, using a specific commit (710a81b) of the riscv-gnu-toolchain.
- Execution in RISC-V QEMU is demonstrated via shell scripts that load the compiled shared object using dlopen.
- A static cross-compilation example is also provided for running inference without dlopen.

## Relationships

- [[Sipeed_MAIX_series]] – The Sipeed MAIX series is an example of a RISC-V development board that could potentially run models compiled with this workflow.

## Sources

- [GitHub repository rpelke/tvmonriscv](https://github.com/rpelke/tvmonriscv/)
