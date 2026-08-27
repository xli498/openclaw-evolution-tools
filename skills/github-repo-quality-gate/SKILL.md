---
name: "github-repo-quality-gate"
description: "Safely improve and verify a public GitHub repository: inspect current state, make atomic changes, protect branches and history, validate content locally, and require GitHub Actions success on the exact final commit. Use when reviewing or improving a GitHub repo, adding LICENSE, migrating branches, standardizing Skills, adding quality-gate workflows, or confirming CI failures are fixed."
version: "1.0.0"
---

# GitHub Repository Quality Gate

## Purpose

Use this workflow to improve a public GitHub repository without losing history, creating misleading green checks, or claiming success before the final remote commit is verified.

## Safety boundary

- Inspect the current remote branch, files, and protection state before making changes.
- Use focused, atomic commits. Do not force-push a public branch unless an explicit recovery plan and user approval exist.
- Do not expose tokens, secrets, private paths, personal data, or raw logs in repository content.
- A workflow file being present is **not** proof of CI. Require a successful GitHub Actions run on the final commit SHA.
- Treat migration steps such as default-branch changes and remote branch deletion as ordered operations with a rollback point.

## Workflow

### 1. Baseline the remote repository

Record a concise baseline before writing:

| Area | Verify |
|---|---|
| Repository | visibility, archived state, default branch, license |
| History | current head SHA and recent commits |
| Files | existing README, docs, workflows, source, tests, templates |
| Automation | Actions enabled, workflow state, latest run status and SHA |
| Branches | default branch, stale branch references, protections if applicable |

Use remote API data as the source of truth. Local clones may have stale fetch rules or branches.

### 2. Define the smallest complete change set

Prioritize in this order:

1. security and legal basics: no secrets, correct license;
2. correctness: broken links, false claims, stale documentation contracts;
3. executable quality gates: deterministic tests, syntax checks, validators;
4. maintenance: contribution/security guidance and issue templates;
5. discoverability: topics, cross-links, presentation polish.

Do not add boilerplate that has no repository-specific value.

### 3. Standardize reusable Skills when present

For each `skills/<name>/SKILL.md`, validate a stable frontmatter contract based on the official OpenClaw / Agent Skills schema (`name`, `description`, `version`):

```yaml
---
name: "unique-kebab-case-skill-name"
description: "one-line purpose including when to use the skill"
version: "1.0.0"
---
```

Then validate:

- required fields (`name`, `description`) exist and have correct types;
- `version`, when present, is valid SemVer;
- skill names are unique, lowercase kebab-case, and match their directory name;
- non-standard legacy fields (e.g. `triggers`, `dependencies`, `author`, `created`, `tags`) are not reintroduced;
- relative Markdown links resolve;
- documentation pages are not silently used as a replacement for `SKILL.md`.

### 4. Build tests from real behavior, not README promises

Before adding CI assertions:

1. run the existing command or script against its committed fixtures;
2. inspect its actual exit code, output, and machine-readable contract;
3. create deterministic fixtures for loop/normal/error cases if historical logs are ambiguous;
4. document the distinction between observation artifacts and test fixtures;
5. assert the stable contract, not guessed wording.

Historical logs are evidence. Deterministic fixtures are tests. Do not force code to fit an inaccurate README claim.

### 5. Handle default-branch migration safely

For `master` to `main` migration:

1. create `main` at the current `master` head;
2. set `main` as default branch;
3. scan code, docs, workflows, and badges for `master` references;
4. delete remote `master` only after default branch changes successfully;
5. update local clone fetch refspecs, fetch `main`, fast-forward, set `origin/HEAD`, and delete local `master` only after confirming it has no unique commits.

### 6. Make one atomic remote change per repository

A commit may contain related code, tests, docs, and workflow updates for one capability. Keep unrelated repositories and unrelated concerns separate.

After writing through an API, re-fetch files and head SHA. Do not assume the local clone or an API response reflects later history changes.

### 7. Verify locally, then verify remotely

Local verification examples:

- Python: `python -m py_compile ...`
- Shell: `bash -n ...`
- behavior tests with committed fixtures;
- Markdown relative-link validation;
- Skill frontmatter and link validation;
- documentation evidence-contract validation.

Remote verification checklist:

- workflow is active and Actions are enabled;
- trigger a controlled run when necessary;
- latest run is `completed/success`;
- run `head_sha` equals the current default-branch head SHA;
- inspect failed logs before claiming completion.

### 8. Read CI notifications correctly

A failure email refers to the named historical run and commit. It remains in email after a later repair.

To determine current state, compare:

```text
current main SHA == latest successful workflow run head SHA
```

If they differ, the repository is not yet fully verified.

## Failure patterns

| Symptom | Cause | Correct response |
|---|---|---|
| Local push rejected after API write | remote moved independently | fetch/rebase carefully; avoid force-push unless explicitly approved |
| Force push removed an API-created commit | histories diverged | restore missing files through a new forward commit; re-verify remote tree |
| Workflow exists but no run appears | API-created commit may not emit a push event | add controlled `workflow_dispatch`, trigger once, then inspect resulting SHA |
| CI fails immediately after adding a validator | validator parses unrelated content or assumes undocumented behavior | inspect failed logs; narrow the parser or correct the contract; rerun CI |
| Historical log does not satisfy new test | evidence artifact differs from deterministic test fixture | preserve it as evidence; add a dedicated fixture and document threshold differences |
| Local clone remains on deleted branch | stale remote fetch refspec | fetch `main` explicitly, update refspec, set `origin/HEAD`, then switch safely |

## Completion gate

Do not report repository work as complete until:

- [ ] Final remote head SHA is known
- [ ] Local/remote checks pass for the changed capability
- [ ] Required workflows are active
- [ ] Latest required workflow is `completed/success`
- [ ] Its `head_sha` equals current default-branch head
- [ ] No new secrets, broken links, stale branch references, or unsupported claims were introduced
