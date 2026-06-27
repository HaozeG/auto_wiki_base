---
cold_start: false
created: '2025-07-17'
inbound_links: 0
scorecard:
  bridge_score: 0.5
  claim_density: 0.6
  hub_potential: 0.4
  novelty_delta: 0.9
  self_containedness: 0.5
sources:
- https://github.com/Arm-China/Compass_Apache_TVM/blob/main/NEWS.md
- https://github.com/Arm-China/Compass_Apache_TVM/blob/main/README.md
- https://gitee.com/Arm-China/Compass_Apache_TVM
tags:
- compiler
- neural-network
- open-source
- arm-china
- tvm
type: entity
updated: '2026-06-27'
---

# Compass Apache TVM

Compass Apache TVM is an enhanced fork of the Apache TVM deep learning compiler developed by Arm China. It is designed to provide quick support, optimization, and heterogeneous execution for a wide range of neural network (NN) models. Building on the Apache TVM foundation, Compass adds features such as a user-defined code generation guide, Relay annotation and partitioning for external compilers, and support for custom hardware accelerator backends through the VTA (Versatile Tensor Accelerator) framework. The project aims to streamline the deployment of neural networks across diverse hardware platforms, including custom accelerators and specialized instruction sets.

## Key Claims

- Compass Apache TVM is an enhanced version of Apache TVM by Arm China, focusing on rapid NN model support and optimization.
- It includes a "Bring Your Own Codegen Guide" (Part 2, PR #4718) to facilitate custom code generation.
- It provides Relay annotation and partitioning for external compilers (PR #4570), enabling integration with third-party compilation flows.
- It incorporates VTA as a customized accelerator backend and offers a custom hardware backend example.
- The project is hosted on GitHub (Arm-China/Compass_Apache_TVM) and mirrored on Gitee.

## Relationships

- [[ai_chip_export_controls]] – Because Compass Apache TVM is developed by Arm China, it is used in the context of Chinese AI chip development that is subject to export controls. The compiler may be employed to optimize models for domestic accelerators like Huawei’s Ascend series, which are directly impacted by U.S. restrictions.

## Sources

- GitHub repository NEWS.md: https://github.com/Arm-China/Compass_Apache_TVM/blob/main/NEWS.md
- GitHub repository README.md: https://github.com/Arm-China/Compass_Apache_TVM/blob/main/README.md
- Gitee repository: https://gitee.com/Arm-China/Compass_Apache_TVM
