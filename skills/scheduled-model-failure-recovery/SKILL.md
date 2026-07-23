---
name: "scheduled-model-failure-recovery"
description: "Diagnose and safely recover scheduled AI jobs when model routes fail. Separates transient upstream errors, credential failures, discovery-only access, runtime overrides, and job-specific model pins; preserves job payloads and verifies real generation before declaring recovery."
triggers: ["定时任务模型调用失败", "cron 出现 5xx 或 timeout", "模型列表可见但实际推理失败", "切换默认模型后任务仍失败", "排查 session、agent 或 job 的模型路由差异"]
dependencies: []
version: "1.0.0"
author: "xli498"
created: "2026-07-23"
tags: ["scheduling", "model-routing", "cron", "recovery", "reliability"]
---

# Scheduled Model Failure Recovery

## Purpose

Use this workflow when scheduled AI jobs fail because of model/provider routing. It distinguishes temporary upstream issues from permanent authorization or configuration faults, and prevents destructive “fixes” that replace job prompts, timeouts, or delivery rules while trying to change only a model.

## Safety boundary

- Never expose credentials, request bodies containing private content, recipient IDs, or raw provider diagnostics in public artifacts.
- Do not change provider URLs, credentials, default routing, scheduled payloads, and delivery targets in one recovery step.
- A successful model-list endpoint does not prove generation access. Test minimal real inference separately.
- Preserve the full scheduled job payload. Change only the intended model field unless the user explicitly requests broader edits.
- Do not create duplicate runs to “see if it recovers”; respect normal schedule, idempotency, and delivery controls.

## Evidence first

For each failed job, capture a redacted evidence record:

| Evidence | Why it matters |
|---|---|
| job ID/name and scheduled time | identifies the actual execution path |
| configured job model and timeout | explicit job pin may bypass global default |
| run status, duration, and provider error class | separates 401/403/5xx/timeout behavior |
| active session model | detects session-specific override, but is not proof for cron |
| global primary/fallback route | identifies intended default behavior |
| agent/channel model registry | identifies effective routing shadowing |

Prefer status codes and provider error categories over a generic local error label. Some schedulers collapse provider errors into `timeout` or another generic summary.

## Classification

| Signal | Likely class | Safe next action |
|---|---|---|
| 401 / invalid credential | authorization failure | stop retries; rotate or repair access through approved path |
| 403 / access forbidden | model entitlement failure | preserve fallback; contact provider administrator with redacted request ID |
| 5xx / service unavailable | transient upstream failure | verify provider health independently; allow next scheduled run or use one controlled recovery run |
| `/models` succeeds but generation fails | discovery-only access | mark provider unusable for inference; do not promote to primary |
| job succeeds manually but fails on schedule | job context, timeout, or explicit override | inspect job model/payload and isolated runtime constraints |
| default changed but job still uses old route | explicit job model pin | patch only job model field, then verify next run |

## Workflow

### 1. Confirm the failed execution path

1. Inspect the specific job and its latest runs.
2. Record model override, timeout, thinking mode, and delivery behavior.
3. Determine whether it runs in an isolated session, a persistent session, or the main session.
4. Check for an explicit job model before changing global defaults.

### 2. Verify provider health at two levels

| Test | Purpose |
|---|---|
| authenticated model discovery | confirms provider reachability and discovery authorization |
| minimal generation request | confirms actual inference authorization and upstream availability |

Use a harmless small prompt and strict output cap. Record only status/result class. Do not use a production task body as a health probe.

### 3. Inspect effective routing layers

Check separately:

- global primary and fallback order;
- agent-local provider/model registry;
- channel-specific routing;
- persisted session overrides;
- scheduled-job explicit model field.

A correct global default does not override an explicit scheduled-job pin. A working interactive session does not prove an isolated job can resolve the same provider.

### 4. Apply the smallest recovery

Choose one path based on evidence:

- **Transient 5xx:** keep route unchanged, wait for next run or perform one controlled run if delivery is time-sensitive.
- **Discovery-only / 403:** revert to a known inference-capable provider; do not leave the blocked provider as primary.
- **Explicit job pin:** patch only the job model field; retain its prompt, timeout, thinking, idempotency, and delivery configuration.
- **Registry shadowing:** register the intended provider/model in the effective registry, then test real inference.
- **Credential failure:** stop automated retries and use the approved credential-repair process.

### 5. Verify recovery end-to-end

Recovery is complete only when:

1. minimal generation succeeds through the chosen provider;
2. the effective job model resolves as intended;
3. one controlled execution or the next scheduled execution succeeds;
4. artifact generation and delivery state are checked separately;
5. unrelated providers and jobs remain intact.

## Controlled recovery run rules

A manual run is appropriate only when all are true:

- the job is read-only or idempotent;
- a duplicate output is prevented by its own delivery key/state;
- the failure class and target recovery route are known;
- one run will materially validate the fix.

Otherwise wait for the next scheduled interval and monitor the result.

## Failure patterns

| Failure | Bad response | Correct response |
|---|---|---|
| Job reports timeout with hidden 5xx diagnostics | tune timeout blindly | inspect provider status class first |
| New model appears in discovery response | make it primary | validate real inference first |
| Change job model through full payload replacement | lose prompt/timeout/delivery behavior | patch only the model field |
| Global default switched, job still fails | repeat global edits | inspect explicit job pin and isolated route |
| One success after provider outage | assume permanent fix | retain fallback and verify subsequent scheduled behavior |

## Completion gate

- [ ] Failed job and latest run evidence recorded in redacted form
- [ ] Discovery and real inference tested separately
- [ ] Effective routing layers inspected
- [ ] Only the necessary model/registry field changed
- [ ] Full job payload and delivery behavior preserved
- [ ] Controlled or scheduled run verifies recovery
- [ ] Artifact generation and recipient delivery are reported separately
