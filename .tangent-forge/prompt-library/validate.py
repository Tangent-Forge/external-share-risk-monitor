#!/usr/bin/env python3
"""
Tangent Forge Prompt Library - Validation Script

Validates PROMPT_INDEX.json against schema and checks that all
referenced prompt files exist.

Usage:
    python validate.py
    python validate.py --verbose
"""

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Error: jsonschema library not installed")
    print("Install with: pip install jsonschema")
    sys.exit(1)

# Configuration
LIBRARY_ROOT = Path(__file__).parent
INDEX_FILE = LIBRARY_ROOT / "PROMPT_INDEX.json"
SCHEMA_FILE = LIBRARY_ROOT / "schemas" / "prompt_library.schema.json"


def load_json(file_path):
    """Load JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {file_path}")
        print(f"  {e}")
        sys.exit(1)


def validate_schema(data, schema):
    """Validate data against JSON schema."""
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True, None
    except jsonschema.exceptions.ValidationError as e:
        return False, str(e)


def check_prompt_files(index_data, verbose=False):
    """Check that all referenced prompt files exist."""
    missing = []
    existing = []
    
    for prompt in index_data.get('prompts', []):
        prompt_file = LIBRARY_ROOT / prompt['file']
        
        if prompt_file.exists():
            existing.append(prompt['id'])
            if verbose:
                print(f"  ✓ {prompt['id']}: {prompt['file']}")
        else:
            missing.append({
                'id': prompt['id'],
                'file': prompt['file']
            })
            if verbose:
                print(f"  ✗ {prompt['id']}: {prompt['file']} (MISSING)")
    
    return existing, missing


def check_duplicate_ids(index_data):
    """Check for duplicate prompt IDs."""
    ids = [p['id'] for p in index_data.get('prompts', [])]
    duplicates = [id for id in ids if ids.count(id) > 1]
    return list(set(duplicates))


def main():
    """Run validation checks."""
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    
    print("=== Tangent Forge Prompt Library Validation ===\n")
    
    # Load files
    print("Loading files...")
    index_data = load_json(INDEX_FILE)
    schema_data = load_json(SCHEMA_FILE)
    print("  ✓ Loaded PROMPT_INDEX.json")
    print("  ✓ Loaded schema\n")
    
    # Validate against schema
    print("Validating PROMPT_INDEX.json against schema...")
    is_valid, error = validate_schema(index_data, schema_data)
    
    if is_valid:
        print("  ✓ Schema validation passed\n")
    else:
        print("  ✗ Schema validation failed:")
        print(f"    {error}\n")
        sys.exit(1)
    
    # Check for duplicate IDs
    print("Checking for duplicate prompt IDs...")
    duplicates = check_duplicate_ids(index_data)
    
    if duplicates:
        print(f"  ✗ Found {len(duplicates)} duplicate IDs:")
        for dup_id in duplicates:
            print(f"    - {dup_id}")
        print()
        sys.exit(1)
    else:
        print("  ✓ No duplicate IDs found\n")
    
    # Check prompt files
    print("Checking prompt files...")
    existing, missing = check_prompt_files(index_data, verbose)
    
    if missing:
        print(f"\n  ✗ {len(missing)} prompt files missing:")
        for item in missing:
            print(f"    - {item['id']}: {item['file']}")
        print()
        sys.exit(1)
    else:
        print(f"  ✓ All {len(existing)} prompt files exist\n")
    
    # Summary
    print("=== Validation Summary ===")
    print(f"Total prompts: {len(index_data.get('prompts', []))}")
    print(f"Categories: {len(index_data.get('categories', {}))}")
    print(f"Status: ✓ ALL CHECKS PASSED")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
