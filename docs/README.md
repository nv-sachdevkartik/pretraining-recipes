# Building Documentation

We use [Sphinx](https://www.sphinx-doc.org/en/master/) with the
[Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/stable/) for
maintaining and generating the documentation.

To avoid dependency conflicts, use a Python virtual environment when possible.

## Current Documentation

Linux:

```bash
cd docs
python -m pip install -r requirements.txt
make current-docs
xdg-open _build/current/index.html
```

Windows:

```bat
cd docs
python -m pip install -r requirements.txt
make current-docs
start _build\current\index.html
```

## Repository Layout

```text
docs/
  conf.py              Sphinx configuration
  index.md             top-level table of contents
  source/              maintained documentation chapters
  _static/css/         small project-specific style overrides
  _build/current/      generated HTML output
```
