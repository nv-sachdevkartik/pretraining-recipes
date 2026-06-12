---
name: agent-pack-maintenance
description: Use for maintaining reusable agent packs, memory schemas, validation scripts, task packet templates, and self-correction workflows.
---

# Agent Pack Maintenance Skill

Use this skill when adding or reviewing reusable agents, skills, memory, or
review workflows.

## Workflow

1. Decide whether the change belongs in an agent spec, skill, memory file,
   checklist, script, or reference.
2. Keep agent specs short and operational.
3. Keep skills self-contained with `SKILL.md` frontmatter.
4. Keep memory compact and source-linked.
5. Run `python3 scripts/validate_pack.py .`.
6. Review for process artifacts that should not be mirrored into public docs.

## Checks

- Agent and skill frontmatter include `name` and `description`.
- Handoff rules are explicit.
- Validation is standard-library only.
- Durable memory avoids secrets and transient noise.
