# Dataset Map

Pretraining and mid-training need different data mixtures. The same corpus can
be useful in both stages, but only if source identity, action representation,
and evaluation boundaries are preserved.

## Pretraining Dataset Families

| Family | Representative sources | Why it is needed | Required metadata |
| --- | --- | --- | --- |
| Cross-embodiment robot trajectories | Open X-Embodiment, BridgeData V2, DROID, RoboNet, Language Table, RT-X-style corpora. | Provides manipulation diversity across robots, cameras, objects, tasks, and action spaces. | Source dataset, embodiment ID, instruction, video, state, action, camera metadata, episode outcome. |
| In-domain robot and deployment data | Target robot teleoperation, lab fleet logs, production recordings, Cortex 2.0-style industrial data. | Captures object distributions, workcell geometry, contact states, failures, and recoveries missing from public corpora. | Robot/site/task IDs, timestamps, interventions, failures, retries, operator metadata, sensor availability. |
| Humanoid and bimanual data | GR00T N1-style humanoid data, RH20T, ALOHA/ACT-style bimanual data. | Needed for whole-body, dexterous, or bimanual control where arm-only data is insufficient. | Joint schema, action space, teleop interface, camera rig, contact state, embodiment family. |
| Human egocentric and actionless video | Ego4D, EPIC-KITCHENS, HowTo-style instructional video, LAPA/LAWM/VideoVLA-style sources. | Adds temporal procedure knowledge, affordances, and human intent at larger scale than robot data. | Narration/captions, action labels if available, object events, time alignment, task tags. |
| Synthetic and simulation data | RoboCasa, RLBench, CALVIN, ManiSkill, Isaac Sim rollouts, generated world-model data. | Expands rare events, curricula, perturbations, and controllable long-tail coverage. | Simulator version, assets, controller, randomization, success labels, sim-to-real tags. |
| Auxiliary vision-language data | Image-text, video-text, robotics captions, embodied QA, affordance data. | Builds object recognition, OCR, grounding, and instruction following. | Provenance, filtering scores, licenses, task/domain tags. |
| World-model visual data | Robot videos, human videos, deployment recordings, Cosmos/DreamGen-style physical video. | Supports predictive dynamics, future-state modeling, and rollout scoring. | Ordered frames, camera metadata, state/action when available, outcome/event labels. |
| Reward, outcome, and failure telemetry | Intervention logs, collision/contact flags, success/failure traces, Cortex 2.0 PRO-style telemetry. | Trains progress, risk, completion, and efficiency heads; improves data filtering and rollout ranking. | Outcome definitions, event labels, intervention type, timestamps, state/action history. |

## Mid-Training Dataset Families

| Family | Representative sources | Use | Quality bar |
| --- | --- | --- | --- |
| Embodied VLM bridge data | Embodied QA, scene grounding, affordance questions, spatial reasoning, task decomposition. | Preserves VLM reasoning while adapting it to robot-relevant visual targets. | Questions must be grounded in observable state and action-relevant scene features. |
| Related robot trajectories | BridgeData V2, DROID, OXE subsets close to the target robot or camera setup. | Adapts representations to action prediction before target-domain finetuning. | Keep embodiment IDs and action normalization explicit. |
| Target-embodiment seed demos | Clean teleoperation on target robot, including easy, hard, perturbation, failure, and recovery episodes. | Anchors the action head and robot-state interface. | Prefer coverage and metadata over only perfect demonstrations. |
| Human video latent-action bridge | LAPA, LAWM, VideoVLA, action-tokenized egocentric video. | Adds long-horizon temporal structure when robot actions are unavailable. | Verify latent actions correspond to robot-executable changes. |
| Synthetic curriculum data | RoboCasa, RLBench, CALVIN, ManiSkill, generated perturbations. | Fills task gaps and balances object/task distributions. | Track generator and cap ratios unless closed-loop validation supports more. |
| Reward/progress/failure bridge | Progress scores, near misses, intervention flags, Cortex 2.0-style telemetry. | Trains ranking, progress, risk, and episode-quality models. | Requires dense, consistent label definitions and held-out deployment traces. |
