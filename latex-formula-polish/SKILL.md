---
name: latex-formula-polish
description: Write and revise LaTeX mathematical content with a coding-time typesetting harness. Use when creating or editing theorem statements, lemmas, proofs, model equations, estimates, parameter blocks, aligned derivations, matrices, or formula-heavy .tex sections, especially when layout, equation numbering, references, Overfull hbox warnings, or PDF visual quality could be affected.
---

# LaTeX Formula Harness

Use this skill while writing or editing mathematical LaTeX, not only after the compiled PDF looks bad. Treat mathematical content and its typesetting harness as one deliverable: the source should preserve meaning, compile cleanly, avoid predictable overfull displays, and render with stable visual structure.

The goal is typesetting discipline, not mathematical rewriting. Preserve statements, notation, labels, numbering, assumptions, cross-references, and citation structure unless the user explicitly asks for mathematical changes. When a layout fix requires a local structural edit, keep the mathematical content equivalent and explain the change if it affects readability or reference structure.

## Harness Contract

Before editing formula-heavy text, identify the local compile command, the relevant `.tex` entry point, the edited labels, and the PDF pages likely to change. If the repository already has a Makefile, latexmk configuration, build script, or CI command, use that. If not, create no new build system unless needed; record the direct compile command that proves the edited section.

For substantial formula work, compile after the first meaningful edit and again at the end. Scan for undefined references, undefined citations, equation-numbering changes, formula-related `Overfull \hbox` warnings, and new LaTeX errors. When the final PDF exists, render or inspect the affected pages visually rather than relying only on log output.

Read `references/coding-harness.md` before writing or substantially revising formula-heavy LaTeX. Read `references/patterns.md` when concrete layout transformations are needed.

## Writing Workflow

Design the equation layout while writing the mathematics. Break formulas by semantic role, not by raw character count. Establish one clear alignment spine for derivations, inequalities, and estimates. Group terms by mathematical function: drift, diffusion, jump, residual, stochastic term, coefficient block, denominator class, or assumption family. Do not write a long horizontal display first and defer all line breaking to a later cleanup pass.

Choose environments deliberately. Use `aligned` for most multi-line displays with one main spine, `alignedat` for paired definitions and parameter grids, `split` for one numbered display with controlled continuation, and `gathered` when vertical stacking matters more than column alignment. Use `array` only for genuinely tabular mathematical content.

For theorem and proof sections, keep statement readability, proof flow, labels, and references stable. If a proof contains a long estimate, structure it as an argument with readable display blocks rather than a dense sequence of unplanned line breaks.

## Completion Standard

Finish with the source changes, compile command, warning summary, affected labels or equation numbers, visual inspection of affected PDF pages when available, and any remaining layout risk. A formula-heavy edit without a compile or visual check is incomplete unless the environment prevents verification, in which case state exactly what remains unverified.
