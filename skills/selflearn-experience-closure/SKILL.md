---
name: "selflearn-experience-closure"
description: "SelfLearn 经验闭环全流程：从犯错触发到人工批准 promotion，并将已验证经验写入永久规则。当出错修复后需要经验沉淀、用户纠正后需要更新可复用规则、同类错误多次出现需要走 GEP 闭环、或用户要求执行经验闭环时使用。"
version: 1.0.0
---

# selflearn-experience-closure

## Rules
- 触发条件：同一任务中同类工具调用失败或重试超过 5 次、出错修复后、用户纠正后、探索出新路径后、同类错误出现 3 次以上
- 事件先写入 memory/.selflearn/events.jsonl，默认 open 状态
- 只有写明修复方案+最小验证证据后才能转 resolved
- 只有人工批准+目标文件引用后才能转 promoted
- AutoMemory（若部署）只汇总 resolved/promoted 的脱敏摘要
- SelfLearn 只生成 evolution-drafts/pending 候选
- GEP 审查（见 [gep-evolution-flow](../gep-evolution-flow/SKILL.md)）只做人工审查，禁止自动写入 AGENTS/TOOLS/USER
- 禁止自动批准或自动删除

## Examples
- 陷阱：修完错误直接写 TOOLS.md 不经过 GEP → 正确：走完 open→resolved→draft→GEP→promotion 全流程
- 陷阱：events.jsonl 写 resolved 没有 verification 证据 → 正确：必须附上可验证的最小证据
- 陷阱：evolution draft 没有 YAML frontmatter → 正确：必须包含 id/status/type/source_events（数据契约以 guide.md 第 3 节为准；promotion_target 在批准后回写，不在创建时填写）

## Supplement
完整操作手册见同目录 [guide.md](./guide.md)：含 6 步流程、事件与草稿数据契约（YAML frontmatter）、GEP 审查标准、promotion 边界、审计清单与状态检查命令。适用场景：用户说"跑一遍进化流程"时优先读取此 skill 执行。
