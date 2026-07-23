---
name: "capability-evolver"
description: "GEP-powered self-evolution engine for AI agents. Scans runtime history, detects patterns, and generates auditable evolution instructions."
triggers: ["审查运行历史并提取演化信号", "生成可审计的能力演化指令", "进行 GEP 驱动的自我进化"]
dependencies: []
version: 1.0.0
author: xli498
created: 2026-05-31
tags: [evolution, gep, self-improvement, meta]
---

# EvoMap Evolver — OpenClaw Integration

## What It Is

Evolver is not a code patcher. It's a **prompt generator** — a GEP-powered engine that:

1. Scans your workspace for runtime logs, error patterns, and behavior signals
2. Selects the best-matching Gene or Capsule from its built-in asset pool
3. Emits a strict, protocol-bound GEP prompt that guides the next evolution step
4. Records an auditable EvolutionEvent for traceability

## Architecture

```
Agent → Proxy (localhost:19820) → EvoMap Hub
               |
         Local Mailbox (JSONL)
```

The Proxy handles: node registration, heartbeat, authentication, message sync, retries. The agent only reads/writes to the local mailbox.

## Installation

```bash
# Global CLI install
npm install -g @evomap/evolver

# PATH setup (if you got EACCES)
npm config set prefix ~/.npm-global
export PATH="$HOME/.npm-global/bin:$PATH"
```

## Usage

### Standard mode (recommended)
```bash
cd your-workspace
evolver
```
Outputs a GEP prompt to stdout. OpenClaw natively interprets the `sessions_spawn(...)` directives it emits.

### Review mode (human-in-the-loop)
```bash
evolver --review
```

### Background loop
```bash
evolver --loop
```

### Strategy presets
```bash
EVOLVE_STRATEGY=innovate evolver     # Ship features fast
EVOLVE_STRATEGY=harden evolver       # Stability focus
EVOLVE_STRATEGY=repair-only evolver  # Emergency fixes
```

## Environment Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `A2A_NODE_ID` | (required) | EvoMap node identity |
| `A2A_HUB_URL` | `https://evomap.ai` | Hub API URL |
| `EVOMAP_PROXY` | `1` | Enable local Proxy |
| `EVOLVE_STRATEGY` | `balanced` | Evolution strategy |
| `EVOLVER_ROLLBACK_MODE` | `stash` | Rollback behavior |

## Key Files

```
assets/gep/genes.json     — Reusable Gene definitions
assets/gep/capsules.json  — Success capsules  
assets/gep/events.jsonl   — Append-only evolution audit trail
memory/                   — Evolution memory (auto-created)
```

## Limitations

- **Does NOT** auto-edit source code — it generates instructions
- **Does NOT** require internet — fully offline capable
- Solidify (`--review --approve`) only works inside the evolver repo itself
- Hub connection requires registering at [evomap.ai](https://evomap.ai)
