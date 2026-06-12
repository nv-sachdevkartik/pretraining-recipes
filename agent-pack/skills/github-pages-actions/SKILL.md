---
name: github-pages-actions
description: Use for GitHub Actions based GitHub Pages deployment, Sphinx artifact publishing, Pages workflow debugging, and public URL drift checks.
---

# GitHub Pages Actions Skill

Use this skill when a repository publishes docs to GitHub Pages through GitHub
Actions.

## Workflow

1. Inspect workflow permissions, build job, artifact upload, and deploy job.
2. Confirm the workflow uses official Pages artifact deployment.
3. Avoid privileged REST calls that try to change repository Pages settings at
   runtime.
4. Check Actions status and public URL after deployment.
5. Compare latest commit, built artifact, and public page when the live site
   appears stale.
6. Hand off to visual QA for rendered page inspection.

## Checks

- `pages: write` and `id-token: write` are explicit where required.
- The build artifact contains the expected HTML, CSS, images, and search index.
- The public URL is checked after Actions completes.
- Any required repository setting is documented as an owner action.
