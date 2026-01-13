# Tangent Forge Prompt Library

**Version:** 1.0.0  
**Updated:** 2025-12-25  
**Purpose:** Curated collection of production-ready prompts organized by domain

---

## How to Use This Library

1. **Browse by Category** — Find prompts organized by domain below
2. **Search by Tag** — Use the tag index at the bottom
3. **Reference by ID** — Each prompt has a unique ID (e.g., DEV-001)
4. **Load Programmatically** — Parse `PROMPT_INDEX.json` for automation

---

## Categories

| ID | Category | Description | Count |
|----|----------|-------------|-------|
| DEV | Development & Code | Code review, refactoring, debugging | 3 |
| DOCS | Documentation | Doc generation, review, governance | 3 |
| REVIEW | Review & Audit | Code review, system audit, compliance | 5 |
| SYS | System & Infrastructure | System optimization, drive cleanup | 6 |
| META | Meta & Orchestration | Prompt engineering, agent orchestration | 2 |

---

## Development & Code (DEV)

| ID | Name | Complexity | Tags |
|----|------|------------|------|
| [DEV-001](#dev-001) | Master Ruleset Execution | High | governance, hygiene, master |
| [DEV-002](#dev-002) | Governance Compliance Audit | Medium | audit, compliance, review |
| [DEV-003](#dev-003) | Comprehensive System Review | High | architecture, review, ocr |

---

## Documentation (DOCS)

| ID | Name | Complexity | Tags |
|----|------|------------|------|
| [DOCS-001](#docs-001) | Documentation Suite Generator | High | documentation, generator |
| [DOCS-002](#docs-002) | Documentation Reconciliation Pass | Medium | reconciliation, workflow |
| [DOCS-003](#docs-003) | Documentation Audit | Low | audit, read-only |

---

## Review & Audit (REVIEW)

| ID | Name | Complexity | Tags |
|----|------|------------|------|
| [REVIEW-001](#review-001) | Script Classification Pass | Medium | scripts, classification |
| [REVIEW-002](#review-002) | Script Cleanup Sequence | High | scripts, cleanup, sequence |
| [REVIEW-003](#review-003) | Data Asset Classification | Medium | data, csv, json |
| [REVIEW-004](#review-004) | UI/UX Design Review | Medium | ui, ux, accessibility |
| [REVIEW-005](#review-005) | Code Quality Review | Medium | code, quality |

---

## System & Infrastructure (SYS)

| ID | Name | Complexity | Tags |
|----|------|------------|------|
| [SYS-001](#sys-001) | System Baseline Snapshot | Medium | baseline, snapshot |
| [SYS-002](#sys-002) | Installed Applications Audit | Medium | applications, inventory |
| [SYS-003](#sys-003) | Background Processes Audit | Medium | processes, services |
| [SYS-004](#sys-004) | Drive File System Audit | High | drive, filesystem |
| [SYS-005](#sys-005) | Performance Bottleneck Analysis | High | performance, bottleneck |
| [SYS-006](#sys-006) | Lean Boot Profile Design | Medium | boot, optimization |

---

## Meta & Orchestration (META)

| ID | Name | Complexity | Tags |
|----|------|------------|------|
| [META-001](#meta-001) | Project Extractor | High | extraction, mapping |
| [META-002](#meta-002) | Unified Master Setup | High | setup, cleanup, master |

---

## Tag Index

| Tag | Prompts |
|-----|---------|
| architecture | DEV-003 |
| audit | DEV-002, DOCS-003, SYS-001, SYS-002, SYS-003, SYS-004 |
| baseline | SYS-001 |
| boot | SYS-006 |
| bottleneck | SYS-005 |
| classification | REVIEW-001, REVIEW-003 |
| cleanup | REVIEW-001, REVIEW-002, META-002 |
| code | REVIEW-005 |
| compliance | DEV-002, DOCS-003 |
| csv | REVIEW-003 |
| data | REVIEW-003 |
| documentation | DOCS-001 |
| drive | SYS-004 |
| extraction | DEV-003, META-001 |
| filesystem | SYS-004 |
| generator | DOCS-001 |
| governance | DEV-001 |
| hygiene | DEV-001 |
| inventory | SYS-002 |
| json | REVIEW-003 |
| mapping | META-001 |
| master | DEV-001, META-002 |
| ocr | DEV-003 |
| optimization | SYS-006 |
| performance | SYS-005, SYS-006 |
| processes | SYS-003 |
| quality | REVIEW-005 |
| read-only | DOCS-003 |
| reconciliation | DOCS-002 |
| review | DEV-002, DEV-003, REVIEW-004, REVIEW-005 |
| scripts | REVIEW-001, REVIEW-002 |
| sequence | REVIEW-002 |
| services | SYS-003 |
| setup | META-002 |
| snapshot | SYS-001 |
| ui | REVIEW-004 |
| ux | REVIEW-004 |
| workflow | DOCS-002 |

---

## Prompt Details

### DEV-001
**Master Ruleset Execution**

Execute project tasks while adhering to strict governance and hygiene standards. Combines Staff Engineer and Documentation Auditor roles.

**File:** `prompts/dev/DEV-001_master_ruleset_execution.md`

---

### DEV-002
**Governance Compliance Audit**

Post-execution compliance review. Use after DEV-001 to verify all rules were followed.

**File:** `prompts/dev/DEV-002_governance_compliance_audit.md`

---

### DEV-003
**Comprehensive System Review**

Staff-to-Principal level review of extraction/OCR systems. Covers architecture, modularity, OCR quality, template systems, and evolution planning.

**File:** `prompts/dev/DEV-003_comprehensive_system_review.md`

---

### DOCS-001
**Documentation Suite Generator**

Create complete documentation suite: README, CONTRIBUTING, indexes, public/dev/private separation, PR templates.

**File:** `prompts/docs/DOCS-001_documentation_suite_generator.md`

---

### DOCS-002
**Documentation Reconciliation Pass**

Post-change workflow to ensure all docs reflect current state. Mandatory after any code change.

**File:** `prompts/docs/DOCS-002_documentation_reconciliation.md`

---

### DOCS-003
**Documentation Audit**

Read-only audit of documentation. Produces compliance report without making changes.

**File:** `prompts/docs/DOCS-003_documentation_audit.md`

---

### REVIEW-001
**Script Classification Pass**

Classify scripts using 4-label system: ACTIVE, REFERENCE, ARCHIVE, DEAD.

**File:** `prompts/review/REVIEW-001_script_classification.md`

---

### REVIEW-002
**Script Cleanup Sequence**

Full 6-prompt sequence: Inventory → Classify → Registry → Archive Headers → Move Files → Validate.

**File:** `prompts/review/REVIEW-002_script_cleanup_sequence.md`

---

### REVIEW-003
**Data Asset Classification**

Classify CSV/JSON files into: FIXTURE, CONFIG, GENERATED, REFERENCE, ARCHIVE.

**File:** `prompts/review/REVIEW-003_data_asset_classification.md`

---

### REVIEW-004
**UI/UX Design Review**

Evaluate UI for visual hierarchy, accessibility, intuitiveness, and interaction affordances.

**File:** `prompts/review/REVIEW-004_uiux_design_review.md`

---

### REVIEW-005
**Code Quality Review**

Senior engineer review covering completeness, API design, test coverage, and security.

**File:** `prompts/review/REVIEW-005_code_quality_review.md`

---

### SYS-001
**System Baseline Snapshot**

Create ground truth snapshot: OS, hardware, storage, package managers, virtualization, security.

**File:** `prompts/system/SYS-001_system_baseline_snapshot.md`

---

### SYS-002
**Installed Applications Audit**

Inventory all installed apps. Classify as Core OS, Developer Tool, Productivity, Background Utility, Bloat.

**File:** `prompts/system/SYS-002_installed_apps_audit.md`

---

### SYS-003
**Background Processes Audit**

Inventory running processes and services. Classify as Critical, Optional, Vendor Noise, Suspect.

**File:** `prompts/system/SYS-003_background_processes_audit.md`

---

### SYS-004
**Drive File System Audit**

Structural index of all drives: folder taxonomy, large files, duplicates, dev artifact sprawl.

**File:** `prompts/system/SYS-004_drive_filesystem_audit.md`

---

### SYS-005
**Performance Bottleneck Analysis**

Identify bottlenecks under idle, typical, and peak workloads. Analyze I/O, RAM, CPU, GPU.

**File:** `prompts/system/SYS-005_performance_bottleneck_analysis.md`

---

### SYS-006
**Lean Boot Profile Design**

Design optimized boot profile for dev work, OCR processing, multi-monitor stability.

**File:** `prompts/system/SYS-006_lean_boot_profile.md`

---

### META-001
**Project Extractor**

Scan project content, classify by category, cross-reference with ecosystem, identify conflicts.

**File:** `prompts/meta/META-001_project_extractor.md`

---

### META-002
**Unified Master Setup**

Combined cleanup of scripts, documentation, and data assets in one sequential pass.

**File:** `prompts/meta/META-002_unified_master_setup.md`

---

## Adding New Prompts

1. Create prompt file in appropriate `prompts/{category}/` folder
2. Use naming convention: `{ID}_{snake_case_name}.md`
3. Add entry to `PROMPT_INDEX.json`
4. Update this index with new entry

### Prompt File Template

```markdown
# {PROMPT_ID}: {Prompt Name}

**Category:** {Category}  
**Complexity:** {Low|Medium|High}  
**Tags:** {comma-separated tags}  
**Source:** {Original source file if adapted}

---

## Purpose

{Brief description of what this prompt does}

## When to Use

{Trigger conditions or use cases}

## Prompt

```
{The actual prompt text}
```

## Expected Output

{Description of expected output format}

## Variants

{Optional: alternative versions for different contexts}
```
