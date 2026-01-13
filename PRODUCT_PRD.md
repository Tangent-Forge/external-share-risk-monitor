# PRODUCT PRD: External Share Risk Monitor

## 1. Executive Summary

**External Share Risk Monitor** is a security-focused admin tool that scans Google Drive for files shared externally (outside the organization) and provides risk assessment, reporting, and remediation workflows to prevent data leakage.

## 2. Target Persona

- **Security Officers**: Monitoring data leakage and compliance violations
- **IT Admins**: Managing external access policies
- **Compliance Teams**: Ensuring data governance standards
- **Legal Teams**: Reviewing sensitive document sharing

## 3. Core Features (v1.0)

- **External Share Scanner**: Scan Drive for files shared with external users or publicly
- **Risk Scoring Engine**: Assign risk levels based on file sensitivity and access type
- **Remediation Dashboard**: Bulk remove external access or revoke public links
- **Audit Logging**: Track all remediation actions for compliance
- **Scheduled Reports**: Weekly risk reports sent to security team

## 4. Technical Architecture

- **Framework**: Apps Script with `Drive` API (v3) + `Admin SDK`
- **Performance**: Use `pageSize` and `nextPageToken` for efficient large-scale scanning
- **Data Persistence**: Google Sheet for current "Risk Benchmarks"

## 5. Build Checklist (v1.0 Build-Out)

- [ ] **BUILD-001**: Implement `RiskScanner.gs` - Query `Drive.Files.list` with `q='visibility != private'`
- [ ] **BUILD-002**: Implement `RiskScorer.gs` - Calculate risk scores based on file type and access
- [ ] **BUILD-003**: Implement `RemediationModule.gs` - Bulk revoke external access
- [ ] **BUILD-004**: UI: "Risk Dashboard" Sidebar with KPI cards
- [ ] **BUILD-005**: Reporting: "Weekly Risk Digest" via Gmail

---
*Status: Initial Planning | Readiness: Agent-Ready (Scaffold Tier)*
