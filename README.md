# OpenClaw Evolution Tools

OpenClaw 的自主进化工具链——记忆、演化、学习。

## 三个工具

| 工具 | 功能 | 基于 |
|:-----|:-----|:-----|
| 🧠 **MemOS Local** | 分层记忆操作系统。L1 痕迹 → L2 策略 → L3 世界模型。SQLite 存储，零云端依赖。 | `@memtensor/memos-local-plugin` |
| 🌐 **EvoMap Evolver** | GEP 驱动的自我演化引擎。基因、胶囊、事件。可审计的演化路径。 | `@evomap/evolver` |
| 📖 **Self-Improving Agent** | 结构化学习。7 个触发条件，3 文件知识体系，自动技能提取。 | `proactive-self-improving-agent` |

## 为什么需要这些工具

AI Agent 通常在每次对话中从零开始。没有记忆、没有学习、没有演化。

三个工具分别解决三个核心问题：
1. **记忆**（MemOS）— Agent 如何记住学过的东西？
2. **演化**（EvoMap）— Agent 如何在没有人工干预的情况下改进？
3. **学习**（Self-Improving）— Agent 如何将经验转化为技能？

## 架构

```
┌─────────────────────────────────────────────────┐
│            Self-Improving Agent                 │
│  (结构化学习 / 技能结晶)                         │
├─────────────────────────────────────────────────┤
│              EvoMap Evolver                     │
│     (GEP 基因 / 胶囊 / 演化审计)                │
├─────────────────────────────────────────────────┤
│              MemOS Local Plugin                 │
│  (L1 痕迹 → L2 策略 → L3 世界模型)              │
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

详见 [`skills/`](./skills/) 目录中每个工具的配置指南。

## 实际使用：KAIROS 心跳

在 OpenClaw 中，演化工具每天通过 KAIROS 心跳自动运行：

```bash
# 会话启动时的 KAIROS 心跳
python3 scripts/kairos_heartbeat.py --quick
```

实际输出示例：

```
KAIROS Heartbeat v1.0
──────────────────────────────────────
Scanning environment...
  Crontabs: 4 active jobs
  Memory health: 23 entries, 3 outdated
  Skills patch check: 2 skills have updates available
  Error log: 7 entries (2 new since last check)
  Pending tasks: 1 (openclaw-config-guide docs)

Recommendation: Low confidence — no critical items
  - 2 skills have pending updates (low priority)
  - 1 pending task (openclaw-config-guide docs/05)
```

## 实际使用：AutoDream 记忆整理

```bash
# 检查是否需要记忆整理
python3 scripts/autodream.py --check
```

实际输出示例：

```
AutoDream Check
──────────────────────────────────────
Last dream: 2025-06-01 08:00 (13.2 hours ago)
Pending fragments: 8
Fragment quality score: 0.45

Gating checks:
  ✅ Time gate: 13.2h > 12h threshold
  ✅ Quantity gate: 8 > 5 threshold
  ✅ Quality gate: 0.45 > 0.3 threshold

All 3 gates passed — dream cycle recommended.
Run: python3 scripts/autodream.py --dream
```

## 实际使用：AutoMemory 自动记忆

```bash
# 对话结束后自动提取记忆
python3 scripts/auto_memory.py
```

实际输出示例：

```
AutoMemory Extraction
──────────────────────────────────────
Analyzing conversation...
  Topics detected: MiMo degenerate loop, proxy config, HTTP headers
  Classification:
    [project] MiMo Degenerate Loop: root cause is reasoning=True fixed point
    [reference] env-proxy vs explicit-proxy with undici incompatibility
    [feedback] HTTP Header 中文字符 → ByteString 错误

3 new entries ready for MEMORY.md
```

## 三重门控机制

AutoDream 的记忆整理采用三重门控，至少 2/3 通过才执行：

| 门控 | 条件 | 当前设置 |
|------|------|----------|
| 时间 | 距上次整理 | > 12 小时 |
| 量级 | 待整理碎片 | > 5 条 |
| 质量 | 碎片化程度 | > 0.3 |

这个设计确保记忆整理只在累积足够有意义的内容时才执行，避免频繁的低质量整理。

## GEP 演化流程

```
扫描 ──▶ 信号检测 ──▶ 基因选择 ──▶ GEP 提示 ──▶ 固化
  │           │              │              │            │
  │  feature  │              │              │            │
  │  _request │          Genes              │        git commit +
  │  bypass   │     (可复用模式)             │     EvolutionEvent
  │  drift    │                             │
  └──────────────────────────────────────────┘
                 (反馈循环)
```

使用：`cd your-workspace && evolver`

## 实际经验

以下是基于 OpenClaw 真实部署经验的演化协议（Evolution Protocol）核心模式：

1. **KAIROS 心跳** — 会话启动时扫描环境，检测值得主动处理的事项
2. **AutoDream 记忆整理** — 空闲时压缩巩固记忆（三重门控）
3. **AutoMemory 自动记忆** — 对话结束后自动提取值得保存的内容
4. **Context Engineering** — 动态组装上下文（L0-L3 分层加载）
5. **Self-Learn 自学习** — 任务完成后自动复盘，提取经验
6. **情绪感知** — 检测用户状态，自适应调整交互方式

## 参考

- 视频教程：**@功夫龙虾** 抖音
- MemOS：[MemTensor/MemOS](https://github.com/MemTensor/MemOS)
- EvoMap：[EvoMap/evolver](https://github.com/EvoMap/evolver)
- Self-Improving Agent：[claw-opus/proactive-self-improving-agent](https://github.com/claw-opus/proactive-self-improving-agent)

## License

MIT
