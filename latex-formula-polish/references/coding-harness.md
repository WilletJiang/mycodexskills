# LaTeX Formula Coding-Time Harness

A formula-heavy LaTeX edit should carry its verification path while the text is being written. The harness is the connection between mathematical meaning, source structure, compiler output, and rendered PDF quality.

## Minimum Harness

Identify the build entry point before editing. Prefer the repository's existing command, such as `latexmk`, `make`, an arXiv build script, or a journal template command. If no command exists, use the smallest direct compile command that can build the document.

Record the affected source file, nearby theorem or lemma names, edited labels, expected equation numbering behavior, and pages likely to change. If the document is large, compile the full document at the final gate even when local source inspection is enough for intermediate work.

## Log Checks

After meaningful formula edits, inspect the build log for LaTeX errors, undefined references, undefined citations, multiply defined labels, missing files, and formula-related `Overfull \hbox` warnings. An overfull warning is not automatically a failure, but a new or worsened warning near edited math must be investigated.

Do not hide log output that would reveal real errors. If the build is noisy before the edit, distinguish pre-existing warnings from new warnings introduced by the change.

## Visual Checks

Log checks cannot prove mathematical layout quality. When a PDF is available, inspect affected pages. For local visual inspection, render pages with the repository's existing tool or a standard PDF renderer. Check alignment spines, equation centering, line breaks, theorem statement spacing, page breaks through long derivations, and whether labels, captions, or surrounding prose collide with displays.

For multi-line equations, verify the source alignment structure, not only the apparent screen position. Good visual alignment should come from `&` anchors, environment choice, and semantic grouping rather than manual spacing.

## Source Rules

Write formulas in their final intended structure from the start. Avoid pushing all terms into one long line with the assumption that a later pass will split it. Use local line breaking before global knobs. Document-level settings such as `fleqn`, `emergencystretch`, or `allowdisplaybreaks` are secondary tools and should not compensate for poor local formula structure.

Preserve mathematical meaning. Do not rename symbols, weaken assumptions, change theorem statements, alter labels, reorder equations semantically, or modify cited claims for layout convenience. If a display must be reorganized, keep the mathematical order and references clear.

## Reporting

Report the compile command, whether it passed, new or relevant warnings, affected labels, inspected PDF pages, and any unverified items. If compilation is impossible in the current environment, leave the exact command needed to verify the edit later.
