---
name: brand-guidelines
description: Apply Anthropic brand colors and typography with a visual render check. Use when brand colors, typography, visual formatting, or company design standards are relevant.
license: Complete terms in LICENSE.txt
---

# Anthropic Brand Guidelines

Use this skill to apply Anthropic's visual identity to slides, documents, reports, or other artifacts where brand consistency matters. Preserve readability and content hierarchy first; brand styling should clarify the artifact, not obscure it.

The core neutral palette is dark `#141413`, light `#faf9f5`, mid gray `#b0aea5`, and light gray `#e8e6dc`. The accent palette is orange `#d97757`, blue `#6a9bcc`, and green `#788c5d`. Use the neutral palette for structure and legibility, then apply accents sparingly to calls to action, highlights, shapes, and section rhythm.

Use Poppins for headings when available, with Arial as the fallback. Use Lora for body text when available, with Georgia as the fallback. Headings are typically text at 24 points or larger; body text should remain readable and should not be forced into display styling.

When applying brand styling programmatically, use precise RGB values and preserve existing semantic hierarchy. In PowerPoint workflows, `python-pptx` and `RGBColor` are appropriate for color application. Do not restyle established templates indiscriminately; match the existing system when the file already has a clear brand implementation.

## Visual Harness

After applying brand styling, render or open the artifact when tooling is available. Check typography, color fidelity, contrast, hierarchy, spacing, and whether accents clarify rather than dominate. For documents or presentations, inspect rendered pages or slides rather than relying only on source properties.

If rendering is unavailable, report the exact command needed to inspect the artifact and identify which brand checks remain pending.
