---
type: entity
tags:
  - risc-v
  - open-source
  - cpu
  - storage
  - chips-alliance
  - western-digital
sources:
  - https://github.com/chipsalliance/Cores-SweRV
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.7
  claim_density: 0.75
  self_containedness: 0.85
  bridge_score: 0.45
  hub_potential: 0.35
---

# Western Digital SweRV RISC-V Core

The SweRV core family is a set of open-source RISC-V processor cores originally designed and used by Western Digital (WD) for its NAND flash storage controllers and subsequently open-sourced in 2019 under the Apache 2.0 license via the CHIPS Alliance. The flagship SweRV EH1 is a 9-stage, dual-issue in-order pipeline capable of 4.9 CoreMark/MHz, synthesizing at 1.8 GHz in a 28 nm process—performance competitive with ARM Cortex-M7. Western Digital's decision to open-source SweRV marked the first time a major storage company released a production-grade RISC-V core as open hardware, establishing SweRV as an important reference design for the RISC-V ecosystem. The family grew to include EH2 (dual-hardware-thread variant for higher throughput) and EL2 (ultra-low-power, single-issue pipeline targeting IoT and embedded ML edge nodes). While not designed specifically for ML inference, SweRV cores are used as reference platforms for evaluating open-source RISC-V ML toolchains and have been integrated in academic neural network accelerator research.

## Key Claims

- SweRV EH1 was open-sourced by Western Digital in February 2019 under Apache 2.0, making it the first production RISC-V core from a major storage OEM to be released as open hardware.
- EH1 achieves 4.9 CoreMark/MHz with a 9-stage dual-issue in-order pipeline, synthesizing at 1.8 GHz in TSMC 28nm—comparable to ARM Cortex-M7 performance.
- EH2 adds dual hardware threads (SMT) to the EH1 microarchitecture, improving throughput for mixed storage and compute workloads without doubling area.
- EL2 is an ultra-low-power single-issue 4-stage variant targeting IoT and embedded ML edge deployments at sub-100 MHz frequencies.
- CHIPS Alliance, a Linux Foundation project, now hosts and maintains the SweRV core repositories, broadening community contributions beyond WD.
- SweRV cores are deployed in Western Digital's NVMe and flash storage controller ASICs, giving them a production track record outside the academic domain.

## Relationships

- [[risc_v_architecture]] — SweRV implements the RISC-V RV32IMC ISA; its open-source release is a landmark in the RISC-V commercial adoption story.
- [[fpga_riscv_isa_extension_nn_inference]] — SweRV EL2 has been used in FPGA-based NN inference research contexts.
- [[tinyml_mcu_inference]] — EL2 targets power envelopes relevant to TinyML MCU inference workloads.
- [[lowrisc_opentitan]] — Parallel open-source RISC-V hardware effort (security-focused) from lowRISC/Google.

## Sources

- CHIPS Alliance SweRV core repository: https://github.com/chipsalliance/Cores-SweRV
- Western Digital SweRV announcement blog post (February 2019)
- CHIPS Alliance project page: https://chipsalliance.org/
