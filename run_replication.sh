#!/usr/bin/env bash
# Driver loop for the harness v2 replication test: run research sessions
# against varied RISC-V AI accelerator queries until wiki/_pages reaches
# 100 pages (same stopping criterion as the original research/riscv-ai-accelerator
# run), or the query list is exhausted.
set -uo pipefail
cd "$(dirname "$0")"
source subagent_env_setup.sh

TARGET_PAGES=100
LOGFILE="replication_run.log"

queries=(
  "T-Head XuanTie C908 C910 RISC-V AI core"
  "SiFive Intelligence X280 vector processor AI"
  "RISC-V Vector Extension RVV 1.0 intrinsics compiler"
  "K230 Kendryte KPU edge AI SoC RISC-V"
  "Tenstorrent Grayskull Wormhole RISC-V AI chip"
  "RISC-V matrix extension MTE IME proposal"
  "MLIR xDSL RISC-V vector codegen GEMM"
  "LLVM RISC-V vector backend autovectorization"
  "SpacemiT K1 X60 RISC-V AI SoC"
  "Sophon SG2042 RISC-V HPC many-core"
  "XiangShan RISC-V out-of-order processor vector"
  "PULP platform RISC-V edge AI accelerator"
  "Allwinner D1 T-Head C906 RISC-V AI"
  "RISC-V AI accelerator benchmark TOPS per watt comparison"
  "RVME RISC-V matrix engine extension design"
  "Rockchip RK3588 NPU AI benchmark"
  "RISC-V GEMM kernel optimization hand-tuned"
  "OpenGEMM RISC-V generic micro-kernel template"
  "RISC-V LLM inference llama.cpp RVV"
  "TVM IREE RISC-V compiler AI deployment"
  "Andes NX27V AX45MPV RISC-V vector core"
  "Ventana Veyron RISC-V server AI"
  "Esperanto ET-SoC-1 RISC-V AI accelerator"
  "RISC-V custom instruction extension SIMD DSP accelerator design"
  "RISC-V AI accelerator power efficiency TOPS per watt"
  "T-Head XuanTie SHL heterogeneous library HHB toolchain"
  "RISC-V object detection YOLO edge inference benchmark"
  "RISC-V robotics autonomous driving embedded vision SoC"
  "RISC-V AI accelerator wafer scale chiplet interconnect UCIe"
  "XuanTie C920 Sophon SG2042 HPC benchmark"
  "RISC-V AI accelerator memory bandwidth HBM DDR chiplet"
  "RISC-V verification formal methods hardware fuzzing"
  "RISC-V speech recognition audio ML inference embedded"
  "GCC Clang RISC-V vector autovectorization compiler benchmark"
  "RISC-V AI accelerator quantization INT8 FP16 kernel"
  "RISC-V open source hardware governance foundation"
  "Semidynamics Tensor Unit RISC-V AI core"
  "StarFive VisionFive JH7110 RISC-V AI SoC"
  "RISC-V AI accelerator FPGA prototype dataflow"
  "MobileNetV2 RISC-V NPU benchmark deployment"
  "RISC-V AI accelerator sparse DNN FPGA extension"
  "RISC-V vector memory architecture shift network"
  "RISC-V AI SoC automotive functional safety ISO 26262"
  "RISC-V AI accelerator design space edge vs server vs HPC"
)

for q in "${queries[@]}"; do
  count=$(find wiki/_pages -name '*.md' ! -name '.gitkeep' | wc -l)
  echo "[$(date -u +%FT%TZ)] page_count=$count query=\"$q\"" | tee -a "$LOGFILE"
  if [ "$count" -ge "$TARGET_PAGES" ]; then
    echo "[$(date -u +%FT%TZ)] TARGET REACHED: $count pages >= $TARGET_PAGES, stopping." | tee -a "$LOGFILE"
    break
  fi
  python3 tools/orchestrator.py research --query "$q" --max-candidates 10 --max-new-pages 6 --depth shallow \
    >> "$LOGFILE" 2>&1
  git add -A wiki/ CLAUDE.md >> "$LOGFILE" 2>&1
  git commit -q -m "research | $q" >> "$LOGFILE" 2>&1 || true
done

final_count=$(find wiki/_pages -name '*.md' ! -name '.gitkeep' | wc -l)
echo "[$(date -u +%FT%TZ)] DONE. final page_count=$final_count" | tee -a "$LOGFILE"
