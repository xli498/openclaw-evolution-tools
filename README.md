# 🧬 OpenClaw Evolution Tools

> *"Memory is not a file. Evolution is not a prompt. Growth is not a patch."*
> — **Elon Musk** (probably, if he built AI agents)

---

## The Trinity

Three tools. One mission: **make your OpenClaw agent stop being an amnesiac goldfish and start being a self-evolving intelligence.**

| Tool | What It Is | Powered By |
|:-----|:-----------|:-----------|
| 🧠 **MemOS Local** | A memory operating system. L1 traces, L2 policies, L3 world models. SQLite-backed, zero cloud. | `@memtensor/memos-local-plugin` |
| 🌐 **EvoMap Evolver** | GEP-powered self-evolution engine. Genes, Capsules, Events. Auditable evolution from day one. | `@evomap/evolver` |
| 📖 **Self-Improving Agent** | Structured learning. 7 triggers, 3-file knowledge system, automatic skill extraction. | `proactive-self-improving-agent` |

---

## Why This Matters

Most AI agents suffer from a fatal design flaw: **they start each conversation as a blank slate.**

Three conversations in, they're still asking your name. Ten conversations in, they've forgotten the lesson they learned in conversation #3. One hundred conversations in, they've learned exactly nothing.

This is stupid. We fixed it.

### The Stack

```
┌─────────────────────────────────────────────────┐
│            Self-Improving Agent                 │
│  (Structured Learning / Skill Crystallization)  │
├─────────────────────────────────────────────────┤
│              EvoMap Evolver                     │
│     (GEP Genes / Capsules / Evolution Audit)    │
├─────────────────────────────────────────────────┤
│              MemOS Local Plugin                 │
│  (L1 Traces → L2 Policies → L3 World Models)   │
├─────────────────────────────────────────────────┤
│              OpenClaw Runtime                   │
│      (Lossless-claw / Memory Core / Agent)      │
└─────────────────────────────────────────────────┘
```

---

## What Each Tool Does (In One Sentence)

**MemOS**: Automatically remembers every interaction, organizes them into hierarchical memory layers, and retrieves the right context at the right time — no prompt engineering required.

**EvoMap**: Scans your agent's runtime history, detects failure patterns and optimization opportunities, and generates auditable evolution instructions in the Genome Evolution Protocol (GEP) format.

**Self-Improving Agent**: Captures lessons from corrections, errors, and feature requests; crystallizes them into reusable skills; and prevents your agent from making the same mistake twice.

---

## Quick Start

```bash
# 1. MemOS Local Plugin
openclaw plugins install @memtensor/memos-local-plugin

# 2. EvoMap Evolver CLI
npm install -g @evomap/evolver

# 3. Self-Improving Agent (if not already installed)
git clone https://github.com/claw-opus/proactive-self-improving-agent.git
```

See the [`skills/`](./skills/) directory for detailed setup guides for each tool.

---

## The Evolution Loop (GEP Flow)

```
Scan ──▶ Signal Detection ──▶ Gene Selection ──▶ GEP Prompt ──▶ Solidify
  │                               │                    │              │
  │   user_feature_request        │                    │              │
  │   tool_bypass                Genes                 │          git commit +
  │   protocol_drift         (reusable patterns)       │       EvolutionEvent
  │                                                    │
  └────────────────────────────────────────────────────┘
                    (feedback loop)
```

Run it: `cd your-workspace && evolver`

---

## Philosophy

**Three hard problems in AI agent engineering:**
1. **Memory** — How does an agent remember what it learned?
2. **Evolution** — How does an agent improve without human rewrites?
3. **Learning** — How does an agent turn experience into skill?

Each tool solves exactly one of these. Together, they form a complete stack.

*"The best way to predict the future is to build it. And then let it build itself."*
— Also probably Elon

---

## Credits

- Video tutorial: **@功夫龙虾** on Douyin
- MemOS: [MemTensor/MemOS](https://github.com/MemTensor/MemOS) (⭐9.4k)
- EvoMap: [EvoMap/evolver](https://github.com/EvoMap/evolver) (⭐7.6k)
- Self-Improving Agent: [claw-opus/proactive-self-improving-agent](https://github.com/claw-opus/proactive-self-improving-agent)

---

## License

MIT — Build stuff. Don't be evil. Evolve or die.
