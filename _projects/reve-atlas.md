---
layout: page
title: REVE Embedding Atlas
description: Explore a million EEG and MEG windows, directly in your browser.
img: assets/img/portfolio/reve-atlas.png
importance: 1
category: research
related_publications: true
---

The **REVE Embedding Atlas** is an interactive, serverless web application that allows researchers to visually explore and analyze projected EEG and MEG windows from the [REVE](https://brain-bzh.github.io/reve/) pretraining dataset (25,000 subjects across 92 datasets) directly in the browser.

<div class="row justify-content-sm-center">
  <div class="col-sm-10 mt-3 mt-md-0 text-center">
    <a href="https://jonathanlys01.github.io/reve-atlas/" target="_blank" rel="noopener noreferrer">
      {% include figure.liquid loading="eager" path="assets/img/portfolio/reve-atlas.png" title="REVE Embedding Atlas Screenshot" class="img-fluid rounded z-depth-1" %}
    </a>
  </div>
</div>
<div class="caption">
  Interactive 2D embedding atlas powered by Apple Embedding Atlas and DuckDB-WASM.
</div>

### Highlights

- **Interactive Embedding Exploration**: Visualizes projected 2D embeddings of over 1,000,000 EEG/MEG windows using Apple Embedding Atlas, color-coded across diverse datasets (TUH, ICARE, OpenNeuro, etc.).
- **Completely Serverless (DuckDB-WASM)**: Queries public Parquet tables hosted on Hugging Face directly inside the browser using DuckDB-WASM and HTTP byte-range requests — zero backend server required.
- **Subset & Diversity Selection**: Explores Determinantal Point Processes (DPP) and ranking selections across candidate pools.
- **Live Cross-Filtering**: Real-time SQL predicate filtering, reconstruction loss histograms, and dataset breakdowns.

### Links

- **Live Explorer**: [jonathanlys01.github.io/reve-atlas](https://jonathanlys01.github.io/reve-atlas/)
- **Code Repository**: [github.com/jonathanlys01/reve-atlas](https://github.com/jonathanlys01/reve-atlas)
- **Dataset on Hugging Face**: [huggingface.co/datasets/jonathan-lys/reve-atlas](https://huggingface.co/datasets/jonathan-lys/reve-atlas)
