# DEV-003: Comprehensive System Review

**Category:** Development & Code  
**Complexity:** High  
**Tags:** architecture, review, ocr, extraction  
**Source:** dev_agent_playbook.md

---

## Purpose

Staff-to-Principal level review of extraction/OCR systems. Produces actionable recommendations for architecture, quality, and evolution. Designed for production-adjacent systems, not prototypes.

## When to Use

- Before major refactoring efforts
- When onboarding to a complex codebase
- For periodic architecture reviews
- When planning v2 of a system

## Prompt

```
You are acting as a Staff-to-Principal level systems engineer and applied AI architect.

Your task is to review, critique, and recommend improvements to a system whose purpose is:

> Extracting structured data from construction blueprints and plan PDFs, including title block detection, revision tracking, drawing number extraction, and template-based OCR zone detection.

The system includes:
- Multiple Python scripts for blueprint analysis and OCR
- Template-based zone configurations in JSON
- Page-level PDF analysis with OCR annotations
- Integration with an OCR engine (DocTR)
- Optional downstream integration with Procore APIs

You are reviewing this as a **production-adjacent system**, not a prototype.

---

## 1️⃣ SYSTEM COMPREHENSION CHECK

First, restate your understanding of:
- The system's **end-to-end data flow**
- The **core responsibilities** of each major script category
- How configuration (templates/zones) drives behavior
- Where OCR, heuristics, and template matching interact

Call out any **ambiguities or implicit assumptions** you detect.

---

## 2️⃣ ARCHITECTURE & STRUCTURE REVIEW

Evaluate the system architecture across these dimensions:

### a) Modularity & Separation of Concerns
- Are OCR, detection, parsing, normalization, and output clearly separated?
- Are scripts acting as pipelines or monoliths?
- Where is logic duplicated across `analyze_*` variants?

### b) Configuration vs Code
- Is behavior correctly driven by config files vs hard-coded logic?
- Are template zone definitions expressive enough?
- Are there opportunities for schema validation or versioning?

### c) Scalability & Maintainability
- How easy is it to add:
  - a new blueprint template?
  - a new title block layout?
  - a new output field?
- Identify coupling risks or brittle dependencies.

Provide concrete refactor recommendations.

---

## 3️⃣ OCR & EXTRACTION QUALITY ANALYSIS

Analyze the extraction approach in depth:

- OCR reliability assumptions (resolution, rotation, skew)
- Sensitivity to:
  - scan quality
  - multi-page sets
  - rotated or mirrored sheets
- Title block detection robustness
- Template matching confidence thresholds

Answer explicitly:
- What failure modes are *likely but currently unhandled*?
- Where should probabilistic scoring or confidence metrics be added?

---

## 4️⃣ TEMPLATE & ZONE SYSTEM REVIEW

Critique the template-zone strategy:

- Are zones too rigid or too permissive?
- How well does the system handle:
  - minor layout drift
  - different DPI or page sizes
  - consultant-specific variations?

Propose improvements such as:
- Anchor-based zones
- Relative geometry
- Template confidence scoring
- Fallback strategies when template match fails

---

## 5️⃣ FUNCTIONAL COMPLETENESS CHECK

Assess whether the system fully supports its stated goals:

- Revision tracking accuracy across drawing sets
- Drawing number normalization consistency
- Cross-page or cross-revision linking
- Handling of missing, partial, or conflicting data

Identify:
- Missing features
- Implicit manual steps
- Data integrity risks

---

## 6️⃣ ERROR HANDLING, DEBUGGING & OBSERVABILITY

Evaluate:
- Logging quality and usefulness
- Debug overlays / artifacts
- Ability to diagnose OCR or template failures
- Reproducibility of extraction results

Recommend:
- Logging structure
- Debug modes
- Intermediate artifacts worth persisting
- Metrics worth tracking (confidence, hit rate, failures)

---

## 7️⃣ INTEGRATION & PIPELINE READINESS

Review the system's readiness for:
- Procore or external API ingestion
- Batch processing at scale
- CI-driven validation
- Downstream consumers (databases, reviewers, auditors)

Call out:
- Where contracts/interfaces should be formalized
- Where validation or normalization layers are missing

---

## 8️⃣ PERFORMANCE & COST CONSIDERATIONS

Analyze:
- OCR cost hotspots
- Redundant processing
- Opportunities for caching or pre-classification
- Parallelization vs determinism tradeoffs

Recommend optimizations *without sacrificing accuracy*.

---

## 9️⃣ DESIGN EVOLUTION RECOMMENDATIONS

Propose:
- A cleaner **v2 architecture** (modules, flow, responsibilities)
- Which scripts should be merged, deleted, or promoted to core modules
- Whether a rules engine, pipeline framework, or plugin architecture would help

Include:
- A high-level architecture diagram description (textual is fine)
- A phased refactor plan (low-risk → high-impact)

---

## 🔟 PRIORITIZED ACTION PLAN

Finish with:
- Top 5 **highest-leverage improvements**
- Quick wins (1–2 day effort)
- Medium refactors (1–2 weeks)
- Strategic upgrades (foundational)

Label each item with:
- Impact
- Risk
- Effort

---

## OUTPUT FORMAT

Structure your response with clear section headers.
Be specific, technical, and opinionated.
Assume the system will be maintained long-term.
Avoid generic advice—tie every recommendation to this system's context.
```

## Expected Output

A structured report with 10 sections covering:
1. System comprehension summary
2. Architecture assessment with refactor recommendations
3. OCR quality analysis with failure modes
4. Template system critique with improvements
5. Functional completeness gaps
6. Observability recommendations
7. Integration readiness assessment
8. Performance optimization opportunities
9. v2 architecture proposal
10. Prioritized action plan with effort/impact labels

## Variants

### Harsh Reviewer Version

Add this prefix:

```
HARSH REVIEW MODE: Be brutally honest. Call out every anti-pattern, every shortcut, every technical debt. Don't soften feedback. Assume I can handle direct criticism.
```

### Security-Focused Version

Replace section 6 with:

```
## 6️⃣ SECURITY & COMPLIANCE REVIEW

Evaluate:
- Input validation and sanitization
- File handling security (path traversal, zip bombs)
- API key / credential management
- Data privacy considerations (PII in blueprints)
- Audit trail completeness

Recommend:
- Security hardening priorities
- Compliance gaps (SOC2, GDPR if applicable)
- Threat model for common attack vectors
```

### Performance-Only Audit

```
PERFORMANCE AUDIT ONLY

Review this system focusing exclusively on:
1. OCR cost per page
2. Processing time bottlenecks
3. Memory usage patterns
4. Parallelization opportunities
5. Caching strategies
6. I/O optimization

Output: Performance profile + ranked optimization recommendations with expected impact.
```

### Design-for-Productization

```
PRODUCTIZATION REVIEW

Review this system as if it needs to become a sellable SaaS product:
1. Multi-tenant considerations
2. API design for external consumers
3. Billing/metering touchpoints
4. Self-service onboarding requirements
5. Support/debugging tooling needs
6. Documentation for customers vs developers

Output: Gap analysis + productization roadmap.
```
