# Quillmark Python Demo

A minimal demonstration of using the [Quillmark](https://pypi.org/project/quillmark/) package to render markdown content into an Air Force official memorandum.

## Overview

This demo shows how to:
- Use the Quillmark Python package to render documents
- Generate an official Air Force memorandum from markdown
- Utilize the `tonguetoquill-collection/quills/usaf_memo` Quill for proper formatting

## Installation

1. Clone this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the demo script to generate a PDF memorandum:

```bash
python demo.py
```

This will:
1. Read the content from `sample-memo.md`
2. Use the USAF memo Quill to format the document according to AFH 33-337 standards
3. Generate `output_memo.pdf` in the current directory

## Files

- `demo.py` - Main script that demonstrates the Quillmark workflow
- `sample-memo.md` - Example Air Force memorandum in markdown format
- `requirements.txt` - Python package dependencies
- `tonguetoquill-collection/` - Collection of Quills for different document types

## How It Works

The demo follows these steps:

1. **Load the Quill**: Loads the USAF memo Quill from `tonguetoquill-collection/quills/usaf_memo`
2. **Parse Markdown**: Parses the markdown file with YAML frontmatter containing memo metadata
3. **Create Workflow**: Creates a rendering workflow based on the Quill
4. **Render to PDF**: Renders the document to PDF format
5. **Save Output**: Saves the generated PDF to disk

## Example Markdown

The `sample-memo.md` file demonstrates proper markdown structure for an Air Force memorandum:

```markdown
---
QUILL: usaf_memo
letterhead_title: DEPARTMENT OF THE AIR FORCE
letterhead_caption:
  - HEADQUARTERS UNITED STATES AIR FORCE
memo_for:
  - ALL PERSONNEL
memo_from:
  - HQ USAF/A1
  - Organization Name
  - Street Address
  - City ST ZIP
subject: Memo Subject
signature_block:
  - NAME, Rank, USAF
  - Duty Title
---

Your memo content goes here...
```

## Learn More

- [Quillmark Documentation](https://quillmark.readthedocs.io/)
- [Quillmark on PyPI](https://pypi.org/project/quillmark/)
- [Air Force Handbook 33-337](https://www.af.mil/AFH33-337/) - The Tongue and Quill

## License

See LICENSE file for details.
