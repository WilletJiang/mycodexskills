# DOCX Creation-Time Render Harness

A professional Word document should be rendered while it is being created or edited. OOXML validation proves the package is structurally plausible; it does not prove that pagination, tables, images, comments, or tracked changes look correct.

## Minimum Harness

Identify the document path, expected output path, conversion command, and pages most likely to change. Prefer the bundled LibreOffice wrapper:

```bash
python scripts/office/soffice.py --headless --convert-to pdf document.docx
```

Render the PDF to page images when visual inspection is needed:

```bash
pdftoppm -png -r 150 document.pdf page
```

## What To Inspect

Check cover pages, section starts, dense tables, image-heavy pages, pages near inserted or deleted content, headers, footers, page numbers, table of contents, captions, equations, comments, and tracked changes. Look for overflow, broken numbering, unexpected page breaks, cropped images, missing fonts, inconsistent styles, and review markup that changes layout.

## Iteration

Render after the first meaningful layout pass, after major structural edits, and at the final gate. If conversion is unavailable, leave the exact command and mark visual verification as pending rather than claiming the document is finished from XML inspection alone.
