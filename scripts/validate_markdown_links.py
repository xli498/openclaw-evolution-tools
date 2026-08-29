#!/usr/bin/env python3
"""Validate relative Markdown links across repository documentation."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def resolve_repo_target(source: Path, target: str) -> Path | None:
    """Resolve a local link only when it stays inside the repository."""
    resolved = (source.parent / target).resolve()
    try:
        resolved.relative_to(ROOT)
    except ValueError:
        return None
    return resolved


def main() -> int:
    errors: list[str] = []
    files = sorted(ROOT.rglob("*.md"))
    for path in files:
        if ".git" in path.parts:
            continue
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "//", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            resolved = resolve_repo_target(path, target)
            if resolved is None:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository {target}")
            elif not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken relative link {target}")
    if errors:
        print("Markdown link validation failed:", *[f"- {e}" for e in errors], sep="\n")
        return 1
    print(f"Markdown link validation passed: {len(files)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
