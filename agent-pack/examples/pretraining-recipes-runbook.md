# Pretraining Recipes Runbook

Use this runbook when maintaining the VLA pretraining recipes docs.

## Research

1. Use `vla-researcher` to gather sources.
2. Add new papers to the reference map with source links.
3. Keep dataset family recommendations tied to evidence.

## Docs

1. Use `sphinx-docs-builder` for source edits.
2. Run `make verify` from the docs repository when available.
3. Check that MyST directives render correctly.

## Deployment

1. Use `github-pages-deployer` to inspect Actions and Pages output.
2. Avoid workflow steps that require changing Pages settings at runtime.
3. Let Actions deploy the Sphinx artifact.

## Visual QA

1. Inspect the public URL after Actions completes.
2. Compare with local HTML if the public page looks stale.
3. Check image paths and dimensions directly.

## Review And Memory

1. Use `expert-reviewer` to reject weak claims or public process artifacts.
2. Use `memory-curator` to capture reusable decisions and failure modes.
