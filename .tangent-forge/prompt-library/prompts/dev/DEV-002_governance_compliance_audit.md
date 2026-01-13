# DEV-002: Governance Compliance Audit

**Category:** Development & Code  
**Complexity:** Medium  
**Tags:** audit, compliance, review  
**Source:** dev_agent_playbook.md

---

## Purpose

Perform a compliance review on changes made by a development agent. Use this after DEV-001 or any development task to verify all governance rules were followed.

## When to Use

- After any development task completes
- Before merging PRs
- When validating agent output
- As part of code review process

## Prompt

```
You are a Project Auditor. Your task is to perform a compliance review on the last set of changes made by the development agent.

INPUT: [Paste the agent's full output (code and compliance checklist) here]

---

### 🔎 AUDIT CHECKLIST

Review the input against the Master Ruleset and report on the following:

1. **Rule D & F (Parity Check):** Was a baseline output or a new test added? Did the agent explicitly confirm that no extraction behavior was changed?

2. **Rule A & B (Code Structure):** Was a new module created (e.g., `pdf_utils.py`)? Was the original script modified to use the new module? Is there still an interactive prompt?

3. **Rule H, I, J (Documentation):**
    - List all new or modified documentation files. Is each file correctly placed under `/public`, `/dev`, or `/private`?
    - If any topic was deferred or only partially implemented, was a corresponding entry created/updated in the `DEVELOPMENT_LOG.md`?

4. **Rule K (Discoverability):** If a new documentation file was created, confirm it was added to the `DOCUMENTATION_INDEX.md`.

### 📝 COMPLIANCE REPORT

Deliver a pass/fail assessment for each rule, and for any **fail** item, provide the exact file change required to bring it into compliance.

- **Outcome:** [PASS/FAIL]
- **Violations:** [List all violations and the recommended fix for each.]
```

## Expected Output

```markdown
## Compliance Report

### Rule Assessment

| Rule | Status | Notes |
|------|--------|-------|
| D - Refactor Safety | PASS | Baseline frozen, no behavior change |
| F - Parity Test | PASS | test_extraction_parity.py added |
| A - Single Entrypoint | PASS | CLI via `python -m project` |
| B - Modularity | PASS | pdf_utils.py extracted to /utils |
| H - Doc Classification | PASS | All docs in correct zones |
| I - No Deletions | PASS | No files deleted |
| J - Idea Tracking | FAIL | Open TODO not logged |
| K - Discoverability | PASS | Index updated |

### Violations

**Rule J Violation:**
- Location: `docs/dev/ARCHITECTURE.md` line 45
- Issue: Contains `TODO: implement caching` without DEVELOPMENT_LOG entry
- Fix: Add entry `DL-XXX: Implement caching layer` to DEVELOPMENT_LOG.md

### Outcome: FAIL (1 violation)

### Required Actions
1. Add DEVELOPMENT_LOG entry for caching TODO
2. Update ARCHITECTURE.md to reference the log entry ID
```

## Variants

### Quick Check (Trusted Agent)

```
Quick compliance check on these changes:

[PASTE CHANGES]

Check only:
- No deletions?
- Open work logged?
- Docs indexed?

Output: PASS/FAIL + any violations.
```

### Pre-Merge Gate

```
PRE-MERGE COMPLIANCE GATE

Changes to review:
[PASTE PR DIFF OR SUMMARY]

This PR cannot merge until ALL rules pass:
- [ ] Rule D: Parity maintained
- [ ] Rule F: Tests added
- [ ] Rule H: Docs classified correctly
- [ ] Rule I: No deletions
- [ ] Rule J: Open work logged
- [ ] Rule K: Index updated

Output: MERGE READY or BLOCKED + required fixes.
```

### Batch Audit

```
Audit these multiple changes for compliance:

Change 1: [description]
Change 2: [description]
Change 3: [description]

For each change, report:
- Compliance status
- Any violations
- Recommended fixes

Summary: X of Y changes compliant.
```
