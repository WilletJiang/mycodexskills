---
name: docx
description: Create, read, edit, and manipulate Word documents with a creation-time render harness. Trigger on Word documents, .docx files, tracked changes, comments, document templates, reports, memos, letters, professional formatting, tables of contents, page numbers, headers, embedded images, extraction, reorganization, legacy .doc conversion, review, and redlining. Do not use for PDFs, spreadsheets, or unrelated coding tasks.
license: Proprietary. LICENSE.txt has complete terms
---

# DOCX Workflows

Treat a `.docx` file as a package of OOXML parts. Choose the lightest reliable workflow for the task, preserve existing formatting unless the user asks to redesign it, and validate the result before claiming completion.

For text extraction, use Pandoc with tracked changes preserved:

```bash
pandoc --track-changes=all document.docx -o output.md
```

For raw OOXML inspection or surgical edits, unpack the file:

```bash
python scripts/office/unpack.py document.docx unpacked
```

For legacy `.doc` conversion or render checks, use LibreOffice through the wrapper:

```bash
python scripts/office/soffice.py --headless --convert-to docx document.doc
python scripts/office/soffice.py --headless --convert-to pdf document.docx
```

Read `references/create-documents.md` when generating a new document, `references/edit-existing-docx.md` when modifying an existing file, and `references/ooxml-patterns.md` for tracked changes, comments, images, relationships, and schema-sensitive edits.

Read `references/render-harness.md` before creating or substantially editing a professional document, template, report, or redline where layout matters.

## Editing Standard

Use the smallest XML edit that achieves the requested change. Copy surrounding run, paragraph, and section properties when inserting content into an existing design. Preserve styles, numbering, relationships, headers, footers, comments, and revision metadata unless the task explicitly changes them. Use `scripts/comment.py` for comment boilerplate and `scripts/accept_changes.py` when tracked changes must be accepted through LibreOffice.

## Creation-Time Render Harness

During creation or substantial editing, establish the render command early. Convert the working document to PDF after the first meaningful layout pass, inspect representative pages, and repeat after major structural changes. XML validation is necessary but not sufficient for professional documents.

Inspect pagination, headings, tables, images, captions, equations, headers, footers, page numbers, comments, tracked changes, table of contents behavior, margins, and text overflow. For redlines, verify both the edited package and the rendered review view when possible.

After editing, repack and validate with the Office helper scripts. Before delivery, provide render evidence or state the exact render command and pending checks.
