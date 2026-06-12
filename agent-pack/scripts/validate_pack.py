#!/usr/bin/env python3
"""Validate the VLA agent pack structure without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "agent_matrix.yaml",
    "soul/operating_principles.md",
    "references/agent_best_practices.md",
    "memory/memory_schema.yaml",
    "memory/session_learnings.md",
    "review/checklists.md",
    "templates/task_packet.md",
]

BANNED_PUBLIC_ARTIFACTS = [
    "".join(["Senior", " Robotics", " Rule"]),
    "".join(["Recipe", " Implication"]),
    "".join(["The main", " design decision", " is"]),
    "".join(["Out", " of scope", ":"]),
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise AssertionError(f"{path}: must be UTF-8 text") from exc


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = read_text(path)
    if not text.startswith("---\n"):
        raise AssertionError(f"{path}: missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise AssertionError(f"{path}: unterminated YAML frontmatter")
    data: dict[str, str] = {}
    for raw_line in text[4:end].splitlines():
        if not raw_line.strip() or raw_line.startswith("  - "):
            continue
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        data[key.strip()] = value.strip()
    for key in ("name", "description"):
        if not data.get(key):
            raise AssertionError(f"{path}: frontmatter missing {key}")
    return data


def validate_required(root: Path) -> list[str]:
    errors = []
    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            errors.append(f"missing required file: {rel}")
    return errors


def validate_frontmatter(root: Path) -> list[str]:
    errors = []
    for path in sorted((root / "agents").glob("*.agent.md")):
        try:
            data = parse_frontmatter(path)
            expected = path.name.removesuffix(".agent.md")
            if data["name"] != expected:
                errors.append(f"{path}: name {data['name']!r} does not match {expected!r}")
        except AssertionError as exc:
            errors.append(str(exc))
    for path in sorted((root / "skills").glob("*/SKILL.md")):
        try:
            parse_frontmatter(path)
        except AssertionError as exc:
            errors.append(str(exc))
    return errors


def validate_artifacts(root: Path) -> list[str]:
    errors = []
    scan_roots = [root / "README.md", root / "AGENTS.md", root / "agents", root / "skills"]
    paths: list[Path] = []
    for item in scan_roots:
        if item.is_file():
            paths.append(item)
        elif item.is_dir():
            paths.extend(item.rglob("*.md"))
    for path in sorted(paths):
        text = read_text(path)
        for banned in BANNED_PUBLIC_ARTIFACTS:
            if banned in text:
                errors.append(f"{path}: contains banned process artifact {banned!r}")
    return errors


def validate_ascii_for_specs(root: Path) -> list[str]:
    errors = []
    for path in sorted(root.rglob("*.md")) + sorted(root.rglob("*.yaml")):
        text = read_text(path)
        if re.search(r"[^\x09\x0a\x0d\x20-\x7e]", text):
            errors.append(f"{path}: contains non-ASCII text")
    return errors


def main(argv: list[str]) -> int:
    root = Path(argv[1] if len(argv) > 1 else ".").expanduser().resolve()
    errors = []
    errors.extend(validate_required(root))
    errors.extend(validate_frontmatter(root))
    errors.extend(validate_artifacts(root))
    errors.extend(validate_ascii_for_specs(root))
    if errors:
        print("validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    agent_count = len(list((root / "agents").glob("*.agent.md")))
    skill_count = len(list((root / "skills").glob("*/SKILL.md")))
    print(f"ok: {root} ({agent_count} agents, {skill_count} skills)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
