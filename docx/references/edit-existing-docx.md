# Editing Existing DOCX Files

Follow the unpack-edit-pack workflow. Keep edits surgical and verify every modified document before declaring success.

## Step 1: Unpack

```bash
python scripts/office/unpack.py document.docx unpacked/
```

This extracts XML, pretty-prints it, merges adjacent runs by default, and converts smart quotes into XML-safe entities.

## Step 2: Edit XML

Edit files inside `unpacked/word/`.

- Prefer direct file edits over writing ad hoc Python scripts for one-off replacements.
- Preserve surrounding `<w:rPr>` and `<w:pPr>` blocks when replacing content.
- Use the smallest possible tracked-change region instead of replacing whole paragraphs unnecessarily.
- Use `Codex` as the default author for tracked changes and comments unless the user requests a different author name.

### Smart Quote Entities

Use entities when adding text that includes quotes or apostrophes:

```xml
<w:t>Here&#x2019;s a quote: &#x201C;Hello&#x201D;</w:t>
```

| Entity | Character |
|--------|-----------|
| `&#x2018;` | ‘ |
| `&#x2019;` | ’ |
| `&#x201C;` | “ |
| `&#x201D;` | ” |

### Adding Comments

Use `comment.py` to update the required OOXML comment files:

```bash
python scripts/comment.py unpacked/ 0 "Comment text with &amp; and &#x2019;"
python scripts/comment.py unpacked/ 1 "Reply text" --parent 0
python scripts/comment.py unpacked/ 2 "Text" --author "Custom Author"
```

Then add the marker runs in `document.xml`. See [ooxml-patterns.md](ooxml-patterns.md).

## Step 3: Pack and Validate

```bash
python scripts/office/pack.py unpacked/ output.docx --original document.docx
```

Validation and auto-repair can fix:

- invalid `durableId` values above the allowed range
- missing `xml:space="preserve"` on text nodes with leading or trailing whitespace

Validation will not fix:

- malformed XML
- invalid element nesting
- missing relationships
- broken schema ordering

## Common Pitfalls

- Replace entire `<w:r>` blocks when introducing tracked changes rather than inserting `<w:del>` or `<w:ins>` inside an existing run.
- Copy the original `<w:rPr>` formatting into inserted and deleted runs so the visible style remains stable.
- Delete only the changed tokens when redlining prose; do not mark unrelated surrounding text.
- When removing the entire content of a paragraph or list item, also mark the paragraph mark as deleted so accepted changes do not leave an empty paragraph behind.
