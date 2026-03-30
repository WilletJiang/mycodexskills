---
name: latex-formula-polish
description: Beautify and stabilize LaTeX mathematical typesetting in `.tex` files. Use when Codex needs to condense multi-line equations, align `=`, `+`, `-`, `\le`, or similar symbols, fix formula-related `Overfull \hbox` issues, reorganize theorem/lemma displays, make parameter blocks or matrix lists more regular, or generally polish the visual layout of math without changing its meaning.
---

# LaTeX Formula Polish

## Overview

Polish LaTeX math by improving structure, alignment, and visual balance while preserving the mathematics exactly. Treat this as typesetting work first: reduce clutter, expose semantic groups, and make the page feel stable.

Read [references/patterns.md](references/patterns.md) when you need concrete layout patterns or example transformations.

## Workflow

1. Inspect the target formulas in the `.tex` source before editing.
2. Identify the actual defect:
   - too many short lines
   - symbols not aligned
   - visual center unstable
   - formula overflows the measure
   - parameter block or definition block looks ragged
3. Preserve mathematical meaning. Do not rename symbols, alter assumptions, or change numbering unless required by the formatting fix.
4. Rebuild the formula around a clear skeleton instead of nudging whitespace.
5. Compile when feasible and verify that the result is visually improved and free of new warnings.

## Core Rules

- Break lines by semantic groups, not by raw character count.
- Prefer one strong alignment spine over many local alignments.
- Keep outer operators on a clean vertical column when the expression is multi-line.
- Let continuation lines read as intentional continuations, not as leftovers.
- Use shorter lines to improve balance, but do not fragment aggressively.
- Prefer structural edits over spacing hacks.

## Choose The Right Environment

- Use `aligned` for most multi-line equations with one main alignment spine.
- Use `alignedat` for parameter grids or paired objects such as `C/A`, `S_1/S_2`, `R_1/R_2`.
- Use `split` when one numbered display needs controlled continuation but not multiple alignment blocks.
- Use `gathered` only when vertical stacking matters more than column alignment.
- Avoid `array` unless the content is truly tabular.

## Layout Heuristics

### Condense Without Hiding Structure

- Merge adjacent short terms when they share the same coefficient, denominator class, or logical role.
- Keep each line dense enough to feel purposeful, but short enough to scan in one glance.
- When reducing line count, group terms into visually meaningful pairs or blocks.

### Align Symbols Rigorously

- Put the main `=` on the alignment anchor.
- Align continuation `+`, `-`, `\le`, `\ge`, or similar leading symbols on the same anchor column when they are siblings in the same derivation.
- Prefer a shared `&` anchor like `&{}+` or `&{}\le` over manual spacing.
- Use `\phantom{=}` only when a continuation line should start exactly under the operator slot of the first line and a shared anchor alone is insufficient.

### Stabilize The Visual Center

- Avoid a layout where a lone minus line or short continuation line pulls the formula off-center.
- Put the dominant structural block on the first line after `=`.
- Move secondary nonlinear, stochastic, or residual terms to later lines.
- Keep sibling terms together so the eye sees blocks, not fragments.

### Fix Overfull Formula Lines

- First change breakpoints, not font size.
- Split paired definitions into stacked aligned lines instead of forcing them onto one row.
- Recast long inequalities as two or three aligned lines with a stable symbol spine.
- For parameter lists, convert long horizontal runs into grouped aligned blocks.
- Tighten excessive inter-column spacing before resorting to more invasive changes.

## Common Targets

### Model Equations

- Separate drift, diffusion, and jump terms into their own lines.
- Inside the drift, keep the main deterministic core together and place additive nonlinear terms on a controlled continuation line.

### Chains Of Inequalities Or Estimates

- Align the comparison symbols.
- Keep coefficient-heavy correction terms grouped by role.
- If a proof line contains storage or trigger terms, group them by sign and denominator structure.

### Definitions And Parameter Blocks

- Stack paired definitions such as `\Phi/\Psi` or `D_x/E_y`.
- Use `alignedat` for two-column parameter presentations.
- For matrices and `\operatorname{diag}(...)` lists, choose between a one-line display and a wrapped display based on actual page width, not habit.

## Verification

- Compile the document if practical.
- Check for formula-related `Overfull \hbox` warnings.
- Confirm that aligned symbols are truly column-aligned in source structure, not merely visually close.
- Confirm that equation numbering, labels, and references still work.
- Prefer local fixes. Do not introduce global settings unless repeated local issues justify them.

## Global Knobs

Use document-level adjustments only as secondary tools:

- `fleqn` can help when the document already uses flush-left displays.
- `\setlength{\emergencystretch}{...}` can reduce borderline overflow pressure.
- `\allowdisplaybreaks[1]` can help long derivations span pages more gracefully.

Do not add global knobs as a substitute for poor local line breaking.
