#!/usr/bin/env bash
# Paper 7 / research_plan Phase 3 v1: constructive composition via disjoint
# coefficient blocks over a shared frozen orthonormal basis.
#
#   ./run_disjoint_v1.sh pilot     capacity pilot (minimum viable slice per modality)
#   ./run_disjoint_v1.sh main      the two composition arms (disjoint-sum vs shared)
#   ./run_disjoint_v1.sh bpb       secondary BPB-retention column (the v0 instrument)
#   ./run_disjoint_v1.sh seed 1042 repeat the disjoint arm at another seed
#
# House budget conventions (results/lfm230m-standard-20260701): eval-tokens
# 32768, sensor-limit 64, max-eval-items 64, rank 4, target all, lr 1e-3.
# Frozen bricks get 600 task steps / 300 text steps (the registered 2x law;
# v0's 150 steps/brick numbers are NOT reused).
set -euo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

OUT="${OUT:-results/lfm230m-disjoint-20260802}"
PY="${PY:-./.venv/bin/python}"
CKPT="hf:LiquidAI/LFM2.5-230M"
COMMON=(--checkpoint "${CKPT}" --eval-tokens 32768 --sensor-limit 64)
SEED="${2:-42}"
K_SLICE="${K_SLICE:-256}"
K_TOTAL="${K_TOTAL:-768}"

mkdir -p "${OUT}/logs"
export PYTHONUNBUFFERED=1

run() { # run <name> <args...>
  local name="$1"; shift
  if [[ -s "${OUT}/${name}.json" ]]; then
    echo "=== skip ${name} (exists) ==="
    return
  fi
  echo "=== ${name} $(date +%H:%M:%S) ==="
  "${PY}" -m src.cli "$@" > "${OUT}/${name}.json"
}

case "${1:-main}" in
pilot)
  # Minimum viable slice per modality: single-modality probes on the frozen
  # basis at width 128 vs 256, true condition only (controls are at chance in
  # every published frozen run). Rows of a Cholesky-whitened Gaussian basis are
  # exchangeable, so a width-w slice at offset 0 stands in for any offset.
  for width in 128 256; do
    for modality in imu audio; do
      run "pilot-task-${modality}-frozen-${width}" task-eval \
        --modality "${modality}" --checkpoint "${CKPT}" \
        --bridge "basis-frozen-${width}" --steps 600 --max-eval-items 64 \
        --conditions true --seed "${SEED}"
    done
  done
  ;;
main)
  # Arm A: disjoint slices, k_total = 3 * K_SLICE, merged by sum and by mean.
  run "compose-task-IAV-disjoint-${K_TOTAL}-seed${SEED}" compose-task "${COMMON[@]}" \
    --task-bricks imu,audio --context-bricks vision \
    --bridge "basis-disjoint-${K_TOTAL}" --allocation disjoint \
    --task-steps 600 --text-steps 300 --merge-modes sum,mean \
    --max-eval-items 64 --seed "${SEED}" \
    --log-csv "${OUT}/logs/compose-task-disjoint-seed${SEED}.csv"
  # Arm B: same bricks, same frozen rows, but every brick writes all K_SLICE
  # coordinates (the v0 shared-basis regime) — the mean-merge baseline.
  run "compose-task-IAV-shared-${K_SLICE}-seed${SEED}" compose-task "${COMMON[@]}" \
    --task-bricks imu,audio --context-bricks vision \
    --bridge "basis-frozen-${K_SLICE}" --allocation shared \
    --task-steps 600 --text-steps 300 --merge-modes sum,mean \
    --max-eval-items 64 --seed "${SEED}" \
    --log-csv "${OUT}/logs/compose-task-shared-seed${SEED}.csv"
  ;;
bpb)
  # Secondary column, for continuity with the v0 table only.
  run "compose-IAV-disjoint-${K_TOTAL}-seed${SEED}" composition "${COMMON[@]}" \
    --bricks imu,audio,vision --bridge "basis-disjoint-${K_TOTAL}" --allocation disjoint \
    --steps-per-brick 300 --merge-modes mean,sum --seed "${SEED}" \
    --log-csv "${OUT}/logs/compose-bpb-disjoint-seed${SEED}.csv"
  run "compose-IAV-shared-${K_SLICE}-seed${SEED}" composition "${COMMON[@]}" \
    --bricks imu,audio,vision --bridge "basis-frozen-${K_SLICE}" --allocation shared \
    --steps-per-brick 300 --merge-modes mean,sum --seed "${SEED}" \
    --log-csv "${OUT}/logs/compose-bpb-shared-seed${SEED}.csv"
  ;;
seed)
  run "compose-task-IAV-disjoint-${K_TOTAL}-seed${SEED}" compose-task "${COMMON[@]}" \
    --task-bricks imu,audio --context-bricks vision \
    --bridge "basis-disjoint-${K_TOTAL}" --allocation disjoint \
    --task-steps 600 --text-steps 300 --merge-modes sum,mean \
    --max-eval-items 64 --seed "${SEED}" \
    --log-csv "${OUT}/logs/compose-task-disjoint-seed${SEED}.csv"
  ;;
*)
  echo "usage: $0 {pilot|main|bpb|seed <seed>}" >&2
  exit 2
  ;;
esac

echo "DONE ${1:-main} $(date)"
