---
name: vla-researcher
description: Use for VLA pretraining or mid-training research, dataset maps, survey synthesis, paper integration, and evidence-backed recipe recommendations.
---

# VLA Researcher Skill

Use this skill when the task involves VLA datasets, pretraining, mid-training,
recipe design, survey papers, or adding papers to a VLA knowledge base.

## Workflow

1. Define the research question and the expected artifact.
2. Search current sources. Prefer papers, official project pages, official
   repositories, dataset cards, and benchmark docs.
3. Use surveys to structure the topic, then verify specific claims against
   primary sources.
4. Build a source table with title, URL, source type, date or version, and
   relevance.
5. Separate evidence, inference, recommendation, and uncertainty.
6. Ask the expert reviewer to check claims before public docs are updated.

## Output Shape

- Dataset families needed for pretraining.
- Dataset families needed for mid-training.
- Which sources support each family.
- Recipe recommendations and caveats.
- Open questions.

## Checks

- No uncited dataset claims.
- No stale "latest" claims without current web verification.
- Newly requested papers are included in references and recipe implications.
