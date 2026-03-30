# Portability and Architecture Targeting

## Scope

Use this guide when choosing architecture targets, feature gates, or fallbacks.

## Default Target Set

Unless the deployment fleet is known to be narrower, treat these as common modern targets:

- SM80 class systems such as A100
- SM89 class systems such as RTX 4090
- SM90 class systems such as H100

Prefer implementations that stay strong across this set instead of overfitting to one device.

## Practical Rules

- Do not hardcode a single architecture unless the deployment target is explicitly fixed.
- Prefer vendor-library paths when they already encapsulate architecture-specific tuning.
- Keep architecture-specific fast paths behind correct fallbacks.
- Validate launch configurations against register, shared-memory, and occupancy limits on the real targets.

When the environment is unknown, a common starting point is:

```bash
TORCH_CUDA_ARCH_LIST="${TORCH_CUDA_ARCH_LIST:-8.0;8.9;9.0}"
```

Narrow the list once the actual fleet is known.

## Feature Tiers

Organize implementations into tiers:

1. Portable baseline path
2. Preferred accelerated path for broadly supported features
3. Architecture-specialized path only when a measured win justifies the complexity

Never let an architecture-specialized path be the only correct path.

## Gating Strategy

Use compile-time guards such as `__CUDA_ARCH__` for architecture-specific code generation when appropriate. Use runtime capability checks for dispatch or launch choices that depend on the installed device.

Preserve:

- output semantics
- accumulation policy
- numerical contract
- fallback behavior on unsupported hardware

## Avoid Overfitting

Be cautious when a kernel only wins because one device has unusually generous register or shared-memory limits. A slightly less exotic kernel is often the right choice when it is robust across the target fleet and simpler to maintain.
