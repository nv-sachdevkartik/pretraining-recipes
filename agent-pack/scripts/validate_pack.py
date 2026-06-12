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
    "templates/evidence_record.yaml",
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
            data = parse_frontmatter(path)
            expected = path.parent.name
            if data["name"] != expected:
                errors.append(f"{path}: name {data['name']!r} does not match {expected!r}")
        except AssertionError as exc:
            errors.append(str(exc))
    return errors


def parse_matrix(root: Path) -> tuple[dict[str, dict[str, object]], list[str], str | None]:
    text = read_text(root / "agent_matrix.yaml")
    agents: dict[str, dict[str, object]] = {}
    workflow_agents: list[str] = []
    entry_agent: str | None = None
    in_agents = False
    current: str | None = None
    handoff_mode = False

    for line in text.splitlines():
        if line.startswith("  entry_agent:"):
            entry_agent = line.split(":", 1)[1].strip()
        if line == "agents:":
            in_agents = True
            continue
        if line == "workflows:":
            in_agents = False
            current = None
            handoff_mode = False
            continue
        if in_agents:
            match = re.match(r"^  ([a-z0-9-]+):\s*$", line)
            if match:
                current = match.group(1)
                agents[current] = {"handoffs": []}
                handoff_mode = False
                continue
            if not current:
                continue
            if line.startswith("    file:"):
                agents[current]["file"] = line.split(":", 1)[1].strip()
            elif line.startswith("    skill:"):
                agents[current]["skill"] = line.split(":", 1)[1].strip()
            elif line.startswith("    can_handoff_to:"):
                handoff_mode = True
            elif handoff_mode and line.startswith("      - "):
                agents[current]["handoffs"].append(line.split("-", 1)[1].strip())
            elif line.startswith("    ") and not line.startswith("      "):
                handoff_mode = False
        else:
            stage = re.match(r"^\s+-\s+([a-z0-9-]+):", line)
            if stage:
                workflow_agents.append(stage.group(1))
    return agents, workflow_agents, entry_agent


def validate_matrix(root: Path) -> list[str]:
    errors: list[str] = []
    agents, workflow_agents, entry_agent = parse_matrix(root)
    if not agents:
        return ["agent_matrix.yaml: no agents parsed"]
    if entry_agent not in agents:
        errors.append(f"agent_matrix.yaml: entry_agent {entry_agent!r} is not a known agent")
    for name, spec in agents.items():
        file_value = spec.get("file")
        if not isinstance(file_value, str):
            errors.append(f"agent_matrix.yaml: agent {name} missing file")
        elif not (root / file_value).is_file():
            errors.append(f"agent_matrix.yaml: agent {name} file does not exist: {file_value}")
        skill_value = spec.get("skill")
        if isinstance(skill_value, str) and not (root / skill_value).is_file():
            errors.append(f"agent_matrix.yaml: agent {name} skill does not exist: {skill_value}")
        for target in spec.get("handoffs", []):
            if target not in agents:
                errors.append(f"agent_matrix.yaml: agent {name} hands off to unknown agent {target}")
    for agent in workflow_agents:
        if agent not in agents:
            errors.append(f"agent_matrix.yaml: workflow references unknown agent {agent}")
    return errors


def validate_agent_contracts(root: Path) -> list[str]:
    errors: list[str] = []
    required_sections = ["# Inputs", "# Outputs", "# Handoff", "# Self-Check"]
    for path in sorted((root / "agents").glob("*.agent.md")):
        text = read_text(path)
        for section in required_sections:
            if section not in text:
                errors.append(f"{path}: missing required section {section}")
    return errors


def schema_required_fields(root: Path, record_type: str) -> list[str]:
    text = read_text(root / "memory/memory_schema.yaml")
    fields: list[str] = []
    in_record = False
    in_required = False
    for line in text.splitlines():
        if re.match(r"^  [a-z_]+:\s*$", line):
            in_record = line.strip() == f"{record_type}:"
            in_required = False
            continue
        if in_record and line.strip() == "required_fields:":
            in_required = True
            continue
        if in_required:
            if line.startswith("      - "):
                fields.append(line.split("-", 1)[1].strip())
            elif line and not line.startswith("      "):
                break
    return fields


def top_level_yaml_keys(path: Path) -> set[str]:
    keys = set()
    for line in read_text(path).splitlines():
        if line and not line.startswith(" ") and ":" in line:
            keys.add(line.split(":", 1)[0].strip())
    return keys


def validate_templates(root: Path) -> list[str]:
    errors: list[str] = []
    memory_template = root / "templates/memory_record.yaml"
    memory_keys = top_level_yaml_keys(memory_template)
    memory_type = next(
        (
            line.split(":", 1)[1].strip()
            for line in read_text(memory_template).splitlines()
            if line.startswith("type:")
        ),
        "",
    )
    for field in schema_required_fields(root, memory_type):
        if field not in memory_keys:
            errors.append(f"{memory_template}: missing schema field {field}")

    evidence_template = root / "templates/evidence_record.yaml"
    evidence_keys = top_level_yaml_keys(evidence_template)
    for key in ("source_id", "title", "url", "source_type", "accessed", "claims_supported"):
        if key not in evidence_keys:
            errors.append(f"{evidence_template}: missing required key {key}")
    return errors


def validate_artifacts(root: Path) -> list[str]:
    errors = []
    paths = sorted(root.rglob("*.md")) + sorted(root.rglob("*.yaml"))
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
    errors.extend(validate_matrix(root))
    errors.extend(validate_agent_contracts(root))
    errors.extend(validate_templates(root))
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
