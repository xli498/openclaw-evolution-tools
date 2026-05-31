# Self-Improving Agent

> *"An agent that doesn't learn from its mistakes is just a very expensive echo."*

## What It Is

A structured learning system that captures experience, prevents repeated failures, and crystallizes knowledge into reusable skills.

## Features

- **7 Trigger Conditions**: Error, correction, knowledge gap, better approach, capability request, task completion review, academic extension
- **Structured Records**: LEARNINGS / ERRORS / FEATURE_REQUESTS — three-file system
- **Experience Evolution**: Promotion mechanism (≥3 occurrences = auto-promote to skill)
- **Safety Guards**: ADL drift prevention + VFM value-first scoring
- **Operations Log**: JSONL-format CHANGELOG for machine-readable audit

## Installation

```bash
# Via OpenClaw add
openclaw add https://github.com/yanhongxi-openclaw/proactive-self-improving-agent

# Or manual clone
git clone https://github.com/yanhongxi-openclaw/proactive-self-improving-agent.git
```

## Usage

The skill auto-loads when an agent starts. Ensure `.learnings/` exists in your workspace:

```bash
mkdir -p .learnings
```

## Trigger Flow

```
Error Occurred
    │
    ▼
Trigger Detected ──▶ Record to ERRORS.md / LEARNINGS.md
    │
    ▼
Retry Counter ≥ 3? ──▶ Yes: Auto-promote to skill extraction
    │                       │
    No                      ▼
    │              Create skill in skills/<name>/
    ▼                      
Continue             Update CHANGELOG.jsonl
```

## Related

- Repository: [claw-opus/proactive-self-improving-agent](https://github.com/claw-opus/proactive-self-improving-agent)
- Also available: [lanyasheng/self-improving-agent](https://github.com/lanyasheng/self-improving-agent) (anti-loop hardened fork)
