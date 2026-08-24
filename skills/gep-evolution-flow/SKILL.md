---
name: "gep-evolution-flow"
description: "将经验信号整理为可审计的演进候选；仅生成草案，不自动安装、应用或启动后台循环。"
triggers: ["需要将经验信号转成 evolution draft", "执行 GEP 审查或 promotion 流程", "审计演化对象与证据链"]
dependencies: []
version: 1.0.0
author: xli498
created: 2026-07-23
tags: [evolution, selflearn, skill]
---

# GEP Evolution Flow — 从信号到候选

> 本文使用“Mutation / Gene / Capsule”等名称描述一个**本地候选数据模型**，不声称这是某个上游协议的当前版本或官方规范。

## 候选数据模型

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

## 受控流程

1. 仅用脱敏、有限的历史信号生成候选；
2. 标注证据、推断和未验证项；
3. 人工审查候选的权限、写入范围、依赖和回滚点；
4. 仅在得到明确批准后，通过宿主正式流程创建或应用目标 Skill；
5. 以新会话和真实任务回归验收。

不要启动持续循环，不要直接执行第三方安装命令，也不要把候选当作已固化经验。

## Practical Example

示例：

```
Signals detected:  user_feature_request, tool_bypass
Gene selected:     gene_gep_optimize_prompt_and_assets
Strategy:          balanced
Outcome:           GEP prompt generated + recorded to events.jsonl
```

候选可被提交到人工审批流程；只有批准、正式扫描和真实任务回归都完成后，才可称为已生效。

## Limitations

- 第三方工具的版本、许可证、联网行为和安装方法必须在使用前查阅其官方文档；
- 本 Skill 不提供第三方 CLI 的安装、注册或后台循环命令；
- 候选文本不是自动补丁，也不是生产变更授权。
