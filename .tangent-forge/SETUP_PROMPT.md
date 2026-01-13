# Agent Rules Setup Prompt

**Purpose:** Hand this prompt to a dev agent to bootstrap the Tangent Forge governance system in any repository.

---

## Master Setup Prompt

```
You are a repository governance agent. Your task is to set up the Tangent Forge Agent Rules system in this repository.

## Source Files

You have access to:
- AGENT_RULES.json — Machine-readable ruleset
- AGENT_RULES.md — Human-readable documentation

## Hard Rules

- Read-only until explicitly authorized to create files
- No deletions of any kind
- Stop and ask if anything is ambiguous
- Mark unknowns as TODO

## Setup Sequence

### Phase 1: Audit Current State (No Changes)

1. Scan the repository structure
2. Identify existing governance artifacts:
   - README.md
   - docs/ folder structure
   - .gitignore
   - Any existing registries or logs
3. Report what exists vs. what's missing from the required artifacts list

### Phase 2: Create Folder Structure

Create these directories if they don't exist:
- docs/
- docs/public/
- docs/dev/
- docs/private/
- docs/archive/

### Phase 3: Create Governance Artifacts

Create these files using templates from AGENT_RULES.md:

1. `docs/DOCUMENTATION_INDEX.md`
   - Link all existing docs
   - Separate into Public / Dev / Private / Archive sections

2. `docs/dev/DEVELOPMENT_LOG.md`
   - Sections: Active, Deferred, Completed, Archived but Unresolved
   - Initialize with any open TODOs found during scan

3. `docs/dev/SCRIPT_STATUS_REGISTRY.md`
   - Sections: Active, Reference, Archived, Dead
   - Populate by classifying existing scripts

4. `docs/dev/DATA_ASSET_REGISTRY.md`
   - Classify all CSV/JSON files found
   - Record path, category, canonical status

### Phase 4: Update .gitignore

Ensure .gitignore includes:
```
# Tangent Forge Governance
docs/private/
artifacts/

# Secrets
*.env
!*.env.example
*.key
*.pem
*.p12

# Generated
__pycache__/
*.pyc
node_modules/
.venv/
```

### Phase 5: Install Rules Files

Copy to repository root:
- `.tangent-forge/AGENT_RULES.json`
- `.tangent-forge/AGENT_RULES.md`
- `.tangent-forge/schemas/agent_rules.schema.json`

### Phase 6: Create PR Template (Optional)

If `.github/` exists, create `.github/PULL_REQUEST_TEMPLATE.md`:

```markdown
## Documentation Reconciliation Checklist

### Core Docs
- [ ] README.md reviewed/updated
- [ ] DOCUMENTATION_INDEX.md reviewed/updated

### Script & Data Governance
- [ ] SCRIPT_STATUS_REGISTRY.md updated (if scripts changed)
- [ ] DATA_ASSET_REGISTRY.md updated (if CSV/JSON/config changed)
- [ ] DEVELOPMENT_LOG.md updated (if anything archived or deferred)

### Archival Safety
- [ ] No unfinished work archived without a log entry
- [ ] Archived items reference superseding files or tracking IDs

### Commit/Ignore Standard
- [ ] Generated outputs routed to `/artifacts/` and gitignored
- [ ] Internal docs in `/docs/private/` and gitignored

**Explanation (if any boxes unchecked):**
[Provide justification here]
```

### Phase 7: Validation Report

Produce a final report:
- Files created
- Files updated
- Compliance status for each required artifact
- Any TODOs or unresolved items
- Next recommended steps

## Output Format

For each file created or updated, provide:
1. Full path
2. Full content
3. Brief rationale

End with a compliance checklist showing pass/fail for each required artifact.
```

---

## Quick Verification Prompt

After setup, use this to verify everything is in place:

```
Verify this repository's compliance with Tangent Forge Agent Rules.

Check:
1. All required artifacts exist
2. .gitignore covers sensitive paths
3. All docs are linked in DOCUMENTATION_INDEX.md
4. All scripts are classified in SCRIPT_STATUS_REGISTRY.md
5. No open TODOs exist without DEVELOPMENT_LOG entries

Output:
- Compliance score (X of Y artifacts present)
- List of violations with recommended fixes
- Overall status: COMPLIANT / NON-COMPLIANT / PARTIAL
```

---

## Standing Rule (System Prompt Injection)

Add this to any dev agent's system prompt for ongoing enforcement:

```
You are operating in a repository with Tangent Forge governance.

**Mandatory Rule (Documentation Reconciliation Pass):**
Any change to code, scripts, file structure, data assets, tests, or archive status MUST be followed by a Documentation Reconciliation Pass.

**Work is not considered complete until:**
1. Documentation (including all Registry and Log files) accurately reflects the current repo state.
2. OR, you explicitly state why no documentation changes are required.

- Never silently archive unfinished work.
- Never skip reconciliation.
- Reference AGENT_RULES.json for specific rule IDs if needed.
```
