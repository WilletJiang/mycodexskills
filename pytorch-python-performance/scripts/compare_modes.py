#!/usr/bin/env python3
"""Compare eager and optional torch.compile execution around the same callable."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare eager and compiled execution for the same call."
    )
    parser.add_argument("--setup", required=True, help="Python setup code.")
    parser.add_argument("--call", required=True, help="Callable expression, for example 'model(x)'.")
    parser.add_argument(
        "--compile-target",
        help="Name of the callable object in setup to wrap with torch.compile.",
    )
    parser.add_argument(
        "--compiled-call",
        help="Expression for the compiled variant. Defaults to replacing the compile target name in --call.",
    )
    parser.add_argument("--warmup", type=int, default=20, help="Warmup iterations.")
    parser.add_argument("--iters", type=int, default=100, help="Timed iterations.")
    parser.add_argument("--label", default="compare", help="Label for output.")
    return parser.parse_args()


def make_compiled_call(call: str, target_name: str, compiled_name: str) -> str:
    pattern = rf"\b{re.escape(target_name)}\b"
    updated, count = re.subn(pattern, compiled_name, call, count=1)
    if count == 0:
        raise ValueError(
            "Could not derive compiled call automatically. Pass --compiled-call explicitly."
        )
    return updated


def run_bench(setup: str, stmt: str, warmup: int, iters: int) -> dict[str, Any]:
    from pathlib import Path
    import sys

    script_path = (
        Path(__file__).resolve().parent / "bench_stmt.py"
    )
    completed = subprocess.run(
        [
            sys.executable,
            str(script_path),
            "--setup",
            setup,
            "--stmt",
            stmt,
            "--warmup",
            str(warmup),
            "--iters",
            str(iters),
            "--json",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def main() -> int:
    args = parse_args()

    eager_result = run_bench(args.setup, args.call, args.warmup, args.iters)
    results: dict[str, Any] = {
        "label": args.label,
        "eager": eager_result["summary"],
    }

    if args.compile_target:
        compiled_name = "__compiled_target"
        compile_setup = (
            args.setup
            + "\nimport torch\n"
            + f"{compiled_name} = torch.compile({args.compile_target})\n"
        )
        compiled_call = args.compiled_call or make_compiled_call(
            args.call, args.compile_target, compiled_name
        )
        try:
            compiled_result = run_bench(
                compile_setup,
                compiled_call,
                args.warmup,
                args.iters,
            )
        except subprocess.CalledProcessError as exc:
            results["compiled_error"] = {
                "returncode": exc.returncode,
                "stdout": (exc.stdout or "").strip(),
                "stderr": (exc.stderr or "").strip(),
            }
        else:
            results["compiled"] = compiled_result["summary"]
            eager_mean = eager_result["summary"]["mean_ms"]
            compiled_mean = compiled_result["summary"]["mean_ms"]
            if compiled_mean > 0:
                results["compiled_speedup_pct"] = ((eager_mean / compiled_mean) - 1.0) * 100.0

    print(json.dumps(results, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
