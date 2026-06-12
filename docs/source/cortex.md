# Cortex 2.0 Addendum

Added paper:
[`Cortex 2.0: Grounding World Models in Real-World Industrial Deployment`](https://arxiv.org/abs/2604.20246).

Project links:

- [Cortex 2.0 project page](https://cortex2.sereact.ai/)
- [Cortex 2.0 benchmark page](https://cortex2.sereact.ai/benchmark)

## Why It Matters

Cortex 2.0 is important because it treats deployment data as a training engine,
not merely an evaluation artifact. The reusable lesson is the pattern:
operational recordings, target teleoperation, open robot data, and synthetic
episodes can train a visual-latent world model plus progress, risk, and
efficiency scoring.

## Dataset Treatment

| Source | How to use it | Public reuse status |
| --- | --- | --- |
| Industrial deployment recordings | In-domain fleet telemetry for world-model training, scoring, and failure mining. | Proprietary; do not list as a downloadable public dataset. |
| Targeted teleoperation | Fill gaps found by deployment failures and benchmark misses. | Collection pattern is reusable; exact data is not public in the checked sources. |
| Open robot data | Public cross-embodiment mixture component. | Reusable when licenses allow. |
| RoboCasa-style synthetic episodes | Curriculum and rare-event expansion. | Validate in real closed loop before scaling ratios. |
| Progress/risk/efficiency telemetry | Train data filters, reward/progress heads, and rollout rankers. | Requires internal label definitions and audit trails. |

## Recipe Implication

If a VLA recipe includes a world model or rollout scorer, keep deployment
telemetry as a named dataset family with its own manifest, quality gates, and
holdout strategy.
