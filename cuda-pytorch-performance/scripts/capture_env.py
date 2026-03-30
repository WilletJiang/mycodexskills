#!/usr/bin/env python3
"""Capture a concise environment snapshot for CUDA and PyTorch performance work."""

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

    cuda_available = bool(torch.cuda.is_available())
    torch_info: dict[str, Any] = {
        "version": getattr(torch, "__version__", None),
        "cuda_runtime": getattr(torch.version, "cuda", None),
        "git_version": getattr(torch.version, "git_version", None),
        "cuda_available": cuda_available,
        "cudnn_available": bool(torch.backends.cudnn.is_available()),
        "cudnn_version": torch.backends.cudnn.version(),
        "allow_tf32_matmul": bool(torch.backends.cuda.matmul.allow_tf32),
        "allow_tf32_cudnn": bool(torch.backends.cudnn.allow_tf32),
    }

    if cuda_available:
        devices = []
        for index in range(torch.cuda.device_count()):
            props = torch.cuda.get_device_properties(index)
            devices.append(
                {
                    "index": index,
                    "name": props.name,
                    "capability": f"{props.major}.{props.minor}",
                    "total_memory_bytes": props.total_memory,
                    "multi_processor_count": props.multi_processor_count,
                }
            )
        torch_info["devices"] = devices

    return torch_info


def collect_nvidia_smi() -> dict[str, Any] | None:
    nvidia_smi = shutil.which("nvidia-smi")
    if not nvidia_smi:
        return None

    gpu_query = run_command(
        [
            nvidia_smi,
            "--query-gpu=index,name,driver_version,memory.total,pci.bus_id",
            "--format=csv,noheader",
        ]
    )
    summary = run_command([nvidia_smi])
    return {"query": gpu_query, "summary": summary}


def collect_topology() -> dict[str, Any]:
    topology: dict[str, Any] = {}

    if shutil.which("lscpu"):
        topology["lscpu"] = run_command(["lscpu"])
    if shutil.which("numactl"):
        topology["numactl_hardware"] = run_command(["numactl", "--hardware"])
    if shutil.which("nvidia-smi"):
        topology["nvidia_smi_topo"] = run_command(["nvidia-smi", "topo", "-m"])

    return topology


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

    topology = collect_topology()
    if topology:
        snapshot["topology"] = topology

    return snapshot


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Capture a JSON snapshot of CUDA, PyTorch, and topology facts."
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
