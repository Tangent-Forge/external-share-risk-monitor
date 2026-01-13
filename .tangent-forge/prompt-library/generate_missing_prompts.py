#!/usr/bin/env python3
"""
Generate missing prompt markdown files from PROMPT_INDEX.json

This script reads PROMPT_INDEX.json and creates markdown files for any
prompts that don't already exist.
"""

import json
from pathlib import Path

# Configuration
LIBRARY_ROOT = Path(__file__).parent
INDEX_FILE = LIBRARY_ROOT / "PROMPT_INDEX.json"
PROMPTS_DIR = LIBRARY_ROOT / "prompts"

# Category mappings
CATEGORIES = {
    "dev": "Development & Code",
    "docs": "Documentation",
    "review": "Review & Audit",
    "system": "System & Infrastructure",
    "extraction": "Extraction & Analysis",
    "meta": "Meta & Orchestration"
}


def load_index():
    """Load the prompt index."""
    with open(INDEX_FILE, 'r') as f:
        return json.load(f)


def generate_prompt_markdown(prompt_data):
    """Generate markdown content for a prompt."""
    category_name = CATEGORIES.get(prompt_data['category'], prompt_data['category'])
    
    content = f"""# {prompt_data['id']}: {prompt_data['name']}

**Category:** {category_name}  
**Complexity:** {prompt_data['complexity'].capitalize()}  
**Tags:** {', '.join(prompt_data['tags'])}"""
    
    if prompt_data.get('source'):
        content += f"  \n**Source:** {prompt_data['source']}"
    
    content += """

---

## Purpose

{description}

## When to Use

Use this prompt when you need to {use_case}.

## Prompt

```
[PROMPT CONTENT TO BE FILLED IN]

This prompt requires manual completion based on the source material.
Refer to: {source}
```

## Expected Output

- Detailed analysis or implementation
- Compliance with governance standards
- Clear documentation of changes

## Notes

This prompt was auto-generated from PROMPT_INDEX.json.
Please update with actual prompt content from the source material.
""".format(
        description=prompt_data['description'],
        use_case=prompt_data['description'].lower(),
        source=prompt_data.get('source', 'original documentation')
    )
    
    return content


def main():
    """Generate missing prompt files."""
    index = load_index()
    
    created = []
    existing = []
    
    for prompt in index['prompts']:
        prompt_file = LIBRARY_ROOT / prompt['file']
        
        if prompt_file.exists():
            existing.append(prompt['id'])
            continue
        
        # Create directory if needed
        prompt_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Generate and write markdown
        content = generate_prompt_markdown(prompt)
        prompt_file.write_text(content, encoding='utf-8')
        
        created.append(prompt['id'])
        print(f"✓ Created: {prompt['file']}")
    
    # Summary
    print(f"\n=== Summary ===")
    print(f"Created: {len(created)} prompts")
    print(f"Existing: {len(existing)} prompts")
    print(f"Total: {len(index['prompts'])} prompts")
    
    if created:
        print(f"\nNewly created prompts:")
        for prompt_id in created:
            print(f"  - {prompt_id}")


if __name__ == "__main__":
    main()
