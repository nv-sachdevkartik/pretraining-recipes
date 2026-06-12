# Overview

This project tracks dataset and training-recipe knowledge for VLA systems. It
is not a model implementation and should stay documentation-first unless the
repository grows a tested library later.

## Review Finding

The previous public repository was a hand-written static HTML page. That made
the content hard to extend because navigation, style, references, and research
claims all lived in one file.

The corrected structure is:

- Sphinx source in `docs/`
- topic pages in `docs/source/`
- a small Book Theme configuration in `docs/conf.py`
- reproducible local build commands in `docs/Makefile`
- a GitHub Pages workflow in `.github/workflows/docs.yml`

## Scope

Covered:

- VLA pretraining and mid-training taxonomy
- dataset families and mixture design
- recipe evidence from VLA papers and surveys
- Cortex 2.0 deployment-data guidance
- quality gates for real, synthetic, and deployment telemetry

Out of scope:

- downstream policy finetuning except as contrast
- RL post-training recipes
- deployment operations beyond data-loop implications
