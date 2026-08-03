#!/usr/bin/env bash
# Paper 7 / research_plan Phase 3 v2: the follow-ups registered when v1's
# disjoint-sum gate failed in all twelve cells, plus the constructive pivot
# (input-conditioned gating).
#
#   ./run_disjoint_p2.sh seeds      seed completion (disjoint s2042, shared s1042/s2042)
#   ./run_disjoint_p2.sh audiopower audio single at 1800 steps, then its merged cells
#   ./run_disjoint_p2.sh pairwise   2-way merges: does damage scale with brick COUNT?
#   ./run_disjoint_p2.sh gate       the gated arm (oracle ceiling vs learned routers)
#   ./run_disjoint_p2.sh gate2      the same arm with a load-balanced router
#   ./run_disjoint_p2.sh dose       beta-attenuated merges: retention vs cos(merged, own)
#
# Budgets follow v1 exactly (eval-tokens 32768, sensor-limit 64, max-eval-items
# 64, rank 4, target all, lr 1e-3, 600 task steps / 300 text steps) so every
# number is directly comparable to results/lfm230m-disjoint-20260802.
# alpha-norm / alpha-rsqrtn ride along on the seed runs for free: they are
# eval-side rescalings of the same trained bricks.
set -euo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

OUT="${OUT:-results/lfm230m-disjoint-p2-20260803}"
PY="${PY:-./.venv/bin/python}"
CKPT="hf:LiquidAI/LFM2.5-230M"
COMMON=(--checkpoint "${CKPT}" --eval-tokens 32768 --sensor-limit 64)
MERGES="${MERGES:-sum,mean,alpha-norm,alpha-rsqrtn}"

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

three_way() { # three_way <arm> <bridge> <allocation> <seed>
  local arm="$1" bridge="$2" allocation="$3" seed="$4"
  run "compose-task-IAV-${arm}-seed${seed}" compose-task "${COMMON[@]}" \
    --task-bricks imu,audio --context-bricks vision \
    --bridge "${bridge}" --allocation "${allocation}" \
    --task-steps 600 --text-steps 300 --merge-modes "${MERGES}" \
    --max-eval-items 64 --seed "${seed}" \
    --log-csv "${OUT}/logs/compose-task-${arm}-seed${seed}.csv"
}

case "${1:-seeds}" in
seeds)
  # Follow-up 1: bring disjoint-768 to 3 seeds and shared-256 to 3.
  three_way "disjoint-768" "basis-disjoint-768" disjoint 2042
  three_way "shared-256" "basis-frozen-256" shared 1042
  three_way "shared-256" "basis-frozen-256" shared 2042
  ;;
audiopower)
  # Follow-up 2: audio singles at 600 frozen steps score 2-8/64 against a 1/50
  # chance rate, so audio's retention ratio is meaningless. Check the single
  # first (cheap), then rerun its merged cells with audio at 1800 steps.
  # Conditions are restricted to `true`: the controls sit at chance in every
  # frozen run published so far, and `others_only` (the load-bearing control)
  # does not depend on the measured brick's condition.
  run "power-task-audio-frozen-256-s1800" task-eval \
    --modality audio --checkpoint "${CKPT}" \
    --bridge basis-frozen-256 --steps 1800 --max-eval-items 64 \
    --conditions true,no_bridge --seed 42
  run "compose-task-IAV-disjoint-768-audio1800-seed42" compose-task "${COMMON[@]}" \
    --task-bricks imu,audio --context-bricks vision \
    --bridge basis-disjoint-768 --allocation disjoint \
    --task-steps 600 --task-steps-per-brick audio=1800 --text-steps 300 \
    --merge-modes "${MERGES}" --conditions true \
    --max-eval-items 64 --seed 42 \
    --log-csv "${OUT}/logs/compose-task-audio1800-seed42.csv"
  ;;
pairwise)
  # Follow-up 3: does the damage scale with the NUMBER of foreign bricks or
  # with the presence of any? Same 256-wide slices as the 3-way arm
  # (basis-disjoint-512 = 2 x 256), one seed, true condition only. Audio runs
  # at the 1800 steps follow-up 2 showed it needs, so these rows are directly
  # comparable to compose-task-IAV-disjoint-768-audio1800-seed42 (the 2-foreign
  # reference with the same per-brick budgets).
  run "compose-task-IA-disjoint-512-seed42" compose-task "${COMMON[@]}" \
    --task-bricks imu,audio --context-bricks "" \
    --bridge basis-disjoint-512 --allocation disjoint \
    --task-steps 600 --task-steps-per-brick audio=1800 --text-steps 300 \
    --merge-modes "${MERGES}" \
    --conditions true --max-eval-items 64 --seed 42 \
    --log-csv "${OUT}/logs/compose-task-IA-seed42.csv"
  run "compose-task-IV-disjoint-512-seed42" compose-task "${COMMON[@]}" \
    --task-bricks imu --context-bricks vision \
    --bridge basis-disjoint-512 --allocation disjoint \
    --task-steps 600 --text-steps 300 --merge-modes "${MERGES}" \
    --conditions true --max-eval-items 64 --seed 42 \
    --log-csv "${OUT}/logs/compose-task-IV-seed42.csv"
  run "compose-task-AV-disjoint-512-seed42" compose-task "${COMMON[@]}" \
    --task-bricks audio --context-bricks vision \
    --bridge basis-disjoint-512 --allocation disjoint \
    --task-steps 600 --task-steps-per-brick audio=1800 --text-steps 300 \
    --merge-modes "${MERGES}" \
    --conditions true --max-eval-items 64 --seed 42 \
    --log-csv "${OUT}/logs/compose-task-AV-seed42.csv"
  ;;
gate)
  # Follow-up 5 (the constructive pivot): per-brick input-conditioned gating
  # over the coefficient heads. gate-oracle is the hard one-hot ceiling;
  # gate-learned is a softmax router on the concatenated brick features;
  # gate-task additionally sees which task is being asked.
  run "compose-task-IAV-disjoint-768-gate-seed42" compose-task "${COMMON[@]}" \
    --task-bricks imu,audio --context-bricks vision \
    --bridge basis-disjoint-768 --allocation disjoint \
    --task-steps 600 --text-steps 300 --merge-modes sum \
    --gate-steps 600 --gate-modes gate-oracle,gate-learned,gate-task \
    --conditions true,shuffled --max-eval-items 64 --seed 42 \
    --log-csv "${OUT}/logs/compose-task-gate-seed42.csv"
  ;;
gate2)
  # Follow-up 7: the same gated arm with a load-balanced router, and with audio
  # at the 1800 steps it needs, so that both experts are worth routing to.
  run "compose-task-IAV-disjoint-768-gate2-seed42" compose-task "${COMMON[@]}" \
    --task-bricks imu,audio --context-bricks vision \
    --bridge basis-disjoint-768 --allocation disjoint \
    --task-steps 600 --task-steps-per-brick audio=1800 --text-steps 300 \
    --merge-modes sum \
    --gate-steps 600 --gate-modes gate-oracle,gate-learned,gate-task,gate-balanced \
    --gate-balance-weight 0.1 \
    --conditions true --max-eval-items 64 --seed 42 \
    --log-csv "${OUT}/logs/compose-task-gate2-seed42.csv"
  ;;
gate3)
  # Follow-up 8: sweep the load-balancing weight inside one run. Training the
  # bricks costs ~16 min; each additional router costs ~42 s, so the sweep is
  # nearly free once the run is up.
  run "compose-task-IAV-disjoint-768-gate3-seed42" compose-task "${COMMON[@]}" \
    --task-bricks imu,audio --context-bricks vision \
    --bridge basis-disjoint-768 --allocation disjoint \
    --task-steps 600 --task-steps-per-brick audio=1800 --text-steps 300 \
    --merge-modes sum \
    --gate-steps 600 \
    --gate-modes gate-oracle,gate-learned,gate-balanced-0.5,gate-balanced-2,gate-balanced-8 \
    --conditions true --max-eval-items 64 --seed 42 \
    --log-csv "${OUT}/logs/compose-task-gate3-seed42.csv"
  ;;
gate4)
  # Follow-up 9: the router learning rate, which arm 5 set to 10x the bridge lr
  # precisely so a failure could not be blamed on the optimizer -- and which the
  # lambda sweep implicates as the cause of the saturation.
  run "compose-task-IAV-disjoint-768-gate4-seed42" compose-task "${COMMON[@]}" \
    --task-bricks imu,audio --context-bricks vision \
    --bridge basis-disjoint-768 --allocation disjoint \
    --task-steps 600 --task-steps-per-brick audio=1800 --text-steps 300 \
    --merge-modes sum \
    --gate-steps 600 \
    --gate-modes gate-oracle,gate-learned,gate-lr-1,gate-lr-0.1,gate-lr-0.01 \
    --conditions true --max-eval-items 64 --seed 42 \
    --log-csv "${OUT}/logs/compose-task-gate4-seed42.csv"
  ;;
dose)
  # Follow-up 6: attenuate the foreign bricks by beta instead of swapping brick
  # sets, so cos(merged, own) sweeps continuously with everything else fixed.
  # beta-1 is exactly `sum`. Audio runs at 1800 steps so both probes have power.
  run "compose-task-IAV-disjoint-768-dose-seed42" compose-task "${COMMON[@]}" \
    --task-bricks imu,audio --context-bricks vision \
    --bridge basis-disjoint-768 --allocation disjoint \
    --task-steps 600 --task-steps-per-brick audio=1800 --text-steps 300 \
    --merge-modes beta-0.125,beta-0.25,beta-0.5,beta-0.75,sum \
    --conditions true --max-eval-items 64 --seed 42 \
    --log-csv "${OUT}/logs/compose-task-dose-seed42.csv"
  ;;
*)
  echo "usage: $0 {seeds|audiopower|pairwise|gate|gate2|gate3|gate4|dose}" >&2
  exit 2
  ;;
esac

echo "DONE ${1:-seeds} $(date)"
