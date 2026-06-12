# Review Checklists

## Research Review

- Claims cite primary sources or clearly marked survey sources.
- Claims have claim IDs mapped to source IDs and evidence locations.
- Evidence, inference, recommendation, and uncertainty are separated.
- Dataset names, paper names, dates, and links are checked against current
  sources.
- New papers are placed in the correct section of the reference map.
- No unsupported "best" or "state of the art" claims remain.

## Sphinx Documentation Review

- `make verify` or equivalent build/check target passes.
- MyST directives render as navigation or admonitions, not code blocks.
- The toctree is coherent and uses stable page names.
- Cross-references and static assets resolve under the repository base URL.
- Public pages do not include internal process notes or agent artifacts.
- If branch-source or fallback HTML is used, `.nojekyll`, `html_baseurl`, and
  custom-domain behavior are checked.

## GitHub Pages Review

- Workflow uses official Pages artifact deployment.
- The build job installs pinned or bounded documentation dependencies.
- The deploy job has explicit Pages and id-token permissions.
- Split build/deploy workflows use `needs: build`, `environment: github-pages`,
  and page URL output wiring.
- The workflow does not require privileged API calls to change repo settings.
- Public URL is checked after Actions completes, with allowance for cache delay.

## Visual QA Review

- Homepage, navigation, and at least one content page are checked in a browser.
- Images render at the expected aspect ratio and are not cropped unexpectedly.
- Theme styling loads from the deployed base path.
- Narrow and wide viewports do not hide core content.
- Screenshots are archived when diagnosing a public regression.

## Agent Pack Review

- Every agent spec has frontmatter with `name` and `description`.
- Every skill has a valid `SKILL.md`.
- Agents declare inputs, outputs, checks, and handoff rules.
- Matrix paths, skill references, handoff targets, and workflow agents validate.
- Memory files avoid secrets and one-off noise.
- Validation scripts pass without network access.
