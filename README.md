# OpenClaw Evolution Tools

OpenClaw 的记忆、演化与学习工具选型/集成参考。它不自动安装组件、不修改配置，也不提供 KAIROS、AutoDream、AutoMemory 的运行时实现。先阅读[范围与安全边界](./docs/00-范围与安全边界.md)。

## 四个工具

| 工具 | 功能 | 基于 |
|:-----|:-----|:-----|
| 🧠 **MemOS Local** | 分层记忆操作系统。L1 痕迹 → L2 策略 → L3 世界模型。SQLite 存储，零云端依赖。 | `@memtensor/memos-local-plugin` |
| 🌐 **EvoMap Evolver** | GEP 驱动的自我演化引擎。基因、胶囊、事件。可审计的演化路径。 | `@evomap/evolver` |
| 📖 **Self-Improving Agent** | 结构化学习。7 个触发条件，3 文件知识体系，自动技能提取。 | `proactive-self-improving-agent` |
| 🔁 **SelfLearn 经验闭环** | 犯错→事件→draft→GEP→promotion 全流程。出错修复/用户纠正后自动沉淀经验为永久规则。 | `selflearn-experience-closure` |

## 使用前先看

- [范围与安全边界](./docs/00-范围与安全边界.md)：安装、联网、重启与持续循环的边界。
- [工具选型与冲突矩阵](./docs/01-工具选型与冲突矩阵.md)：避免多个记忆/自进化组件重复写入或重复调度。

## 为什么需要这些工具

AI Agent 通常在每次对话中从零开始。没有记忆、没有学习、没有演化。

四个工具分别解决四个核心问题：
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

# 4. SelfLearn 经验闭环
已内置于 OpenClaw 的 SelfLearn 系统和 AGENTS.md 经验闭环规则中；完整 SKILL.md 见 [`skills/selflearn-experience-closure/`](./skills/selflearn-experience-closure/)
```

详见 [`skills/`](./skills/) 目录中每个工具的配置指南。

## 运行时能力的边界

本仓库**不包含** `scripts/kairos_heartbeat.py`、`scripts/autodream.py` 或 `scripts/auto_memory.py`，因此不能把它当作这些命令的安装包或运行说明。

KAIROS、AutoDream、AutoMemory 仅用于说明一种设计模式：把状态巡检、记忆整理和经验提取分成可审计的独立阶段。实际实现应由当前运行时已安装的组件提供，并且必须确认：

- 谁是唯一的记忆写入源；
- 谁负责周期调度；
- 是否会联网、外发或消耗额度；
- 如何验证、停止和回滚。

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
