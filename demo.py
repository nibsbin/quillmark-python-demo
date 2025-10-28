"""
Quillmark Python Demo

This script demonstrates how to use the Quillmark package to render
a markdown file to an Air Force official memorandum in PDF format.
"""

import quillmark
import sys
from pathlib import Path


def main():
    """Render sample-memo.md to a PDF using the usaf_memo Quill."""
    
    # Define file paths
    markdown_file = Path("sample-memo.md")
    quill_path = Path("tonguetoquill-collection/quills/usaf_memo")
    output_file = Path("output_memo.pdf")
    
    # Check if input file exists
    if not markdown_file.exists():
        print(f"Error: {markdown_file} not found!")
        sys.exit(1)
    
    # Check if quill exists
    if not quill_path.exists():
        print(f"Error: Quill path {quill_path} not found!")
        sys.exit(1)
    
    try:
        # Read the markdown content
        with open(markdown_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Create a Quillmark instance
        qm = quillmark.Quillmark()
        
        # Load and register the USAF memo quill
        print("Loading USAF memo Quill...")
        quill = quillmark.Quill.from_path(str(quill_path))
        qm.register_quill(quill)
        
        # Parse the markdown document
        print("Parsing markdown document...")
        parsed = quillmark.ParsedDocument.from_markdown(markdown_content)
        
        # Create a workflow from the parsed document
        print("Creating workflow...")
        workflow = qm.workflow_from_parsed(parsed)
        
        # Render the document to PDF
        print("Rendering to PDF...")
        result = workflow.render(parsed, format=quillmark.OutputFormat.PDF)
        
        # Check if artifacts were generated
        if not result.artifacts:
            print("Error: No artifacts were generated!")
            sys.exit(1)
        
        # Save the result
        print(f"Saving output to {output_file}...")
        result.artifacts[0].save(str(output_file))
        
        print(f"\n✓ Successfully generated {output_file}")
        print(f"  Artifacts created: {len(result.artifacts)}")
        
    except quillmark.ParseError as e:
        print(f"Error parsing markdown: {e}")
        sys.exit(1)
    except quillmark.CompilationError as e:
        print(f"Error compiling document: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
