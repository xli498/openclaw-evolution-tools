---
name: "selflearn-experience-closure"
description: "SelfLearn 经验闭环全流程：从犯错触发到人工批准 promotion，并将已验证经验写入永久规则。"
triggers: ["出错修复后需要经验沉淀", "用户纠正后需要更新可复用规则", "同类错误三次以上需要走 GEP 闭环", "用户要求执行经验闭环"]
dependencies: []
version: 1.0.0
author: xli498
created: 2026-07-23
tags: [evolution, selflearn, skill]
fingerprint: "ded9b4f87e854b0d3e663f6e60b7b3f864d5333fd14e5551fe12791fff2e8a36"
created_at: "2026-07-23T06:08:52.718Z"
---

# selflearn-experience-closure

## Metadata
- Created At: 2026-07-23T06:08:52.718Z

## Rules
- 触发条件：工具>5次/出错修复/用户纠正/新路径/同类3+次
- 事件先写入 memory/.selflearn/events.jsonl，默认 open 状态
- 只有写明修复方案+最小验证证据后才能转 resolved
- 只有人工批准+目标文件引用后才能转 promoted
- AutoMemory 只汇总 resolved/promoted 的脱敏摘要
- SelfLearn 只生成 evolution-drafts/pending 候选
- GEP 只审查，禁止自动写入 AGENTS/TOOLS/USER
- 禁止自动批准或自动删除

## Examples
- 陷阱：修完错误直接写 TOOLS.md 不经过 GEP → 正确：走完 open→resolved→draft→GEP→promotion 全流程
- 陷阱：events.jsonl 写 resolved 没有 verification 证据 → 正确：必须附上可验证的最小证据
- 陷阱：evolution draft 没有 YAML frontmatter → 正确：必须包含 id/status/type/source_events/promotion_target

## Supplement
完整操作手册见同目录 [guide.md](./guide.md)（含6步流程、命令示例、JSON格式、GEP审查标准、审计清单）。适用场景：用户说"跑一遍进化流程"时优先读取此 skill 执行。

## Tags
- selflearn
- evolution
- experience-closure
- GEP
- promotion
