# VLA Agent Pack

Reusable agents, skills, memory, and review checklists extracted from the VLA
pretraining recipes documentation effort.

This package is intentionally separate from the public documentation content.
It stores operating knowledge for researchers, documentation builders, website
debuggers, deployers, reviewers, and memory curators without leaking process
notes into the published reader-facing handbook.

## What This Contains

- `agents/`: reusable agent specifications with roles, tool boundaries,
  memory contracts, and handoff rules.
- `skills/`: Codex-compatible skills that can be installed or copied into an
  agent runtime.
- `memory/`: durable learnings and schemas for deciding what should survive
  between sessions.
- `review/`: quality gates for research content, Sphinx docs, GitHub Pages,
  visual rendering, and agent hygiene.
- `references/`: source-backed best practices used to design the pack.
- `scripts/`: small standard-library utilities for validation and fan-out
  planning.
- `templates/`: reusable task packets and memory records.
- `soul/`: concise operating principles that shape agent behavior.

## Quick Start

```bash
cd ~/pretrain/vla-agent-pack
python3 scripts/validate_pack.py .
python3 scripts/fanout_plan.py --goal "Refresh VLA dataset recipe docs"
```

To use the Codex skills, copy the desired skill folder from `skills/` into the
runtime skill directory, or keep this repository as a reference pack and have
agents read the relevant `SKILL.md` files directly.

## Core Workflow

1. Start with `agents/orchestrator.agent.md`.
2. Split research, documentation, deploy, visual QA, review, and memory tasks
   using `scripts/fanout_plan.py`.
3. Require source-backed research before content edits.
4. Run local validation before publishing.
5. Ask an expert reviewer agent to check claims, structure, and public-facing
   tone.
6. Curate durable memory at the end of the work, keeping only reusable facts,
   decisions, and failure modes.

## Design Principles

- Prefer a single focused agent when handoff would add overhead.
- Use multi-agent fan-out when evidence gathering, implementation, review, and
  visual QA can proceed independently.
- Keep public documentation free of internal process artifacts.
- Treat memory as a data product: scoped, deduplicated, source-linked, and
  revisited when it becomes stale.
- Self-correction is a workflow, not a slogan: every agent needs explicit
  verification steps and a reviewer with permission to reject weak output.

## GitHub Placement

The canonical editable copy can live at `~/pretrain/vla-agent-pack`. A mirrored
copy may be committed under `agent-pack/` in the `pretraining-recipes`
repository so the package can be reviewed and versioned with the docs project.
