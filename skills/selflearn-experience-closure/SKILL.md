---
name: "selflearn-experience-closure"
description: "SelfLearn 经验闭环全流程：从犯错触发 → 事件写入 → resolved 标记 → evolution draft 生成 → GEP 审查 → 人工批准 promotion → 写入永久规则。涵盖 AGENTS.md 中进化协议的全部约束和禁令。\n\nWhen to use: 当用户要求跑一遍进化流程/经验闭环时；当出错修复/用户纠正/同类错误3+次后需要沉淀经验时；当用户要求将某次经验保存为永久规则时。"
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
SKILL.md 位于 ~/.openclaw/workspace/skills/selflearn-flow/SKILL.md，含完整步骤、命令和审计清单。适用场景：用户说\"跑一遍进化流程\"时优先读取此 skill 执行。

## Tags
- selflearn
- evolution
- experience-closure
- GEP
- promotion
