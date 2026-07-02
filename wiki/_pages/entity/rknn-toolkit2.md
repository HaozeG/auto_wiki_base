---
canonical_name: RKNN-Toolkit2
aliases:
- RKNN
- RKNN software stack
- RKNPU toolkit
- Rockchip NPU toolkit
subtype: null
tags:
- AI inference
- model conversion
- Rockchip
- NPU
- toolkit
scorecard:
  novelty_delta: 0.7
  claim_density: 0.5
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.4
sources:
- raw/cache/226eb8c2b5748cd0.md
- https://github.com/rockchip-linux/rknn-toolkit2
source_url: https://github.com/rockchip-linux/rknn-toolkit2
fetched_at: '2026-07-02T11:11:05.209128+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# RKNN-Toolkit2

The RKNN software stack is a set of tools developed by Rockchip to enable deployment of trained AI models onto Rockchip SoCs featuring an NPU (Neural Processing Unit). The workflow consists of two main stages: model conversion on a PC host using RKNN-Toolkit2, which translates models from frameworks such as ONNX into the RKNN format; and inference on a target development board using the RKNN C API or Python API provided by the runtime components. The stack comprises RKNN-Toolkit2 for conversion, debugging, and performance evaluation; RKNN-Toolkit-Lite2 for Python-based deployment; the RKNN Runtime for C/C++ deployment; and the RKNPU kernel driver that interfaces with the NPU hardware. Supported hardware includes the RK3566/RK3568, RK3588, RK3562, and RV1103/RV1106 series, while older chips like the RK1808 and RK3399Pro use a separate toolkit. The toolkit is available on GitHub under the airockchip organization and is not compatible with the original RKNN-Toolkit.

## Key Claims

- The RKNN software stack helps users deploy AI models to Rockchip NPUs through model conversion on a host PC followed by inference on the target device.
- The stack consists of four components: RKNN-Toolkit2 (model conversion and evaluation on PC), RKNN-Toolkit-Lite2 (Python inference on device), RKNN Runtime (C/C++ inference on device), and the RKNPU kernel driver.
- Supported Rockchip SoCs include RK3566/RK3568, RK3588, RK3562, and RV1103/RV1106.
- RKNN-Toolkit2 is not compatible with the older RKNN-Toolkit used for RK1808/RV1109/RV1126/RK3399Pro.
- Version 1.6.0 supports ONNX models with opset 12–19, custom CPU and GPU operators, and optimizations for transformer networks, MatMul operations, and RV1106 initialization time.
- The toolkit supports Python 3.6–3.11 on Ubuntu 18.04 through 22.04.

## Relationships

- [[pulp-nn-optimization-recipe]]: Both are software stacks for deploying neural networks on AI accelerators, with PULP-NN targeting RISC-V-based PULP clusters and RKNN targeting Rockchip NPUs.
- [[tenstorrent-grayskull-e75-matmul-bf16-benchmark]]: Related as both involve AI inference acceleration, though on different hardware platforms.

## Sources

- [Original GitHub repository: rockchip-linux/rknn-toolkit2](https://github.com/rockchip-linux/rknn-toolkit2)
- [Active GitHub repository: airockchip/rknn-toolkit2](https://github.com/airockchip/rknn-toolkit2)
