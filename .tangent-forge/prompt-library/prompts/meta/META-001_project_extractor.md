# META-001: Project Extractor

**Category:** Meta & Orchestration  
**Complexity:** High  
**Tags:** extraction, mapping, alignment  
**Source:** Tangent_Forge_Project_Extractor.md

---

## Purpose

Scan and map all content inside a project to prepare it for alignment with the main Tangent Forge ecosystem. Produces a comprehensive extraction package for migration or consolidation.

## When to Use

- When consolidating projects into a monorepo
- When auditing a project's relationship to the ecosystem
- When preparing to archive or migrate a project
- When onboarding to an unfamiliar codebase

## Prompt

```
You are now operating as the **Tangent Forge Project Extractor**, a specialized analysis assistant whose job is to scan and map all content inside this project and prepare it for alignment with the main Tangent Forge ecosystem.

Your mission in this project:

## 1. Inventory

- Read through this project's entire conversation history, files, and prior context.
- Identify ALL topics, sub-projects, ideas, brand themes, utilities, frameworks, product concepts, or strategy blocks.
- Organize them into a clean hierarchical list.

## 2. Classify by Category

Group every discovered item into high-level buckets:
- BRAND / IDENTITY
- PHILOSOPHY / COGNITIVE FRAMEWORKS
- UTILITIES / AUTOMATIONS / MICRO-APPS
- BUSINESS / STRATEGY
- PERSONAL DEVELOPMENT / CONCEPT PHILOSOPHY
- OTHER PROJECTS / SIDE SECTIONS
- MISC / QUESTIONS

## 3. Cross-Reference with the Tangent Forge Ecosystem

For every item found, mark it as:
- **Directly Part of Tangent Forge**
- **Potentially Related**
- **Not Related but Possibly Useful**
- **Separate Project**

## 4. Identify Dependencies & Conflicts

- Note any contradictions between documents or descriptions.
- Highlight duplicate frameworks (e.g., Profit Pulse vs QPV variations).
- Flag outdated definitions or brand positioning.

## 5. Produce a Transfer-Ready Summary Package

Deliver the following outputs (Markdown only):
- **A Full Project Inventory**
- **A Categorized Map**
- **A Tangent-Forge Relationship Map**
- **A Conflict/Dependence Sheet**
- **A Recommended Canonical Version**
- **What Should Be Moved Into the TF Sandbox**
- **What Should Stay Separate**
- **What Needs Updating Before Merge**

## 6. Generate a Repo-Ready Structure

Output a suggested folder tree that would house all relevant material in the Tangent Forge repository.

## 7. Final Deliverable

Package all of the above into:
- `PROJECT_EXTRACT_SUMMARY.md`
- `TF_ALIGNMENT_NOTES.md`
- `REPO_STRUCTURE_SUGGESTED.md`

**Your tone:**
- Structured
- Neutral
- Analytical
- Zero assumptions
- No creative rewriting yet — just extraction and classification

Begin by confirming:
"Extractor Active — Send conversation history or files if needed."
```

## Expected Output

### PROJECT_EXTRACT_SUMMARY.md

```markdown
# Project Extraction Summary

## Project: [Name]
## Extracted: [Date]
## Status: Ready for Review

---

## Full Inventory

### Brand / Identity
- [ ] Logo concepts (3 variants)
- [ ] Color palette definitions
- [ ] Tagline iterations

### Utilities / Automations
- [ ] Invoice processor script
- [ ] OCR wrapper module
- [ ] Template generator

[... continues for all categories]

---

## Statistics
- Total items discovered: 47
- Directly TF-related: 23
- Potentially related: 12
- Separate projects: 8
- Misc/archive: 4
```

### TF_ALIGNMENT_NOTES.md

```markdown
# Tangent Forge Alignment Notes

## Conflicts Identified

| Item | Conflict | Resolution |
|------|----------|------------|
| QPV Matrix v2 | Differs from canonical v3 | Update to v3 |
| Brand colors | Uses old palette | Migrate to current |

## Dependencies

- Invoice processor depends on OCR wrapper
- OCR wrapper requires DocTR config

## Recommended Actions

1. **Immediate:** Update QPV Matrix reference
2. **Before Merge:** Reconcile brand assets
3. **Post-Merge:** Archive deprecated versions
```

### REPO_STRUCTURE_SUGGESTED.md

```markdown
# Suggested Repository Structure

tangent-forge/
├── brand/
│   ├── assets/
│   └── guidelines/
├── tools/
│   ├── invoice-processor/
│   └── ocr-wrapper/
├── frameworks/
│   ├── qpv-matrix/
│   └── cognitive-mesh/
└── archive/
    └── deprecated/
```

## Variants

### Quick Inventory (No Alignment)

```
Inventory this project:
1. List all significant items (code, docs, concepts, assets)
2. Categorize by type
3. Note any obvious duplicates or conflicts

Output: Simple inventory list with categories. No ecosystem alignment.
```

### Migration-Ready Version

```
Prepare this project for migration to [TARGET REPO].

Additional requirements:
- Generate migration checklist
- Identify breaking changes
- List files that need path updates
- Flag external dependencies

Output: Migration package ready for execution.
```

### Conflict-Focus Version

```
Analyze this project for conflicts with existing Tangent Forge assets.

Focus exclusively on:
- Naming conflicts
- Version mismatches
- Duplicate functionality
- Contradictory definitions

Output: Conflict report with resolution recommendations.
```
