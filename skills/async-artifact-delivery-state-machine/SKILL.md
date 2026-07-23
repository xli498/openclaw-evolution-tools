---
name: "async-artifact-delivery-state-machine"
description: "Reliably deliver generated files or messages across asynchronous channels using idempotency keys, immutable artifacts, explicit delivery states, uncertainty handling, and user-level receipt confirmation."
triggers: ["生成了文件但需要可靠投递", "附件投递失败或会话失效", "需要避免重复发送", "用户反馈没有收到文件", "设计跨渠道异步交付流程"]
dependencies: []
version: "1.0.0"
author: "xli498"
created: "2026-07-23"
tags: ["delivery", "artifact", "idempotency", "reliability", "async"]
---

# Async Artifact Delivery State Machine

## Purpose

Use this pattern when an agent generates a report, file, image, or message that must be delivered through an asynchronous channel. Generation success is not delivery success. The state machine prevents duplicate sends, accidental regeneration, and unsafe retries when the provider result is uncertain.

## Safety boundary

- Never put credentials, recipient identifiers, private URLs, message bodies, or raw provider responses into public logs or repository fixtures.
- Do not report an artifact as delivered merely because it was generated or uploaded.
- Do not automatically resend when provider outcome is uncertain; duplicate delivery can be worse than delay.
- Treat explicit user feedback such as “not received” as stronger evidence than a provider acceptance response.

## State model

```text
artifact ready
  -> queued
  -> sending
  -> delivered         (provider returned a durable delivery/message identifier)
  -> pending           (known not sent; safe to retry later)
  -> uncertain         (provider outcome unknown; freeze automatic resend)
  -> failed_terminal   (known unrecoverable without changed input or permission)
```

Keep state transitions append-only or auditable. Store only a redacted destination label and an artifact fingerprint, never the sensitive destination itself.

## Workflow

### 1. Freeze the artifact before queueing

1. Generate the artifact.
2. Run content and format validation appropriate to the artifact type.
3. Copy it into immutable, content-addressed storage or record a checksum and byte size.
4. Queue the immutable copy, not a mutable working file.

This ensures a delayed retry sends the same reviewed artifact rather than a changed or partially regenerated replacement.

### 2. Use a deterministic idempotency key

Construct an idempotency key from a stable business identity, for example:

```text
<task-type>:<logical-date-or-source-id>:<recipient-scope>
```

Rules:

- Same logical delivery => same key.
- New revision => explicit revision component, not a silently changed file under the old key.
- Before sending, look up prior state for the key.
- `delivered`, `uncertain`, and terminal states block blind duplicate attempts.

### 3. Send through one owner

Only one sender/worker may claim a queued key at a time. The sender records:

- state before and after attempt;
- timestamp;
- redacted provider classification;
- durable delivery/message identifier if returned;
- immutable artifact fingerprint.

Do not mix direct sends, queue sends, and manual scripts for the same key unless they share the same state store.

### 4. Classify outcomes precisely

| Outcome | State | Automatic action |
|---|---|---|
| Provider confirms a durable message/delivery ID | `delivered` | block duplicates |
| Channel/session is known unavailable before send | `pending` | retain queue; retry only after recovery signal |
| Network/provider result is ambiguous after request | `uncertain` | freeze resend; require reconciliation or human review |
| Validation fails before queueing | not queued | fix artifact; do not send |
| Permanent permission/recipient error | `failed_terminal` | notify owner; require changed permission/input |

### 5. Recover from session or channel loss

When a channel requires an inbound session or ephemeral recipient handle:

1. keep the immutable queued artifact;
2. notify through an available fallback channel once, without exposing content;
3. wait for a verified recovery signal, such as a new inbound message or renewed authorization;
4. replay the original key only if it is still `pending`;
5. never regenerate just because delivery failed.

### 6. Reconcile user receipt

There are three distinct levels:

| Level | Meaning |
|---|---|
| Generated | file/content exists and validation passed |
| Provider accepted | sender received a provider success response or message ID |
| User confirmed | recipient confirms receipt and can access the artifact |

If a recipient says they did not receive it, mark delivery as unconfirmed even if the provider previously accepted it. Reconcile the original artifact/key before creating another one.

## Minimal audit record

```json
{
  "idempotency_key": "report:2026-07-23:recipient-scope",
  "artifact_sha256": "<checksum>",
  "state": "pending",
  "attempt_count": 1,
  "provider_result": "session_unavailable",
  "delivery_id": null,
  "updated_at": "<ISO-8601 timestamp>"
}
```

Keep the real recipient and raw provider payload out of public records.

## Failure patterns

| Failure | Bad response | Correct response |
|---|---|---|
| Artifact generated but send fails | claim success | report generated + pending delivery separately |
| Session unavailable | regenerate every run | keep original immutable artifact and wait for recovery |
| Timeout after request | resend immediately | mark uncertain and reconcile first |
| User says “not received” | trust provider response over user | treat as not confirmed; replay original artifact safely |
| Two send paths exist | send through both | route all attempts through one keyed state owner |

## Completion gate

- [ ] Artifact validation completed before queueing
- [ ] Immutable artifact fingerprint recorded
- [ ] Deterministic idempotency key used
- [ ] Exactly one delivery owner handled the key
- [ ] Provider result classified as delivered, pending, uncertain, or terminal
- [ ] User receipt is not overstated
- [ ] No credentials, recipient IDs, content, or raw provider payloads leaked
