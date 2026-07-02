---
canonical_name: HHB MobileNetV2 C908 Compilation
aliases:
- HHB compilation for C908
- K230 HHB model compilation
subtype: null
hardware_targets:
- XuanTie C908
- K230
workloads:
- MobileNetV2 (ONNX)
datatypes:
- INT8
metrics: []
toolchains:
- HHB 2.2.35
- TVM (underlying)
- Docker
constraints:
- RISC-V Vector Extension 1.0
- K230 platform
- hhb-2.2.35 docker image
- Docker environment required
evidence_strength: reported
tags:
- compilation
- model deployment
- HHB
- C908
- K230
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/1b8d62580955e804.md
- https://www.kendryte.com/k230/en/v1.7/02_applications/tutorials/K230_AI_in_Action_HHB_Neural_Network_Model_Deployment_Tool.html
source_url: https://www.kendryte.com/k230/en/v1.7/02_applications/tutorials/K230_AI_in_Action_HHB_Neural_Network_Model_Deployment_Tool.html
fetched_at: '2026-07-02T06:12:25.049872+00:00'
type: optimization_recipe
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# HHB MobileNetV2 C908 Compilation

This recipe describes the process of compiling an ONNX-format MobileNetV2 model for execution on the XuanTie C908 core found in the Canaan Kendryte K230 SoC, using the T-Head HHB toolset version 2.2.35. The transformation requires a Docker environment containing the HHB image, and adapts a C906 board configuration to the C908 target by modifying the `--board` parameter and adding quantization-related options. The result is a C-based binary that can be cross-compiled with the K230 RTT toolchain and run on the board. This recipe is documented as a reported procedure with no measured performance data, serving as a starting point for deployment rather than an optimization with quantified speedup.

## Key Claims

- HHB successfully compiles MobileNetV2 ONNX model for the C908 target when the board configuration is changed from c906 to c908.
- The compilation includes quantization using scheme `int8_asym_w_sym` with a single calibration image (`persian_cat.jpg`).
- The full compilation pipeline involves model import, quantization, optimization, conversion to csinn, operator fusion, operator split, and layout conversion.
- Different models may require different HHB parameters; users should consult T-Head or run `hhb -h`.

## Transformation

- Prerequisites:
  - Local PC with Docker installed.
  - HHB docker image version 2.2.35 (tar archive downloaded from official source).
  - MobileNetV2 ONNX model file (mobilenetv2-12.onnx).
  - A calibration image (e.g., persian_cat.jpg) for quantization.
  - Understanding of HHB parameters or willingness to consult T-Head.
- Steps:
  1. Extract and load the HHB docker image: `tar xzf hhb-2.2.35.docker.tar.gz && cd hhb-2.2.35.docker/ && docker load < hhb.2.2.35.img.tar && ./start_hhb.sh`.
  2. Inside the container, copy the C906 example folder to create a C908 folder: `cp -a /home/example/c906 /home/example/c908`.
  3. Navigate to the ONNX MobileNetV2 example: `cd /home/example/c908/onnx_mobilenetv2/`.
  4. Modify `run.sh`:
     - Change `--board c906` to `--board c908`.
     - Add calibration set parameter: `-cd persian_cat.jpg`.
     - Add quantization scheme: `--quantization-scheme "int8_asym_w_sym"`.
     - Ensure `--fuse-conv-relu` is present for operator fusion.
  5. Execute `./run.sh` to start compilation. The tool will output logs for each stage and produce C code or binaries.
- Expected effect:
  - Generation of C code or executable binary targeted at the C908 core, optimized with INT8 asymmetric quantization for weights (symmetric) and activations (asymmetric).
- Failure modes:
  - Missing calibration data may lead to quantization failure.
  - Incorrect `--board` parameter results in compilation for the wrong target architecture, potentially causing runtime errors.
  - Some models may require different quantization schemes or additional pre-processing steps.
- Measurements:
  - No quantitative performance measurements are provided in the source documentation. The output is a compiled binary ready for execution; actual performance depends on the model and runtime environment.

## Relationships

- The recipe is specific to the [[hhb]] toolset and targets the [[k230]] hardware platform, which integrates the XuanTie C908 core with RISC-V Vector Extension 1.0.
- The compiled output is intended to be cross-compiled with the K230 RTT toolchain and run on the board, complementing the workflow described in the K230 hardware target page.
- This compilation procedure is a prerequisite for obtaining benchmark results on the C908 for MobileNetV2; no benchmark page currently exists for this combination.

## Sources

- https://www.kendryte.com/k230/en/v1.7/02_applications/tutorials/K230_AI_in_Action_HHB_Neural_Network_Model_Deployment_Tool.html
