#!/usr/bin/env bash
set -euo pipefail

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  cat <<'EOF'
Usage: profile_nsys.sh OUTPUT_BASENAME -- command [args...]

Environment overrides:
  NSYS_TRACE        Trace domains. Default: cuda,nvtx,osrt,cublas,cudnn
  NSYS_SAMPLE       Sampling mode. Default: none
  NSYS_EXTRA_ARGS   Extra arguments appended before the command
EOF
  exit 0
fi

if [[ $# -lt 3 ]]; then
  echo "Usage: profile_nsys.sh OUTPUT_BASENAME -- command [args...]" >&2
  exit 1
fi

if ! command -v nsys >/dev/null 2>&1; then
  echo "nsys not found in PATH" >&2
  exit 2
fi

output_base="$1"
shift

if [[ "$1" != "--" ]]; then
  echo "Expected '--' before the profiled command" >&2
  exit 1
fi
shift

trace_domains="${NSYS_TRACE:-cuda,nvtx,osrt,cublas,cudnn}"
sample_mode="${NSYS_SAMPLE:-none}"

declare -a extra_args=()
if [[ -n "${NSYS_EXTRA_ARGS:-}" ]]; then
  # shellcheck disable=SC2206
  extra_args=(${NSYS_EXTRA_ARGS})
fi

exec nsys profile \
  --force-overwrite=true \
  --sample="${sample_mode}" \
  --trace="${trace_domains}" \
  --output "${output_base}" \
  "${extra_args[@]}" \
  "$@"
