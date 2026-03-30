# OOXML Patterns for DOCX

Read this file when editing tracked changes, comments, or embedded assets directly in XML.

## Schema Compliance

- In `<w:pPr>`, keep elements in schema order.
- Add `xml:space="preserve"` to `<w:t>` elements with leading or trailing whitespace.
- Use eight-digit hexadecimal RSIDs such as `00AB1234`.

## Tracked Changes

### Insertion

```xml
<w:ins w:id="1" w:author="Codex" w:date="2025-01-01T00:00:00Z">
  <w:r><w:t>inserted text</w:t></w:r>
</w:ins>
```

### Deletion

```xml
<w:del w:id="2" w:author="Codex" w:date="2025-01-01T00:00:00Z">
  <w:r><w:delText>deleted text</w:delText></w:r>
</w:del>
```

Inside `<w:del>`, use `<w:delText>` instead of `<w:t>`.

### Minimal Redlines

```xml
<w:r><w:t>The term is </w:t></w:r>
<w:del w:id="1" w:author="Codex" w:date="2025-01-01T00:00:00Z">
  <w:r><w:delText>30</w:delText></w:r>
</w:del>
<w:ins w:id="2" w:author="Codex" w:date="2025-01-01T00:00:00Z">
  <w:r><w:t>60</w:t></w:r>
</w:ins>
<w:r><w:t> days.</w:t></w:r>
```

### Deleting a Whole Paragraph or List Item

```xml
<w:p>
  <w:pPr>
    <w:rPr>
      <w:del w:id="1" w:author="Codex" w:date="2025-01-01T00:00:00Z"/>
    </w:rPr>
  </w:pPr>
  <w:del w:id="2" w:author="Codex" w:date="2025-01-01T00:00:00Z">
    <w:r><w:delText>Entire paragraph content...</w:delText></w:r>
  </w:del>
</w:p>
```

Without the paragraph-mark deletion inside `<w:pPr><w:rPr>`, accepting changes leaves an empty paragraph behind.

### Rejecting Another Author's Insertion

```xml
<w:ins w:author="Jane" w:id="5">
  <w:del w:author="Codex" w:id="10">
    <w:r><w:delText>their inserted text</w:delText></w:r>
  </w:del>
</w:ins>
```

### Restoring Another Author's Deletion

```xml
<w:del w:author="Jane" w:id="5">
  <w:r><w:delText>deleted text</w:delText></w:r>
</w:del>
<w:ins w:author="Codex" w:id="10">
  <w:r><w:t>deleted text</w:t></w:r>
</w:ins>
```

## Comments

`<w:commentRangeStart>` and `<w:commentRangeEnd>` must be siblings of `<w:r>`, never nested inside a run.

```xml
<w:commentRangeStart w:id="0"/>
<w:r><w:t>text</w:t></w:r>
<w:commentRangeEnd w:id="0"/>
<w:r>
  <w:rPr><w:rStyle w:val="CommentReference"/></w:rPr>
  <w:commentReference w:id="0"/>
</w:r>
```

Replies nest inside the parent comment range:

```xml
<w:commentRangeStart w:id="0"/>
  <w:commentRangeStart w:id="1"/>
  <w:r><w:t>text</w:t></w:r>
  <w:commentRangeEnd w:id="1"/>
<w:commentRangeEnd w:id="0"/>
```

## Images

To add an image manually:

1. Copy the file into `word/media/`.
2. Add a relationship entry in `word/_rels/document.xml.rels`.
3. Add a content type in `[Content_Types].xml`.
4. Add the drawing reference in `document.xml`.

```xml
<Relationship Id="rId5" Type=".../image" Target="media/image1.png"/>
```

```xml
<Default Extension="png" ContentType="image/png"/>
```

```xml
<w:drawing>
  <wp:inline>
    <wp:extent cx="914400" cy="914400"/>
    <a:graphic>
      <a:graphicData uri=".../picture">
        <pic:pic>
          <pic:blipFill><a:blip r:embed="rId5"/></pic:blipFill>
        </pic:pic>
      </a:graphicData>
    </a:graphic>
  </wp:inline>
</w:drawing>
```
