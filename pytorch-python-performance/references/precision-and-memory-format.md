# Precision and Memory Format

## Scope

Use this guide when dtype policy, AMP, or layout choices may unlock speed.

## Mixed Precision

Check whether the workload should use:

- BF16
- FP16
- AMP autocast
- TF32 where appropriate

This is often one of the highest-return PyTorch-level changes on GPU workloads.

## Validation Rule

Treat precision changes as performance experiments with correctness implications. Keep:

- the same task semantics
- representative validation checks
- clear reporting of the dtype policy you used

## AMP Checks

Look for:

- training or inference still running in full FP32 without need
- unnecessary casts inside the hot path
- modules forced back to FP32 because of awkward wrapper code
- missing `GradScaler` when FP16 training needs it

## Memory Format

For convolution-heavy models, consider whether `channels_last` is worth testing. It is not universal, but when it fits the model and backend path, it can be a clean PyTorch-level win.

## Built-In Fast Paths

Check whether the code can benefit from:

- larger or cleaner batching
- built-in attention fast paths
- less layout churn before core ops

Do not promise a fast path until the benchmark confirms it.
