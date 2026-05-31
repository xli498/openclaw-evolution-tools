# Installation Guide

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

## Step 4: Gateway Restart

MemOS tools only become available after gateway restart:

```bash
openclaw gateway restart
```

After restart:
- MemOS tools: `memos_search`, `memos_get`, `memos_timeline`, etc.
- Viewer: `http://localhost:18799`
- EvoMap: CLI ready, just `evolver` in workspace
- Self-Improving Agent: auto-loaded

## Verification

```bash
# Check plugin status
openclaw plugins list | grep -E "memos|evolver"

# Test evolver
cd ~/.openclaw/workspace && evolver

# Check self-improving agent
ls ~/.openclaw/workspace/skills/proactive-agent/
```
