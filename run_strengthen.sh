#!/usr/bin/env bash
# Additional runs that raise the statistical power of the basis-mixture paper.
#
# Two things the first pass left thin:
#   1. The headline parity claim (dense vs trained basis-16 on the six-way IMU
#      probe) rested on three seeds each, with a per-seed spread wider than the
#      difference being claimed. This adds seeds 3042 and 4042.
#   2. The span threshold was bracketed at two points per task, never mapped.
#      This fills in k = 32, 48, 96, 128 with a frozen basis on both task
#      complexities, three seeds each, which is where the threshold lives.
#
# Run names follow the existing sweep convention so the renderer can look them
# up unchanged: task-<modality>-<bridge>[-s<steps>][-blr0][-seed<N>], with
# seed 42 carrying no suffix.
#
# Usage: ./run_strengthen.sh [output-dir]
set -euo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}"

OUT="${1:-results/lfm230m-strengthen}"
CKPT="hf:LiquidAI/LFM2.5-230M"
RUN=".venv/bin/paper-run"
mkdir -p "${OUT}"

# One run. Skips work that already has a result so the sweep is resumable.
emit() {
  local name="$1"; shift
  local target="${OUT}/${name}.json"
  if [[ -s "${target}" ]]; then
    echo "[skip] ${name}"
    return 0
  fi
  echo "[run ] ${name}"
  if ! "${RUN}" "$@" >"${target}.partial" 2>"${OUT}/${name}.err"; then
    echo "[FAIL] ${name} — see ${OUT}/${name}.err" >&2
    rm -f "${target}.partial"
    return 1
  fi
  mv "${target}.partial" "${target}"
}

seed_suffix() { [[ "$1" == "42" ]] && echo "" || echo "-seed$1"; }

echo "=== 1. Headline seeds: six-way IMU probe, dense vs trained basis-16"
for seed in 3042 4042; do
  emit "task-imu-dense$(seed_suffix "${seed}")" \
    task-eval --modality imu --checkpoint "${CKPT}" \
    --bridge dense --seed "${seed}" --steps 600
  emit "task-imu-basis-16$(seed_suffix "${seed}")" \
    task-eval --modality imu --checkpoint "${CKPT}" \
    --bridge basis-16 --seed "${seed}" --steps 600
done

echo "=== 2. Span map, frozen basis, six-way IMU (600 steps)"
for k in 32 48 96 128; do
  for seed in 42 1042 2042; do
    emit "task-imu-basis-${k}-blr0$(seed_suffix "${seed}")" \
      task-eval --modality imu --checkpoint "${CKPT}" \
      --bridge "basis-${k}" --basis-lr-scale 0 --seed "${seed}" --steps 600
  done
done

echo "=== 3. Span map, frozen basis, fifty-way audio (1200 steps)"
# 1200 steps matches the budget at which the published k=64 and k=256 frozen
# audio points were measured, so the new k values are comparable to them.
for k in 32 48 96 128; do
  for seed in 42 1042 2042; do
    emit "task-audio-basis-${k}-s1200-blr0$(seed_suffix "${seed}")" \
      task-eval --modality audio --checkpoint "${CKPT}" \
      --bridge "basis-${k}" --basis-lr-scale 0 --seed "${seed}" --steps 1200
  done
done

echo "=== done. $(ls -1 "${OUT}"/*.json 2>/dev/null | wc -l) result files in ${OUT}"
