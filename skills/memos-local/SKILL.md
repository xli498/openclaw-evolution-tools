---
name: "memos-local"
description: "MemOS Local — a Memory Operating System for AI agents. Four cooperating memory layers, zero cloud dependency, automatic recall and save."
triggers: ["设计或维护本地记忆系统", "需要分层记忆检索与持久化", "排查智能体记忆召回问题"]
dependencies: []
version: 1.0.0
author: xli498
created: 2026-07-23
tags: [evolution, selflearn, skill]
---

# MemOS Local Plugin

> *"Your AI agent deserves a memory, not a sticky note."*

## What It Is

MemOS is a **Memory Operating System** for AI agents. Four cooperating memory layers, zero cloud dependency, automatic recall and save.

## Memory Layers

```
L1 — Traces:         Step-level grounded records (action + observation + reflection)
L2 — Policies:       Sub-task strategies induced across traces
L3 — World Models:   Compressed environmental cognition derived from L2 + L1
Skill —              Crystallized capabilities the agent can invoke directly
```

## Installation

```bash
openclaw plugins install @memtensor/memos-local-plugin
```

Or if the CLI times out:

```bash
cd ~/.openclaw/extensions
npm install @memtensor/memos-local-plugin
# Then manually add to openclaw.json:
# plugins.entries.memos-local-plugin = { enabled: true }
```

## Configuration

Runtime data lives at `~/.openclaw/memos-plugin/config.yaml`:

```yaml
viewer:
  port: 18799

embedding:
  provider: local        # No API key needed

llm:
  provider: host         # Uses host's LLM

algorithm:
  lightweightMemory:
    enabled: true        # Low-cost summaries; set false for full evolution

hub:
  enabled: false
```

## Tools

After gateway restart, the plugin exposes 6 tools:

| Tool | Purpose |
|------|---------|
| `memos_search` | Free-text memory search across 3 tiers |
| `memos_get` | Get specific memory by ID |
| `memos_timeline` | Timeline view of memories |
| `memos_environment` | Environment/context info |
| `memos_skill_list` | List crystallized skills |
| `memos_skill_get` | Get skill details |

## Viewer

After the plugin loads, visit `http://localhost:18799` for the Memory Viewer SPA.

## Research

- Paper: [arXiv:2507.03724](https://arxiv.org/abs/2507.03724)
- +43.70% accuracy vs OpenAI Memory
- Saves 35.24% memory tokens
- Docs: [memos-docs.openmem.net](https://memos-docs.openmem.net)
