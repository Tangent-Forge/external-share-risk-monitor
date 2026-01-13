# DOCS-003: Documentation Audit

**Category:** Documentation  
**Complexity:** Medium  
**Tags:** audit, compliance, governance  

---

## Purpose

Audit repository documentation for completeness, accuracy, and compliance with Tangent Forge governance standards.

## When to Use

- Monthly or quarterly maintenance cycles.
- Before a major release or milestone.
- When onboarding a new development team or agent.

## Prompt

```markdown
Perform a comprehensive Documentation Audit of this repository.

Objective:
Verify documentation completeness, accuracy, and compliance with Tangent Forge governance standards.

Process:

1. **Inventory All Documentation**
   - List all markdown files in the repository
   - Categorize by location (root, docs/public, docs/dev, docs/private, docs/archive)
   - Identify orphaned docs (not linked in DOCUMENTATION_INDEX.md)

2. **Check Required Artifacts**
   Verify presence and quality of:
   - [ ] README.md (purpose, installation, usage, examples)
   - [ ] DOCUMENTATION_INDEX.md (all docs linked, properly categorized)
   - [ ] docs/dev/DEVELOPMENT_LOG.md (active, deferred, completed sections)
   - [ ] docs/dev/SCRIPT_STATUS_REGISTRY.md (all scripts classified)
   - [ ] docs/dev/DATA_ASSET_REGISTRY.md (all data files classified)
   - [ ] .gitignore (sensitive paths covered)

3. **Validate Documentation Headers**
   Each doc should have:
   - Purpose statement
   - Audience (Public/Dev/Internal)
   - Status (Active/Draft/Archived)
   - Last Updated date

4. **Check for Broken References**
   - File links that point to non-existent files
   - Outdated paths
   - Missing images or assets

5. **Verify Archival Compliance**
   - All archived docs have DEVELOPMENT_LOG entries
   - Archive headers present on archived scripts
   - No orphaned TODOs in archived files

6. **Produce Audit Report**
   List:
   - Compliance score (X of Y required artifacts present)
   - Missing or incomplete artifacts
   - Broken references
   - Orphaned documentation
   - Recommended fixes (prioritized)
   - Overall status: COMPLIANT / NON-COMPLIANT / PARTIAL

**Output Format:**
Structured report with pass/fail for each check and actionable recommendations.
```

## Expected Output

- Comprehensive audit report mapping files to governance requirements.
- Prioritized list of documentation debt.
- Overall compliance status (COMPLIANT/NON-COMPLIANT/PARTIAL).

## Notes

- This prompt is read-only; it does not modify documentation.
- Use DOCS-002 (Reconciliation) to apply fixes identified in this audit.
