---
cold_start: false
created: '2025-12-10'
inbound_links: 0
scorecard:
  bridge_score: 0.8
  claim_density: 0.7
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://github.com/RLC-Lab/riscv-ros2
tags:
- riscv
- ros2
- slam
- docker
- cross-compilation
- milk-v-meles
type: entity
updated: '2026-06-27'
---

# RISC-V ROS2 Docker Build System

The RISC-V ROS2 Docker Build System is an open-source project hosted on GitHub by RLC-Lab that provides a flexible, Docker-based build system designed to simplify the deployment of ROS 2 (Robot Operating System 2) and mainstream SLAM algorithms on RISC-V processor hardware. It handles the complexities of cross-compilation, enabling developers to build and run robotics applications without deep knowledge of RISC-V toolchains. The project targets the Milk-V Meles single-board computer based on the TH1520 RISC-V SoC, and supports ROS 2 Humble and Jazzy distributions. It has successfully ported Gmapping 2D LiDAR SLAM, LIO-SAM 3D LiDAR SLAM, and ORB-SLAM3 visual SLAM algorithms to run on RISC-V hardware, demonstrating that modern robotics middleware and perception stacks can operate on open-standard instruction set architectures.

## Key Claims

- The project provides a Docker-based build system using `docker buildx` for cross-compiling ROS 2 and SLAM algorithms for RISC-V targets.
- It supports cross-platform development on Linux, macOS, and Windows.
- Build scripts are optimized for Ubuntu and Debian target platforms with configurable Python versions.
- Successfully runs ROS 2 distributed communication between RISC-V devices and x86 PCs over a LAN.
- Ported and tested Gmapping (2D LiDAR) and LIO-SAM (3D LiDAR) SLAM algorithms.
- Ported ORB-SLAM3 visual SLAM algorithm.
- Developed and tested on Milk-V Meles (TH1520 SoC) running RevyOS (Debian-based), with host workstation Ubuntu 24.04 LTS and 128 GB RAM.
- Prebuilt Docker images are available for ROS 2 Humble and Jazzy on RISC-V.
- The project includes tutorials for setup, building, and running LiDAR and visual SLAM.
- Future work includes instruction-level parallel optimization, middleware communication tuning, OS scheduling improvements, and compiler toolchain optimization.

## Relationships

No existing wiki pages on RISC-V software, ROS 2, or SLAM are present in the current graph. This page serves as an initial entry point for connecting RISC-V hardware to robotics software.

## Sources

- GitHub repository: https://github.com/RLC-Lab/riscv-ros2
- README file (resource content provided in EvalManifest)
