# Recipe Source Map

The dataset map is synthesized from VLA survey papers and concrete recipe
papers. The repeated pattern is simple: broad robot data gives transfer, target
data gives deployment relevance, and bridge objectives make VLM features useful
for action.

| Recipe family | Dataset signal | Training lesson |
| --- | --- | --- |
| RT-1 / RT-2 / RT-X | Large robot demos, web-scale VLM data, cross-embodiment mixtures. | General VL knowledge helps, but robot action data is the control substrate. |
| Open X-Embodiment / Octo / OpenVLA | OXE, BridgeData, DROID, RoboNet, RT-1-style corpora. | Open baselines depend on heterogeneous robot trajectory mixtures. |
| pi0 / pi0.5 | Large robot data, web-scale knowledge, action chunking and flow matching. | Action interface and horizon choices matter as much as raw scale. |
| GR00T N1 | Humanoid and manipulation demos, synthetic augmentation, simulation, multi-embodiment data. | Humanoid VLAs need explicit embodiment and control-schema metadata. |
| RDT / SmolVLA / LingBot / X-VLA | Compact policies, robot mixtures, language-conditioned manipulation. | Smaller models still need strong data curation and action normalization. |
| Qwen-VLA / VLA Foundry-style recipes | VLM initialization, embodied action tuning, mixture ablations. | Mid-training should be separate from final task finetuning. |
| EmbodiedMidtrain and VLM-initialization studies | Embodied QA, robot data, task reasoning, initialization ablations. | VLM initialization is not automatically optimal for control without embodied adaptation. |
| LAPA / LAWM / VideoVLA / FAST | Human videos, latent actions, action tokenization. | Actionless video can teach temporal structure when converted into robot-relevant latent supervision. |
| DreamGen / Cosmos / world-model VLA work | Synthetic physical video, generated rollouts, dynamics data. | World-model data can expand coverage, but needs real closed-loop validation. |
| Cortex 2.0 | Deployment recordings, targeted teleoperation, public robot data, synthetic simulation. | Deployment telemetry is a first-class training asset for world models and reward/progress scoring. |

## Practical Shopping List

| Priority | Dataset asset | Stage |
| --- | --- | --- |
| P0 | OXE-derived public robot mixture with BridgeData V2, DROID, RT-X-style sources, RoboNet, and Language Table where licenses permit. | Pretraining and mid-training baseline. |
| P0 | Target robot teleoperation with success, partial success, failure, recovery, and perturbation episodes. | Mid-training and finetuning. |
| P0 | Fleet/deployment telemetry with interventions and outcome labels. | Pretraining, world modeling, reward/progress modeling. |
| P1 | Egocentric/instructional human video converted to representation or latent-action objectives. | Pretraining and mid-training bridge. |
| P1 | Simulation and synthetic curricula for rare events and controllable perturbations. | Pretraining, mid-training, stress testing. |
| P1 | Embodied VLM instruction, QA, spatial reasoning, and task-decomposition data. | Mid-training. |
| P2 | Generated world-model rollouts with provenance separated from real logs. | World-model pretraining and scoring. |
