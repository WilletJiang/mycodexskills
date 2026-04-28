---
name: pptx
description: Create, edit, inspect, and repair PowerPoint files with a creation-time render harness. Trigger whenever a .pptx file is an input, output, or intermediate artifact, including slide decks, presentations, pitch decks, speaker notes, template editing, layout repair, content extraction, deck merging, slide splitting, and any request that requires opening, creating, or modifying a PowerPoint file.
license: Proprietary. LICENSE.txt has complete terms
---

# PPTX Workflows

Use this skill for PowerPoint files. Start by deciding whether the task is content extraction, template-based editing, or new deck creation. Preserve an existing template's layout system unless the user asks for a redesign.

For extraction and inspection:

```bash
python -m markitdown presentation.pptx
python scripts/thumbnail.py presentation.pptx
python scripts/office/unpack.py presentation.pptx unpacked
```

Read `editing.md` for template editing, slide manipulation, OOXML cleanup, and pack validation. Read `pptxgenjs.md` when creating a deck from scratch.

Read `references/render-harness.md` before creating a deck, editing a template, or making layout-sensitive changes.

## Design Standard

A presentation should have a clear visual system: a content-informed palette, consistent typography, intentional spacing, and a repeated motif that supports the subject. Avoid plain title-and-bullet slides when the content calls for comparison, process, evidence, hierarchy, or narrative. Use charts, diagrams, images, icons, callouts, timelines, and structured layouts when they make the argument clearer.

Choose typography and color for the topic and audience. Keep body text readable, use strong hierarchy between title, section headers, body, captions, and data labels, and maintain reliable margins. Do not use decorative title underlines as a default device. Do not let text boxes, footers, citations, or visual elements collide.

## Creation-Time Render Harness

Treat every deck as a rendered artifact during creation. Build a small slice, render it, inspect it, then continue. Do not wait until the final slide to discover that the layout system fails.

Extract text to check ordering, missing content, typos, and placeholder remnants:

```bash
python -m markitdown output.pptx
python -m markitdown output.pptx | grep -iE "xxxx|lorem|ipsum|this.*(page|slide).*layout"
```

Render the deck for visual inspection:

```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

Inspect for overlap, overflow, weak contrast, cramped margins, inconsistent alignment, narrow text boxes, orphaned captions, placeholder content, and slides whose layout no longer matches their content. Fix issues and re-render affected slides before declaring success.

## Dependencies

Use `markitdown` for text extraction, Pillow for thumbnail grids, `pptxgenjs` for new decks, LibreOffice through `scripts/office/soffice.py` for conversion, and Poppler for page images.
