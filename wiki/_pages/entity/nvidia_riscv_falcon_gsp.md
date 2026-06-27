---
type: entity
tags: [risc-v, NVIDIA, GPU, firmware, embedded-controller, Falcon]
sources:
  - https://docs.kernel.org/gpu/nova/core/falcon.html
  - https://download.nvidia.com/XFree86/Linux-x86_64/560.28.03/README/gsp.html
  - https://deepwiki.com/NVIDIA/open-gpu-kernel-modules/4.3-gsp-gpu-system-processor
  - https://www.techpowerup.com/291088/nvidia-unlocks-gpu-system-processor-gsp-for-improved-system-performance
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# NVIDIA RISC-V: Falcon and GPU System Processor (GSP)

NVIDIA has embedded RISC-V microcontrollers inside its GPUs for low-level firmware, power management, and initialization tasks, making NVIDIA one of the largest volume deployers of RISC-V in production silicon. The original Falcon (FAst Logic Controller) architecture was NVIDIA's proprietary RISC-like microcontroller present in every modern GPU for decades, handling secure boot, display control, video decoding, and copy engines. Starting with the Turing GPU generation (2018), NVIDIA introduced the GPU System Processor (GSP), a dedicated RISC-V core embedded on the GPU die that offloads GPU initialization and runtime management from the host CPU driver to on-GPU firmware, improving latency and reducing host CPU overhead. GSP is enabled by default for all Turing and later GPUs in the open-source kernel module released by NVIDIA in 2022.

## Key Claims

- NVIDIA GPUs embed multiple Falcon microcontroller instances per chip for secure firmware tasks, initialization, copy engines, and power management.
- Starting with Turing (2018), NVIDIA replaced legacy Falcon CPU with a RISC-V core for the GSP (GPU System Processor) role.
- GSP firmware files are architecture-specific binaries (e.g., gsp_tu10x.bin for Turing) distributed with the NVIDIA driver and loaded at driver initialization.
- Falcon cores operate in three security modes: Non-Secure (NS), Light Secure (LS), and Heavy Secure (HS), with HS mode used for sensitive cryptographic and boot operations.
- NVIDIA open-sourced its GPU kernel modules in May 2022 (open-gpu-kernel-modules on GitHub), exposing the GSP communication interface.
- Offloading GPU management to the RISC-V GSP improves system performance by reducing host CPU interrupt latency for GPU management tasks.
- Modern NVIDIA GPUs may contain multiple distinct RISC-V/Falcon instances: GSP for management, SEC2 for security, and per-engine controllers.

## Relationships

- [[risc_v_profiles_rva]]: NVIDIA's embedded RISC-V cores do not follow the RVA application profiles — they use custom ISA subsets suited for firmware, not general compute.
- [[chips_alliance_governance]]: CHIPS Alliance governance is separate from NVIDIA's proprietary Falcon/GSP deployment; NVIDIA has not contributed its RISC-V firmware cores to open-source.
- [[qualcomm_riscv_ai]]: Like Qualcomm, NVIDIA is a major non-traditional adopter of RISC-V for control-path firmware rather than primary compute.

## Sources

- https://docs.kernel.org/gpu/nova/core/falcon.html
- https://download.nvidia.com/XFree86/Linux-x86_64/560.28.03/README/gsp.html
- https://deepwiki.com/NVIDIA/open-gpu-kernel-modules/4.3-gsp-gpu-system-processor
- https://www.techpowerup.com/291088/nvidia-unlocks-gpu-system-processor-gsp-for-improved-system-performance
