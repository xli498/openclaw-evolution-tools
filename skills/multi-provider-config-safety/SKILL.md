---
name: "multi-provider-config-safety"
description: "Safely audit, add, or change multi-provider AI model configuration. Verifies provider isolation, agent-level model registration, real inference access, fallback behavior, and rollback evidence without exposing credentials."
triggers: ["新增或修改 AI provider", "切换默认模型或 fallback", "模型能列出但推理失败", "排查 provider 配置覆盖或路由异常"]
dependencies: []
version: "1.0.0"
author: "xli498"
created: "2026-07-23"
tags: ["openclaw", "provider", "model-routing", "configuration", "safety"]
---

# Multi-Provider Configuration Safety

## Purpose

Use this workflow when adding, changing, or diagnosing an AI model provider in a system that has multiple providers, model routes, or agent-level overrides. Its goal is to prevent silent key replacement, provider collisions, false health checks, and fallback surprises.

## Safety boundary

- Never print, commit, screenshot, or copy API keys, bearer tokens, cookies, or complete provider configuration files.
- Treat a provider as **unverified** until a minimal real inference request succeeds. A successful model-list endpoint is only discovery evidence.
- Do not overwrite a provider entry to add another provider. Add a distinct provider identifier.
- For configuration writes, identify impact and rollback before applying the smallest patch. Use the runtime's supported configuration API when available.

## Workflow

### 1. Build a redacted inventory

Before changing anything, record only:

| Check | Required evidence |
|---|---|
| Global model routing | primary model, fallback order, channel-specific overrides |
| Agent-level overrides | provider/model registry that can shadow global routing |
| Provider identity | provider ID, base URL host, registered model IDs, auth method type |
| Existing behavior | active session model and recent fallback/error summary |

Redact credentials as a short fingerprint or fixed mask. Do not store raw values in issues, commits, logs, or skills.

### 2. Detect configuration shadowing

Many runtimes have more than one source of truth. Verify whether agent-local model registries, session overrides, or channel routing rules shadow global defaults.

Checklist:

- Global default primary and fallback sequence match the intended route.
- The target provider and model exist in every registry consulted by the runtime.
- A channel-specific route does not pin another provider unexpectedly.
- A persisted session override is either intentional or cleared before judging global routing.

### 3. Verify two independent health levels

| Level | Minimal test | What it proves |
|---|---|---|
| Discovery | authenticated model listing | the credential can reach provider discovery |
| Inference | minimal chat/completion request with a small token cap | the credential is authorized for actual generation |

**Do not infer inference access from discovery access.** A provider can return model metadata while rejecting generation upstream.

Record only status class, provider/model ID, timestamp, and a redacted request identifier if one exists:

```text
provider/model | discovery=200 | inference=502 upstream_access_forbidden
```

### 4. Change one route at a time

1. Add or update the provider as an independent entry.
2. Register the model in the agent-level registry if the runtime uses one.
3. Change only the intended primary model or only the intended job override; preserve payloads, prompts, timeouts, and fallback order.
4. Keep the prior working route as the first rollback target until inference is verified.
5. Avoid changing provider URL, keys, model routing, and channel overrides in one write.

### 5. Verify actual runtime behavior

After a configuration change:

- check the active session model;
- run a small real request through the runtime, not only direct HTTP;
- confirm fallback only occurs when the primary actually fails;
- verify scheduled jobs with explicit model overrides separately;
- check that unrelated providers still remain registered and usable.

### 6. Roll back safely

Roll back if inference fails, a provider disappears, or routing changes unexpectedly:

1. restore the prior known-working model route;
2. leave unrelated providers untouched;
3. verify a minimal inference request and the active session route;
4. document the failure with redacted evidence and do not repeatedly retry the same failing path.

## Common failure patterns

| Symptom | Likely cause | Safe response |
|---|---|---|
| `/models` succeeds, generation fails | discovery permission differs from inference authorization | keep fallback active; contact provider administrator with redacted request ID |
| Global primary is correct but session uses another model | persisted session or channel override | inspect and intentionally clear/reset only that override |
| New provider disappears after restart | agent-local registry shadows global configuration | register it in the effective agent registry, then verify again |
| Adding provider breaks an existing one | provider object/key was overwritten | restore prior entry from redacted inventory; use distinct IDs going forward |
| Scheduled job still fails after default switch | job has an explicit model override | patch only the job model field; do not replace its whole payload |

## Verification checklist

- [ ] No secrets in the change, commit, issue, or diagnostic output
- [ ] Existing provider entries still exist after the change
- [ ] Target model exists in effective runtime registry
- [ ] Discovery and inference were tested separately
- [ ] Active session route matches the intended route
- [ ] Explicit scheduled-job routes were inspected separately
- [ ] Rollback model and verification evidence are recorded
