# Tangent Forge Agent Rules & Prompt Library

A complete governance system for dev agents and a curated prompt library for structured workflows.

---

## Quick Start

### 1. Bootstrap a Repository

Hand this prompt to any dev agent:

```
Read .tangent-forge/SETUP_PROMPT.md and execute the Master Setup Prompt to bootstrap governance in this repository.
```

### 2. Enable Prompt Coach

Add to your AI tool's system prompt or custom instructions:

```
You have access to the Tangent Forge Prompt Library. When you notice the user could benefit from a structured prompt (cleanup, review, audit, documentation), briefly mention the relevant prompt ID. If no prompt fits, offer to generate one in JSON schema format.
```

### 3. Use a Prompt

Reference by ID in any conversation:

> "Run DEV-003 (Comprehensive System Review) on this codebase"

---

## What's Included

```
tangent-forge-agent-rules/
├── README.md                    # This file - overview of the system
├── AGENT_RULES.json          # Machine-readable ruleset
├── AGENT_RULES.md            # Human-readable documentation
├── SETUP_PROMPT.md           # Bootstrap prompt for new repos
├── DEPLOYMENT_GUIDE.md          # Deployment and rollout guide
├── schemas/
│   └── agent_rules.schema.json
│
└── prompt-library/
    ├── PROMPT_INDEX.json     # Machine-readable prompt catalog
    ├── PROMPT_INDEX.md       # Human-readable prompt index
    ├── PROMPT_COACH.md       # Meta-prompt for recommendations
    ├── ingest_prompt.py      # Script to add new prompts
    ├── schemas/
    │   └── prompt_library.schema.json
    └── prompts/
        ├── dev/                 # Development process prompts (DEV-001, DEV-002, DEV-003)
        ├── docs/                # Documentation task prompts (DOCS-001, DOCS-002, DOCS-003)
        ├── review/              # Code/process review prompts (REVIEW-001 through REVIEW-007)
        ├── system/              # System-level audit prompts (SYS-001 through SYS-006)
        ├── extraction/       # Data extraction prompts
        └── meta/                # Meta-task prompts (META-001, META-002)
```

---

## Agent Rules

### Philosophy

> **Observe → Index → Classify → Optimize → Govern**

### Global Constraints

| Constraint | Description |
|------------|-------------|
| No Deletions | Archive with log entry instead |
| Rollback Plan | Every change must be reversible |
| Log All Changes | Every modification is recorded |
| Stop on Ambiguity | Ask, don't guess |
| Index Over Action | Classify before changing |

### Domains

| Domain | Key Rules |
|--------|-----------|
| **Code** | Single entrypoint, modularity, refactor safety |
| **Testing** | Baseline first, parity tests, artifacts gitignored |
| **Documentation** | Classification zones, never delete, track open work |
| **Scripts** | 4-label system (ACTIVE/REFERENCE/ARCHIVE/DEAD) |
| **Data** | 5-bucket classification, canonical versions |
| **Security** | No hardcoded secrets, env vars only |

See [AGENT_RULES.md](AGENT_RULES.md) for complete documentation.

---

## Prompt Library

### Categories

| ID | Category | Description |
|----|----------|-------------|
| DEV | Development | Code review, architecture, refactoring |
| DOCS | Documentation | Generation, governance, reconciliation |
| REVIEW | Audit | Classification, compliance, cleanup |
| SYS | System | Optimization, performance, drive audit |
| META | Orchestration | Prompt engineering, project extraction |

### Key Prompts

| ID | Name | Use When |
|----|------|----------|
| DEV-001 | Master Ruleset Execution | Starting any governed task |
| DEV-003 | Comprehensive System Review | Deep architecture review |
| DOCS-002 | Documentation Reconciliation | After any code change |
| REVIEW-002 | Script Cleanup Sequence | Inheriting messy codebase |
| META-001 | Project Extractor | Consolidating projects |

See [prompt-library/PROMPT_INDEX.md](prompt-library/PROMPT_INDEX.md) for full catalog.

---

## Installation

### Python Dependencies

```bash
cd prompt-library
pip install -r requirements.txt
```

Required packages:
- `jsonschema>=4.0.0` - Schema validation
- `pyperclip>=1.8.0` - Clipboard support

### Validation

Verify the library is set up correctly:

```bash
cd prompt-library
python validate.py
```

---

## Adding New Prompts

### Method 1: Interactive

```bash
cd prompt-library
python ingest_prompt.py --interactive
```

### Method 2: From JSON

When an AI generates a prompt in schema format:

```bash
python ingest_prompt.py new_prompt.json
```

### Method 3: From Clipboard

Copy JSON from AI response, then:

```bash
python ingest_prompt.py --from-clipboard
```

### Get Help

```bash
python ingest_prompt.py --help
```

### JSON Schema for New Prompts

```json
{
  "id": "CATEGORY-NNN",
  "name": "Human-Readable Name",
  "category": "dev|docs|review|system|extraction|meta",
  "description": "What this prompt does",
  "tags": ["searchable", "tags"],
  "complexity": "low|medium|high",
  "when_to_use": "Trigger conditions",
  "prompt": "The full prompt text..."
}
```

---

## Prompt Coach

The Prompt Coach is a meta-instruction that makes any AI aware of your library.

### How It Works

1. Add the coach instruction to your AI's system prompt
2. AI passively watches for patterns in your conversation
3. When a structured prompt would help, it suggests one
4. If no prompt exists, it offers to generate one in schema format

### Pattern Recognition

| You Say | Coach Suggests |
|---------|----------------|
| "clean up these scripts" | REVIEW-002: Script Cleanup |
| "review this architecture" | DEV-003: System Review |
| "docs are outdated" | DOCS-002: Reconciliation |
| "optimize performance" | SYS-005: Bottleneck Analysis |
| (describes repetitive task) | "Want me to create a reusable prompt?" |

See [prompt-library/PROMPT_COACH.md](prompt-library/PROMPT_COACH.md) for full instruction.

---

## Integration

### Claude.ai / ChatGPT

Add to custom instructions:
```
You have access to the Tangent Forge Prompt Library...
[paste from PROMPT_COACH.md]
```

### Claude Code / Cursor / Windsurf

Add to workspace rules or project config.

### API / MCP Server

Expose as tools:
- `search_prompts(query)` — Find matching prompts
- `get_prompt(id)` — Retrieve full prompt text
- `add_prompt(json)` — Add to library

---

## Extending the System

### Custom Categories

Add to `PROMPT_INDEX.json`:

```json
"categories": {
  "custom": {
    "id": "CUSTOM",
    "name": "My Custom Category",
    "description": "Prompts for specific workflow",
    "path": "prompts/custom/"
  }
}
```

### Custom Rules

Add to `AGENT_RULES.json`:

```json
"domains": {
  "custom": {
    "id": "CUSTOM",
    "name": "My Custom Domain",
    "rules": [...]
  }
}
```

### Validate Changes

Both JSON files have schemas for validation:
- `schemas/agent_rules.schema.json`
- `prompt-library/schemas/prompt_library.schema.json`

---

## ML Enhancement Path

The system works without ML, but can be enhanced:

| Tier | Capability | Requirement |
|------|------------|-------------|
| 1 | Pattern matching | Just the prompt coach instruction |
| 2 | Semantic search | Embed prompts, vector similarity |
| 3 | Learning system | Track usage, retrain recommendations |

---

## License

Internal use. Tangent Forge.

---

## Contributing

1. Generate prompt using schema format
2. Run `python ingest_prompt.py <file.json>`
3. Verify prompt file created correctly
4. Update any related documentation
