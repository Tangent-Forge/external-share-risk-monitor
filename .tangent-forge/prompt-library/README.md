# Tangent Forge Prompt Library

**Version:** 1.0
**Last Updated:** 2026-01-02
**Purpose:** Specialized prompts for governance, development, and system audits

---

## 📚 About This Library

This prompt library provides pre-written, tested prompts for common repository governance and development tasks. Each prompt is designed to be handed directly to an AI agent (like Claude) to perform specific audits, reviews, or setup tasks.

**Part of:** Tangent Forge Agent Rules Framework
**Source:** U:/TANGENT_FORGE/tools/prompt-library_builder/

---

## 📂 Prompt Categories

### 🛠️ Development (dev/)

| Prompt | Purpose | When to Use |
|--------|---------|-------------|
| **DEV-001** | Master Ruleset Execution | Apply all governance rules to new feature development |
| **DEV-002** | Governance Compliance Audit | Check repository compliance with Tangent Forge rules |
| **DEV-003** | Comprehensive System Review | Deep-dive architectural review and optimization recommendations |

### 📖 Documentation (docs/)

| Prompt | Purpose | When to Use |
|--------|---------|-------------|
| **DOCS-001** | Documentation Suite Generator | Generate CONTRIBUTING.md, API docs, update README |
| **DOCS-002** | Documentation Reconciliation | Ensure docs match code after changes |
| **DOCS-003** | Documentation Audit | Find outdated, missing, or inconsistent documentation |
| **DOCS-004** | Documentation Folder Consolidation | Consolidate overlapping or redundant doc folders |

### 🔍 Review (review/)

| Prompt | Purpose | When to Use |
|--------|---------|-------------|
| **REVIEW-001** | Script Classification | Classify all scripts as ACTIVE/REFERENCE/ARCHIVE/DEAD |
| **REVIEW-002** | Script Cleanup Sequence | Add archive headers, create archive README |
| **REVIEW-003** | Data Asset Classification | Classify all CSV/JSON/config files |
| **REVIEW-004** | UI/UX Design Review | Evaluate user experience and accessibility |
| **REVIEW-005** | Code Quality Review | Check for magic values, test coverage, dead code |
| **REVIEW-006** | Security Review | Find hardcoded secrets, insecure patterns |
| **REVIEW-007** | Visibility/Access Audit | Find hidden features, improve discoverability |

### 🖥️ System (system/)

| Prompt | Purpose | When to Use |
|--------|---------|-------------|
| **SYS-001** | System Baseline Snapshot | Capture performance metrics before major changes |
| **SYS-002** | Installed Apps Audit | Survey installed applications and dependencies |
| **SYS-003** | Background Processes Audit | Identify resource-consuming processes |
| **SYS-004** | Drive/Filesystem Audit | Analyze disk usage and organize files |
| **SYS-005** | Performance Bottleneck Analysis | Identify and fix performance issues |
| **SYS-006** | Lean Boot Profile | Optimize system startup time |

### 🎯 Meta (meta/)

| Prompt | Purpose | When to Use |
|--------|---------|-------------|
| **META-001** | Project Extractor | Extract project requirements from documentation |
| **META-002** | Unified Master Setup | Bootstrap entire governance system in one pass |

---

## 🚀 How to Use These Prompts

### Method 1: Direct Copy-Paste

1. Read the prompt file (e.g., `prompts/review/REVIEW-006_security_review.md`)
2. Copy the entire content
3. Paste into Claude or your AI agent
4. The agent will execute the audit/review/task

### Method 2: Reference in Conversation

```
"Please run REVIEW-006 (Security Review) from the Tangent Forge prompt library
located at .tangent-forge/prompt-library/prompts/review/REVIEW-006_security_review.md"
```

### Method 3: Automated Execution (Future)

```bash
# Planned: Command-line runner
tangent-forge run REVIEW-006
```

---

## 📋 Common Workflows

### After Writing New Code

1. **DOCS-002** - Documentation Reconciliation
2. **REVIEW-005** - Code Quality Review
3. **REVIEW-006** - Security Review (if handling sensitive data)

### Before Major Release

1. **DEV-002** - Governance Compliance Audit
2. **DOCS-003** - Documentation Audit
3. **REVIEW-007** - Visibility/Access Audit
4. **SYS-001** - System Baseline Snapshot

### Repository Cleanup

1. **REVIEW-001** - Script Classification
2. **REVIEW-002** - Script Cleanup Sequence
3. **REVIEW-003** - Data Asset Classification
4. **DOCS-004** - Documentation Folder Consolidation (after DOCS-005 organization)

### Documentation Organization

1. **DOCS-003** - Documentation Audit (analyze current state)
2. **DOCS-005** - Full Documentation Organization (implement plan)
3. **DOCS-004** - Folder Consolidation (eliminate overlaps)
4. **DOCS-002** - Documentation Reconciliation (update links)

### Performance Optimization

1. **SYS-001** - System Baseline Snapshot (before)
2. **SYS-005** - Performance Bottleneck Analysis
3. **DEV-003** - Comprehensive System Review
4. **SYS-001** - System Baseline Snapshot (after comparison)

### New Repository Setup

1. **META-002** - Unified Master Setup (bootstraps everything)
2. **DEV-002** - Governance Compliance Audit (verify setup)

---

## 📊 Prompt Execution History (This Repository)

| Date | Prompt | Outcome | Notes |
|------|--------|---------|-------|
| 2026-01-02 | REVIEW-001 | ✅ Complete | Classified 77 Python files (REVIEW-001 report) |
| 2026-01-02 | REVIEW-002 | ✅ Complete | Archived 2 scripts, created archive README |
| 2026-01-02 | DOCS-003 | ✅ Complete | Audited 112 markdown files, health score 72/100 |
| 2026-01-02 | DOCS-002 | ✅ Complete | Priority 1 reconciliation, updated USER_GUIDE |
| 2026-01-02 | DEV-002 | ✅ Complete | Governance audit PASS, 0 violations |
| 2026-01-02 | DOCS-005 | ✅ Complete | Organized 41 files into 6 categories |
| 2026-01-02 | DOCS-004 | ✅ Complete | Consolidated 4 overlapping folders (14→10) |
| 2026-01-01 | REVIEW-006 | ✅ Complete | Found 3 security issues (SEC-001, SEC-002, SEC-003) |
| 2026-01-01 | REVIEW-002 | ✅ Complete | Classified 3 archived GUIs, created archive README |
| 2026-01-01 | REVIEW-001 | ✅ Complete | Classified 5 GUIs, 15 scripts |
| 2026-01-01 | REVIEW-003 | ✅ Complete | Classified 7 data assets |
| 2026-01-01 | REVIEW-004 | ✅ Complete | UX Score: 68.5/100 → identified improvements |
| 2026-01-01 | REVIEW-005 | ✅ Complete | Code Quality: 71/100 → identified gaps |
| 2026-01-01 | DOCS-002 | ✅ Complete | Identified missing documentation |
| 2026-01-01 | DEV-003 | ⏳ Running | OCR system review (72/100) |
| 2026-01-01 | REVIEW-007 | ✅ Complete | Feature visibility audit - exposed hidden ROI editor |

---

## 🔗 Related Documentation

- **[AGENT_RULES.md](../AGENT_RULES.md)** - Core governance framework documentation
- **[AGENT_RULES.json](../AGENT_RULES.json)** - Machine-readable ruleset
- **[SETUP_PROMPT.md](../SETUP_PROMPT.md)** - Guide for setting up governance in new repos
- **[DEPLOYMENT_GUIDE.md](../DEPLOYMENT_GUIDE.md)** - Deployment and rollout guide

---

## 📝 Prompt Naming Convention

Format: `{CATEGORY}-{NUMBER}_{descriptive_name}.md`

Examples:
- `REVIEW-001_script_classification.md`
- `DEV-003_comprehensive_system_review.md`
- `SYS-005_performance_bottleneck_analysis.md`

**Categories:**
- `DEV` - Development processes
- `DOCS` - Documentation tasks
- `REVIEW` - Code/process reviews
- `SYS` - System-level audits
- `META` - Meta-tasks (setup, extraction)

---

## 🎯 Quick Reference

**Need to find security issues?** → REVIEW-006
**Documentation out of date?** → DOCS-002 or DOCS-003
**Slow performance?** → SYS-005
**New repository setup?** → META-002
**Code quality concerns?** → REVIEW-005
**Hidden features?** → REVIEW-007
**Script organization messy?** → REVIEW-001 + REVIEW-002

---

## 💡 Tips

1. **Run audits regularly** - Don't wait for problems to appear
2. **Combine prompts** - Many work well together (e.g., REVIEW-001 → REVIEW-002)
3. **Track execution** - Document what you ran and when (see table above)
4. **Update prompts** - If you improve a prompt, update it in the library
5. **Create new prompts** - Follow the naming convention and PR template

---

**Repository:** DocTR_Process
**Framework:** Tangent Forge Agent Rules v1.0
**Prompt Count:** 21 specialized prompts
**Status:** Active - Ready for use

---

*This library is part of the Tangent Forge governance framework.*
*All prompts are versioned and tested.*
