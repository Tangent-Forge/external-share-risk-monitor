#!/usr/bin/env python3
"""
Tangent Forge Prompt Library - Ingestion Script

Validates and adds new prompts to the library.
Ensures schema compliance and updates the index.

Usage:
    python ingest_prompt.py <prompt.json>
    python ingest_prompt.py --from-clipboard
    python ingest_prompt.py --interactive
"""

import json
import sys
import os
from pathlib import Path
from datetime import date
import re

# Configuration
LIBRARY_ROOT = Path(__file__).parent
INDEX_FILE = LIBRARY_ROOT / "PROMPT_INDEX.json"
SCHEMA_FILE = LIBRARY_ROOT / "schemas" / "prompt_library.schema.json"
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
    """Load the current prompt index."""
    with open(INDEX_FILE, 'r') as f:
        return json.load(f)


def save_index(index):
    """Save the updated prompt index."""
    with open(INDEX_FILE, 'w') as f:
        json.dump(index, f, indent=2)
    print(f"✓ Updated {INDEX_FILE}")


def validate_prompt(prompt_data):
    """Validate a prompt entry against requirements."""
    errors = []
    
    # Required fields
    required = ["id", "name", "category", "description", "tags", "complexity", "prompt"]
    for field in required:
        if field not in prompt_data:
            errors.append(f"Missing required field: {field}")
    
    if errors:
        return errors
    
    # ID format
    if not re.match(r'^[A-Z]+-\d{3}$', prompt_data["id"]):
        errors.append(f"Invalid ID format: {prompt_data['id']} (expected CATEGORY-NNN)")
    
    # Category
    if prompt_data["category"] not in CATEGORIES:
        errors.append(f"Invalid category: {prompt_data['category']} (valid: {list(CATEGORIES.keys())})")
    
    # Complexity
    if prompt_data["complexity"] not in ["low", "medium", "high"]:
        errors.append(f"Invalid complexity: {prompt_data['complexity']}")
    
    # Tags format
    for tag in prompt_data.get("tags", []):
        if not re.match(r'^[a-z][a-z0-9-]*$', tag):
            errors.append(f"Invalid tag format: {tag} (use lowercase, hyphenated)")
    
    # Prompt length
    if len(prompt_data.get("prompt", "")) < 50:
        errors.append("Prompt text too short (minimum 50 characters)")
    
    return errors


def generate_file_path(prompt_data):
    """Generate the file path for a prompt."""
    category = prompt_data["category"]
    prompt_id = prompt_data["id"]
    name_slug = prompt_data["name"].lower().replace(" ", "_").replace("-", "_")
    name_slug = re.sub(r'[^a-z0-9_]', '', name_slug)
    return f"prompts/{category}/{prompt_id}_{name_slug}.md"


def generate_prompt_file(prompt_data):
    """Generate markdown file content for a prompt."""
    content = f"""# {prompt_data['id']}: {prompt_data['name']}

**Category:** {CATEGORIES.get(prompt_data['category'], prompt_data['category'])}  
**Complexity:** {prompt_data['complexity'].capitalize()}  
**Tags:** {', '.join(prompt_data['tags'])}  
"""
    
    if prompt_data.get('source'):
        content += f"**Source:** {prompt_data['source']}\n"
    
    content += f"""
---

## Purpose

{prompt_data['description']}

## When to Use

{prompt_data.get('when_to_use', 'Use when this type of task is needed.')}

## Prompt

```
{prompt_data['prompt']}
```
"""
    
    if prompt_data.get('expected_output'):
        content += f"""
## Expected Output

{prompt_data['expected_output']}
"""
    
    if prompt_data.get('variants'):
        content += "\n## Variants\n"
        for variant in prompt_data['variants']:
            content += f"""
### {variant['name']}

{variant.get('description', '')}

```
{variant['prompt']}
```
"""
    
    return content


def get_next_id(index, category):
    """Get the next available ID for a category."""
    prefix = category.upper()
    existing_ids = [
        p["id"] for p in index["prompts"] 
        if p["id"].startswith(prefix)
    ]
    
    if not existing_ids:
        return f"{prefix}-001"
    
    numbers = [int(id.split("-")[1]) for id in existing_ids]
    next_num = max(numbers) + 1
    return f"{prefix}-{next_num:03d}"


def add_prompt(prompt_data, index):
    """Add a validated prompt to the library."""
    # Generate file path
    file_path = generate_file_path(prompt_data)
    prompt_data["file"] = file_path
    
    # Add metadata
    prompt_data["created"] = prompt_data.get("created", date.today().isoformat())
    prompt_data["updated"] = date.today().isoformat()
    
    # Create prompt file
    full_path = LIBRARY_ROOT / file_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(full_path, 'w') as f:
        f.write(generate_prompt_file(prompt_data))
    print(f"✓ Created {file_path}")
    
    # Add to index (create minimal entry)
    index_entry = {
        "id": prompt_data["id"],
        "name": prompt_data["name"],
        "category": prompt_data["category"],
        "file": file_path,
        "description": prompt_data["description"],
        "tags": prompt_data["tags"],
        "complexity": prompt_data["complexity"]
    }
    
    if prompt_data.get("source"):
        index_entry["source"] = prompt_data["source"]
    
    index["prompts"].append(index_entry)
    
    return index


def interactive_mode():
    """Interactively create a new prompt."""
    print("\n📝 Tangent Forge Prompt Library - Add New Prompt\n")
    
    index = load_index()
    
    # Category
    print("Categories:", ", ".join(CATEGORIES.keys()))
    category = input("Category: ").strip().lower()
    if category not in CATEGORIES:
        print(f"Invalid category. Using 'meta'.")
        category = "meta"
    
    # Auto-generate ID
    suggested_id = get_next_id(index, category)
    prompt_id = input(f"ID [{suggested_id}]: ").strip() or suggested_id
    
    # Basic info
    name = input("Name: ").strip()
    description = input("Description: ").strip()
    tags = input("Tags (comma-separated): ").strip().split(",")
    tags = [t.strip().lower().replace(" ", "-") for t in tags if t.strip()]
    
    complexity = input("Complexity (low/medium/high) [medium]: ").strip() or "medium"
    when_to_use = input("When to use (optional): ").strip()
    
    # Prompt text
    print("\nEnter prompt text (end with a line containing only '---'):")
    lines = []
    while True:
        line = input()
        if line.strip() == "---":
            break
        lines.append(line)
    prompt_text = "\n".join(lines)
    
    # Build prompt data
    prompt_data = {
        "id": prompt_id,
        "name": name,
        "category": category,
        "description": description,
        "tags": tags,
        "complexity": complexity,
        "prompt": prompt_text
    }
    
    if when_to_use:
        prompt_data["when_to_use"] = when_to_use
    
    # Validate
    errors = validate_prompt(prompt_data)
    if errors:
        print("\n❌ Validation errors:")
        for e in errors:
            print(f"  - {e}")
        return
    
    # Add to library
    index = add_prompt(prompt_data, index)
    save_index(index)
    
    print(f"\n✅ Prompt {prompt_id} added successfully!")
    print(f"   File: {prompt_data['file']}")


def from_json(json_path):
    """Add a prompt from a JSON file."""
    with open(json_path, 'r') as f:
        prompt_data = json.load(f)
    
    errors = validate_prompt(prompt_data)
    if errors:
        print("❌ Validation errors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    
    index = load_index()
    
    # Check for duplicate ID
    existing_ids = [p["id"] for p in index["prompts"]]
    if prompt_data["id"] in existing_ids:
        print(f"❌ Prompt ID {prompt_data['id']} already exists")
        sys.exit(1)
    
    index = add_prompt(prompt_data, index)
    save_index(index)
    
    print(f"\n✅ Prompt {prompt_data['id']} added successfully!")


def from_clipboard():
    """Add a prompt from clipboard JSON."""
    try:
        import pyperclip
        json_text = pyperclip.paste()
        prompt_data = json.loads(json_text)
    except ImportError:
        print("❌ pyperclip not installed. Run: pip install pyperclip")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in clipboard: {e}")
        sys.exit(1)
    
    errors = validate_prompt(prompt_data)
    if errors:
        print("❌ Validation errors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    
    index = load_index()
    index = add_prompt(prompt_data, index)
    save_index(index)
    
    print(f"\n✅ Prompt {prompt_data['id']} added from clipboard!")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Tangent Forge Prompt Library - Ingestion Script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ingest_prompt.py prompt.json           # Add from JSON file
  python ingest_prompt.py --interactive         # Interactive mode
  python ingest_prompt.py --from-clipboard      # Add from clipboard
        """
    )
    
    parser.add_argument(
        'json_file',
        nargs='?',
        help='Path to JSON file containing prompt data'
    )
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Interactive mode for creating a new prompt'
    )
    parser.add_argument(
        '--from-clipboard', '-c',
        action='store_true',
        help='Add prompt from clipboard JSON'
    )
    
    args = parser.parse_args()
    
    if args.interactive:
        interactive_mode()
    elif args.from_clipboard:
        from_clipboard()
    elif args.json_file:
        if not args.json_file.endswith('.json'):
            print(f"Error: File must be a .json file")
            sys.exit(1)
        from_json(args.json_file)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
