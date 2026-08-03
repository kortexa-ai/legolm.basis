#!/usr/bin/env bash
# Paper 7 / research_plan Phase 3 v3: the two decisive pre-draft experiments.
#
#   ./run_decisive.sh router   Arm 1: task-conditioned router, lr x entropy grid
#   ./run_decisive.sh layer    Arm 2: layer-partitioned composition, seed 42
#   ./run_decisive.sh layer2   Arm 2, second seed (1042) if wall clock allows
#
# Budgets follow v1/v2 exactly (eval-tokens 32768, sensor-limit 64,
# max-eval-items 64, rank 4, target all, lr 1e-3, imu 600 / audio 1800 task
# steps, vision 300 text steps) so every number is directly comparable to
# results/lfm230m-disjoint-p2-20260803/compose-task-IAV-disjoint-768-audio1800-seed42.json,
# which is the registered full-layer comparator.
set -euo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

OUT="${OUT:-results/lfm230m-decisive-20260803}"
PY="${PY:-./.venv/bin/python}"
CKPT="hf:LiquidAI/LFM2.5-230M"
COMMON=(--checkpoint "${CKPT}" --eval-tokens 32768 --sensor-limit 64)

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
  echo "=== done ${name} $(date +%H:%M:%S) ==="
}

layer_arm() { # layer_arm <seed>
  local seed="$1"
  run "compose-task-IAV-layer-256-seed${seed}" compose-task "${COMMON[@]}" \
    --task-bricks imu,audio --context-bricks vision \
    --bridge basis-frozen-256 --allocation layer \
    --task-steps 600 --task-steps-per-brick audio=1800 --text-steps 300 \
    --merge-modes sum,mean \
    --conditions true,shuffled,random --max-eval-items 64 --seed "${seed}" \
    --log-csv "${OUT}/logs/compose-task-layer-seed${seed}.csv"
}

router_arm() { # router_arm <seed>
  local seed="$1"
  run "compose-task-IAV-disjoint-768-router-seed${seed}" compose-task "${COMMON[@]}" \
    --task-bricks imu,audio --context-bricks vision \
    --bridge basis-disjoint-768 --allocation disjoint \
    --task-steps 600 --task-steps-per-brick audio=1800 --text-steps 300 \
    --merge-modes sum \
    --gate-steps 600 \
    --gate-modes gate-oracle,gate-learned-lr-1,gate-task-lr-0.3,gate-task-lr-1,gate-task-lr-3,gate-task-lr-0.3-ent0.1,gate-task-lr-1-ent0.1,gate-task-lr-3-ent0.1 \
    --conditions true --max-eval-items 64 --seed "${seed}" \
    --log-csv "${OUT}/logs/compose-task-router-seed${seed}.csv"
}

case "${1:-layer}" in
router)
  # Arm 1: the registered sweet spot. v2 swept the router lr with a FEATURE-ONLY
  # router and swept the balance weight with a feature-only router, but never
  # gave the task-conditioned router anything but the saturating 10x lr. Grid is
  # lr in {3e-4, 1e-3, 3e-3} x entropy bonus in {none, 0.1}. gate-learned-lr-1
  # rides along as the null: with leak-free pools its input distribution is
  # identical across tasks, so a constant IS its optimum.
  router_arm 42
  ;;
router2)
  # Added mid-session after arm 1 PASSED on seed 42: a one-seed pass on a
  # two-task setup is exactly what phase 2 flagged as unrealistically easy, so
  # the replicate is what makes the constructive claim reportable.
  router_arm 1042
  ;;
router-seed)
  # Added after the seed-1042 replicate REVERSED the seed-42 pass (the router
  # collapsed onto IMU in all six cells). With the two registered seeds split
  # 1-1, the reportable quantity is no longer "does it pass" but "how often
  # does it escape collapse", so further seeds are run to estimate that rate.
  router_arm "${2:?router-seed needs a seed}"
  ;;
layer)
  # Arm 2: disjoint LAYER SETS instead of disjoint coefficient slices. Each
  # brick gets its own 256-row frozen basis over its own contiguous block of the
  # flat LoRA vector (imu 0-4, audio 5-8, vision 9-13 on LFM2.5-230M), so
  # cos(merged, own) restricted to a brick's own sites is exactly 1.0 while the
  # global cosine falls to ~0.45. Full controls.
  layer_arm 42
  ;;
layer2)
  layer_arm 1042
  ;;
*)
  echo "usage: $0 {router|router2|layer|layer2}" >&2
  exit 2
  ;;
esac

echo "DONE ${1:-layer} $(date)"
