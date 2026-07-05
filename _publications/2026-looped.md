---
title: "Inner Loop Inference for Pretrained Transformers: Unlocking Latent Capabilities Without Training"
authors: "<b>Jonathan Lys</b>, Vincent Gripon, Bastien Pasdeloup, Axel Marmoret, Lukas Mauch, Fabien Cardinaux, Ghouthi Boukli Hacene"
collection: publications
category: conferences
permalink: /publication/2026-looped
excerpt: "This paper proposes inference-time inner looping to extend computation in frozen pretrained Transformers without training."
date: 2026-02-16
venue: "EUSIPCO"
paperurl: 'https://arxiv.org/abs/2602.14759'
bibtexurl: 'https://arxiv.org/bibtex/2602.14759'
citation: 'Lys, et al. (2026). &quot;Inner Loop Inference for Pretrained Transformers: Unlocking Latent Capabilities Without Training.&quot; In 2026 34th European Signal Processing Conference <i>(EUSIPCO)</i>. IEEE.'
---

**Abstract**: Deep Learning architectures, and in particular Transformers, are conventionally viewed as a composition of layers. These layers are actually often obtained as the sum of two contributions: a residual path that copies the input and the output of a Transformer block. As a consequence, the inner representations (i.e. the input of these blocks) can be interpreted as iterative refinement of a propagated latent representation. Under this lens, many works suggest that the inner space is shared across layers, meaning that tokens can be decoded at early stages. Mechanistic interpretability even goes further by conjecturing that some layers act as refinement layers. Following this path, we propose inference-time inner looping, which prolongs refinement in pretrained off-the-shelf language models by repeatedly re-applying a selected block range. Across multiple benchmarks, inner looping yields modest but consistent accuracy improvements. Analyses of the resulting latent trajectories suggest more stable state evolution and continued semantic refinement. Overall, our results suggest that additional refinement can be obtained through simple test-time looping, extending computation in frozen pretrained models.
