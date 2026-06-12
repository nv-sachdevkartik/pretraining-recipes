# Training Stages

The useful split is not simply "pretraining" versus "finetuning." VLA systems
usually need a bridge stage that adapts a general VLM or robot foundation model
to embodied action before final task specialization.

| Stage | Goal | Primary data | Keep separate |
| --- | --- | --- | --- |
| Pretraining | Learn broad visual, language, temporal, physical, and action representations. | Vision-language data, cross-embodiment robot trajectories, human video, synthetic rollouts, world-model video, deployment telemetry. | Held-out sites, target tasks, final evaluation objects. |
| Mid-training | Bridge representations into robot-control interfaces. | Embodied QA, related robot trajectories, action-token or latent-action data, target-embodiment seed demos, reward/progress labels. | Final robot benchmark episodes. |
| Finetuning | Adapt to a robot, task family, controller, and safety envelope. | Target robot demos, interventions, recoveries, perturbations, site-specific failures. | Evaluation splits by task, object, operator, site, and collection time. |
