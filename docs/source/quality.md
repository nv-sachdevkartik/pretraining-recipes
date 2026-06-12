# Quality Gates

Dataset scale is useful only when data is identifiable, synchronized, and
evaluable. These gates should exist before any dataset enters a pretraining or
mid-training mixture.

| Gate | Requirement | Failure avoided |
| --- | --- | --- |
| Source identity | Every episode has dataset, robot, site, task, camera, and collection-protocol IDs. | Aggregate metrics hide bad or dominant sources. |
| Action normalization | Units, control frequency, coordinate frame, gripper convention, and horizon are explicit. | The model learns incompatible actuator semantics. |
| Temporal sync | Video, proprioception, action, force/contact, language, and outcome streams are aligned. | The policy learns lagged or impossible labels. |
| Language audit | Instructions match episode behavior; templated instructions are marked. | Offline instruction metrics fail under paraphrase. |
| Outcome labels | Success, failure, partial progress, intervention, reset, and retry semantics are documented. | Reward heads learn site or operator shortcuts. |
| Holdout design | Split by task, object, embodiment, operator, site, and collection time where possible. | Pretraining leaks deployment evaluation. |
| Synthetic provenance | Simulator, assets, randomization, renderer, controller, prompt, and seed are recorded. | Synthetic improvements cannot be reproduced or debugged. |
| Closed-loop eval | Offline loss is paired with real or high-fidelity success, robustness, and safety metrics. | Token prediction improves while robot behavior regresses. |

## Manifest Columns

Minimum useful episode manifest:

```text
episode_id, source_dataset, robot_id, embodiment_family, task_id,
language_instruction, camera_ids, action_space, control_hz, state_schema,
success_label, failure_type, intervention_type, site_id, operator_id,
collection_time, license, train_val_test_split
```
