# Agent Pack Operating Contract

This file is the shared contract for all agents in this package.

## Mission

Help maintain high-quality VLA pretraining and mid-training research
documentation by combining evidence-first research, lean implementation,
public-site QA, expert review, and durable memory.

## Non-Negotiables

- Use primary sources when making research claims: papers, official project
  pages, official repositories, dataset cards, and documentation.
- Separate evidence, inference, recommendations, and open questions.
- Keep reusable process notes in this package, not in the public handbook.
- Validate before publishing: build docs, inspect rendered output, and check
  assets.
- Keep changes scoped and lean. Do not add framework or process weight unless
  it improves repeatability.

## Session Learnings To Preserve

- Sphinx source files must use correct MyST directive syntax. If a toctree is
  rendered as a code block, inspect indentation and directive fences first.
- GitHub Pages Actions should publish the built artifact. Do not rely on a
  workflow step that tries to mutate Pages settings with insufficient token
  permissions.
- Broken public styling often means the site is serving stale or fallback HTML.
  Compare source, built local HTML, Actions artifacts, and the live URL.
- Use SVG or well-managed static assets for diagrams. If legacy PNG paths still
  exist, refresh them or keep compatibility copies.
- Public docs should not include internal review labels, process commentary,
  or "agent voice" artifacts.

## Review Culture

Reviewers should be direct and specific. Findings lead, with file paths and
lines where possible. Summaries are secondary. A reviewer should reject content
that is unsourced, overconfident, stale, or inappropriate for public docs.

## Memory Policy

Durable memory is for reusable operating knowledge:

- Decisions that should guide future work.
- Failure modes and their fixes.
- Project-specific conventions.
- Source links that anchor recurring research.

Do not store transient mood, one-off debugging noise, private credentials, or
large copied excerpts from copyrighted sources.
