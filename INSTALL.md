# Installation Guide

> 本文只提供上游工具的集成检查清单，不是自动安装脚本。安装插件、Skill、全局 npm 包、修改配置或重启 Gateway 前，都应先阅读[范围与安全边界](./docs/00-范围与安全边界.md)，确认影响并保留回滚路径。

## Prerequisites

- OpenClaw (any version ≥ 2026.5)
- Node.js ≥ 18
- Git

## Step 1: MemOS Local Plugin

```bash
# Option A: Via OpenClaw CLI (recommended)
openclaw plugins install @memtensor/memos-local-plugin

# Option B: Manual install
cd ~/.openclaw/extensions
npm install @memtensor/memos-local-plugin

# Create runtime config
mkdir -p ~/.openclaw/memos-plugin
cp ~/.openclaw/extensions/node_modules/@memtensor/memos-local-plugin/templates/config.openclaw.yaml \
   ~/.openclaw/memos-plugin/config.yaml
chmod 600 ~/.openclaw/memos-plugin/config.yaml

# Register in openclaw.json:
# openclaw gateway call config.get
# Then patch to add: plugins.entries.memos-local-plugin = { enabled: true }
```

## Step 2: EvoMap Evolver

```bash
# Install globally
npm install -g @evomap/evolver

# If you get EACCES:
npm config set prefix ~/.npm-global
export PATH="$HOME/.npm-global/bin:$PATH"

# Verify
evolver --help

# Place the SKILL.md from skills/evomap-evolver/ into your OpenClaw skills/
```

## Step 3: Self-Improving Agent

```bash
# Via OpenClaw add
openclaw add https://github.com/yanhongxi-openclaw/proactive-self-improving-agent

# Or if you already have it
ls ~/.openclaw/workspace/skills/proactive-agent/
```

## Step 4: 验证与受控重载

不要把重启当成安装的默认下一步。先确认插件是否真的要求重启、当前 Gateway 是否在运行，以及配置是否已备份。

建议的验证顺序：

1. 检查插件/CLI 是否已安装；
2. 查阅该组件当前版本的官方加载说明；
3. 对只读功能做最小验证；
4. 只有明确要求且已确认影响时，才使用当前 OpenClaw 推荐的重载或重启方式；
5. 重启后重新检查会话模型、插件工具注册和日志。

`evolver --loop` 属于长期自动化，不应作为安装完成后的默认验证命令。优先使用单次或 review 模式。

## Verification

```bash
# Check plugin status
openclaw plugins list | grep -E "memos|evolver"

# Test evolver
cd ~/.openclaw/workspace && evolver

# Check self-improving agent
ls ~/.openclaw/workspace/skills/proactive-agent/
```
