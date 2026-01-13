# DOCS-002: Documentation Reconciliation Pass

**Category:** Documentation  
**Complexity:** Medium  
**Tags:** reconciliation, post-change, workflow  
**Source:** _documentation_prompts.md

---

## Purpose

Ensure all documentation accurately reflects the current state of the repository after code changes. This is a mandatory post-change workflow.

## When to Use

- After any code change
- After any file structure change
- After archiving or reorganizing
- Before closing a PR
- After any refactoring

## Prompt

```
You have completed changes to this repository. Now perform a Documentation Reconciliation Pass.

Objective:
Ensure all documentation accurately reflects the current state of the repository after your changes.

Process:

1. **Summarize what changed**
   - Files moved, renamed, archived, created, or removed from tracking
   - Functionality added, modified, or deprecated
   - Configuration changes

2. **Review Core Docs and Dev Governance Docs**
   Check each for accuracy:
   - README.md
   - DOCUMENTATION_INDEX.md
   - SCRIPT_STATUS_REGISTRY.md
   - DATA_ASSET_REGISTRY.md
   - DEVELOPMENT_LOG.md
   - Any other docs that reference changed files

3. **Update all affected documents**
   - Fix broken references
   - Update descriptions to match new behavior
   - Add new entries for new files
   - Mark archived items appropriately
   - Log any unresolved questions or deferred decisions in DEVELOPMENT_LOG.md

4. **Produce a final report**
   List:
   - Updated docs (with brief description of changes)
   - Reviewed-but-unchanged docs (with reason no update needed)
   - Any new log entries created

**Mandatory Rule:**
Work is not considered complete until documentation reflects reality or the reason for no update is explicitly stated.
```

## Expected Output

```markdown
## Documentation Reconciliation Report

### Changes Summary
- Moved `analyze_v3.py` → `scripts/archive/analyze_v3.py`
- Created `utils/pdf_utils.py` (extracted from main script)
- Updated `config/templates.json` with new zone definitions

### Documents Updated

| Document | Changes Made |
|----------|--------------|
| README.md | Updated installation steps, added new CLI flags |
| DOCUMENTATION_INDEX.md | Added link to new API_REFERENCE.md |
| SCRIPT_STATUS_REGISTRY.md | Moved analyze_v3.py to Archived section |
| DEVELOPMENT_LOG.md | Added DL-045: Caching implementation deferred |

### Documents Reviewed (No Changes Needed)

| Document | Reason |
|----------|--------|
| CONTRIBUTING.md | No workflow changes |
| docs/dev/ARCHITECTURE.md | Structure unchanged |

### New Log Entries

- **DL-045:** Caching implementation
  - Status: Deferred
  - Reason: Out of scope for current sprint
  - Revisit: v1.3.0

### Reconciliation Status: COMPLETE ✓
```

## Variants

### Quick Reconciliation (Minimal Changes)

```
Quick Documentation Reconciliation

Changes made: [BRIEF DESCRIPTION]

Check and update if needed:
- [ ] README.md
- [ ] DOCUMENTATION_INDEX.md
- [ ] SCRIPT_STATUS_REGISTRY.md (if scripts changed)
- [ ] DATA_ASSET_REGISTRY.md (if data files changed)
- [ ] DEVELOPMENT_LOG.md (if work deferred)

Report: Which docs updated, which unchanged, why.
```

### Pre-Commit Hook Version

```
PRE-COMMIT DOC CHECK

Files changed in this commit:
[LIST OF CHANGED FILES]

For each changed file, verify:
1. Is it referenced in any documentation?
2. Are those references still accurate?
3. Does any registry need updating?

Output:
- PASS (all docs accurate) or
- FAIL (list required doc updates)
```

### Batch Reconciliation

```
Batch Documentation Reconciliation

Multiple changes occurred:
1. [Change 1]
2. [Change 2]
3. [Change 3]

Reconcile all changes in a single pass:
- Consolidate all doc updates
- Avoid redundant edits
- Produce unified report

Output: Single reconciliation report covering all changes.
```

## Standing Rule

Add this to agent system prompts for automatic enforcement:

```
**Mandatory Rule (Documentation Reconciliation Pass):**
Any change to code, scripts, file structure, data assets, tests, or archive status MUST be followed by a Documentation Reconciliation Pass.

**Work is not considered complete until:**
1. Documentation (including all Registry and Log files) accurately reflects the current repo state.
2. OR, you explicitly state why no documentation changes are required.

- Never silently archive unfinished work.
- Never skip reconciliation.
```
