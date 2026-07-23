---
name: selflearn-flow
description: 经验闭环（SelfLearn）全流程skill——从犯错触发到经验沉淀为永久规则。涵盖事件写入、resolved标记、evolution draft生成、GEP审查、promotion落地的完整链路。
triggers:
  - 用户要求"跑一遍进化流程"/"走一遍SelfLearn"/"经验闭环"
  - 用户纠正、出错修复、同类错误3+次后建议执行
  - 用户主动要求沉淀某次经验为永久规则
dependencies: []
version: 1.0.0
author: self-evolution
created: 2026-07-23
---

# SelfLearn 经验闭环流程

## 触发条件
满足任一即触发 SelfLearn：
- 工具调用 > 5 次
- 出错修复成功
- 用户纠正行为/偏好
- 探索新路径/流程
- 同类错误出现 3+ 次
- 用户明确要求"沉淀经验"/"走流程"

## 工作目录
所有 SelfLearn 文件存储在 `~/.openclaw/workspace/memory/.selflearn/`

## 流程步骤

### 1. 写入事件（open）

```bash
# 追加到 events.jsonl，格式：
{"id":"SL-YYYYMMDD-<slug>","type":"<type>","status":"open","priority":"<high|medium|low>","area":"<area>","summary":"<中文摘要>","evidence":["证据1","证据2"],"resolution":null,"verification":null,"promotion_target":"none","promotion_ref":null,"created_at":"YYYY-MM-DDTHH:MM:SS+08:00","updated_at":"YYYY-MM-DDTHH:MM:SS+08:00"}
```

事件类型：
- `error` — 错误/故障
- `correction` — 用户纠正
- `best_practice` — 最佳实践/新发现
- `knowledge_gap` — 知识缺口
- `feature_request` — 功能需求

### 2. 标记 resolved

当修复完成且有**最小验证证据**后，更新事件状态：

```python
ev.update({"status":"resolved","resolution":"<修复方案>","verification":"<验证证据>"})
```

验证证据**不能为空**，必须可复现或可证明修复有效。

### 3. 生成 evolution draft

从 resolved 事件生成可复用候选：

```bash
mkdir -p ~/.openclaw/workspace/memory/evolution-drafts/pending
```

draft 文件使用 YAML frontmatter：
```yaml
---
id: ED-YYYYMMDD-<slug>
status: pending
type: best_practice
source_events: [SL-XXXX, SL-XXXX]
promotion_target: TOOLS.md  # 建议目标文件
created_at: YYYY-MM-DDTHH:MM:SS+08:00
---
```

内容要求：具体、可复用、包含排查步骤+验证方法。

### 4. GEP 审查

审查维度（每项 PASS/FAIL 打分）：
1. **安全性** — 无密钥/凭据/内部路径泄露
2. **准确性** — 内容与实际情况一致
3. **可复用性** — 下次遇到同类问题能直接照着走
4. **格式合规** — YAML frontmatter + 正确 markdown
5. **自动写入禁令** — 是否试图自动写入 AGENTS/TOOLS/USER

分级：P0（阻塞）→ P1（严重）→ P2（建议）→ 观察项

未修复 P0/P1 前不得 promotion。

### 5. Promotion（人工批准后）

```bash
# 移入 promoted 目录
mv pending/<draft> promoted/<draft>

# 更新 frontmatter
status: pending → status: promoted
promotion_ref: <目标文件>§<章节>

# 写入目标文件（TOOLS.md / AGENTS.md）
# 更新源事件的 promotion_target 和 promotion_ref
```

### 6. 禁令（禁止）
- **禁止** AutoMemory 接收原始错误噪声、密钥或完整敏感命令
- **禁止** 自动写入 AGENTS.md / TOOLS.md / USER.md
- **禁止** 自动批准或自动删除
- **禁止** SelfLearn 自行 promotion，必须经人工批准

## 输出审计

每次闭环完成后检查：
- events.jsonl：事件数、open/resolved 比例
- summary.json：汇总是否更新
- draft 状态：pending → promoted
- 目标文件：内容正确写入
- 无越界行为：未自动写入 AGENTS/TOOLS/USER

## 快速参考（一行命令检查状态）

```bash
# 查看所有事件统计
python3 -c "import json; e=[json.loads(l) for l in open('/home/sandbox/.openclaw/workspace/memory/.selflearn/events.jsonl') if l.strip()]; print(f'总计 {len(e)} 个，resolved {sum(1 for x in e if x[\"status\"]==\"resolved\")}，open {sum(1 for x in e if x[\"status\"]==\"open\")}')"

# 列出所有 pending draft
ls ~/.openclaw/workspace/memory/evolution-drafts/pending/

# 查看 summary
cat ~/.openclaw/workspace/memory/.selflearn/summary.json
```
