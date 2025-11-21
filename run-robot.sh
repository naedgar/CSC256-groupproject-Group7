#!/usr/bin/env bash
set -euo pipefail
# Wrapper to run Robot with correct PYTHONPATH and virtualenv
# Usage: ./run-robot.sh [robot-args]

# Default venv path (adjust if your venv is elsewhere)
VENV_PATH="${VENV_PATH:-/Users/nateedgar/Documents/GitHub/CSC256Group}"

if [ -d "$VENV_PATH" ]; then
  # shellcheck disable=SC1091
  source "$VENV_PATH/bin/activate"
else
  echo "Warning: virtualenv not found at $VENV_PATH — proceeding without activating venv"
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

echo "Running Robot: output -> robot-reports/  (using --pythonpath .)"
robot --outputdir robot-reports --pythonpath . tests/robot/suites "$@"
