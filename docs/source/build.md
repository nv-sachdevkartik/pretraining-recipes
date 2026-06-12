# Build and Maintenance

## Local Build

```bash
cd docs
python -m pip install -r requirements.txt
make current-docs
```

The generated HTML is written to:

```text
docs/_build/current/
```

## Verify

```bash
make -C docs current-docs
```

The build uses `-W --keep-going`, so warnings fail the build while still
showing the full warning set.

## GitHub Pages

The public site is deployed by `.github/workflows/docs.yml`. In repository
settings, GitHub Pages must use `Source: GitHub Actions`; branch publishing will
serve the Markdown fallback instead of the Sphinx artifact.

## Extend

Add new pages under `docs/source/`, then include them in the relevant
`toctree` in `docs/index.rst`.

Keep pages narrow:

- one concept per file
- tables for dataset and recipe matrices
- references near the claim they support
- no generated HTML edits by hand
