---
name: docx
description: Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include any mention of Word, .docx files, tracked changes, comments, document templates, reports, memos, letters, or professional documents with formatting such as headings, tables of contents, page numbers, headers, or embedded images. Also use when extracting or reorganizing content from .docx files, converting legacy .doc files, or preparing a document for review or redlining. Do not use for PDFs, spreadsheets, or unrelated coding tasks.
license: Proprietary. LICENSE.txt has complete terms
---

# DOCX Creation, Editing, and Analysis

## Overview

Treat `.docx` as a ZIP archive of XML parts. Keep the main skill short and route into the right workflow quickly.

## Workflow Decision Tree

| Task | Action |
|------|--------|
| Read document text | Use `pandoc --track-changes=all document.docx -o output.md` |
| Inspect raw OOXML | Run `python scripts/office/unpack.py document.docx unpacked/` |
| Convert legacy `.doc` | Run `python scripts/office/soffice.py --headless --convert-to docx document.doc` |
| Create a new document | Read [references/create-documents.md](references/create-documents.md) |
| Edit an existing document | Read [references/edit-existing-docx.md](references/edit-existing-docx.md) |
| Work directly with tracked changes, comments, or OOXML patterns | Read [references/ooxml-patterns.md](references/ooxml-patterns.md) |

## Quick Start

### Read Content

```bash
pandoc --track-changes=all document.docx -o output.md
python scripts/office/unpack.py document.docx unpacked/
```

### Convert to Images

```bash
python scripts/office/soffice.py --headless --convert-to pdf document.docx
pdftoppm -jpeg -r 150 document.pdf page
```

### Accept Tracked Changes

```bash
python scripts/accept_changes.py input.docx output.docx
```

## Rules That Always Apply

- Validate generated or modified documents before declaring success.
- Prefer the smallest possible XML edit when modifying existing files.
- Preserve existing formatting by copying the surrounding run or paragraph properties.
- Use smart quote entities in OOXML when adding professional prose.
- Preserve existing behavior unless the task explicitly requires a visible document change.

## Bundled Resources

### scripts/

- `scripts/office/unpack.py` unpacks Office files for editing.
- `scripts/office/pack.py` repacks and validates Office files.
- `scripts/office/validate.py` runs schema and redlining validation.
- `scripts/comment.py` creates comment boilerplate across the required OOXML files.
- `scripts/accept_changes.py` accepts tracked changes through LibreOffice.

Run `--help` before reading large helper scripts unless customization is necessary.

### references/

- [references/create-documents.md](references/create-documents.md) for generating new `.docx` files with `docx`.
- [references/edit-existing-docx.md](references/edit-existing-docx.md) for unpack-edit-pack workflows.
- [references/ooxml-patterns.md](references/ooxml-patterns.md) for tracked changes, comments, images, and schema-sensitive XML patterns.

## Dependencies

- `pandoc` for text extraction.
- `docx` (`npm install -g docx`) for generating new documents.
- LibreOffice via `scripts/office/soffice.py` for conversion and acceptance workflows.
- `pdftoppm` for image conversion.
