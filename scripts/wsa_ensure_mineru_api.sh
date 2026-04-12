#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PORT="${WSA_MINERU_API_PORT:-18000}"
HOST="${WSA_MINERU_API_HOST:-0.0.0.0}"
SESSION="${WSA_MINERU_TMUX_SESSION:-mineru_api}"
CONDA_ENV="${WSA_MINERU_CONDA_ENV:-dpl}"
CONDA_BIN="${WSA_MINERU_CONDA_BIN:-$HOME/miniconda3/bin/conda}"
LOG_PATH="${WSA_MINERU_LOG_PATH:-$HOME/mineru_api.log}"

if ! command -v tmux >/dev/null 2>&1; then
  echo "tmux is required to keep MinerU API running on WSA." >&2
  exit 1
fi

if [ ! -x "${CONDA_BIN}" ]; then
  echo "conda is required to run MinerU inside ${CONDA_ENV}: ${CONDA_BIN} not found." >&2
  exit 1
fi

if command -v lsof >/dev/null 2>&1; then
  if lsof -iTCP:"${PORT}" -sTCP:LISTEN -n -P >/dev/null 2>&1; then
    echo "MinerU API already listening on ${HOST}:${PORT}"
    exit 0
  fi
fi

tmux has-session -t "${SESSION}" 2>/dev/null && tmux kill-session -t "${SESSION}"
mkdir -p "$(dirname "${LOG_PATH}")"

tmux new-session -d -s "${SESSION}" \
  "cd ${ROOT} && export MINERU_MODEL_SOURCE=local CUDA_VISIBLE_DEVICES=\${CUDA_VISIBLE_DEVICES:-0} CONDA_NO_PLUGINS=true && ${CONDA_BIN} run -n ${CONDA_ENV} mineru-api --host ${HOST} --port ${PORT} >> ${LOG_PATH} 2>&1"

sleep 6

if command -v lsof >/dev/null 2>&1 && ! lsof -iTCP:"${PORT}" -sTCP:LISTEN -n -P >/dev/null 2>&1; then
  echo "Failed to start MinerU API on ${HOST}:${PORT}. Recent log:" >&2
  sed -n '1,160p' "${LOG_PATH}" >&2 || true
  exit 1
fi

echo "MinerU API ready at http://127.0.0.1:${PORT}"
