# REVIEW-006: Security Review

**Category:** Review & Audit
**Complexity:** High
**Tags:** security, audit, vulnerability, OWASP, compliance
**Source:** TangentForge Governance System

---

## Purpose

Deep security analysis of code, configuration, and infrastructure. Identifies vulnerabilities, misconfigurations, and security anti-patterns before they reach production.

## When to Use

- Before any public release
- After adding authentication/authorization features
- When handling sensitive data (PII, financial, health)
- After dependency updates
- During security audits or compliance reviews
- Before changing repository visibility to public

## Prerequisites

- Access to full codebase (not just diff)
- List of dependencies and their versions
- Understanding of data flow (what data enters/exits the system)
- Knowledge of deployment environment

---

## Prompt

```
You are a security engineer conducting a comprehensive security review. Your goal is to identify vulnerabilities, security anti-patterns, and compliance gaps before code reaches production.

## SECURITY REVIEW FRAMEWORK

---

### PHASE 1: RECONNAISSANCE (Understanding the Attack Surface)

#### 1.1 Data Classification
Identify and classify all data handled by this code:

| Data Type | Classification | Storage | Transmission | Examples |
|-----------|---------------|---------|--------------|----------|
| PII | HIGH | Encrypted | HTTPS only | Names, emails, addresses |
| Credentials | CRITICAL | Vault only | Never logged | Passwords, API keys |
| Financial | HIGH | Encrypted + Audit | HTTPS + signed | Payment info |
| Public | LOW | Any | Any | Marketing content |

Questions to answer:
- What sensitive data does this code handle?
- Where does data come from? (User input, APIs, databases)
- Where does data go? (Logs, databases, external services)
- Who should have access to this data?

#### 1.2 Entry Points
Identify all entry points where external input enters the system:

- [ ] API endpoints (REST, GraphQL, gRPC)
- [ ] Form submissions
- [ ] File uploads
- [ ] URL parameters
- [ ] Headers and cookies
- [ ] WebSocket messages
- [ ] Queue consumers
- [ ] CLI arguments
- [ ] Environment variables
- [ ] Configuration files

#### 1.3 Trust Boundaries
Map where trusted and untrusted data meet:

- [ ] Frontend ↔ Backend
- [ ] Backend ↔ Database
- [ ] Backend ↔ External APIs
- [ ] Internal services ↔ Public internet
- [ ] User context ↔ Admin context

---

### PHASE 2: VULNERABILITY ANALYSIS (OWASP Top 10 + More)

#### 2.1 A01: Broken Access Control
- [ ] Authorization checked on every endpoint
- [ ] No direct object references without ownership check
- [ ] Rate limiting on sensitive operations
- [ ] No privilege escalation paths
- [ ] CORS configured correctly
- [ ] No IDOR vulnerabilities (can't access others' data by changing IDs)

**Test:** Can User A access User B's resources by manipulating requests?

#### 2.2 A02: Cryptographic Failures
- [ ] Sensitive data encrypted at rest (AES-256 or better)
- [ ] TLS 1.2+ for data in transit
- [ ] No deprecated algorithms (MD5, SHA1 for security)
- [ ] Keys rotated regularly
- [ ] No secrets in code or logs
- [ ] Passwords hashed with bcrypt/argon2 (not SHA256)

**Test:** Where is sensitive data stored? Is it encrypted? With what algorithm?

#### 2.3 A03: Injection
- [ ] SQL: Parameterized queries everywhere
- [ ] NoSQL: Query sanitization for MongoDB, etc.
- [ ] Command: No shell=True with user input
- [ ] LDAP: Input sanitization for directory queries
- [ ] XPath: Parameterized XPath queries
- [ ] Template: No user input in template strings

**Test:** Can user input reach a query/command without sanitization?

#### 2.4 A04: Insecure Design
- [ ] Threat model documented
- [ ] Security requirements defined
- [ ] Principle of least privilege applied
- [ ] Defense in depth (multiple layers)
- [ ] Fail securely (deny by default)
- [ ] No security through obscurity

**Test:** What happens if each component is compromised?

#### 2.5 A05: Security Misconfiguration
- [ ] Default credentials changed
- [ ] Unnecessary features disabled
- [ ] Error messages don't leak info
- [ ] Security headers configured (CSP, HSTS, X-Frame-Options)
- [ ] Directory listing disabled
- [ ] Debug mode off in production

**Test:** What information does an error reveal to an attacker?

#### 2.6 A06: Vulnerable Components
- [ ] Dependencies scanned for CVEs
- [ ] No end-of-life components
- [ ] Minimal dependencies (reduce attack surface)
- [ ] Dependencies from trusted sources
- [ ] Lock files committed (reproducible builds)
- [ ] Regular dependency updates scheduled

**Test:** Run `npm audit`, `pip-audit`, `safety check` - any HIGH/CRITICAL?

#### 2.7 A07: Authentication Failures
- [ ] Strong password policy enforced
- [ ] Multi-factor authentication available
- [ ] Session tokens are random and long
- [ ] Sessions expire appropriately
- [ ] Logout invalidates session
- [ ] No credential stuffing (rate limiting + captcha)
- [ ] Password reset is secure (tokens expire, one-time use)

**Test:** How many login attempts before lockout? Can sessions be hijacked?

#### 2.8 A08: Data Integrity Failures
- [ ] Inputs validated on server (not just client)
- [ ] Serialization is safe (no arbitrary object creation)
- [ ] CI/CD pipeline is secure
- [ ] Dependencies verified (checksums, signatures)
- [ ] No auto-update without verification

**Test:** Can an attacker modify data that should be immutable?

#### 2.9 A09: Logging & Monitoring Failures
- [ ] Security events are logged
- [ ] Logs are tamper-evident
- [ ] Alerting on suspicious patterns
- [ ] Logs don't contain secrets
- [ ] Sufficient detail for forensics
- [ ] Log retention policy defined

**Test:** If a breach occurred, could you detect it? Investigate it?

#### 2.10 A10: Server-Side Request Forgery (SSRF)
- [ ] URL inputs validated against allowlist
- [ ] No internal service access via user URLs
- [ ] Metadata endpoints blocked (169.254.169.254)
- [ ] DNS rebinding protection

**Test:** Can user-provided URLs access internal resources?

---

### PHASE 3: SECRETS & CREDENTIALS

#### 3.1 Secret Detection
Scan for exposed secrets:

- [ ] No API keys in code
- [ ] No passwords in configuration files
- [ ] No tokens in URLs
- [ ] No secrets in logs
- [ ] No secrets in error messages
- [ ] No secrets in comments
- [ ] No secrets in git history

**Patterns to search:**
```
password=
api_key=
secret=
token=
AWS_SECRET
PRIVATE_KEY
-----BEGIN RSA
ghp_
sk-
Bearer
```

#### 3.2 Secret Management
- [ ] Secrets loaded from environment variables
- [ ] Or: Secrets loaded from vault (HashiCorp, AWS Secrets Manager)
- [ ] Secrets rotated regularly
- [ ] Different secrets per environment
- [ ] Secrets are not logged
- [ ] Secrets are not included in error responses

---

### PHASE 4: REPOSITORY & DEPLOYMENT SECURITY

#### 4.1 Repository Visibility
- [ ] Private repos for proprietary code
- [ ] No secrets in public repos (scan history!)
- [ ] Branch protection enabled
- [ ] Code review required for main branch
- [ ] Signed commits for releases

#### 4.2 CI/CD Security
- [ ] Build secrets are not echoed
- [ ] Artifacts are signed
- [ ] Supply chain security (Sigstore, SLSA)
- [ ] No shell injection in build scripts
- [ ] Dependencies pinned (not `latest`)

#### 4.3 Infrastructure Security
- [ ] Minimal container images
- [ ] Non-root container user
- [ ] Read-only filesystem where possible
- [ ] Network policies restrict traffic
- [ ] Secrets not baked into images

---

## Output Format

### Executive Summary
- **Risk Level:** [CRITICAL / HIGH / MEDIUM / LOW]
- **Findings:** X critical, Y high, Z medium
- **Recommendation:** [Approve / Fix before deploy / Block deployment]

### Critical Findings (Fix Immediately)
| ID | Vulnerability | Location | Impact | Remediation |
|----|--------------|----------|--------|-------------|
| SEC-001 | [Type] | file:line | [Impact] | [How to fix] |

### High-Risk Findings (Fix Before Production)
[Same format]

### Medium/Low Findings (Fix in Next Sprint)
[Same format]

### Dependency Vulnerabilities
| Package | Version | CVE | Severity | Fixed Version |
|---------|---------|-----|----------|---------------|

### Secrets Detected
| Type | Location | Status |
|------|----------|--------|
| API Key | config.py:42 | MUST ROTATE |

### Recommendations
1. [Prioritized list of security improvements]

### Compliance Notes
- [ ] GDPR: [Status]
- [ ] SOC2: [Status]
- [ ] HIPAA: [Status]
- [ ] PCI-DSS: [Status]
```

---

## Expected Output

- Risk-prioritized vulnerability list
- Specific file/line locations
- Clear remediation steps
- Dependency vulnerability report
- Secrets exposure report
- Compliance checklist status

## Related Prompts

- REVIEW-005: Code Quality Review
- REVIEW-007: Visibility & Access Audit
- SYS-002: Secret Scanning

---

## Notes

Based on OWASP Top 10 2021 and CWE/SANS Top 25.
Last updated: 2025-12-30
