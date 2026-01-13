# REVIEW-007: Visibility & Access Audit

**Category:** Review & Audit
**Complexity:** Medium
**Tags:** visibility, access, permissions, github, privacy, public, private
**Source:** TangentForge Governance System

---

## Purpose

Comprehensive audit of repository visibility settings, access controls, and privacy configurations. Ensures repositories have appropriate visibility for their content and proper access controls in place.

## When to Use

- Before changing a repository from private to public
- During quarterly access reviews
- When onboarding/offboarding team members
- Before open-sourcing internal projects
- During compliance audits
- When preparing for acquisition or audit

## Prerequisites

- Admin access to repository settings
- List of team members and their roles
- Understanding of data sensitivity in the repository
- Knowledge of compliance requirements (if any)

---

## Prompt

```
You are conducting a visibility and access audit for a software repository. Your goal is to ensure the repository has appropriate visibility settings and access controls for its content.

---

## PART 1: VISIBILITY ASSESSMENT

### 1.1 Current State
Document the current visibility configuration:

- **Repository visibility:** [ ] Public [ ] Private [ ] Internal (Enterprise)
- **GitHub/GitLab organization:** [Name]
- **Fork visibility:** [ ] Allowed [ ] Restricted
- **Wiki visibility:** [ ] Enabled [ ] Disabled
- **Issues visibility:** [ ] Public [ ] Private
- **Pages visibility:** [ ] Public [ ] Private [ ] None

### 1.2 Content Classification

Analyze repository contents for sensitivity:

#### Secrets & Credentials
- [ ] Scan git history for exposed secrets
- [ ] Check configuration files for hardcoded values
- [ ] Review environment files (.env, .env.example)
- [ ] Inspect CI/CD configurations for exposed variables

**Finding:** [ ] No secrets found [ ] Secrets in history (MUST clean before public) [ ] Active secrets (BLOCK public)

#### Proprietary Code
- [ ] Contains trade secrets or proprietary algorithms
- [ ] Contains licensed third-party code (check license compatibility)
- [ ] Contains client-specific implementations
- [ ] Contains competitive advantage code

**Finding:** [ ] Open-sourceable [ ] Requires review [ ] Must remain private

#### Sensitive Data
- [ ] Contains PII (names, emails, addresses)
- [ ] Contains test data with real user information
- [ ] Contains financial data
- [ ] Contains health information (HIPAA)
- [ ] Contains authentication fixtures

**Finding:** [ ] No sensitive data [ ] Sanitization needed [ ] Cannot be public

#### Documentation
- [ ] Contains internal processes
- [ ] Contains security documentation
- [ ] Contains architecture that reveals attack surface
- [ ] Contains API documentation with security details

**Finding:** [ ] Safe for public [ ] Redaction needed [ ] Keep internal

---

### 1.3 Visibility Decision Matrix

Use this matrix to determine appropriate visibility:

| Condition | Visibility | Rationale |
|-----------|------------|-----------|
| Contains active secrets | PRIVATE | Security risk |
| Contains secrets in history | PRIVATE until cleaned | Security risk |
| Contains PII | PRIVATE | Privacy/compliance |
| Contains proprietary algorithms | PRIVATE | Business value |
| Client work (without permission) | PRIVATE | Contractual |
| Internal tools (no external value) | PRIVATE or INTERNAL | No benefit to public |
| Open source library | PUBLIC | Community benefit |
| Portfolio/demo project | PUBLIC | Career benefit |
| Educational content | PUBLIC | Community benefit |
| Has OSS license + clean history | PUBLIC | Ready for community |

### 1.4 Visibility Recommendation

Based on analysis, recommend:

- [ ] **KEEP PRIVATE:** [Reason]
- [ ] **MAKE PUBLIC (after remediation):** [Required steps]
- [ ] **MAKE INTERNAL:** [Reason - Enterprise only]
- [ ] **ARCHIVE:** Repository no longer needed

---

## PART 2: ACCESS CONTROL AUDIT

### 2.1 Current Access List

Document who has access:

| User/Team | Role | Access Level | Last Active | Appropriate? |
|-----------|------|--------------|-------------|--------------|
| @username | Developer | Write | 2025-01-15 | ✅ Yes |
| @old-employee | Former | Write | 2024-06-01 | ❌ Revoke |
| Team: Backend | Team | Write | Active | ✅ Yes |
| Bot: CI | Service | Write | Active | ⚠️ Review scope |

### 2.2 Access Level Review

For each access type, verify appropriateness:

#### Admin Access
- [ ] Limited to repository owners/maintainers
- [ ] No inactive admins (>90 days)
- [ ] Service accounts have minimal admin rights
- [ ] All admins have 2FA enabled

#### Write Access
- [ ] Only active contributors
- [ ] External collaborators have expiration
- [ ] Bot/service accounts use least privilege
- [ ] No shared accounts

#### Read Access
- [ ] Appropriate for visibility setting
- [ ] External readers are intentional
- [ ] No access leakage through forks

### 2.3 Branch Protection Review

| Branch | Protected? | Required Reviews | Required Checks | Force Push Blocked? |
|--------|------------|------------------|-----------------|---------------------|
| main | [ ] Yes [ ] No | X approvals | [CI checks] | [ ] Yes [ ] No |
| develop | [ ] Yes [ ] No | X approvals | [checks] | [ ] Yes [ ] No |
| release/* | [ ] Yes [ ] No | X approvals | [checks] | [ ] Yes [ ] No |

### 2.4 Security Settings Review

- [ ] Vulnerability alerts enabled
- [ ] Dependabot enabled
- [ ] Secret scanning enabled (if available)
- [ ] Code scanning enabled (if applicable)
- [ ] Deploy keys reviewed and minimal

---

## PART 3: BEFORE GOING PUBLIC CHECKLIST

If recommending PUBLIC visibility, complete this checklist:

### 3.1 Pre-Flight Checks

#### History Cleaning
- [ ] Run `git log --all -p | grep -i password` - no results
- [ ] Run `git log --all -p | grep -i api_key` - no results
- [ ] Run `git log --all -p | grep -i secret` - review any results
- [ ] Use `git-filter-repo` or BFG to remove any secrets found
- [ ] Consider starting fresh if history is too contaminated

#### Required Files
- [ ] LICENSE file exists (MIT, Apache 2.0, GPL, etc.)
- [ ] README.md is complete and public-appropriate
- [ ] CONTRIBUTING.md explains how to contribute
- [ ] CODE_OF_CONDUCT.md sets community standards
- [ ] SECURITY.md explains how to report vulnerabilities

#### Configuration
- [ ] .gitignore includes .env, secrets, credentials
- [ ] .env.example has dummy values only
- [ ] No real URLs, IPs, or internal hostnames
- [ ] CI/CD secrets are stored in GitHub Secrets, not code

#### Documentation Review
- [ ] No internal jargon or company-specific references
- [ ] No links to internal resources
- [ ] No screenshots with sensitive information
- [ ] No references to internal systems

### 3.2 Post-Public Actions

After making public:
- [ ] Enable branch protection on main
- [ ] Enable vulnerability alerts
- [ ] Enable Dependabot
- [ ] Set up issue templates
- [ ] Set up PR template
- [ ] Add topics for discoverability
- [ ] Create initial release
- [ ] Monitor for issues/PRs

---

## PART 4: COMPLIANCE CONSIDERATIONS

### 4.1 License Compatibility

If using third-party code:

| Dependency | License | Compatible with your license? |
|------------|---------|-------------------------------|
| [Package] | MIT | ✅ Yes (permissive) |
| [Package] | GPL-3.0 | ⚠️ Must also use GPL |
| [Package] | Proprietary | ❌ Cannot open source |

### 4.2 Export Control

If applicable:
- [ ] No cryptography that requires export license
- [ ] No dual-use technology
- [ ] No country-specific restrictions

### 4.3 Data Protection

- [ ] GDPR compliant (no EU PII without consent)
- [ ] CCPA compliant (no CA resident data)
- [ ] No health data (HIPAA)
- [ ] No financial data (PCI-DSS)

---

## Output Format

### Visibility Audit Summary

**Repository:** [name]
**Current Visibility:** [Public/Private/Internal]
**Recommended Visibility:** [Public/Private/Internal]
**Risk Level:** [Low/Medium/High/Critical]

### Findings

| ID | Category | Finding | Severity | Action Required |
|----|----------|---------|----------|-----------------|
| VIS-001 | Secrets | API key in git history | CRITICAL | Clean history before public |
| VIS-002 | Access | Inactive admin @user | MEDIUM | Revoke access |
| VIS-003 | Protection | Main branch unprotected | HIGH | Enable branch protection |

### Access Review

| Action | User/Team | Current | Recommended | Reason |
|--------|-----------|---------|-------------|--------|
| REVOKE | @former-employee | Write | None | Left company |
| REDUCE | @contractor | Admin | Write | Least privilege |
| KEEP | @maintainer | Admin | Admin | Active owner |

### Remediation Checklist

Before changing visibility to PUBLIC:

- [ ] Step 1: [Specific action]
- [ ] Step 2: [Specific action]
- [ ] Step 3: [Specific action]

### Timeline

| Date | Milestone |
|------|-----------|
| Today | Complete audit |
| +7 days | Remediation complete |
| +14 days | Verification review |
| +21 days | Visibility change (if approved) |
```

---

## Expected Output

- Clear visibility recommendation with rationale
- Complete access list with action items
- Prioritized remediation checklist
- Timeline for visibility change (if applicable)
- Compliance status for relevant regulations

## Variants

### Quick Access Review (15 min)
Focus on Part 2 only - just audit who has access.

### Pre-Public Checklist Only
Focus on Part 3 only - when decision to go public is already made.

### Compliance-Focused
Deep dive on Part 4 with additional regulatory checks.

---

## Related Prompts

- REVIEW-005: Code Quality Review
- REVIEW-006: Security Review
- SYS-002: Secret Scanning

---

## Notes

This prompt supports the Tangent Forge governance system's visibility management features.
Last updated: 2025-12-30
