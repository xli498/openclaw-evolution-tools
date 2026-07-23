#!/usr/bin/env python3
"""Dependency-free validation for OpenClaw SKILL.md files."""
from __future__ import annotations
import json, re, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("name", "description", "triggers", "dependencies", "version", "author", "created")
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

def parse_frontmatter(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---": raise ValueError("frontmatter must start on line 1")
    try: end = lines.index("---", 1)
    except ValueError: raise ValueError("frontmatter is not terminated")
    data = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"): continue
        if ":" not in line: raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        try: data[key] = json.loads(value)
        except json.JSONDecodeError: data[key] = value.strip('"\'')
    return data, "\n".join(lines[end + 1:])

def main():
    errors, names = [], set()
    skills = sorted(ROOT.glob("skills/*/SKILL.md"))
    if not skills: errors.append("no skills/*/SKILL.md found")
    for path in skills:
        tag = path.relative_to(ROOT)
        try: meta, body = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{tag}: {exc}"); continue
        for key in REQUIRED:
            if key not in meta or meta[key] in ("", None): errors.append(f"{tag}: missing {key}")
        if isinstance(meta.get("name"), str):
            if meta["name"] in names: errors.append(f"{tag}: duplicate name {meta['name']}")
            names.add(meta["name"])
        if not isinstance(meta.get("triggers"), list) or not meta.get("triggers"): errors.append(f"{tag}: triggers must be a non-empty JSON/YAML list")
        if not isinstance(meta.get("dependencies"), list): errors.append(f"{tag}: dependencies must be a list")
        if not isinstance(meta.get("version"), str) or not SEMVER.match(meta["version"]): errors.append(f"{tag}: version must be SemVer")
        try: date.fromisoformat(str(meta.get("created")))
        except ValueError: errors.append(f"{tag}: created must be ISO date YYYY-MM-DD")
        for target in LINK.findall(body):
            if target.startswith(("http://", "https://", "mailto:", "#")): continue
            target = target.split("#", 1)[0]
            if target and not (path.parent / target).resolve().exists(): errors.append(f"{tag}: broken relative link {target}")
    if errors:
        print("SKILL validation failed:", *[f"- {e}" for e in errors], sep="\n")
        return 1
    print(f"SKILL validation passed: {len(skills)} skills")
    return 0
if __name__ == "__main__": sys.exit(main())
