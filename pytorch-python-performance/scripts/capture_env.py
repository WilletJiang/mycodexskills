#!/usr/bin/env python3
"""Capture a concise PyTorch runtime snapshot."""

from __future__ import annotations

import argparse
import json
import platform
import shutil
import subprocess
import sys
from typing import Any


def run_command(command: list[str]) -> dict[str, Any]:
    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        return {"ok": False, "error": str(exc)}

    return {
        "ok": completed.returncode == 0,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def maybe_import_torch() -> dict[str, Any] | None:
    try:
        import torch
    except Exception as exc:  # pragma: no cover - environment-dependent
        return {"import_error": str(exc)}

    torch_info: dict[str, Any] = {
        "version": getattr(torch, "__version__", None),
        "cuda_runtime": getattr(torch.version, "cuda", None),
        "git_version": getattr(torch.version, "git_version", None),
        "cuda_available": bool(torch.cuda.is_available()),
        "cudnn_available": bool(torch.backends.cudnn.is_available()),
        "cudnn_version": torch.backends.cudnn.version(),
        "num_threads": torch.get_num_threads(),
        "num_interop_threads": torch.get_num_interop_threads(),
    }

    if torch.cuda.is_available():
        devices = []
        for index in range(torch.cuda.device_count()):
            props = torch.cuda.get_device_properties(index)
            devices.append(
                {
                    "index": index,
                    "name": props.name,
                    "capability": f"{props.major}.{props.minor}",
                    "total_memory_bytes": props.total_memory,
                }
            )
        torch_info["devices"] = devices

    return torch_info


def collect_nvidia_smi() -> dict[str, Any] | None:
    nvidia_smi = shutil.which("nvidia-smi")
    if not nvidia_smi:
        return None
    return run_command([nvidia_smi, "-L"])


def build_snapshot() -> dict[str, Any]:
    snapshot: dict[str, Any] = {
        "python": {
            "version": sys.version,
            "executable": sys.executable,
        },
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "processor": platform.processor(),
        },
    }

    torch_info = maybe_import_torch()
    if torch_info is not None:
        snapshot["torch"] = torch_info

    nvidia_smi = collect_nvidia_smi()
    if nvidia_smi is not None:
        snapshot["nvidia_smi"] = nvidia_smi

    if shutil.which("lscpu"):
        snapshot["lscpu"] = run_command(["lscpu"])

    return snapshot


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Capture Python, PyTorch, CPU, and CUDA environment details."
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="JSON indentation level. Use 0 for compact output.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    snapshot = build_snapshot()
    indent = None if args.indent == 0 else args.indent
    print(json.dumps(snapshot, indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
