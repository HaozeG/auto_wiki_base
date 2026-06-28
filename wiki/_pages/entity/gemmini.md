---
cold_start: true
created: 2026-06-27
inbound_links: 21
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://github.com/ucb-bar/gemmini
- https://arxiv.org/abs/1911.09925
- https://people.eecs.berkeley.edu/~ysshao/assets/papers/beagle_esscirc_2021.pdf
tags:
- risc-v
- accelerator
- systolic-array
- open-source
- ml-hardware
- uc-berkeley
type: entity
updated: 2026-06-27
---

# Gemmini

Gemmini is an open-source, parameterizable systolic array accelerator generator for deep neural network (DNN) inference, developed at UC Berkeley as part of the Chipyard SoC ecosystem. It connects to a host RISC-V CPU via the Rocket Chip Co-processor (RoCC) interface, enabling tightly coupled hardware–software co-design. Gemmini targets full-stack DNN exploration: the same generator can produce silicon tape-outs, FPGA prototypes, and cycle-accurate simulations from a single parametric description, making it a primary vehicle for architecture research in the RISC-V ML-hardware space.

## Key Claims

- Default configuration uses a 16×16 systolic array of multiply-accumulate (MAC) units; array dimensions are configurable (e.g., 32×32) via Chisel generator parameters `meshRows`, `meshColumns`, `tileRows`, `tileColumns`.
- Supports both output-stationary and weight-stationary dataflows, selectable at runtime or hardened at elaboration time, distinguishing it from fixed-dataflow accelerators.
- Data types are fully configurable: default input is 8-bit integer (`SInt(8.W)`), accumulator is 32-bit integer, with optional IEEE floating-point modes (e.g., `Float(8, 24)`).
- Memory subsystem comprises a banked scratchpad SRAM for input/weight storage and a separate accumulator SRAM with in-place adder units for partial-sum accumulation.
- Exposed to software via custom RoCC instructions: `mvin`/`mvout` for DMA transfers, `matmul.preload` and `matmul.compute.*` for computation, and high-level CISC-style loop instructions (`gemmini_loop_ws`, `gemmini_loop_conv_ws`) for large matrix multiplications and convolutions.
- Demonstrated on ResNet-50 and multi-layer perceptron (MLP) workloads via ONNX-Runtime integration within the Chipyard framework.
- A silicon prototype reported in ESSCIRC 2021 (Beagle SoC) achieved 106.1 GOPS/W on a 16 mm² heterogeneous RISC-V multi-core die.

## Relationships

- [[risc_v_vector_extension]]: Gemmini complements RVV by providing fixed-function matrix datapath acceleration rather than programmable vector lanes.
- [[tvm_riscv_backend]]: TVM can target Gemmini's RoCC instruction interface for model compilation, enabling end-to-end ML deployment.
- [[ara_vector_processor]]: Both are UC Berkeley / ETH Zurich open-source accelerators; Gemmini uses systolic arrays while Ara uses in-order vector lanes.

## Sources

- GitHub repository: https://github.com/ucb-bar/gemmini
- Paper: "Gemmini: An Agile Systolic Array Generator Enabling Systematic Evaluations of Deep-Learning Architecture Stacks" — arXiv:1911.09925
- Silicon demo: Beagle SoC, ESSCIRC 2021 — https://people.eecs.berkeley.edu/~ysshao/assets/papers/beagle_esscirc_2021.pdf
