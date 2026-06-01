# OpenClaw Evolution Tools

三个工具，解决 AI Agent 的三个核心问题：记忆、进化、学习。

## 工具清单

| 工具 | 功能 | 上游 |
|:-----|:-----|:-----|
| 🧠 **MemOS Local** | 分层记忆系统（L1 痕迹 → L2 策略 → L3 世界观），SQLite 存储，零云端依赖 | `@memtensor/memos-local-plugin` |
| 🌐 **EvoMap Evolver** | GEP 驱动的自进化引擎，扫描运行历史，检测失败模式，生成可审计的进化指令 | `@evomap/evolver` |
| 📖 **Self-Improving Agent** | 结构化学习，7 种触发条件，3 文件知识系统，自动技能提取 | `proactive-self-improving-agent` |

## 解决什么问题

大多数 AI Agent 每次对话都从零开始。第三次对话还在问你叫什么名字，第十次对话忘了第三次学到的教训，第一百次对话什么都没学到。

这三个工具分别解决：

- **记忆** — Agent 怎么记住学到的东西？→ MemOS
- **进化** — Agent 怎么在没有人类重写的情况下自我改进？→ EvoMap
- **学习** — Agent 怎么把经验转化为技能？→ Self-Improving Agent

## 架构

```
┌─────────────────────────────────────────────────┐
│            Self-Improving Agent                 │
│  (结构化学习 / 技能结晶)                         │
├─────────────────────────────────────────────────┤
│              EvoMap Evolver                     │
│     (GEP 基因 / 胶囊 / 进化审计)                 │
├─────────────────────────────────────────────────┤
│              MemOS Local Plugin                 │
│  (L1 痕迹 → L2 策略 → L3 世界观)                │
├─────────────────────────────────────────────────┤
│              OpenClaw Runtime                   │
│      (Lossless-claw / Memory Core / Agent)      │
└─────────────────────────────────────────────────┘
```

## 快速开始

```bash
# 1. MemOS Local Plugin
openclaw plugins install @memtensor/memos-local-plugin

# 2. EvoMap Evolver CLI
npm install -g @evomap/evolver

# 3. Self-Improving Agent
git clone https://github.com/claw-opus/proactive-self-improving-agent.git
```

详见 [`skills/`](./skills/) 目录下各工具的安装指南。

## 实际使用示例

### EvoMap Evolver 输出

```bash
$ cd ~/.openclaw/workspace && evolver

[EvoMap Evolver v1.2.3]
Scanning workspace...
Found 3 signal patterns:

  1. tool_bypass (confidence: 0.85)
     Pattern: Agent skipped available skills, hand-crafted solution
     Gene: SKILL_SCAN_FIRST
     Action: Add mandatory skill scan to AGENTS.md

  2. protocol_drift (confidence: 0.72)
     Pattern: Agent used web_fetch instead of browser for interactive sites
     Gene: TOOL_FALLBACK_CHAIN
     Action: Define tool fallback priority in TOOLS.md

  3. user_feature_request (confidence: 0.91)
     Pattern: User requested "remember this" 5 times without persistence
     Gene: AUTO_MEMORY_TRIGGER
     Action: Enable auto-memory on keyword detection

Evolution instructions written to .evolution/pending/
```

### MemOS 工具调用

```
memos_search(query="代理配置") → 返回相关记忆片段
memos_get(id="mem_abc123") → 获取完整记忆条目
memos_timeline(days=7) → 最近 7 天的记忆时间线
memos_environment() → 当前环境上下文
memos_skill_list() → 已安装技能列表
```

### Self-Improving Agent 触发条件

| 触发 | 场景 | 动作 |
|------|------|------|
| `correction` | 用户纠正了 Agent 的回答 | 记录正确答案 |
| `error` | 工具调用失败 | 记录失败原因和修复方法 |
| `feature_request` | 用户要求新功能 | 记录需求和实现方案 |
| `preference` | 用户表达偏好 | 写入 USER.md |
| `lesson` | 学到新教训 | 写入 lessons.md |
| `pattern` | 发现重复模式 | 提取为技能 |
| `decision` | 做出重要决策 | 记录决策和上下文 |

## 进化流程（GEP）

```
扫描 ──▶ 信号检测 ──▶ 基因选择 ──▶ GEP Prompt ──▶ 固化
  │                           │                    │         │
  │   user_feature_request    │                    │         │
  │   tool_bypass            基因               git commit +
  │   protocol_drift        (可复用模式)      EvolutionEvent
  │
  └──────────────────────────────────────────────────┘
                    (反馈循环)
```

运行: `cd your-workspace && evolver`

## 依赖关系

三个工具可以独立使用，但组合效果最佳：

- **只装 MemOS** → 有记忆，但不会自动进化
- **只装 EvoMap** → 能检测模式，但没有结构化记忆
- **三个都装** → 记忆 → 检测 → 进化 → 学习，完整循环

## 子技能

详见 [`skills/`](./skills/) 目录：

- [`evomap-evolver/`](./skills/evomap-evolver/) — EvoMap 安装与 OpenClaw 集成
- [`gep-evolution-flow/`](./skills/gep-evolution-flow/) — GEP 进化流程配置
- [`memos-local/`](./skills/memos-local/) — MemOS Local Plugin 配置
- [`self-improving-agent/`](./skills/self-improving-agent/) — Self-Improving Agent 集成

## 参考

- 视频教程: **@功夫龙虾** (抖音)
- MemOS: [MemTensor/MemOS](https://github.com/MemTensor/MemOS) (⭐9.4k)
- EvoMap: [EvoMap/evolver](https://github.com/EvoMap/evolver) (⭐7.6k)
- Self-Improving Agent: [claw-opus/proactive-self-improving-agent](https://github.com/claw-opus/proactive-self-improving-agent)

## License

MIT
