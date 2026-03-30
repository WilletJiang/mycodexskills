#!/usr/bin/env python3
"""Benchmark a Python statement with warmup and optional CUDA synchronization."""

from __future__ import annotations

import argparse
import json
import math
import statistics
import time
from typing import Any


def maybe_import_torch():
    try:
        import torch
    except Exception:
        return None
    return torch


TORCH = maybe_import_torch()


def synchronize_if_needed() -> None:
    if TORCH is None:
        return
    if TORCH.cuda.is_available():
        TORCH.cuda.synchronize()


def summarize(samples_ms: list[float]) -> dict[str, Any]:
    ordered = sorted(samples_ms)
    count = len(ordered)
    if count == 0:
        raise ValueError("no samples collected")

    p90_index = min(count - 1, math.ceil(0.9 * count) - 1)
    return {
        "count": count,
        "min_ms": min(ordered),
        "max_ms": max(ordered),
        "mean_ms": statistics.fmean(ordered),
        "median_ms": statistics.median(ordered),
        "p90_ms": ordered[p90_index],
        "stdev_ms": statistics.stdev(ordered) if count > 1 else 0.0,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Benchmark a Python statement with warmup iterations."
    )
    parser.add_argument("--setup", default="", help="Python code executed once before timing.")
    parser.add_argument("--stmt", required=True, help="Python statement to benchmark.")
    parser.add_argument("--warmup", type=int, default=20, help="Warmup iterations.")
    parser.add_argument("--iters", type=int, default=100, help="Timed iterations.")
    parser.add_argument("--label", default="benchmark", help="Label for output.")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of a plain-text summary.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    namespace: dict[str, Any] = {}

    if args.setup:
        exec(compile(args.setup, "<setup>", "exec"), namespace, namespace)

    statement = compile(args.stmt, "<stmt>", "exec")

    for _ in range(args.warmup):
        exec(statement, namespace, namespace)
    synchronize_if_needed()

    samples_ms: list[float] = []
    for _ in range(args.iters):
        synchronize_if_needed()
        start = time.perf_counter()
        exec(statement, namespace, namespace)
        synchronize_if_needed()
        samples_ms.append((time.perf_counter() - start) * 1000.0)

    result = {
        "label": args.label,
        "warmup": args.warmup,
        "iters": args.iters,
        "cuda_sync": bool(TORCH is not None and TORCH.cuda.is_available()),
        "summary": summarize(samples_ms),
    }

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        summary = result["summary"]
        print(
            (
                f"{args.label}: mean={summary['mean_ms']:.3f} ms, "
                f"median={summary['median_ms']:.3f} ms, "
                f"p90={summary['p90_ms']:.3f} ms, "
                f"stdev={summary['stdev_ms']:.3f} ms, "
                f"min={summary['min_ms']:.3f} ms, "
                f"max={summary['max_ms']:.3f} ms, "
                f"n={summary['count']}"
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
