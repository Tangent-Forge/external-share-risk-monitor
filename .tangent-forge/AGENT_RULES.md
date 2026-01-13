# Tangent Forge Agent Rules

**Version:** 1.0.0  
**Updated:** 2025-12-25  
**Purpose:** Canonical ruleset for dev agents operating in Tangent Forge repositories  
**Audience:** Dev agents, human developers, onboarding  
**Status:** Active

---

## Philosophy

> **Observe → Index → Classify → Optimize → Govern**

All agent operations follow this sequence. Action comes after understanding.

---

## Global Constraints

These apply to every operation, in every domain:

| Constraint | Description |
|------------|-------------|
| **No Deletions** | Never delete files outright; archive with log entry |
| **Rollback Plan** | Every change must have a reversal path |
| **Log All Changes** | Every modification is recorded |
| **Stop on Ambiguity** | If unclear, STOP and ask—don't guess |
| **Index Over Action** | Prefer classification and recommendations over immediate changes |
| **Mark Unknowns** | Anything unclear is marked as `TODO` |

---

## Domain: Code Hygiene & Architecture

| ID | Rule | Severity |
|----|------|----------|
| CODE-001 | **Single Entrypoint** — All main execution routes through one non-interactive CLI entrypoint | Required |
| CODE-002 | **Modularity** — Extraction, OCR, PDF, and config in separate `/core`, `/utils`, `/config` modules | Required |
| CODE-003 | **Non-Interactive** — Use argparse for deterministic execution; prompts only as fallback | Required |
| CODE-004 | **Refactor Safety** — Any refactor must produce zero behavior change vs. baseline | Required |
| CODE-005 | **Granularity** — Keep changes under ~500 lines per PR | Recommended |

---

## Domain: Testing & Artifact Hygiene

| ID | Rule | Severity |
|----|------|----------|
| TEST-001 | **Baseline First** — Freeze golden output baseline before modifying extraction logic | Required |
| TEST-002 | **Parity Test** — Mandatory test comparing new outputs to baseline (normalize whitespace, sort rows) | Required |
| TEST-003 | **Generated Outputs** — Route all run outputs to `artifacts/` and gitignore | Required |

---

## Domain: Documentation Governance

| ID | Rule | Severity |
|----|------|----------|
| DOC-001 | **Classification** — Docs in `docs/public/` (user-safe), `docs/dev/` (developer), `docs/private/` (internal, gitignored) | Required |
| DOC-002 | **Never Delete** — Move superseded docs to `docs/archive/` | Required |
| DOC-003 | **No Silent Archival** — Open ideas require `DEVELOPMENT_LOG.md` entry before archiving | Required |
| DOC-004 | **Discoverability** — Every doc linked exactly once in `docs/DOCUMENTATION_INDEX.md` | Required |
| DOC-005 | **Header Standard** — Every doc has: Purpose, Audience, Status, Last Updated | Recommended |
| DOC-006 | **Reconciliation** — Any code change triggers a Documentation Reconciliation Pass | Required |
| DOC-007 | **Folder Organization** — No overlapping folders (e.g., dev/, dev_log/, dev_plan/); use DOCS-004 prompt for consolidation | Recommended |

---

## Domain: Script Classification & Archival

### The 4-Label System

| Label | Meaning |
|-------|---------|
| 🟢 **ACTIVE** | Imported, called by CLI, used in tests, known current |
| 🟡 **REFERENCE** | Not executed but has reusable logic, OCR tuning, good comments |
| 🔵 **ARCHIVE** | Superseded by newer version, won't be modified |
| 🔴 **DEAD** | One-off experiments, debug variants, unclear origin |

> ⚠️ **DEAD ≠ DELETE** — DEAD means "park safely and document why"

| ID | Rule | Severity |
|----|------|----------|
| SCRIPT-001 | **4-Label System** — All scripts classified as ACTIVE/REFERENCE/ARCHIVE/DEAD | Required |
| SCRIPT-002 | **Registry** — Record in `docs/dev/SCRIPT_STATUS_REGISTRY.md` | Required |
| SCRIPT-003 | **Archive Header** — Archived/Dead scripts get status header block | Required |
| SCRIPT-004 | **Folder Structure** — Organize into `scripts/active/`, `scripts/reference/`, `scripts/archive/` | Recommended |

### Archive Header Template

```python
# ARCHIVE STATUS: Archived
# SUPERSEDED BY: scripts/active/analyze_v4.py
# REASON: Logic consolidated into v4
# TRACKING: DL-021
```

---

## Domain: Data Asset Governance

### Classification Buckets

| Bucket | Destination | Description |
|--------|-------------|-------------|
| FIXTURE | `tests/fixtures/` | Test data, baselines, golden files |
| CONFIG | `config/` | Templates, mappings, label configs |
| GENERATED | `artifacts/` (gitignored) | Runtime outputs, reports, debug dumps |
| REFERENCE | `data/reference/` | Useful sample inputs (small only) |
| ARCHIVE | `data/archive/` | Old versions, superseded files |

| ID | Rule | Severity |
|----|------|----------|
| DATA-001 | **Classification** — All CSV/JSON classified into buckets | Required |
| DATA-002 | **Registry** — Record in `docs/dev/DATA_ASSET_REGISTRY.md` | Required |
| DATA-003 | **Canonical Version** — Document which version is canonical when multiples exist | Required |

---

## Domain: Security & Secrets

| ID | Rule | Severity |
|----|------|----------|
| SEC-001 | **No Hardcoded Secrets** — Never commit API keys, passwords, tokens | Critical |
| SEC-002 | **Environment Variables** — All secrets from env vars | Critical |
| SEC-003 | **Gitignore Enforcement** — Sensitive paths must be gitignored | Critical |
| SEC-004 | **Example Files** — Provide `.env.example` with dummy values | Recommended |

### Patterns to Scan

- `sk-*` (OpenAI)
- `sk-ant-*` (Anthropic)
- `AIza*` (Google)
- `AKIA*` (AWS)
- `ghp_*`, `gho_*` (GitHub)
- `xox*` (Slack)
- `-----BEGIN` (Private keys)

---

## Domain: System & Drive Auditing

| ID | Rule | Severity |
|----|------|----------|
| SYS-001 | **Read-Only Mode** — Default to read-only until explicitly authorized | Required |
| SYS-002 | **Baseline Snapshot** — Create ground truth before any optimization | Required |
| SYS-003 | **File Registry** — Maintain system file registry as cleanup control plane | Recommended |

---

## Workflows

### Documentation Reconciliation Pass

**Trigger:** After any code, script, file structure, data asset, test, or archive status change

1. Summarize what changed
2. Review core docs (README, DOCUMENTATION_INDEX, registries, logs)
3. Update all affected documents
4. Log unresolved questions in DEVELOPMENT_LOG
5. Produce final report

> **Completion Rule:** Work is not complete until documentation reflects reality

### Script Cleanup Sequence

1. Inventory (no changes)
2. Classify (ACTIVE/REFERENCE/ARCHIVE/DEAD)
3. Create registries and governance docs
4. Add archive headers + log open items
5. Move files to status folders
6. Validate and report

### System Audit Sequence

0. System Context Snapshot (Baseline)
1. Installed Applications Audit
2. Background Processes & Services
3. Startup & Auto-Run Governance
4. Drive & File System Audit
5. Performance Bottleneck Analysis
6. Config & Policy Optimization
7. Cleanup & Governance Playbook

---

## Required Artifacts

Every governed repository should have:

- `docs/DOCUMENTATION_INDEX.md`
- `docs/dev/DEVELOPMENT_LOG.md`
- `docs/dev/SCRIPT_STATUS_REGISTRY.md`
- `docs/dev/DATA_ASSET_REGISTRY.md`
- `.gitignore` (properly configured)

Optional but recommended:

- `docs/dev/ARCHIVING_STANDARD.md`
- `.github/PULL_REQUEST_TEMPLATE.md`

---

## Usage

### For Agents

Load `AGENT_RULES.json` into system context or reference this document.

### For Humans

Use the PR checklist and reconciliation workflow to enforce rules manually.

### For Automation

Parse `AGENT_RULES.json` to build pre-commit hooks, CI checks, or custom tooling.
