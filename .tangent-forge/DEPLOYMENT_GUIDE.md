# Governance Deployment Guide

## Quick Start - Deploy to All Repos

### Step 1: Review the Repo List

The deployment script targets these active repos:

**PathForge Apps:**
- prompt-finder
- pathfinder
- geo-finder
- therapist-finder

**Google Workspace Apps:**
- tangent-core
- brand-color-harmonizer
- rubric-to-comment-ai

**Other Products:**
- drive-cleanup-toolkit
- receiptiq
- invoice-sorter
- docs-to-notion

### Step 2: Run Dry Run (Preview)

```powershell
cd U:\TANGENT_FORGE\tools\prompt-library_builder
.\deploy_governance_to_repos.ps1 -DryRun
```

This shows what would happen without making changes.

### Step 3: Execute Deployment

```powershell
.\deploy_governance_to_repos.ps1
```

**What it does:**
1. Clones repos to `U:\TF_REPOS\` (or pulls latest if already cloned)
2. Copies `.tangent-forge/` folder to each repo
3. Commits with message: "chore: add Tangent Forge governance system"
4. Pushes to remote

### Step 4: Verify

Check a few repos on GitHub to confirm `.tangent-forge/` folder appears.

---

## What Gets Deployed

Each repo receives:

```
.tangent-forge/
├── AGENT_RULES.json          # Machine-readable governance rules
├── AGENT_RULES.md             # Human-readable documentation
├── SETUP_PROMPT.md            # Bootstrap instructions for AI
└── schemas/
    └── agent_rules.schema.json
```

---

## Customization

### Change Target Directory

```powershell
.\deploy_governance_to_repos.ps1 -ReposDir "C:\MyRepos"
```

### Add/Remove Repos

Edit `deploy_governance_to_repos.ps1` line 32-47:

```powershell
$Repos = @(
    "repo-name-1",
    "repo-name-2"
)
```

---

## Troubleshooting

### "Git clone failed"
- Verify you have access to the repo
- Check GitHub authentication (SSH keys or token)

### "Push failed"
- Commits are saved locally
- Manually push later: `cd U:\TF_REPOS\<repo>; git push`

### "Already exists - skipping"
- Repo already has `.tangent-forge/` folder
- Manually update if needed

---

## After Deployment

Once folders are deployed, you can bootstrap governance in each repo individually:

```
Read .tangent-forge/SETUP_PROMPT.md and execute the Master Setup Prompt
```

This will:
- Audit the repo structure
- Update `.gitignore`
- Create PR template (optional)
- Apply repo-specific governance rules
