# Session Learnings

Scope: VLA pretraining recipes documentation and agent-pack maintenance.
Last verified: 2026-06-12.
Source: observed session outcomes, local repository checks, and linked
best-practice references.

## Public Documentation Hygiene

Public VLA docs should focus on research content, datasets, recipe choices, and
quality gates. Internal labels, reviewer slogans, implementation rationale, and
agent commentary belong in this pack or another private notes area.

## Sphinx And MyST

Type: failure_mode. Confidence: high.

If Sphinx renders navigation directives as code blocks, inspect MyST directive
syntax and indentation. The fastest signal is to compare the rendered homepage
with the raw source and the local build output.

## GitHub Pages

Type: project_convention. Confidence: high.

Use GitHub Actions to build and deploy the Sphinx artifact. A workflow token may
not be allowed to update Pages settings through the REST API, so the workflow
should not depend on mutating repository Pages settings at deploy time.

## Assets

Type: failure_mode. Confidence: medium.

For stable public diagrams, prefer SVG when it can represent the information
cleanly. If older PNG paths are still referenced by existing pages or caches,
refresh compatibility copies instead of leaving broken assets behind.

## Visual QA

Type: workflow_pattern. Confidence: high.

A docs build can pass while the public site is visually broken. Always check:

- Local rendered HTML.
- Browser console or network failures when available.
- Static asset paths under the deployed base URL.
- Whether the public site is stale relative to the latest commit.

## VLA Research

Type: project_convention. Confidence: high.

For VLA pretraining and mid-training recipe content, keep dataset lists tied to
paper or dataset sources. Mark recommendations as recommendations, not facts.
Keep newly added papers in the reference map and state why they affect the
recipe.
