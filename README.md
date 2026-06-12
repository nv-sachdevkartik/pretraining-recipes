# Pretraining Recipes

Research notes and dataset guidance for VLA pretraining and mid-training.

The maintained source lives in `docs/` and is built with Sphinx and the
Sphinx Book Theme.

## Browse

Public documentation:

```text
https://nv-sachdevkartik.github.io/pretraining-recipes/
```

## Build

```bash
cd docs
python -m pip install -r requirements.txt
make current-docs
```

Open the generated site:

```bash
xdg-open _build/current/index.html
```

## Scope

- VLA pretraining and mid-training definitions
- dataset requirements and mixture design
- recipe and ablation guidance
- architecture, action representation, infrastructure, and evaluation notes
- Cortex 2.0 deployment-data addendum

Post-training, preference learning, RL, and deployment adaptation are out of
scope except when they clarify the boundary with pretraining or mid-training.
