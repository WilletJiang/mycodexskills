# Runtime Modes and Autograd

## Scope

Use this guide for inference-mode choices, gradient tracking, and optimizer reset behavior.

## Inference Basics

For inference, make sure the code uses both:

- `model.eval()`
- `torch.inference_mode()` when semantics allow it

`eval()` changes module behavior such as dropout and batch norm. `inference_mode()` disables autograd-related tracking more aggressively than `no_grad()`.

## When to Use no_grad Instead

Prefer `torch.no_grad()` when you need to avoid gradient tracking but still need behavior that `inference_mode()` would restrict.

## Training-Side Checks

During training, look for:

- accidental inference-only contexts wrapping training code
- unnecessary retention of tensors for backward
- optimizer reset patterns that spend time zeroing memory unnecessarily

If semantics allow it, `optimizer.zero_grad(set_to_none=True)` can reduce memory traffic and modestly improve performance.

## Decision Rule

For inference:

- default to `eval()`
- default to `inference_mode()`
- fall back to `no_grad()` only when needed

For training:

- do not disable autograd blindly
- inspect gradient-reset behavior and unnecessary tensor retention
