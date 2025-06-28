---
title: "Criteo Internship"
excerpt: "A diffusion-based image background generation project<br/><img src='/images/portfolio/shoe.png' width='300'>"
collection: portfolio
date: 2024-10-11
---

*Context: internship at Criteo AI Lab, where I worked on the AdBooster project. It was co-hosted by the CAML Core Embeddings and AIR Generative models teams at Criteo, Paris, FR*

In the context of online advertising, the idea is to improve the visual quality of a product image, often originally with a plain white background, by generating an aesthetically pleasing background, conditionally to a text prompt. This process is called **outpainting** as opposed to inpainting, where the goal is to fill in missing parts of an image.

During the internship, I built a dataset, trained several large diffusion models for image background generation, and implemented a pipeline to generate high-quality images.

The models are largely based on the [ControlNet](https://arxiv.org/abs/2302.05543) architecture, and it's [extension](https://www.yahooinc.com/research/publications/salient-object-aware-background-generation-using-text-guided-diffusion-models):

<img src='/images/portfolio/yahoo-cn.png' width='100%'>