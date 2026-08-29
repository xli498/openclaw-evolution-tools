## SelfLearn Experience Closure Guide

### Scope

Use this guide to move a verified lesson from a resolved SelfLearn event into a reviewable evolution draft. It does not authorize automatic promotion, automatic writes to user profile files, or deletion of records.

### 1. Record the event

Create one event record in `memory/.selflearn/events.jsonl` with:

- a stable event ID;
- category (`error`, `correction`, `best_practice`, `knowledge_gap`, or `feature_request`);
- sanitized evidence;
- current status (`open`, `resolved`, or `promoted`);
- timestamps and links to the relevant validation evidence.

Never store complete credentials, private prompts, personal data, or raw sensitive commands in the event payload.

### 2. Resolve before promotion

An event may move from `open` to `resolved` only after all of the following exist:

1. a concrete remediation or reusable procedure;
2. minimal validation evidence showing the remediation works;
3. a clear scope and non-goal statement;
4. no unresolved safety, privacy, or ownership issue.

A single occurrence is normally recorded and tracked. Promote a recurring pattern only when evidence shows it is reusable rather than incidental.

### 3. Create a reviewable draft

Write candidates to `memory/evolution-drafts/pending/`. Each draft is a Markdown file with a YAML frontmatter header followed by a structured body — this is the single authoritative draft contract:

```yaml
# frontmatter（创建时必填）
---
id: draft_<timestamp>          # 稳定唯一 ID
status: pending                # pending → promoted（仅经人工批准）
type: error | correction | best_practice | knowledge_gap | feature_request
source_events: [ "<event-id>", ... ]  # 指向 events.jsonl 中的来源事件
---
```

Body 必须写清：

- the trigger and intended use;
- exact guardrails and non-goals;
- supporting evidence and validation command or fixture;
- affected files or Skills;
- rollback or rejection path.

`promotion_target` 与 `promotion_ref` 不在创建时填写：它们在人工批准后按第 5 步回写到来源事件，避免草案预设晋升去向。

The draft is pending until an authorized human review approves it. A pending file is not an installed Skill and is not proof of behavioral adoption.

### 4. Promotion boundary and GEP review criteria

Promotion requires explicit human approval and a traceable target. GEP 审查（见 [gep-evolution-flow](../gep-evolution-flow/SKILL.md)）在批准前逐项核对：

1. 证据可追溯：draft 的每项主张都能回链到 source_events 中的脱敏证据；
2. 范围明确：写清影响文件/Skill、非目标（non-goals）与爆炸半径；
3. 无敏感内容：不含凭据、私有 Prompt、个人数据或未脱敏命令；
4. 可回滚：给出拒绝/回滚路径与验证命令；
5. 权限最小：不要求超出目标文件范围的写入或执行权限。

Approved changes must be made through the formal Skill/workflow process, then verified through:

1. the formal scan path;
2. a clean-session recall or invocation check;
3. a task-level regression that shows the new behavior is actually followed.

### 5. Update source events

After an approved promotion, update the source event with `promotion_target` and `promotion_ref`. Do not silently overwrite the original evidence.

### 6. Prohibitions

- Do not send raw error noise, keys, or full sensitive commands to AutoMemory (if deployed).
- Do not automatically write `AGENTS.md`, `TOOLS.md`, or `USER.md`.
- Do not automatically approve or delete drafts.
- Do not let SelfLearn promote its own output without human approval.

## Output audit

After each closure, check:

- `events.jsonl`: event count and open/resolved ratio;
- `summary.json`: summary refresh state;
- draft status: `pending` → `promoted` only with approval;
- target files: correct content is present;
- boundary compliance: no automatic writes to profile or policy files.

## Quick status check

```bash
# Override the default workspace when needed.
WORKSPACE="${OPENCLAW_WORKSPACE:-$HOME/.openclaw/workspace}"

# Summarize event states.
python3 - "$WORKSPACE/memory/.selflearn/events.jsonl" <<'PY'
import json
import sys

with open(sys.argv[1], encoding="utf-8") as fh:
    events = [json.loads(line) for line in fh if line.strip()]
print(
    f"total {len(events)}, "
    f"resolved {sum(x['status'] == 'resolved' for x in events)}, "
    f"open {sum(x['status'] == 'open' for x in events)}"
)
PY

# List pending drafts and inspect the aggregate summary.
ls "$WORKSPACE/memory/evolution-drafts/pending/"
cat "$WORKSPACE/memory/.selflearn/summary.json"
```
