---
title: "REVE Embedding Atlas"
excerpt: "An interactive browser-based explorer for the REVE pretraining dataset with 1M+ projected EEG/MEG windows<br/><img src='/images/portfolio/reve-atlas.png' width='80%'>"
collection: portfolio
date: 2026-09-23
---

*Context: interactive explorer deployed at [jonathanlys01.github.io/reve-atlas](https://jonathanlys01.github.io/reve-atlas/). Source code available on [GitHub](https://github.com/jonathanlys01/reve-atlas) and public Parquet tables hosted on [Hugging Face](https://huggingface.co/datasets/jonathan-lys/reve-atlas).*

[REVE](https://arxiv.org/abs/2510.21585) (*Representation for EEG with Versatile Embeddings*) is a foundation model for EEG and MEG signals, pretrained on over 60,000 hours of recording data spanning 92 datasets and 25,000 subjects.

The **REVE Embedding Atlas** is an interactive, serverless web application that allows researchers and users to visually explore and analyze projected EEG and MEG windows from the REVE-1 pretraining set directly in the browser:

<p align="center">
  <a href="https://jonathanlys01.github.io/reve-atlas/" target="_blank" rel="noopener noreferrer">
    <img src="/images/portfolio/reve-atlas.png" alt="REVE Embedding Atlas Screenshot" width="100%" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" />
  </a>
</p>

### Key Features

* **Interactive Embedding Exploration**: Visualizes projected 2D embeddings of over 1,000,000 EEG/MEG windows using [Apple Embedding Atlas](https://github.com/apple/embedding-atlas), color-coded across diverse datasets (TUH, ICARE, OpenNeuro benchmarks, NMT, and more).
* **Completely Serverless (DuckDB-WASM)**: Queries public Parquet tables hosted on Hugging Face directly inside the browser using DuckDB-WASM and HTTP byte-range requests—requiring no application backend, server infrastructure, or client-side authentication tokens.
* **Subset & Diversity Selection**: Explores precomputed Determinantal Point Processes (DPP) and ranking selections across candidate pools, evaluating the trade-off between reconstruction loss and Vendi diversity scores.
* **Cross-Filtering & Metadata Analytics**: Live filtering with SQL predicates, reconstruction loss histograms, recording index distributions, and dataset breakdowns.

### Links

* **Live Demo**: [jonathanlys01.github.io/reve-atlas](https://jonathanlys01.github.io/reve-atlas/)
* **Code Repository**: [github.com/jonathanlys01/reve-atlas](https://github.com/jonathanlys01/reve-atlas)
* **Dataset on Hugging Face**: [huggingface.co/datasets/jonathan-lys/reve-atlas](https://huggingface.co/datasets/jonathan-lys/reve-atlas)
* **Related Paper**: [REVE: A Foundation Model for EEG (NeurIPS 2025)](https://arxiv.org/abs/2510.21585)
