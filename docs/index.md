---
title: Welcome to VLA Training Recipes
---

# Welcome to VLA Training Recipes

![VLA data recipe pipeline](_static/img/vla-recipe-map.png)

This documentation is a research handbook for building and evaluating
vision-language-action (VLA) pretraining and mid-training data recipes. It is
organized as an engineering reference: start with the training-stage taxonomy,
map the dataset families, then use the recipe and quality-gate pages as
checklists for building a training corpus.

<section class="recipe-cover" aria-label="VLA training recipe structure">
  <div class="recipe-cover__grid">
    <div class="recipe-cover__item">
      <span class="recipe-cover__label">Stage 01</span>
      <span class="recipe-cover__value">Pretraining data mixtures</span>
    </div>
    <div class="recipe-cover__item">
      <span class="recipe-cover__label">Stage 02</span>
      <span class="recipe-cover__value">Embodied mid-training bridges</span>
    </div>
    <div class="recipe-cover__item">
      <span class="recipe-cover__label">Stage 03</span>
      <span class="recipe-cover__value">Quality gates and holdouts</span>
    </div>
    <div class="recipe-cover__item">
      <span class="recipe-cover__label">Evidence</span>
      <span class="recipe-cover__value">Papers, surveys, and dataset sources</span>
    </div>
  </div>
</section>

<section class="recipe-card-grid" aria-label="Guide sections">
  <a class="recipe-card" href="source/training_stages.html">
    <span>Training Stages</span>
    Separate broad representation learning, embodied bridge training, and target-domain finetuning.
  </a>
  <a class="recipe-card" href="source/datasets.html">
    <span>Dataset Map</span>
    Track public robot corpora, in-domain logs, synthetic rollouts, human video, and reward telemetry.
  </a>
  <a class="recipe-card" href="source/recipes.html">
    <span>Recipe Source Map</span>
    Translate survey and model-paper evidence into practical corpus-building decisions.
  </a>
  <a class="recipe-card" href="source/quality.html">
    <span>Quality Gates</span>
    Define manifest columns, evaluation splits, metadata requirements, and data acceptance checks.
  </a>
  <a class="recipe-card" href="source/references.html">
    <span>References</span>
    Keep the cited VLA surveys, datasets, and model papers in one place.
  </a>
  <a class="recipe-card" href="source/build.html">
    <span>Build and Maintenance</span>
    Maintain the Sphinx build, GitHub Pages workflow, and public artifacts.
  </a>
</section>

## Research Guide

- [Overview](source/overview.md)
- [Training Stages](source/training_stages.md)
- [Dataset Map](source/datasets.md)
- [Recipe Source Map](source/recipes.md)
- [Quality Gates](source/quality.md)
- [References](source/references.md)

## Project

- [Build and Maintenance](source/build.md)
