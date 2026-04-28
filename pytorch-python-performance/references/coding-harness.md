# PyTorch Coding-Time Harness

A performance-sensitive PyTorch change should leave behind an executable harness while the code is being written. The harness is the contract between implementation, correctness, and measurement.

## Minimum Harness Shape

Use the repository's existing layout when it has one. A practical harness usually has a small correctness entry point, a benchmark entry point, and one remote run recipe. The exact names can follow local conventions, but the roles must be present.

```text
tests or experiments
  correctness entry point for the changed path
  benchmark entry point for representative shapes
  remote GPU run script or documented command
  result file or log directory
```

The correctness path should compare the new implementation with the old implementation, a reference implementation, or a mathematical oracle. It should cover the normal shape, at least one edge shape, the intended dtype policy, and any randomness or masking behavior that affects semantics.

The benchmark path should construct inputs deterministically, warm up the path, synchronize CUDA timing when CUDA is available, report enough iterations for stable measurements, and separate setup time from measured time. For `torch.compile`, report compile overhead separately from steady-state execution unless the workload is long-lived enough that compile cost is irrelevant.

## Remote GPU Execution

When the local machine has no NVIDIA GPU, still create the harness locally and run CPU smoke tests. The remote GPU command should be concrete enough to execute later through SSH, Slurm, a container job, or the repository's experiment runner. Do not infer GPU performance from Mac CPU timing.

Capture the environment inside the GPU job, not only on the login shell. At minimum record the git revision, command line, Python version, PyTorch version, CUDA availability, GPU name, driver-visible CUDA version if available, dtype policy, shape matrix, batch size, and output log path.

## Coding Rules

Keep production code and harness changes synchronized. If a change introduces a new fast path, runtime mode, dtype mode, batch mode, compiled mode, or data pipeline mode, the harness must expose that mode explicitly. If a proposed optimization cannot be tested with a small deterministic harness, first reduce the workload until it can.

Keep benchmark inputs representative but small enough for iteration. Add a larger shape only after the small harness is correct. Record failures as useful outputs: graph breaks, recompilation, CUDA out-of-memory, numerical drift, data loader starvation, and host oversubscription are all harness findings.

## Reporting

Report results as a comparison against the baseline. Include correctness tolerance, shape and dtype coverage, timing metric, iteration count, device, command, and whether results came from local smoke execution or remote GPU execution. If the GPU run is pending, say so plainly and leave the command ready to run.
