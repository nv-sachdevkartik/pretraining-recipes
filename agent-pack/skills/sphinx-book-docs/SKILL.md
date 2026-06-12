---
name: sphinx-book-docs
description: Use for creating, fixing, or reviewing Sphinx documentation that uses the Sphinx Book Theme, MyST Markdown, and GitHub Pages publishing.
---

# Sphinx Book Docs Skill

Use this skill for Sphinx source edits, Book Theme structure, MyST directives,
static assets, and documentation build quality.

## Workflow

1. Inspect `docs/conf.py`, `docs/index.md` or `index.rst`, requirements, and
   the repository build commands.
2. Keep source pages small and reader-facing.
3. Use MyST directives with correct fences and indentation.
4. Keep generated output out of source unless intentionally used as a fallback.
5. Run the configured local build and verification target.
6. For GitHub Pages fallback or branch-source publishing, check `.nojekyll`,
   `sphinx.ext.githubpages`, `html_baseurl`, and `CNAME` behavior.
7. Hand off to visual QA for screenshots when rendering was part of the issue.

## Checks

- Toctree renders as navigation, not a code block.
- Theme assets load locally.
- Images resolve under the configured base URL.
- GitHub Pages fallback output includes `.nojekyll` when Sphinx generates it.
- Public docs contain research content, not internal agent process notes.
