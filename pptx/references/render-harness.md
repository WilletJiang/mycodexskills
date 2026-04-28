# PPTX Creation-Time Render Harness

A presentation should be rendered repeatedly while it is being created or edited. Slide XML and text extraction cannot prove that a deck is visually coherent.

## Minimum Harness

Identify the deck path, conversion command, affected slides, and expected visual role of each affected slide. Use text extraction for content integrity and PDF rendering for layout:

```bash
python -m markitdown output.pptx
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

## What To Inspect

Inspect title slides, section dividers, dense content slides, chart slides, image-heavy slides, comparison layouts, timelines, footers, citations, and any slide generated from a template placeholder. Check overlap, clipping, text wrapping, contrast, slide margins, alignment, inconsistent motifs, missing images, placeholder remnants, and charts or icons that no longer match the message.

## Iteration

Render after the first layout slice, after applying a template transformation, and at the final gate. When a fix changes spacing or text length, re-render the affected slide. If rendering is unavailable, leave the exact command and mark visual verification as pending.
