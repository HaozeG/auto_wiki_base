---
cold_start: true
constraints:
- RISC-V architecture
- liquid cooling
- 128 GB VRAM
- teraflop-class inference
- models up to 120B parameters
- open-source software stack
- starting at $9,999
- Q2 2026 availability
created: '2026-07-08'
hardware_targets:
- TT-QuietBox 2
- Blackhole
inbound_links: 0
scorecard:
  bridge_score: 0.8
  claim_density: 0.7
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://via.tt.se/pressmeddelande/4282452/tenstorrent-unveils-tt-quietboxtm-2-the-first-risc-v-ai-workstation-with-a-fully-open-source-stack-to-deliver-teraflop-class-inference?publisherId=3236991&lang=en
tags:
- Tenstorrent
- QuietBox
- RISC-V
- AI workstation
- open-source
toolchains:
- TT-Forge
- PyTorch
- TensorFlow
- ONNX
- JAX
- PaddlePaddle
type: hardware_target
updated: '2026-06-29'
---

# TT-QuietBox 2

The TT-QuietBox 2 is a desktop AI workstation developed by Tenstorrent, built on a RISC-V architecture and designed to deliver teraflop-class AI inference. It is the first commercially available RISC-V-based AI workstation with a fully open-source software stack, including the TT-Forge open-source AI compiler that can compile models from PyTorch, ONNX, TensorFlow, JAX, and PaddlePaddle directly to the hardware. The system features liquid cooling and 128 GB of VRAM, enabling it to run models up to 120 billion parameters. The TT-QuietBox 2 is based on the Tenstorrent Blackhole architecture and is available starting at $9,999 with global shipping in Q2 2026. The workstation represents a significant step toward open-source, RISC-V-based AI compute in a desktop form factor, competing with proprietary AI workstations based on x86 and GPU architectures.

## Key Claims

- First RISC-V-based AI workstation with a fully open-source software stack.
- Delivers teraflop-class AI inference performance.
- Includes 128 GB of VRAM, capable of running models up to 120 billion parameters.
- Powered by TT-Forge open-source AI compiler, supporting major deep learning frameworks: PyTorch, TensorFlow, ONNX, JAX, and PaddlePaddle.
- Liquid-cooled design for sustained performance in a desktop form factor.
- Priced starting at $9,999 and ships globally in Q2 2026.

## Optimization-Relevant Details

- ISA/profile: RISC-V (specific extensions and core count not disclosed; likely based on Blackhole architecture with Tensix cores).
- Vector/matrix/accelerator support: Presumably includes Tensix cores with tile-based matrix engines (based on Tenstorrent Blackhole lineage).
- Memory/cache/TLB/DMA: 128 GB VRAM (likely GDDR6 or HBM; exact type not specified).
- Compiler/toolchain support: TT-Forge as the primary compiler, supporting PyTorch, TensorFlow, ONNX, JAX, and PaddlePaddle. Additional toolchain details not provided in the press release.

## Relationships

- [[Tenstorrent_Grayskull_e150]] – Earlier Tenstorrent accelerator architecture, providing context for the evolution to the Blackhole-based QuietBox 2.
- [[Gemmini_Architecture]] – Another RISC-V-based DNN accelerator, highlighting different design choices for RISC-V AI hardware (systolic array vs. dataflow grid).

## Sources

- Tenstorrent press release (via via.tt.se): [TT-QuietBox 2 announcement](https://via.tt.se/pressmeddelande/4282452/tenstorrent-unveils-tt-quietboxtm-2-the-first-risc-v-ai-workstation-with-a-fully-open-source-stack-to-deliver-teraflop-class-inference?publisherId=3236991&lang=en)
- Additional coverage from GamesBeat, StorageReview, and other outlets (as cited in search snippets).
