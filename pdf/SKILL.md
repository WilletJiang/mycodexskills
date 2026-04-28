---
name: pdf
description: Use this skill whenever the user wants to read, extract, create, edit, combine, split, rotate, watermark, encrypt, decrypt, OCR, annotate, or fill PDF files. Trigger whenever a .pdf file is mentioned or when the requested deliverable is a PDF. Use visual rendering or OCR for scanned, multi-column, figure-heavy, or layout-sensitive PDFs.
license: Proprietary. LICENSE.txt has complete terms
---

# PDF Workflows

Use this skill when PDF is either the input format or the required output format. Choose the tool by document structure: use text extraction for simple born-digital PDFs, OCR for scanned pages, form tooling for fillable forms, and rendering when visual fidelity or reading order matters.

For academic papers, two-column reports, proceedings papers, figure-heavy documents, dense tables, mathematical displays, footnotes, marginal notes, or any PDF where reading order matters, treat plain text extraction as provisional. Render pages to images first and inspect the layout visually. If the PDF has no reliable text layer, or if extracted text disagrees with the rendered page, use OCR and reconcile the result against the page image. The rendered page is the authority for reading order.

For basic page operations, use `pypdf`. It is appropriate for merging, splitting, rotating, metadata inspection, encryption, and simple watermarking. For layout-aware text and table extraction, use `pdfplumber`, but validate multi-column output visually before relying on it. For new programmatic PDFs, use ReportLab. For command-line restructuring, use `qpdf` when available. For scanned documents, convert pages to images and use OCR.

## Layout-Sensitive Reading

Use this path when the document is two-column, scanned, math-heavy, table-heavy, or visually complex. First render page images:

```bash
mkdir -p pages
python scripts/convert_pdf_to_images.py input.pdf pages
```

If the bundled converter is unavailable, use Poppler directly:

```bash
mkdir -p pages
pdftoppm -png -r 200 input.pdf pages/page
```

Inspect the rendered pages before summarizing, quoting, extracting tables, or answering questions about the document. For scanned pages or unreliable text layers, run OCR on the rendered page images when OCR tooling is available:

```bash
tesseract pages/page_1.png stdout -l eng
```

OCR recovers text; it does not prove layout order. For multi-column pages, verify that the reading sequence follows the visual columns, captions, footnotes, and equation placement.

## Common Commands

Text extraction:

```bash
pdftotext -layout input.pdf output.txt
```

Merge with `qpdf`:

```bash
qpdf --empty --pages file1.pdf file2.pdf -- merged.pdf
```

Split page ranges:

```bash
qpdf input.pdf --pages . 1-5 -- pages-1-5.pdf
```

Render pages for inspection:

```bash
python scripts/convert_pdf_to_images.py input.pdf output-dir
```

Extract embedded images:

```bash
pdfimages -j input.pdf image
```

## Python Patterns

Use `PdfReader` and `PdfWriter` from `pypdf` for structural changes. Use `pdfplumber.open` for text and tables. When creating PDFs with ReportLab, avoid Unicode subscript and superscript characters with built-in fonts because they often render incorrectly; use ReportLab paragraph markup such as `<sub>` and `<super>` instead.

For fillable forms, read `forms.md` before editing. The bundled form scripts inspect fields, extract structure, fill fields, and create validation images. For broader library usage and troubleshooting, read `reference.md`.

## Verification

After modifying or reading a PDF, inspect page count, page order, rotation, visible content, and form field state as relevant. When layout matters, render pages to images and compare visually. When OCR is used, sample the extracted text against the page images because OCR confidence is not proof of correctness. For two-column PDFs, explicitly check that extracted text has not interleaved left and right columns.
