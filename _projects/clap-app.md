---
layout: page
title: CLAP Sound Retrieval
description: Finding sounds with language, and exploring the space between them.
img: assets/img/portfolio/clap-viz.png
importance: 3
category: machine learning
---

_Project developed as part of the Deep Learning coursework at IMT Atlantique. Code and materials available on [GitHub](https://github.com/jonathanlys01/DL_2023_CLAP)._

**CLAP** (_Contrastive Language-Audio Pretraining_) is a multimodal learning strategy that projects audio signals and natural language descriptions into a shared representation space. The model is trained via contrastive objectives to maximize mutual information between corresponding text-audio pairs while repelling non-matching pairs.

With an aligned representation space, the model unlocks:

- **Zero-shot Sound Classification**: Classifying audio clips into unseen categories using natural language prompts.
- **Text-Prompted Audio Retrieval**: Searching large sound archives using arbitrary descriptive sentences.
- **Interactive Latent Exploration**: Visualizing and analyzing clustering behavior of acoustic features.

<div class="row justify-content-sm-center">
  <div class="col-sm-10 mt-3 mt-md-0 text-center">
    {% include figure.liquid loading="eager" path="assets/img/portfolio/clap-viz.png" title="CLAP Latent Space Visualization" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  2D t-SNE projection of the aligned text-audio latent space evaluated on ESC-50.
</div>

### Links

- **Source Code**: [github.com/jonathanlys01/DL_2023_CLAP](https://github.com/jonathanlys01/DL_2023_CLAP)
