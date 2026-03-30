# Numerics and Correctness

## Scope

Use this guide whenever an optimization changes execution order, dtype behavior, kernels, or communication.

## General Rules

- Correctness comes before speed.
- Do not loosen tolerances just to force a pass.
- Do not silently change accumulation type, reduction order, or math mode.
- Explain any expected numerical drift from fusion, reordering, or reduced precision.

## Dtype-Aware Validation

Use workload-appropriate tolerances instead of one global threshold.

Typical guidance:

- FP32 pointwise or layout-preserving ops should be tight.
- FP32 reductions may need slightly looser tolerances if the order changes.
- FP16 and BF16 paths often need FP32 accumulation when numerically important.
- TF32 should match the intended baseline policy or be declared as a change.

If the repository defines official tolerances, use them instead of inventing new ones.

## Training Validation

When training is in scope, validate more than the forward pass:

- forward output agreement
- backward gradient agreement
- short-run loss behavior over multiple optimizer steps
- absence of new NaNs, Infs, or divergence

Useful tools include:

- `gradcheck` on reduced problems when it applies
- finite-difference checks for custom gradients
- side-by-side comparisons against the reference implementation

## Distributed Validation

For multi-GPU paths, also verify:

- collective semantics
- global-batch equivalence
- changed nondeterminism from floating-point reduction order
- correctness of overlap scheduling and stream dependencies

## Release Checklist

Before declaring success, confirm:

- representative shapes pass correctness checks
- unsupported shapes or dtypes fail clearly or fall back clearly
- benchmarks and correctness were run with the same semantics
- the final summary documents any numerical tradeoffs
