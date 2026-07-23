---
name: "gep-evolution-flow"
description: "GEP Evolution Flow — standardized protocol for scanning runtime history, detecting patterns, and generating auditable evolution instructions."
triggers: ["需要将经验信号转成 evolution draft", "执行 GEP 审查或 promotion 流程", "审计演化对象与证据链"]
dependencies: []
version: 1.0.0
author: xli498
created: 2026-07-23
tags: [evolution, selflearn, skill]
---

# GEP Evolution Flow — From Signals to Skills

> *"Evolution is not optional. Adapt or die."* — EvoMap

## The GEP Protocol (v1.10.3)

The Genome Evolution Protocol standardizes agent evolution into 5 objects:

### 0. Mutation (The Trigger)
The reason evolution is needed. Detected from runtime signals.

```json
{
  "type": "Mutation",
  "id": "mut_<timestamp>",
  "category": "repair|optimize|innovate|explore",
  "trigger_signals": ["tool_bypass", "user_feature_request"],
  "risk_level": "low|medium|high"
}
```

### 1. PersonalityState (The Mood)
The agent's current mental state, controlling how boldly it evolves.

```json
{
  "type": "PersonalityState",
  "rigor": 0.85,
  "creativity": 0.3,
  "verbosity": 0.2,
  "risk_tolerance": 0.4,
  "obedience": 0.9
}
```

### 2. EvolutionEvent (The Record)
Auditable trace of what happened and whether it succeeded.

### 3. Gene (The Knowledge)
Reusable evolution pattern — the "DNA" of your agent's improvement history.

| Field | Purpose |
|-------|---------|
| `id` | Descriptive name: `gene_tool_integration_pipeline` |
| `category` | repair / optimize / innovate / explore |
| `signals_match` | Signal patterns that trigger this gene |
| `strategy` | Step-by-step execution plan |
| `constraints` | Blast radius limits |
| `validation` | Commands to verify success |
| `routing_hint` | Cost tier + reasoning level |

### 4. Capsule (The Success Pattern)
A proven evolution that worked. Future evolutions reference capsules first before creating new genes.

## Common Signals

| Signal | Meaning |
|--------|---------|
| `tool_bypass` | Agent used shell/exec instead of registered tool |
| `user_feature_request` | User asked for new capability |
| `protocol_drift` | Evolution output doesn't follow GEP schema |
| `log_error` | Error pattern in runtime logs |
| `perf_bottleneck` | Performance degradation detected |

## Running the Flow

```bash
# Simple scan + GEP output
evolver

# Human review before solidifying  
evolver --review

# Continuous evolution loop
evolver --loop

# With custom strategy
EVOLVE_STRATEGY=harden evolver --loop
```

## Practical Example

From our workspace run:

```
Signals detected:  user_feature_request, tool_bypass
Gene selected:     gene_gep_optimize_prompt_and_assets
Strategy:          balanced
Outcome:           GEP prompt generated + recorded to events.jsonl
```

The GEP prompt was then used to create a `tool-integration-pipeline` skill via `save_self_evolution_skill`, completing the full loop: **scan → gene → prompt → solidify → skill**.

## Limitations

- `--approve` solidify only works inside the EvoMap repo (needs its validation scripts)
- Hub features (skill store, task distribution) require [evomap.ai](https://evomap.ai) registration
- The tool is a **prompt generator**, not an auto-patcher
