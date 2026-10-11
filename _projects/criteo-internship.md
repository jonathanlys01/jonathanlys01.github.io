---
layout: page
title: Diffusion Background Generation
description: Diffusion-based outpainting pipeline for high-fidelity product image background generation at Criteo AI Lab
img: assets/img/portfolio/shoe.png
importance: 2
category: research
---

*Research project carried out during an internship at Criteo AI Lab, co-hosted by the CAML Core Embeddings and AIR Generative Models teams in Paris, France.*

In the context of online advertising, the goal of this project was to improve the visual appeal of product images (which frequently feature stark, plain white backgrounds) by synthesizing aesthetically coherent backgrounds conditioned on descriptive text prompts. This process is known as **outpainting**, as opposed to standard inpainting where the interior of a bounding box or mask is completed.

<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0 text-center">
    {% include figure.liquid loading="eager" path="assets/img/portfolio/shoe.png" title="Diffusion Background Synthesis" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  Example product background outpainting conditioned on text prompts.
</div>

### Methodology & Contributions

* **Dataset Construction**: Curated a large-scale paired dataset of commercial product photography with diverse environmental contexts and lighting conditions.
* **Diffusion Model Training**: Trained and fine-tuned large-scale latent diffusion models with tailored conditioning for preserving foreground object geometry, lighting consistency, and fine details.
* **ControlNet Architecture**: Leveraged and adapted the [ControlNet](https://arxiv.org/abs/2302.05543) architecture alongside salient object-aware extensions to enforce precise boundary adherence and prevent foreground leakage.

<div class="row justify-content-sm-center">
  <div class="col-sm-10 mt-3 mt-md-0 text-center">
    {% include figure.liquid loading="eager" path="assets/img/portfolio/yahoo-cn.png" title="Model Architecture" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  Salient object-aware conditioning pipeline for text-guided background generation.
</div>
